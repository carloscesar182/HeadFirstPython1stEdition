# It is a list within a list within a list
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

for each_item in movies:  # Processing the movies list
    if isinstance(each_item, list):  # To check if the current item is a list
        for nested_item in each_item:  # If it is a list, use another 'for' loop to process the nested list
            if isinstance(nested_item, list):  # It will check inside of your first list if have another ones
                for deeper_item in nested_item:  # It is going to make you crazy!!!
                    if isinstance(deeper_item, list):
                        for deepest_item in deeper_item:
                            print(deepest_item)
                    else:
                        print(deeper_item)
            else:
                print(nested_item)  # If the current item of the enclosing list isn´t a list, display it on screen
    else:
        print(each_item)
