# zdefiniowanie naiwnego algorytmu
def naive_search(pattern: str, text: str) -> list[int]:

    # pobranie długości patternu
    pattern_len = len(pattern)

    # pobranie długości tekstu
    text_len = len(text)

    ans = []

    # przechodzimy po tekście przesuwając okno patternu o jeden
    for i in range(text_len - pattern_len + 1):

        # sprawdzenie czy mamy match na indeksie i
        j = 0
        while j < pattern_len:
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == pattern_len:
            ans.append(i)

    return ans

