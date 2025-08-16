
# declare 'copy_sort' function to recieve a list reference 'array' as input and return a sorted copy as output
def copy_sort(array):
    copy = array[:]  # variable copy declared as array list
    sorted_copy = []  # variable sorted_copy declared as empty list
    # Algorithmm sequence to be added here
    while len(copy) > 0:  # continue if length of copy elements are > 0
        minimum = 0  # variable minimum assigned 0 value
        # variable element, list elements from start to last copy element
        for element in range(0, len(copy)):
            if copy[element] < copy[minimum]:
                minimum = element
        print('\tRemoving', copy[minimum],
              'from', copy)
        sorted_copy.append(copy.pop(minimum))
    return sorted_copy


array = [5, 3, 1, 2, 6, 4]
print('Copy Sort...\nArray :', array)
print('Copy :', copy_sort(array))
print('Array:', array)
