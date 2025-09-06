from tkinter import *
import tkinter.messagebox as mbox

# create a Window object and specify a title
window = Tk()
window.title('Checkbox Button Example')

# create a frame to contain widgets
frame = Frame(window)

# construct three integer variable objects to store values
var_1 = BooleanVar()
var_2 = BooleanVar()
var_3 = BooleanVar()


# create three check button widgets whose values will be assigned to the integer variable, whether checked or not.
book_1 = Checkbutton(frame, text='HTML',
                     variable=var_1)
book_2 = Checkbutton(frame, text='CSS',
                     variable=var_2)
book_3 = Checkbutton(frame, text='JS',
                     variable=var_3)


# add a function to display a check button selection
def dialog():
    s = 'Your Choice:'
    if var_1.get() == 1:
        s += '\nHTML in easy steps'
    if var_2.get() == 1:
        s += '\nCSS in easy steps'
    if var_3.get() == 1:
        s += '\nJavaScript in easy steps'
    mbox.showinfo('Selection', s)


# create a button to call the function when clicked
btn = Button(frame, text='Choose', command=dialog)


# add the push button and check buttons to the frame
btn.pack(side=RIGHT, padx=5)
book_1.pack(side=LEFT)
book_2.pack(side=LEFT)
book_3.pack(side=LEFT)
frame.pack(padx=30, pady=30)


# add the loop to capture this windows events
window.mainloop()
