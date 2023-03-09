import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

class CreateDiagramm:

    def __init__(self):
        # Load Excel sheet into a pandas DataFrame
        data = pd.read_excel('..\Files\Gleitschubversage_Wand_3.xlsx', sheet_name='Sheet0')

        # Extract three diagrams from the DataFrame
        fig1, ax1 = plt.subplots()
        data.plot(x='C_1_Zeit[s]', y='C_2_WA-50_1[mm]', ax=ax1)

        fig2, ax2 = plt.subplots()
        data.plot(x='C_1_Zeit[s]', y='C_2_WA-100_3[mm]', ax=ax2)

        fig3, ax3 = plt.subplots()
        data.plot(x='C_1_Zeit[s]', y='C_2_WA-20_3[mm]', ax=ax3)

        # Create tkinter GUI
        root = tk.Tk()
        root.title('Live View of Diagrams')

        # Create a frame for the diagrams
        frame = tk.Frame(root)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create a vertical scrollbar for the frame
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a canvas for the frame with the scrollbar attached
        canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Configure the scrollbar to scroll the canvas
        scrollbar.config(command=canvas.yview)

        # Create a frame within the canvas for the diagrams
        diagram_frame = tk.Frame(canvas)
        diagram_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create matplotlib FigureCanvasTkAgg objects for the three diagrams
        canvas1 = FigureCanvasTkAgg(fig1, master=diagram_frame)
        canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        canvas2 = FigureCanvasTkAgg(fig2, master=diagram_frame)
        canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        canvas3 = FigureCanvasTkAgg(fig3, master=diagram_frame)
        canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Create a window within the canvas to contain the frame
        window = canvas.create_window(0, 0, anchor=tk.NW, window=diagram_frame)

    # Define start and stop functions for the live view
    def start(self, canvas1, canvas2, canvas3):
        while True:
            canvas1.draw()
            canvas2.draw()
            canvas3.draw()
            self.update()
            time.sleep(1)

    def stop(self):
        self.quit()

    def button(self):
        # Create tkinter buttons for starting and stopping the live view
        start_button = tk.Button(self, text='Start', command=self.start)
        start_button.pack(side=tk.LEFT)

        stop_button = tk.Button(self, text='Stop', command=self.stop)
        stop_button.pack(side=tk.RIGHT)

# Run the tkinter main loop
#root.mainloop()