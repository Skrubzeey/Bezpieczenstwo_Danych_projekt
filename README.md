# Badanie algorytmu Knutha-Morrisa-Pratta (KMP)

## 1. Informacje o projekcie

**Przedmiot:** Bezpieczeństwo Danych  
**Język programowania:** Python 3.x  
**Temat:** Eksperymentalna analiza algorytmu Knutha-Morrisa-Pratta (KMP) w kontekście wyszukiwania wzorców tekstowych.

## 2. Cel projektu

Celem projektu jest implementacja oraz przeprowadzenie eksperymentalnej analizy algorytmu Knutha-Morrisa-Pratta (KMP), służącego do wyszukiwania wystąpień określonego wzorca w tekście.

W ramach projektu zostanie zbadana efektywność algorytmu w zależności od długości tekstu, długości wzorca oraz charakterystyki analizowanych danych. Szczególna uwaga zostanie poświęcona wydajności czasowej, złożoności obliczeniowej oraz potencjalnym zastosowaniom algorytmu w obszarze bezpieczeństwa danych.

## 3. Opis teoretyczny

### 3.1. Algorytm Knutha-Morrisa-Pratta

Algorytm KMP jest algorytmem wyszukiwania wzorca w tekście, który wykorzystuje informacje o strukturze badanego wzorca, aby ograniczyć liczbę niepotrzebnych porównań znaków.

W przeciwieństwie do naiwnego algorytmu wyszukiwania KMP nie rozpoczyna porównywania wzorca od początku po każdym niedopasowaniu. Zamiast tego korzysta z tablicy LPS (*Longest Proper Prefix which is also Suffix*), która określa długość najdłuższego właściwego prefiksu będącego jednocześnie sufiksem danego fragmentu wzorca.

### 3.2. Złożoność obliczeniowa

Dla tekstu o długości \(n\) oraz wzorca o długości \(m\):

- **Czasowa:** \(O(n+m)\).
- **Pamięciowa:** \(O(m)\) dodatkowej pamięci na tablicę LPS, z pominięciem pamięci wejściowej i wynikowej.

### 3.3. Znaczenie w kontekście bezpieczeństwa danych

Wyszukiwanie wzorców może być wykorzystywane jako jeden z elementów analizy danych, między innymi do:

- wykrywania określonych ciągów znaków w logach systemowych;
- wyszukiwania znanych sygnatur w analizowanych plikach;
- identyfikowania wystąpień określonych fraz w zbiorach danych;
- analizy tekstowych danych wejściowych pod kątem zdefiniowanych wzorców.

Sam algorytm KMP nie zapewnia szyfrowania ani ochrony poufności danych. Może jednak stanowić element większego systemu analizy i monitorowania bezpieczeństwa.

## 4. Zakres projektu

Projekt obejmuje następujące zadania:

1. Zapoznanie się z zasadą działania algorytmu KMP.
2. Implementację algorytmu w języku Python.
3. Przygotowanie zestawów danych testowych o różnych rozmiarach.
4. Przeprowadzenie eksperymentów dla różnych długości tekstu i wzorca.
5. Pomiar czasu wykonania algorytmu.
6. Porównanie wyników z naiwnym algorytmem wyszukiwania wzorca.
7. Analizę otrzymanych wyników i sformułowanie wniosków.

## 5. Struktura projektu

```text
kmp-data-security/
├── src/
│   ├── kmp.py
│   └── naive_search.py
├── experiments/
│   ├── run_experiments.py
│   └── results/
│       └── results.csv
├── tests/
│   └── test_kmp.py
├── plots/
│   └── execution_time.png
├── requirements.txt
├── README.md
└── .gitignore
```

Opis katalogów i plików:

- `src/kmp.py` — implementacja algorytmu KMP.
- `src/naive_search.py` — implementacja naiwnego algorytmu wyszukiwania.
- `experiments/run_experiments.py` — skrypt przeprowadzający eksperymenty.
- `experiments/results/` — wyniki pomiarów.
- `tests/` — testy poprawności implementacji.
- `plots/` — wykresy przedstawiające wyniki eksperymentów.
- `requirements.txt` — lista dodatkowych zależności.

## 6. Wymagania i uruchomienie

### 6.1. Wymagania

- Python w wersji 3.x.
- Git (opcjonalnie).
- Biblioteki dodatkowe wymagane do generowania wykresów, np. `matplotlib` i `pandas`.

### 6.2. Pobranie projektu

```bash
git clone [URL_REPOZYTORIUM]
cd kmp-data-security
```

### 6.3. Utworzenie środowiska wirtualnego

```bash
python -m venv .venv
```

Aktywacja środowiska:

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 6.4. Instalacja zależności

```bash
pip install -r requirements.txt
```

### 6.5. Uruchomienie eksperymentów

```bash
python experiments/run_experiments.py
```

### 6.6. Uruchomienie testów

```bash
python -m unittest discover -s tests
```

Powyższe polecenia zakładają, że pliki i skrypty zostały zaimplementowane zgodnie z przedstawioną strukturą.

## 7. Metodyka eksperymentów

Eksperymenty mają na celu ocenę wydajności algorytmu KMP w różnych warunkach wejściowych.

### 7.1. Badane parametry

- **Długość tekstu:** liczba znaków analizowanego tekstu.
- **Długość wzorca:** liczba znaków poszukiwanego ciągu.
- **Rodzaj danych:** tekst losowy, tekst powtarzalny oraz tekst naturalny.
- **Liczba wystąpień wzorca:** brak wystąpień, pojedyncze wystąpienie lub wiele wystąpień.
- **Czas wykonania:** czas potrzebny na wyszukanie wzorca.

