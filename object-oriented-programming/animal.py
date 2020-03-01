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

    def __repr__(self):  # repr = representation
        return Animal.name + ' is of species' + self.species

    def __str__(self):
        return 'This object belongs to class ' + Animal.name

class Dog(Animal):  # inherits attributes of Animal (Dog is a subclass)
    def speak(self):
        print('Bark!Bark!Bark!')
