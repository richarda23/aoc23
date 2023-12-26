import pytest

from tests.graph_utils import create_dg_from_matrix
from utils import file2lines, ints_in_line, MyRange, print_grid, copy_grid
from typing import List, Dict, Tuple
from collections import deque
import re
import math
from collections import Counter

import networkx as nx


def get_matrix(filename) -> List[str]:
    return file2lines(filename)


def get_matrix_as_2d_array(filename) -> List[List[str]]:
    m = file2lines(filename)
    for i, row in enumerate(m):
        m[i] = [c for c in row]
    return m


def sum_sp_weights(graph, sp: List[any]):
    """
    takes a graph and array of SPs and calculates the value
    """
    weights = 0
    for i in range(0, len(sp) - 1):
        j = i + 1
        weights = weights + graph.get_edge_data(sp[i], sp[j])['value']
    return weights


class Test17:

    def test_eg_simple_sp(self):
        lines = get_matrix_as_2d_array("dec17testdata.txt")
        graph = create_dg_from_matrix(lines)
        sp = nx.shortest_path(graph, "0-0", "3-3", 'value')
        print(sp)
        assert 21 == sum_sp_weights(graph, sp)
        assert 5 == sum_sp_weights(graph, nx.shortest_path(graph, "0-0", "1-1", 'value'))
