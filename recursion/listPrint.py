# write a function printList(lst) that prints out all the elements of lst
# using recursion
# printLst([1,2,3])
# 1
# 2
# 3

def printLst(lst):
    if len(lst) == 1:  # base case
        print(lst[0])
    else:
        print(lst[0])
        printLst(lst[1:])


