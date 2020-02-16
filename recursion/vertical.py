# vertical(n) prints digits of n vertically, i.e. staking on each other

def vertical(n):
    # base case is when n is a single-digit integer.
    if n < 10:
        print(n)
    else:
        vertical(n // 10)
        print(n % 10)

# prints the digits now in reverse order

def reverseVertical(n):
    # base case is when n is a single-digit integer.
    if n < 10:
        print(n)
    else:
        print(n % 10)
        reverseVertical(n // 10)
