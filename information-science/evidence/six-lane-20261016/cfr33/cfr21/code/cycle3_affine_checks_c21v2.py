#!/usr/bin/env python3
"""Stand-alone controls for cycle3_pair_c21v2 (CFR21 lane, InfoCFR27Lift). Pure Python, no subprocesses.

Normal form (unchanged from v1): rows 0, t, mu*h^2, mu^2*h, g, mu*g(h^2), mu^2*g(h) over Z_n, h^3=id, mu^3=1,
generator s=(mu,(1 2 3)(4 5 6)) with row0 fixed. Modes: fixed (h(0)=g(0)=0) and free (h without fixed points).

Part A, random algebra (no search). For random order-3 permutations h and random arrays g (half of them
permutations), every unit u and every eligible shift a (fixed: h(a)=a, free: every a), and b=g(a):
    h'(x)=u*(h(u^-1*x+a)-a),   g'(x)=u*(g(u^-1*x+a)-b)   (mod n).
The seven rows rebuilt from (h',g') are compared entry by entry with the explicit transform of the original rows:
column x reads original column t=u^-1*x+a, row r is translated by -(0,a,mu*a,mu^2*a,b,mu*b,mu^2*b)[r], then
scaled by u. Also asserted: g'(0)=0, h' is a permutation with h'^3=id, Fix(h')={u*(f-a): f in Fix(h)}, fixed
mode keeps h'(0)=0 while every ineligible shift breaks it, free mode stays fixed-point free, the shift vector is
fixed by s, and both column sets are s-invariant (s maps column t to column h(t)). Four deliberately wrong
formulas (shift sign, b+1, no unit scaling, mu/mu^2 swapped in the shift vector) must be caught by the same
entrywise comparison. Cases: n21 with every mu^3=1 (mu4 is the g06 target), prime analogues n7,13,19,31
(fixed mode only: a free order-3 permutation needs 3|n) and n3,9,15,27 (both modes).

Part B, independent h counts and affine classes. n7 and n9 (every mu^3=1, both modes): itertools.permutations
over all of Z_n keeps h^3=id and the mode condition, then direct-checks all six row pairs of [0,t,mu*h^2,mu^2*h]
(compared with the single-map criterion t-mu*h^2(t) bijective). These sets are tiny (n9 is expected empty: a
4-row DM over Z_9 is known not to exist), so n13 fixed mode (every mu^3=1) is added via an exhaustive recursive
cycle construction pruned only by repeated row1-row2 differences (a necessary condition) with every leaf
direct-checked on all six top pairs; at n7/n9 the recursion must reproduce the permutation sets exactly.
Affine classes are AGL(1,n)-conjugacy orbits intersected with the mode's set, counted by orbit marking; the
C-style eligible-shift lexicographic test must select exactly the class minima, eligible conjugates must stay in
the set and (fixed mode) ineligible ones must leave it.
g level, n7/n9 only: pointwise backtracking checks all 21 row pairs directly, for the v1 model (fixed: g(0)=0;
free: any g(0)) and the v2 model (class-minimal h and g(0)=0, also searched directly). Every v1 solution must
map, by every eligible (u,a) reaching its class minimum and b=g(a), into the v2 solutions.

Part C, v1 positives (--v1-calib DIR, default ../calib/cycle3-v1 beside this script; skipped if absent). Each
existing nN-muMU-fixed.dmraw of a Part B case must be a DM in the exact v1 normal form; every eligible (u,a)
reaching its class minimum (b=g(a)) must give a DM with that minimal h and g(0)=0. Where Part B has no g level
(n13) a mapped positive sets the expected v2 first-mode status to SATISFIABLE.

Part D, optional --logdir DIR with cycle3_pair_c21v2 stdout files hcount-N-MU-MODE.out and first-N-MU-MODE.out
(MODE fixed|free) for Part B cases. hcount and hcanonical in the final line must equal the independent total and
class counts, with 's HCOUNT COMPLETE'. A first-mode SATISFIABLE must print v h/v g with h in the mode's set,
class-minimal, g(0)=0, all 21 pairs a DM (and in the brute v2 set at n7/n9); the status must match any Part B/C
expectation (no expectation: recorded only). hcount-21-4-fixed.out/hcount-21-4-free.out are compared with the v1
totals 468198/841428 (runs/cycle3-v1/outputs/n21-mu4-*-hcount.out); their hcanonical is only bounded,
ceil(hcount/(phi(n)*n)) <= hcanonical <= hcount. With --logdir at least one log must be compared.

Usage: cycle3_affine_checks_c21v2.py [--seed S] [--trials T] [--v1-calib DIR] [--logdir DIR] [--out-json NEW.json]
Prints 'CYCLE3 AFFINE CHECKS PASS' and exits 0 only if every check passes; otherwise FAIL and exit 1.
--out-json is created exclusively (mode x) with all counts, failures (first 200) and input SHA256s.
"""
import argparse
import hashlib
import itertools
import json
from math import gcd
import os
from pathlib import Path
import random
import re
import sys

