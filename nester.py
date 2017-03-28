"""This is the 'nester.py' module, and it provides a function called
print_lol() which prints lists that may or may not include nested lists."""
def print_lol(the_list, level=0):
    """This function takes a positional argument called 'the_list', which is any
    Python list (of, possibly, nested lists). Each data item in the provided list
    is (recursively) printed on the screen on its own line.
    A second argument called 'level' is used to insert tab-stops and it have a default value fixed and it made him
    as an OPTIONAL argument"""

    for each_item in the_list:  # Process the provided list with a 'for' loop
        if isinstance(each_item, list):  # If the item is being processed is itself a list, invoke the function
            print_lol(each_item, level+1)  # Give the second argument to the function plus 1 each time it run
        else:
            for tab_stop in range(level):  # Use the value of 'level' to control how many tab-stops are used
                print("\t", end='')  # Display a TAB character for each level of indentation
            print(each_item)  # If the item is being processed ISN´T a list, display the item on screen
