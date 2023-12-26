import pytest
from utils import  copy_grid, file2lines,transpose, ints_in_line, get_columns, MyRange
from typing import List, Dict, Tuple
import re
import math
from collections import Counter


def get_matrix(filename) -> List[str]:
    return file2lines(filename)

def parse_puzzles(lines: List[str])->List[List[str]]:
    puzzles = []
    current = []
    for l in lines:
        if len(l) ==0:
            puzzles.append(current)
            current = []
            continue
        else:
            current.append(l)
    puzzles.append(current)
    return puzzles

def _doreflection(puzzle: List[str], v:bool = False, ):
    row_count = len(puzzle)
    reflection_rows = []
    for i, row in enumerate(puzzle):
        if i < row_count -1:
            if puzzle[i+1] == row:
                if v:
                    print(f"row {i} equals row {i+1}")
                ## we've got a line of symmetry between i and i+1
                ## check if it's perfect symmetry
                d1 = i
                d2 = i+1
                offset = 0
                is_perfect = True
                while d1 -offset >= 0 and d2 + offset<= row_count-1:
                    row1 = puzzle[d1 - offset]
                    row2 = puzzle[d2 + offset]
                    if v:
                        print (f"comparing {row1} with {row2}")
                    if row1 != row2:
                        is_perfect = False
                        break
                    offset+=1
                if is_perfect:
                    reflection_rows.append( i+1)
    return reflection_rows

def calculate_1diff(puzzle: List[str], original_results: int, v:bool = False):
    for i in range(0, len(puzzle)-1):
        for j in range (i+1,len(puzzle)):

            diff_count = [puzzle[j][k] ==puzzle[i][k] for k in range(len(puzzle[0]))]
            if sum([d==False for d in diff_count]) == 1:
                if v:
                    print(f"{i} and {j} differ by one")
                copy = copy_grid(puzzle)
                ## make them the same so they reflect
                copy[i]=copy[j]
                reflections = _doreflection(copy)
                print(f"reflections are {reflections}, original = {original_results}")
                result = [ x for x in reflections if x not in  original_results]
                if len(result) > 0 and result[0] > 0:
                    if v:
                        print(f"has reflection at {result}")
                    return result[0]
    return 0

def analyze_puzzle(puzzle: List[List[str]], v= False):
    # rows

    row_reflections = _doreflection(puzzle)  
    puzzle_cols = transpose(puzzle)
    col_reflections = _doreflection(puzzle_cols)
    original = (row_reflections, col_reflections)
    print("row diff:")
    row_diff = calculate_1diff(puzzle, original[0], v=True)
    print("col diff:")
    col_diff = calculate_1diff(puzzle_cols, original[1], v=True)
    print (f"origgrow-{row_reflections}, origcol-{col_reflections}, rowdiff {row_diff}, coldiff {col_diff}")
    if row_diff > 0:
        return 100 * row_diff
    else:
        return col_diff

   

def analyse_puzzles(puzzles: List[List[str]]):
   results = [analyze_puzzle(p, v=True) for p in puzzles]
   return results

def analyse_puzzle_pt2(puzzles: List[List[str]]):
    return sum([analyze_puzzle(p) for p in puzzles])



class Test14:
    
    def test_result(self):
        lines = get_matrix("dec14data.txt")
        puzzles = parse_puzzles(lines)
        print(analyse_puzzles(puzzles[5:6]))
        print(analyse_puzzle_pt2(puzzles))
        ## 39291 too high  
        ## 37269 too low  

    # def test_testresult(self):
    #     lines = get_matrix("tests/dec14testdata.txt")
    #     puzzles = parse_puzzles(lines)
    #     assert 4 == len(puzzles)
    #     assert 7 == len(puzzles[0])
    #     assert 7 == len(puzzles[1])

    def test_parsegames(self):
        lines = get_matrix("tests/dec14testdata.txt")
        puzzles = parse_puzzles(lines)
        # assert 300 == analyze_puzzle(puzzles[0], v=False)
        # assert 100 == analyze_puzzle(puzzles[1], v=False)
        # assert 1 == analyze_puzzle(puzzles[2], v=False)
    #     assert 5 == analyze_puzzle(puzzles[4], v=False)
    #     assert 1 == analyze_puzzle(puzzles[5], v=False)
    #     assert 0 == analyze_puzzle(puzzles[6], v=False)
    #     assert 405 == analyse_puzzles(puzzles[0:2])
        # print(analyse_puzzles(puzzles[:2]))

    def test_zip(self):
        a='dasdfsf'
        b='dfgdfgg'
        c= list(zip(a,b))
        assert [[1,2,3,4],[5,6,7,8]] == [[1,2,3,4],[5,6,7,8]]  

