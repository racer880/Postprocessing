import tkinter as tk
import subprocess
import sys,os

# Parameter
font_size_title = 24
font_size_text = 14
y_space = 30
font_name_title = "Arial bold"
font_name_text = "Arial"
sheet_names = []


def create_diagram():
    # Pfad zum MATLAB-Skript
    current_dir = os.getcwd()
    relative_path = os.path.join(current_dir, "Files", r"PlotToVideo.m")
    # Aufruf des MATLAB-Skripts
    subprocess.call(["matlab", "-nodesktop", "-nosplash", "-r", f"run('{relative_path}'); input('Press Enter to exit');"])
class PlotToVideo(tk.Frame):
    def __init__(self, parent, master_class, buttons):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.master_class = master_class
        self.config(bg='gray')

        self.construct_grid()
        self.create_gui_new(buttons)

    def construct_grid(self):
        # configure the grid
        for i in range(10):
            self.columnconfigure(i, weight=1)
        for j in range(10):
            self.rowconfigure(j, weight=1)

    def create_gui_new(self, buttons):

        # Title
        self.title_label = tk.Label(self, text="Plot to Video - Konverter", font=(font_name_title, font_size_title),background="grey")
        self.title_label.grid(column=3, row=0, padx=520, pady=2 * y_space, sticky=tk.NSEW, columnspan=6)


        # Create folder button
        self.info_button = tk.Button(self, text="MATLAB-Skript öffnen", width=50, height=5, command=create_diagram)
        self.info_button.grid(column=4, row=2, padx=70, pady=y_space, sticky=tk.EW)

        # Back to Homepage
        self.info_button = tk.Button(self, text="Zurück", width=50, height=5, command=lambda: self.back_to_homepage(buttons))
        self.info_button.grid(column=6, row=2, padx=5, pady=y_space, sticky=tk.EW)

        # Details
        self.infobox_label = tk.Label(self, text="________________________________________", font=(font_name_title, font_size_title), background="grey")
        self.infobox_label.grid(column=2, row=5, padx=0, pady=2 * y_space, sticky=tk.EW, columnspan=8)
        self.infobox2_label = tk.Label(self, text="Details zur App:", font=(font_name_title, font_size_text), background="grey")
        self.infobox2_label.grid(column=2, row=6, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox3_label = tk.Label(self, text=" - Ziel der App: XY-Diagramm als mp4-Datei darstellen", font=(font_name_title, font_size_text), background="grey")
        self.infobox3_label.grid(column=2, row=7, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox4_label = tk.Label(self, text="- Ein Punkt folgt dabei das erzeugte Diagramm", font=(font_name_title, font_size_text), background="grey")
        self.infobox4_label.grid(column=2, row=8, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox5_label = tk.Label(self, text="- Die Geschwindigkeit zwischen 2 Rohdaten kann zwischen 10-1000 ms eingestellt werden" , font=(font_name_title, font_size_text), background="grey")
        self.infobox5_label.grid(column=2, row=9, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox6_label = tk.Label(self, text="- Dringend benötigt: MATLAB-Software", font=(font_name_title, font_size_text), background="grey")
        self.infobox6_label.grid(column=2, row=10, padx=50, pady=y_space, sticky=tk.W, columnspan=8)

    def back_to_homepage(self, buttons):
        self.destroy()
        # Create a label for the title
        self.master.title_label.grid(row=0, column=1, columnspan=4, pady=40)
        k = 0
        for i in range(4):
            for j in range(4):
                buttons[k].grid(row=i + 1, column=j + 1, padx=20, pady=20)
                k = k + 1
