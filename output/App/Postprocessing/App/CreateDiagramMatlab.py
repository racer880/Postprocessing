import os
import tkinter as tk
from tkinter import ttk
import subprocess

# Parameter
font_size_title = 24
font_size_text = 14
y_space = 30
font_name_title = "Arial bold"
font_name_text = "Arial"
sheet_names = []

class CreateDiagramMatlab(tk.Frame):
    def __init__(self, parent, master_class, buttons):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.master_class = master_class
        self.config(bg='gray')

        self.script_options = ["X_Achse_als_Referenz.m", "Y_Achse_als_Referenz.m"]
        self.script_var = tk.StringVar()

        self.construct_grid()
        self.create_widgets(buttons)

    def construct_grid(self):
        # configure the grid
        for i in range(10):
            self.columnconfigure(i, weight=1)
        for j in range(10):
            self.rowconfigure(j, weight=1)
    def create_widgets(self, buttons):
        # Dropdown-Menü für die Skriptauswahl
        self.title_label = tk.Label(self, text="2D-Diagramm mit MATLAB erstellen", font=(font_name_title, font_size_title),
                                    background="grey")
        self.title_label.grid(column=3, row=0, padx=450, pady=2 * y_space, sticky=tk.NSEW, columnspan=6)

        self.script_dropdown = ttk.Combobox(self, textvariable=self.script_var, values=self.script_options)
        self.script_dropdown.grid(column=4, row=2, padx=0, pady=y_space, sticky=tk.EW, columnspan=3)
        self.script_dropdown.current(0)  # Standardauswahl auf das erste Skript setzen

        # Button zum Öffnen des MATLAB-Skripts
        self.open_button = tk.Button(self, text="MATLAB-Skript öffnen", width=50, height=5, command=self.open_script)
        self.open_button.grid(column=4, row=3, padx=0, pady=y_space, sticky=tk.EW)

        # Back to Homepage
        self.info_button = tk.Button(self, text="Zurück", width=50, height=5,
                                     command=lambda: self.back_to_homepage(buttons))
        self.info_button.grid(column=6, row=3, padx=5, pady=y_space, sticky=tk.EW)


        # Details
        self.infobox_label = tk.Label(self, text="________________________________________", font=(font_name_title, font_size_title), background="grey")
        self.infobox_label.grid(column=2, row=5, padx=0, pady=2 * y_space, sticky=tk.EW, columnspan=8)
        self.infobox2_label = tk.Label(self, text="Details zur App:", font=(font_name_title, font_size_text), background="grey")
        self.infobox2_label.grid(column=2, row=6, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox3_label = tk.Label(self, text=" - Ziel der App: Ausgabe von 2D-Diagrammen", font=(font_name_title, font_size_text), background="grey")
        self.infobox3_label.grid(column=2, row=7, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox4_label = tk.Label(self, text="- Es kann zwischen X/Y-Achse als Referenz gewählt werden", font=(font_name_title, font_size_text), background="grey")
        self.infobox4_label.grid(column=2, row=8, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox5_label = tk.Label(self, text="- Speichern des Plots direkt über Menü am Plot" , font=(font_name_title, font_size_text), background="grey")
        self.infobox5_label.grid(column=2, row=9, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox6_label = tk.Label(self, text="- Dringend benötigt: MATLAB-Software", font=(font_name_title, font_size_text), background="grey")
        self.infobox6_label.grid(column=2, row=10, padx=50, pady=y_space, sticky=tk.W, columnspan=8)

    def open_script(self):
        selected_script = self.script_var.get()
        # Pfad zum MATLAB-Skript
        current_dir = os.getcwd()
        relative_path = os.path.join(current_dir, "Files", selected_script)
        # Aufruf des MATLAB-Skripts
        subprocess.call(
            ["matlab", "-nodesktop", "-nosplash", "-r", f"run('{relative_path}'); input('Press Enter to exit');"])

    def back_to_homepage(self, buttons):
        self.destroy()
        # Create a label for the title
        self.master.title_label.grid(row=0, column=1, columnspan=4, pady=40)
        k = 0
        for i in range(4):
            for j in range(4):
                buttons[k].grid(row=i + 1, column=j + 1, padx=20, pady=20)
                k = k + 1
