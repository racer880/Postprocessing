import tkinter as tk
import subprocess

class VideoPlotter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Video Plotter")

        self.create_button()

    def create_button(self):
        button = tk.Button(self.window, text="Erstellen", command=self.create_video)
        button.pack()

    def create_video(self):
        subprocess.call(["matlab", "-nodesktop", "-r", "addpath('Files'); PlotToVideo;"])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    plotter = VideoPlotter()
    plotter.run()
