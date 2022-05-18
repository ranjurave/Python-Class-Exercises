class Person:
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

    def display_name(self):
        print(f"{self.fName} {self.lName}")

class Student(Person):
    def __init__(self, fName, lName, gYear, sGrades):
        super().__init__(fName,lName)
        self.gYear = gYear
        self.sGrades = sGrades

    def display_grade(self):
        print(f"{self.fName} has a grade of {self.sGrades}")

s1 = Student("Joe","Jae",2021, 45)
s1.display_name()
s1.display_grade()
