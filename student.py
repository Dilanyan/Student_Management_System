from person import Person
class Student(Person):
    def __init__(self, name, surname, age, grade=0, number = 0, current_year_grade = 0, previous_year_grade = 0):
        super().__init__(name, surname, age)
        self.grade = grade
        self.previous_year_grade = previous_year_grade
        self.current_year_grade = current_year_grade
        self.number = number

    def pass_fail_exam(self):
        if self.current_year_grade or self.previous_year_grade:
            grade = (self.previous_year_grade + self.current_year_grade) / 2 if self.previous_year_grade else self.current_year_grade
            return "Pass" if grade >= 50 else "Fail"
        else:
            return "Pass" if self.grade >= 50 else "Fail"

    def e_mmail(self):
        email = self.name + "." + self.surname + str(self.number) + "@myschool.armstqb"
        return email

    def introduce(self):
        print(f"Hi, my name is {self.name} {self.surname}, I am {self.age} years old and I am a student. My grade is {self.grade}")