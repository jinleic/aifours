#!/usr/bin/env python3
"""reviewer-control-v1.py -- f139 review: reviewer-written exact finite control.

Scope (projection-only, exactly as in the f139 manifest):
  p odd prime; W a D_{2p} word of length N=4p-1 with F=3p-2 reflections and R=p+1 rotations.
  Delete rotations -> cyclic reflection-only projection; its maximal CYCLIC constant runs are the
  "projection runs", labelled by the reflection exponent c (sigma_c := rho^c sigma).
  Hypothesis: exactly p odd-length projection runs with pairwise distinct labels; even runs arbitrary.
  If the cyclic actual word contains four consecutive letters sigma_c rho_u sigma_c rho_v whose two
  sigma_c lie in one odd projection run, then some 2p indices i_1<...<i_{2p} (ORIGINAL linear order)
  satisfy a_{i_1} ... a_{i_{2p}} = e.

Conventions: a letter (x,e) means rho^x sigma^e; sigma_c = (c,1); rho_u = (u,0).
Group law (x,e)(y,b) = (x + (-1)^e y mod p, e xor b), cross-checked here against the permutation
representation rho: i -> i+1, sigma: i -> -i on Z/p with g*h := g o h (apply h first).

Standard library only.  Nothing written by the candidate's author is imported, read or executed by
this script; its producer, premise checker, recipe implementation, DP cross-check and mutations are
the reviewer's own.
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


class ControlError(Exception):
    pass


def clock():
    return subprocess.run(['/bin/date', '-u', '+%Y-%m-%dT%H:%M:%SZ'],
                          capture_output=True, text=True, check=True).stdout.strip()


# ---------------------------------------------------------------- group D_{2p}
def mul(p, g, h):
    x, e = g
    y, b = h
    return ((x + (y if e == 0 else -y)) % p, e ^ b)


def prod(p, letters):
    acc = (0, 0)
    for g in letters:
        acc = mul(p, acc, g)
    return acc


def perm_of(p, g):
    x, e = g
    return tuple((x + (i if e == 0 else -i)) % p for i in range(p))


def perm_compose(f, g):
    return tuple(f[g[i]] for i in range(len(f)))


def perm_prod(p, letters):
    acc = tuple(range(p))
    for g in letters:
        acc = perm_compose(acc, perm_of(p, g))
    return acc


def group_selftest(p):
    elems = [(x, e) for x in range(p) for e in (0, 1)]
    # permutation representation is faithful and respects the law
    if len({perm_of(p, g) for g in elems}) != 2 * p:
        raise ControlError('GROUP_REP_NOT_FAITHFUL')
    for g in elems:
        for h in elems:
            if perm_of(p, mul(p, g, h)) != perm_compose(perm_of(p, g), perm_of(p, h)):
                raise ControlError('GROUP_LAW_MISMATCH')
    rho, sig = (1, 0), (0, 1)
    if prod(p, [sig, sig]) != (0, 0) or prod(p, [rho] * p) != (0, 0):
        raise ControlError('GROUP_RELATIONS')
    if prod(p, [sig, rho, sig]) != ((-1) % p, 0):
        raise ControlError('GROUP_CONJUGATION')
    for a in range(p):
        for b in range(p):
            if prod(p, [(a, 1), (b, 1)]) != ((a - b) % p, 0):
                raise ControlError('PAIR_PRODUCT')
    for c in range(p):
        for u in range(p):
            for v in range(p):
                if prod(p, [(c, 1), (u, 0), (c, 1), (v, 0)]) != ((v - u) % p, 0):
                    raise ControlError('FOURBLOCK_PRODUCT')
    return True


# ------------------------------------------------------------ projection runs
def projection_runs(p, word):
    """Maximal cyclic constant runs of the reflection-only projection, in cyclic projection order
    starting at a run boundary.  Each run: label, positions (actual indices, projection order), length."""
    refs = [i for i, (x, e) in enumerate(word) if e == 1]
    labels = [word[i][0] for i in refs]
    F = len(refs)
    start = None
    for k in range(F):
        if labels[k] != labels[k - 1]:          # k-1 == -1 wraps cyclically
            start = k
            break
    if start is None:
        raise ControlError('SINGLE_PROJECTION_RUN')
    rotated = list(zip(labels[start:] + labels[:start], refs[start:] + refs[:start]))
    runs = []
    for label, grp in itertools.groupby(rotated, key=lambda t: t[0]):
        pos = [i for _, i in grp]
        runs.append({'label': label, 'positions': pos, 'length': len(pos)})
    return runs


def check_premise(p, word):
    N = len(word)
    if N != 4 * p - 1:
        raise ControlError('LENGTH')
    for x, e in word:
        if not (0 <= x < p and e in (0, 1)):
            raise ControlError('LETTER_RANGE')
    F = sum(1 for _, e in word if e == 1)
    if F != 3 * p - 2:
        raise ControlError('REFLECTION_COUNT')
    runs = projection_runs(p, word)
    odd = [r for r in runs if r['length'] % 2 == 1]
    if len(odd) != p:
        raise ControlError('PREMISE_ODD_RUN_COUNT')
    if len({r['label'] for r in odd}) != p:
        raise ControlError('PREMISE_LABELS_NOT_DISTINCT')
    return runs


def find_fourblocks(p, word, runs):
    """All cyclic start positions s with (word[s..s+3] mod N) = sigma_c rho_u sigma_c rho_v and the
    two sigma_c in one ODD projection run."""
    N = len(word)
    run_of = {}
    for ri, r in enumerate(runs):
        for i in r['positions']:
            run_of[i] = ri
    out = []
    for s in range(N):
        a, b, c, d = (word[(s + k) % N] for k in range(4))
        if a[1] == 1 and b[1] == 0 and c[1] == 1 and d[1] == 0 and a[0] == c[0]:
            if run_of[s] == run_of[(s + 2) % N] and runs[run_of[s]]['length'] % 2 == 1:
                out.append(s)
    return out


# ------------------------------------------------------------ the §3 recipe
def recipe_selector(p, word, runs, s, drop_choice=0):
    """Build the 2p-index selector of the candidate's §3 for the block starting at s.
    Returns (sorted original indices, info).  Raises ControlError on a recipe failure
    (NO_DIRECTED_PAIR / NOT_ENOUGH_PAIRS) -- impossible under the premise, reachable under mutation."""
    N = len(word)
    block = [(s + k) % N for k in range(4)]
    u, v = word[block[1]][0], word[block[3]][0]
    t = (u - v) % p
    cut = [(block[3] + 1 + k) % N for k in range(N - 4)]            # cut order after the block
    refs_cut = [i for i in cut if word[i][1] == 1]
    refpos = {i: k for k, i in enumerate(refs_cut)}
    pieces = []                                                       # (run index, label, positions)
    for ri, r in enumerate(runs):
        pos = sorted((i for i in r['positions'] if i not in block), key=refpos.__getitem__)
        seg = []
        for i in pos:
            if seg and refpos[i] != refpos[seg[-1]] + 1:
                pieces.append((ri, r['label'], seg))
                seg = []
            seg.append(i)
        if seg:
            pieces.append((ri, r['label'], seg))
    pairs, reps = [], {}
    for ri, label, seg in pieces:
        for k in range(0, len(seg) - 1, 2):
            pairs.append((seg[k], seg[k + 1]))
        if len(seg) % 2 == 1:
            if ri in reps:
                raise ControlError('STRUCTURE_TWO_LEFTOVERS_ONE_RUN')
            reps[ri] = (refpos[seg[-1]], label, seg[-1])
    for ri, r in enumerate(runs):
        if (r['length'] % 2 == 1) != (ri in reps):
            raise ControlError('STRUCTURE_LEFTOVER_PARITY')
    need = p - 2 - (1 if t else 0)
    if len(pairs) < need:
        raise ControlError('NOT_ENOUGH_PAIRS')
    chosen_reps = []
    if t:
        ordered = sorted(reps.values())
        found = None
        for a in range(len(ordered)):
            for b in range(a + 1, len(ordered)):
                if (ordered[a][1] - ordered[b][1]) % p == t:
                    found = (ordered[a][2], ordered[b][2])
                    break
            if found:
                break
        if found is None:
            raise ControlError('NO_DIRECTED_PAIR')
        chosen_reps = list(found)
    use = list(pairs)
    while len(use) > need:
        del use[drop_choice % len(use)]
    sel = list(block) + [i for pr in use for i in pr] + chosen_reps
    if len(sel) != 2 * p or len(set(sel)) != 2 * p:
        raise ControlError('SELECTOR_SIZE')
    info = {'t': t, 'u': u, 'v': v, 'pairs_available': len(pairs), 'pairs_used': len(use),
            'reps': chosen_reps, 'block': block}
    return sorted(sel), info


def verify_identity(p, word, sel):
    letters = [word[i] for i in sel]
    a = prod(p, letters) == (0, 0)
    b = perm_prod(p, letters) == tuple(range(p))
    if a != b:
        raise ControlError('REPRESENTATION_DISAGREEMENT')
    return a


def exists_identity_subsequence(p, word, k):
    """Independent of the recipe: does ANY increasing index sequence of length k multiply to e?"""
    layers = [set() for _ in range(k + 1)]
    layers[0].add((0, 0))
    for g in word:
        for c in range(k - 1, -1, -1):
            if layers[c]:
                nxt = layers[c + 1]
                for h in layers[c]:
                    nxt.add(mul(p, h, g))
    return (0, 0) in layers[k]


# ------------------------------------------------------------ reviewer producer
def produce(p, rng, want_unequal, n_even):
    units = p - 2 - n_even
    if units < 0:
        raise ValueError('too many even runs')
    odd_len = [3] + [1] * (p - 1)                 # run 0 is the designated block run
    even_len = [2] * n_even
    for _ in range(units):
        j = rng.randrange(p + n_even)
        if j < p:
            odd_len[j] += 2
        else:
            even_len[j - p] += 2
    odd_labels = list(range(p))
    rng.shuffle(odd_labels)
    seq = [['odd', odd_labels[j], odd_len[j], j == 0] for j in range(p)]
    rng.shuffle(seq)
    for m in range(n_even):
        seq.insert(rng.randrange(len(seq) + 1), ['even', None, even_len[m], False])
    L = len(seq)
    for idx in range(L):
        if seq[idx][0] == 'even':
            forbidden = {seq[(idx - 1) % L][1], seq[(idx + 1) % L][1]} - {None}
            seq[idx][1] = rng.choice([c for c in range(p) if c not in forbidden])
    for idx in range(L):
        if seq[idx][1] == seq[(idx + 1) % L][1]:
            raise ControlError('PRODUCER_ADJACENT_EQUAL')
    refl = []
    for ri, (kind, label, length, isblock) in enumerate(seq):
        refl.extend([(label, ri)] * length)
    F = len(refl)
    if F != 3 * p - 2:
        raise ControlError('PRODUCER_F')
    bri = next(ri for ri, item in enumerate(seq) if item[3])
    bpos = [k for k, (_, ri) in enumerate(refl) if ri == bri]
    j = rng.randrange(len(bpos) - 1)
    b1, b2 = bpos[j], bpos[j + 1]
    u = rng.randrange(p)
    v = rng.choice([x for x in range(p) if x != u]) if want_unequal else u
    gaps = [[] for _ in range(F)]
    gaps[b1] = [u]
    gaps[b2] = [v]
    for _ in range(p + 1 - 2):
        k = rng.randrange(F)
        while k == b1:
            k = rng.randrange(F)
        gaps[k].append(rng.randrange(p))
    cyc = []
    for k in range(F):
        cyc.append((refl[k][0], 1))
        cyc.extend((r, 0) for r in gaps[k])
    N = len(cyc)
    if N != 4 * p - 1:
        raise ControlError('PRODUCER_N')
    off = rng.randrange(N)
    word = cyc[off:] + cyc[:off]
    meta = {'n_even': n_even, 'u': u, 'v': v, 'run_kinds': [s[0] for s in seq],
            'run_labels': [s[1] for s in seq], 'run_lengths': [s[2] for s in seq],
            'linear_offset': off}
    return word, meta


# ------------------------------------------------------------ mutations
def mutate_labels(p, word, runs, rng):
    """Relabel one odd run to another odd run's label while keeping every run boundary
    (new label differs from both cyclic neighbours).  Breaks ONLY the distinct-labels premise."""
    L = len(runs)
    odd_idx = [ri for ri, r in enumerate(runs) if r['length'] % 2 == 1]
    odd_labels = {runs[ri]['label'] for ri in odd_idx}
    options = []
    for ri in odd_idx:
        nb = {runs[(ri - 1) % L]['label'], runs[(ri + 1) % L]['label'], runs[ri]['label']}
        for c in sorted(odd_labels - nb):
            options.append((ri, c))
    if not options:
        return None
    ri, c = rng.choice(options)
    w = list(word)
    for i in runs[ri]['positions']:
        w[i] = (c, 1)
    return w, {'run': ri, 'old_label': runs[ri]['label'], 'new_label': c}


def mutate_runcount(p, word, runs, block_start, rng):
    """Move one boundary reflection from an odd run A (length>=3) to a cyclically adjacent odd run B
    (neither containing the designated block): both become even, so exactly p-2 odd runs remain and
    their labels stay distinct.  Breaks ONLY the run-count premise."""
    L = len(runs)
    N = len(word)
    blockpos = {block_start, (block_start + 2) % N}
    options = []
    for ri, r in enumerate(runs):
        if r['length'] % 2 == 0 or r['length'] < 3 or blockpos & set(r['positions']):
            continue
        for d in (1, -1):
            rj = (ri + d) % L
            if runs[rj]['length'] % 2 == 0 or blockpos & set(runs[rj]['positions']):
                continue
            moved = r['positions'][-1] if d == 1 else r['positions'][0]
            options.append((moved, runs[rj]['label'], ri, rj))
    if not options:
        return None
    moved, newlabel, ri, rj = rng.choice(options)
    w = list(word)
    w[moved] = (newlabel, 1)
    return w, {'moved_index': moved, 'from_run': ri, 'to_run': rj, 'new_label': newlabel}


def run_mutation_bypass(p, w, block_start):
    """Ignore the premise, rebuild runs, and try the recipe on the designated block."""
    runs = projection_runs(p, w)
    blocks = find_fourblocks(p, w, runs)
    if block_start not in blocks:
        return 'BLOCK_LOST'
    try:
        sel, info = recipe_selector(p, w, runs, block_start)
    except ControlError as exc:
        return str(exc)
    return 'RECIPE_SUCCEEDED_IDENTITY' if verify_identity(p, w, sel) else 'RECIPE_SUCCEEDED_NONIDENTITY'


# ------------------------------------------------------------ deterministic adversarial families
def adversarial_word(p, kind):
    """Deterministic premise-breaking words on which the section-3 recipe must fail for u-v=1.
    kind='labels':   p odd runs whose labels in cut order are 1,2,...,p-1,p-1 (label 0 missing; the
                     duplicate run is separated from its twin by an even run of label 0, length 2).
    kind='runcount': p-2 odd runs with distinct labels 1,...,p-2 and one even run (label 0, length 4).
    In both, the representatives' labels are non-decreasing integers in [1,p-1] in cut order, so no
    earlier-minus-later difference is congruent to 1; the block has u=1, v=0."""
    if kind == 'labels':
        spec = [(1, 2 * p - 3)] + [(c, 1) for c in range(2, p)] + [(0, 2), (p - 1, 1)]
    elif kind == 'runcount':
        spec = [(1, 2 * p - 3)] + [(c, 1) for c in range(2, p - 1)] + [(0, 4)]
    else:
        raise ValueError(kind)
    refl = [c for c, L in spec for _ in range(L)]
    if len(refl) != 3 * p - 2:
        raise ControlError('ADVERSARIAL_F')
    word = [(1, 1), (1, 0), (1, 1), (0, 0)] + [(c, 1) for c in refl[2:]] + [(0, 0)] * (p - 1)
    if len(word) != 4 * p - 1:
        raise ControlError('ADVERSARIAL_N')
    return word


def adversarial_control(p, kind, expected_reject):
    w = adversarial_word(p, kind)
    try:
        check_premise(p, w)
        premise = 'SURVIVED'
    except ControlError as exc:
        premise = str(exc)
    runs = projection_runs(p, w)
    odd = [r for r in runs if r['length'] % 2]
    bypass = run_mutation_bypass(p, w, 0)
    return {'premise_check': premise, 'premise_rejected_as_intended': premise == expected_reject,
            'odd_runs': len(odd), 'distinct_odd_labels': len({r['label'] for r in odd}),
            'rep_labels_cut_order': [r['label'] for r in runs if r['length'] % 2],
            'block_t': 1, 'recipe_bypass': bypass,
            'recipe_failed_as_intended': bypass == 'NO_DIRECTED_PAIR',
            'dp_some_2p_identity_selector_exists_informational': exists_identity_subsequence(p, w, 2 * p),
            'word_letters_(x,e)': w}


# ------------------------------------------------------------ exhaustive p=3
def exhaustive_p3(rng, skip_full_dp=False):
    p, N, F, R = 3, 11, 7, 4
    stats = {'label_sequences_total': 3 ** F, 'label_sequences_meeting_premise': 0,
             'skeletons_meeting_premise': 0, 'skeletons_with_block': 0,
             'recipe_cases': 0, 'recipe_identity': 0, 'branches': {},
             'dp_cases_others_zero': 0, 'dp_identity_others_zero': 0,
             'dp_sample_random_others': 0, 'dp_sample_identity': 0,
             'dp_all_rotation_assignments_words': 0, 'dp_all_rotation_assignments_identity': 0}
    for labels in itertools.product(range(p), repeat=F):
        proj = [(c, 1) for c in labels]
        try:
            runs0 = projection_runs(p, proj)
        except ControlError:
            continue
        odd = [r for r in runs0 if r['length'] % 2]
        if len(odd) != p or len({r['label'] for r in odd}) != p:
            continue
        stats['label_sequences_meeting_premise'] += 1
        for rotpos in itertools.combinations(range(N), R):
            rotset = set(rotpos)
            word = []
            it = iter(labels)
            for i in range(N):
                word.append((0, 0) if i in rotset else (next(it), 1))
            runs = check_premise(p, word)
            stats['skeletons_meeting_premise'] += 1
            blocks = find_fourblocks(p, word, runs)
            if not blocks:
                continue
            stats['skeletons_with_block'] += 1
            if not skip_full_dp:
                for vals in itertools.product(range(p), repeat=R):
                    w = list(word)
                    for i, x in zip(rotpos, vals):
                        w[i] = (x, 0)
                    stats['dp_all_rotation_assignments_words'] += 1
                    if exists_identity_subsequence(p, w, 2 * p):
                        stats['dp_all_rotation_assignments_identity'] += 1
            n_even = sum(1 for r in runs if r['length'] % 2 == 0)
            for s in blocks:
                for u in range(p):
                    for v in range(p):
                        w = list(word)
                        w[(s + 1) % N] = (u, 0)
                        w[(s + 3) % N] = (v, 0)
                        sel, info = recipe_selector(p, w, runs, s)
                        stats['recipe_cases'] += 1
                        key = ('t0' if info['t'] == 0 else 'tnz') + '/e' + str(n_even)
                        stats['branches'][key] = stats['branches'].get(key, 0) + 1
                        if verify_identity(p, w, sel):
                            stats['recipe_identity'] += 1
                        stats['dp_cases_others_zero'] += 1
                        if exists_identity_subsequence(p, w, 2 * p):
                            stats['dp_identity_others_zero'] += 1
                        if rng.random() < 0.05:
                            for i in rotpos:
                                if i not in ((s + 1) % N, (s + 3) % N):
                                    w[i] = (rng.randrange(p), 0)
                            stats['dp_sample_random_others'] += 1
                            if exists_identity_subsequence(p, w, 2 * p):
                                stats['dp_sample_identity'] += 1
    return stats


def encode(word):
    return [2 * x + e for x, e in word]


# ------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--results', required=True)
    ap.add_argument('--fixtures', required=True)
    ap.add_argument('--seed', type=int, default=20261028139)
    ap.add_argument('--per-p', type=int, default=400)
    ap.add_argument('--skip-exhaustive', action='store_true')
    ap.add_argument('--skip-exhaustive-full-dp', action='store_true')
    args = ap.parse_args()
    for path in (args.results, args.fixtures):
        if os.path.exists(path):
            raise SystemExit('refusing to overwrite ' + path)
    t_start = clock()
    wall0 = time.time()
    with open(os.path.abspath(__file__), 'rb') as fh:
        self_sha = hashlib.sha256(fh.read()).hexdigest()
    rng = random.Random(args.seed)
    primes = [3, 5, 7, 11, 13]
    report = {'kind': 'REVIEWER_EXACT_FINITE_CONTROL_F139', 'script_sha256': self_sha,
              'python': sys.version, 'platform': platform.platform(), 'seed': args.seed,
              'clock_start_utc': t_start, 'group_selftest': {}, 'positive': {}, 'mutation_labels': {},
              'mutation_runcount': {}, 'verifier_sensitivity': {}, 'exhaustive_p3': None}
    fixtures = {'seed': args.seed, 'convention': '(x,e) = rho^x sigma^e; sigma_c=(c,1); rho_u=(u,0)',
                'word_encoding': 'each letter (x,e) is stored as the integer 2*x+e; indices are 0-based original positions',
                'positive': {}, 'mutation_labels': {}, 'mutation_runcount': {}}
    for p in primes:
        report['group_selftest'][str(p)] = group_selftest(p)
        st = {'words': 0, 'blocks_tested': 0, 'recipe_identity': 0, 'recipe_failures': 0,
              'dp_identity': 0, 'u_ne_v_words': 0, 'u_eq_v_words': 0, 'blocks_t_nonzero': 0,
              'blocks_t_zero': 0, 'n_even_hist': {}, 'pairs_available_always_p_minus_2': True,
              'blocks_wrapping_linear_end': 0, 'max_blocks_in_word': 0}
        fx = []
        sens = {'corruptions': 0, 'nonidentity': 0}
        ml = {'attempted': 0, 'mutable': 0, 'rejected_intended': 0, 'rejected_other': 0, 'survived': 0,
              'bypass_t_nonzero': {}, 'bypass_t_zero': {}, 'dp_identity_on_mutant': 0}
        mr = dict(ml)
        mr['bypass_t_nonzero'], mr['bypass_t_zero'] = {}, {}
        fxl, fxr = [], []
        n_even_max = min(3, p - 2)
        for n in range(args.per_p):
            want_unequal = (n % 5) != 0           # 80% unequal, 20% equal
            n_even = rng.randrange(n_even_max + 1)
            word, meta = produce(p, rng, want_unequal, n_even)
            runs = check_premise(p, word)
            if sum(1 for r in runs if r['length'] % 2 == 0) != n_even:
                raise ControlError('PRODUCER_EVEN_COUNT')
            blocks = find_fourblocks(p, word, runs)
            if not blocks:
                raise ControlError('PRODUCER_NO_BLOCK')
            st['words'] += 1
            st['n_even_hist'][str(n_even)] = st['n_even_hist'].get(str(n_even), 0) + 1
            st['u_ne_v_words' if meta['u'] != meta['v'] else 'u_eq_v_words'] += 1
            st['max_blocks_in_word'] = max(st['max_blocks_in_word'], len(blocks))
            N = len(word)
            sels = []
            for s in blocks:
                st['blocks_tested'] += 1
                if s + 3 >= N:
                    st['blocks_wrapping_linear_end'] += 1
                try:
                    sel, info = recipe_selector(p, word, runs, s, drop_choice=rng.randrange(10 ** 6))
                except ControlError as exc:
                    st['recipe_failures'] += 1
                    sels.append({'block_start': s, 'error': str(exc)})
                    continue
                if info['pairs_available'] != p - 2:
                    st['pairs_available_always_p_minus_2'] = False
                st['blocks_t_nonzero' if info['t'] else 'blocks_t_zero'] += 1
                ok = verify_identity(p, word, sel)
                st['recipe_identity'] += ok
                if not ok:
                    raise ControlError('RECIPE_SELECTOR_NOT_IDENTITY p=%d word=%r s=%d' % (p, word, s))
                sels.append({'block_start': s, 't': info['t'], 'selector': sel})
                # verifier sensitivity: corrupt one index
                for _ in range(2):
                    others = [i for i in range(N) if i not in sel]
                    bad = sorted(set(sel) - {rng.choice(sel)} | {rng.choice(others)})
                    sens['corruptions'] += 1
                    sens['nonidentity'] += (not verify_identity(p, word, bad))
            if exists_identity_subsequence(p, word, 2 * p):
                st['dp_identity'] += 1
            fx.append({'word': encode(word), 'meta': meta, 'selectors': sels})
            # ----- mutation 1: labels
            ml['attempted'] += 1
            m = mutate_labels(p, word, runs, rng)
            if m is not None:
                w, minfo = m
                ml['mutable'] += 1
                try:
                    check_premise(p, w)
                    ml['survived'] += 1
                    verdict = 'SURVIVED'
                except ControlError as exc:
                    verdict = str(exc)
                    if verdict == 'PREMISE_LABELS_NOT_DISTINCT':
                        ml['rejected_intended'] += 1
                    else:
                        ml['rejected_other'] += 1
                s0 = blocks[0]
                t0 = (w[(s0 + 1) % N][0] - w[(s0 + 3) % N][0]) % p
                res = run_mutation_bypass(p, w, s0)
                bucket = ml['bypass_t_nonzero'] if t0 else ml['bypass_t_zero']
                bucket[res] = bucket.get(res, 0) + 1
                ml['dp_identity_on_mutant'] += exists_identity_subsequence(p, w, 2 * p)
                fxl.append({'word': encode(w), 'mutation': minfo, 'premise_check': verdict, 'bypass': res})
            # ----- mutation 2: run count
            mr['attempted'] += 1
            m = mutate_runcount(p, word, runs, blocks[0], rng)
            if m is not None:
                w, minfo = m
                mr['mutable'] += 1
                try:
                    check_premise(p, w)
                    mr['survived'] += 1
                    verdict = 'SURVIVED'
                except ControlError as exc:
                    verdict = str(exc)
                    if verdict == 'PREMISE_ODD_RUN_COUNT':
                        mr['rejected_intended'] += 1
                    else:
                        mr['rejected_other'] += 1
                runs_m = projection_runs(p, w)
                odd_m = [r for r in runs_m if r['length'] % 2]
                if len(odd_m) != p - 2 or len({r['label'] for r in odd_m}) != p - 2:
                    raise ControlError('MUTATION_RUNCOUNT_SHAPE')
                s0 = blocks[0]
                t0 = (w[(s0 + 1) % N][0] - w[(s0 + 3) % N][0]) % p
                res = run_mutation_bypass(p, w, s0)
                bucket = mr['bypass_t_nonzero'] if t0 else mr['bypass_t_zero']
                bucket[res] = bucket.get(res, 0) + 1
                mr['dp_identity_on_mutant'] += exists_identity_subsequence(p, w, 2 * p)
                fxr.append({'word': encode(w), 'mutation': minfo, 'premise_check': verdict, 'bypass': res})
        report['positive'][str(p)] = st
        report['verifier_sensitivity'][str(p)] = sens
        report['mutation_labels'][str(p)] = ml
        report['mutation_runcount'][str(p)] = mr
        fixtures['positive'][str(p)] = fx
        fixtures['mutation_labels'][str(p)] = fxl
        fixtures['mutation_runcount'][str(p)] = fxr
    report['adversarial_labels'] = {str(p): adversarial_control(p, 'labels', 'PREMISE_LABELS_NOT_DISTINCT')
                                    for p in primes}
    report['adversarial_runcount'] = {str(p): adversarial_control(p, 'runcount', 'PREMISE_ODD_RUN_COUNT')
                                      for p in primes}
    if not args.skip_exhaustive:
        report['exhaustive_p3'] = exhaustive_p3(rng, args.skip_exhaustive_full_dp)
    report['wall_seconds'] = round(time.time() - wall0, 3)
    with open(args.fixtures, 'x', encoding='utf-8') as out:
        json.dump(fixtures, out, sort_keys=True, separators=(',', ':'))
        out.write('\n')
    with open(args.fixtures, 'rb') as fh:
        report['fixtures_sha256'] = hashlib.sha256(fh.read()).hexdigest()
    report['fixtures_path'] = os.path.abspath(args.fixtures)
    report['clock_end_utc'] = clock()
    with open(args.results, 'x', encoding='utf-8') as out:
        json.dump(report, out, sort_keys=True, indent=1)
        out.write('\n')
    print(json.dumps({k: report[k] for k in ('positive', 'mutation_labels', 'mutation_runcount',
                                              'verifier_sensitivity', 'exhaustive_p3', 'wall_seconds',
                                              'clock_start_utc', 'clock_end_utc', 'script_sha256',
                                              'fixtures_sha256')}, sort_keys=True))
    for kind in ('adversarial_labels', 'adversarial_runcount'):
        print(kind, json.dumps({q: {k: v for k, v in r.items() if k != 'word_letters_(x,e)'}
                                for q, r in report[kind].items()}, sort_keys=True))


if __name__ == '__main__':
    main()
