import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image


class ReadMetadata:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Read Metadata")

        self.file_path = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Dateipfad anzeigen
        self.file_label = tk.Label(self.window, textvariable=self.file_path)
        self.file_label.pack(pady=10)

        # Suchen-Button
        self.search_button = tk.Button(self.window, text="Suchen", command=self.search_file)
        self.search_button.pack(pady=5)

        # Ausgeben-Button
        self.export_button = tk.Button(self.window, text="Ausgeben", command=self.read_metadata)
        self.export_button.pack(pady=5)

    def search_file(self):
        file_types = [
            ("JPEG-Dateien", "*.jpg;*.jpeg"),
            ("PNG-Dateien", "*.png"),
            ("Alle Dateien", "*.*")
        ]
        file_path = filedialog.askopenfilename(filetypes=file_types)
        if file_path:
            self.file_path.set(file_path)
        else:
            messagebox.showinfo("Fehler", "Keine Datei ausgewählt.")

    def read_metadata(self):
        file_path = self.file_path.get()
        if file_path:
            try:
                image = Image.open(file_path)
                exif_data = image._getexif()
                if exif_data:
                    messagebox.showinfo("Metadaten", str(exif_data))
                else:
                    messagebox.showinfo("Metadaten", "Keine Metadaten vorhanden.")
            except Exception as e:
                messagebox.showinfo("Fehler", str(e))
        else:
            messagebox.showinfo("Fehler", "Keine Datei ausgewählt.")

    def run(self):
        self.window.mainloop()


# Verwendung der Klasse
app = ReadMetadata()
app.run()
