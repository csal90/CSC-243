# tuples

phoneBook = {('chris', 'salas'): '(123)456-7890', ('kaitlyn', 'columbia'): '(321)654-0987'}
# tuple acting as a key in a dict


# exercise 1
# lookup(dict) takes a phone book dict as a parameter and prompts the user to enter the first and last of a person
# and prints the phone number associated with the person.
# Enter the first name: Chris
# Enter the last name: Salas
# (123)456-7890

def lookup(dict):
    fname = input('Enter the first name: ')
    lname = input('Enter the last name: ')
    key = dict[(fname, lname)]
    if key in dict:
        return key
    else:
        print('Not found.')
