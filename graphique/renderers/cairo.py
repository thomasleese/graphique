import cairocffi as cairo

from ._renderer import Renderer
from ..scene import *


class CairoRenderer(Renderer):

    def __init__(self, chart):
        super().__init__(chart)

        self.chart = chart

        self.current_position = [Vector(0, 0)]

    def clear(self):
        self.context.set_source_rgb(1, 1, 1)
        self.context.rectangle(0, 0, self.chart.width, self.chart.height)
        self.context.fill()

    def save(self, filename):
        self.surface.write_to_png(filename)

    def draw(self):
        self.chart.layout()

        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.chart.width, self.chart.height)
        self.context = cairo.Context(self.surface)

        self.clear()

        self.draw_node(self.chart)

    def draw_node(self, node):
        if isinstance(node, Text):
            self.draw_text_node(node)
        elif isinstance(node, Rectangle):
            self.draw_rectangle_node(node)

        self.current_position.append(self.current_position[-1] + node.position)

        for child in node.children:
            self.draw_node(child)

        self.current_position.pop()

    def draw_text_node(self, node):
        self.context.set_source_rgb(0, 0, 0)
        self.context.set_font_size(node.font.size)
        _, _, text_width, text_height, _, _ = self.context.text_extents(node.text)
        self.context.move_to(
            self.current_position[-1].x + node.x + (node.width - text_width) / 2,
            self.current_position[-1].y + node.y + text_height + (node.height - text_height) / 2
        )
        self.context.show_text(node.text)

    def draw_rectangle_node(self, node):
        self.context.rectangle(
            self.current_position[-1].x + node.x,
            self.current_position[-1].y + node.y,
            node.width, node.height
        )

        if node.colour:
            self.context.set_source_rgb(node.colour.r, node.colour.g, node.colour.b)
            self.context.fill()

        if node.line_colour:
            self.context.set_source_rgb(node.line_colour.r, node.line_colour.g, node.line_colour.b)
            self.context.stroke()
