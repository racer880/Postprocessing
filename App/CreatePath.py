import tkinter as tk
import HomePage
import os


class CreatePath(tk.Frame):
    def __init__(self, parent, master_class, buttons):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.master_class = master_class
        self.config(bg='gray')
        self.button1 = tk.Button(self, text="Open Subclass", command=lambda: self.back_to_masterclass(buttons))
        self.button1.grid(row=0, column=0)

    def back_to_masterclass(self, buttons):
        self.destroy()
        print("Zurück ins Hauptmenu von App 3 aus!")

        # Create a label for the title
        self.master.title_label.grid(row=0, column=1, columnspan=4, pady=40)
        k = 0
        for i in range(4):
            for j in range(4):
                buttons[k].grid(row=i + 1, column=j+1, padx=20, pady=20)
                k = k + 1


