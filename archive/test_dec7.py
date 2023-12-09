import pytest
from utils import  file2lines, ints_in_line, MyRange
from typing import List, Dict, Tuple
import re
import math
from collections import Counter


def get_matrix(filename) -> List[str]:
    return file2lines(filename)

CardValues = ['A', 'K', 'Q', 'J', 'T', '9','8','7','6','5','4','3','2']

def _is5ofakind(hand:str):
    return _isnofakind(hand, 5)

def _isnofakind(hand:List[str], n: int):
    c = Counter(hand)
    return c.most_common()[0][1] == n

def _is4ofakind(hand:List[str]):
    return _isnofakind(hand, 4)

def _is3ofakind(hand:List[str]):
    return _isnofakind(hand, 3)

def _is_fullhouse(hand:List[str]):
    c = Counter(hand)
    most_common = c.most_common()
    return len(most_common) == 2 and most_common[0][1] == 3

def _is2pair(hand:List[str]):
    c = Counter(hand)
    most_common = c.most_common()
    return len(most_common) == 3 and most_common[0][1] == 2 and most_common[1][1] == 2

def _ispair(hand:List[str]):
    c = Counter(hand)
    most_common = c.most_common()
    return len(most_common) == 4

def _ishighcard(hand:List[str]):
    return len(set(hand)) == 5

def score_hand_by_type(hand:List[str]):
    if _is5ofakind(hand):
        return 10
    elif _is4ofakind(hand):
        return 9
    elif _is_fullhouse(hand):
        return 8
    elif _is3ofakind(hand):
        return 7
    elif _is2pair(hand):
        return 6
    elif _ispair(hand):
        return 5
    else:
        return 4
def score_hand_by_position(hand:List[str]):
    cardsreversed = CardValues[::-1]
    return (cardsreversed.index(hand[0]) * 13 **5 +
     cardsreversed.index(hand[1]) * 13 **4 +
     cardsreversed.index(hand[2]) * 13 **3 +
     cardsreversed.index(hand[3]) * 169 +
     cardsreversed.index(hand[4]) * 13)
 
 

## TODO
## score hands and order by type, print out
## sort by hand value as well

def compare_card(c1, c2):
    if CardValues.index(c1)< CardValues.index(c2):
        return -1
    if CardValues.index(c1)> CardValues.index(c2):
        return 1
    return 0

def sort_cards(cards: List[str]):
    cards.sort(key=lambda c: CardValues.index(c))

class TestDec5Test:

    def test_by_position(self):
        hands = [
            '44664',
            '44256',
            'AAAAA',
            'KK234',
            '234KK',
            'A3456',
            'KKAAA',
            'AAKAA',
        ]
        inorder = sorted(hands, key = score_hand_by_position)
        print(inorder)
    def test_rank_hands(self):
        hands = [
            '44664',
            '44256',
            'AAAAA',
             'KK234',
             'A3456',
            'KKAAA',
            'AAKAA',
        ]
        inorder = sorted(hands, key = score_hand_by_type, reverse = True)
        assert 'AAAAA'== inorder[0]
        assert 'A3456'== inorder[-1]
    def test_is_bigger(self):
        initial_cards = list('A2K57')
        expected = 'AK752'
        sort_cards(initial_cards)
        assert expected == ''.join(initial_cards) 

    def test_is5ofakind(self):
        hand =list('AAAAA')
        hand2 =list('AKAAA')
        assert True == _is5ofakind(hand)
        assert False == _is5ofakind(hand2)

    def test_is3ofakind(self):
        hand =list('AAA23')
        hand2 =list('4A4A4')## full house
        hand3 =list('424A3')
        assert True == _is3ofakind(hand)
        assert True == _is3ofakind(hand2)
        assert False == _is3ofakind(hand3)

    def test_isfull_house(self):
        hand =list('AAA22')
        hand2 =list('4A4A4')## full house
        hand3 =list('424A3')
        assert True == _is_fullhouse(hand)
        assert True == _is_fullhouse(hand2)
        assert False == _is_fullhouse(hand3)

    def test_is4ofakind(self):
        hand =list('AAAAA')
        hand2 =list('AKAAA')
        assert False == _is4ofakind(hand)
        assert True == _is4ofakind(hand2)

    def test_is2pair(self):
        hand = list('AQKKA')
        hand2 =list('42423')
        assert True == _is2pair(hand)
        assert True == _is2pair(hand2)
        assert False == _ispair(hand2)
        assert False == _ispair(hand2)

    def test_is2pair(self):
        hand = list('AQK3A')
        hand2 =list('42423')
        assert True == _ispair(hand)
        assert False == _is2pair(hand)
        assert False == _ispair(hand2)

    def test_process(self):
        pass

    def testprint_test_result(self):
        lines = get_matrix("tests/dec7data.txt")
        hands2score= {}
        for l in lines:
            l=l.strip()
            parts = re.split(r'\s+', l)
            hands2score[parts[0]] = int(parts[1])
        inorder = sorted(list(hands2score.keys()), key = score_hand_by_position,reverse = True)
        inorder2 = sorted(inorder, key= score_hand_by_type, reverse = True)
        sum = 0
        for i, hand in enumerate(inorder2[::-1]):
            rank = i +1
            score = rank *hands2score[hand]
            print(f"score for hand {hand} is {score}")
            sum = sum+ score
        print(sum)


    def print_result(self):
        lines = get_matrix("tests/dec7data.txt")
        pass