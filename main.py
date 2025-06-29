name = input("Enter student name: ")
surname = input("Enter student surname: ")
age = int(input("Enter student age: "))
if age < 18:
    print("Dear {} {} is under 18 so, for now he/she is a primary school student".format(name, surname, age))
elif 18 <= age <= 24:
    print("Dear {} {} student, is a college student".format(name, surname))
    print("Now let's to calculate the average grade for previous and current year - ")
    currentYearGrade = int(input("Enter student current year grade. From 1 to 100: "))
    if age > 18:
        previousYearGrade = int(input("Enter student previous year grade. From 1 to 100: "))
        studentGrade = (previousYearGrade + currentYearGrade)/2
        if studentGrade >= 50:
            print("Congratulation. The {} {} student pass the exam".format(name, surname))
        else:
            print("The {} {} fails. Need to hug".format(name, surname))
    else:
        print("This  {} {} student is only 18 year old, obviously he hasn't previous year grade. So calculating the current year grade ".format(name, surname))

        if currentYearGrade >= 50:
            print("Congratulation. The {} {} student pass the exam".format(name, surname))
        else:
            print("The {} {} fails. Need to hug".format(name, surname))
else:
    print("Hmmm. There is no issue, for you we have special offers. Call us")