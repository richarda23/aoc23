import pytest
from utils import  file2lines, ints_in_line, MyRange
from typing import List, Dict, Tuple
import re
import math
from collections import Counter


def get_matrix(filename) -> List[str]:
    return [l.strip() for l in file2lines(filename)]

def expand(lines:List[str]):
    empty_rows = [i for i,row in enumerate(lines) if row.find('#') == -1]
    empty_cols = []
    col_count = len(lines[0])
    cols = []
    for i in  range(col_count):
        col = [row [i] for row in lines]
        cols.append(col)
        if '#' not in col:
            empty_cols.append(i)
    for row_idx in empty_rows:
        lines.insert(row_idx, '.' * col_count)
    rc = []
    for i,row in enumerate(lines):
        row_l = [c for c in row]
        print(row_l)
        for col in empty_cols:
            row_l.insert(col, '.')

        expanded_r = ''.join(row_l)
        rc.append(expanded_r)

    return rc
    

class Test11:

    def test_expand(self):
        lines = get_matrix("tests/dec11testdata.txt")
        print(lines)
        expanded = expand(lines)
        print(expanded)
        assert 12 == len(expanded)
        assert 13 == len(expanded[0])

        pass
    
    def result(self):
        #lines = get_matrix("tests/dec10data.txt")
        pass

    def test_result(self):
        lines = get_matrix("tests/dec11testdata.txt")

        pass