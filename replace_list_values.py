a = [10, 20, 30, 40, 50]

# changing list items using index
print("Changing list items using index:")
a[2] = 57
print(a)

#using lamda function to change items
print("Using lambda function to change items:")
a = list(map(lambda x: x + 5 if x == 40 else x, a))
print(a)

#using loop to change items
print("Using loop to change items:")
for i in range(len(a)):
    if(a[i]==50):
        a[i] = 100
    print(a)

#using while loop to change items
print("Using while loop to change items:")
i = 0
while(i < len(a)):
    if(a[i]==20):
        a[i] = 1
    i += 1
    print(a)
