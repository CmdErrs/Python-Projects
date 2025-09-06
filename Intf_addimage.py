from tkinter import *
window=Tk()
window.title('Image Example')

# create an image object from a local image file
img = PhotoImage(file='python.gif')


# create a Label object to display the image above a coloured background
label = Label(window, image=img, bg='magenta')


# create a half-size Image object from the first Image object
small_img = PhotoImage.subsample(img, x=2,y=2)


# create a button to display the small image
btn=Button(window, image=small_img)


# create a text field and embed the small image, then insert some text after it
txt=Text(window, width=25, height=7)
txt.image_create('1.0', image=small_img)
txt.insert('1.1', 'Python Fun!')


# create a canvas and paint the small image above a coloured background, then paint a diagonal line over the top of it.
can = \
Canvas(window, width=100, height=100, bg='pink')
can.create_image((50,50), image=small_img)
can.create_line(0,0,100,100,width=25, fill='magenta')


# add widgets to the window
label.pack(side=TOP)
btn.pack(side=LEFT, padx=10)
txt.pack(side=LEFT)
can.pack(side=LEFT, padx=10)

window.mainloop()

         