PI = (0, 2, 3, 1, 5, 6, 4)  # s sends row i to row PI[i]: row0 fixed, (1 2 3)(4 5 6)
PAIRS = [(i, j) for i in range(7) for j in range(i)]
EARLY_PAIRS = [(i, j) for i in range(5) for j in range(i)]  # rows 0..4 of column t need only g(t)
LATE_PAIRS = [(i, j) for i in (5, 6) for j in range(i)]  # rows 5,6 need g on the whole h-orbit of t
A_NS = (21, 7, 13, 19, 31, 3, 9, 15, 27)
B_PERMUTE_NS = (7, 9)  # itertools.permutations, recursion cross-check and g level
B_RECURSE_NS = (13,)  # recursion only, h level only
V1_TOTALS = {(21, 4, 'fixed'): 468198, (21, 4, 'free'): 841428}
HEADER = 'c cycle3_pair_c21v2 n %d mu %d %s %s limit '
FINAL_RE = re.compile(r'^c final [0-9.]+ hcount (\d+) hcanonical (\d+) hnodes \d+ gnodes \d+ '
                      r'timed_out (\d+) signal (\d+)$')
HCOUNT_DONE = 's HCOUNT COMPLETE (not a seven-row DM conclusion)'
SAT = 's SATISFIABLE'
EXHAUSTED = 's EXHAUSTED-RESTRICTED (this exact row-cycling model only)'
MAX_RECORDED_FAILURES = 200


class Recorder:
    def __init__(self):
        self.count = 0
        self.failures = []

    def check(self, cond, msg):
        if not cond:
            self.count += 1
            if len(self.failures) < MAX_RECORDED_FAILURES:
                self.failures.append(msg)
        return bool(cond)


def mus_of(n):
    return [m for m in range(1, n) if pow(m, 3, n) == 1]


def units_of(n):
    return [(u, pow(u, -1, n)) for u in range(1, n) if gcd(u, n) == 1]


def rows_of(n, mu, h, g):
    m2 = mu * mu % n
    return [[0] * n,
            list(range(n)),
            [mu * h[h[t]] % n for t in range(n)],
            [m2 * h[t] % n for t in range(n)],
            [g[t] % n for t in range(n)],
            [mu * g[h[h[t]]] % n for t in range(n)],
            [m2 * g[h[t]] % n for t in range(n)]]


def s_image(n, mu, col):
    img = [0] * 7
    for i in range(7):
        img[PI[i]] = mu * col[i] % n
    return img


def s_invariant(n, mu, rows, h):
    cols = [[rows[r][t] for r in range(7)] for t in range(n)]
    if any(s_image(n, mu, cols[t]) != cols[h[t]] for t in range(n)):
        return False
    return {tuple(s_image(n, mu, c)) for c in cols} == {tuple(c) for c in cols}


def conj(n, h, u, ui, a):
    return tuple(u * (h[(ui * x + a) % n] - a) % n for x in range(n))


def regauge(n, g, u, ui, a, b):
    return tuple(u * (g[(ui * x + a) % n] - b) % n for x in range(n))


def shift_vector(n, mu, a, b, swap_mu=False):
    m1, m2 = mu % n, mu * mu % n
    if swap_mu:
        m1, m2 = m2, m1
    return [0, a % n, m1 * a % n, m2 * a % n, b % n, m1 * b % n, m2 * b % n]


def explicit_transform(n, rows, u, ui, a, vec):
    return [[u * (rows[r][(ui * x + a) % n] - vec[r]) % n for x in range(n)] for r in range(7)]


