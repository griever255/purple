import numpy
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
class Deck(object):
    def __init__(self):
        self.cards = []

    def get_cards(self):
        return self.cards
    
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

    def add_card(self, card):
        if card not in self.cards:
            self.cards.append(card)
        else:
            raise ValueError("Card is already in deck")

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
        else:
            raise ValueError("Card not in the deck")
    
    def __str__(self):
        string = ""
        for i, c in enumerate(self.get_cards()):
            if i == len(self.get_cards())-1:
                string += c.__str__()
            else:
                string += c.__str__() + ", "
        return string
        

def draw_cards(deck, in_play, n):
    """
    Draws n number of cards from the top of the deck
    and adds it to in_play

    Assumes: 
    deck (Deck) is not empty
    in_play (Deck)
    n (int) is the number of cards to draw

    Returns: The resulting deck and in_play cards
    """
    drawn_cards = []
    for draw in range(n):
        drawn_cards.append(random.choice(deck.get_cards()))
        deck.remove_card(drawn_cards[draw])
        in_play.add_card(drawn_cards[draw])
    return deck, in_play

def action_to_cards(action):
    """
    Action (str) and returns (int) number of cards to draw
    """
    action = action.lower()
    options = {
        "purple": 2
    }
    return options[action]

if __name__ == "__main__":
    # Initialize the game with a shuffled deck of 52 cards
    deck = Deck()
    deck.initialize()
    in_play = Deck()
    discard = Deck()
    random.shuffle(deck.cards)

    action = input("What would you like?: ")
    n = action_to_cards(action)
    deck, in_play = draw_cards(deck, in_play, n)
    print(in_play)
    print(deck)
    



