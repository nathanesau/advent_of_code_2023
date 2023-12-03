from util import read_input, solve, test
import re

def part1(lines):
    total = 0
    config = [{'count': 12, 'type': 'red'}, {'count': 13, 'type': 'green'}, {'count': 14, 'type': 'blue'}]
    for line in lines:
        game_id = int(line.split(": ")[0].split("Game ")[1])
        game_input = line.split(": ")[1]
        cube_sets = [cube_set.split(', ') for cube_set in game_input.split("; ")]
        reveals = []
        for cube_set in cube_sets:
            for entry in cube_set:
                reveals.append({'count': int(entry.split(' ')[0]), 'type': entry.split(' ')[1]})
        # validate against config
        valid = True
        for entry in config:
            max_reveal = max([r for r in reveals if r['type'] == entry['type']], key=lambda x: x['count'])['count']
            if max_reveal > entry['count']:
                valid = False
        if valid:
            total += game_id
    return total

def part2(lines):
    total = 0
    for line in lines:
        game_id = int(line.split(": ")[0].split("Game ")[1])
        game_input = line.split(": ")[1]
        cube_sets = [cube_set.split(', ') for cube_set in game_input.split("; ")]
        reveals = []
        for cube_set in cube_sets:
            for entry in cube_set:
                reveals.append({'count': int(entry.split(' ')[0]), 'type': entry.split(' ')[1]})
        power = 1
        for color in ['red', 'green', 'blue']:
            max_reveal = max([r for r in reveals if r['type'] == color], key=lambda x: x['count'])['count']
            power *= max_reveal
        total += power
    return total

day = __file__.split('day')[-1].split('.py')[0]
solve(part1, day)
solve(part2, day)
#test(part1, ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"])
#test(part2, ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"])