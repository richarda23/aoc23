import pytest
from utils import  file2lines, ints_in_line
from typing import List, Dict
from collections import OrderedDict
import re


def get_matrix(filename):
    return file2lines(filename)

def parse(lines: List[str]):
    rc = OrderedDict() # map of maps
    map_name=""
    for i,l in enumerate(lines):
        l = l.strip()
        if i == 0 and ":" in l:
            rc['seeds']= ints_in_line(l)
        elif ":" in l:
            map_name=re.search(r'[\w\-]+', l).group()
            rc [map_name] = []
        elif re.match(r'\d', l):
            d = ints_in_line(l)
            rc[map_name].append(d)
    return rc

def find (maps:Dict[str, List[List[int]]]):
    seeds = maps['seeds']
    for k,v in list(maps.items())[1:]:
        for seed_idx, seed in enumerate(seeds):
            for s_range in v:
                if seed in range(s_range[1], s_range[1] + s_range[2]):
                    seeds[seed_idx] = s_range[0] + (seed - s_range[1])
    return seeds

def find_part2_by_ranges(maps:Dict[str, List[List[int]]]):
    seeds = maps['seeds']
    min_size = 3000000000
    all_ranges = []
    for k,v in list(maps.items())[1:]:
        for s_range in v:
            all_ranges.append(s_range[1])
            all_ranges.append(s_range[1] + s_range[2])
    sorted_ranges = sorted(all_ranges)
    for i, v in enumerate(sorted_ranges):
        seed
        for j in range(i+1, len(sorted_ranges) -1):
            if sorted_ranges[j]!= v:




def find_part2 (maps:Dict[str, List[List[int]]]):
    seeds = maps['seeds']
    min_size = 3000000000
    for i in range(0,len(seeds),2):
        print (f"rang {i}")
        s_start = seeds[i]
        for seedn in range (s_start, s_start+seeds[i+1]):
            if (seedn % 100000 == 0):
                print (f"{seedn - s_start}/{seeds[i+1]}")
            for k,v in list(maps.items())[1:]:
                    for s_range in v:
                        if seedn in range(s_range[1], s_range[1] + s_range[2]):
                            seedn = s_range[0] + (seedn - s_range[1])
                            if k == 'humidity-to-location' and seedn < min_size:
                                min_size = seedn
                            break

    return min_size



class TestDec5Test:

    def test_process(self):
        lines = get_matrix("./tests/dec5testdata.txt")
        maps  = parse(lines)
        assert 4 == len(maps['seeds'])# number of seeds
        assert 2 == len(maps['seed-to-soil'])

    def test_mapping(self):
        lines = get_matrix("./tests/dec5testdata.txt")
        maps  = parse(lines)
        print(min(find(maps)))

    def test_mapping2(self):
        lines = get_matrix("./tests/dec5testdata.txt")
        maps  = parse(lines)
        result = find_part2_by_ranges(maps)
        print(result)