from Deck import *

class Hand:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.aces = 0
        self.soft = False

    def add_card(self,card):
        self.hand.append(card.card_value())
        self.hand_value += ranks[card.rank]

        if card.rank == 'Ace':
            self.aces += 1
            self.soft = True

    def adjust_for_ace(self):
        while self.aces > 0 and self.hand_value > 21:
            self.hand_value -= 10
            self.aces -= 1

    def hand_busts(self,hand):
        return self.hand_value > 21


    #def is_split(self):
        #return self.hand[0] == self.hand[1]

# test_hand = Hand()
# test_deck = Deck()
# test_hand.add_card(test_deck.deal_card())
# print(test_hand.hand)
