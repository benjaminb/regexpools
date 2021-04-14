from random import randint, choices
import re, string
from tqdm import trange, tqdm

UNWANTED = '#()[]{}*^+$|\\?<>' + string.whitespace
ALPHABET = [c for c in string.printable if c not in UNWANTED]

class RegexGenerator():

    def __init__(self, text):
        self.text = text
        self.clause_types = [self.random_ngram, 
                             self.random_or_clause, 
                             self.random_star_clause]

    def random_ngram(self, length=4):
        '''Picks a random ngram from the text'''
        assert length <= len(self.text), "Selected ngram length is longer than the text"
        
        start = randint(1, len(self.text) - length)
        return self.text[start:start + length]

    def random_or_clause(self, num_ngrams=8, ngram_len=4, random_ngram_len=False):
        '''Constructs a random or clause for a regex using ngrams of length ngram_len
           If random_ngram_len=True, then ngrams will be of length 2 to ngram_len, inclusive'''
        r = '('

        # If using random ngram lengths, choose randomly. Else, use a constant function
        def rand_func(n):
            return randint(1, n)
        
        def const_func(n):
            return ngram_len

        ngram_len_func = rand_func if random_ngram_len else const_func

        r += ''.join(self.random_ngram(ngram_len_func(ngram_len)) + '|' for _ in range(num_ngrams))

        # Replace last pipe with closing paren
        return r[:-1] + ')'

    def random_star_clause(self, ngram_len=4):
        return '(' + self.random_ngram(ngram_len) + ')*'

    def random_regex(self, probs=[0.5, 0.35, 0.15], min_length=2, max_length=16):
        r = ""
        length = randint(min_length, max_length)
        for _ in range(length):
            clause_type = choices(self.clause_types, weights=probs, k=1)[0]
            r += clause_type()
        return r