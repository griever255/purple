import numpy as np 
import random as rand 

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
                correction = {
                    1: "Ace",
                    11: "Jack",
                    12: "Queen",
                    13: "King",
                }
                r = correction.get(r, r)
                self.cards.append(Card(r,s))
    def show(self):
        for c in self.cards:
            c.show()

deck = Deck()
rand.shuffle(deck.cards)
deck.show()

