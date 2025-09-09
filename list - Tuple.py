
#tuples are 
#   immutable, can contain not unique elements
#   Tuple packing is defined using parentheses: (element1, element2)    colours_tuple = ( 'Red' , 'Blue' , 'Green', 'Red' )
#   Sequence unpacking -stored values assigned to individual values     a, b, c, d = colours_tuple
#   element access                                                      tuple[0]



# type(), and len() functions work on tuples

days = ( 'Mon' , 'Tue' , 'Wed' , 'Thu' , 'Fri' , 'Sat' , 'Sun' )
print( 'days:' , type( days))

print( 'Days of the week:' , days )
print( 'No. of days in week:' , len(days))
print( 'Start day of week:' , days[0])

user = ( 'John' , 'Doe' , 'Paris' , '555-1324' )
print( 'Name:' , user[0] , user[1])
print('Phone Number:' , user[3])

