#!/usr/bin/env python3
"""Pobiera publikacje członków zespołu z ORCID (i uzupełnia dane z Crossref).

Czyta numery ORCID z _data/team.yml i zapisuje _data/publications_auto.json.
Strona używa tego pliku zamiast _data/publications.yml. Jeśli pobieranie się nie
uda, plik nie jest nadpisywany i strona pokazuje dotychczasową listę.

Uruchamiane automatycznie przez GitHub Actions przed każdym budowaniem strony.
Używa wyłącznie biblioteki standardowej Pythona.
"""
import json
import os
import re
import sys
import html
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEAM = os.path.join(ROOT, "_data", "team.yml")
OUT = os.path.join(ROOT, "_data", "publications_auto.json")
UA = "phenomics-site-builder/1.0 (static website build)"
SKIP_TYPES = {"data-set", "other", "lecture-speech", "conference-poster",
              "conference-abstract", "dissertation-thesis", "supervised-student-publication",
              "research-technique", "physical-object", "software", "website", "patent"}
MIN_YEAR = int(os.environ.get("PUB_MIN_YEAR", "0"))


def get_json(url, accept="application/json"):
    req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


import unicodedata


def ascii_fold(text):
    text = (text or "").replace("ł", "l").replace("Ł", "L")
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()


def team_blocks():
    """Wpisy z _data/team.yml jako słowniki (prosty parser, bez PyYAML)."""
    text = open(TEAM, encoding="utf-8").read()
    out = []
    for block in re.split(r"^- ", text, flags=re.M)[1:]:
        d = {}
        for line in ("  " + block).splitlines():
            m = re.match(r"^\s{2}(\w+):\s*(.*?)\s*(#.*)?$", line)
            if m:
                d[m.group(1)] = m.group(2).strip('"')
        out.append(d)
    return out


def team_members():
    """(nazwisko, pierwsza litera imienia) członków zespołu, bez polskich znaków.
    Uwzględnia też inne nazwiska z pola other_names (np. panieńskie)."""
    out = set()
    for d in team_blocks():
        names = [d.get("name", "")]
        names += [n.strip() for n in d.get("other_names", "").strip("[]").split(",") if n.strip()]
        for n in names:
            parts = n.split()
            if len(parts) >= 2:
                out.add((ascii_fold(parts[-1]), ascii_fold(parts[0])[:1]))
    return out


def joined_dates():
    """ORCID -> (rok, miesiąc) dołączenia do zespołu (pole joined: RRRR-MM)."""
    out = {}
    for d in team_blocks():
        m = re.match(r"(\d{4})(?:-(\d{1,2}))?", d.get("joined", ""))
        if d.get("orcid") and m:
            out[d["orcid"]] = (int(m.group(1)), int(m.group(2) or 1))
    return out


def mark_team(authors, members):
    """Zwraca listę autorów w HTML z pogrubionymi członkami zespołu."""
    out = []
    for a in authors:
        fam, ini = a
        label = html.escape(f"{fam} {ini}".strip())
        if (ascii_fold(fam), ascii_fold(ini)[:1]) in members:
            label = f"<strong>{label}</strong>"
        out.append(label)
    return ", ".join(out)


def orcids():
    ids = re.findall(r'orcid:\s*"?(\d{4}-\d{4}-\d{4}-\d{3}[\dX])"?', open(TEAM, encoding="utf-8").read())
    return list(dict.fromkeys(ids))


def val(d, *path):
    for k in path:
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


def clean(text):
    text = html.unescape(html.unescape(text or ""))
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()


SKIP_TITLE = re.compile(r"^(corrigendum|erratum|correction|retraction)\b", re.I)


def tkey(title):
    return re.sub(r"[^a-z0-9]", "", ascii_fold(title))


def norm_doi(doi):
    doi = (doi or "").strip().lower()
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", doi)
    return doi or None


