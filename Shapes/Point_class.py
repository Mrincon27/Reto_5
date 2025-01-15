
class Point:
    """Class to represent a 2D point."""

    def __init__(self, coords: tuple):
        """Initialize the point with x and y coordinates."""
        self.x, self.y = coords

    def compute_distance(self, other: "Point"):
        """Calculate the distance to another point."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        """String representation of the point."""
        return f"Point({self.x}, {self.y})"
