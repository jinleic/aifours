#!/usr/bin/env python3
"""Raw D_(2p) ordered-subword smoke for the seven c5 HYP run structures.
No half-window/lambda code or claimant imports. Finite reflection-label samples only, not a universal proof.
Usage: python3 -B olson_c5_raw_ordered_smoke.py NEW_OUTPUT_DIRECTORY
"""
import ast
from datetime import datetime
import hashlib
import itertools
import json
from pathlib import Path
import random
import re
import sys
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
PROOF = HERE / 'olson-c5-parent-inputs-v1/inverse-run-count/mixdef-high/c5/proof-Cplus-r1.md'
EXPECTED = 'd5a1ba78834e7cfb452c8e97066cf29a81ca659f53928936643bd5115ebeaf4a'


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def multiply(a, b, p):
    return ((a[0] + (-b[0] if a[1] else b[0])) % p, a[1] ^ b[1])


def product(word, indices, p):
    acc = (0, 0)
    for i in indices:
        acc = multiply(acc, word[i], p)
    return acc


def ordered_witness(word, size, p):
    states = [dict() for _ in range(size + 1)]
    states[0][(0, 0)] = ()
    for i, letter in enumerate(word):
        for n in range(min(size, i + 1), 0, -1):
            for state, selected in states[n - 1].items():
                dest = multiply(state, letter, p)
                if dest not in states[n]:
                    states[n][dest] = selected + (i,)
        if (0, 0) in states[size]:
            return states[size][(0, 0)]
    return None


def main():
    out = Path(sys.argv[1])
    out.mkdir(exist_ok=False)
    start = time.monotonic()
    raw = PROOF.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == EXPECTED, 'proof pin mismatch')
    pattern = r'^ H([1-7]): p = ([0-9]+),[^\n]*\n     a = (\[[^\n]*?\]), b = (\[[^\n]*?\]), l = (\[[^\n]*?\])$'
    data = re.findall(pattern, raw.decode(), flags=re.MULTILINE)
    require(len(data) == 7, 'seven run data rows not found')
    # These two words have the same letters but different ordered products.
    rho, sigma = (1, 0), (0, 1)
    require(ordered_witness([rho, sigma, rho, sigma], 4, 5) == (0, 1, 2, 3), 'ordered positive control')
    require(ordered_witness([rho, rho, sigma, sigma], 4, 5) is None, 'order-sensitive negative control')
    rng = random.Random(20261017)
    for _ in range(32):
        word = [(rng.randrange(5), rng.randrange(2)) for _ in range(8)]
        brute = next((q for q in itertools.combinations(range(8), 4) if product(word, q, 5) == (0, 0)), None)
        fast = ordered_witness(word, 4, 5)
        require((brute is None) == (fast is None), 'DP/brute mismatch')
        if fast is not None:
            require(product(word, fast, 5) == (0, 0), 'bad DP control witness')
    rows = []
    for h, ptext, aa, bb, ll in data:
        p = int(ptext)
        a, b, lengths = [ast.literal_eval(z) for z in (aa, bb, ll)]
        k = len(a)
        require(len(b) == len(lengths) == k, 'run lengths inconsistent')
        ys = [[0] * k, [1] * k, [j % 2 for j in range(k)], [j % p for j in range(k)]]
        ys += [[rng.randrange(p) for _ in range(k)] for _ in range(60)]
        instances = []
        for labels in ys:
            if time.monotonic() - start > 120:
                raise RuntimeError('UNKNOWN: internal 120s smoke cap')
            word = []
            for pos in range(k):
                word += [(1, 0)] * a[pos] + [(p - 1, 0)] * b[pos]
                word += [(labels[pos], 1)] * lengths[pos]
            require(len(word) == 4 * p - 2, 'wrong inherited word length')
            witness = ordered_witness(word, 2 * p, p)
            require(witness is not None, 'candidate counterexample: inspect raw word before any claim')
            require(len(witness) == 2 * p and list(witness) == sorted(set(witness))
                    and product(word, witness, p) == (0, 0), 'invalid ordered witness')
            instances.append({'reflection_labels': labels, 'identity_subword_indices_zero_based': witness,
                              'raw_word_sha256': hashlib.sha256(json.dumps(word, separators=(',', ':')).encode()).hexdigest()})
        rows.append({'H': int(h), 'p': p, 'raw_word_length': 4 * p - 2, 'samples': len(instances),
                     'instances': instances})
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(), 'status': 'PASS',
              'proof_sha256': EXPECTED, 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'seed': 20261017, 'word_structures': 7, 'raw_words_checked': sum(r['samples'] for r in rows),
              'controls': {'order_sensitive_positive': True, 'same_multiset_order_sensitive_negative': True,
                           'brute_short_words': 32}, 'wall_seconds': time.monotonic() - start, 'rows': rows,
              'scope': '448 explicit ordered-subword witnesses in the 7 HYP run structures; no universal theorem, no reflection-label exhaustion, no new Olson gate.'}
    with (out / 'result.json').open('x') as f:
        json.dump(result, f, indent=1)
        f.write('\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'rows'}, indent=1))


if __name__ == '__main__':
    main()
