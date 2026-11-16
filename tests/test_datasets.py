import random

import pytest
from algorithms.kmp_algorithm import kmp_algorithm
from utils import kmp_comparisons, naive_comparisons

from experiments.datasets import (
    ALPHABET_SIZES,
    ALPHABETS,
    all_matches_case,
    kmp_worst_case,
    natural_case,
    naive_worst_case,
    uniform_case,
)

# ---------------------------------------------------------------------------
# Zbiór 1
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("sigma", ALPHABET_SIZES)
def test_uniform_lengths_and_alphabet(sigma):
    text, pattern = uniform_case(5000, 16, sigma, random.Random(1))

    assert len(text) == 5000
    assert len(pattern) == 16

    if sigma == 256:
        assert isinstance(text, bytes)
    else:
        assert set(text) <= set(ALPHABETS[sigma])


@pytest.mark.parametrize("sigma", ALPHABET_SIZES)
def test_uniform_pattern_from_text_occurs(sigma):
    text, pattern = uniform_case(5000, 16, sigma, random.Random(2))

    assert kmp_algorithm(text=text, pattern=pattern)


def test_uniform_same_seed_same_data():
    a = uniform_case(1000, 8, 4, random.Random(42), from_text=False)
    b = uniform_case(1000, 8, 4, random.Random(42), from_text=False)

    assert a == b


def test_uniform_distribution_is_roughly_flat():
    text, _ = uniform_case(100_000, 4, 4, random.Random(3))

    # każda z 4 liter powinna stanowić ~25% tekstu
    for letter in "ACGT":
        assert abs(text.count(letter) / len(text) - 0.25) < 0.01


# ---------------------------------------------------------------------------
# Zbiór 2
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("lang", ["pl", "en"])
def test_natural_pattern_from_text_occurs(lang):
    text, pattern = natural_case(10_000, 32, lang, random.Random(4))

    assert len(text) == 10_000
    assert len(pattern) == 32
    assert kmp_algorithm(text=text, pattern=pattern)


def test_natural_text_longer_than_corpus():
    text, _ = natural_case(1_000_000, 8, "en", random.Random(5))

    assert len(text) == 1_000_000


def test_natural_polish_keeps_diacritics():
    text, _ = natural_case(10_000, 8, "pl", random.Random(6))

    assert set("ąęółżś") & set(text)
    assert "\n" not in text


def test_natural_pattern_from_other_language_is_absent():
    text, pattern = natural_case(10_000, 32, "pl", random.Random(7), from_text=False)

    assert kmp_algorithm(text=text, pattern=pattern) == []


# ---------------------------------------------------------------------------
# Zbiór 4
# ---------------------------------------------------------------------------

N = 2000


@pytest.mark.parametrize("m", [2, 10, 100])
def test_naive_worst_case_exact_count(m):
    text, pattern = naive_worst_case(N, m)

    assert naive_comparisons(text, pattern) == (N - m + 1) * m
    assert kmp_comparisons(text, pattern) <= 2 * N


@pytest.mark.parametrize("m", [2, 10, 100])
def test_all_matches_case(m):
    text, pattern = all_matches_case(N, m)

    assert kmp_algorithm(text=text, pattern=pattern) == list(range(N - m + 1))
    assert naive_comparisons(text, pattern) == (N - m + 1) * m
    assert kmp_comparisons(text, pattern) == N


@pytest.mark.parametrize("m", [10, 100])
def test_kmp_worst_case_close_to_2n(m):
    text, pattern = kmp_worst_case(N, m)

    assert len(text) == N
    # KMP nigdy nie przekracza 2n, a tu zbliża się do tej granicy
    assert 1.8 * N <= kmp_comparisons(text, pattern) <= 2 * N
