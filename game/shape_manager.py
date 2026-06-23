from models.placed_shape import PlacedShape


class ShapeManager:

    def __init__(self):

        self.shapes = []

    def add_shape(self, shape_type, x, y):

        self.shapes.append(
            PlacedShape(shape_type, x, y)
        )

    def undo(self):

        if self.shapes:
            self.shapes.pop()

    def clear(self):

        self.shapes.clear()