import numpy as np


def rope_bridge():
    with open("data/09.txt") as f:
        lines = f.readlines()
    instructions = [line.strip() for line in lines]

    rope = LongRope(2)
    for instruction in instructions:
        direction, steps = instruction.split()
        for _ in range(int(steps)):
            rope.move(direction=direction)
    print(f"Star 1: {len(rope.tail_positions)}")

    # Star 2
    rope = LongRope(10)
    for instruction in instructions:
        direction, steps = instruction.split()
        for _ in range(int(steps)):
            rope.move(direction=direction)

    print(f"Star 2: {len(rope.tail_positions)}")


class LongRope:
    def __init__(self, size):
        self.knots = [np.array([0, 0]) for _ in range(size)]
        self.tail_positions = {(0, 0)}

    def move(self, direction):
        match direction:
            case "R":
                self.knots[0][0] += 1
            case "L":
                self.knots[0][0] -= 1
            case "U":
                self.knots[0][1] += 1
            case "D":
                self.knots[0][1] -= 1

        for i, knot in enumerate(self.knots[1:]):
            head = self.knots[i]
            distance = head - knot
            if any(abs(distance) > 1):
                knot[0] += np.sign(distance[0])
                knot[1] += np.sign(distance[1])
        self.tail_positions.add((self.knots[-1][0], self.knots[-1][1]))


if __name__ == "__main__":
    rope_bridge()
