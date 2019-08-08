#Solitaire
'''Writing a program to play the popular card game of solitaire. Suites are represented
by their first letter: 'S', 'D', 'H', 'C'. Each suit has 13 cards from ace,2-10,jack, queen,
king with ranks 1-13. '''



import random
from random import shuffle
import pygame


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    #Implementing build in methods to print card object
    def __str__(self):
        return self.show()

    #Change number values to face cards
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
        #Loop for suits
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            #Each suit 1 - 14
            for val in range(1,14):
                self.cards.append(Card(suit, val))
                

     #Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            #fisher yates shuffle algorithm
            for i in range(length-1, 0, -1):
                #Random index
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
                #Shuffle cards
                random.shuffle(self.cards)


    #Return the top card 
    def deal(self):
        return self.cards.pop()



##Test
#deck = Deck()
#deck.shuffle()
#deck.show()
#card = deck.deal()
#card2 = deck.deal()
#card3 = deck.deal()


#Creates screen
gameDisplay = pygame.display.set_mode((800, 600))
pygame.init()
pygame.display.set_caption('Solitaire')
clock = pygame.time.Clock()
#Color for background
background_color =[12, 222, 9]
gameDisplay.fill(background_color)

#Exit if no cards left
#This will probably not be needed unless have a way to calculate there are no more moves left
no_moves = False
while not no_moves:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            no_moves = True


        print(event)

    pygame.display.update()






    

