class Shape:

    def __init__(self, name):

        self.name = name

        self.x = 0
        self.y = 0

    def __str__(self):
        return self.name