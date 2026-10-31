#!/usr/bin/env python3
"""proof-control-matching-exhaustive-v1.py  (reviewer-authored, f113 review)

Independent exhaustive control for Sections 4-5 of
frontier-20261028-global-ame46-maximal-coefficients29-v1.md.

Pure combinatorics on {0,1,2}^4, coordinates A,B,C,D.  A perfect matching
between the residual alphabets of a coordinate pair is the graph of a
permutation s of {0,1,2}: forbidden cells {(x, s(x))}.

For EVERY choice of six permutations (s_AB, s_AC, s_AD, s_BC, s_BD, s_CD)
-- 6^6 = 46656 configurations, NO relabeling -- let S be the set of
4-tuples avoiding all six forbidden cells.  We test:

 (a) Section 4 bound: |S| <= 12, and every A-fiber of S has <= 4 tuples.
 (b) Section 5 (equality case): no E subset of S satisfies the residual
     condition (1): all six pair projections equal the full 6-cell
     complement of the matching AND every projected cell has >= 2
     extensions.  The condition is monotone in E (projections and
     extension counts only grow with E), so it suffices to test S itself.
 (c) The three-cube-edge lemma: any three distinct edges of the 3-cube
     cover >= 4 vertices.
 (d) Cross-check of the author's relabeled counts (A-matchings = identity):
     histogram over 216 interleaf triples, maximum 12, drop-CD maximum 15.

The author's control code was NOT imported or executed.
"""
import itertools, json, sys
from collections import Counter
from pathlib import Path

PERMS = list(itertools.permutations(range(3)))
PAIRS = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
CELLS = list(itertools.product(range(3), repeat=4))


def avoiding(cfg):
    """cfg: dict pair->perm. Return tuples avoiding all six matchings."""
    out = []
    for w in CELLS:
        ok = True
        for (i, j), s in cfg.items():
            if w[j] == s[w[i]]:
                ok = False
                break
        if ok:
            out.append(w)
    return out


def residual_condition(S, cfg):
    """True iff every pair projection of S is the full 6-cell complement and
    every projected cell has >= 2 extensions in S."""
    for (i, j), s in cfg.items():
        cnt = Counter((w[i], w[j]) for w in S)
        comp = {(x, y) for x in range(3) for y in range(3) if y != s[x]}
        if set(cnt) != comp:
            return False
        if min(cnt.values()) < 2:
            return False
    return True


def fiber_dichotomy(S):
    """Section 5 bookkeeping for a 12-tuple S: per A-fiber, per pair among
    B,C,D classify projection as 'square' (4 distinct), 'correlated'
    (2 distinct, each twice) or 'other'."""
    rep = {}
    for a in range(3):
        F = [w for w in S if w[0] == a]
        rep[a] = {}
        for (j, k) in [(1,2),(1,3),(2,3)]:
            cnt = Counter((w[j], w[k]) for w in F)
            if len(F) == 4 and len(cnt) == 4:
                rep[a][f'{j}{k}'] = 'square'
            elif len(F) == 4 and len(cnt) == 2 and set(cnt.values()) == {2}:
                rep[a][f'{j}{k}'] = 'correlated'
            else:
                rep[a][f'{j}{k}'] = 'other'
    return rep


