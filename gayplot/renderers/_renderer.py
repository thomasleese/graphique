class Renderer:

    def __init__(self, scene):
        self.scene = scene

    def save(self, filename):
        raise NotImplementedError('Saving not supported by this renderer.')

    def show(self):
        raise NotImplementedError('Showing not supported by this renderer.')

    def draw(self):
        raise NotImplementedError('Drawing not supported by this renderer.')
