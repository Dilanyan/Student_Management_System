import logging
import json
import os
from hybridstudent import HybridStudent
from student import Student
from teacher import Teacher
from helper import Helper

student_counts = 1
continue_input_user = ""
student_object_list = list()
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
            print(f"Dear {name} {surname} is under 18 so, for now he/she is a primary school student")
            logging.info(f"This {name} {surname} student wants us, so call back or send invitation when he turns 18")

        elif 18 <= student_age <= 120:
            student_offline_lessons_time = Helper.input_digit_from_user("Enter student offline lessons time")
            student_online_lessons_time = Helper.input_digit_from_user("Enter student online lessons time")
            print(f"Dear {name} {surname} student, is a college student. Now let's to calculate the average grade")

            currentYearGrade = Helper.input_digit_from_user("Enter student current year grade. From 1 to 100")

            if student_age > 18:
                previousYearGrade = Helper.input_digit_from_user("Enter student previous year grade. From 1 to 100")
                grade = Helper.student_grade(currentYearGrade, previousYearGrade)

            else:
                print(f"This {name} {surname} student is only 18 year old, obviously he hasn't previous year grade. So calculating the current year grade ")
                grade = Helper.student_grade(currentYearGrade)

            student_object_list.append(HybridStudent(name, surname, student_age, grade, student_offline_lessons_time, student_online_lessons_time))


            # Count user after adding to our college
            print(f"{student_counts} student(s) entered so far.")
            student_counts += 1

        else:
            print("Hmmm. There is no issue, for you we have special offers. Call us")
            logging.critical(f"This user {name, surname, student_age} can be invited to our secret project")


        if student_counts <= max_student_number:
            continue_input_user = input('Continue to input a student? yes/no: ')
            if continue_input_user.lower() == 'yes':
                input_student_or_not = False
            elif continue_input_user.lower() == 'no':
                input_student_or_not = True
            else:
                print('Type yes/no')
                logging.info(f"Typed - {enter_students_manually}. Need to type - yes OR no")


    Helper.students_print(student_object_list)
    Helper.db(student_object_list)
    Helper.input_users_into_file(student_object_list)
    logging.info(student_object_list)



else:
    # Display students form a json file
    file_path_name = input("Input the “StudentsList.json” file path (Like C:\\Users\\'username'\\Downloads or C:\\Users\\username\\Documents): ")
    os.chdir(file_path_name)
    try:
        with open("StudentsList.json", "r") as file:
            students_data = json.load(file)
        print(json.dumps(students_data, indent=4))
    except FileNotFoundError:
        print("The file doesn't exist.")
        logging.error(f"The file doesn't exist.")
    finally:
        print("Operation complete.")
        logging.info(f"Operation complete.")








print("-------------------------------------------  ##  -----------------------------------------")
# A small code which will demonstrate polymorphism partially overriding then
# We will store objects - student and teacher in the list

# Empty List
teachers_students_list = list()

# Students
another_student1 = Student("Ali", "Baba", 40, 1000000, 0)

# Teachers
another_teacher1 = Teacher("George", "Washington", 337, "United States UX/UI Designer")

# Now we will put them into list then call the introduce function from each class (teacher, student)

teachers_students_list.append(another_teacher1)
teachers_students_list.append(another_student1)
Teacher.introduce(teachers_students_list[0])
Student.introduce(teachers_students_list[1])
print("-------------------------------------------  ##  -----------------------------------------")

