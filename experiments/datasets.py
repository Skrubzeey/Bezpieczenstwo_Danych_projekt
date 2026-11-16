"""Generatory zbiorów testowych 1, 2 i 4.

Każda funkcja zwraca parę (tekst, wzorzec) i niczego nie mierzy.
Siatkę parametrów (n, m), ziarno oraz pomiary ustala skrypt benchmarku,
który tylko wywołuje te funkcje. Generatory losowe przyjmują obiekt
random.Random, więc to samo ziarno daje zawsze te same dane.
"""

import random
from functools import cache
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

# ---------------------------------------------------------------------------
# Zbiór 1: losowy tekst o rozkładzie jednostajnym
# ---------------------------------------------------------------------------

# Alfabety o rozmiarach 2, 4 (DNA) i 26. Alfabet 256 to bajty (typ bytes).
ALPHABETS = {
    2: "AB",
    4: "ACGT",
    26: "abcdefghijklmnopqrstuvwxyz",
}
ALPHABET_SIZES = (2, 4, 26, 256)


def random_text(n: int, sigma: int, rng: random.Random) -> str | bytes:
    """Losowy ciąg długości n, każdy symbol alfabetu z równym prawdopodobieństwem."""
    if sigma == 256:
        # prawdziwe dane binarne; KMP i algorytm naiwny działają na bytes bez zmian
        return rng.randbytes(n)
    return "".join(rng.choices(ALPHABETS[sigma], k=n))


def uniform_case(
    n: int, m: int, sigma: int, rng: random.Random, from_text: bool = True
) -> tuple[str | bytes, str | bytes]:
    """Zbiór 1.

    from_text=True  -> wzorzec wycięty z tekstu (na pewno występuje),
    from_text=False -> wzorzec losowy z tego samego alfabetu (zwykle nie występuje).
    """
    text = random_text(n, sigma, rng)
    if from_text:
        start = rng.randrange(n - m + 1)
        return text, text[start : start + m]
    return text, random_text(m, sigma, rng)


# ---------------------------------------------------------------------------
# Zbiór 2: tekst naturalny (nierównomierny rozkład znaków)
# ---------------------------------------------------------------------------

CORPORA = {
    "pl": "pan_tadeusz.txt",
    "en": "alice.txt",
}


@cache
def load_corpus(lang: str) -> str:
    """Wczytuje korpus i zamienia każdy ciąg białych znaków na jedną spację.

    Dzięki temu wcięcia i puste linie nie zaburzają rozkładu znaków.
    Wielkość liter i polskie znaki zostają bez zmian.
    """
    raw = (DATA_DIR / CORPORA[lang]).read_text(encoding="utf-8")
    return " ".join(raw.split())


def natural_text(n: int, lang: str) -> str:
    """Pierwsze n znaków korpusu.

    shortcut: korpus (~0,4 mln znaków) jest powtarzany, gdy n jest większe,
    co dla wzorców m <= 1024 nie zmienia rozkładu; większy korpus, jeśli
    potrzebny będzie tekst bez powtórzeń.
    """
    corpus = load_corpus(lang)
    return (corpus * (n // len(corpus) + 1))[:n]


def natural_case(
    n: int, m: int, lang: str, rng: random.Random, from_text: bool = True
) -> tuple[str, str]:
    """Zbiór 2.

    from_text=True  -> wzorzec to fragment tego samego tekstu (występuje),
    from_text=False -> wzorzec to fragment korpusu w drugim języku
                       (też tekst naturalny, ale zwykle nie występuje).
    """
    text = natural_text(n, lang)
    if from_text:
        source = text
    else:
        source = load_corpus("en" if lang == "pl" else "pl")
    start = rng.randrange(len(source) - m + 1)
    return text, source[start : start + m]


# ---------------------------------------------------------------------------
# Zbiór 4: przypadki pesymistyczne
# ---------------------------------------------------------------------------


def naive_worst_case(n: int, m: int) -> tuple[str, str]:
    """T = a^n, P = a^(m-1) b.

    Algorytm naiwny na każdej z n-m+1 pozycji porównuje wszystkie m znaków
    i dopiero na ostatnim trafia na niezgodność: dokładnie (n-m+1)*m porównań.
    KMP: około 2n porównań.
    """
    return "a" * n, "a" * (m - 1) + "b"


def all_matches_case(n: int, m: int) -> tuple[str, str]:
    """T = a^n, P = a^m: wzorzec występuje na każdej możliwej pozycji.

    Naiwny: (n-m+1)*m porównań; KMP: dokładnie n porównań (lps = [0,1,...,m-1]).
    """
    return "a" * n, "a" * m


def kmp_worst_case(n: int, m: int) -> tuple[str, str]:
    """T = (a^(m-1) c) powtórzone, P = a^(m-1) b (wzorzec o najdłuższym LPS).

    Na każdym znaku 'c' KMP cofa j po całym łańcuchu LPS: m-1, m-2, ..., 0,
    czyli m porównań na jednym znaku tekstu. Łącznie około 2n porównań,
    co jest górną granicą KMP wyprowadzoną w dokumentacji.
    """
    block = "a" * (m - 1) + "c"
    return (block * (n // m + 1))[:n], "a" * (m - 1) + "b"


WORST_CASES = {
    "naive_worst": naive_worst_case,
    "all_matches": all_matches_case,
    "kmp_worst": kmp_worst_case,
}
