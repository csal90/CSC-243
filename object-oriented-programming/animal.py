# Animal OO practice
class Animal:
    name = "Animal"

    def __init__(self, name):
        self.species = 'Unknown'
        self.name = name

    def __del__(self):  # destructor
        print('The object is deleted!')

    def setSpecies(self, species):
        self.species = species

    def speak(self):
        pass


class Dog(Animal):  # inherits attributes of Animal (Dog is a subclass)
    def speak(self):
        print('Bark!Bark!Bark!')


class Book:
    def __init__(self, fname):  # open file and read
        self.f = open(fname, 'r')

    def read(self, size):  # read file and input character size you want to return
        s = self.f.read(size)
        print(s)

    def __del__(self):  # delete object
        self.f.close()
