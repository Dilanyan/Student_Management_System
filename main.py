import logging
import os
from student import Student
from teacher import Teacher
from helper import Helper

student_counts = 1
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
            print(f"Dear {name} {surname} student, is a college student. Now let's to calculate the average grade")

            currentYearGrade = Helper.input_digit_from_user("Enter student current year grade. From 1 to 100")

            if student_age > 18:
                previousYearGrade = Helper.input_digit_from_user("Enter student previous year grade. From 1 to 100")

                # First put the student object into list
                student_object_list.insert(student_counts-1, Student(name, surname, student_age, currentYearGrade, student_counts, previousYearGrade))

                # We can print the exam result if we want
                print(f"{student_object_list[student_counts-1].pass_fail_exam()}")

            else:
                print(f"This {name} {surname} student is only 18 year old, obviously he hasn't previous year grade. So calculating the current year grade ")
                # First put the student object into list
                student_object_list.insert(student_counts - 1,Student(name, surname, student_age, currentYearGrade, student_counts))

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

    Helper.input_users_into_file(student_object_list)
    logging.info(student_object_list)


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
                student_object_list.insert(student_counts - 1, Student(one_student_info[0], one_student_info[1], one_student_info[2], studentGrade, student_counts))
                student_counts += 1

    except FileNotFoundError:
        print("The file doesn't exist.")
        logging.error(f"The file doesn't exist.")
    finally:
        print("Operation complete.")
        logging.info(f"Operation complete.")


# A small cod which will demonstrate polymorphism
# We will store objects - student and teacher in the list

# Empty List
teachers_students_list = list()

# Students
another_student1 = Student("Ali", "Baba", 40, 1000000)

# Teachers
another_teacher1 = Teacher("George", "Washington", 337, "United States UX/UI Designer")

# Now we will put them into list then call the introduce function from each class (teacher, student)

teachers_students_list.append(another_teacher1)
teachers_students_list.append(another_student1)
Teacher.introduce(teachers_students_list[0])
Student.introduce(teachers_students_list[1])





