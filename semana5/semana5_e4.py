my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in my_list[:]:
    if num % 2 !=0:
        my_list.remove(num)
print(my_list)