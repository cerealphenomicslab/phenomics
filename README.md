# Cereal Phenomics Lab · strona www

Strona zespołu **Cereal Phenomics Lab** (Zakład Fenomiki Zbóż,
Instytut Genetyki Roślin PAN, Poznań). Strona jest dwujęzyczna:
polska wersja pod `/`, angielska pod `/en/`.

Strona jest statyczna (Jekyll) i hostowana za darmo na GitHub Pages.
Treść edytuje się w prostych plikach YAML, bez znajomości HTML.

## Gdzie co zmieniać

| Co | Plik |
|---|---|
| Członkowie zespołu, zdjęcia, e-maile, ORCID, ResearchGate, Google Scholar | `_data/team.yml` + zdjęcia w `assets/img/team/` |
| Publikacje | **automatycznie z ORCID** (patrz niżej); `_data/publications.yml` to lista zapasowa |
| Projekty i granty | `_data/projects.yml` |
| Aktualności | `_data/news.yml` (zdjęcia w `assets/img/news/`) |
| Opis zespołu, obszary badań, metody, wyniki | `_data/content.yml` |
| Dane kontaktowe, adres, linki (Scopus itd.) | `_config.yml` |
| Napisy interfejsu (menu, przyciski) | `_data/i18n.yml`, `_data/nav.yml` |
| Kolory, czcionki, wygląd | `assets/css/main.css` |

Każdy wpis ma wersję `_pl` i `_en`. Po zapisaniu zmian na GitHubie (choćby przez
edycję pliku w przeglądarce) strona przebudowuje się sama w ok. 1–2 minuty.

Listę brakujących treści zawiera plik [BRAKUJACE-INFORMACJE.md](BRAKUJACE-INFORMACJE.md).

## Publikacje z ORCID

Przy każdym wdrożeniu (i dodatkowo co poniedziałek rano) skrypt `tools/fetch_publications.py`
pobiera prace wszystkich osób z polem `orcid` w `_data/team.yml`, usuwa duplikaty po DOI
i uzupełnia autorów, tom i strony z Crossref. Członkowie zespołu są pogrubiani automatycznie.
Aby publikacja pojawiła się na stronie, wystarczy dodać ją do swojego profilu ORCID.
Jeśli ORCID jest niedostępny, strona pokazuje listę z `_data/publications.yml`.
Odświeżenie na żądanie: zakładka **Actions → Deploy site to GitHub Pages → Run workflow**.

## Publikacja na GitHub Pages (jednorazowo)

1. Na GitHubie: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. Każdy push do gałęzi `main` uruchamia workflow `.github/workflows/pages.yml`,
   który buduje stronę i publikuje ją pod adresem `https://<login>.github.io/<repo>/`.
   Adres bazowy ustawia się automatycznie, więc niczego nie trzeba zmieniać w `_config.yml`.

## Podpięcie domeny phenomics.pl (po zakupie)

1. U rejestratora domeny ustaw rekordy DNS:
   - `A` dla `phenomics.pl` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - (opcjonalnie IPv6) `AAAA` → `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
   - `CNAME` dla `www` → `<login>.github.io`
2. Na GitHubie: **Settings → Pages → Custom domain** wpisz `phenomics.pl` i zapisz.
   Po weryfikacji zaznacz **Enforce HTTPS**.
3. W `_config.yml` ustaw `url: "https://phenomics.pl"` (przyda się do linków w podglądach w mediach społecznościowych).

## Uruchomienie lokalne (opcjonalnie)

```bash
bundle install
bundle exec jekyll serve
# http://localhost:4000
```
