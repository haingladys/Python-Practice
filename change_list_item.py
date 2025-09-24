a = [11, 22, 33, 44, 55]

# changing list items using index
print("Changing list items using index:")
a[1] = 27  
print(a)

a[-1] = 60
print(a)

a[0] = a[0] + 5
print(a)

#changing list items using slicing
print("Changing list items using slicing:")
a[1:3] = [20, 30]
print(a)
a[2:4] = [40, 50,]
print(a)


#using list comprehension to change items
print("Using list comprehension to change items:")
a = [item * 2 for item in a]
print(a)

#using loop to change items
print("Using loop to change items:")   
for i in range(len(a)):
    a[i] = a[i] + 3
    print(a)

for i , item in  enumerate(a):
    a[i] = item - 2
    print(a)


#using map() to change items
print("Using map() to change items:")
a = list(map(lambda x: x * 3, a))
print(a)


