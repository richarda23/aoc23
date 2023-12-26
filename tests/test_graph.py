import networkx as nx
import pytest


class TestG:

    def test_nodes(self):
        G = nx.Graph()
        G.add_node(1)
        G.add_node(2)
        G.add_node(3)
        G.add_node(4)
        G.add_edge(1,2)
        G.add_edge(2,3)
        G.add_edge(2,4)
        paths = nx.shortest_path(G,1,4)
        print(paths)