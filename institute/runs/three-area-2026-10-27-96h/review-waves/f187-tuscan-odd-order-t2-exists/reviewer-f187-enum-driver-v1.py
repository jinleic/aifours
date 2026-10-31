#!/usr/bin/env python3
"""Reviewer f187 small-order T2 enumeration driver (ReviewF187TuscanOdd21).

Independently authored reviewer code; no author code is imported or executed.
1. Runs the reviewer C enumerator reviewer-f187-t2enum-v1 (cell-level DFS) for
   n = 3..8 with an internal cap, parses every printed normalized solution.
2. Re-verifies every printed solution with a separate Python checker and
   recomputes its boundary profile (must equal the C profile key).
3. Runs a structurally different Python enumerator (row-level, bitset forward
   checking, MRV row choice) for n = 3..8 and compares solution SETS.
4. Positive controls: multiplicative Vatican squares of orders 4 and 6 (p = 5, 7)
   must appear after normalization; negative control: n = 3 has no T1 square
   (hand proof in review-v1.md), so both enumerators must return 0.
5. Orbit closure: renormalizing any solution from any row (and its row-reversal)
   must stay inside the solution set.
6. Compares recomputable fields of the author profiles JSON (DATA only) with
   the reviewer's profiles; B_eq_M is not recomputable (B undefined).
Usage: reviewer-f187-enum-driver-v1.py RECEIPT_OUT.json   (exclusive create)
"""
import hashlib
import itertools
import json
import subprocess
import sys
import time
from collections import Counter

WAVE = ('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/'
        'review-waves/f187-tuscan-odd-order-t2-exists/')
BASE = ('/Users/jinleic/repos/aifours/information-science/evidence/'
        'three-area-20261027-96h/parallel-18/tuscan2-11/')
BIN = WAVE + 'reviewer-f187-t2enum-v1'
SRC = WAVE + 'reviewer-f187-t2enum-v1.c'
PROFILES = (BASE + 'frontier-20261029-small-and-odd-t2-profiles-v1.json',
            '2d78d16d047f415fe4c50902a7a6e1c1e1fe9df7460203eced192082be011316')
ROWS21 = (BASE + 'frontier-20261029-ollis-g21-t2-square-v1.json',
          '4f20ab9ae5c125bf13cdcc9b847d2ee040dac6e29ac9e14a32c5bfd158fb7c3c')
ORDERS = [3, 4, 5, 6, 7, 8]
C_CAP_SECONDS = 20
PY_CAP_SECONDS = 40

out = {'mismatches': []}


def expect(label, observed, expected):
    ok = observed == expected
    out[label] = {'observed': observed, 'expected': expected, 'ok': ok}
    if not ok:
        out['mismatches'].append(label)


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


# ------------------------------------------------------------ python checker
def is_t2(rows):
    n = len(rows)
    if any(sorted(r) != list(range(n)) for r in rows):
        return False
    for m in (1, 2):
        seen = set()
        for r in rows:
            for i in range(n - m):
                p = (r[i], r[i + m])
                if p in seen:
                    return False
                seen.add(p)
    return True


def parity(p):
    n, seen, s = len(p), [False] * len(p), 1
    for i in range(n):
        if not seen[i]:
            j, ln = i, 0
            while not seen[j]:
                seen[j], j, ln = True, p[j], ln + 1
            if ln % 2 == 0:
                s = -s
    return s


