from typing import List, Dict
import pytest
import re
from utils import file2lines

def game_id(linepart:str):
    game_id_re = r'(\d+)$'
    match = re.search(game_id_re, linepart)
    return int(match.group(1))

def parse_line(line:str):
    line_parts1 = line.split(":")
    g_id = game_id(line_parts1[0])
    samples = line_parts1[1].split(";")
    parsed_samples = []
    for s in samples:
        balls = s.split(",")
        sample = {'red':0, 'green':0, 'blue':0}
        for b in balls:
            b = b.strip()
            match = re.search(r'(\d+)\s+(\w+)', b)
            count = int(match.group(1))
            colour = match.group(2)
            sample[colour] = count
        parsed_samples.append(sample)

    return {'id':g_id, 'samples':parsed_samples}

def parse_lines(lines: List[str]):
    return [parse_line(line) for line in lines]

def is_compatible(target, game_samples) -> bool:
    for s in game_samples:
        if s['red'] > target['red'] or  s['blue'] > target['blue'] or  s['green'] > target['green']:
            return False
    return True

def filter_games(target, games:List):
    ok = [ g['id'] for g in games if is_compatible(target, g['samples']) ]
    return ok
    
def result(target:Dict, lines:List) -> int:
    return sum(filter_games(target, parse_lines(lines)))

def game_power(game:List[Dict])->int:
    power = 1
    for col in ['red', 'green', 'blue']:
        power  = power * max([g[col] for g in game])
    return power

class TestDay2:

    def test_iscompatible(self):
        target = {'red':22, 'green':12, 'blue':5}
        game_samples = [
            {'red':22, 'green':12, 'blue':5},
            {'red':21, 'green':11, 'blue':4},
            {'red':1, 'green':1, 'blue':1}
        ]
        assert is_compatible(target, game_samples)
        game_samples[0]['red']=23
        assert is_compatible(target, game_samples) is False

    def test_parse_game_id(self):
        assert 14 ==game_id("Game 14")
        assert 1 ==game_id("Game 1")
    
    def test_parse_line(self):

        game = parse_line("Game 1: 9 red, 2 green, 13 blue; 10 blue, 2 green, 13 red; 8 blue, 3 red, 6 green; 5 green, 2 red, 1 blue")    
        assert 9 == game['samples'][0]['red']
        assert 13 ==  game['samples'][0]['blue']
        assert 2 ==  game['samples'][0]['green']
        assert 10 ==  game['samples'][1]['blue']
        assert 1 ==  game['samples'][-1]['blue']
        assert 5 ==  game['samples'][-1]['green']
        assert 1 == game['id']

    lines = [
        "Game 1: 9 red, 2 green, 13 blue; 10 blue, 2 green, 13 red; 8 blue, 3 red, 6 green; 5 green, 2 red, 1 blue",
        "Game 2: 2 green, 2 blue, 16 red; 14 red; 13 red, 13 green, 2 blue; 7 red, 7 green, 2 blue"
    ]

    def test_parse_lines(self):
        assert 2 == len (parse_lines(self.lines))
        assert 2 == parse_lines(self.lines)[1]['samples'][0]['blue']
        assert 7 == parse_lines(self.lines)[1]['samples'][-1]['green']

    def test_filter(self):
        target = {'red':15, 'green':12, 'blue':15}
        assert [1] == filter_games(target, parse_lines(self.lines))

    def test_result(self):
        target = {'red':12, 'green':13, 'blue':14}
      
        lines =  ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
        assert 8 == result(target, lines)

    def test_real_result1(self):
        target = {'red':12, 'green':13, 'blue':14}

        lines = file2lines("tests/dec2data.txt")
    
    def test_power(self):
        game1 = parse_line("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        game2 = parse_line("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        game3 = parse_line("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        game4 = parse_line("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        game5 = parse_line("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        assert 48 == game_power(game1['samples'])
        assert 12 == game_power(game2['samples'])
        assert 1560 == game_power(game3['samples'])
        assert 630 == game_power(game4['samples'])
        assert 36 == game_power(game5['samples'])

    def test_real_result1(self):

        lines = file2lines("tests/dec2data.txt")
        games = parse_lines(lines)

        result = sum([game_power(g['samples']) for g in games])
        print(result)
    

        
