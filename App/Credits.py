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


class Credits(tk.Frame):
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

        # Titl

        self.title_label = tk.Label(self, text="Release notes", font=(font_name_title, font_size_title),
                                    background="grey")
        self.title_label.grid(column=3, row=0, padx=470, pady=2 * y_space, sticky=tk.NSEW, columnspan=6)

        self.infobox2_label = tk.Label(self, text="App-Informationen", font=(font_name_title, font_size_text), background="grey")
        self.infobox2_label.grid(column=2, row=1, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox3_label = tk.Label(self, text=" - Das Post-Processing-Tool soll den Benutzer bei der Nachbearbeitung der Daten unterstützen", font=(font_name_title, font_size_text), background="grey")
        self.infobox3_label.grid(column=2, row=2, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox4_label = tk.Label(self, text="- Juli 2023 : Release Version 1.0 - App7 + App8 + App10 in Bearbeitung", font=(font_name_title, font_size_text), background="grey")
        self.infobox4_label.grid(column=2, row=3, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox5_label = tk.Label(self, text="- Quellcode unter: https://github.com/racer880/Postprocessing" , font=(font_name_title, font_size_text), background="grey")
        self.infobox5_label.grid(column=2, row=4, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox6_label = tk.Label(self, text="- Erstellen durch Patrick Grubert im Rahmen der Masterarbeit Smartes Baulabor", font=(font_name_title, font_size_text), background="grey")
        self.infobox6_label.grid(column=2, row=5, padx=50, pady=y_space, sticky=tk.W, columnspan=8)
        self.infobox7_label = tk.Label(self, text="- Version 07/2023", font=(font_name_title, font_size_text), background="grey")
        self.infobox7_label.grid(column=2, row=6, padx=50, pady=y_space, sticky=tk.W, columnspan=8)
        # Back to Homepage
        self.info_button = tk.Button(self, text="Zurück", width=50, height=5, command=lambda: self.back_to_homepage(buttons))
        self.info_button.grid(column=6, row=10, padx=5, pady=y_space, sticky=tk.EW)

    def back_to_homepage(self, buttons):
        self.destroy()
        # Create a label for the title
        self.master.title_label.grid(row=0, column=1, columnspan=4, pady=40)
        k = 0
        for i in range(4):
            for j in range(4):
                buttons[k].grid(row=i + 1, column=j + 1, padx=20, pady=20)
                k = k + 1
