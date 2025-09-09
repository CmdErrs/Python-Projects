# widgets
from tkinter import *

window = Tk()
img = PhotoImage(file='image.gif')
# static properties
window.title('Random Number Generator')


# prevent resizing the window along both x and y axis - this will disable the window's resize button
window.resizable(0, 0)


# add a statement to specify text to appear on the face of the first button widget
getBtn.configure(text='Get my random numbers')      # The widgets configure() method allows properties to be subsequently added or modified after they have been created


# add statement to specify text to appear on the face of the second button widget
resBtn.configure(text='Reset')


imgLbl = Label(window, image=img)
label1 = Label(window, relief='groove', width=2)
label2 = Label(window, relief='groove', width=2)
label3 = Label(window, relief='groove', width=2)
label4 = Label(window, relief='groove', width=2)
label5 = Label(window, relief='groove', width=2)
label6 = Label(window, relief='groove', width=2)
getBtn = Button(window)
resBtn = Button(window)


# Geometry
imgLbl.grid(row=1, column=1, rowspan=2)
label1.grid(row=1, column=2, padx=10)
label2.grid(row=1, column=3, padx=10)
label3.grid(row=1, column=4, padx=10)
label4.grid(row=1, column=5, padx=10)
label5.grid(row=1, column=6, padx=10)
label6.grid(row=1, column=7, padx=(10, 20))
getBtn.grid(row=2, column=2, columnspan=4)
resBtn.grid(row=2, column=6, columnspan=2)


# specify that each small empty label should initially display an ellipsis
#initial properties
label1.configure(text='...')
label2.configure(text='...')
label3.configure(text='...')
label4.configure(text='...')
label5.configure(text='...')
label6.configure(text='...') 


# add statement to specify that the second button widget should initially be disabled
resBtn.configure(state=DISABLED)        #button states are recognised by tkinter constants of DISABLED(off), NORMAL(on), or ACTIVE(pressed)


# sustain window
window.mainloop()
