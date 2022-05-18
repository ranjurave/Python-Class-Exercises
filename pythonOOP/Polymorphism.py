class Animal: #Base class
    def __init__(self,name):
        self.name = name
        self.anisound = 'Grrrr...'
    def info(self):
        print(f"I am an animal, My name is {self.name}")
    def sound(self):
        print(self.anisound)

class Cat(Animal): #Derived class
    def __init__(self, name):
        super().__init__(name)
    def info(self):
        print(f"I am a cat, My name is {self.name}")
    def sound(self):
        print(self.anisound+"Meaw...")

class Dog(Animal): #Derived class
    def __init__(self, name):
        super().__init__(name)
    def info(self):
        print(f"I am a dog, My name is {self.name}")
    def sound(self, dogsound):
        print(self.anisound+dogsound)


ani = Animal("base animal")
cat1 = Cat("Kitty")
dog1 = Dog("Doggy")

# Same function has different implementation for different class
ani.info()
cat1.info()
dog1.info()

# Same function has different implementation for different class
ani.sound()
cat1.sound()
dog1.sound("woff...")

