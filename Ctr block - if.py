# if: elif: else: equivalet to switch or case found in other languages


num = int(input('Please Enter A Number: '))

if num > 5:
    print('Number Exceeds 5')
elif num < 5:
    print('Number is Less Than 5')
else:
    print('Number is 5')

if num > 7 and num < 9:
    print('Number is 8')
if num == 1 or num == 3:
    print('Number is 1 or 3')
# if num == 2 or num == 4:
#     print('Number is 2 or 4')
# if num == 5:
#     print('Number is ', num)
