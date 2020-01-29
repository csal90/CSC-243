# charSet(low, high) that prints all the characters who ASCII code are between
# low and high, including both of them.
# e.g charSet(97, 99)
# 'a'
# 'b'
# 'c'

def charSet(low, high):
    for i in range(low, high+1):
        print(chr(i))
        
