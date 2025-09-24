a = [11,22,33,44,55]

#using index
print("Using index:")
print (a[2])
print (a[-2])

#using slicing
print("Using slicing:")
print (a[1:3])
print (a[1:5:2])
print (a[:3])
print (a[::2])

#list comprehension
print("List comprehension:")
b=[item for item in a ]
print (b)

c=[item * 2 for item in a if item % 2==0]
print(c)

#using loop
print("Using loop:")
for item in a:
    item > 20
    print(item)



