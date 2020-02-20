# listPrint(lst)
# listPrint([[1,2],[[[4]]],[1,[3,[5]]]])
# 1
# 2
# 4
# 1
# 3
# 5

def listPrint(lst):
    if len(lst) == 1:  # lst has only one element n
        if type(lst[0]) is list:  # n is a list itself
            listPrint(lst[0])
        else:  # n is not a list itself
            print(lst[0])
    else:
        if type(lst[0]) is list:
            listPrint(lst[0])
        else:  # n is not a list itself
            print(lst[0])
        listPrint(lst[1:])  # takes care rest of list
