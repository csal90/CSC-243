# printMatrix(m) takes a 2D matrix or nested list as parameter and prints out
# the elements in the matrix by its row and columns
# printMatrix([[1,2,3],[4,5,6],[7,8,9]])
# 1 2 3
# 4 5 6
# 7 8 9

def printMatrix(m):
    for r in range(len(m)):
        for c in range(len(m)):
            print(m[r] [c], end=' ')
        print()
    pass


def increment(m, num):
    'Increment every element of m by num'
    for r in range(len(m)):
        for c in range(len(m)):
            print(m[r] [c]+num, end=' ')
            m[r] [c] += num # writing back to the matrix
        print()
    pass 
