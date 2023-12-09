import pytest
from utils import  file2lines, ints_in_line, MyRange
from typing import List, Dict, Tuple
import re
import math
from collections import Counter


def get_matrix(filename) -> List[str]:
    return file2lines(filename)

def calculate_deltas(seq: List[int]):
    delta_lol:List[List[int]] = [seq]
    
    deltas = _get_deltas(seq)
    delta_lol.append(deltas)
    while all([x== 0 for x in deltas]) is False:
        deltas = _get_deltas(deltas)
        delta_lol.append(deltas)
    return delta_lol

def next_in_seq(delta_lol:List[List[int]])->int:
    delta_lol=delta_lol[::-1]
    for deltas in delta_lol:
        deltas.append(0)
    for idx, deltas in enumerate(delta_lol):
        if idx < len(delta_lol) -1:
            delta_lol[idx+1][-1] = delta_lol[idx+1][-2] + deltas[-1]

    return delta_lol[-1][-1]

def _get_deltas(seq: List[int])->List[int]:
    deltas = []
    for idx, n in enumerate(seq):
        if idx < len(seq) - 1:
            delta = seq[idx+1]- n 
            deltas.append(delta)
    return deltas

def process_line(seq: List[int], verbose=False)->int:
    deltas = calculate_deltas(seq)
    if verbose:
        print(deltas)
    result = next_in_seq(deltas)
    return result


class Test9:

    def test_line1(self):
        seq = [ints_in_line (l) for l in  (get_matrix("dec9data.txt"))]
        result = sum([ process_line(s[::-1]) for s in seq])
        print(result)


    def test_result(self):
        seq = [ints_in_line (l) for l in  (get_matrix("dec9data.txt"))]
        result = sum([ process_line(s) for s in seq])

    def test_result_pt2(self):
        seq = [ints_in_line (l) for l in  (get_matrix("dec9testdata.txt"))]
        result = sum([ process_line(s[::-1]) for s in seq])
        print (result)

    def test_process(self):
        seq = [ints_in_line (l) for l in  (get_matrix("dec9testdata.txt"))]
        assert 18 == process_line(seq[0])
        assert 28 == process_line(seq[1])
        assert 68 == process_line(seq[2])

    def test_next(self):
        seq = [ints_in_line (l) for l in  (get_matrix("dec9testdata.txt"))]
        deltas = calculate_deltas(seq[2])
        assert len(seq) - 1, len(deltas)
