import numpy as np 

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def show(self):
        print("{} of {}".format(self.rank, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.initialize()
    
    def initialize(self):
        for r in range(1,14):
            for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
                self.cards.append(Card(r,s))
