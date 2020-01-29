#exercise 1:
- 0 1 2 3 4
for nums in range(0,5):
    print(nums)

- 1 3 5 7
for nums in range(1,8,2):
    print(nums)

-1
for nums in range(1,2):
    print(nums)

- 0 3
for nums in range(1,2):
    print(nums)

- 0 2 4 6 8 10 12
for nums in range(0, 4, 3):
    print(nums)

- 17 13 9 5
for nums in range(0, 13, 2):
    print(nums)

#exercise 2:
#Write a function evenNums(), which prompts a message "Enter a whole number: " to the user to get a number n and prints out even numbers from 0 until n

def evenNums():
    n = int(input('Enter a whole number: '))
    for num in range(0, n+1, 2):
        print(num, end=' ')
evenNums()

#printNums(str) prints out even numbers if str == 'even' or odd numbers if str == 'odd'.
#The function prompt a message "Enter a whole number: ", get a number n from the user then print out either even numbers or odd numbers until n

def printNums(str):
    n = int(input('Enter a whole number: '))

    if str == 'even':
        for num in range(0, n + 1, 2):
            print(num, end=' ')
    elif str == 'odd':
        for num in range(0, n + 2, 2):
            print(num, end=' ')


printNums('')

#Write statements to do the following:
# str='This will be a sunny day.'
# 1. assign a variable n to the count of 'day' in str
str = 'This will be a sunny day'
n = str.count('day')
print(n)
# 2. assign a variable pos to the location/index of string 'sunny' in str
pos = str.find('sunny')
print(pos)
# 3. replace 'sunny' with 'cloudy'
str.replace('sunny', 'cloudy')
print(str)

#login(l) takes a list l consists of strings or names, prompts a message to 'Enter your login id: ' to the user and get a login id from the user, then it check whether the login id is within the list l
def login(l):
    loginId = input('Enter your login id: ')
    if loginId in l:
        print('login successfully')
    else:
        print('invalid login id')

#checkTemp(temp) takes integer parameter temp, and prints a message depending the value of temp
# prints 'it's hot' when temp > 86
# prints 'It's cool' when temp is > 0 and temp <= 86
# prints "It's freezing" when temp <= 0

def checkTemp(temp):
    if temp > 86:
        print("It's hot")
    elif 0 < temp <= 86:
        print("It's cool")
    else:
        print("It's freezing")

checkTemp()
