#raise

# NameError = Variable not found
# IndexError = invalied list index
# ValueError = inappropriate value from operation or function

# statements in the try block are all executed unless and until an exception occurs

# title = 'Coding for Beginners in easy steps'
# try :
#     print( titel )
# except NameError as msg1 :                           # When NameError appears = store default return message as variable 'msg1'
#     print( msg1 )



# title = 'Coding for Beginners in easy steps'
# try :
#     print( titel )
# except ( NameError , IndexError ) as msg2 :          # When multiple exceptions appear = store default return value as variable 'msg2'
#     print( msg2 )
    


day = 33
try :
    if day > 31 :
        raise ValueError( 'Invalid Day Number' )        # specifies ValueError to be given custom value of 'Invalid Day Number'
except ValueError as msg :                              # create variable msg = ValueError
    print( 'The Program found An' , msg )
finally :
          print( 'But Today is Beautiful Anyway.' )
