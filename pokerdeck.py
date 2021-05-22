import random as rnd

# Add here new language name for: Suits, Card Values as a list and Separator as a String 
lang_suits = [["Cuori", "Fiori", "Quadri", "Picche"], ["Clubs", "Diamonds", "Hearts", "Spades"]]
lang_values = [["Asso", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"], ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
lang_sep = ["di", "of"]

# Set here language index for Suits and Values and Separator
LANG_IT = 0 # is the first position in the list of language suits, language Values, Language separator
LANG_EN = 1 # is the second position in the list of language suits, language Values, Language separator
# LANG_XX = 2
# LANG_XX = 3

# Set here the correct languge you want
CURR_LANG = LANG_IT


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def getValue(self):
        return self.value
    
    def getSuit(self):
        return self.suit
    
    def __str__(self):
        return f"{self.value} { lang_sep[CURR_LANG] } {self.suit}"


class Deck:
    def __init__(self):
        rnd.seed()
        self.cards = []
        self.init()
    
    def init(self):
        if CURR_LANG == LANG_IT:
            for suit in lang_suits[CURR_LANG]:
                for value in lang_values[CURR_LANG]:
                    card = Card(value, suit)
                    self.cards.append(card)
        elif CURR_LANG == LANG_EN:
            for suit in lang_suits[CURR_LANG]:
                for value in lang_values[CURR_LANG]:
                    card = Card(value, suit)
                    self.cards.append(card)


    def shuffleCards(self):
        rnd.shuffle(self.cards)

    def showRandomCard(self):
        return self.cards[rnd.randint(0, 51)]
    
    def showCardAtPosition(self, index):
        if index >= 0 and index <= 51:
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
            return self.cards.pop(rnd.randint(0, 51))
        else:
            return None


