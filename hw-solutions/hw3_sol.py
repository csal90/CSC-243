def average(s):
    sum = 0
    for w in s.split():
        sum += len(w)
    return sum / len(s.split())


def orderedWords():
    l = []
    l.append(input('Enter first word: '))
    l.append(input('Enter second word: '))
    l.append(input('Enter third word: '))
    return l[0] <= l[1] and l[1] <= l[2]


def innerProduct(x, y):
    product = 0
    for i in range(len(x)):
        product = product + x[i] * y[i]
    return (product)


def printRightTriangle(n):
    for i in range(1, n + 1):
        for j in range(n, n - i, -1):
            print(j, end=' ')
        print()


def censor(fname):
    f = open(fname, 'r')
    s = f.read()
    f.close()
    words = s.split()
    for i in range(len(words)):
        if len(words[i]) == 4:
            words[i] = 'xxxx'
    out = open('censored.txt', 'w')
    out.write(' '.join(words))
    out.close()