def profile(rows):
    n = len(rows)
    E = {r[0]: r[-1] for r in rows}
    seen, cyc = set(), []
    for a in range(n):
        if a not in seen:
            b, ln = a, 0
            while b not in seen:
                seen.add(b)
                b, ln = E[b], ln + 1
            cyc.append(ln)
    cyc.sort(reverse=True)
    perm = lambda col: sorted(col) == list(range(n))
    d2 = {(r[i], r[i + 2]) for r in rows for i in range(n - 2)}
    M = {(a, b) for a in range(n) for b in range(n) if a != b} - d2
    C = {(r[-1], r[0]) for r in rows}
    R = {(r[-2], r[1]) for r in rows}
    signs = Counter(parity(r) for r in rows)
    return {'E_cycle_type': cyc, 'E_fixed': sum(E[a] == a for a in range(n)),
            'E2id': all(E[E[a]] == a for a in range(n)),
            'latin': all(perm([r[j] for r in rows]) for j in range(n)),
            'second_col_perm': perm([r[1] for r in rows]),
            'penult_col_perm': perm([r[-2] for r in rows]),
            'closing_pairs_eq_M': C == M, 'M_eq_R': M == R,
            'row_sign_classes': sorted(signs.values(), reverse=True)}


def c_key(p):
    return ('E=%s|Efixed=%d|E2id=%d|latin=%d|secondperm=%d|penultperm=%d|CeqM=%d|MeqR=%d|signclasses=%s'
            % (','.join(map(str, p['E_cycle_type'])), p['E_fixed'], p['E2id'], p['latin'],
               p['second_col_perm'], p['penult_col_perm'], p['closing_pairs_eq_M'], p['M_eq_R'],
               ','.join(map(str, p['row_sign_classes']))))


def normalize_from(rows, k):
    """Relabel so that row k becomes identity, then order rows by first symbol."""
    lab = {s: i for i, s in enumerate(rows[k])}
    new = [[lab[s] for s in r] for r in rows]
    new.sort(key=lambda r: r[0])
    return tuple(tuple(r) for r in new)


def is_normalized(rows):
    n = len(rows)
    return list(rows[0]) == list(range(n)) and [r[0] for r in rows] == list(range(n))


# ------------------------------------------------- python row-level enumerator
def py_enum(n, cap):
    t0 = time.time()
    nn = n * n

    def pairs(perm):
        return ([perm[i] * n + perm[i + 1] for i in range(n - 1)] +
                [nn + perm[i] * n + perm[i + 2] for i in range(n - 2)])
    cands = {r: [] for r in range(1, n)}
    for perm in itertools.permutations(range(n)):
        if perm[0] != 0:
            cands[perm[0]].append(perm)
    contain = {r: [0] * (2 * nn) for r in cands}
    lastis = {r: [0] * n for r in cands}
    for r, lst in cands.items():
        for idx, perm in enumerate(lst):
            bit = 1 << idx
            for p in pairs(perm):
                contain[r][p] |= bit
            lastis[r][perm[-1]] |= bit
    row0 = tuple(range(n))
    compat = {}
    for r, lst in cands.items():
        x = (1 << len(lst)) - 1
        for p in pairs(row0):
            x &= ~contain[r][p]
        compat[r] = x & ~lastis[r][n - 1]
    sols, stats = [], {'nodes': 0, 'capped': False}

    def rec(assign, comp):
        if stats['capped']:
            return
        if not comp:
            sols.append(tuple([row0] + [assign[r] for r in range(1, n)]))
            return
        if time.time() - t0 > cap:
            stats['capped'] = True
            return
        r = min(comp, key=lambda q: comp[q].bit_count())
        x = comp[r]
        while x:
            low = x & -x
            x ^= low
            perm = cands[r][low.bit_length() - 1]
            stats['nodes'] += 1
            new, ok = {}, True
            ps = pairs(perm)
            for q, y in comp.items():
                if q == r:
                    continue
                for p in ps:
                    y &= ~contain[q][p]
                y &= ~lastis[q][perm[-1]]
                if not y:
                    ok = False
                    break
                new[q] = y
            if ok:
                assign[r] = perm
                rec(assign, new)
                del assign[r]
    rec({}, compat)
    return sols, stats['capped'], stats['nodes'], round(time.time() - t0, 3)


