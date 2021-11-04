# The Deck of cards class should inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
import random

suits = list(['Hearts', 'Diamonds', 'Clubs', 'Spades'])
digits = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

class Card:
    def __init__(self, suit, digit):
        self.suit = suit
        self.digit = digit
        
    def __repr__(self):
        return f'{self.digit} of {self.suit}'


   


class Deck:
    def __init__(self):
        self.deck = []
        
    def shuff_cards(self):
        for suit in suits:
            for digit in digits:
                self.deck.append(Card(suit, digit))
        if len(self.deck) == 52:
            random.shuffle(self.deck)
            return self.deck

    def deal(self):
        new_card = random.choice(self.deck)
        self.deck.remove(new_card)
        return new_card

    

deck = Deck()
print(deck.shuff_cards())


print(deck.deal())














# Deck_of_card()

# import random

# deck of cards
# deck = {}

# suits = [{"Heart"}, {"Diamond"}, {"Club"}, {"Spade"}]

# numbers = [{"2"}, {"3"}, {"4"}, {"5"}, {"6"}, {"7"}, {"8"}, {"9"}, {"10"}, {"J"}, {"Q"}, {"K"}, {"A"}]

# for suit in suits:
#   deck["suits"] = [suit]

# for num in numbers:
#   deck["values"] = [num]

# print(deck)

# deck = [{'suit': suit["name"], 'value': number["name"]}
#         for suit in suits for number in numbers]
# print(deck)
















































