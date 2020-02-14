# Created a nested loop that will print a triangle of numbers (n)
# nested2(4)

# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

def nested2(n):
    num = 0
    for x in range(0, n):
        num = 0
        for y in range(0, x + 1):
            print(num, end=' ')
            num += 1
        print()
