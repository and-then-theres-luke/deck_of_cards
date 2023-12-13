class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.hand = []

    def draw_hand(self, int, deck):
        i = 0
        while i < int:
            self.draw_card(deck)
            i+=1
        return self
    
    def draw_card(self,deck):
        if len(deck.cards) >= 0:
            new_card = deck.cards[0]
            self.hand.append(new_card)
            deck.cards.pop(0)
            print(f'''{self.name} just drew a card...''')
        else:
            print("Cannot draw any more cards")
        return self
    
    def show_hand(self):
        if len(self.hand) <= 0:
            print("Hand is empty.")
        else:
            for i in range(0,len(self.hand)):
                print(f'''[{i}] - {self.hand[i].string_val} of {self.hand[i].suit}''')
        
    def remove_selection_from_hand_by_point_val(self, point):
        hand_length = len(self.hand)
        for i in range(0,hand_length):
            if self.hand[i].point_val == point:
                self.hand.pop(i)
                break
            else:
                pass
            
    def match_check(self):
        dummy_hand = []
        for i in range(0, len(self.hand)):
            for x in range(0,len(self.hand)):
                if self.hand[i] == self.hand[x]:
                    print(self.hand[i])
                elif self.hand[i].point_val == self.hand[x].point_val:
                    self.hand[i] = False
                    self.hand[x] = False
                    for i in range(0,len(self.hand)):
                        if self.hand[i] == False:
                            pass
                        else:
                            dummy_hand.append(self.hand[i])
                    print(dummy_hand)
                    self.hand = dummy_hand
                    self.show_hand()
                    self.points+=2
                    print(f'''{self.name} has a match! 2 points were added.''')
                    return self