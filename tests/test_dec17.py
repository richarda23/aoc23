import pytest
from networkx import Graph

from tests.graph_utils import create_dg_from_matrix
from utils import file2lines, ints_in_line, MyRange, print_grid, copy_grid
from typing import List, Dict, Tuple, Any
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


def dijkstra(graph: Graph, source: Any, target: Any):
    seen = set()
    dists = {i: 10000 for i in graph.nodes}
    dists[source] = 0
    while len(seen) < len(dists):
        u = min([u for u in dists.items() if u[0] not in seen], key=lambda x: x[1])
        print(f"min is {u}")
        print(f"min node is {u}")
        for v in graph.adj[u[0]]:
            if v in seen:
                continue;
            uv_dist = dists[u[0]] + graph.edges[u[0], v]['value']
            if uv_dist < dists[v]:
                print(f"new min value: {uv_dist} for edge {u}:{v}")
                dists[v] = uv_dist
        seen.add(u[0])
        if u[0] == target:
            break
    return dists


class Test17:

    def test_dijkstra(self):
        lines = get_matrix_as_2d_array("dec17testdata.txt")
        graph = create_dg_from_matrix(lines)
        dists = dijkstra(graph, "0-0", "3-3")
        assert 11 == dists["2-2"]
        assert 5 == dists["1-1"]
        assert 21 == dists["3-3"]
        assert 78 == dijkstra(graph, "0-0", "12-12")['12-12']

    def test_eg_simple_sp(self):
        lines = get_matrix_as_2d_array("dec17testdata.txt")
        graph = create_dg_from_matrix(lines)
        sp = nx.shortest_path(graph, "0-0", "3-3", 'value')
        assert 21 == sum_sp_weights(graph, sp)
        assert 5 == sum_sp_weights(graph, nx.shortest_path(graph, "0-0", "1-1", 'value'))
        assert 78 == sum_sp_weights(graph, nx.shortest_path(graph, "0-0", "12-12", 'value'))
