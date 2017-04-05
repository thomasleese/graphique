class Renderer:

    def __init__(self, scene):
        self.scene = scene

    def save(self, filename):
        raise NotImplementedError('Save not supported by this renderer.')

    def show(self):
        raise NotImplementedError('Show not supported by this renderer.')

    def draw(self):
        raise NotImplementedError('Draw not supported by this renderer.')
