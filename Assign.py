# Operator  Example     Equivalent
# =          a = b       a = b
# +=         a += b      a = (a + b)
# -=         a -= b      a = (a - b)
# *=         a *= b      a = (a * b)
# /=         a /= b      a = (a / b)
# %=         a %= b      a = (a % b)
# //=        a //= b     a = (a // b)
# **=        a **= b     a = (a ** b)

# =     means assign, rather than 'equals'
# ==    compare operator
# \t    add tab space

a = 8
b = 4
print('Assign Values:\t\t' , 'a =' , a , '\t\tb =' , b )

a += b
print( 'Add & Assign:\t\t' , 'a =' , a , '\t(8 += 4)')

a -= b
print('Subtract & Assign:\t' , 'a =' , a , '\t\t(12 - 4)')

a *= b
print('Multiply & Assign:\t' , 'a =' , a , '\t(8 x 4)')

a /= b
print('Divide & Assign:\t' , 'a =' , a , '\t(32 ÷ 4)')

a %= b
print('Modulus & Assign:\t' , 'a =' , a , '\t(8 % 4)')