import pytest
from utils import  file2lines, ints_in_line, MyRange
from typing import List, Dict, Tuple
import re
import math
from collections import Counter
## row, column, pipe
Cell = tuple[int,int,str]
Matrix = List[List[str]]

steps = {
    '|': ((1,0), (-1,0)),
    '-':((0,1), (0,-1)),
    'L':((0,1), (-1,0)),
    'F':((1,0), (0,1)),
    'J':((-1,0), (0,-1)),
    '7':((1,0), (0,-1)),
}

def next(matrix: Matrix, starting: Cell, previous:Cell, current:Cell, v=False):
    path = []
    while current != starting:
        current_pipe = current[2]
        possible_steps = steps[current_pipe]
        for step in possible_steps:
            next_row = current[0] + step[0]
            next_col = current[1] + step[1]
            next_pipe = matrix[next_row][next_col]
            possible_next_cell = (next_row, next_col, next_pipe)
            ## check we are not just reversing back to previous
            if possible_next_cell != previous:
                previous = current
                current = possible_next_cell
                path.append(current)
                if v:
                    print(f"moving to {current}, pathlength is {len(path)}")
                break

    return path
    
def find_start(lines: List[str])->tuple[int, int]:
    row = 0
    col = 0
    for i, l in enumerate(lines):
        s_loc = lines[i].find('S')
        if s_loc != -1:
            return i, s_loc
        
        
def find_loop(area: List[str], start: tuple[int,int]):
    pass

def get_matrix(filename) -> List[str]:
    return file2lines(filename)

class Test10:

    def test_findstart(self):
        lines = get_matrix("tests/dec10data.txt")

        assert(2,0)==find_start(lines)
        prev = (2,0,'F')
        current = (2,1,'J')
        next(lines, prev,prev, current,v=True)
    
    def test_result(self):
        lines = get_matrix("tests/dec10data.txt")
        ## by inspection and calculating start location
        start = (96,101,'L')## the starting step
        current = (96,102,'-')## setting off in any direction
        paths = next(lines, start, start, current,v=True)
        print(len(paths))

    def test_testresult(self):
        lines = get_matrix("tests/dec10testdata.txt")

        pass