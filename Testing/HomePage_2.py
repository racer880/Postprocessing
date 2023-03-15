import tkinter as tk
from PIL import ImageTk, Image

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Post Processing (v0.2)")
        self.master.geometry("1920x1080")


        # Create a frame for the buttons
        frame = tk.Frame(self.master)
        frame.configure(bg='gray')
        frame.pack(pady=20)

        # Create a label for the title
        title_label = tk.Label(frame, text="Post-Processing-Tool (v0.2)", font=("Arial bold", 36))
        title_label.config(bg="gray")
        title_label.grid(row=0, columnspan=4, pady=40, )


        # Create a list of image filenames
        image_filenames = ["../Images/Package.png", "../Images/Diagramm.png", "../Images/Directory.png", "../Images/Video.png"
            , "../Images/Question.png", "../Images/Question.png", "../Images/Question.png", "../Images/Question.png"
            , "../Images/Question.png", "../Images/Question.png", "../Images/Question.png", "../Images/Question.png"
            , "../Images/Question.png", "../Images/Question.png", "../Images/Question.png", "../Images/Notes.png"]

        button_names = ["Sensor-Inventarliste", "Diagramm erstellen", "Ordnerstruktur erstellen", "Video starten"
                        , "App 5", "App 6", "App 7", "App 8"
                        , "App 9", "App 10", "App 11", "App 12"
                        , "App 13", "App 14", "App 15", "Release Notes"]

        # Create a 4x4 grid of buttons with different images
        for i in range(4):
            for j in range(4):
                # Load the image
                image = Image.open(image_filenames[i*4+j])
                image = image.resize((130, 130))  # resize the image
                img = ImageTk.PhotoImage(image)

                # Create a button with the image and black border
                button = tk.Button(frame, text=button_names[i*4+j], font=('Arial bold', 14), image=img, compound="top", command=lambda app_num=i*4+j+1: self.app_clicked(app_num), highlightthickness=3, highlightbackground="black", relief="solid",width=250)
                button.image = img  # Keep a reference to the image to prevent garbage collection
                button.grid(row=i+1, column=j, padx=20, pady=20)

    def app_clicked(self, app_num):
        # This function will be called when a button is clicked
        print(f"App {app_num} clicked")


root = tk.Tk()
app = App(root)
root.configure(bg='gray')
root.mainloop()
