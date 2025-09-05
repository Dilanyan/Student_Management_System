class Person:
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age

    @property
    def get_name(self):
        return self._name

    @property
    def get_surname(self):
        return self._surname

    @property
    def get_age(self):
        return self._age

    def introduce(self):
        print(f"Hi my name is {self.get_name()} {self.get_surname()}, I am {self.get_age()} years old")