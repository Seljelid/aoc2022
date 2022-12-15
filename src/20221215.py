import re


def beacon_exclusion_zone():
    with open("data/15.txt") as f:
        lines = [re.findall(r"-?\d+", line) for line in f.readlines()]

    sensors = []
    for line in lines:
        sensor = Sensor(line[0], line[1], line[2], line[3])
        sensors.append(sensor)

    beacons = set([sensor.closest_beacon for sensor in sensors])
    left_sensor = sorted(sensors, key=lambda s: s.pos[0])[0]
    right_sensor = sorted(sensors, key=lambda s: s.pos[0])[-1]
    min_mh = [sensor.min_manhattan_distance() for sensor in sensors]
    x_min = left_sensor.pos[0] - max(min_mh)
    x_max = right_sensor.pos[0] + max(min_mh)

    row = 2000000
    count = 0
    for x in range(x_min, x_max):
        pos = x, row
        mh = [sensor.manhattan_distance(pos) for sensor in sensors]
        covered = any(x <= y for x, y in zip(mh, min_mh))
        if covered and pos not in beacons:
            count += 1

    print(f"Star 1: {count}")

    # Star 2
    max_range = 4000000
    for sensor in sensors:
        possible = sensor.missed_by_one()
        for pos in possible:
            if _check_pos(pos, sensors, beacons, max_range):
                print(f"Star 2: {pos[0] * 4000000 + pos[1]}")
                return


def _check_pos(pos, sensors, beacons, max_range):
    if pos[0] < 0 or pos[1] < 0 or pos[0] > max_range or pos[1] > max_range:
        return False
    for s in sensors:
        d = s.manhattan_distance(pos)
        if d <= s.d_min or pos in beacons:
            return False
    return True


class Sensor:
    def __init__(self, x, y, i, j):
        self.x = int(x)
        self.y = int(y)
        self.pos = self.x, self.y
        self.closest_beacon = int(i), int(j)
        self.d_min = self.min_manhattan_distance()

    def manhattan_distance(self, point):
        return abs(self.x - point[0]) + abs(self.y - point[1])

    def min_manhattan_distance(self):
        return abs(self.x - self.closest_beacon[0]) + abs(
            self.y - self.closest_beacon[1]
        )

    def missed_by_one(self):
        points = set()
        d = self.d_min + 1
        for i in range(d):
            points.add((self.x + i, self.y - d + i))
            points.add((self.x + d - i, self.y + i))
            points.add((self.x - i, self.y + d - i))
            points.add((self.x - d + i, self.y - i))
        return points


if __name__ == "__main__":
    beacon_exclusion_zone()
