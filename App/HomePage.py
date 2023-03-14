import tkinter as tk
from PIL import ImageTk, Image
from CreatePath import CreatePath
from CreateDiagram import CreateDiagram

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
        self.title_label = tk.Label(self, text="Post-Processing-Tool (v0.2)", font=("Arial bold", 36))
        self.title_label.config(bg="gray")
        self.title_label.grid(row=0, column=1, columnspan=4, pady=40)

        # Create a list of image filenames and button names
        image_filenames = ["../Images/Package.png",
                           "../Images/Diagramm.png",
                           "../Images/Directory.png",
                           "../Images/Video.png",
                           "../Images/Excel.png",
                           "../Images/Ressource.png",
                           "../Images/Question.png",
                           "../Images/Question.png",
                           "../Images/Question.png",
                           "../Images/Question.png",
                           "../Images/Question.png",
                           "../Images/Hinzufuegen.png",
                           "../Images/Earthquake.png",
                           "../Images/Bridge.png",
                           "../Images/Appartment.png",
                           "../Images/Notes.png"]
        button_names = ["Sensor-Inventarliste",
                        "Diagramm erstellen",
                        "Ordnerstruktur erstellen",
                        "Video starten",
                        "Spalten zusammenführen",
                        "Projektressourcen",
                        "App 7",
                        "App 8",
                        "App 9",
                        "App 10",
                        "App 11",
                        "Geräte hinzufügen",
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
            print(f"App {app_num} clicked")
        if app_num == 2:
            self.forget_buttons(app_num)
            CreateDiagram(self, self.parent, buttons).grid(row=0, column=0)
        if app_num == 3:
            self.forget_buttons(app_num)
            CreatePath(self, self.parent, buttons).grid(row=0, column=0)
