# Interlinearer Textgenerator

Dieses Python-Skript ermöglicht es dir, interlineare Text-HTML-Dateien mit optional eingebetteten Video- und Audioplayern zu erstellen.

## Funktionen

- Erstellen von interlinearen Text-HTML-Dateien mit französischen und deutschen Übersetzungen.
- Einbetten von YouTube-Videos in HTML-Dateien.
- Einbetten von Audiodateien in HTML-Dateien.
- GUI für eine einfache Eingabe und Projektverwaltung.

## Verwendung

1. Starte das Skript und das GUI-Fenster wird angezeigt.
2. Fülle die erforderlichen Felder aus:
   - **Titel**: Titel deines interlinearen Textes.
   - **Dateiname/Ordnername**: Name des Ordners und der HTML-Datei, die erstellt werden soll.
   - **Französische Wörter**: Gib den französischen Text im linken Textfeld ein.
   - **Deutsche Wörter**: Gib die entsprechenden deutschen Übersetzungen im rechten Textfeld ein.
   - **Vertikaler Abstand (px)**: Vertikaler Abstand zwischen Wortpaaren in Pixeln.
   - **Schriftgröße**: Schriftgröße des Textes in Pixeln.
   - **Link zum Video (URL) *optional**: Gib die URL eines YouTube-Videos ein (optional).
   - **Audio-Datei verfügbar *optional**: Aktiviere dieses Kontrollkästchen, wenn eine Audiodatei verfügbar ist.
3. Klicke auf **Interlinearen Text erstellen**, um die HTML-Datei zu generieren.
4. Klicke optional auf **Bestehendes Projekt öffnen**, um ein vorhandenes Projekt zum Bearbeiten zu laden.

## Einbetten von Video

Wenn du eine YouTube-Video-URL eingibst, erstellt das Skript eine zweite HTML-Datei mit dem Video am Anfang eingebettet.

## Einbetten von Audio

Wenn du das Kontrollkästchen "Audio-Datei verfügbar" aktivierst, erstellt das Skript eine dritte HTML-Datei mit einem eingebetteten Audioplayer.

## Anforderungen

- Python 3.x
- tkinter (sollte in den meisten Python-Installationen enthalten sein)
- Eine Internetverbindung ist für die grundlegende Funktionalität des Skripts nicht erforderlich. Jedoch ist eine aktive Internetverbindung erforderlich, um HTML-Dateien mit eingebetteten YouTube-Videos anzuzeigen, um den Videoinhalt zu streamen. Das Anzeigen von HTML-Dateien offline führt zu nicht abspielbaren Videos.

## Hinweise

- Stelle sicher, dass du gültige Eingaben machst, um Fehler zu vermeiden.
- Das Skript geht davon aus, dass die Audiodatei sich im gleichen Ordner wie die generierten HTML-Dateien befindet.
- Die generierten HTML-Dateien werden in einem Ordner mit dem angegebenen Dateinamen gespeichert.
