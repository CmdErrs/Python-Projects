#while
# += is short hand for ( i = i + 1 )



i = 1
while i < 4 :
    print( 'Outer Loop iteration:' , i )
    i += 1
    j = 1
    while j < 4 :
        print( '\tInner Loop Iteration' , j )
        j += 1



# Fibonacci loop
a = b = 1
while b < 100:
    print( b )
    a , b = b , a + b

