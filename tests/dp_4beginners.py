import pytest
from utils import  file2lines, ints_in_line, MyRange
from typing import List, Dict, Tuple
import re
import math
from collections import Counter


def get_matrix(filename) -> List[str]:
    return file2lines(filename)

def dpsum (n_num: int):
    if n_num == 1:
        return 1
    return n_num + dpsum(n_num-1)

def dpsum2 (n: int):
    cells = [0]*n
    for i in range(1, len(cells)):
        cells[i] = cells[i-1] + i *2
    return cells[-1]

def min_cost_stair_climb(n: int, k:int = 2, costs:List[int]=[]):
    """
    minimizes the cost of climbing the  stairs
    """
    if len(costs) > 0 and len(costs) != n:
        raise ValueError(f"costs must be same length as n")
    ## initialise
    rc = [0] * (n+1)
    rc[1]  =costs[0]
    for i in range (2, n+1):
        mins = []
        for j in range (1,k+1):
            if i - j < 0:
                continue
            mins.append(rc[i-j])
        rc[i] = costs[i-1] + min(mins)
        print(rc)
    return rc[-1]

def stairs (n: int, k:int  = 3, verbose=False ):
    """
    DP solution to caluclate number of ways to climb n stairs k at a time.
    """
    rc = [0] * (n+1)
    rc [0]=1
    for i in range(1,n+1):
        for j in range (1,k+1):
            if i - j < 0:
                continue
            rc[i] = rc[i]  + rc[i-j]
    if verbose:
        print(rc)
    return rc[-1]

class Test10:

    def test_min_cost_stair_climb(self):
        ##
        assert 1 == min_cost_stair_climb(2, 2, [1,1])
        assert 2 == min_cost_stair_climb(2, 1, [1,1])
        assert 3 == min_cost_stair_climb(2, 1, [2,1])
        assert 1 == min_cost_stair_climb(5, 5, [6,6,6,6,1])
        assert 7 == min_cost_stair_climb(5, 4, [6,6,6,6,1])
        assert 7 == min_cost_stair_climb(5, 3, [6,6,6,6,1])
        assert 13 == min_cost_stair_climb(5, 2, [6,6,6,6,1])

    def test_stairs(self):
        assert 1 == stairs(5, k=1, verbose=True)
        assert 8 == stairs(5, k=2, verbose=True)
        assert 13 == stairs(5, k=3, verbose=True)
        assert 15 == stairs(5, k=4, verbose=True)
        assert 16 == stairs(5, k=5, verbose=True)
        
    def test_sum(self):
        assert 10 == dpsum(4)
        assert 55 == dpsum(10)

    def test_sum2(self):
        n = 10
        assert 90 == dpsum2(n)

    def result(self):
        #lines = get_matrix("tests/dec10data.txt")
        pass

    def test_result(self):
        lines = get_matrix("tests/dec10testdata.txt")

        pass