class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Name is {self.name} age is {self.age}"

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, 2022 - year)

    @staticmethod
    def IsAdult(age):
        return age>18

p1 = Person("Rolf", 42)
print(p1)
print(Person.fromBirthYear("Bob", 2006))
print(p1.IsAdult(30))