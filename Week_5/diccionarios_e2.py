list_a = ['first_name', 'last_name', 'role', ]
list_b= ['Alek', 'Castillo', 'Software Engineer']

test={}

for key in range(len(list_a)):
    
    test[list_a[key]]= list_b[key]

print(test)     