from tkinter import *

# Create the first/main window
root = Tk()
root.title("main_window")
root.iconbitmap("images/cyberDaggerV2.ico")

def open():
    # Create a new window
    top = Toplevel()
    top.title("new_window")

    def close_root():
        top.destroy() # If you use top.quit() all the program will end

    quit = Button(top, text="Close New Window", command=close_root).grid(row=1, column=1)

window_btn = Button(root, text="Open New Window", command=open).pack()

# Refreshes both windows
root.mainloop()
# You can close the Toplevel window, and the program will continue running; however, if you close the root window
# the program will stop running. Whenever you .quit() or .destroy() the root window all the program ends.

# If you are trying to work with variables in between windows, and it is not working, try making the variable a global variable.
