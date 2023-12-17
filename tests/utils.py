import re
from typing import Any, Iterable, List, Dict, Tuple
import math, sys


def file2lines(file_name):
    with open (file_name, 'r') as f:
        lines = f.readlines()
    return [l.strip() for l in lines]

ints = r'\-?\d+'

def ints_in_line(line: str):
    return [int(i) for i in re.findall(ints, line)]

def get_columns(grid: List[str] )->List[List[str]]:
    col_count = len(grid[0])
    cols = []
    for i in  range(col_count):
        col = [row [i] for row in grid]
        cols.append(col)
    return cols

def transpose(grid: List[str]):
    return list(zip(*grid))

def copy_grid(grid : List[str]):
   return [r for r in grid]
    


class MyRange:

    @staticmethod
    def fromOffsets(ranges: List["MyRange"]):
        ### fills in gaps in ranges and returns contiguous block
        ### of ranges
        min_st  = min(r.st for r in ranges)
        max_enf = max(r.end for r in ranges)
        ranges.sort(key = lambda x:x.st)
        rc = []
        if min_st > 0:
            rc.append(MyRange(0, min_st))
        for i, range in enumerate(ranges):
            if i < len(ranges) - 1:
                rc.append(range)
                ## if there's a gap between ranges
                ## fill in 
                if ranges[i+1].st - range.end > 0:
                    rc.append(MyRange(range.end, ranges[i+1].st))
            else:
                rc.append(range)
        return rc
                    
    def __init__(self, st:int, end:int):
        if st > end:
            st,end = end,st
        self.st = st
        self.end = end

    def size(self) -> int:
        return self.end - self.st
    
    def shift(self, offset: int):
        """
        Shifts a range by  an integer offset
        """
        self.st = self.st + offset
        self.end = self.end + offset
    
    def intersect(self, other:"MyRange")->"MyRange":
        """
        Gets a range of the intersection or None if no intersection
        """
        max_start = max(self.st, other.st)
        min_end = min(self.end, other.end)
        
        if max_start < min_end:
            return MyRange(max_start, min_end)
        else:
            return None
    
    def split(self, value:int)-> Tuple["MyRange", "MyRange"]:
        """
        Splits a range into two at the specified value.
        Returns self if value is outside of this range
        """
        if value > self.st and value < self.end:
            return (MyRange(self.st, value), MyRange(value, self.end))
        else:
            return (self)
    
    def _sort(self, ranges: Iterable[Any]):
         ranges.sort(key = lambda x:x.st)
        
    def fragment(self, other: "MyRange")->Tuple:
        """
        Splits overlapping ranges into subranges, returning tuple of 3 ranges.
        If they don't intersect returns the input ranges unchanged
        params: an other range
        """
        r1r2 = [self, other]
        self._sort(r1r2)
        r1 = r1r2[0]
        r2 = r1r2[1]
        intersection = r1.intersect(r2)
        if intersection is None:
            return (self,other)
        else:
            return (
                    MyRange(r1.st, intersection.st),
                    MyRange(intersection.st, intersection.end),
                    MyRange(intersection.end, r2.end),
                    )
        
    def contains(self, value:int)->bool:
        """
        Whether value is in the range or not
        """
        return value >= self.st and value < self.end
        
    def __eq__(self, __value: object) -> bool:
        return self.st ==  __value.st  and self.end == __value.end
        
    def __str__(self) -> str:
        return f"{self.st}-{self.end}"
    
    def __repr__(self):
        return f"MyRange({self.st}, {self.end})"



def get_neighbour_coords(i:int, j:int, row_count:int, col_count:int):
    south=(i+1, j)
    south_east=(i+1, j+1)
    east=(i, j+1)
    north_east=(i-1, j+1)
    north=(i-1, j)
    north_west=(i-1, j-1)
    west=(i, j-1)
    south_west= (i+1, j-1)
    if i == 0:
        if j == 0:
            return [south, south_east, east]
        elif j == col_count - 1:
            return [west, south_west, south]
        else:
            return [west, south_west, south, south_east, east]
    elif i == row_count - 1:
        if j == 0:
            return [north, north_east, east]
        elif j == col_count - 1:
            return [west, north_west, north]
        else:
            return [west, north_west, north, north_east, east]
    elif j == 0:
        return [north, north_east, east, south_east, south]
    elif j == col_count - 1:
        return [north, north_west, west, south_west, south]
    else:
        return [west, north_west, north, north_east, east, south_east, south, south_west]
        
def is_touching(grid:List[List], evaluation_func):
    row_count=len(grid)
    col_count = len(grid[0])
    touching_coords = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            neighbours = get_neighbour_coords(i, j, row_count, col_count)

            for n in neighbours:
                val = grid[i,j]
                if evaluation_func(val):
                    touching_coords.append( (i,j,val))
    return touching_coords


def is_cell_touching(grid:List[List],i:int,j:int, evaluation_func):
    """
    given grid of rows and columns, gets the neighbours of row i, column j.
    For each neighbour evaluates the function, if it's true adds to match
    """
    row_count=len(grid)
    col_count = len(grid[0])
    neighbours = get_neighbour_coords(i, j, row_count, col_count)
    touching_coords = []
    for n in neighbours:
        val = grid[n[0]][n[1]]
        if evaluation_func(val):
            touching_coords.append( (n[0],n[1],val))

    return touching_coords