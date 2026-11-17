# Czego brakuje na stronie (do uzupełnienia)

Teksty, które nie pochodzą ze strony IGR, są na stronie zastąpione placeholderami
w nawiasach kwadratowych, np. `[opis zespołu – akapit 1]`. Wystarczy je podmienić
we wskazanych plikach. Na stronie zostały tylko dane źródłowe: nazwiska, stopnie,
numery i kierownicy grantów, daty, tytuły publikacji i projektów oraz dane kontaktowe IGR.

## Teksty (placeholdery)
1. **Strona główna i „Badania”** (`_data/content.yml`, PL i EN): hasło główne, opis zespołu (2 akapity), 6 obszarów badawczych, metody, najważniejsze wyniki, słowa kluczowe.
2. **Opisy podstron** pod nagłówkami (pole `lead:` w plikach `badania.html`, `zespol.html` itd. oraz `en/*.html`).
3. **Angielska nazwa**: „Cereal Phenomics Team” (ustalone) (`_data/i18n.yml`, `_config.yml`).
4. **Zaproszenie do współpracy i tekst w stopce** (`_data/i18n.yml` → `collab_title`, `collab_text`, `footer_note`).
5. **Aktualności**: 3 puste wpisy (`_data/news.yml`).
6. **Polskie tytuły wszystkich projektów** (`_data/projects.yml` → `title_pl`).
7. **Pełne angielskie tytuły 7 projektów** (OPUS 27, OPUS 21 – Ogrodowicz, OPUS 18, SONATA 12 – Ogrodowicz, OPUS 9, FLOWroots, HOR zad. 88) (`title_en`).
8. **Status projektów NCN** (w realizacji / zakończony) i okresy realizacji (`status`, `period`).
9. Publikacje pobierają się teraz automatycznie z ORCID. Trzeba tylko zadbać, żeby profile ORCID były kompletne.

## Zdjęcia i grafika
10. Lepsza wersja logo: SVG albo PNG min. 1000 px (`assets/img/logo.png`, `assets/img/emblem.png`).
11. Portrety członków zespołu: 4:5, min. 600×750 px (`assets/img/team/`, pole `photo` w `_data/team.yml`).
12. Zdjęcia pola, laboratorium i fenotypowania na stronę główną i do „Badań”.

## Zespół (`_data/team.yml`)
13. Stanowiska: K. Mikołajczak, P. Ogrodowicz, M. Kempa, S. Szczepański, R. Holewińska.
14. Indywidualne e-maile. Brakujące profile (`_data/team.yml`): ResearchGate – D. Maryniak; Google Scholar – wszyscy poza K. Mikołajczakiem i S. Szczepańskim. Linki RG znalezione automatycznie (A. Kuczyńska, K. Mikołajczak, P. Ogrodowicz, M. Kempa) trzeba sprawdzić.
15. Czy dodać A. Aniołę i R. Trzeciak (są na zdjęciu zespołu w serwisie IGR)?

## Kontakt i inne
16. E-mail zespołu lub kierownika (teraz jest `office@igr.poznan.pl`), pokój albo budynek (`_config.yml`).
17. Opcjonalnie: link do zespołowego profilu w Scopus (`_config.yml` → `links`).
18. Wymogi IGR: deklaracja dostępności, polityka prywatności, logotypy instytutu i grantodawców.
