# Create a class file that declares a derived class with a method to return manipulated class variable values
from Obj_polygon import *

class Triangle(Polygon):
    def area(self):
            return(self.width * self.height)/2