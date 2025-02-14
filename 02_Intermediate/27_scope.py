# scope = A variable is only available from inside the region it is created. This is called scope.
# scope resolution = Local < enclosed < global < built-in


# A variable created inside a function belongs to the local scope of that function, 
# and can only be used inside that function.
def myfunc1():
    x = 300
    print(x)

def myfunc2():
    x = 400
    print(x)

myfunc1()
myfunc2()

# As explained in the example above, the variable x is not available outside the function, 
# but it is available for any function inside the function:
def myfunc3():
    x = 300  # No local variable x ia available to inner func. So, inner function takes the enclosed var x in func 3
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc3()


# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
x = 500 # global variable (outside of any function, usually declared at the top)
def myfunc4():
    print(x)

myfunc4()

print(x)


# built-in scope example
from math import e

e = 3

def func5():
    print(e)  # prints the global value of var e and not the built in value. (LEGB)
