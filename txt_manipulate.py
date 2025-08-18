
#   +       Concatenate
#   *       repeat - multiply the string
#   []      slice - select a character at the specified index position
#   [:]     range slice
#   in      membership inclusive - returns true if character exists in string. Case sensitive
#   not in  exclusive - returns True if char doesn't exist in string
#   r/R     Raw string - suppress meaning of escapte characters
#   ''' ''' docstring - descript a modules, function, class or method

def display(s):
    '''Display an argument value.'''
    print(s)

display(display.__doc__)

display(r'C:\Program Files')

display('\nHello' + 'Python')

display('Python is easy steeeeeeps\n'[7:])

display( 'P' in 'Python')
display( 'p' in 'Python')