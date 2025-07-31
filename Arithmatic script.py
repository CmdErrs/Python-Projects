# Operator  Operation
#   +       Addition
#   -       Subtraction
#   *       Multiplication
#   /       Division
#   %       Modulus (remainder)
#   //      Floor division (removes decimal)
#   **      Exponent

#   sep=''  Removes spaces

a = 8
b = 2
print('Addition:\t' , a , '+' , b , '=' , a + b)
#print('Addition (sep):\t' , a , '+' , b , '=' , a + b, sep = '')
print('Subtraction:\t' , a , '-' , b , '=' , a - b)
print('Multiplication:\t' , a , 'x' , b , '=' , a * b)
print('division:\t' , a , '÷' , b , '=' , a / b)
print('Floor Division:\t', a , '÷' , b , '=' , a // b)
print('Remainder:\t', a , '%' , b , '=' , a % b)
print('Exponent:\t', a ,'²', '=' , a ** b , sep = '' )

#playing with sep = ''
print('Exponent wo/sep:\t', a ,'²', '=' , a ** b )
print('Exponent w r:\t', a ,'²', '=' , sep = '') , print(a ** b , end = '\r')

#new changes for VScode git