### 7.2. Scenariusze testowe

| Scenariusz | Charakterystyka | Cel |
|---|---|---|
| Test 1 | Krótki tekst i krótki wzorzec | Weryfikacja podstawowego działania |
| Test 2 | Długi tekst i krótki wzorzec | Ocena wpływu długości tekstu |
| Test 3 | Długi tekst i długi wzorzec | Ocena wpływu długości wzorca |
| Test 4 | Tekst zawierający powtarzające się znaki | Analiza zachowania przy powtarzalnych danych |
| Test 5 | Brak wzorca w tekście | Analiza wyszukiwania zakończonego niepowodzeniem |
| Test 6 | Wzorzec występujący wielokrotnie | Analiza liczby znalezionych wystąpień |

### 7.3. Sposób przeprowadzania pomiarów

Pomiary będą realizowane za pomocą modułu `time` lub `timeit`. Każdy eksperyment powinien zostać wykonany wielokrotnie, a wyniki należy podsumować za pomocą średniej lub mediany czasu wykonania.

W celu zapewnienia porównywalności wyników oba algorytmy powinny otrzymywać identyczne dane wejściowe i zwracać równoważne wyniki.

Należy również uwzględnić koszt przygotowania tablicy LPS w algorytmie KMP, szczególnie w przypadku krótkich tekstów i wzorców.

## 8. Wyniki eksperymentów

W tej sekcji należy umieścić wyniki uzyskane podczas rzeczywistego wykonania testów.

### 8.1. Tabela wyników

| Długość tekstu | Długość wzorca | KMP [ms] | Algorytm naiwny [ms] |
|---:|---:|---:|---:|
| [Wartość] | [Wartość] | [Wynik] | [Wynik] |
| [Wartość] | [Wartość] | [Wynik] | [Wynik] |
| [Wartość] | [Wartość] | [Wynik] | [Wynik] |

### 8.2. Wizualizacja wyników

Wyniki eksperymentów zostaną przedstawione na wykresach umożliwiających porównanie czasu wykonania obu algorytmów w zależności od rozmiaru danych wejściowych.

Przykładowe wykresy:

- czas wykonania w zależności od długości tekstu;
- czas wykonania w zależności od długości wzorca;
- porównanie algorytmów dla danych powtarzalnych;
- porównanie wyników dla różnych scenariuszy testowych.

Wykresy zostaną zapisane w katalogu `plots/`.

## 9. Analiza wyników

Na podstawie przeprowadzonych eksperymentów należy odpowiedzieć na następujące pytania:

1. Jak zmienia się czas wykonania KMP wraz ze wzrostem długości tekstu?
2. Jak długość i struktura wzorca wpływają na wydajność algorytmu?
3. W jakich warunkach KMP osiąga największą przewagę nad algorytmem naiwnym?
4. Czy dla bardzo krótkich tekstów różnice w czasie wykonania są istotne?
5. Czy wyniki pomiarów są zgodne z teoretyczną złożonością obliczeniową?
6. Jakie ograniczenia ma wykorzystanie KMP do analizy danych związanych z bezpieczeństwem?

Wnioski powinny wynikać z rzeczywistych pomiarów, a nie wyłącznie z przewidywań teoretycznych.

## 10. Testy poprawności

Implementacja powinna zostać przetestowana dla następujących przypadków:

- znalezienie wzorca występującego na początku tekstu;
- znalezienie wzorca występującego na końcu tekstu;
- znalezienie wielu wystąpień wzorca;
- brak wzorca w tekście;
- pusty tekst;
- wzorzec dłuższy od tekstu;
- wzorzec zawierający powtarzające się znaki;
- tekst i wzorzec składające się z pojedynczych znaków.

Dodatkowo należy sprawdzić, czy wyniki KMP są zgodne z wynikami algorytmu referencyjnego dla tych samych danych wejściowych.

## 11. Bezpieczeństwo i ograniczenia

Algorytm KMP odpowiada za wyszukiwanie ciągów znaków i sam w sobie nie jest mechanizmem kryptograficznym.

Podczas analizy zastosowań w bezpieczeństwie danych należy uwzględnić następujące kwestie:

- wyszukiwanie wzorców nie zastępuje szyfrowania ani kontroli dostępu;
- skuteczność wykrywania zależy od poprawnego zdefiniowania poszukiwanych wzorców;
- dane testowe powinny być syntetyczne lub odpowiednio zanonimizowane;
- analiza dużych zbiorów danych wymaga uwzględnienia ograniczeń pamięciowych i sposobu wczytywania plików;
- należy określić sposób obsługi kodowania tekstu, wielkości liter i znaków Unicode.

## 14. Literatura i źródła

1. Knuth, D. E., Morris, J. H., Pratt, V. R., *Fast Pattern Matching in Strings*, SIAM Journal on Computing, 1977.
2. Cormen, T. H. i in., *Introduction to Algorithms*, MIT Press.
3. Dokumentacja języka Python: https://docs.python.org/3/
4. [Dodatkowe materiały wykorzystane w projekcie.]

## 15. Licencja

Projekt został przygotowany na potrzeby dydaktyczne przedmiotu „Bezpieczeństwo Danych”.

Licencja: [np. MIT / projekt wyłącznie edukacyjny].
