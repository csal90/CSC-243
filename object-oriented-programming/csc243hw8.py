# Christian Salas
# Worked Alone
import math
from html.parser import HTMLParser
# from urllib.request import urlopen / Needed for testing URL

class BankAccount:
    """Bank account that allows you to withdraw and deposit money"""

    def __init__(self, accountNumber, balance=0):
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __repr__(self):
        return 'Account#{} Balance:{}'.format(self.accountNumber, self.balance)


class SafeBankAccount(BankAccount):
    """Subclass that checks for overdrafts, and negative deposits"""

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Overdraft')
        self.balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Negative deposit')
        self.balance += amount


class Segment:
    """represents a line segment and returns its length and slope."""

    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def length(self):
        return math.sqrt((self.set2[1] - self.set1[1]) ** 2 + (self.set2[0] - self.set1[0]) ** 2)

    def slope(self):
        return (self.set2[1] - self.set1[1]) / (self.set2[0] - self.set1[0])


class ImageLinks(HTMLParser):
    """HTML parser ImageLinks that prints out all the hyperlinks of the images on an HTML web page"""
    def __init__(self):
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if 'img' in tag:
            for attr in attrs:
                if attr[0] == 'src':
                    print(attr[1])

    def handle_endtag(self, tag):
        if 'img' in tag:
            print()


class ListPrinter(HTMLParser):
    """prints a Python list for every unordered list in an HTML web page"""
    # Could not quiet figure this one out.
    dict = {}
    counter = 0
    flag = True

    def handle_starttag(self, startTag, attrs):
        if str(startTag) == "ul":
            self.counter = self.counter + 1
        if self.counter not in self.dict.keys():
            self.dict[self.counter] = []
        if startTag == "li":
            self.flag = True

    def handle_data(self, data):
        if self.flag:
            self.dict[self.counter].append(data)