filename="data.col"
basename = ""

for letter in filename:
    if letter == ".":
##        print("found a dot!")
        break
    basename += letter

print(basename)
