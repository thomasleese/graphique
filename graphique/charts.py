from .graphics import *


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
        self['title'].position = Point(10, 10)
        self['title'].font.size = 24
        self['legend'] = Legend()

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
        self['title'].size = Size(self.width - 20, 50)


class ScatterPlot(Node):

    def __init__(self, dataset):
        super().__init__()

        self.dataset = dataset

        self['area'] = Rectangle(0, 0, 0, 0)
        self['area'].line_width = 2
        self['area'].line_colour = Colour(0, 0, 0, 1)

        self['points'] = Node()

    def add_points(self):
        colours = [Colour.from_rgb(26, 188, 156), Colour.from_rgb(52, 152, 219), Colour.from_rgb(155, 89, 182)]

        for row in self.dataset.rows:
            for i in range(1, len(self.dataset.columns)):
                rect = Ellipse(row.values[0] * 10, self['points'].height - row.values[i] * 10, 2)
                rect.colour = colours[i - 1]
                self['points'].add_child(rect)

    def layout(self):
        self['area'].size = self.size
        self['points'].size = self.size

        self['points'].children.clear()
        self.add_points()


class ScatterChart(Chart):

    def __init__(self, dataset):
        super().__init__(dataset)

        self['plot'] = ScatterPlot(dataset)

    def layout(self):
        super().layout()

        self['plot'].position = Point(10, self['title'].height + 20)
        self['plot'].size = Size(self.width - 20, self.height - (self['title'].y + self['title'].height + 20))
        self['plot'].layout()
