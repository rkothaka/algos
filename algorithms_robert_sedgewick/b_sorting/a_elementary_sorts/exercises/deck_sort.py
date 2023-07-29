from enum import Enum
import random

import b_sorting.a_elementary_sorts.insertion_sort as insertion_sort


class Suit(Enum):
    SPADES = 1
    HEARTS = 2
    CLUBS = 3
    DIAMONDS = 4


class Card:
    rank_order = {
        "2": 0, "3": 1, "4": 2, "5":3, "6": 4, "7": 5, "8": 6,
        "9": 7, "10": 8, "Jack": 9, "Queen": 10, "King": 11, "Ace": 12
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit.name}"

    def __lt__(self, other):
        if self.suit.value != other.suit.value:
            return self.suit.value < other.suit.value
        else:
            return self.rank_order[self.rank] < self.rank_order[other.rank]


def build_deck():
    deck = [Card(rank, suit) for suit in Suit for rank in Card.rank_order]
    return deck


if __name__ == '__main__':
    deck_of_cards = build_deck()
    random.shuffle(deck_of_cards)

    for card in deck_of_cards:
        print(card)

    insertion_sort = insertion_sort.InsertionSort()
    insertion_sort.sort(deck_of_cards)

    for card in deck_of_cards:
        print(card)