def is_dm(n, rows):
    return all(len({(rows[i][t] - rows[j][t]) % n for t in range(n)}) == n for (i, j) in PAIRS)


def top_is_dm(n, mu, h):
    top = rows_of(n, mu, h, [0] * n)[:4]
    return all(len({(top[i][t] - top[j][t]) % n for t in range(n)}) == n for i in range(4) for j in range(i))


def fixed_points(h):
    return {t for t in range(len(h)) if h[t] == t}


def is_order3_perm(n, h):
    return sorted(h) == list(range(n)) and all(h[h[h[t]]] == t for t in range(n))


def random_order3(rng, n, mode):
    if mode == 'free':
        rest = list(range(n))
    else:
        nfix = rng.choice([f for f in range(1, n + 1) if (n - f) % 3 == 0])
        rest = list(range(1, n))
        rng.shuffle(rest)
        rest = rest[nfix - 1:]
    rng.shuffle(rest)
    h = list(range(n))
    for i in range(0, len(rest), 3):
        a, b, c = rest[i:i + 3]
        h[a], h[b], h[c] = b, c, a
    return tuple(h)


def random_g(rng, n, mode, as_permutation):
    if as_permutation:
        g = list(range(n))
        rng.shuffle(g)
        if mode == 'fixed':
            j = g.index(0)
            g[0], g[j] = g[j], g[0]
    else:
        g = [rng.randrange(n) for _ in range(n)]
        if mode == 'fixed':
            g[0] = 0
    return tuple(g)


def part_a(rec, rng, trials):
    cases = [(n, mu, mode) for n in A_NS for mu in mus_of(n) for mode in ('fixed', 'free')
             if mode == 'fixed' or n % 3 == 0]
    rec.check((21, 4, 'fixed') in cases and (21, 4, 'free') in cases, 'A: target n21 mu4 cases missing')
    hits = {'shift_sign': 0, 'b_plus_one': 0, 'no_unit_scaling': 0, 'mu_swapped_shift_vector': 0}
    stats = []
    for (n, mu, mode) in cases:
        units = units_of(n)
        st = {'n': n, 'mu': mu, 'mode': mode, 'samples': 0, 'eligible_transforms': 0,
              'entries_compared': 0, 'ineligible_shifts_checked': 0}
        for trial in range(trials):
            tag = 'A n%d mu%d %s trial%d' % (n, mu, mode, trial)
            h = random_order3(rng, n, mode)
            g = random_g(rng, n, mode, trial % 2 == 0)
            fix = fixed_points(h)
            rec.check(is_order3_perm(n, h), tag + ': generated h is not an order-3 permutation')
            if mode == 'fixed':
                rec.check(h[0] == 0 and g[0] == 0, tag + ': fixed-mode sample lacks h(0)=g(0)=0')
            else:
                rec.check(not fix, tag + ': free-mode sample has a fixed point')
            rows = rows_of(n, mu, h, g)
            rec.check(s_invariant(n, mu, rows, h), tag + ': original columns not s-invariant')
            st['samples'] += 1
            for (u, ui) in units:
                for a in range(n):
                    where = '%s u%d a%d' % (tag, u, a)
                    if mode == 'fixed' and h[a] != a:
                        rec.check(conj(n, h, u, ui, a)[0] != 0, where + ": ineligible shift kept h'(0)=0")
                        st['ineligible_shifts_checked'] += 1
                        continue
                    b = g[a]
                    h2 = conj(n, h, u, ui, a)
                    g2 = regauge(n, g, u, ui, a, b)
                    vec = shift_vector(n, mu, a, b)
                    expl = explicit_transform(n, rows, u, ui, a, vec)
                    rebuilt = rows_of(n, mu, h2, g2)
                    bad = [(r, x) for r in range(7) for x in range(n) if rebuilt[r][x] != expl[r][x]]
                    rec.check(not bad, where + ': rebuilt rows differ from explicit transform at %s' % (bad[:3],))
                    st['eligible_transforms'] += 1
                    st['entries_compared'] += 7 * n
                    rec.check(s_image(n, mu, vec) == vec, where + ': shift vector not fixed by s')
                    rec.check(g2[0] == 0, where + ": g'(0) != 0")
                    rec.check(is_order3_perm(n, h2), where + ": h' is not an order-3 permutation")
                    fix2 = fixed_points(h2)
                    rec.check(fix2 == {u * (f - a) % n for f in fix}, where + ": Fix(h') != u*(Fix(h)-a)")
                    if mode == 'fixed':
                        rec.check(h2[0] == 0, where + ": fixed mode lost h'(0)=0")
                    else:
                        rec.check(not fix2, where + ': free mode gained a fixed point')
                    rec.check(s_invariant(n, mu, rebuilt, h2), where + ': transformed columns not s-invariant')
                    # Mutation controls: the same entrywise comparison must reject wrong formulas.
                    wrong_h = tuple(u * (h[(ui * x - a) % n] + a) % n for x in range(n))
                    wrong_g = tuple(u * (g[(ui * x - a) % n] + b) % n for x in range(n))
                    hits['shift_sign'] += rows_of(n, mu, wrong_h, wrong_g) != expl
                    caught = rows_of(n, mu, h2, regauge(n, g, u, ui, a, b + 1)) != expl
                    rec.check(caught, where + ': b+1 mutation not caught')
                    hits['b_plus_one'] += caught
                    plain_h = tuple((h[(ui * x + a) % n] - a) % n for x in range(n))
                    plain_g = tuple((g[(ui * x + a) % n] - b) % n for x in range(n))
                    hits['no_unit_scaling'] += rows_of(n, mu, plain_h, plain_g) != expl
                    swapped = shift_vector(n, mu, a, b, swap_mu=True)
                    hits['mu_swapped_shift_vector'] += explicit_transform(n, rows, u, ui, a, swapped) != rebuilt
        stats.append(st)
    for name, count in hits.items():
        rec.check(count > 0, 'A: mutation %s was never caught' % name)
    return stats, hits