def main(out_path):
    total_hist = Counter()
    fiber_max = 0
    cond_hits = 0
    twelve_configs = 0
    twelve_failures = Counter()
    sample_twelve = None
    for perms in itertools.product(PERMS, repeat=6):
        cfg = dict(zip(PAIRS, perms))
        S = avoiding(cfg)
        total_hist[len(S)] += 1
        fs = Counter(w[0] for w in S)
        fiber_max = max(fiber_max, max(fs.values()) if fs else 0)
        if residual_condition(S, cfg):
            cond_hits += 1
        if len(S) == 12:
            twelve_configs += 1
            # which part of (1) fails on S?
            reasons = []
            for (i, j), s in cfg.items():
                cnt = Counter((w[i], w[j]) for w in S)
                comp = {(x, y) for x in range(3) for y in range(3) if y != s[x]}
                if set(cnt) != comp:
                    reasons.append(f'proj{i}{j}_size{len(cnt)}')
                elif min(cnt.values()) < 2:
                    reasons.append(f'proj{i}{j}_singleext')
            twelve_failures[tuple(sorted(reasons))] += 1
            if sample_twelve is None:
                sample_twelve = {'config': {f'{i}{j}': list(s) for (i, j), s in cfg.items()},
                                 'S': S, 'fiber_dichotomy': fiber_dichotomy(S),
                                 'failure_reasons': reasons}
    n_cfg = sum(total_hist.values())

    # (c) cube edge lemma
    cube = list(itertools.product((0, 1), repeat=3))
    edges = [frozenset((u, v)) for u, v in itertools.combinations(cube, 2)
             if sum(x != y for x, y in zip(u, v)) == 1]
    min_cover = min(len(frozenset().union(*T)) for T in itertools.combinations(edges, 3))

    # (d) relabeled cross-check: A-matchings identity, interleaf free
    ident = (0, 1, 2)
    rel_hist = Counter(); rel_fiber_max = 0
    for f, g, h in itertools.product(PERMS, repeat=3):
        cfg = {(0,1): ident, (0,2): ident, (0,3): ident, (1,2): f, (1,3): g, (2,3): h}
        S = avoiding(cfg)
        rel_hist[len(S)] += 1
        fs = Counter(w[0] for w in S)
        rel_fiber_max = max(rel_fiber_max, max(fs.values()) if fs else 0)
    drop_cd_max = 0
    for f, g in itertools.product(PERMS, repeat=2):
        cfg = {(0,1): ident, (0,2): ident, (0,3): ident, (1,2): f, (1,3): g}
        drop_cd_max = max(drop_cd_max, len(avoiding(cfg)))

    result = {
        'reviewer': 'f113 proof-review (same-harness), own code',
        'configurations_enumerated': n_cfg,
        'expected_configurations': 6 ** 6,
        'avoiding_size_histogram': dict(sorted(total_hist.items())),
        'max_avoiding_total': max(total_hist),
        'max_avoiding_per_A_fiber': fiber_max,
        'configs_with_12': twelve_configs,
        'configs_where_S_meets_residual_condition': cond_hits,
        'failure_reasons_on_12_configs': {' & '.join(k): v for k, v in sorted(twelve_failures.items())},
        'sample_12_config': sample_twelve,
        'three_cube_edges_min_vertex_cover': min_cover,
        'relabeled_A_identity': {
            'triples': sum(rel_hist.values()),
            'histogram': dict(sorted(rel_hist.items())),
            'max_total': max(rel_hist),
            'max_per_fiber': rel_fiber_max,
            'drop_CD_max': drop_cd_max,
        },
        'verdict_lines': [
            f'(a) max |S| = {max(total_hist)} (claim <=12): ' + ('PASS' if max(total_hist) <= 12 else 'FAIL'),
            f'(a) max A-fiber = {fiber_max} (claim <=4): ' + ('PASS' if fiber_max <= 4 else 'FAIL'),
            f'(b) configs whose S satisfies residual condition (1) = {cond_hits} (claim 0): ' + ('PASS' if cond_hits == 0 else 'FAIL'),
            f'(c) three distinct cube edges cover >= {min_cover} vertices (claim 4): ' + ('PASS' if min_cover == 4 else 'FAIL'),
        ],
    }
    p = Path(out_path)
    with p.open('x', encoding='utf-8') as fh:
        json.dump(result, fh, indent=1); fh.write('\n')
    for line in result['verdict_lines']:
        print(line)
    print('relabeled:', result['relabeled_A_identity'])
    print('12-config failure reasons:', result['failure_reasons_on_12_configs'])


if __name__ == '__main__':
    main(sys.argv[1])
