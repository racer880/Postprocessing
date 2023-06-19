import tkinter as tk
from tkinter import filedialog
import pandas as pd
import sqlite3

# Parameter
font_size_title = 24
font_size_text = 14
y_space = 30
font_name_title = "Arial bold"
font_name_text = "Arial"
sheet_names = []


class ExcelToSQLiteMigrator(tk.Frame):
    def __init__(self, parent, master_class, buttons):
        tk.Frame.__init__(self, parent)
        self.info_button = None
        self.save_path = None
        self.excel_file_path = None
        self.parent = parent
        self.master_class = master_class
        self.config(bg='gray')

        self.construct_grid()
        self.create_gui_new(buttons)

    def construct_grid(self):
        # configure the grid
        for i in range(4):
            self.columnconfigure(i, weight=1)
        for j in range(11):
            self.rowconfigure(j, weight=1)

    def create_gui_new(self, buttons):

        # Title
        self.title_label = tk.Label(self, text="Diagramme erstellen", font=(font_name_title, font_size_title),
                                    background="grey")
        self.title_label.grid(column=0, row=0, padx=5, pady=2 * y_space, sticky=tk.EW, columnspan=4)

        # Choose Excel-File-Button
        self.info_button = tk.Button(self, text="Excel-Datei Auswählen", width=50, height=5, command=lambda: self.choose_excel_file())
        self.info_button.grid(column=1, row=8, padx=5, pady=y_space, sticky=tk.NS)

        # Choose Save-Path-Button
        self.info_button = tk.Button(self, text="Speicherort auswählen", width=50, height=5, command=lambda: self.choose_save_path())
        self.info_button.grid(column=1, row=9, padx=5, pady=y_space, sticky=tk.NS)

        # Choose Migrate-to-sql-Button
        self.info_button = tk.Button(self, text="Excel zu DB migrieren", width=50, height=5, command=lambda: self.migrate_to_sqlite())
        self.info_button.grid(column=1, row=10, padx=5, pady=y_space, sticky=tk.NS)

        # Back to Homepage
        self.info_button = tk.Button(self, text="Zurück", width=50, height=5,
                                     command=lambda: self.back_to_homepage(buttons))
        self.info_button.grid(column=2, row=10, padx=5, pady=y_space, sticky=tk.NS, columnspan=2)

    def choose_excel_file(self):
        self.excel_file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])

    def choose_save_path(self):
        self.save_path = filedialog.askdirectory()

    def migrate_to_sqlite(self):
        if self.excel_file_path is None or self.save_path is None:
            return

        try:
            df = pd.read_excel(self.excel_file_path)
            db_path = self.save_path + "/database.db"
            conn = sqlite3.connect(db_path)
            df.to_sql("data", conn, if_exists="replace", index=False)
            conn.close()
            print("Migration complete.")
        except Exception as e:
            print(f"Error occurred during migration: {str(e)}")


def choose_excel_file(self):
    self.choose_excel_file()


def choose_save_path(self):
    self.choose_save_path()


def migrate_to_sqlite(self):
    self.migrate_to_sqlite()


def back_to_homepage(self, buttons):
    self.destroy()
    # Create a label for the title
    self.master.title_label.grid(row=0, column=1, columnspan=4, pady=40)
    k = 0
    for i in range(4):
        for j in range(4):
            buttons[k].grid(row=i + 1, column=j + 1, padx=20, pady=20)
            k = k + 1