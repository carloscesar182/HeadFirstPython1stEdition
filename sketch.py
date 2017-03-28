# Open a named file and assign the file to a file object called 'data'.
data = open('../HeadFirstPython1stEdition/chapter3/sketch.txt')  # Confirm you are at the right place.
# Use a 'readline()' method to grab a line from the file, then use de 'print()' BIF to display it on screen.
print(data.readline(), end='')  # Will print the first line.
print(data.readline(), end='')  # Will print the second line.

# It´s a standard iteration using the file´s data input.
for each_line in data:
    print(each_line, end='')  # Will print the entire file content.

# Since you are now done with the file, be sure to close it.
data.close()