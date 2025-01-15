from Rectangle_class import Rectangle

class Square(Rectangle):
    """Square class, a special case of Rectangle."""

    def __init__(self, side_length: float):
        super().__init__(side_length, side_length)

    def __str__(self):
        return f"Square(side_length={self.width})"