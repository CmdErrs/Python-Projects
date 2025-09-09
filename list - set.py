#Setting lists
# A set os a list of unique values, mutible, access to powerful functions
# example_set = { 'Alpha' , 'Bravo' , 'Charlie' }

#elements can not be referenced by square brackets []

#Set items must be unique
# list() function may not place element values in the same order as they appear in set

#Set Method             Description
#set.add(x)             Adds item x to set
#set.update(x,y,z)      Adds multiple items to the set
#set.copy()             Returns a copy of the set
#set.pop()              Removes one random item from the set
#set.discard(x)         Removes item x if found in set
#set1.intersection(set2)returns items that appear in both sets
#set1.difference(set2)  returns items in set1 but not in set2

#len()
#type()
# 'value' in set        look for value in set                 
#list()                 convert to regular list, enabling element access

party_goers = { 'Andrew' , 'Barbara' , 'Carole' , 'David' , 'Mark' }
print( 'party_goers:' , type(party_goers))

print( 'Did David go to the party?' , 'David' in party_goers )
print( 'Did Kelly go to the party?' , 'Kelly' in party_goers )

students = { 'Andrew' , 'Kelly' , 'Lynn' , 'David', 'Mark' }

#initialise set with common values
commons = party_goers.intersection( students )

#initialise a regular list of the common values, so the element values can be individually accessed
party_students = list( commons )
#print(party_students)

print( 'Students at the party:' , party_students )
print( 'First student at the party:' , party_students[0] )

print( type(commons) )
print( len(party_students) )