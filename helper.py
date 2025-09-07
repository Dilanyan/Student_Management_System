import re

class Helper:
    """
        In this class collected all methods that will help to do something, for example:
         user input, 
         checking input
         collect user data
         write in a file
         ...
    """
    # This method checks if a user inputs a digit then return int
    @staticmethod
    def input_digit_from_user(field_text=''):
        while True:
            inpt_text = input(f"{field_text}: ")
            if not inpt_text.isdigit():
                print("Invalid number.")
            else:
                break
        return int(inpt_text)

    # This method for name and surname the input text will be cleared from numbers and other characters
    @staticmethod
    def input_username_surname(field_text = ''):
        reg_patt = r"^[A-Za-z]+(?:[-' ][A-Za-z]+)*$"
        while True:
            input_text = input(f"{field_text}: ")
            if re.findall(reg_patt, input_text):
                print(f"Good name, {input_text}!")
                break
            else:
                print("Invalid name.")
        return input_text.capitalize()

    @staticmethod
    # Store the user data in file
    def input_users_into_file(student_instance):
        try:
            with open("C:\\Users\\Narek\\PycharmProjects\\Student_Management_System\\StudentsReport.txt", "a") as file:
                file.write(str(student_instance))
        except FileNotFoundError:
            print("The file doesn't exist.")
        finally:
            print("Operation complete.")

    @staticmethod
    def student_grade(current_year_grade, previous_year_grade = 0):
        grade = (previous_year_grade + current_year_grade) / 2 if previous_year_grade else current_year_grade
        return grade
