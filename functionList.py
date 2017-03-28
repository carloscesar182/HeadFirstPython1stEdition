import nester

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

cast = ["Palin", "Cleese", "Idle", "Jones", "Gilliam", "Chapman"]

names = ["John", "Eric", ["Cleese", "Idle"], "Michael", ["Palin"]]

nester.print_lol(movies, True)  # Invoke the function 'print_lol' inside the 'nester.py' module giving a second argument
nester.print_lol(names)  # Invoke the function 'print_lol' inside the 'nester.py' module without a second argument
