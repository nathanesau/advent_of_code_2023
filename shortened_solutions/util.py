from typing import Callable, List

def read_input(day: int):
    """
    returns input as list of lines
    """
    with open(f"../inputs/day{day}.txt") as f:
        data = f.read()
    return data.splitlines()

def solve(fn: Callable, day: int):
    """
    executes fn against input

    reads provided day input as lines and passes to fn
    """
    lines = read_input(day)
    print(f"day {day} (fn: {fn.__name__}) result = {fn(lines)}")

def test(fn: Callable, lines: List[str]):
    """
    executes fn against testing input provided
    """
    print(f"test (fn: {fn.__name__}) result = {fn(lines)}")
