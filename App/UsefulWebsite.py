import tkinter as tk
import subprocess
import sys,os
import webbrowser

# Parameter
font_size_title = 24
font_size_text = 14
y_space = 30
font_name_title = "Arial bold"
font_name_text = "Arial"
sheet_names = []


def create_diagram():
    webbrowser.open("https://www.adobe.com/de/products/premiere/free-trial-download.html?gclid=CjwKCAjw44mlBhAQEiwAqP3eVuZ77zcx1h7P6IwHC1Rrt_noD_sIYdjTjgsK9p5O9IIGmM-UUvKLlhoCJN8QAvD_BwE&mv=search&mv=search&sdid=FD1KZKX8&ef_id=CjwKCAjw44mlBhAQEiwAqP3eVuZ77zcx1h7P6IwHC1Rrt_noD_sIYdjTjgsK9p5O9IIGmM-UUvKLlhoCJN8QAvD_BwE:G:s&s_kwcid=AL!3085!3!600022136771!e!!g!!premiere%20pro%20download!1419109650!57403483404")
    webbrowser.open("https://tentaclesync.com/timecode-tool")
    webbrowser.open("https://tentaclesync.com/sync-studio")
    webbrowser.open("https://www.python.org/downloads/windows/")
    webbrowser.open("https://ch.mathworks.com/products/matlab.html")
class UsefulWebsite(tk.Frame):
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

        self.title_label = tk.Label(self, text="Nützliche Websiten", font=(font_name_title, font_size_title),
                                    background="grey")
        self.title_label.grid(column=3, row=0, padx=520, pady=2 * y_space, sticky=tk.NSEW, columnspan=6)


        # Create folder button
        self.info_button = tk.Button(self, text="Websiten öffnen", width=50, height=5, command=create_diagram)
        self.info_button.grid(column=4, row=2, padx=70, pady=y_space, sticky=tk.EW)

        # Back to Homepage
        self.info_button = tk.Button(self, text="Zurück", width=50, height=5, command=lambda: self.back_to_homepage(buttons))
        self.info_button.grid(column=6, row=2, padx=5, pady=y_space, sticky=tk.EW)

        # Details
        self.infobox_label = tk.Label(self, text="________________________________________", font=(font_name_title, font_size_title), background="grey")
        self.infobox_label.grid(column=2, row=5, padx=0, pady=2 * y_space, sticky=tk.EW, columnspan=8)
        self.infobox2_label = tk.Label(self, text="Details zur App:", font=(font_name_title, font_size_text), background="grey")
        self.infobox2_label.grid(column=2, row=6, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox3_label = tk.Label(self, text=" - Ziel der App: Hier werden die relaventen Links beim Klicken aufgerufen", font=(font_name_title, font_size_text), background="grey")
        self.infobox3_label.grid(column=2, row=7, padx=50, pady= y_space, sticky=tk.W, columnspan=8)
        self.infobox4_label = tk.Label(self, text="- Bei fehlenden Installationen können hier die App erreicht werden", font=(font_name_title, font_size_text), background="grey")
        self.infobox4_label.grid(column=2, row=8, padx=50, pady= y_space, sticky=tk.W, columnspan=8)


    def back_to_homepage(self, buttons):
        self.destroy()
        # Create a label for the title
        self.master.title_label.grid(row=0, column=1, columnspan=4, pady=40)
        k = 0
        for i in range(4):
            for j in range(4):
                buttons[k].grid(row=i + 1, column=j + 1, padx=20, pady=20)
                k = k + 1