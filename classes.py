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
    

    # def __eq__(self, other):
    #    if isinstance(other, Card):
    #        return self.rank == other.rank         
    #    else:
    #        return False
   

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
        self.hand = [[],[],[]]       
        deck = Deck()
        self.playdeck = deck.deck[:]
        random.shuffle(self.playdeck)
        self.hand[0] = self.playdeck[0:9:3]
        self.hand[1] = self.playdeck[1:9:3]
        self.hand[2] = self.playdeck[2:9:3]
        self.trump = self.playdeck[9:11]
        self.playdeck[0:11] = []


class Player:

    players = []

    def __init__(self, name, type='digital'):
        self.name = name
        self.type = type
        self.bankroll = 100
        self.hand = None
        self.playcard = None
        self.showcard = ' '
        self.trickpoints = 0
        self.dummycards = ['x']*3
        __class__.players.append(self)
        self.position = __class__.players.index(self)
        self.hand_position = __class__.players.index(self)

    def __repr__(self):
        return self.name

p1 = Player('Aunt Sheila')
p2 = Player('Uncle Danny')