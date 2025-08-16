# dict

# Variable - stores a single value
# List - stores multiple values in an ordered index [['a','b','c'],[1,2,3]]
# Tuple - stores multiple fixed values in a sequence ('a','b','c')
# Set - Store multiple unique values in an unordered collection {'a','b','c'}
# Dictionary - stores multuple unordered key:value pairs {:}


# In other programming languages a list is often called an "array" and a diction may be an "associative array"

info = {'name': 'Bob', 'ref': 'Python', 'sys': 'Win'}
print('Info:', type(info))
print('Dictionary:', info)

print('\nReference:', info['ref'])
print('\nKeys:', info.keys())

del info['name']                                   # Delete element 'name'
# append element 'user' = 'tom'
info['user'] = 'Tom'
print('\nDictionary:', info)

# Return boolean value if key is available
print('\nIs There a name Key?:', 'ref' in info)
