import datetime
# This input for digits inputs from the user side. It converts the digit to int and return
def input_digit_from_user(a_number, text=''):
    while not a_number.isdigit() or a_number == "0":
        a_number = input(f"{text}: ")
    return int(a_number)

# Input the username and sure name. Clear form spaces, make Capital the first latter, etc.
def input_username_surename(name_surname, text=''):
    while not name_surname.isalpha():
        name_surname = input(f"{text}: ")
    return name_surname.capitalize()

# Store the user data in the dict
def user_data(user_name, user_surname, user_age, user_grade, user_number):
    current_year = datetime.datetime.now().year - user_age
    return {user_number:{
        'name': user_name.title(),
        'surname': user_surname.title(),
        'age': user_age,
        'grade': user_grade,
        'email': user_name + '.' + user_surname + str(current_year) + '@myschool.armstqb',
        'exam': "Pass" if user_grade >= 50 else "Fail"
    }}

# Neat print of student's data
def students_print(students):
    if students:
        for student_number, student_info in students.items():
            print(f"{student_number} >>> [")
            for key, value in student_info.items():
                print(f"{key.title()}: {value}")
            print("]")
    else:
        print("There is no student")