
#variable global
# variable_outside_function_scope = 8
# def declare_variable():
#   print(f'Inside function: {variable_outside_function_scope}')


# declare_variable()
# print(f'Out of function: {variable_outside_function_scope}')


#local variable
# def declare_variable():
#   variable_inside_function_scope=3
#   print(f'Inside function: {variable_inside_function_scope}')


# declare_variable()
# print(f'Out of function: {variable_inside_function_scope}')


variable = "hello"
def change_global_variable():
    global variable
    variable += " world"
    print (variable)

change_global_variable()
  

