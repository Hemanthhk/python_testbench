#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you and the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()  #Hearts,Diamond,Spade,Clover
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

mycards = [(s,r) for s in SUITE for r in RANKS]
#More primitive implementation
# mycards = []
# for s in SUITE:
#     for r in RANKS:
#         mycards.append((s,r))

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Creating new ordered deck!")
        self.all_cards = mycards

    def shuffle(self):
        print("Shuffling deck")
        shuffle(self.all_cards)

    def split_in_half(self):
        return (self.all_cards[:26],self.all_cards[26:])


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))
    
    def add_card(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        # self.cards.remove(removed_cards)
        return self.cards.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand:Hand):
        self.name=name
        self.hand=hand #Object of Hand class
    
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print(f"{self.name} has placed {drawn_card}")
        print("\n")
        return drawn_card
    
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
    
    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Create a new deck and split into half
d= Deck()
d.shuffle()
half1,half2 = d.split_in_half()

#Create players

comp = Player("Computer",Hand(half1))
name = input("What is your name?")
user = Player(name,Hand(half2))

# Game logic
total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds+=1
    print("Time for a new round!")
    print("Current standings: ")
    print(f"{user.name} has the count: {len(user.hand.cards)}")
    print(f"{comp.name} has the cards: {len(comp.hand.cards)}")
    print("Play a card!")
    print("\n")
    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()


    table_cards.append(c_card)
    table_cards.append(p_card)

    #Compare if the cards are same - For war condition
    if c_card[1] == p_card[1]:
        war_count+=1

        print("War!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add_card(table_cards)
        else:
            comp.hand.add_card(table_cards)
    #Incase of no-war, Just compare the cards
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add_card(table_cards)
        else:
            comp.hand.add_card(table_cards)

print("Game over!, Number of rounds:"+str(total_rounds))
print("War happened "+str(war_count)+" times.")
print("Does the computer still have cards:"+ str(comp.still_has_cards()))
print("Does the human player still have cards?" + str(user.still_has_cards()))

#Who won?
if comp.still_has_cards():
    print("Computer won!")
elif user.still_has_cards():
    print(f"Player: {name} won!")