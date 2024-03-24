# Generator Tekstu Interlinearnego

Ten skrypt w języku Python pozwala na tworzenie plików HTML z tekstem interlinearnym z opcjonalnie osadzonym wideo i audio.

## Funkcje

- Tworzenie plików HTML z tekstem interlinearnym zawierającym tłumaczenia na język niemiecki i polski.
- Osadzanie filmów z YouTube w plikach HTML.
- Osadzanie plików audio w plikach HTML.
- GUI dla łatwego wprowadzania danych i zarządzania projektami.

## Użycie

1. Uruchom skrypt, a pojawi się okno GUI.
2. Wypełnij wymagane pola:
   - **Tytuł**: Tytuł twojego tekstu interlinearnego.
   - **Nazwa pliku / Nazwa folderu**: Nazwa folderu i pliku HTML do utworzenia.
   - **Niemieckie Słowa**: Wprowadź tekst niemiecki w lewym polu tekstowym.
   - **Polskie Słowa**: Wprowadź odpowiadające tłumaczenia na polski w prawym polu tekstowym.
   - **Odległość Pionowa (px)**: Odległość pionowa między parami słów w pikselach.
   - **Rozmiar Czcionki**: Rozmiar czcionki tekstu w pikselach.
   - **Link do Wideo (URL) *opcjonalne**: Wprowadź adres URL filmu z YouTube (opcjonalnie).
   - **Dostępny plik audio *opcjonalne**: Zaznacz to pole, jeśli dostępny jest plik audio.
3. Kliknij przycisk **Utwórz Tekst Interlinearny**, aby wygenerować plik HTML.
4. Opcjonalnie kliknij przycisk **Otwórz Istniejący Projekt**, aby wczytać istniejący projekt do edycji.

## Osadzanie Wideo

Jeśli podasz adres URL filmu z YouTube, skrypt utworzy drugi plik HTML z osadzonym filmem na górze.

## Osadzanie Audio

Jeśli zaznaczysz pole "Dostępny plik audio", skrypt utworzy trzeci plik HTML z osadzonym odtwarzaczem audio.

## Wymagania

- Python 3.x
- tkinter (powinno być zawarte w większości instalacji Pythona)
- Aktywne połączenie z internetem nie jest wymagane do podstawowego działania skryptu. Jednakże, aktywne połączenie z internetem jest wymagane podczas przeglądania plików HTML z osadzonymi filmami z YouTube, aby przesyłać treść wideo. Przeglądanie plików HTML offline spowoduje niemożność odtwarzania filmów.

## Notatki

- Upewnij się, że wprowadzasz poprawne dane, aby uniknąć błędów.
- Skrypt zakłada, że plik audio znajduje się w tym samym folderze co wygenerowane pliki HTML.
- Wygenerowane pliki HTML zostaną zapisane w folderze o podanej nazwie pliku.
