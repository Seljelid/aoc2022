import pandas as pd
import numpy as np


def cathode_ray_tube():
    with open("data/10.txt") as f:
        lines = f.readlines()
    instructions = [line.strip() for line in lines]
    program = pd.DataFrame(
        [inst.split() for inst in instructions], columns=["op", "value"]
    )
    program = program.fillna(0)
    program["value"] = program["value"].astype("int")
    program["time_needed"] = program.apply(lambda x: 2 if x.op == "addx" else 1, axis=1)
    program["cycle"] = program["time_needed"].cumsum()
    program = program.set_index("cycle")
    program["x"] = 1 + program["value"].cumsum()
    program["x"] = program["x"].shift()
    program = program.reindex(range(1, 241))
    program["x"] = program["x"].fillna(method="bfill")
    signal_strength = (
        program.loc[20].x * 20
        + program.loc[60].x * 60
        + program.loc[100].x * 100
        + program.loc[140].x * 140
        + program.loc[180].x * 180
        + program.loc[220].x * 220
    )
    print(f"Star 1: {int(signal_strength)}")

    # Star 2
    crt = []
    program["covers"] = program.apply(
        lambda x: [x["x"] - 1, x["x"], x["x"] + 1], axis=1
    )
    for cycle, row in program.iterrows():
        crt_pos = cycle - 1
        if crt_pos % 40 in row["covers"]:
            crt.append("#")
        else:
            crt.append(".")
    crt = np.array(crt)
    crt = np.reshape(crt, (6, 40))
    print("Star 2:")
    for row in crt:
        print(" ".join(row))


if __name__ == "__main__":
    cathode_ray_tube()
