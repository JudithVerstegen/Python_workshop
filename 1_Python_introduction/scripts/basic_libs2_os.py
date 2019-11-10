# Import the os module for the next couple of Windows examples
import os

# Backslashes in Windows filenames give errors:
##print(os.path.exists('c:\Users\verstege\Documents\temp'))

# Three ways to fix the problem
# Use forward slashes instead
print(os.path.exists('c:/Users/verstege/Documents/temp')) 
# Use double-backslashes
print(os.path.exists('c:\\Users\\verstege\\Documents\\temp')) 
# Prefix the string with r
print(os.path.exists(r'c:\Users\verstege\Documents\temp')) 

# OR (less error prone)
# Use the function join()
# But you still need backslashes
path = os.path.join('c:\\', 'Users', 'verstege', 
                                  'Documents', 'temp')
print(os.path.exists(path)) 
os.chdir(path)

# Or start defining the path from the current directory
# (of the script or of the Python distribution!!)
print(os.getcwd())
os.chdir(os.path.join(os.getcwd(), 'calibration'))
print(os.getcwd())


