# This is a list
movies = ["The Holy Grail", 1975,  # Item 0
          "The life of Brian", 1979,  # Item 1
          "The meaning of Life", 1983]  # Item 2
print(movies[1])  # It will print only the item number 1
print(len(movies))  # It will print how many items your list have

movies.append("Lord of the Rings")  # It will append an item into your list
print(movies)

movies.pop(2)  # It will pop an item from your list
print(movies)

movies.extend(["Titanic", "Harry Potter"])  # It will add another items into your list
print(movies)

movies.remove("The Holy Grail")  # It will remove a specific item from your list
print(movies)

movies.insert(3, "Deadpool")  # It will insert a specific item in a specific slot into your list
print(movies)