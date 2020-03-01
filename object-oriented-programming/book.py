class Book:
    def __init__(self, fname):  # open file and read
        self.f = open(fname, 'r')

    def read(self, size):  # read file and input character size you want to return
        s = self.f.read(size)
        print(s)

    def __del__(self):  # delete object
        self.f.close()