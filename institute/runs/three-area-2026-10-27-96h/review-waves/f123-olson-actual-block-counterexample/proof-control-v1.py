#!/usr/bin/env python3
"""f123 independent finite diagnostic (proof-control-v1).

Independently written for review-wave f123-olson-actual-block-counterexample.
No author code is imported or executed.  Definitions are taken only from the
literal excerpts in source-definition-excerpts-v1.md:

  * ACTUAL block: maximal CYCLIC run of reflections such that every gap between
    cyclically consecutive members is EMPTY (no rotation) and the two reflection
    values are EQUAL.  An occupied gap always separates; an empty gap separates
    iff the values differ.
  * PROJECTED run: maximal cyclic constant run of the reflection-only projection
    (rotations deleted), i.e. equal values alone fuse.
  * RAW edge between cyclically consecutive reflections: present iff values
    differ OR the gap is occupied.  Absent edge == same actual block.

Group arithmetic: D_{2p} realised as affine maps x -> a*x+b (mod p), a in {1,-1};
r^e = (1,e), r^e s = (-1,e); product g*h = g o h (apply h first), so that
s r = r^{-1} s.  Forward convention multiplies a selected subsequence left to
right in original order; the reversed convention multiplies right to left.
"""
import hashlib
import itertools
import json
import math
import os
import platform
import random
import sys
import time

PRIMES = (7, 11, 13, 17, 19, 23)
CLASS_EXHAUST_PRIMES = (7, 11, 13, 17, 19)      # 2^(p-1)-1 tail subsets each
BRUTE_MATCHING_PRIMES = (7, 11, 13, 17)         # 2^(#edges) edge subsets each
INDEX_BRUTE_PRIME = 7                            # C(3p-2, 2p) index subsets


# ---------------------------------------------------------------- group ----
def mul(g, h, p):
    return ((g[0] * h[0]) % p, (g[0] * h[1] + g[1]) % p)


def elt(letter, p):
    kind, e = letter
    return (1, e % p) if kind == 'R' else (p - 1, e % p)


def product(word, idx, p, reverse=False):
    seq = [word[i] for i in idx]
    if reverse:
        seq.reverse()
    g = (1, 0)
    for L in seq:
        g = mul(g, elt(L, p), p)
    return g


IDENT = (1, 0)


# ----------------------------------------------------------------- word ----
def build(p, scale=1):
    """Z rho Z rho Z^(2p-3) rho (T_1 rho) ... (T_(p-2) rho) T_(p-1)."""
    Z, RHO = ('S', 0), ('R', scale % p)
    w = [Z, RHO, Z, RHO] + [Z] * (2 * p - 3) + [RHO]
    for j in range(1, p - 1):
        w += [('S', (j * scale) % p), RHO]
    w.append(('S', ((p - 1) * scale) % p))
    return w


def reflections(word):
    return [i for i, (k, _) in enumerate(word) if k == 'S']


def gaps(word):
    """Cyclic gap q = letters strictly between reflection q and q+1 (mod F)."""
    refs = reflections(word)
    F = len(refs)
    out = []
    for q in range(F):
        i, j = refs[q], refs[(q + 1) % F]
        out.append(word[i + 1:j] if q + 1 < F else word[i + 1:] + word[:j])
    return refs, out


def cyclic_blocks(values, fuse):
    """Split the cyclic sequence `values` (length F) into maximal runs where
    fuse[q] says whether position q and q+1 (mod F) are in the same run.
    Returns list of (value, length, [positions]) in cyclic order from the
    first boundary; one single run if everything fuses."""
    F = len(values)
    if all(fuse):
        return [(values[0], F, list(range(F)))]
    start = next(q for q in range(F) if not fuse[(q - 1) % F])
    blocks = []
    for t in range(F):
        q = (start + t) % F
        if t == 0 or not fuse[(q - 1) % F]:
            blocks.append([values[q], 0, []])
        blocks[-1][1] += 1
        blocks[-1][2].append(q)
    return [tuple(b) for b in blocks]


