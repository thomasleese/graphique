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


class Colour(NamedTuple):
    r: float
    g: float
    b: float
    a: float


class Node:

    def __init__(self, name = None):
        super().__init__()

        self.name = name
        self.children = []
        self.position = Point(0, 0)
        self.size = Size(0, 0)

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    @property
    def width(self):
        return self.size.width

    @property
    def height(self):
        return self.size.height

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def add_child(self, node, name=None):
        if name is not None:
            node.name = name
        # FIXME check node doesn't already exist
        self.children.append(node)

    def __getitem__(self, key):
        node = self.find_child(key)
        if node is None:
            raise KeyError(key)
        return node

    def __setitem__(self, key, value):
        self.add_child(value, key)


class Shape:

    def __init__(self, colour = None, line_colour = None, line_width = None):
        super().__init__()

        self.colour = colour
        self.line_width = line_width
        self.line_colour = line_colour


class Rectangle(Node, Shape):

    def __init__(self, x, y, width, height):
        super().__init__()

        self.position = Point(x, y)
        self.size = Size(width, height)


class Ellipse(Node):

    pass


class Dot(Node):

    pass


class Line(Node):

    pass


class Font:

    def __init__(self, name, size):
        self.name = name
        self.size = size


class Text(Node):

    default_font = Font('sans', 12)

    def __init__(self, text = '', font = None):
        super().__init__()

        self.text = text
        self.font = font if font else self.default_font
