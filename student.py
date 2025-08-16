class Student:
    def __init__(self, name, surname, age, current_year_grade, number, previous_year_grade=0):
        self.name = name
        self.surname = surname
        self.age = age
        self.previous_year_grade = previous_year_grade
        self.current_year_grade = current_year_grade
        self.number = number

    def pass_fail_exam(self):
        grade = (self.previous_year_grade + self.current_year_grade) / 2 if self.previous_year_grade else self.current_year_grade
        return "Pass" if grade >= 50 else "Fail"

    def e_mmail(self):
        email = self.name + "." + self.surname + str(self.number) + "@myschool.armstqb"
        return email