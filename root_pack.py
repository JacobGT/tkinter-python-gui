# Tkinter all ready comes with python, we only have to import it
from tkinter import *  # We import everything (thats what  * means) from tkinter
# In tkinter everything is a widget. There are: button widgets, text widgets, frame widgets, etc.
# So the first thing we need to create is the root widget, the window.
root = Tk()  # Just like that we create the base window, this has to go first in EVERY tkinter program
# Every window has a minimaze, maximiaze, and 'x' button that exits the program

root.title("root_pack")  # With this we can change title of root

# To create basically anything in tkinter you have to follow a two step process
# 1. Define the thing and create it
# 2. Put it up in the screen

# Create a label. / First thing in parameter is where we want to put it, in this case in the root (main) window
myLabel = Label(root, text="Hello World!")  # There are a lot of parameters you can use and text is one of them
myLabel.pack()  # Now we 'pack' the label in the window. The .pack function just shoves it in the windows where there is free space
# Pack just packs this in just as big as the 'stuff' inside is

# Now we need an event loop so that the window refreshes adn knows what is happening
root.mainloop()  # When the program ends, this loop will end.
