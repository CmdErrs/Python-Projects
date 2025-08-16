# Break

# for i in range( 1 , 4 ) :
#     for j in range( 1 , 4 ) :
#        print( 'Running i=' , i , 'j=' , j )


# # add break @ i=2

# for i in range( 1 , 4 ) :
#   for j in range( 1 , 4 ) :
#     if i == 2 and j == 1 :
#         print( 'Breaks inner loop at i=2 j=1' )
#         break                                         # break skips the remainder of loop @ i=2 j=1
#     print( 'Running i=' , i , 'j=' , j )

# add continue @ i=1 & j=1

# for i in range( 1 , 4 ) :
#   for j in range( 1 , 4 ) :
#     if i == 1 and j == 1 :
#         print( 'Continues inner loop at i=1 j=1' )
#         continue                                       # skips single iteration i=1 j=1
#     if i == 2 and j == 1 :
#         print( 'Breaks inner loop at i=2 j=1' )
#         break
#     print( 'Running i=' , i , 'j=' , j )


# swapping order of break & continue does not change output for this example
for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 2:
            print('Breaks inner loop at i=2 j=1')
            break
        if i == 1 and j == 1:
            print('Continues inner loop at i=1 j=1')
            continue                                       # skips iteration i=1 j=1

        print('Running i=', i, 'j=', j)
