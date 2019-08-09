#print(os.getcwd())
#Solitaire
'''Writing a program to play the popular card game of solitaire. Suites are represented
by their first letter: 'S', 'D', 'H', 'C'. Each suit has 13 cards from ace,2-10,jack, queen,
king with ranks 1-13. '''


import os
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
gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.init()
pygame.display.set_caption('Solitaire')
clock = pygame.time.Clock()
#Color for background
background_color =[41, 194, 76]
gameDisplay.fill(background_color)






'''_image_library = {} <--- use for later
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image'''


cardImg = pygame.image.load(r'C:\Users\Kevin Steven Moreno\Desktop\Git\Solitaire\img\2_of_clubs.png')



def card(x,y):
    gameDisplay.blit(cardImg, (x,y))

    
def main():
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            print(event)

        #First foundation
        pygame.draw.rect(gameDisplay, [0,0,0], (900, 125, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (905, 130, 140, 200))
        #Second foundation
        pygame.draw.rect(gameDisplay, [0,0,0], (1100, 125, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (1105, 130, 140, 200))
        #Third foundation
        pygame.draw.rect(gameDisplay, [0,0,0], (1300, 125, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (1305, 130, 140, 200))
        #Fourth foundation
        pygame.draw.rect(gameDisplay, [0,0,0], (1500, 125, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (1505, 130, 140, 200))
            
        #Tableau - 1
        pygame.draw.rect(gameDisplay, [0,0,0], (300, 350, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (305, 355, 140, 200))
        
        #Tableau - 2
        pygame.draw.rect(gameDisplay, [0,0,0], (500, 350, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (505, 355, 140, 200))
        #Tableau - 3
        pygame.draw.rect(gameDisplay, [0,0,0], (700, 350, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (705, 355, 140, 200))
        #Tableau - 4
        pygame.draw.rect(gameDisplay, [0,0,0], (900, 350, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (905, 355, 140, 200))
        #Tableau - 5
        pygame.draw.rect(gameDisplay, [0,0,0], (1100, 350, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (1105, 355, 140, 200))
        #Tableau - 6
        pygame.draw.rect(gameDisplay, [0,0,0], (1300, 350, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (1305, 355, 140, 200))
        #Tableau - 7
        pygame.draw.rect(gameDisplay, [0,0,0], (1500, 350, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (1505, 355, 140, 200))
        

        #The stock - 1
        pygame.draw.rect(gameDisplay, [0,0,0], (300, 125, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (305, 130, 140, 200))
        #The stock - 2
        pygame.draw.rect(gameDisplay, [0,0,0], (500, 125, 150, 210))
        pygame.draw.rect(gameDisplay, [41,194,76], (505, 130, 140, 200))

        #Update screen
        card(50, 150)
        pygame.display.update()
        clock.tick(60)
main()




    

