# start a new program by making the GUI features available and message box features available as a short alias
from tkinter import *
import tkinter.messagebox as mbox


# create a Window object and specify a title
window = Tk()
window.title('Entry Example')


# create a frame containing an entry field for input
frame = Frame(window)
entry = Entry(frame)


# add a function to display data currently entered
def dialog():
    mbox.showinfo('Greetings', 'Welcome ' + entry.get())


# create a button to call the function when clicked
btn=Button(frame, text = 'Enter Name', command=dialog)


# add the button and entry field to the frame at set sides
btn.pack(side = RIGHT, padx=5)
entry.pack(side=LEFT)
frame.pack(padx=20, pady=20)


#add the loop to capture this windows events
window.mainloop


# use a text widget instead of a entry widget if you want the user to enter multiple lines of text. The Text() constructor accepts the same options as the Entry() constructor, plus a height option
# use a label widget instead of an entry widget if you want to display the text that the user cannot edit
