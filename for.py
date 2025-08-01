# for loop doesnt allow step size and end to be specified

# range() can generate a sequence that decreases, counting down, as well as those that count upward
# range(5) iterates through -> 0,1,2,3,4 elements
# range(1,5) interates starting at element -> 1,2,3,4
# range(1,14,4) step by 4 -> 1,5,9,13



chars = [ 'A' , 'B' , 'C' , 'D' ] #list
fruit = ( 'Apple' , 'Banana' , 'Cherry' , 'Duran' ) #tuple - immutable
info = { 'name' : 'Mike' , 'ref' : 'Python' , 'sys' : 'Win' , 'new' : 'set item' } #set - unique elements & functions

print( 'Elements: ' , end = '' )           # end = '' keeps next line with previous
for elements in chars:
    print( elements , end = '')            # end = '' keeps all elements on same line

print( '\nEnumerated:\t' , end = '')
for item in enumerate( chars ) :             # enumerate() displays each elements index number and its value (0, 'A')(1, 'B')(2, 'C')(3, 'D')
    print( item , end = '' )

print( '\nZipped: \t' , end = '' )          
for item in zip( chars, fruit , info ) :   # zip() returns same index number value for each list together. ('A', 'Apple', 'name')('B', 'Banana', 'ref')('C', 'Cherry', 'sys')
    print( item, end = '' )

print( '\nPaired:' )
for key , value in info.items() :          # when looping through a dictionary, to display each key and its value use the dictionary items() method, and specify key name and value.
    print( key , '=' , value )


