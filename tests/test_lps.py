import pytest

from algorithms.kmp_algorithm import compute_lps


@pytest.mark.parametrize(
    ("pattern", "expected"),
    [
        ("", []),
        ("A", [0]),
        ("ABCD", [0, 0, 0, 0]),
        ("AAAA", [0, 1, 2, 3]),
        ("ABAB", [0, 0, 1, 2]),
        ("ABCABC", [0, 0, 0, 1, 2, 3]),
        ("AABAACAABAA", [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]),
        ("ABACABAB", [0, 0, 1, 0, 1, 2, 3, 2]),
    ],
)
def test_compute_lps(pattern, expected):
    assert compute_lps(pattern) == expected