# Fibonacci sequence: 1, 1, 2, 3, 5, 8, ....
# write a recursive function fib(n) that returns the nth number in Fibonacci sequence.
# fib(0)
# 1
# fib(1)
# 1
# fib(2)
# 2
# fib(5)
# 8

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
