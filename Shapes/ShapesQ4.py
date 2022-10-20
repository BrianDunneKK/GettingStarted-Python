import math

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

class Triangle(Shape):
    # https://owlcation.com/stem/Everything-About-Triangles-and-More-Isosceles-Equilateral-Scalene-Pythagoras-Sine-and-Cosine
    type = "triangle"

    def __init__(self, a, b, c):
        # Parameters are the length of each side.
        # Assume side a is along lower side of the MBR, b is to the left and c is on the right
        # c2 = a2 + b2 - 2ab cos C
        # a/sin A = b/sin B = c/sin C
        self.side_a = a
        self.side_b = b
        self.side_c = c
        self.angle_C = math.acos((a*a + b*b - c*c)/(2*a*b))
        self.angle_A = math.asin(a * math.sin(self.angle_C) / c)
        self.angle_B = math.asin(b * math.sin(self.angle_C) / c)
        self.angle_Ad = round(math.degrees(self.angle_A))
        self.angle_Bd = round(math.degrees(self.angle_B))
        self.angle_Cd = round(math.degrees(self.angle_C))
        if self.angle_Bd <= 90 and self.angle_Cd <= 90:
            width = a
        else:
            width = b / math.cos(self.angle_C)
        height = round(b * math.sin(self.angle_C), 1)
        super().__init__(width, height)

    def dimensions(self):
        print(f"My three sides are {self.side_a} x {self.side_b} x {self.side_c}")
        print(f"My three angles are {self.angle_Ad} x {self.angle_Bd} x {self.angle_Cd} degrees")
        super().dimensions()

    def area(self):
        print(f"My area is {0.5 * self.side_a * self.mbr_height}.")

# ----------

s1 = Shape(3, 5)
s1.describe()

s2 = Rectangle(3, 5)
s2.describe()

s3 = Square(4)
s3.describe()

s4 = Triangle(6, 5, 4)
s4.describe()

s5 = Triangle(3, 5, 4)
s5.describe()

s6 = Triangle(5, 4, 3)
s6.describe()

s7 = Triangle(3, 6, 4)
s7.describe()