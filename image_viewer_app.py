from tkinter import *
from PIL import ImageTk, Image

# Creates root window
root = Tk()
root.title("Image Viewer")
root.iconbitmap("images/cyberDaggerV2.ico")

# Creates all images
my_img0 = ImageTk.PhotoImage(Image.open("images/joke0.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("images/joke1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/joke2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/joke3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/joke4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/joke5.png"))
my_img6 = ImageTk.PhotoImage(Image.open("images/joke6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("images/joke7.png"))
my_img8 = ImageTk.PhotoImage(Image.open("images/joke8.jpg"))
my_img9 = ImageTk.PhotoImage(Image.open("images/joke9.jpg"))
# Puts all images in a python list
image_list = [my_img0, my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9]
# Creates label for first image to be displayed
my_label = Label(root, image=my_img0)
my_label.grid(row=0, column=0, columnspan=3)



# Create a label for status of image viewer
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W+E)

# Defines the function for the forward button
def forward(position):
    global my_label
    global button_back
    global button_next

    my_label.grid_forget()  # Forgets and erases the label where the previous image was
    my_label = Label(root, image=image_list[position])  # Creates another label with another image position from list
    button_next = Button(root, text=">>", command=lambda: forward(position + 1))  # Refreshes button info
    button_back = Button(root, text="<<", command=lambda: backward(position - 1))  # Refreshes button info

    if position == 9:
        button_next = Button(root, text=">>", state=DISABLED)  # If it is on last image the button gets disabled

    # Place buttons
    button_next.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    my_label.grid(row=0, column=0, columnspan=3)

    # Refresh status bar
    status = Label(root, text="Image " + str(position + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W+E)

# Defines function for backwards button
def backward(position):
    global my_label
    global button_back
    global button_next

    my_label.grid_forget()  # Forgets and erases the label where the previous image was
    my_label = Label(root, image=image_list[position])  # Creates another label with another image position from list
    button_next = Button(root, text=">>", command=lambda: forward(position + 1))  # Refreshes button info
    button_back = Button(root, text="<<", command=lambda: backward(position - 1))  # Refreshes button info

    if position == 0:
        button_back = Button(root, text="<<", state=DISABLED)  # If it is the first image the button gets disabled

    # Place buttons
    button_next.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    my_label.grid(row=0, column=0, columnspan=3)

    # Refresh status bar
    status = Label(root, text="Image " + str(position + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W+E)

# Create initial backwards and forwards buttons and exit button
button_back = Button(root, text="<<", command=backward, state=DISABLED)
button_next = Button(root, text=">>", command=lambda: forward(1))
button_quit = Button(root, text="EXIT", command=root.quit)
# Place the initial buttons
button_back.grid(row=1, column=0)
button_next.grid(row=1, column=2)
button_quit.grid(row=1, column=1)

root.mainloop()
