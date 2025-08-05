#dict

# Variable - stores a single value
# List - stores multiple values in an ordered index []
# Tuple - stores multiple fixed values in a sequence ()
# Set - Store multiple unique values in an unordered collection {}
# Dictionary - stores multuple unordered key:value pairs {}



info = { 'name' : 'Bob' , 'ref' : 'Python' , 'sys' : 'Win' }
print( 'Info:' , type( info ))
print( 'Dictionary:' , info )

print( '\nReference:' , info[ 'ref' ])
print( '\nKeys:' , info.keys())

del info[ 'name' ]                                   # Delete element 'name'
info[ 'user' ] = 'Tom'                               # append element 'user' = 'tom'
print( '\nDictionary:' , info )

print( '\nIs There a name Key?:' , 'ref' in info )  # Return boolean value if key is available