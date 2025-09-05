from person import Person
class Teacher(Person):
    def __init__(self, name, surname, age, subject):
        super().__init__(name, surname, age)
        self._subject = subject

    def get_subject(self):
        return self._subject

    def introduce(self):
        print(f"Hi, my name is {self._name} {self._surname}, I am {self._age} years old and I am a teacher. My subject is {self.get_subject()}")