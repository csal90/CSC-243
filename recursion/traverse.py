# write a function traverse(path) that traverse the path and prints out the pathname
# for each file
import os


def traverse(path):
    for f in os.listdir(path):
        name = os.path.join(path, f)
        if os.path.isdir(name):
            traverse(name)
        else:
            print(name)


def traverse2(path):
    """same output as traverse, this version has fewer statements"""
    if os.path.isdir(path):
        for f in os.listdir(path):
            traverse2(os.path.join(path, f))
    else:
        print(path)


# write a non-recursive function traverse3(path)
def traverse3(path):
    l = [path]  # contains the pathname for all subdirectories
    while len(l) > 0:
        name = l.pop(0)
        for f in os.listdir(name):
            fname = os.path.join(name, f)
            if os.path.isdir(fname):
                l.append(fname)
            else:
                print(fname)
