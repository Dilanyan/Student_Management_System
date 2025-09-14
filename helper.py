import re
import json

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
    def input_users_into_file(student_object_list):
        try:
            with open("./StudentsReport.json", "a") as file:
                students_list = []
                for student_object in student_object_list:
                    item = {
                              "id": hash(student_object),
                              "name": student_object.get_name(),
                              "surname": student_object.get_surname(),
                              "age": student_object.get_age(),
                              "email": Helper.e_mmail(student_object.get_name(), student_object.get_surname(), hash(student_object)),
                              "grade": student_object.get_grade(),
                              "exam_result": student_object.get_pass_fail_exam(),
                              "offline_lessons_time": student_object.get_offline_lessons_time(),
                              "online_lessons_time": student_object.get_online_lessons_time(),
                            }
                    students_list.append(item)
                students = {"students": students_list}
                json.dump(students, file, indent=4)
        except FileNotFoundError:
            print("The file doesn't exist.")
        finally:
            print("Operation complete.")

    @staticmethod
    def student_grade(current_year_grade, previous_year_grade = 0):
        grade = (previous_year_grade + current_year_grade) / 2 if previous_year_grade else current_year_grade
        return grade

    @staticmethod
    def e_mmail(name, surname, number):
        email = name + "." + surname + "." + str(number) + "@myschool.armstqb"
        return email

    @staticmethod
    # Neat print of student's data
    def students_print(student_object_list):
        for student_object in student_object_list:
            print(student_object.get_name())
            print(student_object.get_surname())
            print(student_object.get_age())
            print(Helper.e_mmail(student_object.get_name(), student_object.get_surname(), hash(student_object)))
            print(student_object.get_grade())
            print(student_object.get_pass_fail_exam())
            print(student_object.get_offline_lessons_time())
            print(student_object.get_online_lessons_time())
            print("------------------------------")

    @staticmethod
    # Print of student's data from json file
    def students_print_from_json_file(students_data):
        for student_main_key_is_dict, student_main_value_is_list in students_data.items():
            print(f"{student_main_key_is_dict} : [")

            for student_dict in student_main_value_is_list:
                for student_info_key, student_info_value in student_dict.items():
                    print(f"{student_info_key.title()}: {student_info_value} ")

            print("]")