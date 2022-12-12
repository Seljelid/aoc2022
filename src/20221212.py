import string
import numpy as np
from collections import deque


def hill_climbing_algorithm():
    with open("data/12.txt") as f:
        lines = f.readlines()
        input = [[c for c in line.strip()] for line in lines]

    alphabet = string.ascii_lowercase
    elevation_grid = {}
    for i, row in enumerate(input):
        for j, elem in enumerate(row):
            if elem == "S":
                start_pos = (i, j)
                elevation_grid[(i, j)] = alphabet.index("a")
            elif elem == "E":
                goal = (i, j)
                elevation_grid[(i, j)] = alphabet.index("z")
            else:
                elevation_grid[(i, j)] = alphabet.index(elem)

    min_distance = _bfs({start_pos}, goal, elevation_grid)
    print(f"Star 1: {min_distance}")

    # Star 2
    starting_points = {
        pos for pos, elevation in elevation_grid.items() if elevation == 0
    }
    min_distance = _bfs(starting_points, goal, elevation_grid)
    print(f"Star 2: {min_distance}")


def _bfs(starting_points, goal, elevation_grid):
    neighbors = lambda i, j: [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    visited = {}
    queue = deque([(start_pos, 0) for start_pos in starting_points])
    while len(queue) > 0:
        pos, distance = queue.popleft()
        if pos in visited:
            continue
        visited[pos] = distance

        for neighbor in neighbors(pos[0], pos[1]):
            if elevation_grid.get(neighbor, np.inf) - elevation_grid[pos] > 1:
                continue
            queue.append((neighbor, distance + 1))
    return visited[goal]


if __name__ == "__main__":
    hill_climbing_algorithm()
