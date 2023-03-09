import tkinter as tk


class MasterClass(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.button1 = tk.Button(self, text="Open Subclass", command=self.open_subclass)
        self.button1.grid(row=0, column=0)

        self.button2 = tk.Button(self, text="Open Subclass 2", command=self.open_subclass2)
        self.button2.grid(row=1, column=0)

    def open_subclass(self):
        self.button1.grid_forget()
        self.button2.grid_forget()
        print("App 1 gestartet!")
        Subclass(self, self.parent).grid(row=0, column=0)

    def open_subclass2(self):
        self.button1.grid_forget()
        self.button2.grid_forget()
        print("App 2 gestartet!")
        Subclass2(self, self.parent).grid(row=0, column=0)


class Subclass(tk.Frame):
    def __init__(self, parent, master_class):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.master_class = master_class

        self.button2 = tk.Button(self, text="Back to MasterClass", command=self.back_to_masterclass)
        self.button2.grid(row=0, column=0)
        print("Grid in App 1 erstellt!")

    def back_to_masterclass(self):
        self.destroy()
        print("Zurück ins Hauptmenu von App 1 aus!")
        self.master.button1.grid(row=0, column=0)
        self.master.button2.grid(row=1, column=0)


class Subclass2(tk.Frame):
    def __init__(self, parent, master_class):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.master_class = master_class

        self.button3 = tk.Button(self, text="Back to MasterClass", command=self.back_to_masterclass)
        self.button3.grid(row=0, column=0)
        print("Grid in App 2 erstellt!")

    def back_to_masterclass(self):
        self.destroy()
        print("Zurück ins Hauptmenu von App 2 aus!")
        self.master.button1.grid(row=0, column=0)
        self.master.button2.grid(row=1, column=0)


if __name__ == '__main__':
    root = tk.Tk()
    app = MasterClass(root)
    app.grid(row=5, column=5)
    root.geometry("1920x1080")
    root.mainloop()
