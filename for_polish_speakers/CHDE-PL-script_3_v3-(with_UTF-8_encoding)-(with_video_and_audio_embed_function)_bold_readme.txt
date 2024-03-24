# Generator Tekstów Interlinearnych

Ten skrypt Pythona umożliwia tworzenie plików HTML z tekstem interlinearnym z opcjonalnie osadzonymi odtwarzaczami wideo i dźwięku.

## Funkcje

- Tworzenie plików HTML z tekstem interlinearnym z tłumaczeniami na Swissgerman i Polski.
- Osadzanie filmów z serwisu YouTube w plikach HTML.
- Osadzanie plików dźwiękowych w plikach HTML.
- Graficzny interfejs użytkownika (GUI) dla łatwego wprowadzania danych i zarządzania projektami.

## Użycie

1. Uruchom skrypt, a pojawi się okno GUI.
2. Wypełnij wymagane pola:
   - **Tytuł**: Tytuł Twojego tekstu interlinearnego.
   - **Nazwa pliku/Nazwa folderu**: Nazwa folderu i pliku HTML, które mają być utworzone.
   - **Swissgerman Words**: Wprowadź tekst w języku Swissgerman w lewym polu tekstowym.
   - **Polish Words**: Wprowadź odpowiadające tłumaczenia po polsku w prawym polu tekstowym.
   - **Odległość pionowa (px)**: Odległość pionowa między parach słów w pikselach.
   - **Rozmiar czcionki**: Rozmiar czcionki tekstu w pikselach.
   - **Link do filmu (URL) *opcjonalnie**: Wprowadź adres URL filmu z YouTube (opcjonalnie).
   - **Dostępny plik audio *opcjonalnie**: Zaznacz to pole, jeśli dostępny jest plik audio.
3. Kliknij przycisk **Utwórz Tekst Interlinearny**, aby wygenerować plik HTML.
4. Opcjonalnie kliknij przycisk **Otwórz Istniejący Projekt**, aby załadować istniejący projekt do edycji.

## Osadzanie Wideo

Jeśli podasz adres URL filmu z serwisu YouTube, skrypt utworzy drugi plik HTML z osadzonym filmem na górze.

## Osadzanie Audio

Jeśli zaznaczysz pole wyboru "Dostępny plik audio", skrypt utworzy trzeci plik HTML z osadzonym odtwarzaczem audio.

## Wymagania

- Python 3.x
- tkinter (powinien być zawarty w większości instalacji Pythona)
- Połączenie internetowe nie jest wymagane do podstawowego działania skryptu. Jednak aktywne połączenie internetowe jest wymagane podczas przeglądania plików HTML z osadzonymi filmami z YouTube, aby strumieniować treści wideo. Przeglądanie plików HTML offline spowoduje niemożność odtwarzania filmów.

## Uwagi

- Upewnij się, że podajesz poprawne dane, aby uniknąć błędów.
- Skrypt zakłada, że plik audio znajduje się w tym samym folderze co wygenerowane pliki HTML.
- Wygenerowane pliki HTML zostaną zapisane w folderze o określonej nazwie pliku.

