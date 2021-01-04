from tkinter import *

root = Tk()
root.title("checkbox")
root.iconbitmap("images/cyberDaggerV2.ico")
root.geometry("500x400")

# Create a tkinter variable
# The default output is an integer 1 or 0 depending if the checkbutton is on or off respectively
var = IntVar()
c = Checkbutton(root, text="Check this box", variable=var).pack()

# You can change the on or off value with this
# var = StringVar()
# c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="off")
# c.deselect()  # There is a weir glitch that if you do not deselect it, it will be selected at first and will not print anything
# c.pack()

def show():
    show_label = Label(root, text=var.get()).pack()

refresh = Button(root, text="Refresh", command=show).pack()

root.mainloop()
