import pytest
from utils import  file2lines, ints_in_line, MyRange, split_list, transpose
from typing import List, Dict, Tuple
import re
import math
from collections import Counter


def get_matrix(filename) -> List[str]:
    return file2lines(filename)

def _tilt_sort(cell: str):
    if cell == 'O':
        return 1
    else:
        return 10

def tilt(line: List[str]):
    sublines = split_list(line, '#')
    print(f"sublines are {sublines}")
    sorted_sublines = [sorted(sub, key = _tilt_sort) for sub in sublines]
    return sorted_sublines

def score (line: List[str], v:bool = False):
    """
    Calculates score for line
    """
    item_count = len(line)
    score = 0
    if v:
        print(f"scoring line: {line}")
    for i, cell in enumerate(line):
        if cell == 'O':
            score += item_count - i
    return score
class Test14:
    
    def result(self):
        #lines = get_matrix("tests/dec10data.txt")
        pass

    def test_result(self):
        lines = get_matrix("tests/dec14testdata.txt")
        cols = transpose(lines)

    def test_score(self):
        lines = get_matrix("tests/dec14testdata.txt")
        cols = transpose(lines)
        assert 31 == score(cols[0], v=True)

    def test_transpose(self):
        lines = get_matrix("tests/dec14testdata.txt")
        cols = transpose(lines)
        sorted = tilt(cols[0])
        print(sorted)


    def test_tiltsort(self):
        s = ['d', 'O', 'x', 'O']
        tilted = sorted(s, key=_tilt_sort)
        assert ['O','O', 'd', 'x'] == tilted
        pass