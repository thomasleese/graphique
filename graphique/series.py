from typing import *

from .graphics import Colour


class Series:

    def __init__(self, name: Optional[str] = None):
        self.name = name
        self.axes = []


class XYSeries(Series):

    def __init__(self, points, name: Optional[str] = None):
        super().__init__(name)

        self.points = points

        self.colour = Colour.from_rgb(26, 188, 156)


class Scatter(XYSeries):

    def __init__(self, points, name: Optional[str] = None):
        super().__init__(points, name)


class Line(XYSeries):

    def __init__(self, points, name: Optional[str] = None):
        super().__init__(points, name)
