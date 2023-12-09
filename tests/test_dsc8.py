import pytest
from utils import  file2lines, ints_in_line, MyRange
from typing import List, Dict, Tuple
import re
import math
from collections import Counter


def get_matrix(filename) -> List[str]:
    return file2lines(filename)

def _create_graph(lines: List[str]):
    rc = {}
    indexes = lines[0].replace("L", "0").replace("R","1")
    indexes = [int(x) for x in indexes]
    for l in lines[2:]:
        nodes = re.findall(r'\w+', l)
        rc[nodes[0]] = (nodes[1], nodes[2])
    return indexes, rc

def _find_starting_nodes(graph)->List[str]:
    all_paths:Dict = graph[1]
    return [x for x in all_paths.keys()if x[-1]=='A']

def navigate(graph, start_node='AAA',  v=False):
    stepcount = 0
    instructions = graph[0]
    all_paths = graph[1]
    curr= start_node
    while curr[-1] != 'Z':
        for step in instructions:
            curr = all_paths[curr][step]
            stepcount +=1
            if v:
                print (f"moved to {curr}, count = {stepcount}")
            if curr[-1] == 'Z':
                return stepcount

    return stepcount

class Test8:

    def test_result_pt1(self):
        pass
        lines = get_matrix("tests/dec8data.txt")
        graph = _create_graph(lines)
        print(navigate(graph))

    def test_result_pt2_test(self):
        lines = get_matrix("tests/dec8pt2testdata.txt")
        graph = _create_graph(lines)
        starting_nodes = _find_starting_nodes(graph)
        results = [navigate(graph, start_node=n) for n in starting_nodes]
        print(results)
    
    def test_result_pt2_test(self):
        lines = get_matrix("tests/dec8data.txt")
        graph = _create_graph(lines)
        starting_nodes = _find_starting_nodes(graph)
        results = [navigate(graph, start_node=n) for n in starting_nodes]
        print(results)

        print(f"lcm: {lcm(results)}")
    def test_create_graph(self):
        lines = get_matrix("tests/dec8testdata.txt")
        graph = _create_graph(lines)
        assert 3 == len(graph[0])

    def test_navigate(self):
        lines = get_matrix("tests/dec8testdata.txt")
        graph = _create_graph(lines)
        assert 6 == navigate(graph, v=True)
        print (math.lcm(*[16343, 16897, 21883, 20221, 19667, 13019]))

    def test_lcm(self):
        assert 16 == math.lcm(*[2,8,16])