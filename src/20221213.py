from ast import literal_eval
from math import prod


def distress_signal():
    with open("data/13.txt") as f:
        packets = [
            literal_eval(line.strip()) for line in f.readlines() if not line.isspace()
        ]
    correct = []
    for i in range(0, len(packets), 2):
        p1 = packets[i]
        p2 = packets[i + 1]
        correct.append(_compare(p1, p2) > 0)

    s = sum(i + 1 for i, value in enumerate(correct) if value)
    print(f"Star 1: {s}")

    # Star 2
    divider_packets = [[[2]], [[6]]]
    packets = [*packets, *divider_packets]
    sorted_packets = sorted(packets, key=Sorter)
    distress_signal = prod(
        sorted_packets.index(divider) + 1 for divider in divider_packets
    )
    print(f"Star 2: {distress_signal}")


def _compare(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        return p2 - p1

    if isinstance(p1, list) and isinstance(p2, list):
        for e1, e2 in zip(p1, p2):
            if result := _compare(e1, e2):
                return result
        return len(p2) - len(p1)

    if isinstance(p1, list):
        return _compare(p1, [p2])

    if isinstance(p2, list):
        return _compare([p1], p2)


class Sorter:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return _compare(other.x, self.x) < 0

    def __eq__(self, other):
        return _compare(self.x, other.x) == 0


if __name__ == "__main__":
    distress_signal()
