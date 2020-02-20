# Fibonacci performance loop vs. recursive function
import time

def timing(func, n, m):
    """Returns current time, then runs func
    for m times, then returns the out time"""
    start = time.time()
    for i in range(m):
        func(n)
    end = time.time()
    return end - start

def fibL(n):  # iteration version
    lst = [1, 1]
    for i in range(2, n + 1):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst[n]

def fibR(n):  # recursive version
    if n == 0 or n == 1:
        return 1
    else:
        return fibR(n - 1) + fibR(n - 2)
