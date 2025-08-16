import random

random_number= random.randint(1,10)
number= int(input("write a number within 1 and 10: "))
while(number!= random_number):
    number= int(input("try again: "))
    if (number==random_number):
        print("correct")