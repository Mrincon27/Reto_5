
class Shape:
    """Base class for all shapes."""

    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("Subclass must implement this method.")

    def perimeter(self):
        """Calculate the perimeter of the shape."""
        raise NotImplementedError("Subclass must implement this method.")
    
    def __str__(self):
        """String representation of the shape."""
        return f"{self.__class__.__name__} instance"
