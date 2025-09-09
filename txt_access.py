
#   r   Open exisitng file to read
#   w   open an existing files to write. creates new file if none exists, or opens an existing files and discards all previous contents
#   a   append tent.opens or create a text file for writing at the end of the file
#   r+  as for r but the file can also be written
#   w+  as for w but the file can also be read
#   a+  as for a but the file can also be read
#       Where the mode includes b after any modes above, the operation related to a binary file rather than a text file - for example rb or w+b

#   readlines() function returns a list of all the lies
#   writelines() function writes list items into a file

file = open('example.txt', 'w')

print('File Name:' , file.name)
print('file Open Mode:', file.mode)

print('Readable:', file.readable())
print('Writable:', file.writable())