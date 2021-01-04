from tkinter import *

root = Tk()
root.title("root_grid")

# Creates a Label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Good bye!")
# the label can use the following parameters (there are way more than just this ones)
# bd=1  ==>  adds a border to a label
# relief=SUNKEN  ==> add a sunken effect

# The grid system is just like it sounds, a grid. It has columns (up to down) and rows (left to right),
# and we refer to them with numbers (remember it always starts with zero)
# In the parameters we need to tell where we want it to be
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
# The grid is relative to each other, so keep that in mind.
# You can also write it like this: myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0, columnspan=5)

# The grid system has a navigation system based on the cardinal points: N,W,S,E.
# So with the sticky=N+E parameter we can tell it to stretch from west to east
# and we can tell it to stay in a place with the anchor=E


root.mainloop()
