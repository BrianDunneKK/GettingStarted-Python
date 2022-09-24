#--- Define the class Animal
class Animal:
    def __init__(self, kind, name, legs = 0):
        self.kind = kind
        self.name = name
        self.legs = legs
        
    def describe(self):
        print(f"My name is {self.name}. I am a {self.kind}. I have {self.legs} legs.")

#--- Define the class Dog
class Dog(Animal):
    def __init__(self, name):
        super().__init__("dog", name, 4)
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def describe(self):
        super().describe()
        for t in self.tricks:
            print(f"I can {t}")   
        
        
#--- Test the classes
a = Animal("dog", "Shep", 4)

d = Dog("Rover")
d.add_trick("roll over")
d.add_trick("play dead")

a.describe()
print("  ---  ")
d.describe()

