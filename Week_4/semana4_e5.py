grade_counter= 1

passed_grades= 0
failed_grades = 0
passed_grades_average = 0
failed_grades_average = 0
grade_average_total = 0

number_of_grades= int(input("how many grades did you receive?: "))

while(grade_counter<=number_of_grades):
    grade= int(input(f"tell me your grade {grade_counter} "))
    if (grade < 70):
        failed_grades= failed_grades + 1
        failed_grades_average = failed_grades_average + grade
    else:   
        passed_grades = passed_grades + 1
        passed_grades_average = passed_grades_average + grade
    grade_counter= grade_counter + 1
    grade_average_total = grade_average_total + (grade / number_of_grades)

if (failed_grades>=1):
    failed_grades_average = failed_grades_average / failed_grades
if (passed_grades>=1):
    passed_grades_average = passed_grades_average / passed_grades

print(f'the student has {passed_grades} passed grades')
print(f'the passed grades average is {passed_grades_average}')
print(f'the student has {failed_grades} failed grades')
print(f'Failed grades average {failed_grades_average}')
print(f'total average is {grade_average_total}')