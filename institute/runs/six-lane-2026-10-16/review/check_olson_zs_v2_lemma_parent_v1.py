"""Parent finite AID (not a proof premise) for Lemma ZS of proof-ROT-half-v2 (7403098f...).
For prime p and integers k, kappa with (G): k>=1, 3k<=2p+1, 0<=kappa<=min(k-1,p-k), enumerate EVERY multiset Y of
R=2p+2kappa-k odd elements of Z_(2p) satisfying (ZP): no zero-sum sub-multiset of length in [2kappa+2, 2p].
Check: some odd generator g gives cost_g(Y) <= k-1 (cost as in the lemma: b>0 costs b-1, b<0 costs |b|, b in (-p,p]).
Enumeration: DFS over nondecreasing element lists; (ZP) is hereditary, so a violating prefix is pruned.
Self-bounded: stops cleanly after BUDGET seconds and marks unfinished parameter sets INCOMPLETE.
Usage: python3 -B check_olson_zs_v2_lemma_parent_v1.py OUTDIR  (OUTDIR must not exist)
"""
import json
import math
import os
import sys
import time

BUDGET = 1500.0
CASES = [(5, None), (7, None), (11, 7), (13, 9)]  # (p, only_k) ; None = every k allowed by (G)


def run_case(p, k, kappa, deadline):
    n = 2 * p
    odd = list(range(1, n, 2))
    gens = [g for g in odd if math.gcd(g, n) == 1]
    inv = {g: pow(g, -1, n) for g in gens}
    R = 2 * p + 2 * kappa - k
    lo, hi = 2 * kappa + 2, 2 * p
    full = (1 << n) - 1
    stats = {'p': p, 'k': k, 'kappa': kappa, 'R': R, 'zp_multisets': 0, 'violations': 0, 'nodes': 0,
             'max_min_cost': None, 'complete': True}
    viol_examples = []

    def rot(mask, x):
        return ((mask << x) | (mask >> (n - x))) & full

    def cost(counts, g):
        gi = inv[g]
        c = 0
        for x, m in counts.items():
            b = (x * gi) % n
            if b > p:
                b -= n
            c += m * ((b - 1) if b > 0 else -b)
        return c

    # reach[l] = bitmask of sums reachable with sub-multisets of length l (l=0..R)
    def dfs(start, size, reach, counts):
        if time.monotonic() > deadline:
            stats['complete'] = False
            return
        stats['nodes'] += 1
        if size == R:
            stats['zp_multisets'] += 1
            best = min(cost(counts, g) for g in gens)
            if stats['max_min_cost'] is None or best > stats['max_min_cost']:
                stats['max_min_cost'] = best
            if best > k - 1:
                stats['violations'] += 1
                if len(viol_examples) < 5:
                    viol_examples.append(dict(counts))
            return
        for idx in range(start, len(odd)):
            x = odd[idx]
            new = list(reach)
            for l in range(size, -1, -1):
                if reach[l]:
                    new[l + 1] |= rot(reach[l], x)
            bad = any(new[l] & 1 for l in range(lo, min(hi, size + 1) + 1))
            if bad:
                continue
            counts[x] = counts.get(x, 0) + 1
            dfs(idx, size + 1, new, counts)
            counts[x] -= 1
            if counts[x] == 0:
                del counts[x]
            if not stats['complete']:
                return

    reach0 = [0] * (R + 2)
    reach0[0] = 1
    dfs(0, 0, reach0, {})
    stats['violation_examples'] = viol_examples
    return stats


def main():
    out = sys.argv[1]
    os.mkdir(out)
    t0 = time.monotonic()
    deadline = t0 + BUDGET
    results = []
    for p, only_k in CASES:
        for k in range(1, (2 * p + 1) // 3 + 1):
            if only_k is not None and k != only_k:
                continue
            for kappa in range(0, min(k - 1, p - k) + 1):
                if time.monotonic() > deadline:
                    results.append({'p': p, 'k': k, 'kappa': kappa, 'complete': False, 'status': 'NOT_STARTED'})
                    continue
                s = run_case(p, k, kappa, deadline)
                s['status'] = 'PASS' if s['complete'] and s['violations'] == 0 else (
                    'FAIL' if s['violations'] else 'INCOMPLETE')
                s['new_in_v2'] = k > (p + 1) // 2
                results.append(s)
                print(json.dumps({x: s[x] for x in ('p', 'k', 'kappa', 'R', 'zp_multisets', 'violations',
                                                     'max_min_cost', 'status')}), flush=True)
    summary = {'script': os.path.abspath(__file__), 'elapsed_s': round(time.monotonic() - t0, 1),
               'all_pass': all(r['status'] == 'PASS' for r in results), 'results': results,
               'scope': 'finite aid only; not a premise of any accepted statement'}
    with open(os.path.join(out, 'RESULT-v1.json'), 'x') as f:
        json.dump(summary, f, indent=1)
        f.write('\n')
    print(json.dumps({'all_pass': summary['all_pass'], 'elapsed_s': summary['elapsed_s']}))


if __name__ == '__main__':
    main()
