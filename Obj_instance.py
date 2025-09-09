# import bird class

from Obj_bird import *
print('\nClass Instance Of:\n', Bird.__doc__)

# add statement to create an instance of the class and pass a string argument value to its variable
polly = Bird('Squawk, squawk!')

# display variable value and call the class method to display the common class variable value
print('\nNumber of Birds:', Bird.count)
print('\nPolly Says:', polly.talk())

# create 2nd instance of the class passing different string argument value to it's variable
harry = Bird('Tweet, Tweet!')

# display variable value and call the class method to display the common class variable value
print('\nNumber of birds:', Bird.count)
print('Harry says:', harry.talk())