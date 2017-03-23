movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


def print_lol(the_list):
    for each_item in the_list:  # Process the provided list with a 'for' loop
        if isinstance(each_item, list):  # If the item is being processed is itself a list, invoke the function
            print_lol(each_item)
        else:
            print(each_item)  # If the item is being processed ISN´T a list, display the item on screen

print_lol(movies)  # Invoke the function
