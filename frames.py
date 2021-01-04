from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Simple Calculator")
root.iconbitmap("images/cyberDaggerV2.ico")

# A frame is like a box with a border, and is used to keep things organized in your window, the text is optional
# Create a LabelFrame widget
frame = LabelFrame(root, text="Frame", padx=10, pady=10)  # Pads the inside of the frame
frame.pack(padx=100, pady=40)  # Pads the outside of the frame

# Instead of placing the button in the root, we can place it in the frame
my_button = Button(frame, text="Click")
# With the frame we can use both grid and pack. We pack the frame and we can grid the button
my_button.grid(row=0, column=0)

my_button2 = Button(frame, text="Click")
my_button2.grid(row=1, column=1)

my_button3 = Button(frame, text="Click")
my_button3.grid(row=2, column=2)

root.mainloop()
