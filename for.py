
chars = [ 'A' , 'B' , 'C' ] #list
fruit = ( 'Apple' , 'Banana' , 'Cherry' ) #tuple - immutable
info = { 'name' : 'Mike' , 'ref' : 'Python' , 'sys' : 'Win' } #set - unique elements & functions

print( 'Elements: \t' , end = '' )
for item in chars:
    print( item , end = '')

print( '\nEnumerated:\t' , end = '')
for item in enumerate( chars ) :
    print( item , end = '' )

print( '\nZipped: \t' , end = '' )
for item in zip( chars, fruit ) :
    print( item, end = '' )

print( '\nPaired:' )
for key , value in info.items() :
    print( key , '=' , value )


