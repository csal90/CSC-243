def fib(n):
    global d
    if n == 0 or n == 1:
        return 1
    else:
        if n - 1 in d:
            t1 = d[n - 1]
        else:
            t1 = fib(n - 1)
        if n - 2 in d:
            t2 = d[n - 2]
        else:
            t2 = fib(n - 2)
        d[n] = t1 + t2
        return t1 + t2


d = {}
