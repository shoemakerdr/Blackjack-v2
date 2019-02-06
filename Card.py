ranks = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
         'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

import random

class Card:
    """Card class that holds a card with a rank and a suit"""
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        return ranks[self.rank]

    def __str__(self):
        return (str(self.rank)+' of '+self.suit)

#test_card = Card('Two','Hearts')
#print(test_card.card_value())