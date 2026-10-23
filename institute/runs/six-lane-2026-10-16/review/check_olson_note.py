"""Finite independent controls for the hand-checked Olson collaborator note."""
from __future__ import annotations

import itertools
import json
from math import gcd


def mul(x: tuple[int, int], y: tuple[int, int], d: int) -> tuple[int, int]:
    return ((x[0] + (-1 if x[1] else 1) * y[0]) % d, x[1] ^ y[1])


def prod(xs: list[tuple[int, int]], d: int) -> tuple[int, int]:
    out = (0, 0)
    for x in xs:
        out = mul(out, x, d)
    return out


def check_examples() -> list[dict]:
    examples = [
        (3, [(1, 1), (0, 1), (1, 1), (0, 1), (0, 0), (0, 0)], [[0, 2], [1, 3], [4, 5]], (2, 0)),
        (4, [(1, 0), (0, 1), (3, 0), (0, 1), (0, 0), (0, 0), (0, 0), (0, 0)], [[0, 2, 4, 6], [1, 3, 5, 7]], (2, 0)),
    ]
    records = []
    for d, word, blocks, expected in examples:
        block_products = [prod([word[i] for i in block], d) for block in blocks]
        actual = prod(word, d)
        if any(p != (0, 0) for p in block_products) or actual != expected:
            raise RuntimeError('Interleaving obstruction mismatch')
        records.append({'rotation_order': d, 'word': word, 'blocks': blocks,
                        'block_products': block_products, 'union_product': actual})
    word = [(1, 0) if i % 2 == 0 else (0, 1) for i in range(11)]
    spans = [(i, j) for i in range(11) for j in range(i + 1, 11)
             if (word[i][1] ^ word[j][1]) == 0]
    best = [0] * 12
    for end in range(1, 12):
        best[end] = best[end - 1]
        for i, j in spans:
            if j == end - 1:
                best[end] = max(best[end], best[i] + 1)
    if best[11] != 3:
        raise RuntimeError('Separated quotient-pair count mismatch')
    records.append({'S3_alternating_word': word, 'max_separated_quotient_pairs': best[11],
                    'rotation_only_six_subword_product': prod(word[::2], 3)})
    return records


def check_inverse_thresholds() -> dict:
    checked = 0
    for n in range(3, 65):
        for d in range(3, n + 1):
            if n % d:
                continue
            delta = d // gcd(d, 2)
            for x in range(n):
                for y in range(n):
                    if x + y < n + delta - 1:
                        continue
                    valid = [k for k in range(max(0, n - y), min(n, x) + 1)
                             if (2 * k - n) % d == 0]
                    if not valid:
                        raise RuntimeError(f'Inverse threshold failed n={n},d={d},x={x},y={y}')
                    checked += 1
    return {'n_max': 64, 'qualifying_count_pairs_checked': checked}


def check_affine_products() -> dict:
    checked = 0
    for d in range(3, 10):
        letters = list(itertools.product(range(d), range(2)))
        for word in itertools.product(letters, repeat=3):
            parity = 0
            exponent = 0
            for x, e in word:
                exponent = (exponent + (-1 if parity else 1) * x) % d
                parity ^= e
            if prod(list(word), d) != (exponent, parity):
                raise RuntimeError('Affine product identity mismatch')
            checked += 1
    return {'rotation_orders': [3, 4, 5, 6, 7, 8, 9], 'length_three_words_checked': checked}


def main() -> None:
    print(json.dumps({'status': 'FINITE_CONTROLS_PASS', 'obstructions': check_examples(),
                      'inverse_count_threshold': check_inverse_thresholds(),
                      'affine_product_identity': check_affine_products(),
                      'limits': 'Finite controls only; universal statements still rest on the written proof. No novelty or breakthrough claim.'}, indent=2))


if __name__ == '__main__':
    main()
