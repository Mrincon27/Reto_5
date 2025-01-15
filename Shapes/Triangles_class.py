from Shape_class import Shape

class Triangle(Shape):
    """General Triangle class defined by the lengths of its three sides."""

    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """Calculate the area of the triangle using Heron's formula."""
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        """Calculate the perimeter of the triangle."""
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        """String representation of the triangle."""
        return f"Triangle(sides={self.side1}, {self.side2}, {self.side3})"

class Equilateral(Triangle):
    """Equilateral Triangle where all sides are equal."""

    def __init__(self, side_length: float):
        super().__init__(side_length, side_length, side_length)

    def __str__(self):
        """String representation of the equilateral triangle."""
        return f"Equilateral Triangle(side_length={self.side1})"

class Isosceles(Triangle):
    """Isosceles Triangle with two equal sides."""

    def __init__(self, equal_side: float, base: float):
        super().__init__(equal_side, equal_side, base)

    def __str__(self):
        """String representation of the isosceles triangle."""
        return f"Isosceles Triangle(equal_side={self.side1}, base={self.side3})"

class Scalene(Triangle):
    """Scalene Triangle with all sides unequal."""

    def __init__(self, side1: float, side2: float, side3: float):
        super().__init__(side1, side2, side3)

    def __str__(self):
        """String representation of the scalene triangle."""
        return f"Scalene Triangle(sides={self.side1}, {self.side2}, {self.side3})"

class Trirectangle(Triangle):
    """Right triangle (a triangle with a right angle)."""

    def __init__(self, base: float, height: float):
        hypotenuse = (base**2 + height**2)**0.5
        super().__init__(base, height, hypotenuse)

    def __str__(self):
        """String representation of the right triangle."""
        return f"Right Triangle(base={self.side1}, height={self.side2})"
