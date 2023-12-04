from util import read_input, solve, test
from collections import defaultdict
import re

def part1(lines):
    total = 0
    for line in lines:
        card_id = int(line.split(": ")[0].split("Card ")[1].strip())
        card_input = line.split(": ")[1]
        winning_cards = [e.strip() if e else 'WCN' for e in card_input.split(" | ")[0].split(' ')]
        player_cards = [e.strip() if e else 'PCN' for e in card_input.split(" | ")[1].split(' ')]
        score = 0
        for card in player_cards:
            if card in winning_cards:
                score = 1 if score == 0 else score * 2
        total += score
    return total

def part2(lines):
    total = 0
    winning_cards = defaultdict(list)
    player_cards = defaultdict(list)
    pcmap = defaultdict(lambda: defaultdict(list))
    for i, line in enumerate(lines):
        card_id = int(line.split(": ")[0].split("Card ")[1].strip())
        card_input = line.split(": ")[1]
        winning_cards[i] = [e.strip() if e else 'WCN' for e in card_input.split(" | ")[0].split(' ')]
        player_cards[i] = [e.strip() if e else 'PCN' for e in card_input.split(" | ")[1].split(' ')]
    for k, v in player_cards.items():
        for k2, v2 in winning_cards.items():
            for card in v2:
                if card in v:
                    pcmap[k][k2].append(card)
    sc = defaultdict(int)
    for i, _ in enumerate(lines):
        row_entries = []
        for (k, v) in sc.items():
            if k != i:
                continue
            for j in range(len(pcmap[k][i])):
                row_entries.append((i+j+1, v))
        for j in range(len(pcmap[i][i])):
            row_entries.append(((i+j+1), 1))
        for e in row_entries:
            sc[e[0]] += e[1]
    total = 0
    for (k, v) in sc.items():
        total += v
    return total + len(lines)

day = __file__.split('day')[-1].split('.py')[0]
solve(part1, day)
solve(part2, day)
# test(part2, lines=[
#     "Card 0: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#     "Card 1: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#     "Card 2:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#     "Card 3: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#     "Card 4: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#     "Card 5: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
# ])