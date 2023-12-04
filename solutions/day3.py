from util import read_input, solve, test
from collections import defaultdict
import re

def gv(grid, r, c):
    if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]):
        return grid[r][c]
    return None

def part1(lines):
    symbols = ['*', '#', '+', '$', '@', '&', '%', '=', '-', '/']
    grid = [list(line) for line in lines]
    total = 0
    for row, line in enumerate(lines):
        for match in re.finditer(r'\d+', line):
            num_range = (match.start(), match.end())
            adj_symbol = False
            for col in range(num_range[0]-1, num_range[1]+1):
                adj_symbol = gv(grid, row-1, col) in symbols or \
                    gv(grid, row, col) in symbols or \
                    gv(grid, row+1, col) in symbols
                if adj_symbol:
                    break
            if adj_symbol:
                total += int(line[match.start():match.end()])
    return total

def part2(lines):
    symbols = ['*']
    grid = [list(line) for line in lines]
    adj_map = defaultdict(list)
    for row, line in enumerate(lines):
        for match in re.finditer(r'\d+', line):
            num_range = (match.start(), match.end())
            for col in range(num_range[0]-1, num_range[1]+1):
                if gv(grid, row-1, col) in symbols:
                    adj_map[(row-1, col)].append(int(line[match.start():match.end()]))
                if gv(grid, row, col) in symbols:
                    adj_map[(row, col)].append(int(line[match.start():match.end()]))
                if gv(grid, row+1, col) in symbols:
                    adj_map[(row+1, col)].append(int(line[match.start():match.end()]))
    total = 0
    for k, v in adj_map.items():
        if len(v) == 2:
            total += (v[0] * v[1])
    return total

day = __file__.split('day')[-1].split('.py')[0]
solve(part1, day)
solve(part2, day)
# test(part2, lines=[
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598.."]
# )