import string

# method 1
filename = "data.col"
index_dot = filename.find(".")
print(filename[0:index_dot])

# method 2
parts = filename.split(".")
print(parts[0])
