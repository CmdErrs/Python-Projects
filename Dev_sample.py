# to generate an integer within the range of 0 to 9: int(random.random()*10
# to generate a whole number within the range of 1 to 10: int(random.random()*10)+1

# to generate 6 unique random numbers within the range of 1 to 9: random.sample(range(10),6)
# to generate 6 unique numbers within the range of 1 to 10: random.sample(range(1,11),6)


from random import random, sample

# assign a random floating-point number to a variable then display it's value
num = random()
print('Random Float 0.0-1.0:', num)

# multiply the floating point number and cast it to become an integer, then display it's value
num = int(num*10)
print('Random integer 0-0:', num)


# add a loop to assign. multiple random integers to a list, then display the list items
nums = []; i=0
while i < 6:
    nums.append(int(random()*10)+1)
    i += 1

print('Random Multiple Integers 1 - 10:' , nums)


# assign multiple unique random integers to the list, then display the list items
nums = sample(range(1,60),6)
print('Random Integer Sample 1-59:', nums)