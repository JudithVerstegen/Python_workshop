#####  numpy  #####
import numpy as np

a = np.array([[1, 3, 4], [2, 7, 6]])
b = np.array([[5, 2, 9], [3, 6, 4]])
print('a is', a)
print('b is', b)

# Slicing arrays
print(a[1])
# Like this: list of rows and list of columns
print('With indices:', a[[0,1],[1,2]])
# With Boolean array of the same shape
p = np.array([[True, True, False],
            [False, True, False]], dtype=bool)
print('Boolean way:', a[p])

# Calculating with arrays
print(a + b) 
print(a > b)

# Where, handy for selection
print(np.where(a > b, 10, 5))
print(np.where(a > b, a, b))

# Create arrays.
print(np.zeros((3,2)))
print(np.ones((2,3), np.int))
print(np.ones((2,3), np.int) * 5)
print(np.empty((2,2)))

# check the data type
print(np.zeros((3,2)).dtype)

# Use a compound data type for structured arrays
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})
print(data.dtype)

# Now we can fill this structured array with data
# of the correct type
name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]
data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)



