from classes.deck import Deck
from classes.card import Card
from classes.player import Player

class Game:
    def __init__(self):
        self.turn_counter = False
        self.is_game_over = False

    def go_fish(self, player1,player2):
        print("Let's play Go Fish!")
        print("Opening a fresh deck...")
        deck = Deck()
        print("Shuffling deck...")
        deck.shuffle_cards()
        print("Deck has been shuffled!")
        print("Each player draws seven cards...")
        player1.hand.clear()
        player1.draw_hand(7,deck)
        player2.hand.clear()
        player2.draw_hand(7,deck)
        print(f'''{player1.name} is Player 1, so they will go first.''')
        while self.is_game_over != True:
            if self.turn_counter == False:
                print(f'''{player1.name}'s Turn!''')
                self.is_game_over = self.player_turn(player1, player2, deck)
            if self.turn_counter == True:
                print(f'''{player2.name}'s Turn!''')
                self.is_game_over = self.player_turn(player2, player1, deck)
        
        

    def switch_turn(self):
        if self.turn_counter == False:
            self.turn_counter = True
        else:
            self.turn_counter = False

    def player_turn(self, player, opponent, deck):
        print(f'''Now it is {player.name}'s turn!''')
        card_found = False
        player.show_hand()
        selection_index = input("Which card are you looking to match?")
        selection_index = int(selection_index)
        selected_card = player.hand[selection_index]
        print(f'''You have selected {selected_card.string_val} of {selected_card.suit}''')
        hand_length = len(opponent.hand)
        for card in range(0,hand_length-1):
            if selected_card.point_val == opponent.hand[card].point_val:
                card_found = True
                print(f'''Good guess! {opponent.name} has one of those!''')
                print(f'''{player.name} gained 2 points!''')
                print(f'''Removing card from {player.name}'s hand...''')
                player.hand.pop(selection_index)
                print(f'''Removing card from {opponent.name}'s hand...''')
                opponent.remove_selection_from_hand_by_point_val(selected_card.point_val)
                print(f'''Checking {player.name}'s hand for matches...''')
                player.match_check()
                if len(player.hand) <= 0:
                    self.is_game_over = True
                self.switch_turn()
        if card_found == False:
            print("Sorry, none found.")
            player.draw_card(deck)
            player.match_check()
            self.switch_turn()