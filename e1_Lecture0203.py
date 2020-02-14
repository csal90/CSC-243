# wordFreq(filename) gathers information on the frequencey of a word appears in
# the file specified by the filename
# wordFreq('sample.txt')
def wordFreq(filename):
    freq = {}
    f = open(filename, 'r')
    text = f.read().split()
    f.close()
    for word in text:
        if word in freq:  # counter for item already exists
            freq[word] += 1  # so increment it
        else:  # counter for item is created
            freq[word] = 1  # an initialized to 1
    return freq


# printDict(dict) prints out the items in the dictionary dict in the following format:
# key1 value1
# key2 value2
# printDict(freq)
# The 5 
def printDict(dict):
    for word in dict:
        print(word, dict[word])


# itemFreq(list) prints out the frequencey of each number in a two dimensional list
# itemFreq([[1,3,5,1,6],[2,4,8,10],[-3,-5,9,11,16,8]])
# 1 appears 2 times
# 3 appears 1 time

def itemFreq(list):
    s1 = '{} appears {} times'
    s2 = '{} sppears {} time'
    dict = {}
    for num in list:
        if num in dict:
            dict[num] = dict[num] + 1
        else:
            dict[num] = 1
    for num in dict:
        if dict[num] > 1:
            print(str.format(item, dict[item]))
        else:
            print(str.format(item, dict[item]))
