#!/usr/bin/env python3
"""Reviewer-authored exact controls for the active-count slice of the AME(4,6) >=46 review.

Written independently of the author's control scripts (which were read for scope only).
Three controls:
  A. Integer arithmetic for the n=7 active-coordinate counting contradiction and the
     general inequality sum_i(6r_i-n) - sum_{i<j}(r_i r_j - n) <= 36-n over all
     feasible n=7 alphabet-size vectors.
  B. Exhaustive 7x7 0/1 support patterns with 16 ones, row/col degree >=2, satisfying
     the necessary unitary conditions (no two rows / columns overlap in exactly one
     position; connected components square). Verifies max row/col degree <= 3 and the
     3x3(8)+2x2+2x2 shape, and separately that a degree-4 row never survives.
  C. Enumeration of residual supports E in {0,1,2}^4 with |E|=16 whose cut-(01|23)
     flattening has the 3x3(8)+2x2+2x2 shape, filtered by all six pair projections
     having exactly 7 values with 2..3 extensions each (row-missing-pair orbit reps).
     For each survivor the forced P-side counts (11 per party, 2 per pair) are
     recomputed from the pair partition, and an exact-cover DFS for a 29-word P is run
     with a node cap as a bonus independence check.
Usage: python3 -B active-count-controls-v1.py <new-output.json>
"""
import argparse
import itertools
import json
import sys
import time
from pathlib import Path


