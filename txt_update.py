#   use 'with' when working with file objects to group file operational statements within a block, ensures file is closed after operation end


text = 'The political slogan "Workers Of The World Unite!" \n'
text += 'is from The Communist Manifesto.'

#   write string to file and display file status
with open('update.txt', 'w') as file:
    file.write(text)
    print('\nFile Now closed?:', file.closed)

print('File now closed?:', file.closed)

file = open('update.txt', 'r')
for line in file:
    print(line, end='')
