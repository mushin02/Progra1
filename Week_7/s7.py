



def get_number():
    try:
        return float(input("what's your number? "))
    except ValueError as e:
        print(f"Error [ValueError]: Please enter a valid number. Details: {e}")
        return 

def show_menu():
    math_operation = input(
        '''
Choose an math_operation:
1 - Sum
2 - Subtract
3 - Multiply
4 - Divide
5 - Exit
--> '''
    )
    if math_operation not in ["1", "2", "3", "4", "5"]:
        print("Invalid option. Please choose one of the available options (1â€“4).")
        return 
    return math_operation

def calculate(current_number, your_other_number, math_operation):

    if math_operation == "5":
        print("Exiting")
        return "exit"

    try:
        if math_operation == "1":
            return current_number + your_other_number
        elif math_operation == "2":
            return current_number - your_other_number
        elif math_operation == "3":
            return current_number * your_other_number
        elif math_operation == "4":
            return current_number / your_other_number
    except ZeroDivisionError as e:
        print(f"Error [ZeroDivisionError]: Cannot divide by zero. Details: {e}")
        return 

def main():
    current_number = None

    while True:
        if current_number is None:
            first_number = get_number()
            if first_number is None:
                continue
            current_number = first_number

        print(f"Current total: {current_number}")

        math_operation = show_menu()
        if math_operation is None:
            continue

        if math_operation == "5":
            result = calculate(current_number, 0, math_operation)  
            if result == "exit":
                break
            continue

        your_other_number = get_number()
        if your_other_number is None:
            continue

        result = calculate(current_number, your_other_number, math_operation)
        if result == "exit":
            break
        if result is not None:
            # print(f"The result is {result}")
            current_number = result    

main()