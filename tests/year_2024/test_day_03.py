import pytest
from advent_of_code.year_2024.day_03 import (
    instruction_compute,
)


@pytest.mark.parametrize(
    "input, use_do_dont_rule, expected",
    [
        [
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
            False,
            161,
        ],
        ["xmul(2,4)", False, 8],
        ["%&mul[3,7]!@^do_not_mul(5,5)", False, 25],
        ["mul(11,8)mul(8,5)", False, 128],
        [
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
            True,
            48,
        ],
    ],
)
def test_instruction_compute(input, use_do_dont_rule, expected):
    result = instruction_compute(input, use_do_dont_rule=use_do_dont_rule)
    print(result)
    assert result == expected
