from tkinter import *

root = Tk()
root.title("buttons")

# define a python function to use in the button
def click():
    # Create a label that is called and posted on the window when the button is clicked
    myLabel1 = Label(root, text="You clicked the button.")
    myLabel1.pack()

# Creates a Button widget
# In the parameters we need to tell it where we want the Button, and then add other parameters
# With the state parameters we can tell it if the user can or can not click the button / the states are DISABLED & ENABLED:
# example: myButton = Button(root, text="Click Me!", state=DISABLED)
# with padx and pady we can resize the button by adding some 'padding'
myButton = Button(root, text="Click Me!", padx=30, pady=10, command=click)
# with the command parameter we can execute a fuction but do not add parenthesis because in this case it will execute it automatically
# before even clicking
# to use parameters you have to use a lambda, an example is provided in calculator_app.py
# ex. button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))

# parameters you can use (note. these are only some of the parameters, there are a LOT):
# fg="black"   ==> changes the foreground color / you can also use hex color code
# bg="blue"    ==> changes the background color  / you can also use hex color code
# padx=10   ==> changes the padding (size) of button in x axis
# pady=10    ==> changes the padding (size) of button in y axis
# state=DISABLED ==> changes the state of active of the button
# command=function ==> execute a fuction


myButton.pack()

root.mainloop()
