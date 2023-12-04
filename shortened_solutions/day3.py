from util import read_input, solve, test
from collections import defaultdict
import re

def gv(grid, r, c):
    return grid[r][c] if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) else None

def part1(lines):
    sb = ['*', '#', '+', '$', '@', '&', '%', '=', '-', '/']
    grid = [list(line) for line in lines]
    def grid_fn(row, col):
        return gv(grid, row-1, col) in sb or gv(grid, row, col) in sb or gv(grid, row+1, col) in sb
    def match_fn(m, line, row):
        return int(line[m.start():m.end()]) if any([grid_fn(row, col) for col in range(m.start()-1, m.end()+1)]) else 0
    def fn(line, row):
        return sum([match_fn(m, line, row) for m in re.finditer(r'\d+', line)])
    return sum([fn(line, row) for row, line in enumerate(lines)])

def part2(lines):
    grid = [list(line) for line in lines]
    adj_map = defaultdict(list)
    def grid_fn(m, line, r, c):
        [adj_map[(p[0], p[1])].append(int(line[m.start():m.end()])) if gv(grid, p[0], p[1]) == '*' else '' for p in [(r-1, c), (r, c), (r+1, c)]]
    def match_fn(m, line, row):
        [grid_fn(m, line, row, col) for col in range(m.start()-1, m.end()+1)]
    def fn(line, row):
        [match_fn(m, line, row) for m in re.finditer(r'\d+', line)]
    [fn(line, row) for row, line in enumerate(lines)]
    return sum([(v[0] * v[1]) if len(v) == 2 else 0 for k, v in adj_map.items()])

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