def analyse(word, p):
    refs, G = gaps(word)
    F = len(refs)
    vals = [word[i][1] for i in refs]
    equal = [vals[q] == vals[(q + 1) % F] for q in range(F)]
    empty = [len(G[q]) == 0 for q in range(F)]
    fuse_actual = [equal[q] and empty[q] for q in range(F)]
    actual = cyclic_blocks(vals, fuse_actual)
    projected = cyclic_blocks(vals, equal)
    raw_present = [not f for f in fuse_actual]            # differ OR occupied
    lengths = [n for _, n, _ in actual]
    o_F = sum(n % 2 for n in lengths)
    e_F = sum(1 - n % 2 for n in lengths)
    H = sum(n // 2 for n in lengths)
    # raw graph components (subgraph of the F-cycle)
    if all(raw_present):
        comps = [list(range(F))]
        nu_formula = F // 2
    else:
        comps = [pos for _, _, pos in cyclic_blocks(list(range(F)), raw_present)]
        nu_formula = sum(len(c) // 2 for c in comps)
    sizes = sorted(len(c) for c in comps)
    return {
        'F': F, 'R': len(word) - F, 'N': len(word),
        'rotations_all_nonzero': all(e % p != 0 for k, e in word if k == 'R'),
        'max_gap_capacity': max(len(g) for g in G),
        'actual_blocks': [(v, n, [refs[q] for q in pos]) for v, n, pos in actual],
        'projected_runs': [(v, n) for v, n, _ in projected],
        'actual_o_e': (o_F, e_F),
        'projected_o_e': (sum(n % 2 for _, n, _ in projected),
                          sum(1 - n % 2 for _, n, _ in projected)),
        'H': H, 'kappa': p - 1 - H, 'k_F': len(lengths),
        'absent_edges': sum(1 for f in fuse_actual if f),
        'degenerate_single_block': all(fuse_actual),
        'raw_present_edges': sum(1 for f in raw_present if f),
        'raw_component_sizes': sizes,
        'raw_components_idx': [[refs[q] for q in c] for c in comps if len(c) > 1],
        'raw_matching_formula': nu_formula,
        'raw_edges_qpairs': [(q, (q + 1) % F) for q in range(F) if raw_present[q]],
    }


# ------------------------------------------------------- raw matching ------
def brute_max_matching(F, edges):
    best = 0
    m = len(edges)
    for mask in range(1 << m):
        used = set()
        ok = True
        cnt = 0
        for b in range(m):
            if mask >> b & 1:
                a, c = edges[b]
                if a in used or c in used:
                    ok = False
                    break
                used.add(a)
                used.add(c)
                cnt += 1
        if ok and cnt > best:
            best = cnt
    return best


# ------------------------------------------------------------ REF/mixed ---
def selection_dp(word, idx_list, p, L, reverse=False, count=False):
    """Over the letters word[i] for i in idx_list taken in order (or reversed
    order), compute for each k<=L the set (or multiplicity) of group elements
    that are products of exactly k selected letters, selected in order."""
    seq = [word[i] for i in idx_list]
    if reverse:
        seq.reverse()
    if count:
        dp = [dict() for _ in range(L + 1)]
        dp[0][IDENT] = 1
        for letter in seq:
            g = elt(letter, p)
            for k in range(L - 1, -1, -1):
                if not dp[k]:
                    continue
                tgt = dp[k + 1]
                for h, c in dp[k].items():
                    gh = mul(h, g, p)
                    tgt[gh] = tgt.get(gh, 0) + c
        return dp
    dp = [set() for _ in range(L + 1)]
    dp[0].add(IDENT)
    for letter in seq:
        g = elt(letter, p)
        for k in range(L - 1, -1, -1):
            if dp[k]:
                dp[k + 1] |= {mul(h, g, p) for h in dp[k]}
    return dp


def alt_sum(tail_vals):
    """A = j_m - j_{m-1} + j_{m-2} - ... for sorted tail exponents."""
    A = 0
    sgn = 1
    for j in reversed(tail_vals):
        A += sgn * j
        sgn = -sgn
    return A


def ref_class_exhaustion(word, p):
    refs = reflections(word)
    zeros = refs[:2 * p - 1]
    tail = refs[2 * p - 1:]
    assert all(word[i] == ('S', 0) for i in zeros) and len(tail) == p - 1
    total = 0
    support = set()
    min_A, max_A = p, 0
    for mask in range(1, 1 << (p - 1)):
        T = [tail[k] for k in range(p - 1) if mask >> k & 1]
        m = len(T)
        k = 2 * p - m
        chosen = zeros[:k] + T
        g = product(word, chosen, p)
        if g == IDENT:
            raise AssertionError('REF identity found in class exhaustion')
        if g[0] != 1:
            raise AssertionError('even reflection count gave a reflection')
        support.add(g[1])
        A = alt_sum([word[i][1] for i in T])
        if not (1 <= A <= p - 1):
            raise AssertionError('alternating-tail bound violated')
        if (-A) % p != g[1]:
            raise AssertionError('alternating sum disagrees with group product')
        min_A, max_A = min(min_A, A), max(max_A, A)
        total += math.comb(2 * p - 1, k)
    return {'classes': (1 << (p - 1)) - 1, 'index_subsets_covered': total,
            'comb_3p-2_choose_2p': math.comb(3 * p - 2, 2 * p),
            'support': sorted(support), 'min_A': min_A, 'max_A': max_A}


def author_selector(word, p):
    refs = reflections(word)
    rot = [i for i, (k, _) in enumerate(word) if k == 'R']
    zeros, tail = refs[:2 * p - 1], refs[2 * p - 1:]
    d = (-pow(3, -1, p)) % p
    return sorted(zeros[:p - 3] + rot + [tail[0], tail[d]]), d


def my_forward_selector(word, p):
    """Z rho Z rho Z^(2p-12) rho T_1 rho rho T_3 rho rho rho  (valid p>=7)."""
    refs = reflections(word)
    rot = [i for i, (k, _) in enumerate(word) if k == 'R']
    zeros, tail = refs[:2 * p - 1], refs[2 * p - 1:]
    big = zeros[2:]                        # the Z^(2p-3) block
    sel = [zeros[0], rot[0], zeros[1], rot[1]] + big[:2 * p - 12]
    rho_before_T1 = rot[2]
    sel += [rho_before_T1, tail[0]]
    rho_T = rot[3:]                        # rho after T_1, T_2, ..., T_(p-2)
    sel += rho_T[0:2] + [tail[2]] + rho_T[2:5]
    return sorted(sel)


def my_reversed_selector(word, p):
    """Index set {2p-4 big-block zeros, T_1, rho, rho, T_3}: identity under the
    right-to-left (reversed) multiplication convention (valid p>=5)."""
    refs = reflections(word)
    rot = [i for i, (k, _) in enumerate(word) if k == 'R']
    zeros, tail = refs[:2 * p - 1], refs[2 * p - 1:]
    big = zeros[2:]
    rho_T = rot[3:]
    return sorted(big[:2 * p - 4] + [tail[0]] + rho_T[0:2] + [tail[2]])


# ------------------------------------------------------------- controls ---
def ctrl_moved_gap(word):
    """Move the first splitting rotation (index 1) to the end."""
    return word[:1] + word[2:] + [word[1]]


def ctrl_no_equal_occupied(p):
    """Z^(2p-1) rho (T_1 rho)...(T_(p-2) rho) T_(p-1) rho rho: no occupied
    equal-value gap; wrap gap has capacity 2 (structural condition violated)."""
    Z, RHO = ('S', 0), ('R', 1)
    w = [Z] * (2 * p - 1) + [RHO]
    for j in range(1, p - 1):
        w += [('S', j), RHO]
    w += [('S', p - 1), RHO, RHO]
    return w


def ctrl_cyclic_shift(word, s):
    return word[s:] + word[:s]


def ctrl_ref_positive(word, p):
    w = list(word)
    w[-1] = ('S', 0)                       # T_(p-1) -> Z
    return w


def linear_block_oe(word):
    prev = None
    runs = []
    for k, v in word:
        if k == 'S':
            if prev is not None and prev == v:
                runs[-1] += 1
            else:
                runs.append(1)
            prev = v
        else:
            prev = None
    return (sum(n % 2 for n in runs), sum(1 - n % 2 for n in runs))


def random_word(p, rng):
    n = rng.randint(6, 22)
    w = []
    for _ in range(n):
        if rng.random() < 0.3:
            w.append(('R', rng.randint(1, p - 1)))
        else:
            w.append(('S', rng.choice([0, 0, 0, 1, 2, rng.randint(0, p - 1)])))
    if not any(k == 'S' for k, _ in w):
        w.append(('S', 0))
    return w


def union_find_blocks(word):
    """Independent second implementation of actual blocks via union-find on
    the reflection cycle."""
    refs, G = gaps(word)
    F = len(refs)
    parent = list(range(F))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for q in range(F):
        if len(G[q]) == 0 and word[refs[q]][1] == word[refs[(q + 1) % F]][1]:
            parent[find(q)] = find((q + 1) % F)
    sizes = {}
    for q in range(F):
        r = find(q)
        sizes[r] = sizes.get(r, 0) + 1
    return sorted(sizes.values())


# ------------------------------------------------------------------ main --
def main():
    t0 = time.time()
    out = {'script': os.path.basename(__file__), 'python': sys.version,
           'platform': platform.platform(), 'start_epoch': t0,
           'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t0)),
           'primes': list(PRIMES), 'family': [], 'controls': {}}
    try:
        with open(__file__, 'rb') as fh:
            out['script_sha256'] = hashlib.sha256(fh.read()).hexdigest()
    except OSError as exc:
        out['script_sha256'] = 'unavailable: %s' % exc

    for p in PRIMES:
        w = build(p)
        a = analyse(w, p)
        L = 2 * p
        rec = {'p': p, 'N': a['N'], 'F': a['F'], 'R': a['R'],
               'rotations_all_nonzero': a['rotations_all_nonzero'],
               'max_gap_capacity': a['max_gap_capacity'],
               'actual_o_e': a['actual_o_e'], 'projected_o_e': a['projected_o_e'],
               'actual_block_lengths': [n for _, n, _ in a['actual_blocks']],
               'projected_run_lengths': [n for _, n in a['projected_runs']],
               'H': a['H'], 'kappa': a['kappa'], 'k_F': a['k_F'],
               'absent_edges': a['absent_edges'],
               'identity_F_minus_kF_eq_2H_minus_eF': a['F'] - a['k_F'] == 2 * a['H'] - a['actual_o_e'][1],
               'identity_oF_eq_p_plus_2kappa': a['actual_o_e'][0] == p + 2 * a['kappa'],
               'bound_B_2kappa_plus_eF_le_p_minus_4': 2 * a['kappa'] + a['actual_o_e'][1] <= p - 4,
               'raw_present_edges': a['raw_present_edges'],
               'raw_component_sizes_summary': {
                   'largest': a['raw_component_sizes'][-1],
                   'isolates': a['raw_component_sizes'].count(1),
                   'components': len(a['raw_component_sizes'])},
               'raw_matching_formula': a['raw_matching_formula'],
               'nu_le_p_minus_2': a['raw_matching_formula'] <= p - 2,
               'nu_le_p_minus_3': a['raw_matching_formula'] <= p - 3,
               'nu_eq_(p+3)/2': a['raw_matching_formula'] == (p + 3) // 2,
               }
        rec['expected_actual_blocks_ok'] = (
            sorted(rec['actual_block_lengths']) == sorted([1, 1, 2 * p - 3] + [1] * (p - 1))
            and rec['actual_o_e'] == (p + 2, 0))
        rec['expected_projected_ok'] = (
            sorted(rec['projected_run_lengths']) == sorted([2 * p - 1] + [1] * (p - 1))
            and rec['projected_o_e'] == (p, 0))
        rec['expected_raw_ok'] = (a['raw_component_sizes'] == sorted([p + 3] + [1] * (2 * p - 5)))
        if p in BRUTE_MATCHING_PRIMES:
            nu_b = brute_max_matching(a['F'], a['raw_edges_qpairs'])
            rec['raw_matching_bruteforce'] = nu_b
            rec['raw_matching_agree'] = (nu_b == a['raw_matching_formula'])
        # REF: group-element DP over the real reflection indices
        refs = reflections(w)
        dp = selection_dp(w, refs, p, L)
        ref_set = dp[L]
        rec['REF_identity_exists'] = IDENT in ref_set
        rec['REF_support_rotation_exponents'] = sorted(b for (aa, b) in ref_set if aa == 1)
        rec['REF_any_reflection_products'] = any(aa != 1 for (aa, _) in ref_set)
        rec['REF_support_is_Fp_minus_0'] = rec['REF_support_rotation_exponents'] == list(range(1, p))
        if p in CLASS_EXHAUST_PRIMES:
            rec['REF_class_exhaustion'] = ref_class_exhaustion(w, p)
            rec['REF_class_exhaustion']['covers_all_index_subsets'] = (
                rec['REF_class_exhaustion']['index_subsets_covered']
                == rec['REF_class_exhaustion']['comb_3p-2_choose_2p'])
        if p == INDEX_BRUTE_PRIME:
            n_id = 0
            n_tot = 0
            supp = set()
            for combo in itertools.combinations(refs, L):
                g = product(w, combo, p)
                n_tot += 1
                if g == IDENT:
                    n_id += 1
                supp.add(g)
            rec['REF_index_bruteforce'] = {'subsets': n_tot, 'identity_count': n_id,
                                           'support': sorted(b for aa, b in supp if aa == 1),
                                           'expected_subsets': math.comb(3 * p - 2, L)}
        if p == 11:
            rng = random.Random(123)
            zeros = refs[:2 * p - 1]
            tail = refs[2 * p - 1:]
            mism = 0
            idc = 0
            for _ in range(20000):
                m = rng.randint(1, p - 1)
                T = sorted(rng.sample(tail, m))
                Zs = sorted(rng.sample(zeros, L - m))
                g = product(w, Zs + T, p)
                g_class = product(w, zeros[:L - m] + T, p)
                if g != g_class:
                    mism += 1
                if g == IDENT:
                    idc += 1
            rec['p11_random_index_subsets'] = {'samples': 20000, 'class_mismatches': mism,
                                               'identity_count': idc}
        # Mixed in-order 2p selections, both conventions, exact counts
        allidx = list(range(len(w)))
        cf = selection_dp(w, allidx, p, L, reverse=False, count=True)
        cr = selection_dp(w, allidx, p, L, reverse=True, count=True)
        rec['mixed_identity_count_forward'] = cf[L].get(IDENT, 0)
        rec['mixed_identity_count_reversed'] = cr[L].get(IDENT, 0)
        rec['mixed_identity_total_2p_subsets'] = math.comb(len(w), L)
        # explicit selectors
        sa, d = author_selector(w, p)
        rec['author_selector'] = {'d': d, 'indices': sa, 'len': len(sa),
                                  'forward_product': product(w, sa, p),
                                  'reversed_product': product(w, sa, p, reverse=True)}
        sf = my_forward_selector(w, p)
        rec['independent_forward_selector'] = {'indices': sf, 'len': len(sf),
                                               'forward_product': product(w, sf, p),
                                               'reversed_product': product(w, sf, p, reverse=True)}
        sr = my_reversed_selector(w, p)
        rec['independent_reversed_selector'] = {'indices': sr, 'len': len(sr),
                                                'forward_product': product(w, sr, p),
                                                'reversed_product': product(w, sr, p, reverse=True)}
        rec['selectors_strictly_increasing'] = all(
            s == sorted(s) and len(set(s)) == len(s) for s in (sa, sf, sr))
        # scaling automorphism a=2
        w2 = build(p, scale=2)
        a2 = analyse(w2, p)
        rec['scaled_a2_same_actual_projected'] = (a2['actual_o_e'], a2['projected_o_e']) == (a['actual_o_e'], a['projected_o_e'])
        rec['scaled_a2_REF_identity_exists'] = IDENT in selection_dp(w2, reflections(w2), p, L)[L]
        if p == 11:
            rec['p11_word_indexed'] = ['%d:%s' % (i, ('Z' if lt == ('S', 0) else ('rho' if lt[0] == 'R' else 'T%d' % lt[1]))) for i, lt in enumerate(w)]
            rec['p11_actual_blocks_indexed'] = a['actual_blocks']
            rec['p11_raw_path_indices'] = a['raw_components_idx']
            stated = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 24, 25, 27, 29, 31, 33, 35, 37, 38, 39, 41]
            steps = []
            g = IDENT
            for i in stated:
                g = mul(g, elt(w[i], p), p)
                steps.append('%d:%s%d->(%d,%d)' % (i, w[i][0], w[i][1], g[0], g[1]))
            rec['p11_stated_selector'] = {'indices': stated, 'len': len(stated),
                                          'equals_author_formula': stated == sa,
                                          'forward_product': g,
                                          'reversed_product': product(w, stated, p, reverse=True),
                                          'steps': steps}
            mut = list(stated)
            mut[mut.index(38)] = 36
            rec['p11_selector_mutation_38to36'] = {'forward_product': product(w, mut, p)}
        out['family'].append(rec)

    # ---------------------------------------------------------- controls --
    C = out['controls']
    for p in (7, 11, 13):
        w = build(p)
        base = analyse(w, p)
        L = 2 * p
        # A: moved occupied gap
        wa = ctrl_moved_gap(w)
        A = analyse(wa, p)
        C['A_moved_gap_p%d' % p] = {
            'word_len': len(wa), 'actual_o_e': A['actual_o_e'], 'projected_o_e': A['projected_o_e'],
            'actual_block_lengths_sorted': sorted(n for _, n, _ in A['actual_blocks']),
            'projection_unchanged': A['projected_o_e'] == base['projected_o_e'] and
                                    [v for v, _ in A['projected_runs']] == [v for v, _ in base['projected_runs']],
            'actual_changed_to_(p,1)': A['actual_o_e'] == (p, 1),
            'raw_component_sizes_nontrivial': [s for s in A['raw_component_sizes'] if s > 1],
            'raw_matching_formula': A['raw_matching_formula'],
            'REF_identity_exists': IDENT in selection_dp(wa, reflections(wa), p, L)[L],
            'kappa': A['kappa'], 'H': A['H']}
        # B: no occupied equal-value gap (negative control for the distinction)
        wb = ctrl_no_equal_occupied(p)
        B = analyse(wb, p)
        C['B_no_equal_occupied_gap_p%d' % p] = {
            'word_len': len(wb), 'N_eq_4p-1': len(wb) == 4 * p - 1,
            'max_gap_capacity': B['max_gap_capacity'],
            'actual_o_e': B['actual_o_e'], 'projected_o_e': B['projected_o_e'],
            'actual_equals_projected': B['actual_o_e'] == B['projected_o_e'] and
                                       sorted(n for _, n, _ in B['actual_blocks']) == sorted(n for _, n in B['projected_runs']),
            'raw_component_sizes_nontrivial': [s for s in B['raw_component_sizes'] if s > 1],
            'raw_matching_formula': B['raw_matching_formula'],
            'REF_identity_exists': IDENT in selection_dp(wb, reflections(wb), p, L)[L]}
        # C: cyclic shifts (one starts inside the big Z block)
        shifts = {}
        for s in (10, len(w) - 1, 4, 2 * p + 2):
            ws = ctrl_cyclic_shift(w, s)
            S = analyse(ws, p)
            shifts['shift_%d' % s] = {
                'cyclic_actual_o_e': S['actual_o_e'],
                'cyclic_actual_lengths_sorted': sorted(n for _, n, _ in S['actual_blocks']),
                'raw_component_sizes_invariant': S['raw_component_sizes'] == base['raw_component_sizes'],
                'raw_matching_invariant': S['raw_matching_formula'] == base['raw_matching_formula'],
                'linear_o_e': linear_block_oe(ws),
                'linear_differs_from_cyclic': linear_block_oe(ws) != S['actual_o_e'],
                'union_find_sizes_agree': union_find_blocks(ws) == sorted(n for _, n, _ in S['actual_blocks'])}
        C['C_cyclic_shift_p%d' % p] = shifts
        # D: REF positive control (T_(p-1) -> Z)
        wd = ctrl_ref_positive(w, p)
        D = analyse(wd, p)
        C['D_ref_positive_p%d' % p] = {
            'actual_o_e': D['actual_o_e'], 'projected_o_e': D['projected_o_e'],
            'REF_identity_exists': IDENT in selection_dp(wd, reflections(wd), p, L)[L],
            'all_2p_zero_reflections_product': product(wd, [i for i in reflections(wd) if wd[i] == ('S', 0)], p)}
        # E: selector mutations
        sa, d = author_selector(w, p)
        wrong_d = (d + 1) % (p - 1)
        refs = reflections(w)
        rot = [i for i, (k, _) in enumerate(w) if k == 'R']
        zeros, tail = refs[:2 * p - 1], refs[2 * p - 1:]
        bad = sorted(zeros[:p - 3] + rot + [tail[0], tail[wrong_d]])
        drop = sa[:-1]
        C['E_selector_mutation_p%d' % p] = {
            'wrong_tail_index_product': product(w, bad, p),
            'wrong_tail_is_identity': product(w, bad, p) == IDENT,
            'dropped_last_rotation_len': len(drop),
            'dropped_last_rotation_product': product(w, drop, p),
            'author_selector_reversed_convention_product': product(w, sa, p, reverse=True)}
    # F: random-word self-consistency of the implementation
    rng = random.Random(20261028)
    checks = {'words': 0, 'degenerate_skipped': 0, 'identity_failures': 0,
              'union_find_disagreements': 0, 'matching_disagreements': 0,
              'matching_bruteforced': 0, 'component_count_failures': 0}
    for _ in range(400):
        p = rng.choice((7, 11, 13))
        w = random_word(p, rng)
        A = analyse(w, p)
        checks['words'] += 1
        if union_find_blocks(w) != sorted(n for _, n, _ in A['actual_blocks']):
            checks['union_find_disagreements'] += 1
        if A['degenerate_single_block']:
            checks['degenerate_skipped'] += 1
            continue
        F, k_F, H, (o, e) = A['F'], A['k_F'], A['H'], A['actual_o_e']
        if not (F - k_F == 2 * H - e == A['absent_edges'] and o == F - 2 * H and o + e == k_F):
            checks['identity_failures'] += 1
        if A['absent_edges'] >= 1 and len(A['raw_component_sizes']) != A['absent_edges']:
            checks['component_count_failures'] += 1
        if len(A['raw_edges_qpairs']) <= 12:
            checks['matching_bruteforced'] += 1
            if brute_max_matching(F, A['raw_edges_qpairs']) != A['raw_matching_formula']:
                checks['matching_disagreements'] += 1
    C['F_random_word_selfconsistency'] = checks

    # ------------------------------------------------------------ verdict --
    fam = out['family']
    out['summary'] = {
        'all_actual_(p+2,0)': all(r['expected_actual_blocks_ok'] for r in fam),
        'all_projected_(p,0)': all(r['expected_projected_ok'] for r in fam),
        'all_raw_shape_path(p+3)+isolates(2p-5)': all(r['expected_raw_ok'] for r in fam),
        'all_nu_eq_(p+3)/2': all(r['nu_eq_(p+3)/2'] for r in fam),
        'all_bruteforce_matching_agree': all(r.get('raw_matching_agree', True) for r in fam),
        'nu_le_p-3_primes': [r['p'] for r in fam if r['nu_le_p_minus_3']],
        'nu_le_p-2_primes': [r['p'] for r in fam if r['nu_le_p_minus_2']],
        'all_REF_fail': all(not r['REF_identity_exists'] for r in fam),
        'all_REF_support_Fp_minus_0': all(r['REF_support_is_Fp_minus_0'] for r in fam),
        'all_class_exhaustion_complete': all(r['REF_class_exhaustion']['covers_all_index_subsets'] for r in fam if 'REF_class_exhaustion' in r),
        'all_mixed_forward_selector_exists': all(r['mixed_identity_count_forward'] > 0 for r in fam),
        'all_mixed_reversed_selector_exists': all(r['mixed_identity_count_reversed'] > 0 for r in fam),
        'all_author_selector_forward_identity': all(r['author_selector']['forward_product'] == IDENT for r in fam),
        'all_independent_forward_selector_identity': all(r['independent_forward_selector']['forward_product'] == IDENT for r in fam),
        'all_independent_reversed_selector_identity': all(r['independent_reversed_selector']['reversed_product'] == IDENT for r in fam),
        'controls_A_detect_(p,1)': all(v['actual_changed_to_(p,1)'] and v['projection_unchanged'] for k, v in C.items() if k.startswith('A_')),
        'controls_B_actual_eq_projected': all(v['actual_equals_projected'] for k, v in C.items() if k.startswith('B_')),
        'controls_C_cyclic_invariant': all(all(s['cyclic_actual_o_e'] == (int(k.split('p')[-1]) + 2, 0) and s['raw_matching_invariant'] and s['raw_component_sizes_invariant'] and s['union_find_sizes_agree'] for s in v.values()) for k, v in C.items() if k.startswith('C_')),
        'controls_C_some_linear_differs': all(any(s['linear_differs_from_cyclic'] for s in v.values()) for k, v in C.items() if k.startswith('C_')),
        'controls_D_ref_positive_found': all(v['REF_identity_exists'] for k, v in C.items() if k.startswith('D_')),
        'controls_E_mutations_not_identity': all((not v['wrong_tail_is_identity']) and v['dropped_last_rotation_product'] != IDENT for k, v in C.items() if k.startswith('E_')),
        'controls_F_clean': all(v == 0 for k, v in C['F_random_word_selfconsistency'].items() if k.endswith(('failures', 'disagreements'))),
    }
    out['end_epoch'] = time.time()
    out['end_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(out['end_epoch']))
    out['elapsed_s'] = round(out['end_epoch'] - t0, 3)
    out['overall'] = 'ALL_EXPECTED' if all(v is True or (isinstance(v, list) and v) for v in out['summary'].values()) else 'DEVIATION'
    path = sys.argv[1]
    with open(path, 'x', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True, default=list)
        fh.write('\n')
    print(json.dumps(out['summary'], sort_keys=True, default=list))
    print('overall:', out['overall'], 'elapsed_s:', out['elapsed_s'])


if __name__ == '__main__':
    main()
