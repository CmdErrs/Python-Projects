#Def.py

# def functionName() :
#     statements-to-be-executed
#     statements-to-be-executed

# variables created inside functions cannot be references from outside the function in which they have been created - LOCAL scope. Variables of same name can appear in different functions wihtout conflict.
# If global and local variable have the same name, LOCAL is used.


# global_var = 1

# def my_vars() :
#     print( 'Global variable:' , global_var )
#     local_var = 2
#     print( 'Local variable:' , local_var )
#     global inner_var                    # declaring inner_val as a global, to allow access outside the function
#     inner_var = 3

# my_vars()

# print( 'Second Global:' , inner_var )



global_var = 1

def my_vars() :
    print( 'Global variable:' , global_var )
    global_var = 2
    print( 'Local variable:' , global_var )
    global inner_var                    # declaring inner_val as a global, to allow access outside the function
    inner_var = 3

my_vars()

print( 'Second Global:' , inner_var )