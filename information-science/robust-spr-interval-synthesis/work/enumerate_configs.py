"""Combinatorial census of alternation-certificate configurations (generalizing the quintic
manuscript's Section 5.3 / Appendix A enumeration to any n).  Exploratory bookkeeping only.

Model (positive nodes only, numerator of exact degree n, m = n+1 nodes, no mass at infinity):
  * numerator components E_b, O_b have interlacing positive roots splitting (0, inf) into
    intervals I_0..I_{n-1}; on I_q, (sgn E_b, sgn O_b) = quadrant pattern q mod 4 with
    patterns 0:(+,+) 1:(-,+) 2:(-,-) 3:(+,-); the minimizing (contact) vertex there is
    D, A, B, C for q mod 4 = 0, 1, 2, 3  (A=(E+,O-), B=(E+,O+), C=(E-,O+), D=(E-,O-));
  * node i (1-based) lies in I_{q_i}, q nondecreasing, orientation sigma_i = c (-1)^{m-i};
  * the contact vertex's sign pattern is (sigma sgn O_b, -sigma sgn E_b)  (rigidity, eq. (4.8));
  * denominator regions r = 0..2(n-1): even r allows only quadrant r/2 (mod 4), odd r allows
    quadrants (r-1)/2 and (r+1)/2; region indices along the nodes must be nondecreasing
    (greedy smallest-region rule of the quintic manuscript, which loses no sequence);
  * multiplicity: a vertex has at most floor(n/2) positive contacts (its pairing polynomial is
    nonnegative of degree n).
Usage: python enumerate_configs.py NMAX
Prints, for each n, the number of q-sequences passing region order, and passing multiplicity.
"""
from __future__ import annotations

import itertools
import sys

PAT = {0: (1, 1), 1: (-1, 1), 2: (-1, -1), 3: (1, -1)}
QUAD = {v: k for k, v in PAT.items()}
VERTEX = {0: "D", 1: "A", 2: "B", 3: "C"}


def region_ok(seq_quads, n):
    r = 0
    rmax = 2 * (n - 1)
    for qd in seq_quads:
        while r <= rmax:
            allowed = {(r // 2) % 4} if r % 2 == 0 else {((r - 1) // 2) % 4, ((r + 1) // 2) % 4}
            if qd in allowed:
                break
            r += 1
        if r > rmax:
            return False
    return True


def census(n):
    m = n + 1
    out = {}
    for c in (1, -1):
        n_region = n_mult = 0
        survivors = []
        for q in itertools.combinations_with_replacement(range(n), m):
            quads = []
            verts = []
            for i, qi in enumerate(q, start=1):
                sig = c * (-1) ** (m - i)
                sE, sO = PAT[qi % 4]
                quads.append(QUAD[(sig * sO, -sig * sE)])
                verts.append(VERTEX[qi % 4])
            if not region_ok(quads, n):
                continue
            n_region += 1
            if max(verts.count(v) for v in "ABCD") > n // 2:
                continue
            n_mult += 1
            survivors.append(("".join(map(str, q)), "".join(verts)))
        out[c] = (n_region, n_mult, survivors)
    return out


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    for n in range(4, nmax + 1):
        res = census(n)
        for c in (1, -1):
            nr, nm, surv = res[c]
            ex = ", ".join(f"{a}:{b}" for a, b in surv[:6])
            print(f"n={n} c={c:+d}: region-order {nr}, + multiplicity {nm}; e.g. {ex}")


if __name__ == "__main__":
    main()
