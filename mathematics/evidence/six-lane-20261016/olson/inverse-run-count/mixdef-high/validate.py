"""Validation of mhc.cpp's exact search (in-process Python + the compiled binary run by the shell):
find a genuine avoider (type (I) shape, B = 0, kappa = 0, all-odd, p = 5) with ../hw.py hw_avoids,
confirm it with the raw ordered-product DP, and print the datum for `mhc one`."""
import sys, os, itertools
sys.path.insert(0, '..')
from hw import hw_avoids, dp_has, word_of
p = 5
a = [1, 1, 1, 1, 1]; b = [0] * 5; l = [5, 5, 1, 1, 1]
found = None
for ys in itertools.product(range(p), repeat=4):
    y = list(ys) + [0]
    if hw_avoids(a, b, l, y, p):
        found = y; break
print('avoider y:', found)
if found:
    print('raw DP has identity 2p-subword:', dp_has(word_of(a, b, l, found, p), p))
print('mhc one args:', p, len(a), *a, *b, *l)
