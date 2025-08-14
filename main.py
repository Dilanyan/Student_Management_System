from functions import sms
import logging
import os
import student
from helper import Helper

students = dict()
student_counts = 1
input_student_or_not = False
logging.basicConfig(filename='sms_logging.log', level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

# Add a new input value that will check if students’ data will be provided manually or from a file
while True:
    enter_students_manually = input("Input students manually? yes/no: ")
    if enter_students_manually.lower() == 'yes':
        break
    elif enter_students_manually.lower() == 'no':
        break
    else:
        print('Type yes/no')
        logging.warning(f"Typed - {enter_students_manually}. Need to type - yes OR no")


if enter_students_manually == "yes":

    max_student_number = Helper.input_digit_from_user("Input the maximum number of students")

    while student_counts <= max_student_number and not input_student_or_not:

        name = Helper.input_username_surname("Enter student name")
        surname = Helper.input_username_surname("Enter student surname")
        student_age = Helper.input_digit_from_user("Enter student age (from 18 to 120)")

        if student_age < 18:
            print("Dear {} {} is under 18 so, for now he/she is a primary school student".format(name, surname, student_age))
            logging.info(f"Input primary school student - {name}, {surname}, {student_age}")
        elif 18 <= student_age <= 120:
            print("Dear {} {} student, is a college student".format(name, surname))
            print("Now let's to calculate the average grade for previous and current year - ")

            currentYearGrade = Helper.input_digit_from_user("Enter student current year grade. From 1 to 100: ")

            if student_age > 18:
                previousYearGrade = Helper.input_digit_from_user("Enter student previous year grade. From 1 to 100: ")

                studentGrade = (previousYearGrade + currentYearGrade) / 2

                if studentGrade >= 50:
                    print("Congratulation. The {} {} student pass the exam".format(name, surname))
                else:
                    print("The {} {} fails. Need to hug".format(name, surname))

                # Add to dict
                students.update(sms.user_data(name, surname, student_age, studentGrade, student_counts))
                sms.input_users_into_file(name, surname, student_age, studentGrade, student_counts)
                logging.info(f"Added a user - {name}, {surname}, {studentGrade}, {name}.{surname}.{student_counts}@myschool.armstqb")

            else:
                print(
                    "This  {} {} student is only 18 year old, obviously he hasn't previous year grade. So calculating the current year grade ".format(
                        name, surname))

                if currentYearGrade >= 50:
                    print("Congratulation. The {} {} student pass the exam".format(name, surname))
                else:
                    print("The {} {} fails. Need to hug".format(name, surname))

                # Add to dict
                students.update(sms.user_data(name, surname, student_age, currentYearGrade, student_counts))
                sms.input_users_into_file(name, surname, student_age, currentYearGrade, student_counts)
                logging.info(f"Added a user - {name}, {surname}, {currentYearGrade}, {name}.{surname}.{student_counts}@myschool.armstqb")

            # Count user after adding to our college
            print(f"{student_counts} student(s) entered so far.")
            student_counts += 1

        else:
            print("Hmmm. There is no issue, for you we have special offers. Call us")
            logging.critical(f"This user {name, surname, student_age} can be invited to our secret project")
            students.update(sms.user_data(name, surname, student_age, 0, student_counts))
            sms.input_users_into_file(name, surname, student_age, 0, student_counts)


        if student_counts <= max_student_number:
            continue_input_user = input('Continue to input a student? yes/no: ')
            if continue_input_user.lower() == 'yes':
                input_student_or_not = False
            elif continue_input_user.lower() == 'no':
                input_student_or_not = True
            else:
                print('Type yes/no')
                logging.info(f"Typed - {enter_students_manually}. Need to type - yes OR no")

    sms.students_print(students)


else:
    # Input students form StudentsList.txt file to StudentsReport.txt file
    file_path_name = input("Input the “StudentsList.txt” file path (Like C:\\Users\\'username'\\Downloads or C:\\Users\\username\\Documents): ")
    os.chdir(file_path_name)
    try:
        with open("StudentsList.txt", "r") as file:
            content = file.readlines()
            for user_row in content:
                one_student_info = user_row.strip().split(' ')
                studentGrade = (int(one_student_info[3]) + int(one_student_info[4])) / 2
                students.update(sms.user_data(one_student_info[0], one_student_info[1], one_student_info[2], studentGrade, student_counts))
                student_counts += 1

    except FileNotFoundError:
        print("The file doesn't exist.")
        logging.error(f"The file doesn't exist.")
    finally:
        print("Operation complete.")
        logging.info(f"Operation complete.")

    for student_id, student_value in students.items():
        print(student_id)
        print(student_value['name'], student_value['surname'], student_value['age'], student_value['grade'], student_value['email'], student_value['exam'])
        sms.input_users_into_file(student_value['name'], student_value['surname'], student_value['age'], student_value['grade'], student_id)








