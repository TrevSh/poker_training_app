#This program generates hands and asks the user to decide which
#hand would win in Poker
import random
import pyinputplus as pi

playerInput = pi.inputInt('How many players would you like to play with?(2-8)',
                           max = 8,
                           min = 2,
                           blank = False)

def CreateDeck():
    Suits = {'Spd','Hrt','Clb','Dmd'}
    Cards = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    Deck = []
    for suit in Suits:
        for card in Cards:
            card_key = suit +' '+ card
            Deck.append(card_key)
    random.shuffle(Deck)
    return Deck

def DealHands (Deck : list,Players : int):
    hands = [[] for _ in range(Players)]

    for _ in range(2):
        for i in range(Players):
            card = random.choice(Deck)
            hands[i].append(card)
            Deck.remove(card)
    return hands

#DISPLAY FLOP(3),TURN(1),and RIVER(1). REMOVE ONE CARD BEFORE EACH
def DealTableCards(Deck):
    table = []

    if Deck:
        print('Pre-pop: ',Deck)
        Deck.pop(0)
        print('Post-pop: ',Deck)
        while table.count(table) < 3:
            table.append(Deck.pop(0))
        while table.count(table) < 5:
            Deck.pop(0)
            table.append(Deck.pop(0))

    print(table)

#ASK PLAYER TO GUESS WHICH HAND WILL WIN UNDER A TIME

#CREATE FUNCTION TO ADD TABLE CARDS TO EACH PLAYER CARD AND FIND WINNER
gameDeck = CreateDeck()
DealHands(gameDeck ,playerInput)
print('Deck:', gameDeck)
print('Table:', DealTableCards(gameDeck))