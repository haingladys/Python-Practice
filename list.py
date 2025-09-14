
mylist = [12, "leopard", 9.0, True, [1, 2, 3]]

"""Indexing and slicing"""

print(mylist[0])
print(mylist[4])
print(mylist[-2])
print(mylist[1:3])
print(mylist[1:3:4])

"""Length"""

print(len(mylist))

"""Concatenation"""

print(mylist+["zebra"])

"""Repitition"""

print(mylist*2)

"""Append and Extend"""

mylist.append(False)
mylist.append(["lion","dove","cow"])
mylist.extend([97,"forest"])
print(mylist)

"""Insert"""

mylist.insert(3,10.30)
print(mylist)

"""Remove and Pop"""

mylist.remove("leopard")
print(mylist)
popped= mylist.pop(2)
print(popped)

"""update"""

mylist[2]="leopard"
print(mylist)

"""Iteration"""

for item in mylist:
  if isinstance(item,str):
    print(item.upper())
  elif isinstance(item,int):
    print(item*2)

for item in range(len(mylist)):
  print(f"Index {item}: {mylist[item]}")

for index, item in enumerate(mylist):
  print(f"Index {index}: {item}")

item = len(mylist)-1
while item >= 0:
  print(mylist[item])
  item =item - 1

"""List Comprehension"""

String_only=[item for item in mylist if isinstance(item,str) ]
print(String_only)
Even_Num=[item**2 for item in mylist if isinstance(item, (int, float)) and item%2==0]
print(Even_Num)

"""Filter"""

Float_only=list(filter(lambda item: isinstance(item, float), mylist))
print(Float_only)

num= [item for item in mylist if isinstance(item, (int, float))]
print(sum(num))
print(max(num))
print(min(num))
print(len(num))
print(avg:=sum(num)/len(num))