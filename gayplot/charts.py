class Legend:

    def __init__(self, columns):
        print(columns)

    def draw(self, renderer):
        pass


class Axis:

    def __init__(self):
        pass


class Chart:

    def __init__(self, dataset, title):
        self.dataset = dataset
        self.title = title


class PieChart(Chart):

    def draw(self, renderer):
        renderer.draw_text(self.title, 0.5, 0.03, 0.03)
