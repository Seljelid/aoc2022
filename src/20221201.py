def calories():
    with open("data/01.txt") as f:
        lines = f.readlines()
    cals = []
    cal_count = 0
    for line in lines:
        if not line.isspace():
            cal_count += int(line)
        else:
            cals.append(cal_count)
            cal_count = 0

    sorted_cals = sorted(cals)
    print(f"Star 1: {sorted_cals[-1]}")
    print(f"Star 2: {sum(sorted_cals[-3:])}")


if __name__ == "__main__":
    calories()
