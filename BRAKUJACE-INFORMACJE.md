# Czego brakuje na stronie (do uzupełnienia)

Opisy na stronie (strona główna, Badania, opisy podstron, zaproszenie do współpracy,
aktualności) to SZKICE przygotowane przez Claude na podstawie opisu zespołu w serwisie IGR,
publikacji i grantów – do przejrzenia i poprawy. Pozostałe [nawiasy] to brakujące dane.

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
13. Stanowiska: K. Mikołajczak, P. Ogrodowicz, M. Kempa, S. Szczepański (R. Holewińska: „Technik” – ewentualnie doprecyzować).
14. Indywidualne e-maile. Brakujące profile (`_data/team.yml`): ResearchGate – D. Maryniak; Google Scholar – wszyscy poza K. Mikołajczakiem i S. Szczepańskim. Linki RG znalezione automatycznie (A. Kuczyńska, K. Mikołajczak, P. Ogrodowicz, M. Kempa) trzeba sprawdzić.
15. Czy dodać A. Aniołę i R. Trzeciak (są na zdjęciu zespołu w serwisie IGR)?

## Kontakt i inne
16. Pokój albo budynek (`_config.yml`). E-mail zespołu ustawiony: cerealphenomicslab@gmail.com.
17. Opcjonalnie: link do zespołowego profilu w Scopus (`_config.yml` → `links`).
18. Wymogi IGR: logotypy grantodawców. Deklaracja dostępności i polityka prywatności są już na stronie – po uruchomieniu domeny wpisać datę publikacji strony w `deklaracja-dostepnosci.md` i `en/accessibility.md`; warto, żeby IGR potwierdził treść.
19. **CV na stronach osobowych**: każdy uzupełnia swoje pliki `_osoby/<nazwisko>.pl.md` i `.en.md` (zwykły Markdown).
20. Pełny tytuł projektu FLOWroots (EPPN2020 ID 206) – nie udało się go znaleźć w sieci.
