import cairocffi as cairo

from ._renderer import Renderer
from ..scene import *


class CairoRenderer(Renderer):

    def __init__(self, chart):
        super().__init__(chart)

        self.chart = chart

    def clear(self):
        self.context.set_source_rgb(1, 1, 1)
        self.context.rectangle(0, 0, self.chart.width, self.chart.height)
        self.context.fill()

    def save(self, filename):
        self.surface.write_to_png(filename)

    def draw(self):
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.chart.width, self.chart.height)
        self.context = cairo.Context(self.surface)

        self.clear()

        self.draw_node(self.chart)

    def draw_node(self, node):
        if isinstance(node, Text):
            self.draw_text_node(node)
        elif isinstance(node, Rectangle):
            self.draw_rectangle_node(node)

        for child in node.children:
            self.draw_node(child)

    def draw_text_node(self, node):
        self.context.set_source_rgb(0, 0, 0)
        self.context.set_font_size(node.font.size)
        _, _, text_width, text_height, _, _ = self.context.text_extents(node.text)
        self.context.move_to(
            node.x + (node.width - text_width) / 2,
            node.y + text_height + (node.height - text_height) / 2
        )
        self.context.show_text(node.text)

    def draw_rectangle_node(self, node):
        self.context.set_source_rgb(node.colour.r, node.colour.g, node.colour.b)
        self.context.rectangle(node.x, node.y, node.width, node.height)
        self.context.fill()
