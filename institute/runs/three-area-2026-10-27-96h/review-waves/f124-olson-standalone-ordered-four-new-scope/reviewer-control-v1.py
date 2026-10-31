#!/usr/bin/env python3
"""reviewer-control-v1.py -- f124 reviewer-written independent finite control.

Scope (standalone field-sequence statement ONLY): for every odd prime p, every
sequence z_1..z_{p+2} over Z/p with z_i != z_{i+1} for all i contains indices
i<j<k<l with z_i - z_j + z_k - z_l == 0 (mod p).

Written by the f124 reviewer. The author checker
frontier-20261028-olson-ordered-four-standalone-checker-v1.py was read as text
and is NOT imported or executed here. No actual-block, reflection, odd-run,
floor, raw-graph, L_RES or Olson application is made. Finite results are not an
all-prime proof; the written argument is reviewed separately in review-v1.md.

Sections
  A  detector cross-validation: O(L^4) brute force versus an independent
     O(L^2) prefix-difference bitmask method, plus a deliberately wrong oracle
     that must disagree (shows the comparison is not tautological)
  B  unnormalized full enumeration at p=3,5: every adjacent-distinct sequence
     of every length 1..p+2; zero-quadruple-free counts per length
  C  exhaustive pruned DFS over zero-quadruple-free adjacent-distinct sequences
     with z_1=0 (translation normalization) for each prime in --primes, up to
     length p+2.  Every node is checked against the internal claims of the
     written argument: multiplicity<=3 (M4), a tripled value excludes any other
     repeat (M3), two doubled values have crossing occurrence intervals (CROSS),
     2a-b is absent for doubled a!=b (ABSENT), full support forces an
     arithmetic progression (AP).  Cross-checked against B at p=3,5.
  D  affine-normalized DFS (z_1=0, z_2=1) for --affine-primes; counts must be
     exactly the z_1=0 counts divided by p-1 at every length >= 2
  E  section-4 positional quadruples: all a!=b, both crossing orders, all five
     insertion slots of x=2a-b, the exact index quadruple named in the text,
     odd primes <= 31; p=2 boundary records that x==b there (oddness is
     load-bearing)
  F  section-2 final step: positions 1,2,3,p+2 of every nonconstant arithmetic
     progression have alternating sum -p*d == 0, odd primes <= 101, with brute
     detection of a zero quadruple in the actual sequence
  G  adjacency hypothesis dropped (--no-adjacency-primes): number of
     zero-quadruple-free length-(p+2) sequences that allow adjacent equalities
     (expected > 0: the hypothesis is load-bearing for the statement)
  H  modulus probes: odd composite n (the written argument uses only that 2 is
     invertible, so no length-(n+2) counterexample is expected over Z/n for odd
     n) and even n (observational only)
  I  random sampling at larger odd primes: every length-(p+2) adjacent-distinct
     sample must contain a zero quadruple
"""
import argparse
import hashlib
import itertools
import json
import os
import platform
import random
import subprocess
import sys
import time
from collections import Counter

SEED = 12420261028  # reviewer seed, distinct from the author seed

EVIDENCE_DIR = ('/Users/jinleic/repos/aifours/mathematics/evidence/'
                'three-area-20261027-96h/parallel-18/ordered-olson')
RUN_DIR = ('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/'
           'review-waves/f124-olson-standalone-ordered-four-new-scope')
BOUND_FILES = [
    os.path.join(RUN_DIR, 'manifest-v1.json'),
    os.path.join(EVIDENCE_DIR, 'frontier-20261028-olson-actual-block-fatal-correction-v1.json'),
    os.path.join(EVIDENCE_DIR, 'frontier-20261028-olson-ordered-four-standalone-v1.md'),
    os.path.join(EVIDENCE_DIR, 'frontier-20261028-olson-ordered-four-standalone-checker-v1.py'),
    os.path.join(EVIDENCE_DIR, 'frontier-20261028-olson-ordered-four-standalone-check-results-v1.json'),
]

