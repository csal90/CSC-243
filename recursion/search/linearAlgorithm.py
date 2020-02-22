def linear_search(lst, t):
    for i in range(len(lst)):
        if lst[i] == t:
            return i
        return -i
