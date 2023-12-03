from util import read_input, solve, test
import re

def part1(lines):
    total = 0
    for line in lines:
        digits = [int(c) for c in line if c.isdigit()]
        val = int(str(digits[0]) + str(digits[-1]))
        total += val
    return total

def part2(lines):
    iw_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    iw_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    total = 0
    for line in lines:
        digits = [(i, int(c)) for i, c in enumerate(line) if c.isdigit()]
        words = []
        for iw in iw_list:
            for match in re.finditer(iw, line):
                words.append((match.start(), iw_map[iw]))
        combined = digits + words
        val = int(str(min(combined, key=lambda x: x[0])[1]) + str(max(combined, key=lambda x: x[0])[1]))
        total += val
    return total

solve(part1, day=1)
solve(part2, day=1)
#test(part2, lines=['eightf24oneone'])