import os
import tkinter as tk
from tkinter import messagebox, ttk

# Parameter
font_size_title = 24
font_size_text = 14
y_space = 20
font_name_title = "Arial bold"
font_name_text = "Arial"
sheet_names = []

class HelpVideos(tk.Frame):
    def __init__(self, parent, master_class, buttons):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.master_class = master_class
        self.config(bg='gray')
        self.video_folder = "Videos"  # Relativer Pfad zum Ordner mit den Videos
        self.video_extension = ".mp4"  # Dateierweiterung der Videos

        # Liste der verfügbaren Videos im Video-Ordner
        self.available_videos = self.get_available_videos()

        self.construct_grid()
        self.create_widgets(buttons)

    def construct_grid(self):
        # configure the grid
        for i in range(10):
            self.columnconfigure(i, weight=1)
        for j in range(10):
            self.rowconfigure(j, weight=1)

    def get_available_videos(self):
        videos = []
        video_path = os.path.join(os.getcwd(), self.video_folder)
        for file_name in os.listdir(video_path):
            if file_name.endswith(self.video_extension):
                videos.append(file_name)
        return videos

    def show_video(self, selected_video):
        video_path = os.path.join(self.video_folder, selected_video)
        if os.path.exists(video_path):
            messagebox.showinfo("Video abspielen", f"Das Video '{selected_video}' wird gestartet.")
            # Code zum Abspielen des Videos
            import subprocess
            subprocess.call(["start", "", video_path], shell=True)  # Öffnet das Video mit dem Standard-Videoplayer (für Windows)
        else:
            messagebox.showerror("Fehler", f"Das Video '{selected_video}' wurde nicht gefunden.")

    def create_widgets(self, buttons):
        # Dropdown-Menü für die Auswahl des Videos
        selected_video = tk.StringVar()

        self.title_label = tk.Label(self, text="Erklärungsvideos zu den Apps", font=(font_name_title, font_size_title),
                                    background="grey")
        self.title_label.grid(column=0, row=0, padx=500, pady=2 * y_space, sticky=tk.NSEW, columnspan=6)

        self.dropdown = ttk.Combobox(self, textvariable=selected_video, values=self.available_videos)
        self.dropdown.grid(column=1, row=1, padx=0, pady=2 * y_space, sticky=tk.EW, columnspan=4)

        # Back to Homepage
        self.info_button = tk.Button(self, text="Zurück", width=50, height=5,
                                     command=lambda: self.back_to_homepage(buttons))
        self.info_button.grid(column=3, row=3, padx=5, pady=2 * y_space, sticky=tk.EW)

        # Details
        self.infobox_label = tk.Label(self, text="________________________________________",
                                      font=(font_name_title, font_size_title), background="grey")
        self.infobox_label.grid(column=0, row=5, padx=0, pady=2 * y_space, sticky=tk.EW, columnspan=8)
        self.infobox2_label = tk.Label(self, text="Details zur App:", font=(font_name_title, font_size_text),
                                       background="grey")

        self.infobox2_label.grid(column=0, row=6, padx=50, pady=y_space, sticky=tk.W, columnspan=8)
        self.infobox3_label = tk.Label(self, text=" - Ziel der App: Einstieg in das Post-Processing-Tool",
                                       font=(font_name_title, font_size_text), background="grey")
        self.infobox3_label.grid(column=0, row=7, padx=50, pady=y_space, sticky=tk.W, columnspan=8)
        self.infobox4_label = tk.Label(self, text=" - Step by Step-Erklärung",
                                       font=(font_name_title, font_size_text), background="grey")
        self.infobox4_label.grid(column=0, row=8, padx=50, pady=y_space, sticky=tk.W, columnspan=8)

        # Funktion zum Abspielen des ausgewählten Videos
        def play_selected_video():
            video_name = selected_video.get()
            self.show_video(video_name)

        # Button zum Abspielen des ausgewählten Videos
        btn_play = tk.Button(self, text="Video abspielen",  width=50, height=5, command=play_selected_video)
        btn_play.grid(column=2, row=3, padx=5, pady=2 * y_space, sticky=tk.EW)

    def back_to_homepage(self, buttons):
        self.destroy()
        # Create a label for the title
        self.master.title_label.grid(row=0, column=1, columnspan=4, pady=40)
        k = 0
        for i in range(4):
            for j in range(4):
                buttons[k].grid(row=i + 1, column=j + 1, padx=20, pady=20)
                k = k + 1



