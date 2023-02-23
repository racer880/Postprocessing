import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Load Excel sheet into a pandas DataFrame
data = pd.read_excel('..\Files\Examples.xlsx', sheet_name='Sheet1')

# Extract three diagrams from the DataFrame
fig1, ax1 = plt.subplots()
data.plot(x='Column1', y='Column2', ax=ax1)

fig2, ax2 = plt.subplots()
data.plot(x='Column1', y='Column3', ax=ax2)

fig3, ax3 = plt.subplots()
data.plot(x='Column1', y='Column4', ax=ax3)

# Create tkinter GUI
root = tk.Tk()
root.title('Live View of Diagrams')

# Create matplotlib FigureCanvasTkAgg objects for the three diagrams
canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

canvas3 = FigureCanvasTkAgg(fig3, master=root)
canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Define start and stop functions for the live view
def start():
    canvas1.draw()
    canvas2.draw()
    canvas3.draw()

def stop():
    root.quit()

# Create tkinter buttons for starting and stopping the live view
start_button = tk.Button(root, text='Start', command=start)
start_button.pack(side=tk.LEFT)

stop_button = tk.Button(root, text='Stop', command=stop)
stop_button.pack(side=tk.RIGHT)

# Run the tkinter main loop
root.mainloop()