def main(argv):
    if len(argv) != 2:
        raise SystemExit('usage: reviewer-f187-enum-driver-v1.py RECEIPT_OUT.json')
    t_start = time.time()
    out['driver_sha256'] = sha(__file__)
    out['c_source_sha256'] = sha(SRC)
    out['c_binary_sha256'] = sha(BIN)
    expect('profiles_json_sha256', sha(PROFILES[0]), PROFILES[1])
    expect('rows21_json_sha256', sha(ROWS21[0]), ROWS21[1])
    pj = json.loads(open(PROFILES[0], 'rb').read())['profiles']
    rows21 = json.loads(open(ROWS21[0], 'rb').read())['rows']

    c_sols, c_runs = {}, {}
    for n in ORDERS:
        t = time.time()
        cp = subprocess.run([BIN, str(n), str(C_CAP_SECONDS), '1000000'], capture_output=True,
                            text=True, timeout=C_CAP_SECONDS + 10)
        lines = cp.stdout.splitlines()
        sol_lines = [ln for ln in lines if ln.startswith('SOL ')]
        summary = [ln for ln in lines if ln.startswith('SUMMARY ')]
        c_runs[n] = {'exit': cp.returncode, 'wall_seconds': round(time.time() - t, 3),
                     'summary': summary, 'profiles': [ln for ln in lines if ln.startswith('PROFILE ')],
                     'stdout_sha256': hashlib.sha256(cp.stdout.encode()).hexdigest(),
                     'stderr': cp.stderr}
        sols, keys_ok, t2_ok, norm_ok = [], 0, 0, 0
        for ln in sol_lines:
            _, flat, key = ln.split(' ')
            vals = list(map(int, flat.split(',')))
            rows = [vals[i * n:(i + 1) * n] for i in range(n)]
            sols.append(tuple(tuple(r) for r in rows))
            t2_ok += is_t2(rows)
            norm_ok += is_normalized(rows)
            keys_ok += (c_key(profile(rows)) == key)
        c_sols[n] = sols
        expect('c_run_n%d_complete_exit0' % n, cp.returncode, 0)
        expect('c_run_n%d_printed_all_solutions' % n,
               len(sols), int(summary[0].split('normalized_T2_solutions=')[1].split()[0]))
        expect('c_run_n%d_solutions_verified_T2_normalized_keymatch' % n,
               [t2_ok, norm_ok, keys_ok], [len(sols)] * 3)
        expect('c_run_n%d_distinct_solutions' % n, len(set(sols)), len(sols))

    out['c_runs'] = c_runs
    out['c_solution_counts'] = {n: len(c_sols[n]) for n in ORDERS}

    py_res = {}
    for n in ORDERS:
        sols, capped, nodes, el = py_enum(n, PY_CAP_SECONDS)
        py_res[n] = {'count': len(sols), 'capped': capped, 'nodes': nodes, 'seconds': el}
        expect('py_enum_n%d_not_capped' % n, capped, False)
        expect('py_enum_n%d_same_solution_set_as_C' % n, sorted(sols) == sorted(c_sols[n]), True)
        expect('py_enum_n%d_all_T2' % n, all(is_t2([list(r) for r in s]) for s in sols), True)
    out['py_enum'] = py_res
    expect('negative_control_n3_zero_solutions', [len(c_sols[3]), py_res[3]['count']], [0, 0])

    for p, n in ((5, 4), (7, 6)):
        vat = [[(i * j) % p - 1 for j in range(1, p)] for i in range(1, p)]
        expect('positive_control_vatican_order_%d_found' % n,
               [is_t2(vat), normalize_from(vat, 0) in set(c_sols[n])], [True, True])

    closure = {}
    for n in (4, 6, 8):
        S = set(c_sols[n])
        imgs = set()
        for s in S:
            rows = [list(r) for r in s]
            rev = [r[::-1] for r in rows]
            for k in range(n):
                imgs.add(normalize_from(rows, k))
                imgs.add(normalize_from(rev, k))
        closure[n] = imgs <= S
        expect('orbit_closure_n%d' % n, imgs <= S, True)

    profs = {n: [profile([list(r) for r in s]) for s in c_sols[n]] for n in (4, 6, 8)}
    out['reviewer_profiles'] = profs
    fields = ['E_cycle_type', 'second_col_perm', 'penult_col_perm', 'closing_pairs_eq_M', 'M_eq_R',
              'row_sign_classes']
    for n, key in ((4, 'n4'), (6, 'n6')):
        expect('profiles_json_%s_vs_unique_reviewer_T2(%d)' % (key, n),
               [{f: pr[f] for f in fields} for pr in profs[n]], [{f: pj[key][f] for f in fields}])
    mine8 = sorted(json.dumps({f: pr[f] for f in fields}, sort_keys=True) for pr in profs[8])
    theirs8 = sorted(json.dumps({f: pj['n8_%d' % i][f] for f in fields}, sort_keys=True)
                     for i in range(6))
    expect('profiles_json_n8_multiset_vs_reviewer_enumeration', mine8, theirs8)
    p21 = profile(rows21)
    expect('profiles_json_n21_vs_reviewer', {f: p21[f] for f in fields},
           {f: pj['n21_G21'][f] for f in fields})
    out['B_eq_M_values_in_json_not_recomputable'] = {k: v['B_eq_M'] for k, v in pj.items()}

    # e_dist: undefined field; try simple reviewer hypotheses (informational only)
    def hyps(rows):
        n = len(rows)
        E = {r[0]: r[-1] for r in rows}
        Einv = {v: k for k, v in E.items()}
        start = {r[0]: r for r in rows}
        end = {r[-1]: r for r in rows}
        d1 = {}
        d2 = {}
        for r in rows:
            for i in range(n - 1):
                d1[(r[i], r[i + 1])] = i
            for i in range(n - 2):
                d2[(r[i], r[i + 2])] = i
        H = {}
        for nm, f in [('col0_of_a_in_row_starting_E(a)', lambda a: start[E[a]].index(a)),
                      ('col0_of_E(a)_in_row_ending_a', lambda a: end[a].index(E[a])),
                      ('col0_of_Einv(a)_in_row_starting_a', lambda a: start[a].index(Einv[a])),
                      ('col0_of_D1_pair_(a,E(a))', lambda a: d1[(a, E[a])]),
                      ('col0_of_D1_pair_(E(a),a)', lambda a: d1[(E[a], a)]),
                      ('col0_of_D2_pair_(a,E(a))_or_-1', lambda a: d2.get((a, E[a]), -1)),
                      ('col0_in_row_starting_E(a)_of_second_symbol_of_row_starting_a',
                       lambda a: start[E[a]].index(start[a][1]))]:
            for shift in (0, 1):
                H['%s+%d' % (nm, shift)] = dict(Counter(str(f(a) + shift) for a in range(n)))
        return H
    hy = {'n4': hyps([list(r) for r in c_sols[4][0]]), 'n6': hyps([list(r) for r in c_sols[6][0]]),
          'n21': hyps(rows21), 'n8': [hyps([list(r) for r in s]) for s in c_sols[8]]}
    match = []
    for h in hy['n4']:
        ok = (hy['n4'][h] == pj['n4']['e_dist'] and hy['n6'][h] == pj['n6']['e_dist'] and
              hy['n21'][h] == pj['n21_G21']['e_dist'] and
              sorted(json.dumps(x[h], sort_keys=True) for x in hy['n8']) ==
              sorted(json.dumps(pj['n8_%d' % i]['e_dist'], sort_keys=True) for i in range(6)))
        if ok:
            match.append(h)
    out['e_dist_hypotheses_matching_all_json_values'] = match
    out['e_dist_hypotheses_values'] = hy

    out['elapsed_seconds'] = round(time.time() - t_start, 3)
    with open(argv[1], 'x', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
        fh.write('\n')
    print(json.dumps({'mismatches': out['mismatches'], 'c_solution_counts': out['c_solution_counts'],
                      'py_enum': py_res, 'e_dist_match': match,
                      'elapsed_seconds': out['elapsed_seconds'], 'driver_sha256': out['driver_sha256']}))
    return 1 if out['mismatches'] else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
