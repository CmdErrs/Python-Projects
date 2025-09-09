# create a new file that delcares a base class with an initialiser method to set a variable and a second method to display that variable value
class Person:
    '''A base class to define Person properties'''
    def __init__(self, name):
        self.name = name

    def speak(self, msg = '(Calling The Base Class)'):
        print(self.name, msg)
              