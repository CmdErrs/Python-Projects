#widgets
from tkinter import *

# add statements to create a Window object and an Image object
window = Tk()
img = PhotoImage(file='image.gif')

# add statements to create all the necessary widgets
imgLbl = Label(window, image=img)
label1 = Label(window, relief='groove', width=2)
label2 = Label(window, relief='groove', width=2)
label3 = Label(window, relief='groove', width=2)
label4 = Label(window, relief='groove', width=2)
label5 = Label(window, relief='groove', width=2)
label6 = Label(window, relief='groove', width=2)
getBtn = Button(window)
resBtn = Button(window)


# add the widgets to the window using the grid layout manager - ready to receive arguments to specify how the widgets should be positioned at the design state next
#Geometry
imgLbl.grid()
label1.grid()
label2.grid()
label3.grid()
label4.grid()
label5.grid()
label6.grid()
getBtn.grid()
resBtn.grid()


#add a loop statement to sustain the window
#sustain window
window.mainloop()