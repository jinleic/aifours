#!/usr/bin/env python3
"""Six/eight-node direct phase-word classification (K3). Stdlib only.

Semantics identical to K1 (frontier-20261029-strict-certificate-five-node-
phase-independent-kernel-v1.py): classes 0..6 with sign pairs
(++),(-+),(--),(+-),(++),(-+),(--); a word is admissible when BOTH parity
sign words contain the oriented subsequence (-,+,-,+) and every pair i<j
satisfies q_j >= q_i - 1, and q_j >= q_i + 2 whenever both parity signs
differ. Validates by reproducing K1's m=5 output (676 alpha-pass, exactly
the three words). New outputs: m=6,7,8 admissible words and, per word,
whether some 5-node O-subsupport is strictly alternating (the 5-node
annihilator-ray admissibility datum). Integer arithmetic only; author-run
in one Eval host, not independent review.
"""
from itertools import product, combinations
import json

PAIRS = {0: (1, 1), 1: (-1, 1), 2: (-1, -1), 3: (1, -1), 4: (1, 1), 5: (-1, 1), 6: (-1, -1)}
TARGET = (-1, 1, -1, 1)


def contains(word):
    it = iter(word)
    return all(s in it for s in TARGET)


def beta_ok(seq):
    for i in range(len(seq)):
        qi, pi = seq[i], PAIRS[seq[i]]
        for j in range(i + 1, len(seq)):
            qj, pj = seq[j], PAIRS[seq[j]]
            if qj < qi - 1:
                return False
            if pi[0] != pj[0] and pi[1] != pj[1] and qj < qi + 2:
                return False
    return True


def is_alt(w):
    return all(w[i] == -w[i + 1] for i in range(len(w) - 1))


def classify(m):
    alpha, full = 0, []
    for seq in product(range(7), repeat=m):
        E = tuple(PAIRS[q][0] for q in seq)
        O = tuple(PAIRS[q][1] for q in seq)
        if not (contains(E) and contains(O)):
            continue
        alpha += 1
        if beta_ok(seq):
            full.append((seq, O))
    return alpha, full


def main():
    out = {"validation_m5": None, "census": {}}
    alpha5, full5 = classify(5)
    words5 = sorted(list(w) for w, _ in full5)
    assert alpha5 == 676 and words5 == [[2, 1, 3, 2, 4], [2, 1, 3, 5, 4], [2, 4, 3, 5, 4]], "K1 mismatch"
    out["validation_m5"] = {"alpha_pass": alpha5, "words": words5}
    for m in (6, 7, 8):
        alpha, full = classify(m)
        recs, n_alt = [], 0
        for w, O in full:
            alt5 = any(is_alt(s) for s in combinations(O, 5))
            n_alt += alt5
            recs.append({"word": list(w), "O": ''.join('+' if v > 0 else '-' for v in O), "alt5": alt5})
        out["census"][str(m)] = {
            "alpha_pass": alpha, "admissible": len(recs),
            "with_alternating_5_support": n_alt,
            "circuit_only": len(recs) - n_alt,
            "distinct_O_words": len(set(r["O"] for r in recs)),
            "records": recs,
        }
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