ODD_PRIMES_TO_101 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                     59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


def file_binding(path):
    with open(path, 'rb') as handle:
        data = handle.read()
    return {'path': path, 'sha256': hashlib.sha256(data).hexdigest(),
            'bytes': len(data), 'LF': data.count(b'\n')}


def date_now():
    return subprocess.run(['/bin/date'], capture_output=True, text=True,
                          check=True).stdout.strip()


# ---------------------------------------------------------------- detectors
def brute_first_zero_quad(seq, n):
    """Reference O(L^4) detector: lexicographically first i<j<k<l with
    z_i - z_j + z_k - z_l == 0 (mod n), else None."""
    for i, j, k, l in itertools.combinations(range(len(seq)), 4):
        if (seq[i] - seq[j] + seq[k] - seq[l]) % n == 0:
            return [i, j, k, l]
    return None


def prefix_masks(seq, n):
    """pref[k] = bitmask over Z/n of {z_i - z_j : i < j < k}."""
    pref = [0] * (len(seq) + 1)
    for k in range(len(seq)):
        mask = pref[k]
        zk = seq[k]
        for i in range(k):
            mask |= 1 << ((seq[i] - zk) % n)
        pref[k + 1] = mask
    return pref


def fast_has_zero_quad(seq, n):
    """Independent O(L^2) detector: a zero quadruple with largest index l exists
    iff for some k<l the value z_l - z_k lies in pref[k]."""
    pref = prefix_masks(seq, n)
    for l in range(len(seq)):
        zl = seq[l]
        for k in range(l):
            if (pref[k] >> ((zl - seq[k]) % n)) & 1:
                return True
    return False


def wrong_oracle(seq, n):
    """Deliberately wrong predicate (plain sum of four entries) used only to
    show that the cross-validation in section A can fail."""
    for i, j, k, l in itertools.combinations(range(len(seq)), 4):
        if (seq[i] + seq[j] + seq[k] + seq[l]) % n == 0:
            return True
    return False


# ---------------------------------------------------------------- DFS
def rotate(mask, shift, n, full):
    shift %= n
    return ((mask << shift) | (mask >> (n - shift))) & full


