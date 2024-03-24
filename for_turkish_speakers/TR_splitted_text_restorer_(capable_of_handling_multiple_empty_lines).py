import tkinter as tk

def on_text_change(event):
    input_textarea.configure(height=input_textarea.tk.call(input_textarea._w, "count", "-lines", "1.0", "end"))
    output_textarea.configure(height=output_textarea.tk.call(output_textarea._w, "count", "-lines", "1.0", "end"))

def restore_text():
    input_lines = input_textarea.get("1.0", "end").split('\n')  # Get lines from input text
    output_lines = []
    current_line = []  # List to store words for each line
    for line in input_lines:
        if line.strip():  # Check if the line is not empty
            current_line.append(line)  # Add word to current line
        elif current_line:  # If line is empty but there are words in current line
            output_lines.append(" ".join(current_line))  # Join words with space and add to output lines
            current_line = []  # Reset current line
        else:  # If there are consecutive empty lines
            output_lines.append("")  # Add one empty line to output
    
    if current_line:  # If there are remaining words in the current line
        output_lines.append(" ".join(current_line))  # Join words with space and add to output lines
    
    output_text = "\n".join(output_lines)  # Join output lines with single newline characters
    output_textarea.delete("1.0", "end")
    output_textarea.insert("1.0", output_text)

root = tk.Tk()
root.title("Text Restorer")

# Configure row and column to expand when window is resized
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Create input textarea with scrollbar
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

input_textarea = tk.Text(input_frame, height=10, width=30)
input_textarea.pack(side="left", fill="both", expand=True)

input_scrollbar = tk.Scrollbar(input_frame, command=input_textarea.yview)
input_scrollbar.pack(side="right", fill="y")
input_textarea.config(yscrollcommand=input_scrollbar.set)
input_textarea.bind("<Configure>", on_text_change)

# Create button
restore_button = tk.Button(root, text="Restore Text", command=restore_text)
restore_button.grid(row=1, column=0, padx=5, pady=5)

# Create output textarea with scrollbar
output_frame = tk.Frame(root)
output_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

output_textarea = tk.Text(output_frame, height=10, width=30)
output_textarea.pack(side="left", fill="both", expand=True)

output_scrollbar = tk.Scrollbar(output_frame, command=output_textarea.yview)
output_scrollbar.pack(side="right", fill="y")
output_textarea.config(yscrollcommand=output_scrollbar.set)
output_textarea.bind("<Configure>", on_text_change)

root.mainloop()
