# midterm 1

def firstNames(lst):
    l = []  # accumulator
    for name in lst:
        l.append(name.split(',')[1])  # first name is second element in the list
    return l


def specialCharCount(str):
    count = {'!': 0, '@': 0, '#': 0, '$': 0, '&': 0}
    for c in str:
        if c in count:
            count[c] += 1  # every time we see a special character, increment by 1
        print('!, @, #, $, & appear, {}, {}, {}, {}, {} times'.format(count['!'], count['@'],
                                                                      count['#'], count['$'], count['&']))


def printNumTriangle(n):
    for i in range(1, n + 1):  # outer loop to go over rows
        for n in range(1, i + 1):  # number of each row
            print(n, end=' ')  # prints number on each row
        print()  # prints the next row


def validPwd(pwd):
    if len(pwd) < 8:
        return False
    count_alphabet = 0
    count_digit = 0
    count_special = 0
    for c in pwd:
        if c.isaplha():
            count_alphabet += 1
        if c.isdigit():
            count_digit += 1
        if c in '!@#$%^&*':
            count_special += 1
    return count_alphabet > 0 and count_digit > 0 and count_special > 0  # only return when the counters
    # have 1 or more elements in them