def hset_by_permutations(rec, tag, n, mu, mode, perms3):
    out = []
    for h in perms3:
        if (mode == 'fixed' and h[0] != 0) or (mode == 'free' and fixed_points(h)):
            continue
        direct = top_is_dm(n, mu, h)
        single = len({(t - mu * h[h[t]]) % n for t in range(n)}) == n
        rec.check(direct == single, '%s: top-pair criterion mismatch for h=%s' % (tag, h))
        if direct:
            out.append(h)
    return out


def hset_by_recursion(rec, tag, n, mu, mode):
    """Every order-3 h (fixed: h(0)=0; free: no fixed point) whose top rows form a DM. The smallest open point is
    made fixed or put in an oriented 3-cycle with two larger open points; branches with a repeated row1-row2
    difference t-mu*h^2(t) are cut (necessary condition); each leaf is checked on all six top pairs."""
    h = [None] * n
    used = set()
    out = []

    def search():
        p = next((t for t in range(n) if h[t] is None), None)
        if p is None:
            leaf = tuple(h)
            if rec.check(top_is_dm(n, mu, leaf), '%s: single-map leaf fails a direct top pair: %s' % (tag, leaf)):
                out.append(leaf)
            return
        if mode == 'fixed':
            d = (1 - mu) * p % n
            if d not in used:
                h[p] = p
                used.add(d)
                search()
                used.discard(d)
                h[p] = None
            if p == 0:
                return
        open_pts = [t for t in range(p + 1, n) if h[t] is None]
        for q in open_pts:
            for r in open_pts:
                if q == r:
                    continue
                # cycle p->q->r->p: h^2(p)=r, h^2(q)=p, h^2(r)=q
                ds = {(p - mu * r) % n, (q - mu * p) % n, (r - mu * q) % n}
                if len(ds) < 3 or ds & used:
                    continue
                h[p], h[q], h[r] = q, r, p
                used.update(ds)
                search()
                used.difference_update(ds)
                h[p] = h[q] = h[r] = None

    search()
    return out


