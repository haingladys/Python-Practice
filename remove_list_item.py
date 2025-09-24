a = [111, 220, 340, 940, 550]

print("Using remove() to delete specific item:")
a.remove(111)
print(a)

print("Using pop() to remove item at specific index:")
val = a.pop(1)
print(a)
print("Removed Item:", val)

print("using del to remove item at specific index:")
del a[2]
print(a)

print("Using clear() to remove all items from the list:")
a.clear()
print(a)

