# Fibonacci sequence: 1, 1, 2, 3, 5, 8, ....
# write a function fib(n) that returns the nth number in Fibonacci sequence.
# fib(0)
# 1
# fib(1)
# 1
# fib(2)
# 2
# fib(5)
# 8

def fib1(n):
    lst = [1, 1]
    for i in range(2, n + 1):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst[n]
