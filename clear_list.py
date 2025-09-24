print("using clear() to remove all items from the list:")
movies = [3, "kuruvi", "me before you", "atonement", "intern"]
print("Original List:", movies)
movies.clear()
print("List after clearing:", movies)

print("Reassigning to an Empty List")
numbers = [1, 2, 3, 4, 5]
print("Original List:", numbers)
numbers = []
print("List after reassigning to empty list:", numbers)

print("using del to delete all items from the list:")
books = ["harry potter", "atomic habits", "the power of your subconscious mind"]
del books[:]
print("List after deleting all items:", books)

print("using loop to remove all items from the list:")
fruits = ["apple", "banana", "cherry", "date"]
print("Original List:", fruits)     
while fruits:
    fruits.pop()
    print(fruits)

