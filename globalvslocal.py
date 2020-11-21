# variables created outside of functions are global
# global variables can be used everywhere
# variables of the same name inside a function are local
# locals override globals just for that function

x = "awesome"

def myfunc():
    x = "great"
    print("Python is " + x)

# "global" keyword to make local variable global
# if same name, it will override previous global variable
def afunc():
    global y
    y = "nice"
    print("Python is " + y)

myfunc()
afunc()
print("Python is " + x)