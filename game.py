#Solitaire
'''Writing a program to play the popular card game of solitaire. Suites are represented
by their first letter: 'S', 'D', 'H', 'C'. Each suit has 13 cards from ace,2-10,jack, queen,
king with ranks 1-13. '''



import random
from random import shuffle

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def get_rank():
        return [ "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King" ]

    def get_suit():
        return ["Clubs", "Diamonds", "Hearts", "Spades"]

    def get_value():
        pass
 
    def shuffle():
        pass

    def deal():
        pass

    def empty():
        pass

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.contents = []
        self.contents = [ Card(rank,suit) for rank in get_rank() for suit in get_suits()]
        random.shuffle(self.contents)


    

