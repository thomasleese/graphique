from collections import UserList
from enum import Enum
from typing import *

from .graphics import *


class Orientation(Enum):
    horizontal = 'horizontal'
    vertical = 'vertical'


class Axis:

    def __init__(self):
        self.orientation = Orientation.horizontal


class Legend(Node):

    def __init__(self, columns = None):
        super().__init__()

        print(columns)

    def draw(self, renderer):
        pass


class SeriesList(UserList):

    def __init__(self, chart, data = []):
        self.chart = chart
        self.data = data


class AxesList(UserList):

    def __init__(self, chart, data = []):
        self.chart = chart
        self.data = data


class Chart(Node):

    def __init__(self, series, title: Optional[str] = None):
        super().__init__()

        self.title = title
        self.series = SeriesList(self, series)
        self.axes = AxesList(self)
        self.legend = Legend()
