import pytest
from src.algorithms.kmp_algorithm import kmp_algorithm


@pytest.mark.parametrize(
    ("text", "pattern", "expected"),
    [
        ("abbbcdabbefab", "abb", [0, 6]),
        ("abcdef", "cd", [2]),
        ("abababab", "ab", [0, 2, 4, 6]),
        ("abcdefgabc", "xy", []),
        ("abc", "abc", [0]),
        ("abc", "c", [2]),
        ("aaaaa", "aaa", [0, 1, 2]),
        ("ABABAB", "ABAB", [0, 2]),
        ("mississippi", "issi", [1, 4]),
        ("This is a test message for you", "s", [3, 6, 12, 17, 18])
    ],

)
def test_basic_kmp_cases(text, pattern, expected):
    assert kmp_algorithm(text, pattern) == expected
