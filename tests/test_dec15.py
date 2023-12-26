import pytest
from utils import file2lines, ints_in_line, MyRange, print_grid, copy_grid
from typing import List, Dict, Tuple
from collections import deque
import re
import math
from collections import Counter


def get_matrix(filename) -> List[str]:
    return file2lines(filename)


def get_matrix_as_2d_array(filename) -> List[List[str]]:
    m = file2lines(filename)
    for i, row in enumerate(m):
        m[i] = [c for c in row]
    return m

# direction of travel
N = (-1, 0)
S = (1, 0)
W = (0, -1)
E = (0, 1)


def move(curr_r: int, curr_c: int, direction:Tuple[int, int]) -> Tuple[int, int]:
    new_row = curr_r + direction[0]
    new_col = curr_c + direction[1]
    return new_row, new_col


def assess(mat: List[List[str]], curr_r: int, curr_c: int, direction: List[Tuple[int, int]]):
    feature = mat[curr_r][curr_c]
    if feature == '.':
        return [direction]
    elif feature == '-':
        if direction == E or direction == W:
            return [direction]
        else:
            return [E, W]
    elif feature == '|':
        if direction == N or direction == S:
            return [direction]
        else:
            return [N, S]
    elif feature == '\\':
        if direction == W:
            return [N]
        elif direction == N:
            return [W]
        elif direction == E:
            return [S]
        else:
            return [E]
    elif feature == '/':
        if direction == W:
            return [S]
        elif direction == N:
            return [E]
        elif direction == E:
            return [N]
        else:
            return [W]
    else:
        print(f"Unknown feature {feature} ")
        raise ValueError(feature)


def _is_in_bounds(mat, row, col) -> bool:
    height = len(mat)
    width = len(mat[0])
    return 0 <= row < height and 0 <= col < width


def _make_empty_mat(mat):
    seen = []
    for r in mat:
        seen.append(['.'] * len(r))
    return seen


def explore(mat: List[List[str]], start_r=0, start_c=0, direction=[E], v=False) ->List[List[str]]:
    seen = _make_empty_mat(mat)
    seen[start_r][start_c] = ('#', direction)

    queue = deque()
    direction = assess(mat, start_r, start_c, direction[0])
    queue.append((start_r, start_c, direction[0]))
    #
    # tuples of row, column, direction

    while len(queue) > 0:
        if v:
            print(f"queue size is {len(queue)}")
        command = queue.popleft()
        new_loc = move(command[0], command[1], command[2])
        if _is_in_bounds(mat, new_loc[0], new_loc[1]):

            # loop detection
            if seen[new_loc[0]][new_loc[1]] == ('#', direction.copy()):
                continue
            else:
                seen[new_loc[0]][new_loc[1]] = ('#', direction.copy())
                direction = assess(mat, new_loc[0], new_loc[1], command[2])
        else:
            continue

        # not splitting and within bounds
        while len(direction) == 1 and _is_in_bounds(mat, new_loc[0], new_loc[1]):
            new_loc = move(new_loc[0], new_loc[1], direction[0])
            if _is_in_bounds(mat, new_loc[0], new_loc[1]):
                if v:
                    print(f" marking {seen[new_loc[0]]}  {seen[new_loc[1]]}  as seen")
                if seen[new_loc[0]][new_loc[1]] == ('#', direction.copy()):
                    break
                else:
                    seen[new_loc[0]][new_loc[1]] = ('#', direction.copy())
                    direction = assess(mat, new_loc[0], new_loc[1], direction[0])

        if len(direction) == 2 and seen[new_loc[0]][new_loc[1]] != ('#', direction.copy()):
            if v:
                print(f"Splitting at {new_loc[0]}, {new_loc[1]} - {direction}")
            queue.append((new_loc[0], new_loc[1], direction[0]))
            queue.append((new_loc[0], new_loc[1], direction[1]))

    if v:
        print("Seen grid")
        print_grid(seen)
    return seen


def score (mat):
    total = 0
    for r in mat:
        total += sum([1 for c in r if c[0] == '#'])
    return total


class Test10:

    def result(self):
        # lines = get_matrix("dec15testdata.txt")
        pass

    def test_explore(self):
        lines = get_matrix_as_2d_array("dec15data.txt")
        seen = explore(lines, 0, 0)
        assert 46 == score(seen)

    def test_real_solution(self):
        optics = get_matrix_as_2d_array("dec15data.txt")
        physics = {0: {'dx': 0, 'dy': -1, '/': [2], '\\': [1], '-': [1, 2]},
                   1: {'dx': -1, 'dy': 0, '/': [3], '\\': [0], '|': [0, 3]},
                   2: {'dx': 1, 'dy': 0, '/': [0], '\\': [3], '|': [0, 3]},
                   3: {'dx': 0, 'dy': 1, '/': [1], '\\': [2], '-': [1, 2]}}
        max_energized = 0
        for direction in range(4):
            for i in range(len(optics)):
                photons = [[-1 if direction == 2 else len(optics) if direction == 1 else 0,
                            -1 if direction == 3 else len(optics) if direction == 0 else 0, direction]]
                photons[0][0], photons[0][1] = i if direction in {0, 3} else photons[0][0], i if direction in {1,
                                                                                                               2} else \
                photons[0][1]
                energized = [[[False for i in range(4)] for x in range(len(optics))] for y in range(len(optics))]
                while photons:
                    photon = photons.pop()
                    photon[0], photon[1] = photon[0] + physics[photon[2]]['dx'], photon[1] + physics[photon[2]]['dy']
                    if 0 <= photon[0] < len(optics) and 0 <= photon[1] < len(optics):
                        new_directions = physics[photon[2]][optics[photon[1]][photon[0]]] if optics[photon[1]][
                                                                                                 photon[0]] in physics[
                                                                                                 photon[2]] else [
                            photon[2]]
                        for new_d in new_directions:
                            if not energized[photon[1]][photon[0]][new_d]:
                                photons.append([photon[0], photon[1], new_d])
                                energized[photon[1]][photon[0]][new_d] = True
                max_energized = max(max_energized, sum([1 for row in energized for cell in row if True in cell]))
        print(max_energized)

    def test_part_2(self):
        lines = get_matrix_as_2d_array("dec15data.txt")
        height = len(lines)
        width = len(lines[0])
        commands = []
        for i in range(width):
            commands.append((0, i, S))
            commands.append((height -1, i, N))
        for i in range(height):
            commands.append((i, 0, E))
            commands.append((i, width-1, W))
        bl_corner = commands[1]
        seen =explore(lines, 109, 4, [N])
        print_grid(seen, lambda x: x[0])

        for c in commands:
            s=score(explore(lines, c[0], c[1], [c[2]]))
            print(f"{c}-{s}")

        scores = [score(explore(lines, c[0], c[1], [c[2]])) for c in commands]
        high = max(scores)
        ## 7547 is too low
        ## 7716 is the real answer
        print (f"high = {max(scores)}")




    def test_result(self):
        lines = get_matrix_as_2d_array("dec15testdata.txt")
        print_grid(lines)

    def test_move(self):
        assert (4,5) == move(4,4, E)
        assert (4,3) == move(4,4, W)
        assert (3,4) == move(4,4, N)
        assert (5,4) == move(4,4, S)
