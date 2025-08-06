#Def.py

# def functionName() :
#     statements-to-be-executed
#     statements-to-be-executed

# variables created inside functions cannot be references from outside the function in which they have been created - LOCAL scope. Variables of same name can appear in different functions wihtout conflict.
# If global and local variable have the same name, LOCAL is used.

# nonlocal keyword creates variable that is not global, but appears in some out scope. used in nested functions when variable does not belong to the inner function, and is visible to the outer function


global_var = 1

def my_vars() :
    print( 'Global variable:' , global_var )
    local_var = 2
    print( 'Local variable:' , local_var )
    global inner_var                    # declaring inner_val as a global, to allow access outside the function
    inner_var = 3

my_vars()

print( 'Second Global:' , inner_var )