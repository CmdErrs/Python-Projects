from Obj_man import *
from Obj_hombre import *

# create an instance of each derived class, initialising the 'name' variable attribute
guy_1 = Man('Richard')
guy_2 = Hombre('Ricardo')

#now, call the overriding methods of eah derived class, assigning different values to the 'msg' parameter
guy_1.speak('It\'s a beautiful evening.\n')
guy_2.speak('Es una tarde hermosa.\n')

# explicitly call the base class method, passing a reference to each derived class - but none for the 'msg' variable so its default values will be used
Person.speak(guy_1)
Person.speak(guy_2)

# Method declaration in the derived class must exactly match that in the base class to override it