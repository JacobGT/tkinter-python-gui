from tkinter import *

root = Tk()
root.title("dropdown_menu")
root.iconbitmap("images/cyberDaggerV2.ico")
root.geometry("400x500")

# Create a Tkinter Var
clicked = StringVar()
clicked.set("Choose a Programming Language")
drop = OptionMenu(root, clicked, "Python", "Java", "GoLang", "C#", "C", "C++", "PHP", "JavaScript").pack()
# instead of doing it like above, you can use a python list
# languages = [
# "Python",
# "Java",
# "GoLang",
# "C#",
# "C",
# "C++",
# "PHP",
# "JavaScript"
# ]

# and then
# drop = OptionMenu(root, clicked, *options).pack()

def show():
    show_label = Label(root, text=clicked.get()).pack()

refresh = Button(root, text="Refresh", command=show).pack()


root.mainloop()