def affine_classes(rec, tag, n, mode, hset, units):
    members = set(hset)
    class_min = {}
    classes = 0
    for h in hset:
        if h in class_min:
            continue
        cls = {conj(n, h, u, ui, a) for (u, ui) in units for a in range(n)} & members
        rec.check(h in cls, tag + ': h missing from its own class')
        low = min(cls | {h})
        for x in cls:
            rec.check(x not in class_min, tag + ': affine classes overlap')
            class_min[x] = low
        class_min.setdefault(h, low)
        classes += 1
    canonical = []
    for h in hset:
        lexmin = True
        for (u, ui) in units:
            for a in range(n):
                c = conj(n, h, u, ui, a)
                if mode == 'fixed' and h[a] != a:
                    rec.check(c not in members, tag + ': ineligible conjugate lies in the fixed-mode set')
                    continue
                rec.check(c in members, tag + ': eligible conjugate leaves the enumerated set')
                if c < h:
                    lexmin = False
        rec.check(lexmin == (class_min[h] == h), tag + ': eligible lex test disagrees with the class minimum')
        if lexmin:
            canonical.append(h)
    rec.check(len(canonical) == classes, tag + ': canonical count differs from class count')
    return members, class_min, classes, canonical


def h_orbits(n, h):
    seen, orbs = set(), []
    for t in range(n):
        if t not in seen:
            orb, x = [t], h[t]
            while x != t:
                orb.append(x)
                x = h[x]
            seen.update(orb)
            orbs.append(orb)
    return orbs


def g_solutions(n, mu, h, zero_g0):
    """Every g with rows_of(h,g) a DM: pointwise backtracking with direct difference sets of all 21 row pairs."""
    m2 = mu * mu % n
    orbs = h_orbits(n, h)
    order = [(t, k, i == len(orb) - 1) for k, orb in enumerate(orbs) for i, t in enumerate(orb)]
    used = {p: set() for p in PAIRS}
    g = [None] * n
    sols = []

    def push(pairs, col, added):
        for (i, j) in pairs:
            d = (col[i] - col[j]) % n
            taken = used[(i, j)]
            if d in taken:
                return False
            taken.add(d)
            added.append((i, j, d))
        return True

    def search(pos):
        if pos == len(order):
            sols.append(tuple(g))
            return
        t, k, closes_orbit = order[pos]
        for v in ((0,) if zero_g0 and t == 0 else range(n)):
            g[t] = v
            added = []
            ok = push(EARLY_PAIRS, (0, t, mu * h[h[t]] % n, m2 * h[t] % n, v), added)
            if ok and closes_orbit:
                for s in orbs[k]:
                    col = (0, s, mu * h[h[s]] % n, m2 * h[s] % n, g[s], mu * g[h[h[s]]] % n, m2 * g[h[s]] % n)
                    if not push(LATE_PAIRS, col, added):
                        ok = False
                        break
            if ok:
                search(pos + 1)
            for (i, j, d) in added:
                used[(i, j)].discard(d)
        g[t] = None

    search(0)
    return sols


def map_to_class_min(rec, tag, n, mu, mode, h, g, units, class_min, v2):
    """Apply every eligible (u,a) sending h to its class minimum, with b=g(a). Each image must be a DM with
    g'(0)=0 (and lie in v2 when the brute v2 set is known). Returns the number of such maps."""
    low = class_min[h]
    reached = 0
    for (u, ui) in units:
        for a in range(n):
            if (mode == 'fixed' and h[a] != a) or conj(n, h, u, ui, a) != low:
                continue
            reached += 1
            g2 = regauge(n, g, u, ui, a, g[a])
            rec.check(g2[0] == 0 and is_dm(n, rows_of(n, mu, low, g2)),
                      tag + ': mapped solution is not a DM with g(0)=0')
            if v2 is not None:
                rec.check((low, g2) in v2, tag + ': mapped solution is not in the v2 model')
    return reached


def g_level(rec, tag, n, mu, mode, hset, units, class_min, canonical):
    v1 = []
    for h in hset:
        for g in g_solutions(n, mu, h, mode == 'fixed'):
            rec.check(is_dm(n, rows_of(n, mu, h, g)), tag + ': backtracking returned a non-DM')
            v1.append((h, g))
    v2 = {(h, g) for (h, g) in v1 if class_min[h] == h and g[0] == 0}
    v2_direct = {(h, g) for h in canonical for g in g_solutions(n, mu, h, True)}
    rec.check(v2_direct == v2, tag + ': direct v2 search differs from the filtered v1 solutions')
    for (h, g) in v1:
        rec.check(map_to_class_min(rec, tag, n, mu, mode, h, g, units, class_min, v2) > 0,
                  tag + ': no eligible map reaches the class minimum')
    rec.check(bool(v1) == bool(v2), tag + ': v1 and v2 existence differ')
    return v1, v2


