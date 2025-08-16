
def convert_to_capital():
    with open ("original.txt", "r") as file:
        lines= file.read()

    
    with open ("new.txt", "w") as file2:
        file2.write(lines.upper())

convert_to_capital()