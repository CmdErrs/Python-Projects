# widgets
from tkinter import *
window = Tk()
img = PhotoImage(file='image.gif')
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


# static properties
window.title('Random Number Generator')
window.resizable(0, 0)
getBtn.configure(text='Get my random numbers')
resBtn.configure(text='Reset')  


# initial properties
label1.configure(text='...')
label2.configure(text='...')
label3.configure(text='...')
label4.configure(text='...')
label5.configure(text='...')
label6.configure(text='...')
resBtn.configure(state=DISABLED)


# dynamic properties
from random import sample

# define a function that generates and assigns six unique random numbers to the small labels and reverses the state of both buttons
def pick():
    nums=sample(range(1,60),6)
    label1.configure(text=nums[0])
    label2.configure(text=nums[1])
    label3.configure(text=nums[2])
    label4.configure(text=nums[3])
    label5.configure(text=nums[4])
    label6.configure(text=nums[5])
    getBtn.configure(state=DISABLED)
    resBtn.configure(state=NORMAL)


# define a function to display an ellipsis on each small label and revert both buttons to their initial states
def reset():
    label1.configure(text='...')
    label2.configure(text='...')
    label3.configure(text='...')
    label4.configure(text='...')
    label5.configure(text='...')
    label6.configure(text='...')
    getBtn.configure(state=NORMAL)
    resBtn.configure(state=DISABLED)


#add statements to nominate the relevant function to be called when each button is pressed by the user
getBtn.configure(command=pick)
resBtn.configure(command=reset)


# sustain window
window.mainloop()
