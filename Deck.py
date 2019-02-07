############################################################################################################
# * imports are generally frowned upon because you're introducing everything from a module into scope,
# which you normally don't want to do. Usually, you want to only import the things you need:
# EXAMPLE:
#   from Card import Card, rank, suit
#
# Additionally, you probably want to name your files in lowercase. I believe that's considered "more 
# pythonic".
############################################################################################################
from Card import *

class Deck:
    """Deck class that holds 6 decks of cards"""
    def __init__(self):
        self.cards = []
        for deck in range(6):
            for rank in ranks:
                for suit in suits:
                    self.cards.append(Card(rank, suit))

    def __str__(self):
        decks = ''
        for card in self.cards:
            decks += '\n' + card.__str__()
        return decks

    def shuffle_cards(self):
        return random.shuffle(self.cards)

    def deal_card(self):
        single_card = self.cards.pop()
        return single_card

# deck = Deck()
# print(deck.deal_card())
# deck.shuffle_cards()
# print(deck)
