my_list = [4, 3, 6, 1, 7]

for num in range(len(my_list)):
    if num == 0:
        temp = my_list[num]           
        my_list[num] = my_list[-1]      
    elif num == len(my_list) - 1:
        my_list[num] = temp              

print(my_list)