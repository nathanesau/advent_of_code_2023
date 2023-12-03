from util import read_input, solve, test
import math

def part1(lines):
    cfg = [{'cnt': 12, 'type': 'red'}, {'cnt': 13, 'type': 'green'}, {'cnt': 14, 'type': 'blue'}]
    def fn(line):
        game_id, game_input = int(line.split(": ")[0].split("Game ")[1]), line.split(": ")[1]
        csets = [cset.split(', ') for cset in game_input.split("; ")]
        rs = [{'cnt': int(e.split(' ')[0]), 'type': e.split(' ')[1]} for cset in csets for e in cset]
        mc = {e['type']: max([r for r in rs if r['type'] == e['type']], key=lambda x: x['cnt'])['cnt'] for e in cfg}
        return game_id if all([e['cnt'] >= mc[e['type']] for e in cfg]) else 0
    return sum([fn(line) for line in lines])

def part2(lines):
    def fn(line):
        game_id, game_input = int(line.split(": ")[0].split("Game ")[1]), line.split(": ")[1]
        csets = [cset.split(', ') for cset in game_input.split("; ")]
        rs = [{'cnt': int(e.split(' ')[0]), 'type': e.split(' ')[1]} for cset in csets for e in cset]
        mc = [max([r for r in rs if r['type'] == c], key=lambda x: x['cnt'])['cnt'] for c in ['red', 'green', 'blue']]
        return math.prod(mc)
    return sum([fn(line) for line in lines])

day = __file__.split('day')[-1].split('.py')[0]
solve(part1, day)
solve(part2, day)
#test(part1, ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"])
#test(part2, ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"])