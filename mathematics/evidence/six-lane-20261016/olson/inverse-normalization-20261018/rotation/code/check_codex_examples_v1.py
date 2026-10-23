#!/usr/bin/env python3
"""Raw-DP smoke of the explicit words in the Codex bundle-1 review (R/olson-rotation-bundle1-codex-v1.note.md).
Not a premise.  Positive controls (claimed avoiders must have NO identity 2p-subword) and negative controls
(words claimed solvable must HAVE one; the witness is re-multiplied).
  F1: p=5, w  = r3 r1^6 s0^9 r-1 s0   (claimed SOLVABLE by Theorem SH3+-; length 18 = 4p-2)
      p=5, u° = r1^9 s0^7 r-1 s0      (claimed AVOIDER: Lemma U without 'w avoids' is false)
  F3: p=5, r1^9 s0^8                  (claimed AVOIDER, length 17, kappa = 0, FULL, no odd block)
  F4: p=5..13, r3 s0^(2p-1) r1^(2p-5) s4 (claimed AVOIDER, length 4p-4, kappa = 0, FULL, E = 2)
Usage: check_codex_examples_v1.py OUT.jsonl
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rawdp

def word(spec):
    out = []
    for kind, val, mult in spec:
        out += [(kind, val)] * mult
    return out

def main():
    rows = []
    cases = [("F1-w", 5, word([('r', 3, 1), ('r', 1, 6), ('s', 0, 9), ('r', -1 % 5, 1), ('s', 0, 1)]), True),
             ("F1-u", 5, word([('r', 1, 9), ('s', 0, 7), ('r', -1 % 5, 1), ('s', 0, 1)]), False),
             ("F3", 5, word([('r', 1, 9), ('s', 0, 8)]), False)]
    for p in (5, 7, 11, 13):
        cases.append(("F4", p, word([('r', 3, 1), ('s', 0, 2 * p - 1), ('r', 1, 2 * p - 5), ('s', 4, 1)]), False))
    # negative control for F4: append one more rho_1 (length 4p-3, E = 2, N + E = 4p-1): ELT0 says it must be solvable
    for p in (5, 7, 11):
        cases.append(("F4+r1", p, word([('r', 3, 1), ('s', 0, 2 * p - 1), ('r', 1, 2 * p - 4), ('s', 4, 1)]), True))
    ok_all = True
    for name, p, w, expect in cases:
        has = rawdp.has_identity(w, p, 2 * p)
        wit = rawdp.witness(w, p, 2 * p) if has else None
        prod = rawdp.product(w, wit, p) if wit else None
        ok = (has == expect) and (not has or prod == (0, 1))
        ok_all &= ok
        rows.append(dict(case=name, p=p, length=len(w), word=rawdp.fmt(w), expect_solvable=expect, has=has,
                         witness=wit, witness_product=prod, ok=ok))
    with open(sys.argv[1], "x") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
        f.write(json.dumps(dict(all_ok=ok_all, n=len(rows))) + "\n")
    print("all_ok", ok_all, [(r["case"], r["p"], r["has"], r["ok"]) for r in rows])

if __name__ == "__main__":
    main()
