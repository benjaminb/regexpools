from RegexGenerator import RegexGenerator


reg = RegexGenerator("Hello how are you? I am fine")

print(f"Test getting ngrams:")
for _ in range(3):
    print(f'\t\"{reg.random_ngram(3)}\"')


print("Test random_or_clause:")
for _ in range(3):
    print(f'\t\"{reg.random_or_clause(3)}\"')



print("Test random_or_clause with random ngram length:")
for _ in range(3):
    print(f'\t\"{reg.random_or_clause(3, random_ngram_len=True)}\"')

print("Test random regex generator:")
for _ in range(3):
    print(f'\t\"{reg.random_regex([0.3, 0.5, 0.2])}\"')