def dfs_quadfree(n, max_len, adjacent_distinct=True, fix_second=None,
                 lemma_checks=True):
    """Enumerate every zero-quadruple-free sequence over Z/n with z_1 = 0
    (optionally z_2 = fix_second) up to length max_len.  Because a prefix of a
    zero-quadruple-free sequence is zero-quadruple-free, pruning at the first
    zero quadruple loses nothing: counts[L] is the exact number of such
    sequences of length L with the chosen normalization."""
    full = (1 << n) - 1
    counts = [0] * (max_len + 1)
    viol = Counter()
    full_support_seen = Counter()
    first_example = {}
    seq = [0]
    pref = [0, 0]
    state = {'nodes': 0}

    def check_lemmas(s):
        c = Counter(s)
        mults = sorted(c.values(), reverse=True)
        if mults[0] >= 4:
            viol['M4_value_with_multiplicity_ge_4'] += 1
        if mults[0] == 3 and len(mults) > 1 and mults[1] >= 2:
            viol['M3_triple_coexists_with_other_repeat'] += 1
        doubled = [v for v, m in c.items() if m == 2]
        if len(doubled) >= 2:
            pos = {}
            for idx, v in enumerate(s):
                if c[v] == 2:
                    pos.setdefault(v, []).append(idx)
            for a, b in itertools.combinations(doubled, 2):
                a1, a2 = pos[a]
                b1, b2 = pos[b]
                if not ((a1 < b1 < a2 < b2) or (b1 < a1 < b2 < a2)):
                    viol['CROSS_doubled_pair_not_crossing'] += 1
            present = set(s)
            for a in doubled:
                for b in doubled:
                    if a != b and ((2 * a - b) % n) in present:
                        viol['ABSENT_2a_minus_b_present'] += 1
        if len(c) == n:
            full_support_seen[len(s)] += 1
            d = (s[1] - s[0]) % n
            for i in range(1, len(s) - 1):
                if (s[i + 1] - s[i]) % n != d:
                    viol['AP_full_support_not_arithmetic'] += 1
                    break

    def rec():
        length = len(seq)
        state['nodes'] += 1
        counts[length] += 1
        if length not in first_example:
            first_example[length] = list(seq)
        if lemma_checks:
            check_lemmas(seq)
        if length == max_len:
            return
        forbidden = 0
        for k in range(length):
            forbidden |= rotate(pref[k], seq[k], n, full)
        if adjacent_distinct:
            forbidden |= 1 << seq[-1]
        cand = full & ~forbidden
        if length == 1 and fix_second is not None:
            cand &= 1 << fix_second
        base = pref[length]
        while cand:
            low = cand & -cand
            v = low.bit_length() - 1
            cand ^= low
            mask = base
            for i in range(length):
                mask |= 1 << ((seq[i] - v) % n)
            seq.append(v)
            pref.append(mask)
            rec()
            seq.pop()
            pref.pop()

    t0 = time.time()
    rec()
    attained = max(L for L in range(1, max_len + 1) if counts[L] > 0)
    return {
        'n': n, 'max_len': max_len, 'adjacent_distinct': adjacent_distinct,
        'fix_second': fix_second, 'lemma_checks': lemma_checks,
        'nodes': state['nodes'], 'elapsed_s': round(time.time() - t0, 3),
        'quadfree_counts_by_length': {str(L): counts[L] for L in range(1, max_len + 1)},
        'max_attained_length': attained,
        'first_example_at_max_attained_length': first_example[attained],
        'lemma_violations': dict(viol),
        'full_support_quadfree_by_length': {str(k): v for k, v in sorted(full_support_seen.items())},
    }


# ---------------------------------------------------------------- sections
def section_a(rng, trials):
    agree = 0
    wrong_disagree = 0
    for _ in range(trials):
        n = rng.choice([3, 5, 7, 11, 13])
        length = rng.randint(4, n + 2)
        seq = [rng.randrange(n) for _ in range(length)]
        brute = brute_first_zero_quad(seq, n) is not None
        fast = fast_has_zero_quad(seq, n)
        agree += (brute == fast)
        wrong_disagree += (wrong_oracle(seq, n) != brute)
    return {'trials': trials, 'brute_fast_agree': agree,
            'wrong_oracle_disagreements': wrong_disagree}


def section_b(p):
    counts = {}
    for length in range(1, p + 3):
        total = 0
        free = 0
        for first in range(p):
            for steps in itertools.product(range(1, p), repeat=length - 1):
                seq = [first]
                for d in steps:
                    seq.append((seq[-1] + d) % p)
                total += 1
                if brute_first_zero_quad(seq, p) is None:
                    free += 1
        counts[str(length)] = {'adjacent_distinct_sequences': total,
                               'zero_quadruple_free': free}
    return counts


