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

s1 = Shape(3, 5)
s1.describe()
