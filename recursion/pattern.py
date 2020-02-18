# write a recursive function pattern(n) that takes an integer as input
# parameter and prints a pattern of numbers
# pattern(1)
# 1
# pattern(2)
# 1 2 1
# pattern(3)
# 1 2 1 3 1 2 1

def pattern(n):
    if n == 1:
        print(1, end=' ')
    else:
        pattern(n - 1)
        print(n, end=' ')
        pattern(n - 1)
