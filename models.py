import random


class Deck(object):

    def __init__(self):
        self.suits = ['h', 'd', 'c', 's']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k', 'a']

        self.cards = []

    def shuffle(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(suit + str(rank))
        random.shuffle(self.cards)

    def deal(self):
        card_index = random.randint(1, len(self.cards))
        card = self.cards[card_index]
        self.cards.pop(card_index)

        if len(self.cards) <= 0:
            print("No cards left. Shuffled Deck")
            return None

        return card


class Player(object):

    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = tuple()
