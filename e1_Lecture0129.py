# getNumebers() will get positive numbers from the user and returns a list
# of the entered numbers. It will prompt the user to enter a number until
# the user enters zero

# getNumbers()
# Enter a positive number: 10
# Enter a positive number: 11
# Enter a positive number: 3
# Enter a positive number: 0

def getNumbers():
    l = []
    while True:
        num = int(input('Enter a positive number: '))
        if num == 0:
            break
        l.append(num)
        
        

