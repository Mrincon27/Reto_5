from Shapes.Shape_class import Shape

class Rectangle(Shape):
    """Rectangle class defined by width and height."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of the rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"



