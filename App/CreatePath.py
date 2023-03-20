import tkinter as tk
import os

# Parameter
font_size_title = 24
font_size_text = 14
y_space = 30
font_name_title = "Arial bold"
font_name_text = "Arial"


def build_path(path, directory_folder, sub_folder_1, sub_folder_2, sub_folder_3, sub_folder_4, sub_folder_5, sub_folder_6):
    try:
        os.makedirs(path + '/' + directory_folder)
    except FileExistsError:
        print("Directory folder already create!")
        pass

    if sub_folder_1 is not None:
        try:
            os.makedirs(path + '/' + directory_folder + '/' + sub_folder_1)
        except FileExistsError:
            print("Sub folder 1 already create!")
            pass

    if sub_folder_2 is not None:
        try:
            os.makedirs(path + '/' + directory_folder + '/' + sub_folder_2)
        except FileExistsError:
            print("Sub folder 2 already create!")
            pass

    if sub_folder_3 is not None:
        try:
            os.makedirs(path + '/' + directory_folder + '/' + sub_folder_3)
        except FileExistsError:
            print("Sub folder 3 already create!")
            pass

    if sub_folder_4 is not None:
        try:
            os.makedirs(path + '/' + directory_folder + '/' + sub_folder_4)
        except FileExistsError:
            print("Sub folder 4 already create!")
            pass

    if sub_folder_5 is not None:
        try:
            os.makedirs(path + '/' + directory_folder + '/' + sub_folder_5)
        except FileExistsError:
            print("Sub folder 5 already create!")
            pass

    if sub_folder_6 is not None:
        try:
            os.makedirs(path + '/' + directory_folder + '/' + sub_folder_6)
        except FileExistsError:
            print("Sub folder 5 already create!")
            pass


class CreatePath(tk.Frame):
    def __init__(self, parent, master_class, buttons):
        tk.Frame.__init__(self, parent)
        self.textfield = None
        self.title_label = None
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
        label_names = ["Projektpfad:",
                       "Projektname:",
                       "Unterordner 1:",
                       "Unterordner 2:",
                       "Unterordner 3:",
                       "Unterordner 4:",
                       "Unterordner 5:",
                       "Unterordner 6:"
                       ]
        textfield_names = [os.getcwd(),
                           "Projektname",
                           "0. Metadaten",
                           "1. Skripte",
                           "2. Analysen",
                           "3. Videos",
                           "4. Mehr",
                           "5. Mehr"]
        list_of_textfield = []

        # Title
        self.title_label = tk.Label(self, text="Projektpfad erstellen", font=(font_name_title, font_size_title),
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
        self.info_button = tk.Button(self, text="Erstellen", width=50, height=5, command=lambda: build_path(
            list_of_textfield[0].get(), list_of_textfield[1].get(), list_of_textfield[2].get(),
            list_of_textfield[3].get(), list_of_textfield[4].get(), list_of_textfield[5].get(),
            list_of_textfield[6].get(), list_of_textfield[7].get()))
        self.info_button.grid(column=1, row=10, padx=5, pady=y_space, sticky=tk.NS)

        # Back to Homepage
        self.info_button = tk.Button(self, text="Zurück", width=50, height=5,
                                     command=lambda: self.back_to_homepage(buttons))
        self.info_button.grid(column=2, row=10, padx=5, pady=y_space, sticky=tk.NS, columnspan=2)

    def back_to_homepage(self, buttons):
        # Destructor for actual Object
        self.destroy()
        # Redisplay the forget-buttons
        self.master.title_label.grid(row=0, column=1, columnspan=4, pady=40)
        k = 0
        for i in range(4):
            for j in range(4):
                buttons[k].grid(row=i + 1, column=j + 1, padx=20, pady=20)
                k = k + 1
