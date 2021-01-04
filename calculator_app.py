from tkinter import *

# Create root window
root = Tk()
root.title("Simple Calculator")

# Create entry widget
entryNum = Entry(root, width=35, borderwidth=5)
entryNum.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Define function for when users click a button
def button_click(number):
    current = entryNum.get()
    entryNum.delete(0, END)
    entryNum.insert(0, str(current) + str(number))


# Define function for clearing entry
def button_clear():
    entryNum.delete(0, END)


# Define function for adding process
def button_add():
    first_number = entryNum.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entryNum.delete(0, END)


# Define function for equal button for different math processes
def button_equal():
    second_number = entryNum.get()
    entryNum.delete(0, END)

    if math == "addition":
        entryNum.insert(0, f_num + int(second_number))

    if math == "subtraction":
        entryNum.insert(0, f_num - int(second_number))

    if math == "multiplication":
        entryNum.insert(0, f_num * int(second_number))

    if math == "division":
        entryNum.insert(0, f_num / int(second_number))


# Defines function for subtraction
def button_subtract():
    first_number = entryNum.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entryNum.delete(0, END)


# Defines function for multiplying
def button_multiply():
    first_number = entryNum.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entryNum.delete(0, END)


# Defines function for dividing
def button_divide():
    first_number = entryNum.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entryNum.delete(0, END)


# Create Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)

button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
