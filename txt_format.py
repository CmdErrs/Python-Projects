
#   %d  decimal integer
#   %c  character
#   %f  floating point number


snack = '{} and {} with {}'.format('Burger', 'fries', 'pineapple')

print(snack)

print('\nReplaced:', snack, '\n')

snack = '{1} and {2}'.format('Fish', 'chips', 'pineapple')

print('\nReplaced:', snack, '\n')

snack = '%s and %s' % ('Milk', 'Cookies')
print('\nSubstituted:', snack,'\n' )