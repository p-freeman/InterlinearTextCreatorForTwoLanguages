# Interlinear Text Generator

This Python script allows you to create interlinear text HTML files with optional embedded video and audio players.

## Features

- Create interlinear text HTML files with German and English translations.
- Embed YouTube videos into HTML files.
- Embed audio files into HTML files.
- GUI for easy input and project management.

## Usage

1. Run the script and the GUI window will appear.
2. Fill in the required fields:
   - **Title**: Title of your interlinear text.
   - **Filename/Folder Name**: Name of the folder and HTML file to be created.
   - **German Words**: Enter German text in the left text box.
   - **English Words**: Enter corresponding English translations in the right text box.
   - **Vertical Distance (px)**: Vertical distance between word pairs in pixels.
   - **Font Size**: Font size of the text in pixels.
   - **Link to Video (URL) *optional**: Enter the URL of a YouTube video (optional).
   - **Audio-File available *optional**: Check this box if an audio file is available.
3. Click on **Create Interlinear Text** to generate the HTML file.
4. Optionally, click on **Open Existing Project** to load an existing project for editing.

## Embedding Video

If you enter a YouTube video URL, the script will create a second HTML file with the video embedded at the top.

## Embedding Audio

If you check the "Audio-File available" checkbox, the script will create a third HTML file with an embedded audio player.

## Requirements

- Python 3.x
- tkinter (should be included in most Python installations)
- An internet connection is not required for basic functionality of the script. However, an active internet connection is required when viewing HTML files with embedded YouTube videos to stream the video content. Viewing HTML files offline will result in non-playable videos.

## Notes

- Make sure to provide valid inputs to avoid errors.
- The script assumes that the audio file is in the same folder as the generated HTML files.
- The generated HTML files will be saved in a folder with the specified filename.
