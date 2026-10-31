#!/usr/bin/env python3
"""Exhaustive p=3 brute force for the F=3p-2 band (no proof logic used).

Every linear word over D_6 with exactly F=7 reflections and R=4 rotations is
covered: reflection labels normalised by the translation automorphism
sigma_x -> sigma_(x+v), rho_x -> rho_x (first reflection label 0), all 330
rotation placements and all 81 rotation labelings.  Words with R>4 contain a
subword with R=4 and the same reflections, so R=4 suffices for R>=p+1.

The only computation is an order-preserving subsequence DP over the group,
tracking (selected count, number of selected rotations) -> bitmask of
reachable products.  It records (a) reflection-only identity 2p selections,
(b) identity 2p selections with exactly two rotations, (c) any identity 2p
selection.
"""
import argparse
import hashlib
import itertools
import json

P = 3
TARGET = 2 * P
FULL = (1 << P) - 1


def rotl(m, s):
    s %= P
    return ((m << s) | (m >> (P - s))) & FULL if s else m


def right_mult(mask, y, b):
    r = mask & FULL
    f = mask >> P
    if b == 0:   # (x,0)(y,0)=(x+y,0); (x,1)(y,0)=(x-y,1)
        return rotl(r, y) | (rotl(f, -y) << P)
    # (x,0)(y,1)=(x+y,1); (x,1)(y,1)=(x-y,0)
    return rotl(f, -y) | (rotl(r, y) << P)


TABLE = {(y, b): [right_mult(m, y, b) for m in range(1 << (2 * P))] for y in range(P) for b in (0, 1)}


def reachable(word, max_rot):
    masks = [[0] * (max_rot + 1) for _ in range(TARGET + 1)]
    masks[0][0] = 1
    for y, b in word:
        tab = TABLE[(y, b)]
        add = 0 if b else 1
        for k in range(TARGET - 1, -1, -1):
            row = masks[k]
            nxt = masks[k + 1]
            for r in range(max_rot - add, -1, -1):
                m = row[r]
                if m:
                    nxt[r + add] |= tab[m]
    return masks[TARGET]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    n = 4 * P - 1
    placements = list(itertools.combinations(range(n), P + 1))
    labelings = list(itertools.product(range(P), repeat=P + 1))
    lists = ref_lists = ref_fail_lists = 0
    words_ref_covered = words_checked = two_rot = any_sel = 0
    failures_two = []
    failures_any = []
    min_rot_hist = {}
    for rest in itertools.product(range(P), repeat=3 * P - 3):
        refl = (0,) + rest
        lists += 1
        if reachable([(y, 1) for y in refl], 0)[0] & 1:
            ref_lists += 1
            words_ref_covered += len(placements) * len(labelings)
            continue
        ref_fail_lists += 1
        for pos in placements:
            posset = set(pos)
            for lab in labelings:
                it_r = iter(lab)
                it_f = iter(refl)
                word = [((next(it_r), 0) if i in posset else (next(it_f), 1)) for i in range(n)]
                words_checked += 1
                fin = reachable(word, 2)
                if fin[0] & 1:
                    raise ValueError('REF_DETECTED_IN_REF_FAILING_LIST')
                if fin[2] & 1:
                    two_rot += 1
                    min_rot_hist[2] = min_rot_hist.get(2, 0) + 1
                    continue
                if len(failures_two) < 20:
                    failures_two.append({'reflections': refl, 'rotation_positions': pos, 'rotation_labels': lab})
                full = reachable(word, TARGET)
                hit = [r for r in range(TARGET + 1) if full[r] & 1]
                if hit:
                    any_sel += 1
                    min_rot_hist[min(hit)] = min_rot_hist.get(min(hit), 0) + 1
                elif len(failures_any) < 20:
                    failures_any.append({'reflections': refl, 'rotation_positions': pos, 'rotation_labels': lab})
    result = {
        'result': 'PASS_EXHAUSTIVE_P3_BAND' if not failures_two and not failures_any else 'FAIL_EXHAUSTIVE_P3_BAND',
        'p': P, 'F': 3 * P - 2, 'R': P + 1, 'word_length': n,
        'normalised_reflection_lists': lists, 'ref_lists': ref_lists, 'ref_failing_lists': ref_fail_lists,
        'words_covered_by_REF_list': words_ref_covered, 'words_checked_with_ref_failing_list': words_checked,
        'two_rotation_selector_found': two_rot, 'other_selector_found': any_sel,
        'min_rotation_histogram_for_ref_failing_words': {str(k): v for k, v in sorted(min_rot_hist.items())},
        'failures_without_two_rotation_selector': failures_two, 'failures_without_any_selector': failures_any,
        'symmetry_used': 'translation of reflection labels only (automorphism); R=4 suffices for R>=4 by subword monotonicity',
        'scope': 'finite brute force at p=3; independent of the written proof; not a proof for other p',
    }
    data = json.dumps(result, sort_keys=True, indent=2) + '\n'
    with open(args.output, 'x', encoding='utf-8') as out:
        out.write(data)
    print(json.dumps({k: result[k] for k in ('result', 'normalised_reflection_lists', 'ref_failing_lists',
                                                'words_checked_with_ref_failing_list', 'two_rotation_selector_found',
                                                'other_selector_found', 'min_rotation_histogram_for_ref_failing_words')},
                     sort_keys=True))


if __name__ == '__main__':
    main()
