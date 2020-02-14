# Nested loop example

# print
# 0 1 2 3 4
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4
# 0 1 2 3 4 

for i in range(5):  # Outer loop executing 5x
    for i in range(0, 5):  # Inner loop printing numbers 0 - 4
        print(i, end=' ')  # printing range of numbers with space
    print()  # printing 5x
