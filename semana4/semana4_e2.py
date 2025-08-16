name = input("what's your name? ")
lastname = input("what's your lastname? ")
age= int(input("what's your age "))

if(age <= 5):
    print("you are a baby")
elif(age<=10):
    print("you are a child")
elif(age<=13):
    print("you are a pre-adolescent")
elif(age<=18):
    print("you are an adolescent")
elif(age<=27):
    print("you are a young adult")
elif(age<=60):
    print("you are an adult")
else:
    print("you are an old adult")                       