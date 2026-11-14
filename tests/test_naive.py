import pytest

from src.algorithms.naive_algorithm import naive_search


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
def test_basic_naive_search(text, pattern, expected):
    assert naive_search(pattern, text) == expected


@pytest.mark.parametrize(
    ("text", "pattern", "expected"),
    [
        # 1. Pusty wzorzec
        ("abcdef", "", [0, 1, 2, 3, 4, 5, 6]),

        # 2. Pusty tekst
        ("", "abc", []),

        # 3. Pusty tekst i pusty wzorzec
        ("", "", [0]),

        # 4. Wzorzec dłuższy od tekstu
        ("ab", "abcd", []),

        # 5. Wzorzec identyczny z tekstem
        ("abcdefgh", "abcdefgh", [0]),

        # 6. Wzorzec występuje wielokrotnie i nakłada się
        ("aaaa", "aaa", [0, 1]),

        # 7. Wiele nakładających się wystąpień
        ("aaaaaa", "aaa", [0, 1, 2, 3]),

        # 8. Wzorzec składający się z powtarzających znaków
        ("aaaaaaaa", "aaaa", [0, 1, 2, 3, 4]),

        # 9. Wzorzec występuje na początku i na końcu
        ("abcXYZabc", "abc", [0, 6]),

        # 10. Dopasowanie na końcu tekstu
        ("abcdefgh", "fgh", [5]),

        # 11. Brak dopasowania przy podobnych znakach
        ("aaaaaaaaab", "aaaac", []),

        # 12. Długie powtarzające się prefiksy
        ("aaaaaab", "aaab", [3]),

        # 13. Wielokrotne dopasowania wzorca okresowego
        ("ababababab", "abab", [0, 2, 4, 6]),

        # 14. Trudne dopasowanie wymagające cofania według LPS
        ("ababababaca", "ababaca", [4]),

        # 15. Klasyczny przykład działania KMP
        ("ABABDABACDABABCABAB", "ABABCABAB", [10]),

        # 16. Wzorzec jednoznakowy
        ("banana", "a", [1, 3, 5]),

        # 17. Wzorzec jednoznakowy bez wystąpienia
        ("banana", "z", []),

        # 18. Rozróżnianie wielkości liter
        ("AbAbAb", "ab", []),

        # 19. Znaki Unicode
        ("żółćżółć", "żółć", [0, 4]),

        # 20. Wiele dopasowań z powtarzającym się prefiksem
        ("abcabcabcabc", "abcabc", [0, 3, 6]),
    ],
)
def test_complex_naive_search(text, pattern, expected):
    assert naive_search(pattern, text) == expected
