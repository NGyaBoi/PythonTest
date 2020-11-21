alist = ["apple", "banana", "cherry"]
print(alist)

# prints the second item
print(alist[1])

# prints the last item
print(alist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])    # prints all items from 2 to 5, noted that 5 is not included
print(thislist[:4])     # prints all items from 0 to 4, noted that 4 is not included
print(thislist[2:])     # prints all items from 2 to end
print(thislist[-4:-1])  # prints all items from -4 to -1, noted that -1 is not included

alist[1] = "blackcurrant"   # changes the second item
print(alist)

# checks if a string is in a list
if "apple" in alist:
    print("Yes, 'apple' in in 'alist'")

alist.append("orange")
print(alist)

alist.insert(1, "mango")
print(alist)

alist.remove("banana")
print(alist)

alist.pop()
print(alist)

del alist[0]
print(alist)

alist.clear()
print(alist)

mylist = alist.copy()
del alist

# combine two lists into one
biglist = mylist + thelist
print(biglist)