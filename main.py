input_max_student_number = input("Input the maximum number of students (from 1 to 5): ")
while not input_max_student_number.isdigit() or input_max_student_number == "0":
    print(f"Please, input a number from 1 to 5")
    input_max_student_number = input("Input the maximum number of students (from 1 to 5): ")

max_student_number = int(input_max_student_number)

student_counts = 0
input_student_or_not = True

while student_counts < max_student_number:

    name = input("Enter student name: ")
    surname = input("Enter student surname: ")
    student_age = input("Enter student age (from 18 to 120): ")
    while not student_age.isdigit():
        student_age = input("Enter student age (from 18 to 120): ")

    student_age = int(student_age)
    if student_age < 18:
        print("Dear {} {} is under 18 so, for now he/she is a primary school student".format(name, surname, student_age))
    elif 18 <= student_age <= 120:
        print("Dear {} {} student, is a college student".format(name, surname))
        print("Now let's to calculate the average grade for previous and current year - ")

        currentYearGrade = input("Enter student current year grade. From 1 to 100: ")
        while not currentYearGrade.isdigit() or currentYearGrade == "0":
            currentYearGrade = input("Enter student current year grade. From 1 to 100: ")

        currentYearGrade = int(currentYearGrade)

        if student_age > 18:
            previousYearGrade = input("Enter student previous year grade. From 1 to 100: ")
            while not previousYearGrade.isdigit() or previousYearGrade == "0":
                previousYearGrade = input("Enter student previous year grade. From 1 to 100: ")

            previousYearGrade = int(previousYearGrade)

            studentGrade = (previousYearGrade + currentYearGrade) / 2
            if studentGrade >= 50:
                print("Congratulation. The {} {} student pass the exam".format(name, surname))
            else:
                print("The {} {} fails. Need to hug".format(name, surname))
        else:
            print(
                "This  {} {} student is only 18 year old, obviously he hasn't previous year grade. So calculating the current year grade ".format(
                    name, surname))

            if currentYearGrade >= 50:
                print("Congratulation. The {} {} student pass the exam".format(name, surname))
            else:
                print("The {} {} fails. Need to hug".format(name, surname))
    else:
        print("Hmmm. There is no issue, for you we have special offers. Call us")

    student_counts += 1
    print(f"{student_counts} student(s) entered so far.")

    while True:
        if student_counts < max_student_number:
            input_student_or_not = input('Continue to input a student? yes/no: ')
        if input_student_or_not.lower() == 'yes':
            break
        elif input_student_or_not.lower() == 'no':
            break
        else:
            print('Type yes/no')

    if input_student_or_not == 'no':
        break






