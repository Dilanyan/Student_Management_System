from student import Student
class HybridStudent(Student):
    def __init__(self, name, surname, age, grade, offline_lessons_time, number, online_lessons_time):
        super().__init__(name, surname, age, grade, offline_lessons_time, number)
        self._online_lessons_time = online_lessons_time

    def get_online_lessons_time(self):
        return self._online_lessons_time

    def set_online_lessons_time(self, new_online_lessons_time):
        print(f"{self._online_lessons_time} + {new_online_lessons_time}")
        self._online_lessons_time += new_online_lessons_time
        return self._online_lessons_time

    def get_total_lessons_time(self):
        return self.get_offline_lessons_time() + self.get_online_lessons_time()