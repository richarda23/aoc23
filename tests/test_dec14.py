import pytest
from utils import  file2lines, ints_in_line, MyRange, join_list, rotate_grid, split_list, transpose
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

def tilt(line: List[str])->List[str]:
    """
    Tilts an individual line, returning a new line
    """
    sublines = split_list(line, '#')
    sorted_sublines = [sorted(sub, key = _tilt_sort) for sub in sublines]
    return [c for c in join_list(sorted_sublines)]

def tilt_grid(grid: List[List[str]])->List[List[str]]:
    """
    Tilts whole grid
    """
    return [tilt(line) for line in grid]

def score (line: List[str], v:bool = False)->int:
    """
    Calculates score for line
    """
    item_count = len(line)
    total = 0
    for i, cell in enumerate(line):
        if cell == 'O':
            total += item_count - i
    return total

def score_grid(grid: List[List[str]]):
    total = 0
    for col in  grid:
        total += score(col)
    return total

def print_grid(grid: List[List[str]]):
    print ('\n'+'\n'.join(''.join(l) for l in grid))
class Test14:
    
    def result(self):
        #lines = get_matrix("tests/dec10data.txt")
        pass

    def test_p2(self):
        lines = get_matrix("tests/dec14testdata.txt")
        cols = lines #transpose(lines)
        iteration_scores = {}
        tilted = cols
        print("starting position")
        print_grid(tilted)


        for i in range (1):
            ## rotations
            for j in range (0, 4):
                tilted = rotate_grid(tilted, 1)
                tilted = tilt_grid(tilted)
                print_grid(transpose(tilted))
                
            iteration_score = score_grid(tilted)
            print (f"{i}- {iteration_score}")
            if iteration_score not in iteration_scores:
                iteration_scores[iteration_score]=[i]
            else:
                 iteration_scores[iteration_score].append(i)
            if len(iteration_scores[iteration_score]) > 5:
                pass
        

    def test_result(self):
        lines = get_matrix("tests/dec14data.txt")
        cols = transpose(lines)
        total = 0
        for col in  cols:
            total += score([c for c in join_list(tilt(col))])

    def test_score(self):
        lines = get_matrix("tests/dec14testdata.txt")
        cols = transpose(lines)
        assert 31 == score(cols[0], v=True)

    def test_transpose(self):
        lines = get_matrix("tests/dec14testdata.txt")
        cols = transpose(lines)
        tilted = tilt_grid(cols)
        assert 136 == score_grid(tilted)

    def test_tiltsort(self):
        s = ['d', 'O', 'x', 'O']
        tilted = sorted(s, key=_tilt_sort)
        assert ['O','O', 'd', 'x'] == tilted
        pass