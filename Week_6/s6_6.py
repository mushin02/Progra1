input_stuff = input('write your stuff separated by "-": ')

def sort_strings():
    word = input_stuff.split('-')
    word.sort()
    print ('-'.join(word))    
       
sort_strings()