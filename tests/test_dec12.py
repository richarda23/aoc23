import pytest
from utils import  file2lines, ints_in_line, MyRange
from typing import List, Dict, Tuple
import re
import math
from collections import Counter


def get_matrix(filename) -> List[str]:
    return file2lines(filename)

def process_line(line: str):
    parts = re.split(r'\s+', line)
    records= parts[0]
    blocks = re.split(',', parts[1])
   
    res=[f"#{{{block}}}" for block in blocks]
    res2 = '.*' + '.+'.join(res) + '.*'
    print(res2)
    ## to do brute force
    ## change each ? to either # or .
    ## then see if matches, increment count if so
    for i,c in enumerate(records):
        if c == '?':
            test_record1 = records[:i] + '.' + records[i:]
            test_record2 = records[:i] + '#' + records[i:]
    return 0

class Test12:
    
    def result(self):
        #lines = get_matrix("tests/dec12testdata.txt")
        pass

    def test_result(self):
        lines = get_matrix("tests/dec12testdata.txt")
        result = sum([process_line(l) for l in lines])
        print(result)
        pass