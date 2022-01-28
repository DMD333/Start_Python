class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self):
        suits = ['Hearts', 'diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for value in values for suit in suits]
        print(self.cards)

# -----------------------OLD METHOD---------------------------
        # for value in values:
        #     for suit in suits:
        #         self.cards.append(Card(value, suit))
        # print(self.cards)
# ------------------------------------------------------------

    def __repr__(self):
        return f'Deck of {self.cards} cards'

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        count = self.count()
        actual = min([count, number])
        if count == 0:
            raise ValueError('All cards have been dealt')
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    #
    # def shuffle(self):
    #     if
    #         return
    #     else:
    #         raise ValueError('Only full deks can be shuffled')
    #
    # def deal_cards(self):
    #     return
