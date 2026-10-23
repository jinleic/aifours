"""Parent check of the finite-field facts used by Lemma K1-AG (PROOF_K1_K2.r1.md §4), written independently of the
lane's k1_analytic_checks_v2.py. GF(8) = GF(2)[x]/(x^3 + x + 1), elements encoded as 3-bit integers.
For every 3-subset T of GF(8): t0 = t1+t2+t3 is not in T; V = T + t0 has three distinct nonzero elements and
W = V u {0} is closed under addition; for all r != r' in GF(8)*, |rV n r'V| = 1; the seven sets rV cover every
nonzero element exactly three times. Writes moqls8-k1ag-parent-field-check-v1.json (mode x)."""
import json
import subprocess
from collections import Counter
from itertools import combinations
from pathlib import Path


def gmul(a, b):
    r = 0
    for i in range(3):
        if (b >> i) & 1:
            r ^= a << i
    for d in (4, 3):
        if (r >> d) & 1:
            r ^= 0b1011 << (d - 3)
    return r


def main():
    field_ok = all(gmul(a, 1) == a for a in range(8)) and all(
        sum(1 for b in range(1, 8) if gmul(a, b) == 1) == 1 for a in range(1, 8))
    fails, pairs, subsets = [], Counter(), 0
    for T in combinations(range(8), 3):
        subsets += 1
        t0 = T[0] ^ T[1] ^ T[2]
        V = {t ^ t0 for t in T}
        W = V | {0}
        ok = t0 not in T and 0 not in V and len(V) == 3 and all((a ^ b) in W for a in W for b in W)
        for r in range(1, 8):
            for r2 in range(r + 1, 8):
                k = len({gmul(r, v) for v in V} & {gmul(r2, v) for v in V})
                pairs[k] += 1
                ok = ok and k == 1
        cov = Counter(x for r in range(1, 8) for x in {gmul(r, v) for v in V})
        ok = ok and len(cov) == 7 and set(cov.values()) == {3}
        if not ok:
            fails.append(list(T))
    # mutation control: with a reducible modulus x^3 + 1 the intersection property must fail somewhere
    def gmul_bad(a, b):
        r = 0
        for i in range(3):
            if (b >> i) & 1:
                r ^= a << i
        for d in (4, 3):
            if (r >> d) & 1:
                r ^= 0b1001 << (d - 3)
        return r
    bad_hits = 0
    for T in combinations(range(8), 3):
        t0 = T[0] ^ T[1] ^ T[2]
        V = {t ^ t0 for t in T}
        for r in range(1, 8):
            for r2 in range(r + 1, 8):
                if len({gmul_bad(r, v) for v in V} & {gmul_bad(r2, v) for v in V}) != 1:
                    bad_hits += 1
    rec = {'recorded': subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip(),
           'field_ok': field_ok, 'subsets': subsets, 'intersection_sizes': dict(pairs), 'failures': fails,
           'mutation_reducible_modulus_failures': bad_hits,
           'verdict': 'PASS' if field_ok and subsets == 56 and not fails and dict(pairs) == {1: 1176} and bad_hits > 0
           else 'FAIL'}
    out = Path(__file__).with_suffix('.json')
    with open(out, 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps(rec))


if __name__ == '__main__':
    main()
