# Christian Salas
# Worked Alone
import os


def printListRev(lst):
    """a recursive function printListRev() that takes a list lst as a parameter, prints out the elements in lst in the
    reversed order, with each element on a line."""
    if len(lst) > 0:
        printListRev(lst[1:])
        print(lst[0])


def tough(m, n):
    """a recursive function tough() that takes two non negative integer arguments and outputs a pattern"""
    if n > 0:
        tough(m, n // 2)
        print(" " * m + "*" * n)
        tough(m + n // 2, n // 2)


def numberOfFiles(dir):
    """a recursive function numberOfFiles() that takes a directory name dir as a string parameter, traverses
    all the files and subdirectories under dir, prints the pathname of each traversed regular file and returns
    the total number of traversed regular files."""
    counter = 0
    for i in os.listdir(dir):
        n = os.path.join(dir, i)
        if os.path.isfile(n):
            print(n)
            counter += 1
        else:
            counter += numberOfFiles(n)
    return counter


class House:
    """Create a class House that contains two boolean attributes: doorOpen and lampOn. The House class also has four
     methods: openDoor(), closeDoor(), turnOnLamp(), and turnOffLamp()."""

    def __init__(self):
        self.doorOpen = False
        self.lampOn = False

    def openDoor(self):
        self.doorOpen = True

    def closeDoor(self):
        self.doorOpen = False

    def turnOnLamp(self):
        self.lampOn = True

    def turnOffLamp(self):
        self.lampOn = False

    def __str__(self):
        if self.doorOpen:
            i = "The door is open. "
        else:
            i = "The door is closed. "
        if self.lampOn:
            i += "The lamp is on. "
        else:
            i += "The lamp is off. "
        return i
