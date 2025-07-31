#Operator       Comparative test
# ==             Equality
# !=             inequality
# >              Greater than
# <              Less than
# >=             Greater then or equal
# <=             less than or equal

#unicode value of string compared numerically to achieve comparison result: A = 65 , a = 97

nil = 0
num = 0
top = 1
cap = 'A'
low = 'a'

print('Equality :\t\t' , nil , '==' , num , nil == num )    # \t adds invisible tab space
print('Equality :\t\t' , cap , '==' , low , cap == low )

print('Inequality :\t\t' , nil , '!=' , top , nil != top )
print('Inequality :\t\t' , cap , '!=' , low , cap != low )

print('Greater :\t\t' , nil , '>' , top , nil > top )
print('Lesser :\t\t' , nil , '<' , top, nil < top )

print('More or Equal :\t\t' , nil , '>=' , num , nil >= num )
print('Less or Equal :\t\t' , top, '<=', num , top <= num )

#unicode value of string compared numerically to achieve comparison result: A = 65 , a = 97
print('More or Equal :\t\t' , cap , '>=' , low , cap >= low )
print('Less or Equal :\t\t' , cap, '<=', low , cap <= low )