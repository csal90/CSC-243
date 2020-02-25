# Implement a function product(l) that takes a list l as parameter and multiplies all the numbers
# in l, and returns the product of the multiplication
def product(l):
    result = 1
    for num in l:
        result = result * num
    print(result)


# Write a function that concatenates all #s in a string to 1 string
def digits(s):
    r = ''
    for c in s:
        if c.isdigit():
            r = r + c
    return r


# Write a function divisors(n) that takes an integer n and returns a list of the positive divisors of
# n
# divisors(8)
# [1,2,4,8]
def divisors(n):
    l = []
    for num in range(l, n + 1):
        if n % num == 0:
            l.append(num)
    return l


# Counter loop
l = [1, 3, 5, 7, 9]
for i in range(0, len(l)):
    print(l[i])


# Counter loop - Write a function ascending(l) to check whether a list of numbers is sorted in order
def ascending(l):
    for i in range(len(l) - 1):
        if l[i] > l[i]:
            return False
    return True
