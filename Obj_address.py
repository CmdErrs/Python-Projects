
# Attributes of a class instance can be added, modified, or removed at any time using dot notation to address the attribute
# Making a statement that assigns a value to an attribute will update the value contained within an existing attribute, or create a new attribute of the specified name containing the assigned value:
#   instance-name.attribute-name = value
#   del instance-name.attribute-name

# Alternatively used Python built-on functions
#   getattr(instance-name, 'attribute-name') - return the attribute value of the class instance
#   hasattr(instance-name, 'attribute-name') - return True if attribute-name exists
#   setattr(instance-name, 'attribute-name') - update existing attribute value or create new attribute in the instance
#   delattr(instance-name, 'attribute-name') - remove the attribute from the instance

# import features from Obj_bird class
from Obj_bird import *

# create instance of class, then add a new attribute with an assigned value using dot notation
chick = Bird('Cheep, cheep!')
chick.age = '1 week'

# Display the values in both variable attributes
print('\nChick Says:', chick.talk())
print('\nChick Age:', chick.age)

# modify the new attribute using dot notation and display its new value
chick.age = '2 weeks'
print('\nChick now:', chick.age)

# modify new attribute using built-in function
setattr(chick, 'age', '3 weeks')
print('\nChick now:', chick.age)

# display a list of all non-private instance attributes and their respective values using a built-in function
print('\nChick attributes...')
for attrib in dir(chick) :
    if attrib[0] != '_':
        print(attrib, ':', getattr(chick, attrib))

# Remove new attribute and confirm its removal using a built in function
delattr(chick, 'age')
print('\nChick age Attribute?', hasattr(chick, 'age'))
