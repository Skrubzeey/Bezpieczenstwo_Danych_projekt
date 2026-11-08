from src.algorithms.naive_algorithm import naive_search

text = "aabbbaaacaab"
pattern = "aab"

print(naive_search(pattern=pattern, text=text))