#Solitaire
'''Writing a program to play the popular card game of solitaire. Suites are represented
by their first letter: 'S', 'D', 'H', 'C'. Each suit has 13 cards from ace,2-10,jack, queen,
king with ranks 1-13. '''



import random
from random import shuffle

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    #Implementing build in methods to print card object
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()

    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return "{} of {}".format(val, self.suit)
        
   #''' def get_rank():
        #return [ "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King" ]

    #def get_suit():
        #return ["Clubs", "Diamonds", "Hearts", "Spades"]

   # def get_value():
        #pass'''


    def deal():
        pass

    def empty():
        pass


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    #Display all cards in the deck
    def show(self):
        for card in self.cards:
            print(card.show())

    #Generate 52 cards
    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(1,14):
                self.cards.append(Card(suit, val))

     #Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            #fisher yates shuffle algorithm
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                #Can also use the build in shuffle method
                #random.shuffle(self.cards)


    #Return the top card
    def deal(self):
        return self.cards.pop()


card = Card('Spades', 6)
print(card.show())
myDeck = Deck()
myDeck.shuffle()
myDeck.show()





    

