class Shape:
    name = 'Shape'

    def __init__(self):
        self.count = 0

    def prt(self):
        self.count += 1
        print(Shape.name, 'has been printed', self.count, 'times.')

# child class to shape
class Circle(Shape):
    def setRadius(self, r):
        self.radius = r

    def prt(self):
        print('The circle has a radius of', self.radius)