def works_for(orcid):
    data = get_json(f"https://pub.orcid.org/v3.0/{orcid}/works")
    out = []
    for g in data.get("group", []):
        summaries = g.get("work-summary") or []
        if not summaries:
            continue
        w = summaries[0]
        if w.get("type") in SKIP_TYPES:
            continue
        doi = None
        for eid in val(w, "external-ids", "external-id") or []:
            if eid.get("external-id-type") == "doi":
                doi = norm_doi(eid.get("external-id-value"))
                break
        year = val(w, "publication-date", "year", "value")
        month = val(w, "publication-date", "month", "value")
        out.append({
            "title": clean(val(w, "title", "title", "value")),
            "journal": clean(val(w, "journal-title", "value")),
            "year": int(year) if year and year.isdigit() else None,
            "month": int(month) if month and month.isdigit() else 0,
            "doi": doi,
            "url": val(w, "url", "value"),
            "orcid": orcid,
        })
    return out


def initials(given):
    parts = re.split(r"[\s.]+", given or "")
    out = []
    for p in parts:
        if not p:
            continue
        out.append("-".join(x[0] + "." for x in p.split("-") if x))
    return "".join(out)


UP = "A-ZĄĆĘŁŃÓŚŹŻÄÖÜÉÈÁ"
NAME_IN_TEXT = re.compile(rf"\b([{UP}][{UP}'’-]+(?:[ -][{UP}][{UP}'’-]+)?),?\s+((?:[{UP}]\.\s?-?)+)")


def nice_case(name):
    """RUTKOWSKI -> Rutkowski, ZWIJACZ-KOZICA -> Zwijacz-Kozica (tylko gdy całość wielkimi literami)."""
    if name.upper() != name:
        return name
    return "-".join(" ".join(w.capitalize() for w in part.split(" ")) for part in name.split("-"))


def looks_broken(text):
    return bool(re.search(r"\d|,|@", text or "")) or len((text or "").split()) > 4


def clean_authors(raw):
    """Zamienia listę autorów z Crossref na (nazwisko, inicjały).

    Niektóre wydawnictwa wpisują do Crossref afiliacje w polach autorów
    („Museum and Institute of Zoology…, RUTKOWSKI R., …”). Wtedy wyciągamy
    z tekstu same wzorce NAZWISKO I., a jeśli się nie da – pomijamy autorów.
    """
    out, broken = [], False
    for a in raw:
        fam, giv, name = a.get("family") or "", a.get("given") or "", a.get("name") or ""
        if fam and not looks_broken(fam) and not looks_broken(giv):
            out.append((nice_case(fam.strip()), initials(giv)))
        elif name and not looks_broken(name):
            out.append((name.strip(), ""))
        else:
            broken = True
            print(f"  [autorzy z błędem w Crossref] {json.dumps(a, ensure_ascii=False)[:300]}", file=sys.stderr)
            for text in (giv, fam, name):
                for f, ini in NAME_IN_TEXT.findall(text):
                    out.append((nice_case(f.strip()), ini.replace(" ", "")))
    if broken:
        seen, uniq = set(), []
        for f, i in out:
            if (f, i) not in seen:
                seen.add((f, i)); uniq.append((f, i))
        out = uniq
    return out


def crossref(doi):
    import time
    m = None
    for attempt in range(4):
        try:
            m = get_json("https://api.crossref.org/works/" + urllib.request.quote(doi))["message"]
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                break
            time.sleep(2 * (attempt + 1))
        except Exception:
            time.sleep(2 * (attempt + 1))
    if m is None:
        print(f"  Crossref: brak danych dla {doi}", file=sys.stderr)
        return None
    authors = clean_authors(m.get("author", []))
    vol, iss = m.get("volume"), m.get("issue")
    pages = (m.get("page") or m.get("article-number") or "").replace("-", "–")
    details = ""
    if vol:
        details = vol + (f"({iss})" if iss else "")
    if pages:
        details = f"{details}: {pages}" if details else pages
    dp = (m.get("published-print") or m.get("published-online") or m.get("issued") or {}).get("date-parts", [[None]])
    return {
        "title": clean((m.get("title") or [""])[0]),
        "journal": clean((m.get("container-title") or [""])[0]),
        "authors": authors,
        "details": details,
        "year": dp[0][0] if dp and dp[0] else None,
        "month": dp[0][1] if dp and dp[0] and len(dp[0]) > 1 else 0,
    }


