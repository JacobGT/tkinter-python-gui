from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("message_box")
root.iconbitmap("images/cyberDaggerV2.ico")


# The different type of messagebox and what they return are as follows:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno  NEW ONES include: askyesnocancel, askretrycancel
# askyesno   ==>   yes == 1    /    no == 0
# askyesnocancel ==> yes == 1    /    no == 0    /    cancel == None   (cancel returns None/nothing)
# askretrycancel  ==>   retry == 1    /    cancel == 0
# askokcancel     ==>   ok == 1   /  cancel == 0
# askquestion     ==>   yes == "yes"    /    no == "no"
# showerror, showwarning, & showinfo ==>   ok == "ok"
# Each messagebox has its own icon and special sound.


# Def function of messagebox when the button is clicked
def popup():
    # The most basic messagebox is the show info, and in the parameters it can have: title, message, options
    messagebox.showinfo(title="showinfo", message="This is the showinfo messagebox")
    messagebox.showwarning("showwarning", "This is the showwarning")  # You do not need to specify title and/or message
    messagebox.showerror("showerror", "This is the showerror")  # It is preferable to specify title and message
    messagebox.askquestion(title="askquestion", message="This is the askquestion")
    messagebox.askokcancel(title="askokcancel", message="This is askokcancel")
    messagebox.askyesno(title="askyesno", message="This is askyesno")
    messagebox.askyesnocancel(title="askyesnocancel", message="This is askyesnocancel")
    messagebox.askretrycancel(title="askretrycancel", message="This is askretrycancel")

    # We can see what does it return with a label
    response = messagebox.askretrycancel(title="askyesnocancel", message="This is askyesnocancel")
    Label(root, text=response).pack()

# A message box is a pop up box
button = Button(root, text="Pop up.", command=popup).pack()


root.mainloop()
