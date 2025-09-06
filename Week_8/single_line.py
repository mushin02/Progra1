def remove_lines():
    with open("test.txt", "r") as file:
        lines = file.readlines()

    with open ("test2.txt", "w") as file2:
        for line in lines:
            file2.write(line.strip() + " ")    
remove_lines()