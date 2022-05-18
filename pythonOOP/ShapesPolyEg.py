class BaseShape:
    def __init__(self, name):
        self.name = name
    def areaCalculator(self):
        pass
    def __str__(self):
        return self.name

class Rectange(BaseShape):
    def __init__(self, name, rlength, rbredth):
        super().__init__(name)
        self.rlenght = rlength
        self.rbreadth = rbredth
    def areaCalculator(self):
        return self.rlenght * self.rbreadth

class Circle(BaseShape):
    def __init__(self, name, cradius):
        super().__init__(name)
        self.cradius = cradius
    def areaCalculator(self):
        return 3.14*self.cradius**2

c1 = Circle('cir1', 5)
r1 = Rectange('rec1', 4, 3)
print(f"Area of {c1} is {c1.areaCalculator()}")
print(f"Area if {r1} is {r1.areaCalculator()}")