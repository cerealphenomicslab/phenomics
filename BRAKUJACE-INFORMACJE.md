# Czego brakuje na stronie (do uzupełnienia)

Lista rzeczy, których nie było na stronie IGR albo które wymagają potwierdzenia.
Plik, w którym to się zmienia, podano w nawiasie.

## Najważniejsze
1. **Lepsza wersja logo**: najlepiej SVG albo PNG min. 1000 px, w wersji na jasne i ciemne tło (`assets/img/logo.png`, `assets/img/emblem.png`).
2. **Zdjęcia portretowe członków zespołu**: najlepiej w proporcji 4:5, min. 600×750 px (`assets/img/team/`, pole `photo` w `_data/team.yml`). Na razie są inicjały.
3. **Zdjęcia do strony głównej i „Badania”**: pole, szklarnia, laboratorium, fenotypowanie korzeni. Na razie jest grafika z kłosem i ramka „zdjęcie wkrótce”. Zdjęcie zespołu z serwisu IGR można wykorzystać po potwierdzeniu praw do niego.
4. **Prawdziwe aktualności**: 3 obecne wpisy są **przykładowe** (oznaczone czerwoną etykietą „przykład”) (`_data/news.yml`).
5. **Polska nazwa zespołu**: przyjęłem „Zespół Fenotypowania i Genotypowania Zbóż”; strona IGR po angielsku podaje „Cereal Phenomics Team” (`_data/i18n.yml`).

## Zespół (`_data/team.yml`)
6. Stanowiska (adiunkt, profesor instytutu, specjalista itd.) dla: K. Mikołajczak, P. Ogrodowicz, M. Kempa, S. Szczepański, R. Holewińska.
7. Indywidualne adresy e-mail i numery ORCID (opcjonalnie: krótkie bio, zainteresowania).
8. Czy na stronie mają być też **A. Anioła** i **R. Trzeciak** (są na podpisie zdjęcia zespołu w IGR, ale nie ma ich w składzie zespołu)?
9. Byli członkowie / absolwenci: czy dodać taką sekcję?

## Kontakt (`_config.yml`, sekcja `contact`)
10. Adres e-mail zespołu lub kierownika (teraz jest ogólny `office@igr.poznan.pl`) oraz telefon do zespołu, numer pokoju lub budynku.

## Publikacje (`_data/publications.yml`)
11. Na stronie IGR jest 14 publikacji (2019–2023). Potrzebne nowsze (2024–2026) albo decyzja, że pokazujemy tylko wybrane.
12. Link do pełnego dorobku (Scopus / Google Scholar / ORCID) (`_config.yml` → `links`).
13. Tytuły oznaczone `verify: true` (5 pozycji) wpisałem częściowo z pamięci; trzeba je porównać z oryginałem.

## Projekty (`_data/projects.yml`)
14. **Polskie tytuły projektów to moje tłumaczenia robocze.** Trzeba je podmienić na oficjalne tytuły z umów lub bazy NCN.
15. Kilka angielskich tytułów (OPUS 27, OPUS 21 Ogrodowicz, OPUS 18, SONATA 12 Ogrodowicz, OPUS 9, FLOWroots, HOR zad. 88) jest skróconych; trzeba wpisać pełne brzmienie.
16. Okresy realizacji projektów NCN i ich status (w realizacji / zakończony); dla obu OPUS 21 status jest pusty.
17. Ewentualne inne projekty, współpraca, aparatura, partnerzy.

## Domena i formalności
18. Domena phenomics.pl: instrukcja podpięcia jest w `README.md`.
19. Czy IGR PAN wymaga na stronie: deklaracji dostępności, polityki prywatności/cookies, logotypów instytutu i grantodawców (NCN, MRiRW, UE)?
