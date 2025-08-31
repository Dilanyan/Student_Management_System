class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def introduce(self):
        print(f"Hi my name is {self.name} {self.surname}, I am {self.age} years old")