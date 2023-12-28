import pytest
import math
from advent_of_code.year_2023.solvers.day_6_solvers import (
    Race,
    Races,
    create_races,
    solve_day_6,
)


@pytest.fixture
def day_6_test_input():
    return [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]


@pytest.fixture
def sample_race():
    return Race(time=7, distance_to_beat=9)


@pytest.fixture
def sample_race_part_2():
    return Race(time=71530, distance_to_beat=940200)


@pytest.fixture
def sample_races():
    return Races(
        Race(time=7, distance_to_beat=9),
        Race(time=15, distance_to_beat=40),
        Race(time=30, distance_to_beat=200),
    )


def test_race_initialization(sample_race):
    assert sample_race.time == 7
    assert sample_race.distance_to_beat == 9
    assert sample_race.ways_to_win == 4


def test_race_compute_ways_to_win(sample_race):
    sample_race._compute_ways_to_win()
    assert sample_race.ways_to_win == 4


def test_races_initialisation():
    races = Races()
    for race in races.races:
        print(race)
    assert races.races == []


def test_races_add_race(sample_race):
    races = Races()
    races.add_race(sample_race)
    assert races.races == [sample_race]


def test_races_solve(sample_races):
    assert sample_races.solve() == math.prod([4, 8, 9])


def test_create_races_part_1(day_6_test_input, sample_races):
    test_races = create_races(day_6_test_input, part=1)
    assert test_races.n_races() == 3
    for race, expected_race in zip(test_races.races, sample_races.races):
        assert race.time == expected_race.time
        assert race.distance_to_beat == expected_race.distance_to_beat
        assert race.ways_to_win == expected_race.ways_to_win


def test_create_races_part_2(day_6_test_input, sample_race_part_2):
    test_races = create_races(day_6_test_input, part=2)
    assert test_races.n_races() == 1
    test_race = test_races.races[0]
    assert test_race.time == sample_race_part_2.time
    assert test_race.distance_to_beat == sample_race_part_2.distance_to_beat
    assert test_race.ways_to_win == sample_race_part_2.ways_to_win


def test_solve_day_6(day_6_test_input):
    assert solve_day_6(day_6_test_input) == (288, 71503)
