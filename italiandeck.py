import random as rnd



class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def getValue(self):
        return self.value
    
    def getSuit(self):
        return self.suit
    
    def __str__(self):
        return f"{self.value} di {self.suit}"


class Deck:
    def __init__(self):
        rnd.seed()
        self.cards = []
        self.init()
    
    def init(self):
        for suit in ["Bastoni", "Coppe", "Denari", "Spade"]:
            for value in ["Asso", "2", "3", "4", "5", "6", "7", "8", "9", "Re"]:
                card = Card(value, suit)
                self.cards.append(card)

    def shuffleCards(self):
        rnd.shuffle(self.cards)

    def showRandomCard(self):
        return self.cards[rnd.randint(0, 39)]
    
    def showCardAtPosition(self, index):
        if index >= 0 and index <= 39:
            return self.cards[index]
        else:
            return None

    def drawCard(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def drawCardAtPosition(self, index):
        if len(self.cards) > 0:
            return self.cards.pop(index)
        else:
            return None

    def drawRandomCard(self):
        if len(self.cards) > 0:
            return self.cards.pop(rnd.randint(0, 40))
        else:
            return None

