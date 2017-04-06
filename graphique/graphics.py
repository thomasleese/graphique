from typing import NamedTuple


class BasePoint(NamedTuple):
    x: float
    y: float


class Point(BasePoint):
    """A class representing an x, y coordinate in space."""

    def copy(self, x: float = None, y: float = None):
        return Point(x if x else self.x, y if y else self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Size(BasePoint):
    """A class representing a size in space."""

    @property
    def width(self):
        return self.x

    @property
    def height(self):
        return self.y


class BaseColour(NamedTuple):
    r: float
    g: float
    b: float
    a: float


class Colour(BaseColour):

    @classmethod
    def from_rgb(cls, r, g, b):
        return cls(r / 255, g / 255, b / 255, 1)


class Font:

    def __init__(self, name, size):
        self.name = name
        self.size = size
