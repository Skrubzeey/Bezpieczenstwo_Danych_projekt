import random

from algorithms.naive_algorithm import naive_search
from algorithms.kmp_algorithm import kmp_algorithm


def reference_search_all(text: str, pattern: str) -> list[int]:
    if pattern == "":
        return list(range(len(text) + 1))

    result = []
    start = 0

    while True:
        index = text.find(pattern, start)

        if index == -1:
            break

        result.append(index)

        # +1 pozwala znaleźć również nakładające się wystąpienia.
        start = index + 1

    return result


def test_random_cases():
    rng = random.Random(42)

    alphabets = [
        "AB",
        "ABCD",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "0123456789",
    ]

    for _ in range(10_000):
        alphabet = rng.choice(alphabets)

        text_length = rng.randint(0, 200)
        pattern_length = rng.randint(0, 30)

        text = "".join(
            rng.choices(alphabet, k=text_length)
        )

        pattern = "".join(
            rng.choices(alphabet, k=pattern_length)
        )

        expected = reference_search_all(text, pattern)

        kmp_result = kmp_algorithm(text=text, pattern=pattern)
        naive_result = naive_search(text=text, pattern=pattern)

        assert kmp_result == expected
        assert naive_result == expected
