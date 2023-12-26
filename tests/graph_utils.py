from typing import List

import networkx as nx

N = (-1, 0)
S = (1, 0)
W = (0, -1)
E = (0, 1)

dir_to_move = {
    'N': N,
    'S': S,
    'E': E,
    'W': W
}
move_to_dir = {
    N: 'N',
    S: 'S',
    E: 'E',
    W: 'W'
}


def is_in_bounds(mat, row, col) -> bool:
    height = len(mat)
    width = len(mat[0])
    return 0 <= row < height and 0 <= col < width


def create_dg_from_matrix(mat: List[List[str]]):
    """
    creates a graph where all cells are connected to all others
    2 edge attributes are added:
    - 'dir': the direction of the edge (N,S,E,W)
    - 'value' the cell value
    The node name is in format 'i-j'
    returns: a network x graph
    """
    G = nx.Graph()
    # add all modes
    for i, row in enumerate(mat):
        for j, cell in enumerate(row):
            for move in (N, S, E, W):
                new_i = i + move[0]
                new_j = j + move[1]
                if is_in_bounds(mat, new_i, new_j):
                    G.add_edge(f"{i}-{j}", f"{new_i}-{new_j}", dir=move_to_dir[move], value=int(mat[i][j]))
    return G