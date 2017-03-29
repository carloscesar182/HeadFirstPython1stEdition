# import os

"""Check whether the file exists."""
# if os.path.exists('../HeadFirstPython1stEdition/chapter3/sketch.txt'):
try:
    """"Open a named file and assign the file to a file object called 'data'.
    Confirm you are at the right place."""
    data = open('../HeadFirstPython1stEdition/chapter3/sketch.txt')

    """Use a 'readline()' method to grab a line from the file, then use de 'print()' BIF to display it on screen."""
    # print(data.readline(), end='')  """Will print the first line."""
    # print(data.readline(), end='')  """Will print the second line."""

    """It´s a standard iteration using the file´s data input.
    Process the data, extracting each part from each line and displaying each part on screen."""
    for each_line in data:
        try:
            """Note the use of the 'not' keyword, which negates the value of the condition"""
        # if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:  # Specifying the type of runtime error you are handling.
            pass
    """Since you are now done with the file, be sure to close it."""
    data.close()
except IOError:  # Specifying the type of runtime error you are handling.
    print('The data file is missing!')