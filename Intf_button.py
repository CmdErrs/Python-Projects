
# Responding Buttons
# a Button object is created by specifying the window name and the options as arguments to a Button() constructor
# each option is specified as an option=value pair.
# The command option must always specify the name of the function or method to call when the user clicks that button.

# you can also call a button's invoke() method to call the function nominated to it's command option

# start a new program by making GUI features available, then create a window and specify a title
from tkinter import *
window = Tk()
window.title('Button Example')

# create a button to exit the program when clicked
btn_end = Button(window, text='Close', command=exit)

# add a function to toggle the window's background colour when another button gets clicked


def tog():
    if window.cget('bg') == 'magenta':
        window.configure(bg='light gray')
    else:
        window.configure(bg='magenta')


# then create a button to call the function when clicked
btn_tog = Button(window, text='Switch', command=tog)

# add the buttons to the window with positional padding
btn_tog.pack(padx=120, pady=20)
btn_end.pack(padx=120, pady=20)

window.mainloop