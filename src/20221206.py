def tuning_trouble():
    with open("data/06.txt") as f:
        buffer = f.read().strip()
    for i, _ in enumerate(buffer):
        seq = buffer[i : i + 4]
        if len(set(seq)) == 4:
            print(f"Star 1: {i + 4}")
            break
    for i, _ in enumerate(buffer):
        seq = buffer[i : i + 14]
        if len(set(seq)) == 14:
            print(f"Star 2: {i + 14}")
            break


if __name__ == "__main__":
    tuning_trouble()
