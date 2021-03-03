import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """Making deck of 52 cards"""
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(s, v) for s in suits for v in values]

    def count(self):
        """This method returns number of cards in deck"""
        return len(self.cards)

    def __repr__(self):
        """This method returns number of cards remaining in a deck as string."""
        return "Deck of {} cards".format(len(self.cards))

    def _deal(self, number=1):
        """Removes card from deck"""
        if not self.cards:
            raise ValueError("All cards have been dealt")
        if number > len(self.cards):
            number = len(self.cards)
        return [self.cards.pop() for _ in range(number)]

    def shuffle(self):
        """Shuffling deck of cards"""
        if len(self.cards) == 52:
            random.shuffle(self.cards)
            return self.cards
        else:
            raise ValueError("Only full decks can be shuffled")

    def deal_card(self):
        """Dealing one card from deck"""
        deal = Deck()._deal()
        return deal[0]

    def deal_hand(self, num):
        """Dealing hand"""
        return Deck()._deal(num)

print(Deck().deal_card())

