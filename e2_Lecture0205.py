# multiples() returns three sets of numbers: multiples of 3, multiples of 5,
# multiples of 7. It takes into account only positive numbers up to 50. 
def multiples():
    multhree = set()
    mulfive = set()
    mulseven = set()
    for num in range(1,51):
        if num % 3 == 0:
            multhree.add(num)
        if num % 5 == 0:
            mulfive.add(num)
        if num % 7 == 0:
            mulseven.add(num)
    return multhree, mulfive, mulseven

