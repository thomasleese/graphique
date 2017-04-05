from typing import NamedTuple


class Vector(NamedTuple):
    """A class representing an x, y coordinate in space."""

    x: float
    y: float


class Colour(NamedTuple):
    """A class representing a colour."""

    r: float
    g: float
    b: float
    a: float


class Node:

    def __init__(self, name = None):
        self.name = name
        self.children = []
        self.position = Vector(0, 0)
        self.size = Vector(0, 0)

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    @property
    def width(self):
        return self.size.x

    @property
    def height(self):
        return self.size.y

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

    def __init__(self, colour = Colour(1, 1, 1, 1), line_colour = None, line_width = 1):
        self.colour = colour
        self.line_width = line_width
        self.line_colour = line_colour


class Rectangle(Node, Shape):

    pass


class Ellipse(Node):

    pass


class Point(Node):

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
