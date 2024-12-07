from advent_of_code.utils.input_handling import read_input, parse_args

import math
import re


class Race:
    def __init__(self, time, distance_to_beat):
        self.time = int(time)
        self.distance_to_beat = int(distance_to_beat)
        self._compute_ways_to_win()

    def __str__(self):
        return f"time: {self.time} | " f"distance_to_beat: {self.distance_to_beat} | "

    def _compute_ways_to_win(self):
        possible_speeds = range(self.time + 1)
        self.ways_to_win = 0
        for possible_speed in possible_speeds:
            time_remaining = self.time - possible_speed
            distance_travelled = possible_speed * time_remaining
            if distance_travelled > self.distance_to_beat:
                self.ways_to_win += 1


class Races:
    def __init__(self, *races):
        self.races = list(races)

    def __str__(self):
        return "".join([str(race) for race in self.races])

    def n_races(self):
        return len(self.races)

    def add_race(self, race):
        self.races.append(race)

    def solve(self):
        return math.prod([race.ways_to_win for race in self.races])


def create_races(input, part=1):
    races = Races()

    times = re.findall(r"(\d+)", input[0])
    distances = re.findall(r"(\d+)", input[1])

    if part == 2:
        times = ["".join(times)]
        distances = ["".join(distances)]

    for time, distance in zip(times, distances):
        race = Race(time=time, distance_to_beat=distance)
        races.add_race(race)

    return races


def solve_day_6(input):
    races_part_1 = create_races(input, part=1)
    races_part_2 = create_races(input, part=2)
    return (races_part_1.solve(), races_part_2.solve())


def main():
    args = parse_args()
    input = read_input(args.input_file)
    result_part_1, result_part_2 = solve_day_6(input)
    print(
        f"Day 6: "
        f" Result for part 1 is {result_part_1}. "
        f" Result for part 2 is {result_part_2}. "
    )


if __name__ == "__main__":
    main()
