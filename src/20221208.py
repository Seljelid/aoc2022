import numpy as np


def treetop_tree_house():
    with open("data/08.txt") as f:
        lines = f.readlines()
    rows = [[int(c) for c in line.strip()] for line in lines]
    grid = np.array(rows)

    n_visible = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if (
                grid[i, j] > grid[i, j + 1 :].max(initial=0)  # To the right
                or grid[i, j] > grid[i, :j].max(initial=0)  # To the left
                or grid[i, j] > grid[i + 1 :, j].max(initial=0)  # Below
                or grid[i, j] > grid[:i, j].max(initial=0)  # Above
                or i in (0, grid.shape[0] - 1)
                or j in (0, grid.shape[1] - 1)
            ):
                n_visible += 1

    print(f"Star 1: {n_visible}")

    # Star 2
    scenic_scores = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            tree = grid[i, j]
            right = grid[i, j + 1 :]
            left = np.flip(grid[i, :j])
            below = grid[i + 1 :, j]
            above = np.flip(grid[:i, j])
            if not right.size:
                right_score = 0
            elif tree in right or any(right >= tree):
                right_score = np.argmax(right >= tree) + 1
            else:
                right_score = len(right)
            if not left.size:
                left_score = 0
            elif tree in left or any(left >= tree):
                left_score = np.argmax(left >= tree) + 1
            else:
                left_score = len(left)
            if not below.size:
                below_score = 0
            elif tree in below or any(below >= tree):
                below_score = np.argmax(below >= tree) + 1
            else:
                below_score = len(below)
            if not above.size:
                above_score = 0
            elif tree in above or any(above >= tree):
                above_score = np.argmax(above >= tree) + 1
            else:
                above_score = len(above)
            scenic_score = right_score * left_score * below_score * above_score

            scenic_scores.append(scenic_score)

    print(f"Star 2: {max(scenic_scores)}")


if __name__ == "__main__":
    treetop_tree_house()
