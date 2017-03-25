"""This is the 'nester.py' module, and it provides a function called
print_lol() which prints lists that may or may not include nested lists."""
def print_lol(the_list):
    """This function takes a positional argument called 'the_list', which is any
    Python list (of, possibly, nested lists). Each data item in the provided list
    is (recursively) printed on the screen on its own line."""
    for each_item in the_list:  # Process the provided list with a 'for' loop
        if isinstance(each_item, list):  # If the item is being processed is itself a list, invoke the function
            print_lol(each_item)
        else:
            print(each_item)  # If the item is being processed ISN´T a list, display the item on screen
