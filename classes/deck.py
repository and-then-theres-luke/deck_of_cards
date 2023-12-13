from classes.card import Card
import math
import random

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()
            
    def shuffle_cards(self):
        shuffled_deck = []
        while len(self.cards) > 0:
            selector = math.floor(random.random()*len(self.cards))
            shuffled_deck.append(self.cards[selector])
            self.cards.pop(selector)
        self.cards = shuffled_deck

