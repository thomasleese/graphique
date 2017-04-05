from .scene import *


class Legend(Node):

    def __init__(self, columns=None):
        print(columns)

    def draw(self, renderer):
        pass


class Axis(Node):

    def __init__(self):
        pass


class Chart(Node):

    def __init__(self, dataset, title=None):
        self.dataset = dataset

        self.scene = Scene()
        self.scene['title'] = Text(title)
        self.scene['legend'] = Legend()

    @property
    def title(self):
        return self.scene['title'].text

    @title.setter
    def title(self, value):
        self.scene['title'].text = value

    @property
    def legend(self):
        return self.scene['legend']


class PieChart(Chart):

    def update(self):
        pass
