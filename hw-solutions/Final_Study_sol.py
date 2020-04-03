# CSC 243 Winter 2020 Final Study
def plural(s):
    if len(s)>=3 and (s[-2:]=='sh' or s[-2:]=='ch'):
        res=s+'es'
    elif len(s)>=2:
        if s[-1]=='y':
            if s[-2] in 'aeiou':
                res=s+'s'
            else:
                res=s[:-1]+'ies'
        else:
            res=s+'s'
    else:
        res=s+'s'
    return res

print(plural('shell'), plural('leech'), plural('leash'), plural('cherry'), plural('day'), plural('chair'), plural('box'), plural('knife'))


def findConsecutiveSubstring(str):
    print('findConsecutiveSubstring',str)
    if len(str)<2:
        return ''
    elif len(str)==2:
        if str[0].isalpha() and (ord(str[0])==ord(str[1])-1):
            return str
        else:
            return ''
    else:
        l=len(str)//2
        res=findConsecutiveSubstring(str[l-1:l+1])
        if res:
            return res
        else:
            res=findConsecutiveSubstring(str[:l])
            if res:
                return res
            else:
                return findConsecutiveSubstring(str[l:])

print(findConsecutiveSubstring('aefh'))
print(findConsecutiveSubstring('ae'))
print(findConsecutiveSubstring('ab'))
print(findConsecutiveSubstring('ba'))
print(findConsecutiveSubstring('aegdfxy'))
print(findConsecutiveSubstring('aegmnxz'))



