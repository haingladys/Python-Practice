a = [10, 20, 30, 40, 50, 60, 70]

# Use append() to add the element 8 to the end of the list
print("Using append() to add elements:")
a.append(80)
print(a)

print("Appending different data types:")
a.append("ninety")
print(a)

# Use append() to add a list to the end of the list
print("Appending a list to the end of the list:")
a.append([100, 110])
print(a)

#appending using loop
print("Appending using loop:")
for i in range(5):
    a.append(i)
    print(a)

