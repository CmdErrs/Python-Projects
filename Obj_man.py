# create a class file that also declares a derived class with a method that once again overrides the same method in the base class
from Obj_person import *
class Man(Person):
    '''A derived class to define Man properties.'''
    def speak(self, msg):
        print(self.name, ':\n\tHello!', msg)