import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return f"{self.value} of {self.suit}"
        
class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ['Hearts', 'Diamonds', 'Spades', 'Clubs']
                      for value in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']]
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def take_card(self, card):
        self.hand.append(card)
        
    def __repr__(self):
        return f"Player {self.name} with hand {self.hand}"
        
deck = Deck()
deck.shuffle()

player1 = Player("Player 1")
player2 = Player("Player 2")

for i in range(5):
    player1.take_card(deck.deal())
    player2.take_card(deck.deal())
    
print(player1)
print(player2)

