#!/usr/bin/env python3
"""Proposition SH-ROT check (rotation slice 2026-10-18): w_p = rho_(-3) sigma_2^(2p-5) rho_1^(2p-1) sigma_0, length 4p-4,
non-rigid for p >= 5.  Fresh raw DP must find NO identity 2p-subword.  Also: every one-letter insertion (any letter,
any position) giving a length-(4p-3) word is tested; non-rigid avoiders among them are counted (expected 0 if ROT holds
already at length 4p-3).  Usage: sharp_rot_family_v1.py PMAX PINS  (insertion test only for p <= PINS)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rawdp  # noqa: E402
from sharp_search_v1 import nonrigid  # noqa: E402

def fam(p):
    return [('r', (-3) % p)] + [('s', 2)] * (2 * p - 5) + [('r', 1)] * (2 * p - 1) + [('s', 0)]

def main():
    pmax, pins = int(sys.argv[1]), int(sys.argv[2])
    out = []
    for p in [q for q in range(5, pmax + 1) if all(q % d for d in range(2, q))]:
        w = fam(p)
        rec = {'p': p, 'len': len(w), 'nonrigid': nonrigid(w, p), 'avoider': not rawdp.has_identity(w, p, 2 * p)}
        if p <= pins:
            nr_av = tot = 0
            for pos in range(len(w) + 1):
                for kind in 'rs':
                    for v in range(p):
                        u = w[:pos] + [(kind, v)] + w[pos:]
                        tot += 1
                        if nonrigid(u, p) and not rawdp.has_identity(u, p, 2 * p):
                            nr_av += 1
            rec['insertions'] = tot
            rec['nonrigid_avoiders_at_4p-3'] = nr_av
        out.append(rec)
        print(json.dumps(rec), flush=True)

if __name__ == '__main__':
    main()
