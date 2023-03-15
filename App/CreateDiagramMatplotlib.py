import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

# Parameter
font_size_title = 24
font_size_text = 14
y_space = 30
font_name_title = "Arial bold"
font_name_text = "Arial"
sheet_names = []

class CreateDiagramMatplotlib(tk.Frame):
    def __init__(self, parent, master_class, buttons):
        tk.Frame.__init__(self, parent)
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
        # Create a list of labels and textfield
        label_names = ["Pfad x-Achse:",
                       "Pfad Diagramm 1:",
                       "Pfad Diagramm 2:",
                       "Pfad Diagramm 3:",
                       "Parameter 1:",
                       "Parameter 2:",
                       "Parameter 3:",
                       "Parameter 4:"
                       ]
        textfield_names = ["0",
                           "0",
                           "0",
                           "0",
                           "0",
                           "0",
                           "0",
                           "0"]
        list_of_textfield = []

        # Title
        self.title_label = tk.Label(self, text="Diagramme erstellen", font=(font_name_title, font_size_title),
                                    background="grey")
        self.title_label.grid(column=0, row=0, padx=5, pady=2 * y_space, sticky=tk.EW, columnspan=4)

        for i in range(len(label_names)):
            # Label
            tk.Label(self, text=label_names[i], width=50, font=(font_size_text, font_size_text),
                     background="grey").grid(column=0, row=2 + i, padx=2, pady=y_space)

            # Textfield
            self.textfield = tk.Entry(self, font=(font_name_text, font_size_text))
            self.textfield.insert(0, textfield_names[i])
            self.textfield.grid(column=1, row=2 + i, padx=5, pady=y_space, columnspan=3, sticky=tk.EW)

            # Save textfield in a list
            list_of_textfield.append(self.textfield)

        # Create folder button
        self.info_button = tk.Button(self, text="Erstellen", width=50, height=5, command=self.create_diagram)
        self.info_button.grid(column=1, row=10, padx=5, pady=y_space, sticky=tk.NS)

        # Back to Homepage
        self.info_button = tk.Button(self, text="Zurück", width=50, height=5,
                                     command=lambda: self.back_to_homepage(buttons))
        self.info_button.grid(column=2, row=10, padx=5, pady=y_space, sticky=tk.NS, columnspan=2)

    def create_diagram(self):
        pass

    def browse_file(self, sheet_option):
        global file_path, sheet_name
        file_path = filedialog.askopenfilename()
        try:
            workbook = openpyxl.load_workbook(file_path)
            sheet_names = workbook.sheetnames
            sheet_name.set(sheet_names[0])
            sheet_option['menu'].delete(0, 'end')
            for name in sheet_names:
                sheet_option['menu'].add_command(label=name, command=tk._setit(sheet_name, name))
        except Exception as e:
            messagebox.showerror('Error', e)

    def compare_columns(self, sheet_names, file_path, file_path2, col1_entry, col2_entry, scaling_entry):
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_names[0].get())
            df2 = pd.read_excel(file_path2, sheet_name=sheet_names[1].get())
            col1 = col1_entry.get()
            col2 = col2_entry.get()
            data1 = df[col1].tolist()
            data2 = df2[col2].tolist()
            fig, ax = plt.subplots()
            ax.plot(data1, label='Sheet 1')
            ax.plot(data2, label='Sheet 2')
            ax.legend()
            ax.set_xlabel('Index')
            ax.set_ylabel('Values')
            ax.set_title(f'Comparison of {col1} and {col2}')
            scaling = float(scaling_entry.get())
            fig.set_size_inches(scaling, scaling)
            eps_path = filedialog.asksaveasfilename(defaultextension='.eps')
            fig.savefig(eps_path, format='eps')
            plt.close()
        except Exception as e:
            messagebox.showerror('Error', e)

    def back_to_homepage(self, buttons):
        self.destroy()
        # Create a label for the title
        self.master.title_label.grid(row=0, column=1, columnspan=4, pady=40)
        k = 0
        for i in range(4):
            for j in range(4):
                buttons[k].grid(row=i + 1, column=j+1, padx=20, pady=20)
                k = k + 1


