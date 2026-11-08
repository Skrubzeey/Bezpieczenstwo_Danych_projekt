# implementacja funkcji lps
def compute_lps(pattern: str) -> list[int]:

    m = len(pattern)
    lps = [0] * m
    i = 1

    # długość bieżącego prefikso-sufiksu
    length = 0

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps
