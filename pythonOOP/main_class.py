# Base class
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades)/len(self.grades)


student1 = Student("Rolf",(78,89,87,92))
print(f"The student {student1.name} got {student1.average()} average grade")
