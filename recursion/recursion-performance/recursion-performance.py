import os
import time, random
# binary function searchs target in lst[i:j]
def binary_search_helper(target,lst,i,j):
    if i>=j:
        return -1
    mid=(i+j)//2
    if target==lst[mid]:
        return mid
    elif target<lst[mid]:
        return binary_search_helper(target,lst,i,mid)
    else:
        return binary_search_helper(target,lst,mid+1,j)

lst = [x for x in range(10000)] # 0,1,2,3,...,9997,9998,9999

def binary_search(lst, t):
    #lst.sort()
    return binary_search_helper(t,lst,0,len(lst))

def linear_search(lst, t):
    for i in range(len(lst)):
        if lst[i]==t:
            return i
    return -1

def binary_search_test(lst):
    return binary_search(lst, random.choice(lst))

def linear_search_test(lst):
    return linear_search(lst, random.choice(lst))
    
def timing(func,n,m):
   start=time.time()
   for i in range(m):
       func(n)
   end=time.time()
   return end-start
