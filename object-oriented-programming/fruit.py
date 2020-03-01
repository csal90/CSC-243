# implement a class Fruit that supports the following methods
# f = Fruit('orange')
# print(f)
# orange
# f.setType('banana')
# print(f)
# banana

class Fruit:
    def __init__(self, type):
        self.type = type
        print(type)

    def setType(self, type):
        self.type = type

    def __str__(self):
        return 'Fruit of type ', self.type

    def __repr__(self):
        return self.type
