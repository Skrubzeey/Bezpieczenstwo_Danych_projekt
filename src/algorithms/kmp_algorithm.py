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


def kmp_algorithm(text: str, pattern: str) -> list[int]:
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern=pattern)
    i = 0
    j = 0
    res = []

    while i < n:

        # jeżeli dwa znaki się równają przesuń wskaźnik dalej
        if text[i] == pattern[j]:
            i += 1
            j += 1

            # jeżeli pełen pattern się zgadza
            # wtedy dodaj indeks startowy do res
            if j == m:
                res.append(i - j)

                # wykorzystujemy poprzedni indeks lps
                # aby pominąć niepotrzebne porównania
                j = lps[j - 1]

        # jeżeli nie mamy równości
        else:

            # wykorzystujemy poprzedni lps index
            # aby unikać niepotrzebnych porównań
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return res
