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
    #eng = matlab.engine.start_matlab()
    #eng.cd(r'C:\Users\patrick.grubert\Downloads\Git\PostProcessing\Postprocessing\Files', nargout=0)
    #getattr(eng, "excelColumnMerger")(nargout=0)

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
        for i in range(4):
            self.columnconfigure(i, weight=1)
        for j in range(11):
            self.rowconfigure(j, weight=1)

    def create_gui_new(self, buttons):

        # Title
        self.title_label = tk.Label(self, text="Diagramme erstellen", font=(font_name_title, font_size_title),
                                    background="grey")
        self.title_label.grid(column=0, row=0, padx=5, pady=2 * y_space, sticky=tk.EW, columnspan=4)

        # Create folder button
        self.info_button = tk.Button(self, text="Erstellen", width=50, height=5, command=create_diagram)
        self.info_button.grid(column=1, row=10, padx=5, pady=y_space, sticky=tk.NS)

        # Back to Homepage
        self.info_button = tk.Button(self, text="Zurück", width=50, height=5,
                                     command=lambda: self.back_to_homepage(buttons))
        self.info_button.grid(column=2, row=10, padx=5, pady=y_space, sticky=tk.NS, columnspan=2)

    def back_to_homepage(self, buttons):
        self.destroy()
        # Create a label for the title
        self.master.title_label.grid(row=0, column=1, columnspan=4, pady=40)
        k = 0
        for i in range(4):
            for j in range(4):
                buttons[k].grid(row=i + 1, column=j + 1, padx=20, pady=20)
                k = k + 1
