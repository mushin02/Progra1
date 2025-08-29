

def count_up_and_low_case(string):
    upper_case=0
    lower_case=0

    for letter in string:
        if letter.isupper():
            upper_case+=1
        elif letter.islower():
            lower_case+=1

    print(f'the numer of uppercase letters is {upper_case} and the number of lowercase letters is {lower_case}')   


def main():
    string= "I Love Chinease Food"
    count_up_and_low_case(string)
main()