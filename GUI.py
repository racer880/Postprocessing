import tkinter as tk
from tkinter import ttk
from CreatePath import CreatePath
from Testing.Datenbankgui import Datenbankgui
from Testing.CreateDiagramm import CreateDiagramm
from Testing.datenbank import DB


class GUI(tk.Tk):
    # --------------------------------------------------------------------------------------------
    # Constructor

    def __init__(self, geometry, title):
        super().__init__()
        self.create_window(geometry, title)
        self.construct_grid()
        self.create_home_widgets()

    # --------------------------------------------------------------------------------------------
    # Create Window and Grid

    def create_window(self, geometry, title):
        self.geometry(geometry)
        self.title(title)
        self.configure(background="grey")
        self.resizable(width=False, height=False)

    def construct_grid(self):
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, weight=1)
        self.rowconfigure(10, weight=1)
        self.rowconfigure(11, weight=1)

    # --------------------------------------------------------------------------------------------
    # Clear & Navigation
    def clear_widgets(self):
        # destroy all widgets from frame
        for widgets in self.winfo_children():
            widgets.destroy()

    def goto_home(self):
        self.clear_widgets()
        self.create_home_widgets()

    def goto_SQLinventory(self):
        self.clear_widgets()
        self.create_SQL_widgets()

    def goto_inventory(self):
        self.clear_widgets()
        self.create_excel_widgets()

    def goto_filepath(self):
        self.clear_widgets()
        self.create_filepath_widgets()

    def goto_info(self):
        self.clear_widgets()
        self.create_info_widgets()

    def goto_diagramm(self):
        self.create_diagramm_widgets()

    # --------------------------------------------------------------------------------------------
    # Widgets-Layout

    def create_home_widgets(self):
        # Title
        title_label = ttk.Label(self, text="Post Processing Tool (v0.1)"
                                , font=("Didot", 36), background="grey")
        title_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NS, columnspan=4)

        # Modul_0
        modul_0_button = ttk.Button(self, text="Sensor in SQL-Liste hinzufügen"
                                    , width=50, command=self.goto_SQLinventory)
        modul_0_button.grid(column=1, row=2, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Modul_1
        modul_1_button = ttk.Button(self, text="Sensor in Inventarliste hinzufügen"
                                    , width=50, command=self.goto_inventory)
        modul_1_button.grid(column=1, row=3, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Modul_2
        modul_2_button = ttk.Button(self, text="Nachbearbeitung der Daten", width=50)
        modul_2_button.grid(column=1, row=4, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Modul_0
        modul_4_button = ttk.Button(self, text="Excel-Listen zusammenführen", width=50)
        modul_4_button.grid(column=1, row=5, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Modul_3
        modul_5_button = ttk.Button(self, text="Diagramm erstellen"
                                    , width=50, command=self.goto_diagramm)
        modul_5_button.grid(column=1, row=6, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Modul_4
        modul_6_button = ttk.Button(self, text="Projektpfad erstellen", width=50, command=self.goto_filepath)
        modul_6_button.grid(column=1, row=7, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Modul_0
        modul_7_button = ttk.Button(self, text="XXX", width=50)
        modul_7_button.grid(column=1, row=8, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Info
        info_button = ttk.Button(self, text="Info", width=50, command=self.goto_info)
        info_button.grid(column=0, row=10, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Quit
        quit_button = ttk.Button(self, text="Abbrechen", width=50, command=self.quit)
        quit_button.grid(column=2, row=10, padx=5, pady=5, sticky=tk.NS, columnspan=2)

    def create_SQL_widgets(self):
        title_label = ttk.Label(self, text="Personendatenbank", background="grey")
        title_label.grid(row=0, column=0)

        empty_label = ttk.Label(self, text="", background="grey")
        empty_label.grid(row=0, column=1)

        surname_label = ttk.Label(self, text="Nachname", background="grey")
        surname_label.grid(row=1)

        name_label = ttk.Label(self, text="Vorname", background="grey")
        name_label.grid(row=2)

        modul_1_textfield = ttk.Entry(self)
        modul_1_textfield.grid(row=1, column=1)

        modul_2_textfield = ttk.Entry(self)
        modul_2_textfield.grid(row=2, column=1)

        button_set = ttk.Button(self, text='Eintrag DB', width=20, command=self.action_SQL)
        button_set.grid(row=3, column=0, sticky=tk.W, pady=4)

        button_kill = ttk.Button(self, text='Abbrechen', width=20, command=self.destroy)
        button_kill.grid(row=3, column=1, sticky=tk.W, pady=4)

        status_label = ttk.Label(self, text="")
        status_label.grid(row=6, columnspan=2)

    def create_excel_widgets(self):
        # Title
        title_label = ttk.Label(self, text="Sensor in Inventarliste hinzufügen", font=("Didot", 24), background="grey")
        title_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NS, columnspan=4)

        # Modul_1
        modul_1_button = ttk.Button(self, text="Sensor in Inventarliste hinzufügen", width=50)
        modul_1_button.grid(column=1, row=2, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Modul_2
        modul_2_button = ttk.Button(self, text="Excel-Listen zusammenführen", width=50)
        modul_2_button.grid(column=1, row=4, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Zurück
        info_button = ttk.Button(self, text="Zurück", width=50, command=self.goto_home)
        info_button.grid(column=1, row=10, padx=5, pady=5, sticky=tk.NS, columnspan=2)

    def create_filepath_widgets(self):
        # Title
        title_label = ttk.Label(self, text="Projektpfad erstellen", font=("Didot", 24), background="grey")
        title_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.NS, columnspan=4)

        # Label_1
        modul_1_label = ttk.Label(self, text="Projektpfad:", width=50, background="grey")
        modul_1_label.grid(column=0, row=2, padx=5, pady=5, sticky=tk.E)

        # Textfields_1
        modul_2_textfield = ttk.Entry(self)
        modul_2_textfield.insert(0, "C:/Users/patrick.grubert/PycharmProjects/Postprocessing")
        modul_2_textfield.grid(column=1, row=2, padx=5, pady=5, columnspan=3, sticky=tk.EW)

        # Label_3
        modul_4_label = ttk.Label(self, text="Projektname:", width=50, background="grey")
        modul_4_label.grid(column=0, row=3, padx=5, pady=5, sticky=tk.E)

        # Textfields_2
        modul_5_textfield = ttk.Entry(self)
        modul_5_textfield.insert(0, "Projektname")
        modul_5_textfield.grid(column=1, row=3, padx=5, pady=5, columnspan=3, sticky=tk.EW)

        # Label_4
        modul_6_label = ttk.Label(self, text="Unterordner 1:", width=50, background="grey")
        modul_6_label.grid(column=0, row=4, padx=5, pady=5, sticky=tk.E)

        # Textfields_3
        modul_7_textfield = ttk.Entry(self)
        modul_7_textfield.insert(0, "0. Metadaten")
        modul_7_textfield.grid(column=1, row=4, padx=5, pady=5, columnspan=3, sticky=tk.EW)

        # Label_4
        modul_8_label = ttk.Label(self, text="Unterordner 2:", width=50, background="grey")
        modul_8_label.grid(column=0, row=5, padx=5, pady=5, sticky=tk.E)

        # Textfields_5
        modul_9_textfield = ttk.Entry(self)
        modul_9_textfield.insert(0, "1. Skripte")
        modul_9_textfield.grid(column=1, row=5, padx=5, pady=5, columnspan=3, sticky=tk.EW)

        # Label_4
        modul_10_label = ttk.Label(self, text="Unterordner 3:", width=50, background="grey")
        modul_10_label.grid(column=0, row=6, padx=5, pady=5, sticky=tk.E)

        # Textfields_6
        modul_11_textfield = ttk.Entry(self)
        modul_11_textfield.insert(0, "2. Analysen")
        modul_11_textfield.grid(column=1, row=6, padx=5, pady=5, columnspan=3, sticky=tk.EW)

        # Label_5
        modul_12_label = ttk.Label(self, text="Unterordner 4:", width=50, background="grey")
        modul_12_label.grid(column=0, row=7, padx=5, pady=5, sticky=tk.E)

        # Textfields_7
        modul_13_textfield = ttk.Entry(self)
        modul_13_textfield.insert(0, "3. Videos")
        modul_13_textfield.grid(column=1, row=7, padx=5, pady=5, columnspan=3, sticky=tk.EW)

        # Label_6
        modul_14_label = ttk.Label(self, text="Unterordner 5:", width=50, background="grey")
        modul_14_label.grid(column=0, row=8, padx=5, pady=5, sticky=tk.E)

        # Textfields_8
        modul_15_textfield = ttk.Entry(self)
        modul_15_textfield.insert(0, "4. Mehr")
        modul_15_textfield.grid(column=1, row=8, padx=5, pady=5, columnspan=3, sticky=tk.EW)

        # Erstellen
        info_button = ttk.Button(self, text="Erstellen", width=50, command=lambda: self.create_filepath_directory(
            modul_2_textfield.get(), modul_5_textfield.get(), modul_7_textfield.get(), modul_9_textfield.get()
            , modul_11_textfield.get(), modul_13_textfield.get(), modul_15_textfield.get()))
        info_button.grid(column=1, row=10, padx=5, pady=5, sticky=tk.NS)

        # Zurück
        info_button = ttk.Button(self, text="Zurück", width=50, command=self.goto_home)
        info_button.grid(column=2, row=10, padx=5, pady=5, sticky=tk.NS, columnspan=2)

    def create_info_widgets(self):
        # Title
        title_label = ttk.Label(self, text="Information", font=("Didot", 24),
                                background="grey")
        title_label.grid(column=1, row=0, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Text
        title_label = ttk.Label(self, text="Erstellt durch Patrick Grubert", font=("Didot", 18),
                                background="grey")
        title_label.grid(column=1, row=2, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Text
        title_label = ttk.Label(self, text="Im Rahmen der Masterarbeit", font=("Didot", 18),
                                background="grey")
        title_label.grid(column=1, row=4, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Text
        title_label = ttk.Label(self, text="Smartes Baukastensystem - Messtechnik im Baulabor", font=("Didot", 18),
                                background="grey")
        title_label.grid(column=1, row=6, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Text
        title_label = ttk.Label(self, text="2022 - 2023", font=("Didot", 18),
                                background="grey")
        title_label.grid(column=1, row=8, padx=5, pady=5, sticky=tk.NS, columnspan=2)

        # Zurück
        info_button = ttk.Button(self, text="Zurück", width=50, command=self.goto_home)
        info_button.grid(column=1, row=10, padx=5, pady=5, sticky=tk.NS, columnspan=2)

    def create_diagramm_widgets(self, ):
        CreateDiagramm(self)


    # --------------------------------------------------------------------------------------------
    # Connectivity to other Classes

    def create_filepath_directory(self, modul_2_textfield, modul_5_textfield, modul_7_textfield, modul_9_textfield
                                  , modul_11_textfield, modul_13_textfield, modul_15_textfield):
        CreatePath(str(modul_2_textfield), str(modul_5_textfield), str(modul_7_textfield)
                   , str(modul_9_textfield), str(modul_11_textfield), str(modul_13_textfield), str(modul_15_textfield))

    def action_SQL(self):
        Datenbankgui()

        #db = DB()
        #self.status['text'] = ""
        #db.schreibDB(self.nname.get(), self.vname.get())
        #self.anzeige.configure(state='normal')
        #result = db.leseDB()
        #self.anzeige.delete(1.0, self.END)
        #self.anzeige.insert(self.END, result[0])
        #self.anzeige.configure(state='disabled')
        #self.datensaetze['text'] = "Anzahl Datensätzer: " + result[1]

