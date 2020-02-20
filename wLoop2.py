# while loop
# Allows a user to enter any user name and adds it to list (l)
# once user enters '.' it wil break out of loop

l = []
while True:
    name = input('Enter a name: ')
    if name == '.':
        break
    l.append(name)
