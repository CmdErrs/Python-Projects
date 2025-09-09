# start a new program by making GUI features available amd message box features available as a short alias

from tkinter import *
import tkinter.messagebox as mbox

# create a Window object and specify a title
window = Tk()
window.title('Message Box Example')


# add function to display various message boxes
def dialog():
    var == mbox.askyesno('Message Box', 'Proceed?')
    if var == 1:
        mbox.showinfo('Yes Box', 'Proceeding...')
    else:
        mbox.showwarning('No Box', 'Cancelling...')


# create a button to call the function when clicked
btn = Button(window, text='Click', command=dialog)


# add the button to the window with positional padding
btn.pack(padx=120, pady=50)


# finally, add loop to capture this windows events
window.mainloop()

# options can be added as a third argument to these method calls, for example Add type='abortretryignore' to get three buttons
