# names() prompts users to enter names of students repeatedly until the user
# presses ENTER without typing in a name, at this point this function prints out
# for each name the number of times when the name has been entered.
# names()
# Enter a name: Valirie
# Enter a name: Johnson
# Enter a name: Tommy
# Enter a name: Johnson
# Enter a name: Tommy
# Enter a name: Jennifer
# Enter a name:
# Valirie has been entered 1 times
# Johnson has been entered 2 times
# Tommy has been entered 2 times
# Jennifer has been entered 1 times

def names():
    namedict = {}
    while True:
        studentname = str(input('Enter a name: '))
        if studentname == '':
            break
        elif studentname in namedict:
            namedict[studentname] = namedict[studentname] + 1
        else:
            namedict[studentname] = 1
    for keyvalue in namedict:
        if namedict[keyvalue] > 1:
            print(keyvalue + ' has been entered ' + str(namedict[keyvalue]) + ' times')
        if namedict[keyvalue] == 1:
            print(keyvalue + ' has been entered 1 time')
