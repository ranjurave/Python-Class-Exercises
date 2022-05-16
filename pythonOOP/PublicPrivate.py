class Student:
    school_name = "ABC School"
    def __init__(self, stud_name, stud_class):
        self.__sname = stud_name
        self.__sclass = stud_class

    def getsname(self):
        return self.__sname
    def getsclass(self):
        return self.__sclass

    @classmethod
    def ChangeSchool(cls,newName):
        cls.school_name = newName

s1 = Student('Lee', 5)
s2 = Student('Jack', 7)

print(f'{s1.getsname()} is studying in class {s1.getsclass()} at {s1.school_name}')
print(f'{s2.getsname()} is studying in class {s2.getsclass()} at {Student.school_name}')

Student.ChangeSchool("Hill Valley High School")

print(f'{s1.getsname()} is studying in class {s1.getsclass()} at {s1.school_name}')
print(f'{s2.getsname()} is studying in class {s2.getsclass()} at {Student.school_name}')