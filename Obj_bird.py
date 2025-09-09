#   Class = blueprint with a set of properties that characterise an object

#   Class contains functions and variables to characterise the object

#   properties of a class are referred to as it;s data 'members'

#   Class function members are known as 'methods'
#   Class variable members are known as 'attributes' (declared within a class structure but outside any method definitions)

#   class members can be referenced throughout the program using dot notation, suffixing the member name after the class name. class-name.method-name() or class-name.attribute-name.

# class ClassName:                           #Class names begin with uppercase, object names with lowercase
#   '''class-documentation-string'''
#   class-variable-declarations
#   class-method-definitions


#   Variables declared within the class method are only available locally within the method in which they are declared - they cannot be directly referenced outside the class structure.
#   Typically, variables within class method definitions contain data passed by the caller when an instance copy of the class is created. As this data is only available locally for internal use, it is effectively hidden from the rest of the program. This technique of data 'encapsulation' ensures that data is securely stored within the class structure and is the first principle of Object Oriented Programming OOP.
#   All properties of a class are referenced internally by the dot notation prefix self. self.attribute
#   All method definitions in a class must have self as their first parameter - method 'talk' is 'talk(self)'


#   when a class instance is created, a special __init__(self) method is automatically called. Subsequent parameters can be added in its parentheses if values are to be passed to initialise its attributes.
#   A complete Python class declaration could look like this:
class Critter:
    '''A base class for all critter properties'''
    count = 0  # count variable is a class variable whose integer value gets shared among all instances of this class - referenced as Critter.count from inside or outside class.

    def __init__(self, chat):  # __init__() is the first initialisation method that is automatically called when an instance of the class is created
        self.sound = chat  # the __init__() method initialises an variable 'sound', with a value passed from the 'chat' parameter, and increments the value of the 'count' class variable whenever an instance of this class is created.
        Critter.count += 1

    # the second method talk() is declared like a regular function except the first parameter is 'self', which is automatically incorporated - no value needs to be passed from the caller.
    def talk(self):
        # the talk() method in this case simply returns the value encapsulated in the 'sound' variable.
        return self.sound

    #   The class documentation string can be accessed ia the special __+doc__ docstring attribute with Classname.__doc__

    #   The class instance object returned by the constructor is assigned to a variable using the syntax 'instance-name = ClassName(args)
    #   A class can be defined as a Python module file so it can be imported where instance objects can be created from the 'master' class blueprint.

    # Start a new class file by declaring a new class with a descriptive document string.
class Bird:
    '''A class to define bird properties'''
# Add indented statement to declare and initialise a class variable attribute with an integer zero value
    count = 0
    
# define the initialiser class method to initialise an variable and to increment the class variable
    def __init__(self, chat):
        self.sound = chat
        Bird.count += 1

# add a class method to return the value of the variable when called.
    def talk(self):
        return self.sound
# print(Bird.__doc__)
# print(Critter.__doc__)
