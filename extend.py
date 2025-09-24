a = [10, 23, 39, 40, 50, 60, 70]
b = [477, 588, 786]

print("Using extend() to add elements from one list to another:")
a.extend(b)
print(a)

print("+= operator to extend a list:")
a += [80, 90]
print(a)

print("Using Slicing to extend a list:")
a[len(a):] = [100, 110]
print(a)

print("Using  itertools.chain() to extend a list:")
import itertools
c = [111, 222]
a.extend(itertools.chain(c))
print(a)