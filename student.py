from person import Person
class Student(Person):
    def __init__(self, name, surname, age, grade=0, offline_lessons_time=0, number = 0, current_year_grade = 0, previous_year_grade = 0):
        super().__init__(name, surname, age)
        self._grade = grade
        self._previous_year_grade = previous_year_grade
        self._current_year_grade = current_year_grade
        self._number = number
        self._offline_lessons_time = offline_lessons_time


    def get_previous_year_grade(self):
        return self._previous_year_grade

    def get_current_year_grade(self):
        return self._current_year_grade

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
        if self._current_year_grade or self._previous_year_grade:
            grade = (self._previous_year_grade + self._current_year_grade) / 2 if self._previous_year_grade else self._current_year_grade
            return "Pass" if grade >= 50 else "Fail"
        else:
            return "Pass" if self._grade >= 50 else "Fail"

    def e_mmail(self):
        email = self._name + "." + self._surname + str(self._number) + "@myschool.armstqb"
        return email

    def introduce(self):
        print(f"Hi, my name is {self._name} {self._surname}, I am {self._age} years old and I am a student. My grade is {self._grade}")

    # def offline_lessons_calc(self):
    #     if offline_lesson_time:
    #         return offline_lesson_time
    #     else:
    #         return offline_lesson_time +=