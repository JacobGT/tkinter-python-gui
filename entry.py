from tkinter import *

root = Tk()
root.title("entry")

# Create an Entry widget
# to have an input field we need to call a entry widget
myEntry = Entry(root, width=30)
myEntry.insert(0, "Enter your name: ")  #What this does is it enters a default text in the entry

# parameters you can use with Entry widget (note. these are only some of the parameters, there are a LOT):
# fg="black"   ==> changes the foreground color / you can also use hex color code
# bg="blue"    ==> changes the background color  / you can also use hex color code
# padx=10   ==> changes the padding (size) of button in x axis
# pady=10    ==> changes the padding (size) of button in y axis
# state=DISABLED ==> changes the state of active of the button
# width=50 ==>  change width of entry
# height=50 ==>  change height of entry
# borderwidth=50 ==>  change width of the border
# borderheight=50 ==>  change height of the border
myEntry.pack()

# define a python function to use in the button
def click():
    # gets what is in the Entry widget and concatenate with string
    hello = "Hello " + myEntry.get()
    # sets the value in entry widget to nothing
    myEntry.delete(0, END)
    # Create a label that is called and posted on the window when the button is clicked
    myLabel1 = Label(root, text=hello)
    myLabel1.pack()


myButton = Button(root, text="Enter Name", padx=30, pady=10, command=click)



myButton.pack()

root.mainloop()
