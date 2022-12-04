def camp_cleanup():
    with open("data/04.txt") as f:
        lines = f.readlines()
    section_list = []
    for line in lines:
        bounds = line.strip().replace("-", ",").split(",")
        bounds = [int(bound) for bound in bounds]
        sections = [
            set(range(bounds[0], bounds[1] + 1)),
            set(range(bounds[2], bounds[3] + 1)),
        ]
        section_list.append(sections)

    c = 0
    for pair in section_list:
        if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
            c += 1
    print(f"Star 1: {c}")

    # Star 2
    c = 0
    for pair in section_list:
        if not len(pair[0].intersection(pair[1])) == 0:
            c += 1
    print(f"Star 2: {c}")


if __name__ == "__main__":
    camp_cleanup()
