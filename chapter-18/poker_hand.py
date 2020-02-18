from card import*

class Hist(dict):
    def __init__(self, seq = []):
        """A map from each time (x) to its frequency"""
        for x in seq:
            self.count(x)

    def count(self,x, f=1):
        """Increments the countter associated with item x"""
        self[x] = self.get(x, 0 ) + f
        if self[x] == 0:
            del self[x]


class PokerHand(Hand):
    """Represents a poker hand."""

    all_labels = ['straightflush', 'fourkind', 'fullhouse','flust',
                  'straight', 'threekind', 'twopair', 'pair', 'highcard']

    def make_histograms(self):
        """Computes histograms for suits and hands

        Creates attributes:

        suits: a histogram of suits in the hand.
        ranks: a histogram of the ranks
        sets: a sorted list of the rank in the hand
        """

        self.suits = Hist()
        self.ranks = Hist()

        for c in self.cards:
            self.suits.count(c.suit)
            self.rank.count(c.rank)

        self.sets = self.ranks.values()
        self.sets.sort(reverse=True)

    def has_highcard(self):
        """Returns True if this hand has a high card."""
        return len(self.cards)

    def check_sets(self, *t):
        """Checks whether self.sets contains sets that are
        at least as big as the requirements in t

        t: list of int
        """
        for need, have in zip(t, self.sets):
            if need > have: return False
        return True

    def has_pair(self):
        return self.check_sets(2)

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False


    def has_two_pair(self):
        self.rank_hist()
        i = 0
        for val in self.ranks.values():
            if val == 2:
                i +=1
        if i == 2:
            return True
        return False

    def has_three_of_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val == 3:
                return True
        return False

    '''def has_straight(self):
        for i in range(self.cards):
           if self.card[i] - self.card[i+1]
    '''

    def has_full_house(self):
        if self.has_three_of_kind() and self.has_pair():
            return True
        return False



if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.has_full_house())
        print('')

