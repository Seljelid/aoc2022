from collections import deque
import re


def supply_stacks():
    with open("data/05.txt") as f:
        lines = f.readlines()
    crates = []
    instructions = []
    blank_occured = False
    for line in lines:
        if line.isspace():
            blank_occured = True
            continue
        if not blank_occured:
            crates.append(line)
        else:
            instructions.append(line)

    stacks = [deque() for _ in range(1, int(max(crates[-1].strip().split())) + 1)]
    for crate in crates[:-1]:
        for i in range(1, int(max(crates[-1].strip().split())) + 1):
            idx = crates[-1].index(str(i))
            if crate[idx] != " ":
                stacks[i - 1].append(crate[idx])

    for instruction in instructions:
        n, fr, to = map(int, re.findall(r"\d+", instruction))
        fr, to = fr - 1, to - 1
        for i in range(n):
            stacks[to].appendleft(stacks[fr].popleft())

    print(f"Star 1: {''.join(stack[0] for stack in stacks)}")

    # Star 2
    stacks = [deque() for _ in range(1, int(max(crates[-1].strip().split())) + 1)]
    for crate in crates[:-1]:
        for i in range(1, int(max(crates[-1].strip().split())) + 1):
            idx = crates[-1].index(str(i))
            if crate[idx] != " ":
                stacks[i - 1].append(crate[idx])

    for instruction in instructions:
        n, fr, to = map(int, re.findall(r"\d+", instruction))
        fr, to = fr - 1, to - 1
        moved_crates = deque()
        for i in range(n):
            moved_crates.appendleft(stacks[fr].popleft())
        stacks[to].extendleft(moved_crates)

    print(f"Star 2: {''.join(stack[0] for stack in stacks)}")


if __name__ == "__main__":
    supply_stacks()
