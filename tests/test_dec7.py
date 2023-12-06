import pytest
from utils import  file2lines, ints_in_line, MyRange
from typing import List, Dict, Tuple
import re
import math


def get_matrix(filename) -> List[str]:
    return file2lines(filename)

class TestDec5Test:

    def test_process(self):
        pass

    def print_test_result(self):
        lines = get_matrix("tests/dec7testdata.txt")


    def print_result(self):
        lines = get_matrix("tests/dec7data.txt")
        pass