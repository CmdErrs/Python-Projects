'''
An excerpt from the Ballad of Reading Gaol.
'''
poem = 'I never saw a man who looked\n'
poem += 'With such a wistful eye\n'
poem += 'Upon that little tent of blue\n'
poem += 'Which prisoners call the sky\n'

#   open new file names poem.txt & write to it
file = open('poem.txt', 'w')

#   write string to file and close file
file.write(poem)
file.close()

#   open file with read access
file = open('poem.txt', 'r')

# #   Display contents of file, then close file
# for line in file:
#     print(line, end='')
# file.close()

#   append citation to end of file
file = open('poem.txt', 'a')
file.write('(Oscar Wilde)')
# file.close
file = open('poem.txt', 'r')
print(file.readlines(-1))