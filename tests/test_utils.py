import pytest
from utils import *

class TestUtils:

    def test_ints_from_line(self):
        line="hgjg 234ghgj456gh-567jj987"
        ints = ints_in_line(line)
        assert 4 == len(ints)
        assert 234 == ints[0]
        assert 456 == ints[1]
        assert -567 == ints[2]
        assert 987 == ints[3]

    def _eval(self, x):
        return  type (x) == str

    def test_is_touching(self):
        grid = [[1,2,3,4,5],[4,5,5,6,7], [4,2,3,4,1]]
        print(is_cell_touching (grid, 0, 4,lambda x : x % 3 ==0))

    def test_range(self):
        r1 = MyRange(0,5)
        assert 5 == r1.size()
        r2 = MyRange(6,7)
        assert 1 == r2.size()
        assert None == r2.intersect(r1)

    def test_range2(self):
        r1 = MyRange(0,5)
        assert 5 == r1.size()
        r2 = MyRange(4,5)
        assert 1 == r2.size()
        r3 = r1.intersect(r2)
        assert 1 == r3.size()
        assert 4 == r3.st
        assert 5 == r3.end

    def test_shift(self):
        r2 = MyRange(4,9)
        r2.shift(3)
        assert 7  == r2.st
        assert 12 == r2.end
    
    def test_equal(self):
        r2 = MyRange(4,9)
        r1 = MyRange(4,9)
        r3 = MyRange(4,10)
        assert r1 == r2
        assert r1 != r3
    
    def test_split(self):
        r1 = MyRange(4,9)
        r2,r3 = r1.split(7)

        assert MyRange(4,7) == r2
        assert MyRange(7,9) == r3

    def test_contains(self):
        r1 = MyRange(4,9)

        assert r1.contains(4)
        assert r1.contains(6)
        assert r1.contains(8)
        assert False == r1.contains(9)

    def test_fragment(self):
        r1 = MyRange(0,5)
        assert 5 == r1.size()
        r2 = MyRange(6,7)
        assert 1 == r2.size()
        ## no overlap, 
        assert 2 == len(r2.fragment(r1))
        assert 2 == len(r1.fragment(r2))

        r3 = MyRange(3,7)
        fragments = r3.fragment(r1)
        assert 3 == len(fragments)
        assert 0 == fragments[0].st
        assert 3 == fragments[1].st
        assert 5 == fragments[2].st

    def test_from_ranges(self):
        r1 = MyRange(3,5)
        r2 = MyRange(8,12)
        r3 = MyRange(82,92)
        all_ranges = MyRange.fromOffsets([r1,r2,r3])
        assert 6 == len(all_ranges)
        assert 0 == all_ranges[0].st
        assert 3 == all_ranges[1].st
        assert 5 == all_ranges[2].st
        assert 8 == all_ranges[3].st
        assert 12 == all_ranges[4].st
        assert 82 == all_ranges[5].st

    def test_swap_args(self):
        r1 = MyRange(18,12)
        assert 12 == r1.st
        assert 18 == r1.end

    def test_copy(self):
        a1 = [ 'hello', 'goodbye']
        a2 = copy_grid(a1)
        a2[0] = 'hola'
        assert 'hello' ==a1[0]
        assert 'hola' ==a2[0]

    def test_splitlist(self):
        input = 'ab*ddd**gg'
        list = [c for c in input]
        subs = split_list(list, splitWord='*')
        assert ['a','b'] == subs[0]
        assert ['*'] == subs[1]
        assert ['d','d','d'] == subs[2]
        assert ['*'] == subs[3]
        assert ['*'] == subs[4]
        assert ['g','g'] == subs[5]
        assert input == join_list(subs)


    def test_splitlist2_no_matches(self):
        list = [c for c in 'abddd']
        subs = split_list(list, splitWord='*')
        assert ['a','b','d','d','d'] == subs[0]
        assert 'abddd' == join_list(subs)

    def test_delimiter_at_end(self):
        list = [c for c in 'abddd**']
        subs = split_list(list, splitWord='*')
        print(subs)
        assert ['a','b','d','d','d'] == subs[0]
        assert ['*'] == subs[1]
        assert ['*'] == subs[2]
        assert 'abddd**' == join_list(subs)

    def test_transpose(self):
        data = [
            ('a', 'b', 'c', 'd'),
            ('a1', 'b1', 'c1', 'd1'),
            ('a2', 'b2', 'c2', 'd2'),
        ]

        l1 = rotate_grid(copy_grid(data), 4)
        assert l1 == data
        l2 = rotate_grid(copy_grid(data), 1)
        assert l2[0] == ('d', 'd1', 'd2')
        l3 = rotate_grid(copy_grid(data), 2)
        assert l3[0] == ('d2', 'c2', 'b2', 'a2')
        l4 = rotate_grid(copy_grid(data), 3)
        assert l4[0] == ('a2', 'a1', 'a')

        cw = rotate_grid(copy_grid(data), -1)
        assert cw == l4


