from student import Student
class HybridStudent(Student):
    def __init__(self, name, surname, age, grade, offline_lessons_time, online_lessons_time):
        super().__init__(name, surname, age, grade, offline_lessons_time)
        self._online_lessons_time = online_lessons_time

    def get_online_lessons_time(self):
        return self._online_lessons_time

    def set_online_lessons_time(self, new_online_lessons_time):
        self._online_lessons_time += new_online_lessons_time
        return self._online_lessons_time

    def get_total_lessons_time(self):
        return self.get_offline_lessons_time() + self.get_online_lessons_time()

    def get_name(self):
        return super().get_name

    def get_surname(self):
        return super().get_surname

    def get_age(self):
        return super().get_age

    def get_pass_fail_exam(self):
        return super().pass_fail_exam()