def brute_case(rec, n, mu, mode, units, perms3):
    tag = 'B n%d mu%d %s' % (n, mu, mode)
    recursive = hset_by_recursion(rec, tag, n, mu, mode)
    if perms3 is not None:
        hset = hset_by_permutations(rec, tag, n, mu, mode, perms3)
        rec.check(set(recursive) == set(hset) and len(recursive) == len(hset),
                  tag + ': recursive and permutation enumerations differ')
    else:
        hset = recursive
    members, class_min, classes, canonical = affine_classes(rec, tag, n, mode, hset, units)
    record = {'n': n, 'mu': mu, 'mode': mode,
              'h_enumeration': 'itertools.permutations + recursion' if perms3 is not None else 'recursion',
              'total_h': len(hset), 'affine_classes': classes, 'eligible_lexmin_h': len(canonical),
              'class_minima': [list(h) for h in sorted(canonical)] if len(canonical) <= 64 else None,
              'v1_model_solutions': None, 'v2_model_solutions': None,
              'expected_first_status': None, 'expected_first_source': None}
    v2 = None
    if perms3 is not None:
        v1, v2 = g_level(rec, tag, n, mu, mode, hset, units, class_min, canonical)
        record.update(v1_model_solutions=len(v1), v2_model_solutions=len(v2),
                      expected_first_status='SATISFIABLE' if v2 else 'EXHAUSTED-RESTRICTED',
                      expected_first_source='brute-force g level')
    return {'record': record, 'v2': v2, 'members': members, 'class_min': class_min}


def part_b(rec):
    cases = []
    for n in B_PERMUTE_NS:
        perms3 = [p for p in itertools.permutations(range(n)) if all(p[p[p[x]]] == x for x in range(n))]
        cases += [(n, mu, mode, perms3) for mu in mus_of(n) for mode in ('fixed', 'free')]
    for n in B_RECURSE_NS:
        cases += [(n, mu, mode, None) for mu in mus_of(n) for mode in ('fixed', 'free')
                  if mode == 'fixed' or n % 3 == 0]
    records, index = [], {}
    for (n, mu, mode, perms3) in cases:
        entry = brute_case(rec, n, mu, mode, units_of(n), perms3)
        records.append(entry['record'])
        index[(n, mu, mode)] = entry
    return records, index


def part_c(rec, calib, index):
    out = []
    for key in sorted(index):
        n, mu, mode = key
        path = calib / ('n%d-mu%d-fixed.dmraw' % (n, mu))
        if mode != 'fixed' or not path.is_file():
            continue
        entry = index[key]
        record = entry['record']
        data = path.read_bytes()
        tag = 'C %s' % path.name
        ent = {'dmraw': str(path), 'sha256': hashlib.sha256(data).hexdigest(), 'n': n, 'mu': mu, 'mode': mode}
        try:
            dm = [[int(x) for x in line.split()] for line in data.decode().splitlines() if line.strip()]
        except ValueError:
            dm = []
        ok = rec.check(len(dm) == 7 and all(len(row) == n and all(0 <= x < n for x in row) for row in dm),
                       tag + ': not a 7 x n matrix over Z_n')
        if ok:
            h = tuple(mu * dm[3][t] % n for t in range(n))
            g = tuple(dm[4])
            ok = rec.check(is_dm(n, dm), tag + ': v1 positive is not a DM') and ok
            ok = rec.check(rows_of(n, mu, h, g) == dm, tag + ': v1 positive is not in the v1 normal form') and ok
            ok = rec.check(h in entry['members'] and g[0] == 0, tag + ': v1 positive outside the fixed-mode model') and ok
            if ok:
                maps = map_to_class_min(rec, tag, n, mu, mode, h, g, units_of(n), entry['class_min'], entry['v2'])
                ok = rec.check(maps > 0, tag + ': no eligible map reaches the class minimum') and ok
                ent.update(h=list(h), class_min=list(entry['class_min'][h]), eligible_maps_to_min=maps)
        if ok:
            if record['expected_first_status'] is None:
                record.update(expected_first_status='SATISFIABLE',
                              expected_first_source='v1 positive %s mapped into the v2 model' % path.name)
            else:
                ok = rec.check(record['expected_first_status'] == 'SATISFIABLE',
                               tag + ': brute force has no v2 solution although a v1 positive exists') and ok
        ent['as_expected'] = ok
        out.append(ent)
    return out


