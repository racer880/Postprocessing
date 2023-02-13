import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

class CreateDiagramm:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Chart App")

        # Create a button to open the file dialog
        self.browse_button = tk.Button(text="Browse", command=self.browse_file)
        self.browse_button.pack()

        # Create a label to display the selected file
        self.file_label = tk.Label(text="No file selected")
        self.file_label.pack()

        # Create a button to plot the chart
        self.plot_button = tk.Button(text="Plot Chart", command=self.plot_chart, state=tk.DISABLED)
        self.plot_button.pack()

    def browse_file(self):
        # Open a file dialog and get the selected file's path
        file_path = filedialog.askopenfilename()

        # Update the label to display the selected file
        self.file_label.config(text=file_path)

        # Enable the plot button
        self.plot_button.config(state=tk.NORMAL)

    def plot_chart(self):
        # Read the Excel file into a Pandas DataFrame
        df = pd.read_excel(self.file_label['text'])

        # Select the first sheet in the Excel file
        sheet = df.iloc[:, 0]

        # Get the values and labels for the bar chart
        values = sheet.values
        labels = sheet.index

        # Clear any previous plots
        plt.clf()

        # Create the bar chart
        plt.bar(labels, values)
        plt.xlabel('Labels')
        plt.ylabel('Values')
        plt.title('Bar Chart')

        # Display the chart
        plt.show()


