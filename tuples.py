# a tuple is a collection that is ordered AND unchangeable

thistuple = ("apple", "banana", "cherry")
print(thistuple)

print(thistuple[1])     # prints banana
print(thistuple[-1])    # prints cherry

atuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(atuple[2:5])      # prints the 3rd, 4th, and 5th items
print(atuple[-4:-1])    # prints 4th, 5th, 6th items

# changing tuple values
x = ("jelly", "creme", "sponge")
y = list(x)
y[1] = "mousse"
x = tuple(y)
print(x)

# looping through a tuple
for x in thistuple:
    print(x)

# check if item exists
if "apple" in thistuple:
    print("Yes, 'apple' is in thistuple.")

# tuple length
print(len(thistuple))

# 'del' can delete the tuple entirely
del atuple
print(atuple)