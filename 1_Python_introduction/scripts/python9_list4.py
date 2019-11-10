a_list = [1, 2, 3, 4, 5, 6] 

a_list[1:4]=[9]    # replace elements with one element
print(a_list)

a_list[0:0]=[0,0]  # insert two elements with value 0
print(a_list)

a_list[1:3]=[]     # delete two elements
print(a_list)

