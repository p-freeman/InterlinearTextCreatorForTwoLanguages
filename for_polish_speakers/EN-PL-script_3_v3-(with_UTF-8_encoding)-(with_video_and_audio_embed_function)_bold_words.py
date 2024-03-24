import tkinter as tk
from tkinter import filedialog
import os
import json

class LineNumbers(tk.Text):
    """
    Custom Text widget for displaying line numbers.
    """
    def __init__(self, master, *args, **kwargs):
        tk.Text.__init__(self, master, *args, **kwargs)
        self.config(state="disabled")

    def generate_line_numbers(self, text_widget):
        """
        Generate line numbers based on the content of the text widget.
        """
        self.config(state="normal")
        self.delete("1.0", tk.END)
        line_count = int(text_widget.index("end-1c").split('.')[0])  # Get the number of lines as an integer
        for line_num in range(1, line_count + 1):
            self.insert(tk.END, f"{line_num}\n")
        self.config(state="disabled")


class InterlinearApp:
    """
    Main application class for generating interlinear texts.
    """
    def __init__(self, root):
        # Initialize the GUI window
        self.root = root
        self.root.title("Generator Tekstu Interlinearnego")
        
        # Create a frame to organize GUI elements
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        
        # Labels and entry fields for title, filename, text inputs, and video link
        self.label_title = tk.Label(self.frame, text="Tytuł:")
        self.label_title.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_title = tk.Entry(self.frame, width=30)
        self.entry_title.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        self.label_filename = tk.Label(self.frame, text="Nazwa pliku/Folder:")
        self.label_filename.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_filename = tk.Entry(self.frame, width=30)
        self.entry_filename.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        self.label_polish = tk.Label(self.frame, text="Słowa polskie:")
        self.label_polish.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_polish = tk.Text(self.frame, height=10, width=30)
        self.entry_polish.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        self.entry_polish.bind("<Button-1>", self.scroll_english_to_same_line)
        
        self.label_english = tk.Label(self.frame, text="Słowa angielskie:")
        self.label_english.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.entry_english = tk.Text(self.frame, height=10, width=30)
        self.entry_english.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        
        self.label_vertical_distance = tk.Label(self.frame, text="Odległość pionowa (px):")
        self.label_vertical_distance.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_vertical_distance = tk.Entry(self.frame, width=10)
        self.entry_vertical_distance.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.entry_vertical_distance.insert(0, "10")  # Pre-load with default value
        
        self.label_font_size = tk.Label(self.frame, text="Rozmiar czcionki:")
        self.label_font_size.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.entry_font_size = tk.Entry(self.frame, width=10)
        self.entry_font_size.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.entry_font_size.insert(0, "12")  # Pre-load with default value
        
        self.label_video_link = tk.Label(self.frame, text="Link do wideo (URL) *opcjonalnie:")
        self.label_video_link.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.entry_video_link = tk.Entry(self.frame, width=30)
        self.entry_video_link.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        
        self.audio_checkbox_var = tk.BooleanVar()  # Variable to hold the state of the audio checkbox
        self.audio_checkbox = tk.Checkbutton(self.frame, text="Dostępny plik dźwiękowy *opcjonalnie", variable=self.audio_checkbox_var)
        self.audio_checkbox.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="w")
        
        self.create_button = tk.Button(self.frame, text="Utwórz Interlinearny Tekst", command=self.create_interlinear)
        self.create_button.grid(row=8, column=0, padx=5, pady=5)
        
        self.open_button = tk.Button(self.frame, text="Otwórz Istniejący Projekt", command=self.open_project)
        self.open_button.grid(row=8, column=1, padx=5, pady=5)
        
        self.interlinear_data = {}  
        self.current_project_path = None  
    
    def create_interlinear(self):
        if not (self.entry_title.get() or self.entry_filename.get() or self.entry_polish.get("1.0", tk.END).strip() or self.entry_english.get("1.0", tk.END).strip() or self.entry_vertical_distance.get() or self.entry_font_size.get()):
            return  
        
        title = self.entry_title.get().strip()
        filename = self.entry_filename.get().strip()
        polish_text = self.entry_polish.get("1.0", tk.END).strip()
        english_text = self.entry_english.get("1.0", tk.END).strip()
        vertical_distance = int(self.entry_vertical_distance.get())  
        font_size = int(self.entry_font_size.get())  
        video_link = self.entry_video_link.get().strip()  # Get video link
        audio_available = self.audio_checkbox_var.get()  # Check if audio available checkbox is checked
        
        folder_path = os.path.join(os.getcwd(), f"{filename}")
        os.makedirs(folder_path, exist_ok=True)
        
        polish_text_path = os.path.join(folder_path, "polish_text.txt")
        with open(polish_text_path, "w", encoding="utf-8") as file:
            file.write(polish_text.strip('\n'))
        
        english_text_path = os.path.join(folder_path, "english_text.txt")
        with open(english_text_path, "w", encoding="utf-8") as file:
            file.write(english_text.strip('\n'))
        
                with open(polish_text_path, "r", encoding="utf-8") as file:
            polish_lines = file.readlines()
        
        with open(english_text_path, "r", encoding="utf-8") as file:
            english_lines = file.readlines()
        
        interlinear_html = "<!DOCTYPE html>\n<html>\n<head>\n<meta charset='UTF-8'>\n"  
        interlinear_html += f"<title>{title}</title>\n"  
        interlinear_html += "<style>\n"  
        interlinear_html += f"body {{ font-family: sans-serif; }}\n"  
        interlinear_html += f".word_package {{ display: inline-block; margin-right: 20px; margin-bottom: {vertical_distance}px; }}\n"  
        interlinear_html += ".polish_word {{ font-weight: bold; }}\n"  
        interlinear_html += ".english_word {{ margin-top: 5px; }}\n"  
        interlinear_html += "</style>\n</head>\n<body style='font-size:" + str(font_size) + "px;'>\n"  
        
        interlinear_html += f"<h1>{title}</h1>\n"  
        
        for polish_line, english_line in zip(polish_lines, english_lines):
            if polish_line.strip() == "":
                interlinear_html += "<br>\n"
                continue
            
            interlinear_html += "<div class='word_package'>\n"  
            interlinear_html += f"<div class='polish_word'><b>{polish_line.strip()}</b></div>\n"  
            interlinear_html += f"<div class='english_word'>{english_line.strip()}</div>\n"  
            interlinear_html += "</div>\n"  
        
        interlinear_html += "</body>\n</html>"
        
        file_path = os.path.join(folder_path, f"{filename}.html")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(interlinear_html)
        
        json_data = {
            "title": title,
            "filename": filename,
            "polish_text": polish_text,
            "english_text": english_text,
            "vertical_distance": vertical_distance,
            "font_size": font_size,
            "video_link": video_link,  
            "audio_available": audio_available  # Include audio availability in JSON data
        }
        json_file_path = os.path.join(folder_path, f"{filename}.json")
        with open(json_file_path, "w") as json_file:
            json.dump(json_data, json_file)
        
        print("Interlinear text saved to:", file_path)
        print("Polish text saved to:", polish_text_path)
        print("English text saved to:", english_text_path)
        
        if video_link:
            self.create_interlinear_with_video(title, filename, folder_path, interlinear_html, video_link)
        
        if audio_available:
            self.create_interlinear_with_audio(title, filename, folder_path, interlinear_html)

    def create_interlinear_with_video(self, title, filename, folder_path, interlinear_html, video_link):
        video_embed_code = f"<iframe width='560' height='315' src='{video_link.replace('watch?v=', 'embed/')}' title='YouTube Video Player' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share' allowfullscreen></iframe>"
        
        video_interlinear_html = f"<!DOCTYPE html>\n<html>\n<head>\n<meta charset='UTF-8'>\n<title>{title} with Video</title>\n</head>\n<body>\n{video_embed_code}\n{interlinear_html}</body>\n</html>"
        
        video_file_path = os.path.join(folder_path, f"{filename}_with_video.html")
        with open(video_file_path, "w", encoding="utf-8") as file:
            file.write(video_interlinear_html)
        
        print("Interlinear text with embedded video saved to:", video_file_path)
        
    def create_interlinear_with_audio(self, title, filename, folder_path, interlinear_html):
        audio_embed_code = f"<audio controls='' id='audio-control' type='audio/mpeg'><source src='{filename}.mp3' type='audio/mpeg'></audio>"
        
        audio_interlinear_html = f"<!DOCTYPE html>\n<html>\n<head>\n<meta charset='UTF-8'>\n<title>{title} with Audio</title>\n</head>\n<body>\n{audio_embed_code}\n{interlinear_html}</body>\n</html>"
        
        audio_file_path = os.path.join(folder_path, f"{filename}_with_audio.html")
        with open(audio_file_path, "w", encoding="utf-8") as file:
            file.write(audio_interlinear_html)
        
        print("Interlinear text with embedded audio saved to:", audio_file_path)

    def open_project(self):
        self.entry_title.delete(0, tk.END)
        self.entry_filename.delete(0, tk.END)
        self.entry_polish.delete("1.0", tk.END)
        self.entry_english.delete("1.0", tk.END)
        self.entry_vertical_distance.delete(0, tk.END)
        self.entry_font_size.delete(0, tk.END)
        self.entry_video_link.delete(0, tk.END)
        
        project_folder = filedialog.askdirectory(title="Select Project Folder")
        if not project_folder:
            return  
        
        json_file_path = os.path.join(project_folder, os.path.basename(project_folder) + ".json")
        if os.path.exists(json_file_path):
            with open(json_file_path, "r") as json_file:
                project_data = json.load(json_file)
            
            self.entry_title.insert(0, project_data.get("title", ""))
            self.entry_filename.insert(0, project_data.get("filename", ""))
            self.entry_polish.insert("1.0", project_data.get("polish_text", ""))
            self.entry_english.insert("1.0", project_data.get("english_text", ""))
            self.entry_vertical_distance.insert(0, str(project_data.get("vertical_distance", 10)))
            self.entry_font_size.insert(0, str(project_data.get("font_size", 12)))
            self.entry_video_link.insert(0, project_data.get("video_link", ""))
            
            if project_data.get("audio_available"):
                self.audio_checkbox.select()
        else:
            print("No JSON file found in the selected folder.")

    def scroll_english_to_same_line(self, event):
        index = self.entry_polish.index(tk.CURRENT)
        line_number = int(index.split(".")[0])
        self.entry_english.see(f"{line_number}.0")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterlinearApp(root)
    root.mainloop()

