#   capitalize()        uppercase first letter
#   title()             change all first letters to uppercase
#   upper()             Change the case of all letters to uppercase
#   lower()             change all to lowercase
#   swapcase()          
#   join(seq)           merge string into iterable sequence seq
#   lstrip()            remove leading whitespace
#   rstrip()            remove trailing whitespace
#   strip()             remove both, trailing and leading whitespace
#   replace(old,new)    replace all occurances of old, with new
#   ljust(w,c)          pad string to right to total column width w with character c
#   rjust(w,c)          lef pad
#   center(w,c)         pad string each side to total colum width w with character c (default is space)
#   count(sub)          return the number of occurances of sub
#   find(sub)           return the index number of the first occurance of sun, or return -1 if not found
#   startswith(sub)     return True if sub is found at the start
#   endswith(sub)       True if sub is found at end
#   isalpha()           returns True if all characters are letters only
#   isnumeric()         returns True if all characters are numeric only
#   isalnum()           Returns True if all are alphanumeric only
#   islower()           returns True if string characters are lowercase
#   isupper()           True if all uppercase
#   istitle()           True if all first letters are uppercase

#   isspace()           returns true if string only contains only whitespace
#   isdigit()           returns true if string only contains digits
#   isdecimal()         eturns true if string only contains decimals


string = 'coding for beginners in easy steps'

print('\nAll letters:\t', string.isalpha())

print('\nAll numbers:\t', string.isnumeric())
print('\nAll letters or numbers:\t', string.isalnum()) #space character is not alphanumeric

# print('\nCapitalised:\t', string.capitalize())
# print('\nTitles:\t\t', string.title())
# print('\nCentered:\t', string.center(30, '*'))

# print('\nUppercase:\t', string.upper())

# string = 'Coding for beginners in easy steps'
# print('\nLowercase:\t', string.lower())
# print('\nSwapCase:\t', string.swapcase())
# string = 'coding for beginners in easy steps'
# print('\nJoined:\t\t', string.join('**'))

# print('\nJustified:\t\t', string.rjust(10, '*'))
# print('\nReplaced:\t', string.replace('s', '*'))