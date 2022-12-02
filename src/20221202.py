import pandas as pd


def rock_paper_scissors():
    df = pd.read_csv("data/02.txt", sep=" ", names=["opponent", "me"])
    df = df.replace(
        {
            "A": "rock",
            "B": "paper",
            "C": "scissors",
            "X": "rock",
            "Y": "paper",
            "Z": "scissors",
        }
    )
    df["points"] = df.apply(lambda x: _get_round_points(x.opponent, x.me), axis=1)
    print(f"Star 1: {df['points'].sum()}")

    # Star 2
    df["me"] = df["me"].replace({"rock": "lose", "paper": "draw", "scissors": "win"})
    df = df.rename(columns={"me": "outcome"})
    df["points"] = df.apply(
        lambda x: _get_round_points_2(x.opponent, x.outcome), axis=1
    )
    print(f"Star 2: {df['points'].sum()}")


def _get_round_points_2(opponent, outcome):
    shape_points = {"rock": 1, "paper": 2, "scissors": 3}
    opponent_shape_points = shape_points[opponent]
    match outcome:
        case "lose":
            return (opponent_shape_points - 2) % 3 + 1
        case "draw":
            return opponent_shape_points + 3
        case "win":
            return opponent_shape_points % 3 + 1 + 6


def _get_round_points(opponent, me):
    shape_points = {"rock": 1, "paper": 2, "scissors": 3}
    diff = shape_points[me] - shape_points[opponent]
    if diff == 0:
        round_points = 3 + shape_points[me]
    elif diff in [1, -2]:
        round_points = 6 + shape_points[me]
    elif diff in [-1, 2]:
        round_points = shape_points[me]
    return round_points


if __name__ == "__main__":
    rock_paper_scissors()
