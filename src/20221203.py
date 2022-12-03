import string


def rucksack_reorganization():
    with open("data/03.txt") as f:
        lines = f.readlines()
    rucksacks = []
    alphabet = string.ascii_letters
    priorities_sum = 0
    for line in lines:
        line = line.strip()
        rucksacks.append(line)
        common_item = list(set(line[: len(line) // 2]) & set(line[len(line) // 2 :]))[0]
        priorities_sum += alphabet.index(common_item) + 1

    print(f"Star 1: {priorities_sum}")

    # Star 2
    priorities_sum = 0
    for group in _get_groups(rucksacks):
        common_item = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
        priorities_sum += alphabet.index(common_item) + 1

    print(f"Star 2: {priorities_sum}")


def _get_groups(rucksacks, size=3):
    return (rucksacks[pos : pos + size] for pos in range(0, len(rucksacks), size))


if __name__ == "__main__":
    rucksack_reorganization()
