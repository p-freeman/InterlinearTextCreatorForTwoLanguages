import tkinter as tk

def on_text_change(event):
    input_textarea.configure(height=input_textarea.tk.call(input_textarea._w, "count", "-lines", "1.0", "end"))
    output_textarea.configure(height=output_textarea.tk.call(output_textarea._w, "count", "-lines", "1.0", "end"))

def split_text():
    input_text = input_textarea.get("1.0", "end").split('\n')  # Giriş metnini satırlara ayır
    output_lines = []
    for line in input_text:
        if line.strip():  # Satırın boş olup olmadığını kontrol et
            words = line.split()  # Satırı kelimelere ayır
            output_lines.extend(words)  # Kelimeleri çıktı satırlarına ekle
        output_lines.append("")  # Her boş olmayan satırdan sonra bir boş satır ekle
    
    # Sonuçtan boş satırları kaldır
    while output_lines and not output_lines[-1]:
        output_lines.pop()
    
    output_text = "\n".join(output_lines)  # Çıktı satırlarını yeni satır karakterleriyle birleştir
    output_textarea.delete("1.0", "end")
    output_textarea.insert("1.0", output_text)

root = tk.Tk()
root.title("Metni Bölme")  # Pencere başlığını "Metni Bölme" olarak değiştir

# Pencere boyutu değiştiğinde satır ve sütunun esnemesini ayarla
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Kaydırma çubuğu ile giriş metin alanını oluştur
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

input_textarea = tk.Text(input_frame, height=10, width=30)
input_textarea.pack(side="left", fill="both", expand=True)

input_scrollbar = tk.Scrollbar(input_frame, command=input_textarea.yview)
input_scrollbar.pack(side="right", fill="y")
input_textarea.config(yscrollcommand=input_scrollbar.set)
input_textarea.bind("<Configure>", on_text_change)

# Buton oluştur
split_button = tk.Button(root, text="Metni Böl", command=split_text)  # Buton üzerindeki metni "Metni Böl" olarak değiştir
split_button.grid(row=1, column=0, padx=5, pady=5)

# Kaydırma çubuğu ile çıkış metin alanını oluştur
output_frame = tk.Frame(root)
output_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

output_textarea = tk.Text(output_frame, height=10, width=30)
output_textarea.pack(side="left", fill="both", expand=True)

output_scrollbar = tk.Scrollbar(output_frame, command=output_textarea.yview)
output_scrollbar.pack(side="right", fill="y")
output_textarea.config(yscrollcommand=output_scrollbar.set)
output_textarea.bind("<Configure>", on_text_change)

root.mainloop()
