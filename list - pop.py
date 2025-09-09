#Changing Lists
# list.append(x)    adds item x to the end of the list
# list.extend(L)    adds all items in the list L to the end of the list
# list.insert(i,x)  inserts item x at the index position i
# list.remove(x)    removes first item x from the list
# list.pop(i)       removes item at index position i and returns it
# list.index(x)     returns the index position in the list of first item x
# list.count(x)     returns the number of times x element appears in the list
# list.sort()       sorts all list items, in place, numerically first then alphabetically (1,2,3,A,B,C)
# list.reverse()    reverses all list items, in place

# int(s)            returns numeric version of string

# len(L) returns the total number of elements in the list L. as with index() ,count()returns numeric value, cannot be concatenated to text for output. 

# str(n) returns string value of numeric n

basket = [ 'Apple' , 'bun' , 'cola' ]
crate = [ 'Egg' , 'Fig' , 'Grape' ]

print( 'Basket list:' , basket)
print( 'Basket Elements:' , len(basket))

basket.append( 'Damson' )
print( 'Appended:' , basket )
print( 'Last item removed:' , basket.pop())
print( 'new basket list:' , basket )

basket.extend( crate )
print( 'Extended list:' , basket )
del basket[1]
print( 'item bun removed' , basket )
del basket[1:3]
print( 'slice -cola and egg - removed:' , basket )

print(basket.count('Apple'))
#print(str(5))