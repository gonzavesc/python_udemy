import random
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return "The card is {} of {}".format(self.rank, self.suit)
class Deck():
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
             'Ten', 'Jack', 'Queen', 'King', 'Ace')
    def __init__(self):
        print("Creating a Deck")
        self.deck = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.deck.append(Card(rank,suit))
    def __str__(self):
        a = "All the cards are:\n"
        for item in self.deck:
            a = a+item.__str__() + "\n"
        return a
    def shuffle_deck(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop()
class Hand():
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
    def __init__(self):
            self.cards = []
            self.value = 0
            self.aces = 0
    def add_card(self, card):
        self.cards.append(card)
        self.value+=Hand.values[card.rank]
        if card.rank == 'Ace':
            self.aces+= 1
    def adjust_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
class Chips():
    def __init__(self, starting_value=100):
        self.amount = starting_value
        self.bet = 0
    def win_bet(self):
        self.amount += self.bet
    def lose_bet(self):
        self.amount -= self.bet