#!/usr/bin/env python3
"""Independent exact checks for f32; no author program or result imports."""
from collections import Counter
from itertools import combinations, product
import json
import random


def mul(x, y, p):
    return ((x[0] + (-1 if x[1] else 1) * y[0]) % p, x[1] ^ y[1])


def prod(word, ids, p):
    value = (0, 0)
    for i in ids:
        value = mul(value, word[i], p)
    return value


def omission(ys, j, p):
    word = [(y, 1) for y in ys]
    return prod(word, [i for i in range(len(ys)) if i != j], p)[0]


def rank_mod(mat, p):
    mat = [list(row) for row in mat]
    r = 0
    for c in range(len(mat[0])):
        pivot = next((i for i in range(r, len(mat)) if mat[i][c] % p), None)
        if pivot is None:
            continue
        mat[r], mat[pivot] = mat[pivot], mat[r]
        inverse = pow(mat[r][c] % p, -1, p)
        mat[r] = [(x * inverse) % p for x in mat[r]]
        for i in range(len(mat)):
            if i != r:
                t = mat[i][c] % p
                mat[i] = [(x - t*y) % p for x, y in zip(mat[i], mat[r])]
        r += 1
    return r


def reflection_assay():
    result = []
    for p in (3, 5, 7, 11, 13):
        N = 2*p + 1
        basis = [tuple(int(i == j) for i in range(N)) for j in range(N)]
        mat = [[omission(basis[j], i, p) for j in range(N)] for i in range(N)]
        if rank_mod(mat, p) != N-1:
            raise AssertionError('wrong omission-map rank')
        if any(sum((1 if i % 2 == 0 else -1)*mat[i][j] for i in range(N)) % p
               for j in range(N)):
            raise AssertionError('wrong alternating hyperplane')
        dp = [1] + [0]*(p-1)
        for _ in range(N):
            dp = [sum(dp[(v-a) % p] for a in range(1, p)) for v in range(p)]
        count = p * dp[0]
        if count != (p-1)**N-(p-1):
            raise AssertionError('wrong count formula')
        result.append({'p': p, 'dimension': N, 'rank': N-1, 'no_identity_count': count})
    exhaustive = sum(all(omission(ys, j, 3) for j in range(7))
                     for ys in product(range(3), repeat=7))
    if exhaustive != 126:
        raise AssertionError('bad p=3 omission count')
    return {'finite_field_ranks_and_counts': result, 'p3_words_exhaustive': 3**7,
            'p3_failing': exhaustive}


def extreme_assay():
    result = []
    for p in (3, 5, 7, 11, 13):
        modes = []
        for a in range(1, p):
            word = [(0, 1)]*(2*p-1) + [(a, 1), (2*a % p, 1)]
            word += [(a, 0)]*(2*p-3) + [(2*a % p, 0)]
            n = 2*p
            refs = list(range(2*p+1))
            rotations = list(range(2*p+1, len(word)))
            no_reflection = sum(prod(word, [i for i in refs if i != j], p) == (0, 0)
                                for j in refs)
            two_reflection = sum(prod(word, list(pair)+rotations, p) == (0, 0)
                                 for pair in combinations(refs, 2))
            if no_reflection or (p >= 5 and two_reflection) or (p == 3 and two_reflection != 5):
                raise AssertionError(('extreme-mode mismatch', p, a))
            chosen = list(range(p+1)) + rotations[:p-2] + [rotations[-1]]
            if len(chosen) != n or sorted(set(chosen)) != chosen or prod(word, chosen, p) != (0, 0):
                raise AssertionError('interior selector invalid')
            modes.append(two_reflection)
        result.append({'p': p, 'nonzero_exponents': p-1, 'reflection_only': 0,
                       'all_rotations_plus_two': sorted(set(modes)), 'interior_selector_valid': True})
    return result


def separated_pairs(bits):
    N = len(bits)
    dp = [0] * (N + 1)
    choice = [None] * N
    for i in range(N-1, -1, -1):
        dp[i] = dp[i+1]
        for j in range(i+1, N):
            if bits[i] == bits[j] and 1 + dp[j+1] > dp[i]:
                dp[i], choice[i] = 1 + dp[j+1], j
    pairs = []
    i = 0
    while i < N:
        if choice[i] is None or dp[i] == dp[i+1]:
            i += 1
        else:
            j = choice[i]
            pairs.append((i, j))
            i = j + 1
    if len(pairs) != dp[0]:
        raise AssertionError('bad separated-pair reconstruction')
    return pairs


def run_criterion(bits):
    runs = []
    for b in bits:
        if runs and runs[-1][0] == b:
            runs[-1][1] += 1
        else:
            runs.append([b, 1])
    odd = [i for i, (_, length) in enumerate(runs) if length % 2]
    return (len(odd) == 1 or len(odd) == 3
            and odd[1] == odd[0]+1 and odd[2] == odd[1]+1
            and runs[odd[1]][1] == 1)


def binary_assay():
    rng = random.Random(2026102804)
    results = []
    for k in range(1, 5):
        N, M = 4*k-1, 2*k-1
        count = lifted = 0
        for bits in product((0, 1), repeat=N):
            pairs = separated_pairs(bits)
            claimed = run_criterion(bits)
            if (len(pairs) == M) != claimed:
                raise AssertionError(('classification mismatch', k, bits))
            if not claimed:
                continue
            count += 1
            if k <= 3:
                # One actual lift of EACH classified quotient pattern to C_k x C_2.
                K = [rng.randrange(k) for _ in bits]
                packet = [(K[i]+K[j]) % k for i, j in pairs]
                packet_ids = next((z for z in combinations(range(M), k)
                                   if sum(packet[i] for i in z) % k == 0), None)
                if packet_ids is None:
                    raise AssertionError('actual kernel selector missing')
                indices = [v for z in packet_ids for v in pairs[z]]
                if (len(indices) != 2*k or indices != sorted(set(indices))
                        or sum(K[i] for i in indices) % k != 0
                        or sum(bits[i] for i in indices) % 2 != 0):
                    raise AssertionError('actual original-order selector invalid')
                lifted += 1
        expected = 4*k*(1 << (2*k-1))
        if count != expected:
            raise AssertionError('closed count mismatch')
        results.append({'k': k, 'words': 1 << N, 'saturated': count, 'actual_lifts_checked': lifted})
    return {'seed': 2026102804, 'domains': results}


if __name__ == '__main__':
    print(json.dumps({'reflection': reflection_assay(), 'double_extreme': extreme_assay(),
                      'binary': binary_assay()}, indent=2, sort_keys=True))
