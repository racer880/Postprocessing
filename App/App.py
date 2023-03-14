import tkinter as tk
from HomePage import HomePage


class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        HomePage(self, self.parent).grid(row=0, column=0)


if __name__ == '__main__':
    root = tk.Tk()
    root.configure(bg='gray')
    app = App(root)
    app.grid(row=5, column=4)

    root.geometry("1420x1080")
    root.mainloop()
