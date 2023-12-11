import pytest
from utils import  file2lines, ints_in_line, MyRange
from typing import List, Dict, Tuple
import re
import math
from collections import Counter


def get_matrix(filename) -> List[str]:
    return [l.strip() for l in file2lines(filename)]


def expand_pt2(lines: List[str])->Tuple[List[int], List [int]]:
    empty_rows = [i for i,row in enumerate(lines) if row.find('#') == -1]
    empty_cols = []
    cols = []
    col_count = len(lines[0])

    for i in  range(col_count):
        col = [row [i] for row in lines]
        if '#' not in col:
            empty_cols.append(i)
    return empty_rows, empty_cols



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
    for i,row_idx in enumerate(empty_rows):
        lines.insert(row_idx+i, '.' * col_count)
    rc = []
    for i,row in enumerate(lines):
        row_l = [c for c in row]
        for i,col in enumerate(empty_cols):
            row_l.insert(col + i, '.')

        expanded_r = ''.join(row_l)
        rc.append(expanded_r)

    return rc
    
def find_galaxies(universe: List[str])->List[Tuple[int, int]]:
    galaxies = [(i, j) for i, row in enumerate(universe) for  j,cell in enumerate(row) if universe[i][j] == '#']
    return galaxies


def get_distances_pt2(emptyRowsCols, galaxycoords, multiplier: int):
    distances = 0
    for i, pt in enumerate(galaxycoords):

            if i < len(galaxycoords) -1:
                for j, pt2 in enumerate(galaxycoords):
                    if j > i:
                        emptyRowindexes = emptyRowsCols[0]
                        crossing_rows = 0
                        for emptyRowIndex in emptyRowindexes:
                            minrow = min(pt[0], pt2[0])
                            maxrow = max(pt[0], pt2[0])
                            if emptyRowIndex > minrow and emptyRowIndex < maxrow:
                                crossing_rows = crossing_rows + 1
                        row_dist = (maxrow - minrow) + ((multiplier -1 ) * crossing_rows)

                        emptyColindexes = emptyRowsCols[1]
                        crossing_cols = 0
                        for emptyColIndex in emptyColindexes:
                            mincol = min(pt[1], pt2[1])
                            maxcol = max(pt[1], pt2[1])
                            if emptyColIndex > mincol and emptyColIndex < maxcol:
                                crossing_cols = crossing_cols + 1
                        coldist = (maxcol - mincol) +((multiplier -1 ) * crossing_cols)

                        dist = row_dist + coldist          
                        print(f"dist between {pt} and {pt2} is {dist}")
                        distances += dist
    return distances


class Test11:

    def test_galaxies_pt2(self):
        lines = get_matrix("tests/dec11data.txt")
        ## just gets coords of empty rows and columns
        expanded = expand_pt2(lines)

        ## coords in original
        coords = find_galaxies(lines)
        print (coords)
        dists = get_distances_pt2(expanded, coords, 1000000)
        print(dists)

    def test_galaxies(self):
        lines = get_matrix("tests/dec11testdata.txt")
        expanded = expand(lines)
       # print(expanded)
        coords = find_galaxies(expanded)
        #print(coords)
        distances = 0
        for i, pt in enumerate(coords):

            if i < len(coords) -1:
                for j, pt2 in enumerate(coords):
                    if j > i:
                        dist = abs(pt[0] - pt2[0]) + abs(pt[1] - pt2[1])           
                        # print(f"dist between {pt} and {pt2} is {dist}")
                        distances += dist

        print( distances)

    def test_expand(self):
        lines = get_matrix("tests/dec11testdata.txt")
        expanded = expand(lines)
        assert 12 == len(expanded)
        assert 13 == len(expanded[0])
    
    def result(self):
        #lines = get_matrix("tests/dec10data.txt")
        pass

    def test_result(self):
        lines = get_matrix("tests/dec11testdata.txt")

        pass