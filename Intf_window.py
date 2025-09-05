# tkinter
# geometry managers:
# pack(), place(), grid().

# there can only be one call to the Tk() constructor and it must be at the start of the programming code.

# start a new program with a statement to make the 'tkinter' module GUI methods and attributes available
from tkinter import *

# next add a statement to call upon a constructor to create a Window object
window = Tk()

# add a statement to specify a title for this window
window.title('Label Example')

# add statement to call upon a constructor to create a Label object
label = Label(window, text = 'Hello World!')

# use the packer to add the label to the window with both horizontal and vertical padding for positioning
label.pack(padx = 200, pady = 50)

# Finally add the mandatory statement to maintain the window by capturing events
window.mainloop
