
def append_line():
    with open ("new_registry.txt", "a") as file:
        regitry= file.write(input("Add registry: ") + " ")

append_line()   