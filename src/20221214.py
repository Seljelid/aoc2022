from ast import literal_eval as ev


def regolith_reservoir():
    with open("data/14.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    rock_formations = []
    for line in lines:
        rocks = set()
        coord = line.split(" -> ")
        for r1, r2 in zip(coord, coord[1:]):
            rocks.add(ev(r1))
            rocks.add(ev(r2))
            added_rocks = _inbetween_rocks(ev(r1), ev(r2))
            for rock in added_rocks:
                rocks.add(rock)
            rock_formations.append(rocks)

    y_max = max(c[1] for rocks in rock_formations for c in rocks)
    all_rocks = set([rock for rocks in rock_formations for rock in rocks])
    sand_start = 500, 0
    i = 0
    while True:
        sand_pos = sand_start
        while sand_pos[1] < y_max:
            try:
                sand_pos = next(c for c in _sand_flow(*sand_pos) if c not in all_rocks)
            except:
                i += 1
                break
        else:
            print(f"Star 1: {i}")
            break

        all_rocks.add(sand_pos)

    # Star 2
    all_rocks = set([rock for rocks in rock_formations for rock in rocks])
    i = 0
    while True:
        sand_pos = sand_start
        while True:
            try:
                sand_pos = next(
                    c
                    for c in _sand_flow(*sand_pos)
                    if c not in all_rocks and c[1] < y_max + 2
                )
            except:
                i += 1
                break

        if sand_pos == sand_start:
            print(f"Star 2: {i}")
            break

        all_rocks.add(sand_pos)


def _inbetween_rocks(r1, r2):
    added_rocks = []
    if r1[0] != r2[0]:  # Vertical line
        for x in range(min(r1[0], r2[0]), max(r1[0], r2[0])):
            added_rocks.append((x, r1[1]))
    elif r1[1] != r2[1]:  # Horizontal line
        for y in range(min(r1[1], r2[1]), max(r1[1], r2[1])):
            added_rocks.append((r1[0], y))
    return added_rocks


def _sand_flow(x, y):
    return (x, y + 1), (x - 1, y + 1), (x + 1, y + 1)


if __name__ == "__main__":
    regolith_reservoir()