def section_e(primes):
    cases = 0
    failures = []
    for p in primes:
        for a in range(p):
            for b in range(p):
                if a == b:
                    continue
                x = (2 * a - b) % p
                if x == a or x == b:
                    failures.append({'p': p, 'a': a, 'b': b, 'reason': 'x_equals_a_or_b'})
                for order, pattern in (('a1<b1<a2<b2', [a, b, a, b]),
                                       ('b1<a1<b2<a2', [b, a, b, a])):
                    for slot in range(5):
                        seq = pattern[:slot] + [x] + pattern[slot:]
                        if any(u == v for u, v in zip(seq, seq[1:])):
                            failures.append({'p': p, 'a': a, 'b': b, 'order': order,
                                             'slot': slot, 'reason': 'not_adjacent_distinct'})
                        pos_a = [i for i, v in enumerate(seq) if v == a]
                        pos_b = [i for i, v in enumerate(seq) if v == b]
                        pos_x = seq.index(x)
                        a1, a2 = pos_a
                        b1, b2 = pos_b
                        if order == 'a1<b1<a2<b2':
                            if pos_x < a1:
                                quad = (pos_x, a1, b1, a2)
                            elif pos_x < a2:
                                quad = (a1, pos_x, a2, b2)
                            else:
                                quad = (a1, b1, a2, pos_x)
                        else:
                            if pos_x < a1:
                                quad = (pos_x, a1, b2, a2)
                            elif pos_x < a2:
                                quad = (b1, a1, pos_x, a2)
                            else:
                                quad = (a1, b2, a2, pos_x)
                        i, j, k, l = quad
                        increasing = i < j < k < l
                        total = (seq[i] - seq[j] + seq[k] - seq[l]) % p
                        if not increasing or total != 0:
                            failures.append({'p': p, 'a': a, 'b': b, 'order': order,
                                             'slot': slot, 'seq': seq, 'quad': quad,
                                             'reason': 'claimed_quadruple_wrong'})
                        cases += 1
    # injectivity of b -> 2a-b for fixed a (distinct absent values)
    injective = all(len({(2 * a - b) % p for b in range(p) if b != a}) == p - 1
                    for p in primes for a in range(p))
    # p = 2 boundary: x == b whenever a != b
    p2 = [{'a': a, 'b': b, 'x': (2 * a - b) % 2} for a in range(2) for b in range(2) if a != b]
    return {'primes': primes, 'cases': cases, 'failures': failures,
            'absent_values_injective': injective,
            'p2_boundary_x_equals_b': all(e['x'] == e['b'] for e in p2),
            'p2_boundary_detail': p2}


def section_f(primes):
    checked = 0
    failures = []
    for p in primes:
        for d in range(1, p):
            seq = [(i * d) % p for i in range(p + 2)]
            if any(u == v for u, v in zip(seq, seq[1:])):
                failures.append({'p': p, 'd': d, 'reason': 'not_adjacent_distinct'})
            if (seq[0] - seq[1] + seq[2] - seq[p + 1]) % p != 0:
                failures.append({'p': p, 'd': d, 'reason': 'positions_1_2_3_p+2_nonzero'})
            if ((-p * d) % p) != 0:
                failures.append({'p': p, 'd': d, 'reason': 'minus_p_d_nonzero'})
            if brute_first_zero_quad(seq, p) is None:
                failures.append({'p': p, 'd': d, 'reason': 'no_zero_quadruple_detected'})
            checked += 1
    return {'primes': primes, 'progressions_checked': checked, 'failures': failures}


