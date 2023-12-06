import pytest
import re
from utils import  file2lines
from typing import List, Dict


def get_matrix(filename):
    return [x.strip() for x in file2lines(filename)]

def get_matches(rows: List[str]):
    all_numbers = r'\d+'
    
    rc = [list(re.finditer(all_numbers, row)) for row in rows]
    return rc

def get_symbols(rows: List[str]):
    all_symbols = r'[^\d\.]'
    
    rc = [list(re.finditer(all_symbols, row)) for row in rows]
    return rc

def get_gears(rows: List[str]):
    all_gears = r'\*'
    
    rc = [list(re.finditer(all_gears, row)) for row in rows]
    return rc

def is_near_gear(number_rows, gear_rows):
    gear_n_matches = []# array of tuples
    for i,g_row in enumerate(gear_rows):
         for j, g_match in enumerate(g_row):
            numbers_near_gear = []
            g_st, g_end = g_match.span()
            number_above_row_index= i -1
            if number_above_row_index >= 0:
                number_above_row = number_rows[number_above_row_index]
                for n in number_above_row:
                    n_st, n_end = n.span()
                    if g_st >= n_st - 1 and g_st <= n_end:
                        numbers_near_gear.append(int(n.group()))
            number_below_row_index= i +1
            if number_below_row_index < len(gear_rows):
                number_below_row = number_rows[number_below_row_index]
                for n in number_below_row:
                    n_st, n_end = n.span()
                    if g_st >= n_st - 1 and g_st <= n_end:
                        numbers_near_gear.append(int(n.group()))
            n_row_current = number_rows[i]

            for n in n_row_current:
                n_st, n_end = n.span()
                if g_st >= n_st - 1 and g_st <= n_end:
                    numbers_near_gear.append(int(n.group()))
            gear_n_matches.append(numbers_near_gear)
    return gear_n_matches



def is_near_symbol(number_rows, symbol_rows):
    numbers_near_symbol = []
    for i,row in enumerate(number_rows):
        for j, number_match in enumerate(row):
            number_st, number_end = number_match.span()
            symbol_above_row_index= i -1
            if symbol_above_row_index >= 0:
                symbol_above_row = symbol_rows[symbol_above_row_index]
                for s in symbol_above_row:
                    s_st, s_end = s.span()
                    if s_st >= number_st - 1 and s_st <= number_end:
                        numbers_near_symbol.append(int(number_match.group()))
            symbol_below_row_index= i + 1
            if symbol_below_row_index < len(symbol_rows):
                symbol_below_row = symbol_rows[symbol_below_row_index]
                for s in symbol_below_row:
                    s_st, s_end = s.span()
                    if s_st >= number_st - 1 and s_st <= number_end:
                        numbers_near_symbol.append(int(number_match.group()))
            # same_row
            symbol_row_current = symbol_rows[i]
            for s in symbol_row_current:
                s_st, s_end = s.span()
                if s_st >= number_st - 1 and s_st <= number_end:
                        numbers_near_symbol.append(int(number_match.group()))
    return numbers_near_symbol



class TestDec3:


    def test_gears(self):
        lines = get_matrix("tests/dec3data.txt")
        all_numbers = get_matches(lines)
        all_symbols = get_gears(lines)
        result =  is_near_gear(all_numbers, all_symbols)
        pairs = [r for r in result if len(r) == 2]
        result = sum([p[0] * p[1] for p in pairs])
        print(result)
        # assert 467835 == result



    # def test_is_near(self):
    #     lines = get_matrix("tests/dec3data.txt")
    #     all_numbers = get_matches(lines)
    #     all_symbols = get_symbols(lines)
    #     result =  is_near_symbol(all_numbers, all_symbols)
    #     print(result)
   
        
    

    def test_match_numbers(self):
        lines = get_matrix("tests/dec3testdata.txt")
        all_matches = get_matches([lines[0]]);
        for row_match in all_matches:
            for match in row_match:
                st, end = match.span()
                print(st, end, match.group())


    def test_match_symbols(self):
        lines = get_matrix("tests/dec3testdata.txt")
        all_matches = get_symbols(lines);
        assert 10 == len(all_matches)
        assert 0 == len(all_matches[0])
        assert 1 == len(all_matches[1])
        assert 2 == len(all_matches[8])
        for row_match in all_matches:
            for match in row_match:
                st, end = match.span()
                print(st, end, match.group())


    def test_process(self):
        lines = get_matrix("tests/dec3testdata.txt")
        lth = len(lines[0].strip())
        for l in lines:
            assert len(l.strip()) == lth 