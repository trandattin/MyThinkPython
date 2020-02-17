import random

class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8' ,'9' , '10', 'Jack', 'Queen', 'King']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(rank, suit)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_cards(self, card):
        self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_cards(self.pop_card())

    def deal_hands(self, num_hands, num_cards):
        res = {}
        for i in range(num_hands):
            hand_name = 'hand_num' + str(i+1)
            hand = Hand(hand_name)
            self.move_cards(hand, num_cards)
            self.sort()
            res[hand_name] = hand
        return res

class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label

def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty

hand1 = Hand()
deck = Deck()
deck.shuffle()
res = deck.deal_hands(4, 13)
for k,v in res.items():
    print('Name of player:', k)
    v.sort()
    print(v)

