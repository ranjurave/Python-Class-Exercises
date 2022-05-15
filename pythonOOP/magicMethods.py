class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # def __str__(self):
    #     return f"Person {self.name} is {self.age} years old"
    def __repr__(self):
        return f"Person({self.name} is {self.age} years old)"
    def bornIn(self):
        return 2022-self.age

bob = Person("Bob",35)
print(bob.bornIn())
print(bob)