def section_i(rng, primes, samples):
    out = {}
    for p in primes:
        detected = 0
        free_at_p_plus_1 = 0
        for _ in range(samples):
            seq = [rng.randrange(p)]
            for _ in range(p + 1):
                seq.append((seq[-1] + rng.randrange(1, p)) % p)
            if fast_has_zero_quad(seq, p):
                detected += 1
            if not fast_has_zero_quad(seq[:p + 1], p):
                free_at_p_plus_1 += 1
        out[str(p)] = {'samples': samples, 'length_p_plus_2_detected': detected,
                       'length_p_plus_1_prefix_quadfree': free_at_p_plus_1}
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--output', help='receipt path (exclusive create); omit for a gauge run')
    parser.add_argument('--primes', default='3,5,7,11,13')
    parser.add_argument('--affine-primes', default='7,11,13')
    parser.add_argument('--odd-composites', default='9')
    parser.add_argument('--evens', default='4,6,8')
    parser.add_argument('--no-adjacency-primes', default='3,5,7')
    parser.add_argument('--sample-primes', default='17,19,23,29,31')
    parser.add_argument('--samples', type=int, default=3000)
    parser.add_argument('--detector-trials', type=int, default=20000)
    args = parser.parse_args()

    def ints(text):
        return [int(t) for t in text.split(',') if t.strip()]

    start_date = date_now()
    t_start = time.time()
    rng = random.Random(SEED)
    receipt = {
        'kind': 'F124_REVIEWER_INDEPENDENT_FINITE_CONTROL',
        'scope': ('standalone field-sequence ordered-four statement only; no actual-block, '
                  'reflection, odd-run, floor, raw-graph, L_RES, Olson or f111 application; '
                  'author checker read as text, not imported or executed'),
        'argv': sys.argv, 'python': sys.version, 'platform': platform.platform(),
        'seed': SEED, 'bin_date_at_start': start_date,
        'bound_inputs': [file_binding(path) for path in BOUND_FILES],
        'self_binding': file_binding(os.path.abspath(__file__)),
    }

    primes = ints(args.primes)
    affine_primes = ints(args.affine_primes)

    receipt['A_detector_cross_validation'] = section_a(rng, args.detector_trials)

    receipt['B_unnormalized_full_enumeration'] = {str(p): section_b(p) for p in (3, 5) if p in primes}

    dfs_prime = {}
    for p in primes:
        dfs_prime[str(p)] = dfs_quadfree(p, p + 2, adjacent_distinct=True)
    receipt['C_exhaustive_dfs_z1_zero'] = dfs_prime

    b_c_consistent = True
    for p in (3, 5):
        if str(p) in receipt['B_unnormalized_full_enumeration']:
            for length in range(1, p + 3):
                b_free = receipt['B_unnormalized_full_enumeration'][str(p)][str(length)]['zero_quadruple_free']
                c_free = dfs_prime[str(p)]['quadfree_counts_by_length'][str(length)]
                if b_free != p * c_free:
                    b_c_consistent = False
    receipt['B_vs_C_translation_consistency'] = b_c_consistent

    dfs_affine = {}
    affine_consistent = True
    for p in affine_primes:
        res = dfs_quadfree(p, p + 2, adjacent_distinct=True, fix_second=1)
        dfs_affine[str(p)] = res
        if str(p) in dfs_prime:
            for length in range(2, p + 3):
                if dfs_prime[str(p)]['quadfree_counts_by_length'][str(length)] != \
                        (p - 1) * res['quadfree_counts_by_length'][str(length)]:
                    affine_consistent = False
    receipt['D_exhaustive_dfs_affine_z1_zero_z2_one'] = dfs_affine
    receipt['D_vs_C_scaling_consistency'] = affine_consistent

    receipt['E_section4_positional'] = section_e([q for q in ODD_PRIMES_TO_101 if q <= 31])
    receipt['F_section2_arithmetic_progression_step'] = section_f(ODD_PRIMES_TO_101)

    receipt['G_adjacency_dropped'] = {
        str(p): dfs_quadfree(p, p + 2, adjacent_distinct=False)
        for p in ints(args.no_adjacency_primes)}

    receipt['H_modulus_probes'] = {
        'odd_composite': {str(n): dfs_quadfree(n, n + 2, adjacent_distinct=True)
                          for n in ints(args.odd_composites)},
        'even': {str(n): dfs_quadfree(n, n + 2, adjacent_distinct=True)
                 for n in ints(args.evens)},
    }

    receipt['I_random_sampling'] = section_i(rng, ints(args.sample_primes), args.samples)

    # ------------------------------------------------------------ verdict
    required = {
        'A_detectors_agree_on_all_trials':
            receipt['A_detector_cross_validation']['brute_fast_agree'] == args.detector_trials,
        'A_wrong_oracle_actually_disagrees':
            receipt['A_detector_cross_validation']['wrong_oracle_disagreements'] > 0,
        'B_vs_C_translation_consistency': b_c_consistent,
        'C_no_zero_quadruple_free_sequence_of_length_p_plus_2':
            all(r['quadfree_counts_by_length'][str(r['n'] + 2)] == 0 for r in dfs_prime.values()),
        'C_internal_claims_no_violation':
            all(not r['lemma_violations'] for r in dfs_prime.values()),
        'D_no_zero_quadruple_free_sequence_of_length_p_plus_2':
            all(r['quadfree_counts_by_length'][str(r['n'] + 2)] == 0 for r in dfs_affine.values()),
        'D_internal_claims_no_violation':
            all(not r['lemma_violations'] for r in dfs_affine.values()),
        'D_vs_C_scaling_consistency': affine_consistent,
        'E_section4_all_claimed_quadruples_zero_and_increasing':
            not receipt['E_section4_positional']['failures'],
        'E_absent_values_injective': receipt['E_section4_positional']['absent_values_injective'],
        'F_section2_all_progressions_zero':
            not receipt['F_section2_arithmetic_progression_step']['failures'],
        'I_every_random_length_p_plus_2_sample_detected':
            all(v['length_p_plus_2_detected'] == v['samples'] for v in receipt['I_random_sampling'].values()),
    }
    observational = {
        'tightness_max_quadfree_length_equals_p_plus_1': {
            str(p): r['max_attained_length'] == p + 1 for p, r in ((int(k), v) for k, v in dfs_prime.items())},
        'adjacency_dropped_length_p_plus_2_quadfree_count': {
            k: v['quadfree_counts_by_length'][str(v['n'] + 2)] for k, v in receipt['G_adjacency_dropped'].items()},
        'adjacency_dropped_lemma_violations': {
            k: v['lemma_violations'] for k, v in receipt['G_adjacency_dropped'].items()},
        'odd_composite_length_n_plus_2_quadfree_count': {
            k: v['quadfree_counts_by_length'][str(v['n'] + 2)]
            for k, v in receipt['H_modulus_probes']['odd_composite'].items()},
        'odd_composite_lemma_violations': {
            k: v['lemma_violations'] for k, v in receipt['H_modulus_probes']['odd_composite'].items()},
        'even_length_n_plus_2_quadfree_count': {
            k: v['quadfree_counts_by_length'][str(v['n'] + 2)]
            for k, v in receipt['H_modulus_probes']['even'].items()},
        'even_lemma_violations': {
            k: v['lemma_violations'] for k, v in receipt['H_modulus_probes']['even'].items()},
        'p2_boundary_x_equals_b': receipt['E_section4_positional']['p2_boundary_x_equals_b'],
    }
    receipt['required_checks'] = required
    receipt['observational'] = observational
    receipt['result'] = ('PASS_F124_REVIEWER_STANDALONE_ORDERED_FOUR_FINITE_CONTROL'
                         if all(required.values())
                         else 'FAIL_F124_REVIEWER_STANDALONE_ORDERED_FOUR_FINITE_CONTROL')
    receipt['elapsed_s'] = round(time.time() - t_start, 3)
    receipt['bin_date_at_end'] = date_now()
    receipt['disclaimer'] = ('finite control only; not an all-prime proof, not a human, '
                             'independent-family, formal/kernel, novelty or Olson-closure claim')

    text = json.dumps(receipt, indent=2, sort_keys=True) + '\n'
    if args.output:
        with open(args.output, 'x', encoding='utf-8') as out:
            out.write(text)
    summary = {k: receipt[k] for k in ('result', 'required_checks', 'observational',
                                       'elapsed_s', 'bin_date_at_start', 'bin_date_at_end')}
    summary['dfs_nodes'] = {k: v['nodes'] for k, v in dfs_prime.items()}
    summary['dfs_affine_nodes'] = {k: v['nodes'] for k, v in dfs_affine.items()}
    summary['dfs_counts'] = {k: v['quadfree_counts_by_length'] for k, v in dfs_prime.items()}
    print(json.dumps(summary, indent=1, sort_keys=True))


if __name__ == '__main__':
    main()
