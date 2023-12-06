import pytest
from utils import  file2lines, ints_in_line
from typing import List, Dict
import re

def card_id(linepart:str):
    game_id_re = r'(\d+)$'
    match = re.search(game_id_re, linepart)
    return int(match.group(1))

def get_matrix(filename):
    return file2lines(filename)
#Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53

def parse_line(line):
    id = card_id(line)
    l = line.split(":")
    parts = l[1].split("|")
    winnings = ints_in_line(parts[0])
    actual = ints_in_line(parts[1])
    return {'id':id, 'winning': winnings, 'actual':actual, 'copies':1}

def parse_lines(lines):
    return [parse_line(l.strip()) for l in lines]


def winning(card):
    w = set(card['winning'])
    a = set(card['actual'])
    mywin = w.intersection(a)
    card['my_win'] = list(mywin)
    return

def get_winning(cards):
    return [winning(c) for c in cards]

def score_card(card):
    if len(card['my_win']) > 0:
        return 2** (len(card['my_win']) - 1)
    else:
        return 0
    
def count_matches(card):
    return len(card['my_win']) 

def count_all_matches(cards: List):
    for c in cards:
        c['match_count']=  count_matches(c)

def score_copies(cards: List):
    ## for each card
    for i, c in enumerate(cards):
        score = count_matches(c)
        ## for each copy of the card
        for j in range(0,c['copies']):
            ## update 'score' cards below by 1
            for k in range (i+1, i+score+1):
                cards[k]['copies'] += 1


def score(cards: List):
    for i, c in enumerate(cards):
        score = score_card(c)
        c['score'] = score
    return sum([ score_card(c) for c in cards])
class TestDec4:


    def test_count(self):
        cards = get_matrix("tests/dec5data.txt")
        cards = parse_lines(cards)
        get_winning(cards)
        score_copies(cards)
        print(sum([x['copies'] for x in cards] ))

    def test_match_count(self):
        cards = get_matrix("tests/dec5testdata.txt")
        cards = parse_lines(cards)
        get_winning(cards)
        count_all_matches(cards)
        assert 4 == cards[0]['match_count']
        assert 2 == cards[1]['match_count']
        assert 0 == cards[5]['match_count']

    def test_process(self):
        cards = get_matrix("tests/dec5testdata.txt")
        cards = parse_lines(cards)
        for c in cards:
            assert 5 == len(c['winning'])
            assert 8 == len(c['actual'])

    def test_winning_cards(self):
        cards = get_matrix("tests/dec5testdata.txt")
        cards = parse_lines(cards)

        get_winning(cards)
        assert 13 == score(cards)
    
    def test_result(self):
        cards = get_matrix("tests/dec5data.txt")
        cards = parse_lines(cards)

        get_winning(cards)
