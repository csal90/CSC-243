def duplicatesInLists(l, m):
    for e in l:
        if e in m:
            print(e)


def numbersInString(s):
    for w in s.split():
        if w.isdigit():
            print(w)


def reverseSentence(s):
    l = s.split()
    l.reverse()
    for w in l:
        print(w, end=' ')


def getMinAndMax(fname):
    inf = open(fname, 'r')
    l = []
    for n in inf:
        l.append(int(n))
    print(min(l), max(l))
