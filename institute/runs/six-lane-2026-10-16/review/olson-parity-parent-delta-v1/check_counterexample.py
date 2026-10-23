"""Parent definition-first recheck of the p=13 defect-rule counterexample.
Imports no worker code. Uses D_26 = <r,f | r^13=f^2=1, frf=r^-1>, elements r^x f^e.
For every cyclic run-sign pattern, constrain only the parity of selected reflections in each constant run;
then do exact cardinality/group-product DP. This independently checks interval feasibility and all 8192
pattern hits, without using Lemma GR's window formula. The 26-letter witness is multiplied directly.
"""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    src = HERE / 'inputs/mixdef-low/record_z0_cex.json'
    C = json.loads(src.read_text())
    p = C['p']
    a, b, lengths = C['a'], C['b'], C['l']
    y = C['params']['y']
    k, target, full = len(a), 2 * p, (1 << p) - 1
    word = []
    for t in range(k):
        word += [('R', 1)] * a[t] + [('R', p - 1)] * b[t] + [('F', y[t])] * lengths[t]
    if len(word) != 4 * p - 2:
        raise ValueError('word length')

    def multiply(letters):
        e, x = 0, 0
        for kind, value in letters:
            x = (x + (-1 if e else 1) * value) % p
            e ^= int(kind == 'F')
        return e, x

    positions = C['DP']['witness_positions']
    if len(positions) != target or positions != sorted(set(positions)):
        raise ValueError('ordered witness indices')
    selected = [word[i] for i in positions]
    # Worker encodes negative rotations as -1; normalize only their exponents modulo p.
    stated = [(kind, value % p) for kind, value in C['DP']['witness_letters']]
    same_letters = selected == stated
    prod = multiply(selected)
    mutant = selected[:]
    idx = next(i for i, z in enumerate(mutant) if z[0] == 'R')
    mutant[idx] = ('R', (mutant[idx][1] + 1) % p)
    mutation_product = multiply(mutant)

    def rotate(bits, delta):
        delta %= p
        return ((bits << delta) | (bits >> (p - delta))) & full

    def pattern_has(mask):
        dp = [0] * (target + 1)
        dp[0] = 1  # exponent0 at cardinality0
        sign = 1
        for t in range(k):
            for value in [1] * a[t] + [-1] * b[t]:
                for count in range(target, 0, -1):
                    dp[count] |= rotate(dp[count - 1], sign * value)
            parity = ((mask >> t) ^ (mask >> ((t + 1) % k))) & 1
            choices = range(parity, lengths[t] + 1, 2)
            shift = sign * y[t] if parity else 0
            nxt = [0] * (target + 1)
            for count, bits in enumerate(dp):
                if not bits:
                    continue
                moved = rotate(bits, shift)
                for nref in choices:
                    if count + nref <= target:
                        nxt[count + nref] |= moved
            dp = nxt
            if parity:
                sign = -sign
        if sign != 1:
            raise ValueError('cyclic sign parity')
        return bool(dp[target] & 1)

    hits = [mask for mask in range(1 << k) if pattern_has(mask)]
    hitset = set(hits)
    intervals = {sum(1 << ((start + j) % k) for j in range(size))
                 for start in range(k) for size in range(1, k)}
    interval_hits = sorted(intervals & hitset)
    d = [a[t] - b[t] for t in range(k)]
    x = C['lifts']['x']
    theta = [(y[t - 1] - y[t]) % p for t in range(k)]
    lifts_bound = all((2 * x[t] - theta[t]) % p == 0 for t in range(k))
    bh = [2 * x[t] - d[t] for t in range(k)]
    Z = {t for t in range(k) if bh[t] <= 0}
    mZ = sum(t in Z and (t - 1) % k not in Z for t in range(k))
    phi = sum(d[t] - bh[t] for t in Z) + 2 * mZ
    A, B, R, F = sum(a), sum(b), sum(a) + sum(b), sum(lengths)
    H = sum(n // 2 for n in lengths)
    kappa = (R - (2 * p - k)) // 2
    g = kappa - B
    rec = {'recorded': subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip(),
           'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest(), 'word_length': len(word),
           'witness_same_letters': same_letters, 'witness_product': prod, 'mutation_product': mutation_product,
           'pattern_hits': len(hits), 'proper_interval_patterns': len(intervals), 'interval_hits': interval_hits,
           'pattern_1_3_hits': ((1 << 1) | (1 << 3)) in hitset,
           'params': {'p': p, 'k': k, 'A': A, 'B': B, 'R': R, 'F': F, 'H': H, 'kappa': kappa, 'g': g},
           'theta_matches': theta == C['theta'], 'lifts_bound_to_theta': lifts_bound, 'sum_lifts': sum(x),
           'bh': bh, 'Z0': sorted(Z), 'Phi_Z0': phi, 'threshold': 2 * g + 2,
           'Z0_pattern_hits': sum(1 << t for t in Z) in hitset}
    rec['verdict'] = 'PASS' if (same_letters and prod == (0, 0) and mutation_product != (0, 0)
                                and len(hits) == 664 and len(intervals) == 156 and not interval_hits
                                and rec['pattern_1_3_hits'] and rec['theta_matches'] and lifts_bound
                                and sum(x) == p and phi == 4 < 2 * g + 2 == 6
                                and not rec['Z0_pattern_hits']) else 'FAIL'
    with open(Path(__file__).with_suffix('.json'), 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps(rec))


if __name__ == '__main__':
    main()
