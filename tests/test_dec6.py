import pytest
from utils import  file2lines
from typing import List, Dict
import re


def get_matrix(filename):
    return file2lines(filename)

def parse(lines):
    ## get list of (time, distance) tuples
    rc= []
    times = re.split(r'\s+', lines[0].strip())[1:]
    times =[int(t) for t  in times]
    distances = re.split(r'\s+', lines[1].strip())[1:]
    distances =[int(d) for d  in distances]
    return list(zip(times, distances))

def process_one(race: tuple):
    is_better_count = 0
    race_duration = race[0]
    distance_to_beat = race[1]
    d_prev = 0
    for charging_t in range(1, race_duration):
        d = charging_t * race_duration - charging_t **2
        print(f"For charging time {charging_t} dist is {d}")
        if d > distance_to_beat:
            is_better_count+=1
        ## we are charging too long and going less far now
        if d < d_prev and d < distance_to_beat:
            break
        d_prev = d
    return is_better_count


def process_all(races: List):
    return [process_one(r) for r in races]

def answer_part1(races:List):
    answers = process_all(races)
    p = 1
    for a in answers:
        p = p *a
    return p

class TestDec6Test:

    def test_process(self):
        assert 4 == process_one((7,9))
        assert 8 == process_one((15,40))
        assert 9 == process_one((30,200))

    def test_parse(self):
        lines = get_matrix("tests/dec6testdata.txt")
        parsed = parse(lines)
        assert 3 == len(parsed)
        assert 7 == parsed[0][0]
        assert 9 == parsed[0][1]
    
    def test_answer_1_test(self):
        lines = get_matrix("tests/dec6testdata.txt")
        races = parse(lines)
        assert 288 == answer_part1(races)
    
    def test_answer_1(self):
        lines = get_matrix("tests/dec6data.txt")
        races = parse(lines)
        print(answer_part1(races))

    