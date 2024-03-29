import tkinter as tk
from tkinter import filedialog
import os
import json
from PIL import Image, ImageDraw, ImageFont

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
        self.root.title("Interlinear Text Generator")
        
        # Create a frame to organize GUI elements
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        
        # Labels and entry fields for title, filename, and text inputs
        self.label_title = tk.Label(self.frame, text="Titel:")
        self.label_title.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_title = tk.Entry(self.frame, width=30)
        self.entry_title.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        self.label_filename = tk.Label(self.frame, text="Dateiname/Ordnername:")
        self.label_filename.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_filename = tk.Entry(self.frame, width=30)
        self.entry_filename.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        # Create line number display for French and German text fields
        self.french_line_numbers = LineNumbers(self.frame, width=4, bg="#f0f0f0", bd=0, wrap="none")
        self.french_line_numbers.grid(row=3, column=2, sticky="nsew")
        
        self.german_line_numbers = LineNumbers(self.frame, width=4, bg="#f0f0f0", bd=0, wrap="none")
        self.german_line_numbers.grid(row=3, column=3, sticky="nsew")
        
        self.label_french = tk.Label(self.frame, text="Französische Wörter:")
        self.label_french.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_french = tk.Text(self.frame, height=10, width=30)
        self.entry_french.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        self.entry_french.bind("<Button-1>", self.scroll_german_to_same_line)
        
        self.label_german = tk.Label(self.frame, text="Deutsche Wörter:")
        self.label_german.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.entry_german = tk.Text(self.frame, height=10, width=30)
        self.entry_german.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        
        # Textfields for vertical distance and font size
        self.label_vertical_distance = tk.Label(self.frame, text="Vertikaler Abstand (px):")
        self.label_vertical_distance.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_vertical_distance = tk.Entry(self.frame, width=10)
        self.entry_vertical_distance.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.entry_vertical_distance.insert(0, "10")  # Pre-load with default value
        
        self.label_font_size = tk.Label(self.frame, text="Schriftgröße:")
        self.label_font_size.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.entry_font_size = tk.Entry(self.frame, width=10)
        self.entry_font_size.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.entry_font_size.insert(0, "12")  # Pre-load with default value
        
        # Buttons to fetch text from files and generate interlinear text
        self.create_button = tk.Button(self.frame, text="Interlinearen Text erstellen", command=self.create_interlinear)
        self.create_button.grid(row=6, column=0, padx=5, pady=5)
        
        self.open_button = tk.Button(self.frame, text="Bestehendes Projekt öffnen", command=self.open_project)
        self.open_button.grid(row=6, column=1, padx=5, pady=5)
        
        # Initialize variables for storing interlinear text data
        self.interlinear_data = {}  # Dictionary to store interlinear text data for the current project
        self.current_project_path = None  # Path to the current project folder
        
        # Load existing interlinear text data
        # self.load_interlinear_data()
    
    def create_interlinear(self):
        """
        Create a new interlinear text project.
        """
        # Check if data has been entered
        if not (self.entry_title.get() or self.entry_filename.get() or self.entry_french.get("1.0", tk.END).strip() or self.entry_german.get("1.0", tk.END).strip() or self.entry_vertical_distance.get() or self.entry_font_size.get()):
            return  # If no data has been entered, simply return without performing further actions
        
        # Get inputs from GUI fields
        title = self.entry_title.get().strip()
        filename = self.entry_filename.get().strip()
        french_text = self.entry_french.get("1.0", tk.END).strip()
        german_text = self.entry_german.get("1.0", tk.END).strip()
        vertical_distance = int(self.entry_vertical_distance.get())  # Get vertical distance value
        font_size = int(self.entry_font_size.get())  # Get font size value
        
        # Create a folder for the project
        folder_path = os.path.join(os.getcwd(), f"{filename}")
        os.makedirs(folder_path, exist_ok=True)
        
        # Save French and German text to text files with Windows-compatible line breaks
        french_text_path = os.path.join(folder_path, "french_text.txt")
        with open(french_text_path, "w", encoding="utf-8") as file:
            file.write(french_text.strip('\n'))
        
        german_text_path = os.path.join(folder_path, "german_text.txt")
        with open(german_text_path, "w", encoding="utf-8") as file:
            file.write(german_text.strip('\n'))
        
        # Read French and German text files
        with open(french_text_path, "r", encoding="utf-8") as file:
            french_lines = file.readlines()
        
        with open(german_text_path, "r", encoding="utf-8") as file:
            german_lines = file.readlines()
        
        # Generate interlinear text in HTML format
        interlinear_html = f"<!DOCTYPE html>\n<html>\n<head>\n<meta charset='UTF-8'>\n<title>{title}</title>\n<style>\n"
        interlinear_html += "body { font-family: sans-serif; }\n"  # Use non-serif font for the whole document
        interlinear_html += ".word_package { display: inline-block; margin-right: 20px; margin-bottom: " + str(vertical_distance) + "px; }\n"  # Add vertical margin
        interlinear_html += ".french_word { font-weight: bold; }\n"
        interlinear_html += ".german_word { margin-top: 5px; }\n"
        interlinear_html += "</style>\n</head>\n<body style='font-size:" + str(font_size) + "px;'>\n"  # Set font size
        
        # Add title as H1 header
        interlinear_html += f"<h1>{title}</h1>\n"
        
        # Iterate through French and German lines to create interlinear pairs
        for french_line, german_line in zip(french_lines, german_lines):
            # Handle paragraphs
            if french_line.strip() == "":
                interlinear_html += "<br>\n"
                continue
            
            interlinear_html += "<div class='word_package'>\n"
            interlinear_html += f"<div class='french_word'>{french_line.strip()}</div>\n"
            interlinear_html += f"<div class='german_word'>{german_line.strip()}</div>\n"
            interlinear_html += "</div>\n"
        
        interlinear_html += "</body>\n</html>"
        
        # Save interlinear text to an HTML file inside the project folder
        file_path = os.path.join(folder_path, f"{filename}.html")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(interlinear_html)
        
        # Interlinear data to be saved in JSON file
        json_data = {
            "title": title,
            "filename": filename,
            "french_text": french_text,
            "german_text": german_text,
            "vertical_distance": vertical_distance,
            "font_size": font_size
        }
        json_file_path = os.path.join(folder_path, f"{filename}.json")
        with open(json_file_path, "w") as json_file:
            json.dump(json_data, json_file)
        
        print("Interlinear text saved to:", file_path)
        print("French text saved to:", french_text_path)
        print("German text saved to:", german_text_path)
    
    def open_project(self):
        """
        Open an existing interlinear text project by loading its JSON file.
        """
        # Clear GUI fields
        self.entry_title.delete(0, tk.END)
        self.entry_filename.delete(0, tk.END)
        self.entry_french.delete("1.0", tk.END)
        self.entry_german.delete("1.0", tk.END)
        self.entry_vertical_distance.delete(0, tk.END)
        self.entry_font_size.delete(0, tk.END)
        
        # Prompt user to select a project folder containing the JSON file
        project_folder = filedialog.askdirectory(title="Projektordner auswählen")
        if not project_folder:
            return  # If no folder selected, return without further action
        
        # Load project data from JSON file
        json_file_path = os.path.join(project_folder, os.path.basename(project_folder) + ".json")
        if os.path.exists(json_file_path):
            with open(json_file_path, "r") as json_file:
                project_data = json.load(json_file)
            
            # Fill GUI fields with loaded data
            self.entry_title.insert(0, project_data.get("title", ""))
            self.entry_filename.insert(0, project_data.get("filename", ""))
            self.entry_french.insert("1.0", project_data.get("french_text", ""))
            self.entry_german.insert("1.0", project_data.get("german_text", ""))
            self.entry_vertical_distance.insert(0, str(project_data.get("vertical_distance", 10)))
            self.entry_font_size.insert(0, str(project_data.get("font_size", 12)))
        else:
            print("Keine JSON-Datei im ausgewählten Ordner gefunden.")


    def scroll_german_to_same_line(self, event):
        """
        Scroll the German text field to the same line as the clicked line in the French text field.
        """
        index = self.entry_french.index(tk.CURRENT)
        line_number = int(index.split(".")[0])
        self.entry_german.see(f"{line_number}.0")


if __name__ == "__main__":
    # Create and run the GUI application
    root = tk.Tk()
    app = InterlinearApp(root)
    root.mainloop()
