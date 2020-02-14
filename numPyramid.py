# return
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def printNumPyramid(n):
    for i in range(1, n + 1):
        for n in range(1, i + 1):
            print(n, end=' ')
        print()