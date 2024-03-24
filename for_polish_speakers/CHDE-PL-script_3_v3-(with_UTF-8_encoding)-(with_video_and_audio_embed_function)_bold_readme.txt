# Generator Tekstów Interlinearnych

Ten skrypt w języku Python umożliwia tworzenie plików HTML z tekstem interlinearnym, z opcjonalnie osadzonym wideo i dźwiękiem.

## Funkcje

- Tworzenie plików HTML z tekstem interlinearnym z tłumaczeniami niemieckimi i polskimi.
- Osadzanie filmów z YouTube w plikach HTML.
- Osadzanie plików dźwiękowych w plikach HTML.
- GUI umożliwiające łatwe wprowadzanie danych i zarządzanie projektem.

## Użycie

1. Uruchom skrypt, a pojawi się okno GUI.
2. Wypełnij wymagane pola:
   - **Tytuł**: Tytuł twojego tekstu interlinearnego.
   - **Nazwa pliku/katalogu**: Nazwa katalogu i pliku HTML do utworzenia.
   - **Słowa w Szwajcarskim Niemieckim**: Wpisz tekst niemiecki w lewym polu tekstowym.
   - **Słowa po Polsku**: Wpisz odpowiadające tłumaczenia polskie w prawym polu tekstowym.
   - **Odległość Pionowa (px)**: Odległość pionowa między parach słów w pikselach.
   - **Rozmiar Czcionki**: Rozmiar czcionki tekstu w pikselach.
   - **Link do Wideo (URL) *opcjonalne**: Wprowadź URL filmu z YouTube (opcjonalnie).
   - **Dostępny plik audio *opcjonalne**: Zaznacz to pole, jeśli dostępny jest plik dźwiękowy.
3. Kliknij **Utwórz Tekst Interlinearny**, aby wygenerować plik HTML.
4. Opcjonalnie kliknij **Otwórz Istniejący Projekt**, aby załadować istniejący projekt do edycji.

## Osadzanie Wideo

Jeśli wpiszesz adres URL filmu z YouTube, skrypt utworzy drugi plik HTML z osadzonym na górze filmem.

## Osadzanie Dźwięku

Jeśli zaznaczysz pole "Dostępny plik audio", skrypt utworzy trzeci plik HTML z osadzonym odtwarzaczem audio.

## Wymagania

- Python 3.x
- tkinter (powinien być zawarty w większości instalacji Pythona)
- Połączenie z internetem nie jest wymagane do podstawowego działania skryptu. Jednak aktywne połączenie z internetem jest wymagane podczas przeglądania plików HTML z osadzonymi filmami z YouTube, aby strumieniować zawartość wideo. Przeglądanie plików HTML offline spowoduje niemożność odtwarzania filmów.

## Notatki

- Upewnij się, że wprowadzasz poprawne dane, aby uniknąć błędów.
- Skrypt zakłada, że plik audio znajduje się w tym samym katalogu co wygenerowane pliki HTML.
- Wygenerowane pliki HTML zostaną zapisane w katalogu o podanej nazwie pliku.
