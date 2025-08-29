my_string = "Hello world"

def print_string_backwards():

    for word in range( len(my_string)-1, -1, -1):
        print (my_string[word], end='')

print_string_backwards()        