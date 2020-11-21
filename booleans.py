# compares the two values, and prints either true or false
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

# as a conditional in an lf statement
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# bool() allow you to evaluate any value

# most values are true when content is present
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# some values are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})