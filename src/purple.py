import numpy
import random
import pylab
import scipy.stats

#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 10
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 12
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 10
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 10
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers
pylab.rcParams['lines.markersize'] = 10
#set number of examples shown in legends
pylab.rcParams['legend.numpoints'] = 1

correction = {
    1: "Ace",
    11: "Jack",
    12: "Queen",
    13: "King",
}

rev_corr = {
    "Ace": 1,
    "Jack": 11,
    "Queen": 12,
    "King": 13
}

red = ["Hearts", "Diamonds"]
black = ["Spades", "Clubs"]

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
    
    def set_cards(self, cards):
        self.cards = cards
    
    def initialize(self):
        for r in range(1,14):
            for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
                r = correction.get(r, r)
                self.cards.append(Card(r,s))

    def add_cards(self, cards):
        for card in cards:
            if card not in self.cards:
                self.cards.append(card)
            else:
                raise ValueError("Card is already in deck")

    def remove_cards(self, cards):
        for card in cards:
            if card in self.cards:
                self.cards.remove(card)
            else:
                raise ValueError("Card not in the deck")
    
    def __str__(self):
        string = ""
        suit = None
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

    Returns: The resulting drawn cards, deck, and in_play cards
    """
    drawn_cards = []
    for draw in range(n):
        drawn_cards.append(random.choice(deck.get_cards()))
        deck.remove_cards([drawn_cards[draw]])
    in_play.add_cards(drawn_cards)
    return drawn_cards, deck, in_play

def action_to_cards(action):
    """
    Action (str) and returns (int) number of cards to draw
    """
    action = action.lower()
    options = {
        "red orgy": 4,
        "black orgy": 4,
        "rainbow": 3,
        "purple": 2,
        "red": 1,
        "black": 1,
        "higher": 1,
        "lower": 1
    }
    return options[action]

def check_draw(in_play, drawn_cards, action):
    """
    Compares the drawn_cards (list of cards) to action and returns (bool) True or False
    """
    options = {
        "red": [["R"]],
        "black": [["B"]],
        "purple": [["R","B"], ["B","R"]],
        "rainbow": [["R", "B", "R"], ["B","R","B"]],
        "red orgy": [["R", "R", "R", "B"],
                    ["R", "R", "B", "R"],
                    ["R", "B", "R", "R"],
                    ["B", "R", "R", "R"]],
        "black orgy": [["B", "B", "B", "R"],
                       ["B", "B", "R", "B"],
                       ["B", "R", "B", "B"],
                       ["R", "B", "B", "B"]]
    }
    suit_events = ["red", "black", "purple", "rainbow", "red orgy", "black orgy"]
    rank_events = ["higher", "lower", "push"]
    if action in suit_events:
        suits = []
        for card in drawn_cards:
            suit = card.get_suit()
            if suit in red:
                suits.append("R")
            elif suit in black: 
                suits.append("B")
            else:
                raise ValueError("Dragons...")
        if suits in options[action]:
            return True
        else: 
            return False
    elif action in rank_events:
        for card in drawn_cards:
            rank = card.get_rank()
            rank = rev_corr.get(rank, rank)
            prev_rank = in_play.get_cards()[-2].get_rank()
            prev_rank = rev_corr.get(prev_rank, prev_rank)
            draw_is_higher = rank > prev_rank
            if action == "higher":
                return rank > prev_rank
            elif action == "lower":
                return rank < prev_rank
            elif action == "push":
                return rank == prev_rank

        
            



if __name__ == "__main__":
    # Initialize the game with a shuffled deck of 52 cards
    deck = Deck()
    deck.initialize()
    in_play = Deck()
    discard = Deck()
    random.shuffle(deck.cards)

    numTrials = 100000
    numMore3 = 0
    numGood = 0
    numBad = 0
    cards_reached = []
    for i in range(numTrials):
        first = True
        while True:
            if first:
                action = "red"
            else:
                play_rank = in_play.get_cards()[-1].get_rank()
                play_rank = rev_corr.get(play_rank, play_rank)
                if int(play_rank) < 7:
                    action = "higher"
                elif int(play_rank) > 7:
                    action = "lower"
                else:
                    action = "purple"
            first = False
            n = action_to_cards(action)
            if len(deck.get_cards()) < n:
                random.shuffle(discard.cards)
                new_deck = deck.get_cards()+discard.get_cards()
                deck.set_cards(new_deck)
                discard.set_cards([])
            total_cards = int(len(discard.get_cards()))+int(len(in_play.get_cards()))+int(len(deck.get_cards()))
            drawn_cards, deck, in_play = draw_cards(deck, in_play, n)
            result = check_draw(in_play, drawn_cards, action)
            #print(in_play)
            if result:
                #print(f"That's a good {action}!")
                numGood += 1
            else:
                #print(f"Not a good {action}, drink {len(in_play.get_cards())}!")
                cards_reached.append(len(in_play.get_cards()))
                discard.add_cards(in_play.get_cards())
                if len(in_play.get_cards()) >= 3:
                    numMore3 += len(in_play.get_cards())//3
                in_play.set_cards([])
                numTrials += 1
                numBad += 1
                break
    right_perc = round(numGood/(numGood+numBad)*100,2)
    pass_perc = round(numMore3/numTrials*100,2)
    pylab.hist(cards_reached, max(cards_reached), density=True, label="Monte Carlo")
    pylab.title(f'Started with Color\n \
        Cards Guessed Right: {right_perc}%\n\
        We can Say "Pass": {pass_perc}%')
    pylab.xlabel("Sequential # of Cards (Correct Guesses)")
    pylab.ylabel("# of Games")
    hist = numpy.histogram(cards_reached, max(cards_reached))
    hist_dist = scipy.stats.rv_histogram(hist)
    x = numpy.linspace(0,max(cards_reached), 100)
    pylab.plot(x, hist_dist.pdf(x), label="PDF", color="red")
    pylab.plot(x, hist_dist.cdf(x), label="CDF", color="green")
    pylab.legend(loc="best")
    pylab.savefig("StartwColor.png")


