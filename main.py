import functions

input_max_student_number = input("Input the maximum number of students: ")
max_student_number = functions.input_digit_from_user(input_max_student_number, "Input the maximum number of students")

students = dict()
student_counts = 0
input_student_or_not = ""
input_student_or_not1 = True

while student_counts < max_student_number:

    name = input("Enter student name: ")
    username = functions.input_username_surename(name, "Enter student name")

    surname = input("Enter student surname: ")
    user_surname = functions.input_username_surename(surname, "Enter student surname")

    student_age = input("Enter student age (from 18 to 120): ")
    student_age = functions.input_digit_from_user(student_age, "Enter student age (from 18 to 120)")


    if student_age < 18:
        print("Dear {} {} is under 18 so, for now he/she is a primary school student".format(name, surname, student_age))
    elif 18 <= student_age <= 120:
        print("Dear {} {} student, is a college student".format(name, surname))
        print("Now let's to calculate the average grade for previous and current year - ")

        currentYearGrade = input("Enter student current year grade. From 1 to 100: ")
        currentYearGrade = functions.input_digit_from_user(currentYearGrade, "Enter student current year grade. From 1 to 100: ")

        if student_age > 18:
            previousYearGrade = input("Enter student previous year grade. From 1 to 100: ")
            previousYearGrade = functions.input_digit_from_user(previousYearGrade,"Enter student current year grade. From 1 to 100: ")

            studentGrade = (previousYearGrade + currentYearGrade) / 2

            if studentGrade >= 50:
                print("Congratulation. The {} {} student pass the exam".format(name, surname))
            else:
                print("The {} {} fails. Need to hug".format(name, surname))

            # Add to dict
            students.update(functions.user_data(name, surname, student_age, studentGrade, student_counts))

        else:
            print(
                "This  {} {} student is only 18 year old, obviously he hasn't previous year grade. So calculating the current year grade ".format(
                    name, surname))

            if currentYearGrade >= 50:
                print("Congratulation. The {} {} student pass the exam".format(name, surname))
            else:
                print("The {} {} fails. Need to hug".format(name, surname))

            # Add to dict
            students.update(functions.user_data(name, surname, student_age, currentYearGrade, student_counts))

    else:
        print("Hmmm. There is no issue, for you we have special offers. Call us")
        students.update(functions.user_data(name, surname, student_age, 0, student_counts))

    if 18 <= student_age <= 120:
        print(f"{student_counts + 1} student(s) entered so far.")

    if student_counts + 1 != max_student_number:
        while student_counts < max_student_number:
            input_student_or_not = input('Continue to input a student? yes/no: ')
            if input_student_or_not.lower() == 'yes':
                break
            elif input_student_or_not.lower() == 'no':
                break
            else:
                print('Type yes/no')

    if input_student_or_not == 'no':
        break

    student_counts += 1

functions.students_print(students)




