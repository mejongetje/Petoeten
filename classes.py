import random

class Card:
    def __init__(self, rank, suit, id):
        CARDRANK = [x for x in str('TJQKA')]
        CARDSUIT = ['h','d','s','c']

        self.rank = rank
        self.suit = suit
        self.id = id
        self.name = f'{CARDRANK[rank]}{CARDSUIT[suit]}'
        self.show = True

    def __repr__(self):
        if self.show == True:
            return self.name
        else:
            return ' '

    def __iter__(self):
        return self

    def __lt__(self, other):
        if isinstance(other, Card):
           return self.id < other.id
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Card):
            return self.rank + other.rank

    def __radd__(self, other):
       if other == 0:
           return self
       else:
           return self.__add__(other)
    

    def __eq__(self, other):
       if isinstance(other, Card):
           return self.rank == other.rank         
       else:
           return False
   

class Deck:
    def __init__(self):
        self.deck = []
        num = 0
        for suit in range(4):
            for rank in range(5):
                card = Card(rank,suit,num)
                self.deck.append(card)
                num += 1
                rank += 1

    def __getitem__(self,s):
        return self.deck[s]

    def __iter__(self):
        return self


class Board:
    def __init__(self):
        self.hand = []       
        deck = Deck()
        self.playdeck = deck.deck[:]
        random.shuffle(self.playdeck)
        for i in range(3):
            self.hand.append(self.playdeck[i])
            self.playdeck.remove(self.playdeck[i])
        self.trump = self.playdeck[7]