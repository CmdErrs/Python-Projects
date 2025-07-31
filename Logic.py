#Operator        Operation
#and            Logical AND
#or             Logical OR
#not            Logical NOT

a = True
b = False

#AND evaluations are TRUE if BOTH are true
print('AND Logic:')
print('a and a =' , a and a ) #True
print('a and b =' , a and b ) #False
print('b and b =' , b and b ) #False

# OR evaluations are TRUE if EITHER are true
print('\nOR Logic:' )
print('a or a =' , a or a ) #True
print('a or b =' , a or b ) #True
print('b or b =' , b or b ) #False

# NOT evaluations flip the value, True become False, vice versa
print('\nNOT Logic:')
print('a -' , a , '\tnot a =' , not a ) #False
print('b =' , b , '\tnot b =' , not b ) #True
print('a -' , a , '\tnot b =' , not b ) #True

#boolean values can be represented numerically where True is 1 and False is 0