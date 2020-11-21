# INDEXING

# [num] returns the character at specified position
a = "Hello World"
print(a[1])

b = "Hello World"
print(b[2:5])

c = "Hello World"
print(c[-5:-2])

# returns the length of string
print(len(a))

# STRING METHODS

a = "  Hello, World  "
print(a.strip()) # returns string without whitespace

b = "Hello, World"
print(a.lower()) # returns string in lower case

c = "Hello, World"
print(c.upper()) # returns string in upper case

d = "Hello, World"
print(d.replace("H", "J")) # replaces string with another

e = "Hello, World"
print(e.split(",")) # splits string into substrings

# CHECK STRING

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)

# CONCATENATION

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# FORMATTING

# {} acts as a placeholder for a variable
# format will take the placeholder and format it to the parent variable
age = 36
txt = "My name is John, I am {}"
print(txt.format(age))

quantity = 3
itemnum = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemnum, price))

# escape character \" allow you to use double quotes when normally couldn't
txt = "We are so-called \"Viking\" from the north."

# other escape characters include:
# \'    single quote
# \\    backslash
# \n    new line
# \r    carriage return
# \t    tab
# \b    backspace
# \f    form feed
# \ooo  octo value
# \xhh  hex value