# ---------------------------------------------------------------- A: arithmetic
def control_a():
    w = {k: k - k * (k - 1) // 2 for k in range(5)}
    assert w == {0: 0, 1: 1, 2: 1, 3: 0, 4: -2}
    n, t = 7, 29
    per_party = 6 * 3 - n           # P words active at a given party
    per_pair = 3 * 3 - n            # P words active at both parties of a pair
    s1 = 4 * per_party              # sum_x k(x)
    s2 = 6 * per_pair               # sum_x C(k(x),2)
    assert (per_party, per_pair, s1, s2) == (11, 2, 44, 12)
    assert s1 - s2 == 32 > t
    # nonneg integer multiplicities m_k with sum m_k = 29, sum k m_k = 44, sum C(k,2) m_k = 12
    sols = []
    for m4 in range(30):
        for m3 in range(30):
            m2 = 12 - 3 * m3 - 6 * m4
            if m2 < 0:
                continue
            m1 = 44 - 2 * m2 - 3 * m3 - 4 * m4
            m0 = 29 - m1 - m2 - m3 - m4
            if m1 >= 0 and m0 >= 0:
                sols.append((m0, m1, m2, m3, m4))
    assert sols == []
    # cross-check: for any multiplicities, m0 + m3 + 3 m4 = 29 - 32 = -3 identity
    # general inequality over feasible n=7 alphabet sizes (every pair product >= 7)
    def lhs(nn, r):
        return sum(6 * a - nn for a in r) - sum(r[i] * r[j] - nn for i, j in itertools.combinations(range(4), 2))
    rejected, accepted = [], []
    for r in itertools.product(range(1, 5), repeat=4):
        if r != tuple(sorted(r)):
            continue
        if any(r[i] * r[j] < 7 for i, j in itertools.combinations(range(4), 2)):
            continue
        (rejected if lhs(7, r) > 29 else accepted).append({'r': r, 'lhs': lhs(7, r)})
    assert [x['r'] for x in rejected] == [(3, 3, 3, 3)]
    return {
        'per_word_weights': w,
        'n': n, 't': t, 'P_words_active_per_party': per_party, 'P_words_active_per_pair': per_pair,
        'sum_k': s1, 'sum_C_k_2': s2, 'sum_k_minus_C': s1 - s2, 'bound': t,
        'multiplicity_solutions': sols,
        'n7_general_inequality_rejected': rejected,
        'n7_general_inequality_not_rejected': accepted,
        'n6_3333_lhs': lhs(6, (3, 3, 3, 3)), 'n6_bound': 30,
    }


# ---------------------------------------------------------------- B: 7x7 support patterns
def components(rows, n):
    remain = set(range(n))
    out = []
    while remain:
        rr = {min(remain)}
        while True:
            cols = 0
            for i in rr:
                cols |= rows[i]
            grow = {i for i in remain if rows[i] & cols}
            if grow == rr:
                break
            rr = grow
        out.append((tuple(sorted(rr)), cols))
        remain -= rr
    return out


def control_b(n=7, nnz=16):
    masks = [m for m in range(1 << n) if 2 <= bin(m).count('1') <= nnz - 2 * (n - 1)]
    pc = {m: bin(m).count('1') for m in masks}
    survivors = []
    stats = {'leaves_row_filtered': 0, 'col_degree_or_overlap_rejected': 0, 'rectangular_rejected': 0,
             'degree4_row_leaves': 0}

    def rec(rows, start, budget):
        k = len(rows)
        if k == n:
            if budget != 0:
                return
            stats['leaves_row_filtered'] += 1
            if max(pc[r] for r in rows) >= 4:
                stats['degree4_row_leaves'] += 1
            cols = [sum(((rows[i] >> j) & 1) << i for i in range(n)) for j in range(n)]
            if any(bin(c).count('1') < 2 for c in cols) or \
               any(bin(a & b).count('1') == 1 for a, b in itertools.combinations(cols, 2)):
                stats['col_degree_or_overlap_rejected'] += 1
                return
            parts = components(rows, n)
            if any(len(rr) != bin(cm).count('1') for rr, cm in parts):
                stats['rectangular_rejected'] += 1
                return
            survivors.append(tuple(rows))
            return
        remaining = n - k
        for idx in range(start, len(masks)):
            m = masks[idx]
            p = pc[m]
            # remaining rows (including this one) need at least 2 each
            if p + 2 * (remaining - 1) > budget:
                continue
            # max possible with remaining rows each <= budget: skip check, budget small
            if any(bin(m & r).count('1') == 1 for r in rows):
                continue
            rows.append(m)
            rec(rows, idx, budget - p)
            rows.pop()

    rec([], 0, nnz)
    shapes = {}
    maxdeg = 0
    for rows in survivors:
        cols = [sum(((rows[i] >> j) & 1) << i for i in range(n)) for j in range(n)]
        maxdeg = max(maxdeg, max(pc[r] for r in rows), max(bin(c).count('1') for c in cols))
        parts = components(rows, n)
        shape = tuple(sorted((len(rr), sum(pc[rows[i]] for i in rr)) for rr, cm in parts))
        shapes[str(shape)] = shapes.get(str(shape), 0) + 1
    return {'n': n, 'nnz': nnz, 'row_masks_considered': len(masks), **stats,
            'survivors_up_to_row_order': len(survivors), 'max_degree_among_survivors': maxdeg,
            'component_shapes_(size,nnz)': shapes}


# ---------------------------------------------------------------- C: residual geometry
PAIRS = list(itertools.combinations(range(4), 2))


def proj_counts(E, i, j):
    d = {}
    for x in E:
        key = (x[i], x[j])
        d[key] = d.get(key, 0) + 1
    return d


def residual_ok(E):
    for i, j in PAIRS:
        d = proj_counts(E, i, j)
        if len(d) != 7 or any(c < 2 or c > 3 for c in d.values()):
            return False
    return True


def missing_orbit_reps():
    # two missing pairs in a 3x3 grid, up to S3 x S3: same row, same column, or neither
    return {'same_row': ((0, 0), (0, 1)), 'same_col': ((0, 0), (1, 0)), 'diagonal': ((0, 0), (1, 1))}


def patterns_7x7():
    """All 7x7 supports of shape 3x3(8) + 2x2 + 2x2 on labelled rows/cols 0..6."""
    out = []
    for brow in itertools.combinations(range(7), 3):
        rest_r = [r for r in range(7) if r not in brow]
        for bcol in itertools.combinations(range(7), 3):
            rest_c = [c for c in range(7) if c not in bcol]
            for miss in itertools.product(brow, bcol):
                block = [(r, c) for r in brow for c in bcol if (r, c) != miss]
                # split rest rows into two pairs: fix rest_r[0]'s partner
                for partner in rest_r[1:]:
                    rp1 = (rest_r[0], partner)
                    rp2 = tuple(r for r in rest_r if r not in rp1)
                    for cp1 in itertools.combinations(rest_c, 2):
                        cp2 = tuple(c for c in rest_c if c not in cp1)
                        for (ra, ca), (rb, cb) in (((rp1, cp1), (rp2, cp2)), ((rp1, cp2), (rp2, cp1))):
                            out.append(block + [(r, c) for r in ra for c in ca] + [(r, c) for r in rb for c in cb])
    return out


def exact_cover_P(E, node_cap=200000):
    """DFS for 29 words in 6^4 pairwise pair-distinct, pair-disjoint from E, covering all
    non-E pair values once. Returns ('infeasible', nodes) or ('found', nodes) or ('capped', nodes)."""
    Eproj = {p: set(proj_counts(E, *p)) for p in PAIRS}
    cands = [w for w in itertools.product(range(6), repeat=4)
             if all((w[i], w[j]) not in Eproj[(i, j)] for i, j in PAIRS)]
    slots = {(p, v): [] for p in PAIRS for v in itertools.product(range(6), repeat=2) if v not in Eproj[p]}
    for idx, w in enumerate(cands):
        for p in PAIRS:
            slots[(p, (w[p[0]], w[p[1]]))].append(idx)
    covered = set()
    nodes = [0]
    used_words = []

    def rec():
        nodes[0] += 1
        if nodes[0] > node_cap:
            raise TimeoutError
        if len(covered) == len(slots):
            return True
        # choose uncovered slot with fewest available words
        best, bestlist = None, None
        for s, lst in slots.items():
            if s in covered:
                continue
            avail = [idx for idx in lst if all(((p, (cands[idx][p[0]], cands[idx][p[1]])) not in covered) for p in PAIRS)]
            if best is None or len(avail) < len(bestlist):
                best, bestlist = s, avail
                if not avail:
                    return False
        for idx in bestlist:
            w = cands[idx]
            keys = [(p, (w[p[0]], w[p[1]])) for p in PAIRS]
            covered.update(keys)
            used_words.append(w)
            if rec():
                return True
            used_words.pop()
            covered.difference_update(keys)
        return False

    try:
        found = rec()
    except TimeoutError:
        return 'capped', nodes[0], len(cands)
    return ('found' if found else 'infeasible'), nodes[0], len(cands)


def control_c(dfs_samples=3, node_cap=200000):
    reps = missing_orbit_reps()
    allpairs = [(a, b) for a in range(3) for b in range(3)]
    pats = patterns_7x7()
    results = {'patterns_per_row_col_choice': len(pats), 'orbit_combos': {}, 'total_survivors': 0}
    survivors = []
    for rname, rmiss in reps.items():
        rows = [p for p in allpairs if p not in rmiss]
        for cname, cmiss in reps.items():
            cols = [p for p in allpairs if p not in cmiss]
            cnt = 0
            for pat in pats:
                E = [(rows[r][0], rows[r][1], cols[c][0], cols[c][1]) for r, c in pat]
                if residual_ok(E):
                    cnt += 1
                    survivors.append(E)
            results['orbit_combos'][f'{rname}|{cname}'] = cnt
    results['total_survivors'] = len(survivors)
    # recompute forced P-side counts from the pair partition for every survivor
    bad = 0
    for E in survivors:
        R = [sorted({x[i] for x in E}) for i in range(4)]
        if any(len(r) != 3 for r in R):
            bad += 1
            continue
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                d = proj_counts(E, i, j)
                active_rows = [(a, b) for a in R[i] for b in range(6)]
                if sum(1 for ab in active_rows if ab not in d) != 11:
                    bad += 1
        for i, j in PAIRS:
            d = proj_counts(E, i, j)
            if sum(1 for a in R[i] for b in R[j] if (a, b) not in d) != 2:
                bad += 1
    results['survivors_with_wrong_forced_counts'] = bad
    results['all_survivor_alphabets_size_3'] = all(len({x[i] for x in E}) == 3 for E in survivors for i in range(4))
    dfs = []
    for E in survivors[:dfs_samples]:
        t0 = time.time()
        status, nodes, ncand = exact_cover_P(E, node_cap)
        dfs.append({'E': E, 'status': status, 'nodes': nodes, 'candidate_words': ncand, 'seconds': round(time.time() - t0, 2)})
    results['exact_cover_dfs'] = dfs
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out', type=Path)
    a = ap.parse_args()
    if a.out.exists():
        sys.exit(f'refusing to overwrite {a.out}')
    t0 = time.time()
    res = {'A_arithmetic': control_a()}
    res['B_7x7_support_patterns'] = control_b()
    res['C_residual_geometry'] = control_c()
    res['elapsed_seconds'] = round(time.time() - t0, 2)
    res['scope'] = ('Reviewer-authored bounded exact controls; not a proof of the universal statements, '
                    'not independent-family or formal verification.')
    with a.out.open('x', encoding='utf-8') as f:
        json.dump(res, f, indent=2, default=str)
        f.write('\n')
    print(json.dumps(res, indent=2, default=str))


if __name__ == '__main__':
    main()
