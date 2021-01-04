from tkinter import *

root = Tk()
root.title("radio_buttons")
root.iconbitmap("images/cyberDaggerV2.ico")

# We need to create a tkinter variable to use within the radio button
# tkinter variables are different than python variables
# There are two main ways to do Radio Buttons

"""# Method 1

# This function allows tkinter to keep track of changes made to this variable
op = IntVar()  # The value we have assigned to it is an integer
op.set("1")  # Sets the initial position to 1

def clicked(value):
    Label(root, text=value).pack()

# Create a radio button widget
Radiobutton(root, text="Option 1", variable=op, value=1, command=lambda: clicked(op.get())).pack()
Radiobutton(root, text="Option 2", variable=op, value=2, command=lambda: clicked(op.get())).pack()
Radiobutton(root, text="Option 3", variable=op, value=3, command=lambda: clicked(op.get())).pack()

my_label = Label(root, text=op.get()).pack()"""

# Method 2

# Creates a python list with tuples inside with the radio buttons / this is used when a lot of radio buttons are needed
# the first parameter is what is shown on screen, and the second parameter is the actual value
options = [
    ("Option 1", "1"),
    ("Option 2", "2"),
    ("Option 3", "3")
]

# This function allows tkinter to keep track of changes made to this variable
op = StringVar()  # The value we have assigned to it is a string
op.set("3")  # Sets the initial position to 1

# Create a for loop where the first parameter is text, and the second parameter is option
for text, option in options:
    Radiobutton(root, text=text, variable=op, value=option).pack(anchor=W)

def clicked(value):
    Label(root, text=value).pack()

my_button = Button(root, text="Enter option.", command=lambda: clicked(op.get())).pack()


root.mainloop()
