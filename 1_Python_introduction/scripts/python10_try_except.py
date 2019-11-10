try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')

print("Hello")