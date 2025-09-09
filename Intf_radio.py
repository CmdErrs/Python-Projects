from tkinter import *
import tkinter.messagebox as mbox


# create a Window object and specify a title
window = Tk()
window.title('Radio Button Example')


# create a frame to contain widgets
frame = Frame(window)


# construct a string variable StringVar object to store a selection
book = StringVar()


# create three radio buttons
radio_1 = Radiobutton(frame, text='HTML',
                      variable=book, value='HTML in easy steps')

radio_2 = Radiobutton(frame, text='CSS',
                      variable=book, value='CSS in easy steps')

radio_3 = Radiobutton(frame, text='JS',
                      variable=book, value='JavaScript in easy steps')


# add a statement to specify which radio button will be selected by default when the program starts
radio_1.select()


# add a function to display a radio button selection and a button to call this function
def dialog():
    mbox.showinfo('Selection',
                  'Your Choice: \n' + book.get())


btn = Button(frame, text='Choose', command=dialog)


# add the push button and radio buttons to the frame
btn.pack(side=RIGHT, padx=5)
radio_1.pack(side=LEFT)
radio_2.pack(side=LEFT)
radio_3.pack(side=LEFT)
frame.pack(padx=30, pady=30)


# finally, add the loop to capture this window's events
window.mainloop()



#   A Radiobutton object has a deselect() method that can be used to cancel a selection programmatically
