# inputs
choice = True

# function
def interpret_choice(in_value):
  if in_value == 1:
    output = "The user said yes"
  elif in_value == 0:
    output = "The user said no"
  else:
    output = "Invalid input"
  return output

# MAIN
print(interpret_choice(choice))

