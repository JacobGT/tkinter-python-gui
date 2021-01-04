from tkinter import *
from PIL import ImageTk, Image  # We have to import this to use images
# We also have to: pip install pillow

root = Tk()
root.title("icons & images")
# Add icon to main root window
# The parameters normally would be the location of the file,
# but because it all ready is within the same directory as this .py file we can pass only the name of the file
# in other languages it is called a favicon, here it is called icon
root.iconbitmap("images/greenGuyFawkesMask.ico")

# Tkinters only supports two types of images by itself: gif & ppm but we can use other libraries and modules
# so after importing pil and pip installing pillow, we can start using the image types
# We need to follow a three step process:
# 1. Define the image
# 2. Add the image on a widget with the 'image=' command (almost every widget in tkinter supports an image)
# 3. Put the widget onto the screen
# In the parameters enter the directory in which the file is located, and follow the next code:
my_img = ImageTk.PhotoImage(Image.open("images/coolMasks.png"))
# For explaining purpose I will put it on a label
my_label = Label(root, image=my_img)
my_label.pack()


# Create an exit button
# The commando .quit() we can exit a window
quit_button = Button(root, text="Exit", command=root.quit)
quit_button.pack()

root.mainloop()
