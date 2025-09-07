from person import Person
class Student(Person):
    def __init__(self, name, surname, age, grade, offline_lessons_time, number):
        super().__init__(name, surname, age)
        self._grade = grade
        self._number = number
        self._offline_lessons_time = offline_lessons_time

    def get_number(self):
        return self._number

    def get_grade(self):
        return self._grade

    def get_offline_lessons_time(self):
        return self._offline_lessons_time

    def set_offline_lessons_time(self, new_offline_lessons_time):
        print(f"{self._offline_lessons_time} + {new_offline_lessons_time}")
        self._offline_lessons_time += new_offline_lessons_time
        return self._offline_lessons_time

    def pass_fail_exam(self):
        return "Pass" if self.get_grade() >= 50 else "Fail"

    def e_mmail(self):
        email = self._name + "." + self._surname + str(self._number) + "@myschool.armstqb"
        return email

    def introduce(self):
        print(f"Hi, my name is {self._name} {self._surname}, I am {self._age} years old and I am a student. My grade is {self._grade}")