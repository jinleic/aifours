#!/usr/bin/env python3
"""proof-control-profile-count-v1.py  (reviewer-authored, f113 review)

Independent control for Section 2 of
frontier-20261028-global-ame46-maximal-coefficients29-v1.md.

Given residual alphabet sizes (r_0..r_3) with n=6, the P code (30 words,
pair-injective, pair projections = complements of the 6-cell E projections)
must satisfy, with c_S = number of P words whose active coordinate set is
exactly S (S subset of {0,1,2,3}):
    sum_S c_S = 30
    sum_{S contains i} c_S = 6 r_i - 6              (i = 0..3)
    sum_{S contains i,j} c_S = r_i r_j - 6          (i<j)
    c_S >= 0 integers.
This is the full pattern-count system, of which the candidate's identity (1)
is one linear consequence.  We decide feasibility exactly by brute force over
the 16 nonnegative integer unknowns (bounded by the pair equations), for
every profile in {1,2,3}^4 with every pair product >= 6, plus a direct
numeric evaluation of identity (1) and the per-word maximum.
"""
import itertools, json, sys
from pathlib import Path

SUBSETS = [frozenset(s) for k in range(5) for s in itertools.combinations(range(4), k)]
PAIRS = [(i, j) for i in range(4) for j in range(i + 1, 4)]


def feasible(r):
    single = {i: 6 * r[i] - 6 for i in range(4)}
    pair = {(i, j): r[i] * r[j] - 6 for (i, j) in PAIRS}
    if any(v < 0 for v in pair.values()):
        return False, None
    # Order unknowns: 4-set, 3-sets, 2-sets, 1-sets, empty; bound each by the
    # tightest containing-pair equation and prune greedily.
    order = sorted(SUBSETS, key=lambda s: -len(s))

    def rec(idx, c, used_single, used_pair, total):
        if idx == len(order):
            if total != 30:
                return None
            if any(used_single[i] != single[i] for i in range(4)):
                return None
            if any(used_pair[p] != pair[p] for p in PAIRS):
                return None
            return dict(c)
        S = order[idx]
        ub = 30 - total
        for i in S:
            ub = min(ub, single[i] - used_single[i])
        for p in PAIRS:
            if p[0] in S and p[1] in S:
                ub = min(ub, pair[p] - used_pair[p])
        if ub < 0:
            return None
        # when S is a 1-set, its count is forced by the single equation
        # once all larger sets are placed (every larger set containing i is done)
        rng = range(ub, -1, -1)
        if len(S) == 1:
            i = next(iter(S))
            forced = single[i] - used_single[i]
            rng = [forced] if 0 <= forced <= ub else []
        if len(S) == 0:
            forced = 30 - total
            rng = [forced] if forced >= 0 else []
        for v in rng:
            c[S] = v
            for i in S:
                used_single[i] += v
            for p in PAIRS:
                if p[0] in S and p[1] in S:
                    used_pair[p] += v
            res = rec(idx + 1, c, used_single, used_pair, total + v)
            for i in S:
                used_single[i] -= v
            for p in PAIRS:
                if p[0] in S and p[1] in S:
                    used_pair[p] -= v
            if res is not None:
                return res
            del c[S]
        return None

    out = rec(0, {}, {i: 0 for i in range(4)}, {p: 0 for p in PAIRS}, 0)
    return (out is not None), out


def identity_one(r):
    rhs = sum(6 * r[i] - 6 for i in range(4)) - sum(r[i] * r[j] - 6 for (i, j) in PAIRS)
    return rhs


def main(out_path):
    perword = {k: k - k * (k - 1) // 2 for k in range(5)}
    report = {'per_word_k_minus_choose2': perword, 'max_per_word': max(perword.values()), 'profiles': {}}
    for r in itertools.product((1, 2, 3), repeat=4):
        if any(r[i] * r[j] < 6 for (i, j) in PAIRS):
            continue
        res = feasible(r)
        feas = bool(res and res[0])
        report['profiles'][','.join(map(str, r))] = {
            'identity1_rhs': identity_one(r),
            'identity1_rhs_exceeds_30': identity_one(r) > 30,
            'pattern_system_feasible': feas,
            'witness': ({'+'.join(map(str, sorted(S))) or 'empty': v for S, v in res[1].items() if v} if feas else None),
        }
    report['summary'] = {
        'profiles_tested': list(report['profiles']),
        'infeasible_profiles': [k for k, v in report['profiles'].items() if not v['pattern_system_feasible']],
        'feasible_profiles': [k for k, v in report['profiles'].items() if v['pattern_system_feasible']],
    }
    with Path(out_path).open('x', encoding='utf-8') as fh:
        json.dump(report, fh, indent=1); fh.write('\n')
    print(json.dumps(report['summary']))
    for k, v in report['profiles'].items():
        print(k, 'rhs(1)=', v['identity1_rhs'], 'feasible=', v['pattern_system_feasible'], 'witness=', v['witness'])


if __name__ == '__main__':
    main(sys.argv[1])
