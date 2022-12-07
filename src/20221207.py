from collections import defaultdict, deque


def no_space_left_on_device():
    with open("data/07.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    dirs = defaultdict(int)
    dir_stack = deque()
    for line in lines:
        match line.split():
            case ["$", "cd", "/"]:
                dir_stack = deque()
                dir_stack.append("home")
            case ["$", "cd", ".."]:
                dir_stack.pop()
            case ["$", "cd", new_dir] if new_dir != "/":
                dir_stack.append(new_dir)
            case [size, _] if size.isdigit():
                size = int(size)
                cwd = deque()
                cwd.extend(dir_stack)
                while cwd:
                    dir = "/".join(cwd)
                    dirs[dir] += size
                    cwd.pop()

    total_size = sum(size for size in dirs.values() if size <= 100000)
    print(f"Star 1: {total_size}")

    # Star 2
    removed_size = min(
        size for size in dirs.values() if dirs["home"] - size <= 40000000
    )
    print(f"Star 2: {removed_size}")


if __name__ == "__main__":
    no_space_left_on_device()
