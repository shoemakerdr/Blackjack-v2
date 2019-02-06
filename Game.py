from Deck import *
from Hand import *
from Player import *

class Game:
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()
        self.player = Player()

    def replay(self):
        selection = input('Would you like to play again? Enter Y or N: ').upper()
        while selection != 'Y' and selection != 'N':
            selection = input('Invalid Entry. Please try again. ').upper()

        return selection

    def run(self):
        # Game Setup

        player = Player()
        player_hand = Hand()
        dealer_hand = Hand()
        deck = Deck()
        deck.shuffle_cards()
        player.place_bet()
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        player_hand.adjust_for_ace()
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.adjust_for_ace()
        player.show_some(player_hand,dealer_hand)

        # Gameplay

        player.player_turn(deck,player_hand)

        while dealer_hand.hand_value not in range(17,22):
            dealer_hand.add_card(deck.deal_card())
            dealer_hand.adjust_for_ace()

            if dealer_hand.hand_busts(dealer_hand):
                break

        if dealer_hand.hand_busts(dealer_hand):
            player.show_all(player_hand, dealer_hand)
            print('Dealer busts, Player wins!')
            player.chips_total += player.bet
            print('Chip total: {}'.format(player.chips_total))

        if player_hand.hand_value == dealer_hand.hand_value:
            player.show_all(player_hand, dealer_hand)
            print('Push! Dealer and Player tie!')

        if player_hand.hand_value > dealer_hand.hand_value and player_hand.hand_busts(player_hand) == False:
            player.show_all(player_hand, dealer_hand)
            print('Player wins!')
            player.chips_total += player.bet
            print('Chip total: {}'.format(player.chips_total))

        if player_hand.hand_value < dealer_hand.hand_value and dealer_hand.hand_busts(dealer_hand) == False:
            player.show_all(player_hand, dealer_hand)
            print('Dealer wins!')
            player.chips_total -= player.bet
            print('Chip total: {}'.format(player.chips_total))

        if self.replay() == 'Y':
            self.run()

new_game = Game()
new_game.run()