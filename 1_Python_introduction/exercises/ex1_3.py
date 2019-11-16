import math
import os

# inputs
r = 4
location = os.path.join('C://', 'Users', 'verstege', 'Documents', \
                        'scripts', 'temp')
file_name = 'radius.txt'

# function
def area_circle(radius):
  area = math.pi * radius ** 2
  return area

# MAIN
# compute area
my_area = area_circle(r)
# concatenate file location and name
file_location = os.path.join(location, file_name)
# write input and result to disk
with open(file_location, 'w') as f:
  f.write(str(r))
  f.write('\n')
  f.write(str(my_area))

