# Shapes

1. Create a Shape class that includes methods to describe the shape, its dimensions and area. The __init__() method should have parameters with the size of the shape’s minimum bounding rectangle.
2. Create a Rectangle class based on Shape. Create the same methods with its own implementation of of the dimensions and area methods.
3. Create a Square class based on Rectangle. Modify the __init__() method so that it only takes one parameter.
4. Create a Triangle class based on Shape. Implement the dimensions() and area() methods.
5. Create a Circle class and implement its methods.
6. Add a set_coordinates() method to Shape to set it’s x and y coordinate. Display the coordinates in the describe() method.
7. Add a collision() method to Shape to determine if one shape collides with another shape. Shapes will collide if their minimum bounding rectangles overlap. How would you use this method in a game?
8. Add a move() method to Shape so that move(-2, 3) moves the shape 2 to the left and 3 up.
9. Add a new name variable to Shape and display the name in the describe()method.
10. Create a list of 10 shapes called “Alien 1”, “Alien 2” and so on. Put them all at different coordinates.
11. Create a shape call “Rocket”. Display a list of the aliens shapes that the rocket shape has crashed into.
12. Move the rocket from left to right, stopping when it hits its first alien.
