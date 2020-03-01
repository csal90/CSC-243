# returns the first name in list
# firstNames(['Christian, Salas']
# returns (['Salas'])

def firstNames(lst):
    l = []
    for name in lst:
        l.append(name.split(',')[1])
    return l