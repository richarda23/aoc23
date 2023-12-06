import pytest
from utils import file2lines

def digits(input:str):
        first_char =0
        last_char =0
        for i in input:
              if (i+"").isdigit():
                 first_char = i
                 break
        for i in input[::-1]:
             if (i+"").isdigit():
                last_char = i
                break
        return int(f'{first_char}{last_char}')
s1='two1nine'
s2='eightwothree'
s3='abcone2threexyz'
s4='xtwone3four'
s5='4nineeightseven2'
s6='zoneight234'
s7='7pqrstsixteen'
s8='msixonexch1twokjbdlhchqk1'

numbers = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

def wordToNumber(i):
    if i in numbers:
        return numbers[i]
    else:
        return int(i)
    
def parse(input:str):
    start_index = {k:-1 for k,v in numbers.items()}
    last_index = {k:-1 for k,v in numbers.items()}
    for k,v in numbers.items():
        start_index[k]=input.find(k)
        start_index[str(v)]=input.find(str(v))
        last_index[k]=input.rfind(k)
        last_index[str(v)]=input.rfind(str(v))
    
    existing_first = {k:v for k,v in start_index.items() if v > -1}
    existing_last = {k:v for k,v in last_index.items() if v > -1}
    min_index = min(existing_first.values())
    max_index = max(existing_last.values())

    result = [-1,-1]
    for k,v in existing_first.items():
        if v == min_index:
              result[0] = k
    for k,v in existing_last.items():
        if v == max_index:
              result[1] = k
    
    
    wordsToNumbers = [wordToNumber(k) for k in result ]
    return int(''.join([str(x) for x in wordsToNumbers]))


class TestClass:

    def test_doit(self):
        lines = file2lines("tests/dec1data.txt")

        for l in lines[0:20]:
            print (f"{l} - {parse(l)}")
        result = sum([parse(l) for l in lines])
        print(result)


    def test_part2(self):
        assert parse(s1) == 29
        assert parse(s2) == 83
        assert parse(s3) == 13
        assert parse(s4) == 24
        assert parse(s5) == 42
        assert parse(s6) == 14
        assert parse(s7) == 76
        assert parse(s8) == 61
        total = sum([parse (x) for x in [s1,s2,s3,s4,s5,s6,s7]])
        assert(total == 281)

     
if __name__ == '__main__':
    print("hello")