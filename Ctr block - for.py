# for loop doesnt allow step size and end to be specified

# range() can generate a sequence that decreases, counting down, as well as those that count upward
# range(5) iterates through -> 0,1,2,3,4 elements
# range(1,5) interates starting at element -> 1,2,3,4
# range(1,14,4) step by 4 between 1-14 -> 1,5,9,13

# enumerate(list) displays each elements index number and it's value


# initialise a regular list, a fixed tuple, and an associative dictionary list
chars = ['A', 'B', 'C', 'D']  # list
fruit = ('Apple', 'Banana', 'Cherry', 'Duran')  # tuple - immutable
# set/dictionary - unique elements & functions
info = {'name': 'Mike', 'ref': 'Python', 'sys': 'Win', 'new': 'set item'}

# Display all list element values in variable 'chars'
# end = '' keeps next line with previous
print('Elements: \t', end='')
for elements in chars:
    print(elements, end='')
    # Elements:       ABCD


print('\nEnumerated:\t', end='')
# enumerate() displays each elements index number and its value (0, 'A')(1, 'B')(2, 'C')(3, 'D')
for item in enumerate(chars):
    print(item, end='')
    # Enumerated:     (0, 'A')(1, 'B')(2, 'C')(3, 'D')


print('\nZipped: \t', end='')
# zip() returns same index number value for multiple lists, grouped by index number. ('A', 'Apple', 'name')('B', 'Banana', 'ref')('C', 'Cherry', 'sys')
for item in zip(chars, fruit, info):
    print(item, end='')
    # Zipped:         ('A', 'Apple', 'name')('B', 'Banana', 'ref')('C', 'Cherry', 'sys')('D', 'Duran', 'new')


print('\nPaired:')
# loops through 'info' set and prints each key and their associated value.
for key, value in info.items():
    print(key, '=', value)
    # Paired:
    # name = Mike
    # ref = Python
    # sys = Win
    # new = set item