def main():
    ids = orcids()
    if not ids:
        print("Brak numerów ORCID w _data/team.yml – pomijam.")
        return 0
    all_works, failed = [], []
    for oid in ids:
        try:
            ws = works_for(oid)
            print(f"ORCID {oid}: {len(ws)} prac")
            all_works.extend(ws)
        except Exception as e:
            print(f"ORCID {oid}: błąd {e}", file=sys.stderr)
            failed.append(oid)
    if not all_works:
        print("Nie pobrano żadnych publikacji – zostawiam poprzednią listę.", file=sys.stderr)
        return 0

    # deduplikacja: ten sam DOI albo bardzo podobny tytuł (rok ±1);
    # wersja z DOI ma pierwszeństwo
    from difflib import SequenceMatcher
    all_works.sort(key=lambda w: w["doi"] is None)
    kept = []
    for w in all_works:
        if not w["title"] or SKIP_TITLE.match(w["title"]):
            continue
        k = tkey(w["title"])
        dup = None
        for m in kept:
            if w["doi"] and m["doi"] == w["doi"]:
                dup = m
                break
            if w["doi"] and m["doi"]:
                continue  # dwa różne DOI = dwie różne prace
            short, long_ = sorted((m["_k"], k), key=len)
            similar = (short == long_
                       or (len(short) > 40 and long_.startswith(short))
                       or SequenceMatcher(None, m["_k"], k).ratio() > 0.88)
            if similar and abs((m["year"] or 0) - (w["year"] or 0)) <= 1:
                dup = m
                break
        if dup:
            dup["orcids"].add(w["orcid"])
            continue
        w["orcids"] = {w["orcid"]}
        w["_k"] = k
        kept.append(w)
    merged = {i: w for i, w in enumerate(kept)}

    dois = [w["doi"] for w in merged.values() if w["doi"]]
    with ThreadPoolExecutor(max_workers=3) as ex:
        meta = dict(zip(dois, ex.map(crossref, dois)))

    members = team_members()
    joined = joined_dates()
    pubs = []
    for w in merged.values():
        cr = meta.get(w["doi"]) if w["doi"] else None
        authors_html = mark_team((cr or {}).get("authors") or [], members)
        n_team = max(authors_html.count("<strong>"), len(w["orcids"]))
        item = {
            # cpl = co najmniej 2 członków zespołu wśród autorów; other = 1
            "group": "cpl" if n_team >= 2 else "other",
            "title": (cr or {}).get("title") or w["title"],
            "authors_html": authors_html,
            "journal": (cr or {}).get("journal") or w["journal"] or "",
            "details": (cr or {}).get("details") or "",
            "year": (cr or {}).get("year") or w["year"],
            "doi": w["doi"],
            "url": None if w["doi"] else w["url"],
            "team_orcids": sorted(w["orcids"]),
        }
        if SKIP_TITLE.match(item["title"] or ""):
            continue
        if not item["title"] or not item["year"] or item["year"] < MIN_YEAR:
            continue
        # praca widoczna tylko w ORCID osób, które dołączyły do zespołu później -> pomijamy
        month = (cr or {}).get("month") or w.get("month") or 0
        if all(o in joined and (item["year"], month) < joined[o] for o in w["orcids"]):
            print(f"  [przed dołączeniem do zespołu] {item['year']} | {item['title'][:80]}")
            continue
        pubs.append(item)

    pubs.sort(key=lambda p: (-p["year"], p["title"].lower()))
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(pubs, f, ensure_ascii=False, indent=1)
    for p in pubs:
        print(f"  {p['group']:5} {p['authors_html'].count('<strong>')}/{len(p['team_orcids'])} | {p['year']} | {p['journal'][:40]:40} | {p['doi'] or '---'} | {p['title'][:90]} | {re.sub('<[^>]+>', '', p['authors_html'])[:60]}")
    print(f"Zapisano {len(pubs)} publikacji do {os.path.relpath(OUT, ROOT)}"
          + (f" (nieudane ORCID: {', '.join(failed)})" if failed else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
