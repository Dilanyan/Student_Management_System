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
    user = {'name': user_name, 'surname': user_surname, 'age': user_age, 'grade': user_grade}
    users = {user_number: user}
    return users