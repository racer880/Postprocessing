from tkinter import Tk, Button, Label, filedialog, messagebox
import tkinter as tk
import os

# Parameter
font_size_title = 24
font_size_text = 14
y_space = 20
font_name_title = "Arial bold"
font_name_text = "Arial"
sheet_names = []

class MultipleVideoStart(tk.Frame):
    def __init__(self, parent, master_class, buttons):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.master_class = master_class
        self.config(bg='gray')

        self.video1_path = None
        self.video2_path = None
        self.video3_path = None


        self.construct_grid()
        self.create_gui_new(buttons)

    def construct_grid(self):
        # configure the grid
        for i in range(6):
            self.columnconfigure(i, weight=1)
        for j in range(10):
            self.rowconfigure(j, weight=1)

    def create_gui_new(self, buttons):

        # Title
        self.title_label = tk.Label(self, text="Mehrere Videos starten", font=(font_name_title, font_size_title), background="grey")
        self.title_label.grid(column=1, row=0, padx=520, pady=2 * y_space, sticky=tk.EW, columnspan=6)

        # Video 1 Button
        self.video1_prelabel = tk.Label(self, text="Video 1:", background="grey")
        self.video1_prelabel.grid(column=0, row=1, padx=50, pady=2 * y_space, sticky=tk.EW, columnspan=2)
        self.video1_button = Button(self, text="Video 1 auswählen", command=self.select_video1)
        self.video1_button.grid(column=2, row=1, padx=5, pady=2 * y_space, sticky=tk.NSEW)
        self.video1_label = Label(self, text="Keine Datei ausgewählt", background="grey")
        self.video1_label.grid(column=3, row=1, padx=50, pady=2 * y_space, sticky=tk.EW)

        # Video 2 Button
        self.video2_prelabel = tk.Label(self, text="Video 2:", background="grey")
        self.video2_prelabel.grid(column=0, row=2, padx=5, pady=2 * y_space, sticky=tk.NSEW, columnspan=2)
        self.video2_button = Button(self, text="Video 2 auswählen", command=self.select_video2)
        self.video2_button.grid(column=2, row=2, padx=5, pady=2 * y_space, sticky=tk.NSEW)
        self.video2_label = Label(self, text="Keine Datei ausgewählt", background="grey")
        self.video2_label.grid(column=3, row=2, padx=20, pady=2 * y_space, sticky=tk.EW)

        # Video 3 Button
        self.video3_prelabel = tk.Label(self, text="Video 3:", background="grey")
        self.video3_prelabel.grid(column=0, row=3, padx=5, pady=2 * y_space, sticky=tk.NSEW, columnspan=2)
        self.video3_button = Button(self, text="Video 3 auswählen", command=self.select_video3)
        self.video3_button.grid(column=2, row=3, padx=5, pady=2 * y_space, sticky=tk.NSEW)
        self.video3_label = Label(self, text="Keine Datei ausgewählt", background="grey")
        self.video3_label.grid(column=3, row=3, padx=20, pady=2 * y_space, sticky=tk.EW)

        # Video Start Button
        self.start_button = Button(self, text="Video starten", width=50, height=5, command=self.start_videos)
        self.start_button.grid(column=1, row=4, padx=170, pady=2 * y_space, sticky=tk.EW)

        # Back to Homepage
        self.info_button = tk.Button(self, text="Zurück", width=50, height=5, command=lambda: self.back_to_homepage(buttons))
        self.info_button.grid(column=3, row=4, padx=5, pady=2*y_space, sticky=tk.EW)

        # Details
        self.infobox_label = tk.Label(self, text="________________________________________",
                                      font=(font_name_title, font_size_title), background="grey")
        self.infobox_label.grid(column=1, row=5, padx=0, pady=y_space, sticky=tk.EW, columnspan=6)
        self.infobox2_label = tk.Label(self, text="Details zur App:", font=(font_name_title, font_size_text),
                                       background="grey")

        self.infobox2_label.grid(column=1, row=6, padx=50, pady=y_space, sticky=tk.W, columnspan=6)
        self.infobox3_label = tk.Label(self, text=" - Ziel der App: 2 bis 3 Videos gleichzeitig starten",
                                       font=(font_name_title, font_size_text), background="grey")
        self.infobox3_label.grid(column=0, row=7, padx=50, pady=y_space, sticky=tk.W, columnspan=6)
        self.infobox4_label = tk.Label(self, text=" - Benutzen Sie die Fotos-App von Windows",
                                       font=(font_name_title, font_size_text), background="grey")
        self.infobox4_label.grid(column=0, row=8, padx=50, pady=y_space, sticky=tk.W, columnspan=6)
    def select_video1(self):
        self.video1_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        self.video1_label.config(text=self.video1_path if self.video1_path else "Keine Datei ausgewählt")

    def select_video2(self):
        self.video2_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        self.video2_label.config(text=self.video2_path if self.video2_path else "Keine Datei ausgewählt")

    def select_video3(self):
        self.video3_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
        self.video3_label.config(text=self.video3_path if self.video3_path else "Keine Datei ausgewählt")

    def start_videos(self):
        if self.video1_path and self.video2_path:
            os.startfile(self.video1_path)
            os.startfile(self.video2_path)
            if self.video3_path:
                os.startfile(self.video3_path)
        else:
            messagebox.showwarning("Fehler", "Bitte wählen Sie mindestens zwei Videos aus.")

    def back_to_homepage(self, buttons):
        self.destroy()
        # Create a label for the title
        self.master.title_label.grid(row=0, column=1, columnspan=4, pady=40)
        k = 0
        for i in range(4):
            for j in range(4):
                buttons[k].grid(row=i + 1, column=j + 1, padx=20, pady=20)
                k = k + 1

