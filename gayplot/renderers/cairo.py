from cairocffi import cairo

from ._renderer import Renderer


class CairoRenderer(Renderer):

    def __init__(self, scene):
        super().__init__(scene)

        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, scene.width, scene.height)
        self.context = cairo.Context(self.surface)

        self.context.set_source_rgb(1, 1, 1)
        self.context.rectangle(0, 0, width, height)
        self.context.fill()

    def save(self, filename):
        self.surface.write_to_png(filename)

    def draw_text(self, text, x, y, size):
        self.context.set_source_rgb(0.1, 0.1, 0.1)
        self.context.set_font_size(size * self.height)
        _, _, width, height, dx, dy = self.context.text_extents(text)
        self.context.move_to(x * self.width - width / 2, y * self.height + height / 2)
        self.context.show_text(text)
