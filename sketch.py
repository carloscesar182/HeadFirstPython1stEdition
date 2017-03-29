# Open a named file and assign the file to a file object called 'data'.
data = open('../HeadFirstPython1stEdition/chapter3/sketch.txt')  # Confirm you are at the right place.
# Use a 'readline()' method to grab a line from the file, then use de 'print()' BIF to display it on screen.
#print(data.readline(), end='')  # Will print the first line.
#print(data.readline(), end='')  # Will print the second line.

# It´s a standard iteration using the file´s data input.
# Process the data, extracting each part from each line and displaying each part on screen.
for each_line in data:
    if not each_line.find(':') == -1:  # Note the use of the 'not' keyword, which negates the value of the condition
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')

# Since you are now done with the file, be sure to close it.
data.close()