def read_lines(path):
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest(), data.decode('utf-8', 'replace').splitlines()


def last_final(lines):
    found = None
    for line in lines:
        m = FINAL_RE.match(line)
        if m:
            found = m
    return found


def check_hcount_log(rec, path, key, entry):
    n, mu, mode = key
    sha, lines = read_lines(path)
    tag = 'D %s' % path.name
    ent = {'log': str(path), 'sha256': sha, 'kind': 'hcount', 'n': n, 'mu': mu, 'mode': mode}
    ok = rec.check(bool(lines) and lines[0].startswith(HEADER % (n, mu, mode, 'hcount')), tag + ': header mismatch')
    ok = rec.check(HCOUNT_DONE in lines, tag + ': no complete hcount status line') and ok
    m = last_final(lines)
    ok = rec.check(m is not None, tag + ': no parsable final line') and ok
    if m is not None:
        total, canon, tout, sig = (int(v) for v in m.groups())
        ent.update(hcount=total, hcanonical=canon, timed_out=tout, signal=sig)
        ok = rec.check(tout == 0 and sig == 0, tag + ': timed out or signalled') and ok
        if entry is not None:
            record = entry['record']
            ent.update(expected_hcount=record['total_h'], expected_hcanonical=record['affine_classes'])
            ok = rec.check(total == record['total_h'], tag + ': hcount differs from the independent count') and ok
            ok = rec.check(canon == record['affine_classes'], tag + ': hcanonical differs from the class count') and ok
        else:
            bound = -(-total // (len(units_of(n)) * n))
            ent.update(expected_hcount_v1=V1_TOTALS[key], hcanonical_lower_bound=bound)
            ok = rec.check(total == V1_TOTALS[key], tag + ': hcount differs from the v1 total') and ok
            ok = rec.check(bound <= canon <= total, tag + ': hcanonical outside [ceil(hcount/|AGL|), hcount]') and ok
    ent['as_expected'] = ok
    return ent


def check_candidate(rec, tag, n, mu, entry, lines):
    vh = [line for line in lines if line.startswith('v h ')]
    vg = [line for line in lines if line.startswith('v g ')]
    if not rec.check(len(vh) == 1 and len(vg) == 1, tag + ': expected exactly one v h and one v g line'):
        return False
    try:
        h = tuple(int(x) for x in vh[0].split()[2:])
        g = tuple(int(x) for x in vg[0].split()[2:])
    except ValueError:
        return rec.check(False, tag + ': unparsable v line')
    if not rec.check(len(h) == n and len(g) == n and all(0 <= x < n for x in h + g), tag + ': bad v line values'):
        return False
    ok = rec.check(h in entry['members'], tag + ': printed h is outside the mode h set')
    ok = rec.check(entry['class_min'].get(h) == h, tag + ': printed h is not its affine class minimum') and ok
    ok = rec.check(g[0] == 0, tag + ': printed g(0) != 0') and ok
    ok = rec.check(is_dm(n, rows_of(n, mu, h, g)), tag + ': printed (h,g) is not a DM') and ok
    if entry['v2'] is not None:
        ok = rec.check((h, g) in entry['v2'], tag + ': printed (h,g) is not in the brute v2 set') and ok
    return ok


def check_first_log(rec, path, key, entry):
    n, mu, mode = key
    record = entry['record']
    expected = record['expected_first_status']
    sha, lines = read_lines(path)
    tag = 'D %s' % path.name
    ent = {'log': str(path), 'sha256': sha, 'kind': 'first', 'n': n, 'mu': mu, 'mode': mode,
           'expected_status': expected, 'expected_source': record['expected_first_source']}
    ok = rec.check(bool(lines) and lines[0].startswith(HEADER % (n, mu, mode, 'first')), tag + ': header mismatch')
    status = [line for line in lines if line.startswith('s ')]
    ent['status'] = status[-1] if status else None
    if ent['status'] == SAT:
        ok = check_candidate(rec, tag, n, mu, entry, lines) and ok
        if expected is not None:
            ok = rec.check(expected == 'SATISFIABLE', tag + ': SATISFIABLE but no v2 solution was expected') and ok
    elif ent['status'] == EXHAUSTED:
        if expected is not None:
            ok = rec.check(expected == 'EXHAUSTED-RESTRICTED', tag + ': exhausted although a v2 solution exists') and ok
        else:
            ent['note'] = 'no independent expectation; status recorded only'
    else:
        ok = rec.check(False, tag + ': no conclusive status line') and ok
    ent['as_expected'] = ok
    return ent


def part_d(rec, logdir, index):
    out = []
    for key in sorted(set(index) | set(V1_TOTALS)):
        path = logdir / ('hcount-%d-%d-%s.out' % key)
        if path.is_file():
            out.append(check_hcount_log(rec, path, key, index.get(key)))
        path = logdir / ('first-%d-%d-%s.out' % key)
        if key in index and path.is_file():
            out.append(check_first_log(rec, path, key, index[key]))
    rec.check(bool(out), 'D: --logdir given but no hcount-/first- log of a known case was found')
    return out


def main():
    default_calib = Path(__file__).resolve().parent.parent / 'calib' / 'cycle3-v1'
    ap = argparse.ArgumentParser(description='Controls for cycle3_pair_c21v2; see the module docstring.')
    ap.add_argument('--seed', type=int, default=21062)
    ap.add_argument('--trials', type=int, default=8, help='random (h,g) samples per Part A case')
    ap.add_argument('--v1-calib', default=str(default_calib), help='directory with v1 nN-muMU-fixed.dmraw positives')
    ap.add_argument('--logdir', help='directory with cycle3_pair_c21v2 stdout files (optional)')
    ap.add_argument('--out-json', help='new JSON receipt, created exclusively (optional)')
    args = ap.parse_args()
    if args.trials < 1:
        ap.error('--trials must be positive')
    if args.out_json and os.path.exists(args.out_json):
        ap.error('refusing to overwrite %s' % args.out_json)
    if args.logdir and not os.path.isdir(args.logdir):
        ap.error('no such log directory %s' % args.logdir)
    rec = Recorder()
    a_stats, a_hits = part_a(rec, random.Random(args.seed), args.trials)
    b_records, index = part_b(rec)
    calib = Path(args.v1_calib)
    c_records = part_c(rec, calib, index) if calib.is_dir() else []
    d_records = part_d(rec, Path(args.logdir), index) if args.logdir else []
    result = {
        'script': os.path.abspath(__file__),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python': sys.version.split()[0],
        'seed': args.seed,
        'trials': args.trials,
        'v1_calib': str(calib) if calib.is_dir() else None,
        'part_a_random_algebra': a_stats,
        'part_a_mutation_catches': a_hits,
        'part_b_independent_counts': b_records,
        'part_c_v1_positives': c_records,
        'part_d_logs': d_records,
        'failure_count': rec.count,
        'failures_first': rec.failures,
        'all_as_expected': rec.count == 0,
    }
    if args.out_json:
        with open(args.out_json, 'x') as fh:
            json.dump(result, fh, indent=1)
    print('A cases %d eligible_transforms %d entries_compared %d mutation_catches %s' % (
        len(a_stats), sum(s['eligible_transforms'] for s in a_stats), sum(s['entries_compared'] for s in a_stats),
        json.dumps(a_hits, sort_keys=True)))
    for r in b_records:
        print('B n%(n)d mu%(mu)d %(mode)s total_h %(total_h)d affine_classes %(affine_classes)d '
              'v1_solutions %(v1_model_solutions)s v2_solutions %(v2_model_solutions)s '
              'expect %(expected_first_status)s' % r)
    for c in c_records:
        print('C %s %s' % (os.path.basename(c['dmraw']), 'ok' if c['as_expected'] else 'MISMATCH'))
    for d in d_records:
        print('D %s %s' % (os.path.basename(d['log']), 'ok' if d['as_expected'] else 'MISMATCH'))
    if not c_records:
        print('C no v1 positives read from %s' % calib)
    if rec.count:
        print('CYCLE3 AFFINE CHECKS FAIL %d' % rec.count)
        for msg in rec.failures[:20]:
            print('  ' + msg)
        return 1
    print('CYCLE3 AFFINE CHECKS PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
