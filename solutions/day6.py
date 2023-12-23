from util import read_input, solve, test
import re

def compute_dist(time, held_time):
    speed = held_time
    return (time - held_time) * held_time

def part1(lines):
    time = [int(e) for e in re.findall(r'\d+', lines[0])]
    distance = [int(e) for e in re.findall(r'\d+', lines[1])]
    num_races = len(time) # same as len(distance)
    prod = 1
    for race_num in range(num_races):
        available_time = time[race_num]
        record = distance[race_num]
        ways = 0
        for held_time in range(1, available_time):
            d = compute_dist(available_time, held_time)
            if d > record:
                ways += 1
        prod *= ways
    return prod

def part2(lines): # kind of slow. binary search would be faster.
    time = int(''.join(re.findall(r'\d+', lines[0])))
    distance = int(''.join(re.findall(r'\d+', lines[1])))
    available_time = time
    record = distance
    start, end = None, None
    for held_time in range(1, available_time):
        if (available_time - held_time) * held_time > record:
            start = held_time
            break
    for held_time in range(available_time, 1, -1):
        if (available_time - held_time) * held_time > record:
            end = held_time
            break
    return end - start + 1

day = __file__.split('day')[-1].split('.py')[0]
solve(part1, day)
solve(part2, day)
# test(part2, lines=[
#    "Time:      7  15   30",
#    "Distance:  9  40  200"])