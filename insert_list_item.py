games = ["football","chess","tennis"]

print("Add elements at specific index:")
games.insert(1,"cricket")
print(games)

games.insert(0,"badminton")
print(games)

games.insert(-1,"hockey")
print(games)

print("insert before a specific item:")
index = games.index("tennis")
games.insert(index,"table tennis")
print(games)

print("Insert List in Another List")
indoor = ["carrom","ludo"]
games.insert(2,indoor)
print(games)
