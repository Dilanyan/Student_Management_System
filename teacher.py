from person import Person
class Teacher(Person):
    def __init__(self, name, surname, age, subject):
        super().__init__(name, surname, age)
        self.subject = subject

    def introduce(self):
        print(f"Hi, my name is {self.name} {self.surname}, I am {self.age} years old and I am a teacher. My subject is {self.subject}")