# With tkinter, a scrollbar is a separate widget that can be attached to listbox, text, canvas, and entry widgets.

# start a new program by making GUI features available and a message box features available as a short alias
from tkinter import *
import tkinter.messagebox as mbox


# create a window object and specify the title
window = Tk()
window.title('Listbox Example')


# create a frame to contain widgets
frame = Frame(window)


# create a listbox widget offering three list items
listbox = Listbox(frame)
listbox.insert(1, 'HTML in easy steps')
listbox.insert(2, 'CSS in easy steps')
listbox.insert(3, 'JavaScript in easy steps')


# add a function to display a listbox selection
def dialog():
    mbox.showinfo('Selection', 'Your Choice: ' +
                  listbox.get(listbox.curselection()))


# create a button to call the function when clicked
btn = Button(frame, text='Choose', command=dialog)


# add the button and listbox to the frame at set sides
btn.pack(side = RIGHT, padx =5)
listbox.pack(side = LEFT)
frame.pack(padx = 30, pady= 30)


# if the selectmode is set to MULTIPLE, the curselection() method returns a tuple of the selected index numbers
