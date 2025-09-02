from Obj_duck import *
from Obj_mouse import *

# define a function that accepts any sing object as it's parameter and attempts to call methods of that object
def describe(object):
    object.talk()
    object.coat()


# create an instance object of each class
dolly = Duck()
monty = Mouse()

# add statements to call the function and pass each instance object to it as an argument
describe(dolly)
describe(monty)

#a class can have only one method with a given name- method overloading is not supported in Python                                             