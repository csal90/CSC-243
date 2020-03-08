from random import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

class Deck:
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def __init__(self, shuffle, deal):
        self.shuffle = shuffle
        self.deal = deal

    def shuffle(self, cards):
        return random.shuffle(cards)

    def dealCard(self, cards):
        cards.pop()
        return cards[0]
