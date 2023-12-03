from util import read_input, solve, test
import re

def part1(lines):
    def fn(line):
        digits = [int(c) for c in line if c.isdigit()]
        return int(str(digits[0]) + str(digits[-1]))
    return sum([fn(line) for line in lines])

def part2(lines):
    iw_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    iw_map = {v: str(i+1) for i, v in enumerate(iw_list)}
    def fn(line):
        d = [(i, c) for i, c in enumerate(line) if c.isdigit()]
        w = [(match.start(), iw_map[iw]) for iw in iw_list for match in re.finditer(iw, line)]
        return int(min(d + w, key=lambda x: x[0])[1] + max(d + w, key=lambda x: x[0])[1])
    return sum(fn(line) for line in lines)

day = __file__.split('day')[-1].split('.py')[0]
solve(part1, day)
solve(part2, day)
#test(part2, lines=['eightf24oneone'])