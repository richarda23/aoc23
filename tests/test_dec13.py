import pytest
from utils import  file2lines, ints_in_line, MyRange
from typing import List, Dict, Tuple
import re
import math
from collections import Counter


def get_matrix(filename) -> List[str]:
    return file2lines(filename)

class Test14:
    
    def result(self):
        #lines = get_matrix("tests/dec10data.txt")
        pass

    def test_result(self):
        lines = get_matrix("tests/dec13testdata.txt")

        pass