from tkinter import Tk, Button, filedialog, messagebox
import os

class MultipleVideoStart:
    def __init__(self):
        self.root = Tk()
        self.root.title("Multiple Video Start")

        self.video1_path = None
        self.video2_path = None

        # Video 1 Button
        self.video1_button = Button(self.root, text="Video 1 auswählen", command=self.select_video1)
        self.video1_button.pack()

        # Video 2 Button
        self.video2_button = Button(self.root, text="Video 2 auswählen", command=self.select_video2)
        self.video2_button.pack()

        # Video Start Button
        self.start_button = Button(self.root, text="Video starten", command=self.start_videos)
        self.start_button.pack()

        self.root.mainloop()

    def select_video1(self):
        self.video1_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])

    def select_video2(self):
        self.video2_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])

    def start_videos(self):
        if self.video1_path and self.video2_path:
            os.startfile(self.video1_path)
            os.startfile(self.video2_path)
        else:
            messagebox.showwarning("Fehler", "Bitte wählen Sie beide Videos aus.")


# Starte die GUI
app = MultipleVideoStart()
