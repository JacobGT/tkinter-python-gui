from tkinter import *
# Import the file dialog
from tkinter import filedialog
from PIL import ImageTk, Image


root = Tk()
root.title("open_files_dialog_box")
root.iconbitmap("images/cyberDaggerV2.ico")

def open():
    # Using the file dialog
    # This will not actually open the file, it will only return the name and location of the file
    root.filename = filedialog.askopenfilename(initialdir="C:/", title="Select a Title",
                                               filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"),
                                                          ("jpeg files", "*.jpeg"), ("All Files", "*.*")))
    # Now that we know the location we can call for the image
    mylabel = Label(root, text=root.filename).pack()

    # Showing Image
    global my_img
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_label = Label(root, image=my_img).pack()

my_bttn = Button(root, text="Open Image", command=open).pack()

root.mainloop()
