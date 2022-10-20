class Shape:
    type = "shape"

    def __init__(self, width, height):
        # Parameters are the size of the minimum bounding rectangle
        self.mbr_width = width
        self.mbr_height = height

    def describe(self):
        print(f"\nI am a {self.type}")
        self.dimensions()
        self.area()

    def dimensions(self):
        print(f"I fit inside a rectangle of size {self.mbr_width} x {self.mbr_height} (w x h)")

    def area(self):
        print("I don't know my area.")

# ----------

class Rectangle(Shape):
    type = "rectangle"

    def dimensions(self):
        print(f"My dimensions are {self.mbr_width} x {self.mbr_height} (w x h)")

    def area(self):
        print(f"My area is {self.mbr_width * self.mbr_height}.")

# ----------

class Square(Rectangle):
    type = "square"

    def __init__(self, size):
        super().__init__(size, size)

# ----------

s1 = Shape(3, 5)
s1.describe()

s2 = Rectangle(3, 5)
s2.describe()

s3 = Square(4)
s3.describe()
