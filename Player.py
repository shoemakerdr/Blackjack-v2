from Deck import *
from Hand import *

class Player:
    def __init__(self):
        self.chips_total = 100
        self.bet = 0
        self.deck = Deck()
        self.hand = Hand()

    def place_bet(self):
        while True:
            try:
                self.bet = int(input('How many chips would you like to bet? '))
            except:
                print('Invalid bet. Please try again')
                self.bet = int(input('Please enter a valid bet'))
            else:
                if self.bet > self.chips_total:
                    print('Bet cannot exceeed total! You have: {}'.format(self.chips_total))
                    self.bet = int(input('Please enter a valid bet: '))
                else:
                    break

    def hit(self,deck,hand):
        single_card = deck.deal_card()
        hand.add_card(single_card)
        hand.adjust_for_ace()

    #def split(self,deck,hand):
        #hand.pop_card()
        #single_card = deck.deal_card()
        #hand.add_card(single_card)
        #hand.adjust_for_ace()

    def double_down(self,deck,hand):
        if self.bet * 2 > self.chips_total:
            print('Not enough chips to double down! Current bet would exceed chip total')
        else:
            self.bet = self.bet * 2
            single_card = self.deck.deal_card()
            hand.add_card(single_card)
            hand.adjust_for_ace()

    def show_some(self,player_hand,dealer_hand):
        print('\n')
        print("Dealer's Hand: ")
        print('<card hidden>')
        print(dealer_hand.hand[1])
        print('\n')
        print("Player's Hand:")
        print(player_hand.hand)
        print('Player Total: {}'.format(player_hand.hand_value))

    def show_all(self,player_hand, dealer_hand):
        print('\n')
        print("Dealer's Hand: ")
        print(dealer_hand.hand)
        print('Dealer Total: {}'.format(dealer_hand.hand_value))
        print('\n')
        print("Player's Hand:")
        print(player_hand.hand)
        print('Total: {}'.format(player_hand.hand_value))

    ############################################################################################################
    # Seems like there's a bunch of stuff in here that may belong in the Game class. Generally, you want a
    # method/function to do ONE thing
    ############################################################################################################
    def player_turn(self,deck,hand):
        first_turn = True
        turn = True
        while turn:
            if first_turn:
                selection = input('Hit, Stand, or Double Down? Enter H, ST, or DD: ').upper()

                if selection == 'H':
                    self.hit(deck,hand)
                    self.show_some(hand,hand)
                    if hand.hand_busts(hand):
                        print('Player busts!')
                        self.chips_total -= self.bet
                        print('Chip total: {}'.format(self.chips_total))
                        break
                    first_turn = False

                elif selection == 'ST':
                    break

                elif selection == 'DD':
                    self.double_down(deck,hand)
                    self.show_some(hand,hand)
                    if hand.hand_busts(hand):
                        print('Player busts!')
                        self.chips_total -= self.bet
                        print('Chip total: {}'.format(self.chips_total))
                    break
                else:
                    print('Invalid entry. Please try again')
                    continue
            else:
                selection = input('Hit or Stand? Enter H or ST: ').upper()

                if selection == 'H':
                    self.hit(deck,hand)
                    self.show_some(hand,hand)
                    if hand.hand_busts(hand):
                        print('Player busts!')
                        self.chips_total -= self.bet
                        print('Chip total: {}'.format(self.chips_total))
                        break

                elif selection == 'ST':
                    break

                else:
                    print('Invalid entry. Please try again')
                    continue

# player_hand = Hand()
# dealer_hand = Hand()
# test_player = Player()
# test_player.show_all(player_hand,dealer_hand)
