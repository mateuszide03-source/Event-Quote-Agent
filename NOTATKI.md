# Notatki z nauki

## Status etapów

Etap 1 – ukończony 09.11
Etap 2 – ukończony 11.11

## Uzgodnione uproszczenia (opóźnienie ok. 1 dzień)

- Cennik: 6–8 pozycji.
- Odległości: 4–5 miast w `distances.csv`.
- Oferta: prosty plik `.md` z jedną tabelą kosztów.

## Etap 1 – czego się nauczyłem

- Terminal służy do wydawania poleceń. Komendy: `cd` (change directory, czyli zmień folder), `pwd`, `python`, `git`, `source`. Flagi to dodatkowe opcje komend, np. `-m` i `-u`.
- `.venv` to folder, w którym przechowywane są Python i biblioteki tylko dla tego projektu, żeby nie mieszały się z innymi projektami.
- Biblioteki to zbiór kodu, który ktoś już wcześniej napisał, np. `python-dotenv`, który odczytuje klucz API. Do uruchomienia jednych bibliotek potrzebne są inne, które instalują się same.
- `requirements.txt` to lista bibliotek z konkretnym numerem wersji.
- `.gitignore` to plik, który wysyłamy do gita. Informuje on, jakich plików nie można wysyłać na GitHuba.
- Klucz API to unikalny klucz dostępu do serwera, np. Claude'a. Wywołanie API to zapytanie wysłane przez internet razem z kluczem.
- `add` dodaje pliki do listy, `commit` zapisuje ich wersję w historii na moim komputerze, a `push` wysyła je na GitHuba.

## Etap 2 – czego się nauczyłem

- **JSON i słownik.** Model odsyła JSON jako tekst. `json.loads` zamienia tekst na słownik, na którym Python może pracować. `json.dumps` robi odwrotnie: zamienia słownik z powrotem na tekst, a `indent=2` układa go czytelnie w linijkach z wcięciami.
- **`try/except` łapie błędy.** Gdy model zwróci zepsuty JSON, program się nie wywala, tylko wypisuje komunikat, a moja funkcja zwraca `None`. (`null` to „nic” w JSON-ie, `None` to „nic” w Pythonie.)
- **`def` tworzy funkcję**, czyli nazwany zestaw instrukcji. Wykonuje się wtedy, gdy ją wywołam po nazwie. Parametr to dana wejściowa, a `return` zwraca wynik.
- **Traceback** to raport o błędzie. Na samym dole jest rodzaj błędu, a czytając w górę, widać, w której linijce mojego kodu wystąpił. Linijki z `.venv` to kod bibliotek i mogę je pominąć.
- **Pętla `for ... in`** wykonuje się raz dla każdego elementu listy. **`if`** to nie pętla, tylko warunek: wykonuje kod raz, jeśli warunek jest spełniony.
- **`.append`** dopisuje element na koniec listy. **`.get`** bezpiecznie odczytuje wartość ze słownika: gdy etykiety nie ma, zwraca `None` zamiast błędu.
- **Model nie może zgadywać.** Dane takie jak „next spring” wyglądają jak data, ale jej nie doprecyzowują i wprowadzają w błąd. Doprecyzowałem prompt, żeby niejasne daty traktował jako brak (`null`).
