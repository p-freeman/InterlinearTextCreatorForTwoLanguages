# Generator Tekstu Interlinearnego

Ten skrypt w języku Python umożliwia tworzenie plików HTML z tekstem interlinearnym z opcjonalnie osadzonymi odtwarzaczami wideo i audio.

## Funkcje

- Tworzenie plików HTML z tekstem interlinearnym zawierającym polskie i angielskie tłumaczenia.
- Osadzanie filmów z serwisu YouTube w plikach HTML.
- Osadzanie plików dźwiękowych w plikach HTML.
- GUI dla łatwego wprowadzania danych i zarządzania projektami.

## Użycie

1. Uruchom skrypt, aby wyświetlić okno GUI.
2. Wypełnij wymagane pola:
   - **Tytuł**: Tytuł Twojego tekstu interlinearnego.
   - **Nazwa pliku/folderu**: Nazwa folderu i pliku HTML do utworzenia.
   - **Polskie słowa**: Wpisz tekst w języku polskim w lewym polu tekstowym.
   - **Angielskie słowa**: Wpisz odpowiadające tłumaczenia angielskie w prawym polu tekstowym.
   - **Odległość pionowa (px)**: Odległość pomiędzy parami słów w pikselach.
   - **Rozmiar czcionki**: Rozmiar czcionki tekstu w pikselach.
   - **Link do wideo (URL) *opcjonalnie**: Wprowadź adres URL filmu z serwisu YouTube (opcjonalnie).
   - **Dostępny plik dźwiękowy *opcjonalnie**: Zaznacz to pole, jeśli dostępny jest plik dźwiękowy.
3. Kliknij przycisk **Utwórz Interlinearny Tekst**, aby wygenerować plik HTML.
4. Opcjonalnie kliknij przycisk **Otwórz Istniejący Projekt**, aby załadować istniejący projekt do edycji.

## Osadzanie Wideo

Jeśli podasz adres URL filmu z serwisu YouTube, skrypt utworzy drugi plik HTML z osadzonym filmem na górze.

## Osadzanie Audio

Jeśli zaznaczysz pole "Dostępny plik dźwiękowy", skrypt utworzy trzeci plik HTML z osadzonym odtwarzaczem audio.

## Wymagania

- Python 3.x
- tkinter (powinno być zawarte w większości instalacji Pythona)
- Aktywne połączenie z internetem nie jest wymagane do podstawowego działania skryptu. Jednak aktywne połączenie internetowe jest wymagane podczas oglądania plików HTML z osadzonymi filmami z serwisu YouTube, aby odtworzyć treść wideo. Odtwarzanie plików HTML offline spowoduje brak możliwości odtworzenia filmów.

## Uwagi

- Upewnij się, że wprowadzasz poprawne dane, aby uniknąć błędów.
- Skrypt zakłada, że plik dźwiękowy znajduje się w tym samym folderze co wygenerowane pliki HTML.
- Wygenerowane pliki HTML zostaną zapisane w folderze o określonej nazwie pliku.
