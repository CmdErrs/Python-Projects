#   use 'with' when working with file objects to group file operational statements within a block, ensures file is closed after operation end

#   assign string value to variable 'text'
text = 'The political slogan "Workers Of The World Unite!" \n'
text += 'is from The Communist Manifesto.'

#   write string to file and display file status within 'with block'
with open('update.txt', 'w') as file:
    file.write(text)
    print('\nFile Now closed?:', file.closed)

# new file status outside of with block
print('File now closed?:', file.closed)

# reopen file and confirm written contents
with open('update.txt', 'r+') as file:
    text = file.read()
    print('\nString:', text)

    #   display current file position, then reposition and display new position
    print('\nPosition In File Now:', file.tell())
    position = file.seek(33)
    print('Position In File Now:', file.tell())

    #overwrite text at current position
    
    file.write('All Lands')
    # print('Position In File Now:', file.tell())
    # text = file.read()
    # print('\nString:', text)
    # print(text)
    
    # reposition once more and overwrite the tet from new position
    file.seek(61)
    file.write('the tombstone of Karl Marx')

    file.seek(0)
    text = file.read()
    print('\nString:', text)
#     # just testing
#     print('File now closed?:', file.closed)
# # just testing
# print('File now closed?:', file.closed)

    #overwrite text in current file position
    # print(text)