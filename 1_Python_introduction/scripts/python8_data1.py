filename="data.col"

for letter in filename:
    if letter == ".":
        print("found a dot!")
        break
    print(letter)
