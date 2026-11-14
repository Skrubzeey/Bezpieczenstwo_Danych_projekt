from algorithms.kmp_algorithm import compute_lps


def naive_comparisons(text: str, pattern: str) -> int:
    """Count character comparisons in the naive algorithm."""
    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return 0

    comparisons = 0

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

    return comparisons


def kmp_comparisons(text: str, pattern: str) -> int:
    """Count character comparisons in the KMP algorithm."""
    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return 0

    lps = compute_lps(pattern)

    comparisons = 0
    i = 0
    j = 0

    while i < n:
        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                j = lps[j - 1]

        elif j != 0:
            j = lps[j - 1]

        else:
            i += 1

    return comparisons