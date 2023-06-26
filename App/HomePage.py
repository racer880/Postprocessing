import tkinter as tk
from PIL import ImageTk, Image
from CreatePath import CreatePath
from CreateDiagramMatplotlib import CreateDiagramMatplotlib
from CreateDiagramMatlab import CreateDiagramMatlab
from ExcelColumnMerger import ExcelColumnMerger
from ExcelToSQLiteMigrator import ExcelToSQLiteMigrator

buttons = []


class HomePage(tk.Frame):

    def __init__(self, parent, master_class):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.master_class = master_class
        self.config(bg='gray')

        # Create a frame for the buttons
        self.frame = tk.Frame(self.parent)
        self.frame.configure(bg='gray')
        self.pack(pady=20)

        # Create a label for the title
        self.title_label = tk.Label(self, text="Post-Processing-Tool", font=("Arial bold", 36))
        self.title_label.config(bg="gray")
        self.title_label.grid(row=0, column=1, columnspan=4, pady=40)

        # Create a list of image filenames and button names
        image_filenames = ["../Images/Directory.png",
                           "../Images/Excel.png",
                           "../Images/SQLite.png",
                           "../Images/Matlab.png",
                           "../Images/Metadaten.png",
                           "../Images/Question.png",
                           "../Images/Question.png",
                           "../Images/Question.png",
                           "../Images/Video.png",
                           "../Images/Hinzufuegen.png",
                           "../Images/Package.png",
                           "../Images/Ressource.png",
                           "../Images/Earthquake.png",
                           "../Images/Bridge.png",
                           "../Images/Appartment.png",
                           "../Images/Notes.png"]
        button_names = ["Projektpfad erstellen",
                        "Spalten zusammenführen",
                        "Excel zu Datenbank Konverter",
                        "Diagramm erstellen (MATLAB)",
                        "Metadaten auslesen",
                        "App 6",
                        "App 7",
                        "App 8",
                        "Video starten",
                        "Geräte hinzufügen",
                        "Sensor-Inventarliste",
                        "Projektressourcen",
                        "Projekt: Gleitschubversagen",
                        "Projekt: Hinterrhein",
                        "Projekt: Lysbüchel",
                        "Release Notes"]
        # Create a 4x4 grid of buttons with different images
        for i in range(4):
            for j in range(4):
                # Load the image
                self.image = Image.open(image_filenames[i * 4 + j])
                self.image = self.image.resize((130, 130))  # resize the image
                self.img = ImageTk.PhotoImage(self.image)

                # Create a button with the image and black border
                self.button = tk.Button(self, text=button_names[i * 4 + j], font=('Arial bold', 12), image=self.img,
                                        compound="top", command=lambda app_num=i * 4 + j + 1: self.app_clicked(app_num),
                                        highlightthickness=3, highlightbackground="black", relief="solid", width=300)
                self.button.image = self.img  # Keep a reference to the image to prevent garbage collection
                self.button.grid(row=i + 1, column=j + 1, padx=20, pady=20)
                buttons.append(self.button)

    def forget_buttons(self, app_num):
        self.title_label.grid_forget()
        for i in buttons:
            i.grid_forget()

    def app_clicked(self, app_num):
        # This function will be called when a button is clicked
        print(f"App {app_num} clicked")
        if app_num == 1:
            self.forget_buttons(app_num)
            CreatePath(self, self.parent, buttons).grid(row=0, column=0)
        if app_num == 2:
            self.forget_buttons(app_num)
            ExcelColumnMerger(self, self.parent, buttons).grid(row=0, column=0)
        if app_num == 3:
            self.forget_buttons(app_num)
            ExcelToSQLiteMigrator(self, self.parent, buttons).grid(row=0, column=0)
        if app_num == 4:
            self.forget_buttons(app_num)
            CreateDiagramMatlab(self, self.parent, buttons).grid(row=0, column=0)

