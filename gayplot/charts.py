from .scene import *


class Legend(Node):

    def __init__(self, columns = None):
        super().__init__()

        print(columns)

    def draw(self, renderer):
        pass


class Axis(Node):

    def __init__(self):
        super().__init__()

        pass


class Chart(Node):

    def __init__(self, dataset, title=None):
        super().__init__()

        self.dataset = dataset

        self['title'] = Text(title)
        self['title'].position = Vector(10, 10)
        self['title'].font.size = 36
        self['legend'] = Legend()

        self['rect1'] = Rectangle()
        self['rect1'].colour = Colour(0, 1, 0, 1)
        self['rect1'].position = Vector(10, 70)

        self['rect2'] = Rectangle()
        self['rect2'].colour = Colour(0, 0, 1, 1)

    @property
    def title(self):
        return self['title'].text

    @title.setter
    def title(self, value):
        self['title'].text = value

    @property
    def legend(self):
        return self['legend']

    def layout(self):
        self['title'].size = Vector(self.width - 20, 50)
        self['rect1'].size = Vector(self.width - 410, self.height - 80)
        self['rect2'].size = Vector(380, self.height - 80)
        self['rect2'].position = Vector(self.width - 390, 70)


class PieChart(Chart):

    def update(self):
        pass
