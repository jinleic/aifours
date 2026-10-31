#!/usr/bin/env python3
"""Probe: pure-directness exact cover with MRV element choice (reviewer-written)."""
import sys, time
from math import gcd

def mrv_cover(P, n, forced, node_cap=400_000, pclasses=None):
    P = sorted({p % n for p in P})
    full = (1 << n) - 1
    masks = [0] * n
    for q in range(n):
        m = 0
        for p in P:
            m |= 1 << ((p + q) % n)
        masks[q] = m
    covered = 0
    Q = []
    for q in forced:
        if masks[q] & covered:
            return None, 0, False
        covered |= masks[q]
        Q.append(q)
    nodes = [0]
    capped = [False]

    def rec(cov, avail):
        nodes[0] += 1
        if nodes[0] > node_cap:
            capped[0] = True
            return False
        if cov == full:
            return True
        # MRV: uncovered element with fewest available translates
        best_e, best_c, best_qs = -1, 10 ** 9, None
        unc = ~cov & full
        e = 0
        while unc:
            low = unc & -unc
            e = low.bit_length() - 1
            unc ^= low
            qs = [(e - p) % n for p in P]
            qs = [q for q in qs if q in avail]
            c = len(qs)
            if c < best_c:
                best_e, best_c, best_qs = e, c, qs
                if c <= 1:
                    break
        if best_c == 0:
            return False
        for q in best_qs:
            m = masks[q]
            if pclasses and any(gcd(q - r, n) in pclasses for r in Q):
                continue
            Q.append(q)
            nav = {r for r in avail if masks[r] & m == 0}
            if rec(cov | m, nav):
                return True
            Q.pop()
        return False

    avail = {q for q in range(n) if masks[q] & covered == 0}
    ok = rec(covered, avail)
    return (sorted(Q) if ok else None), nodes[0], capped[0]

if __name__ == "__main__":
    n = 660
    Y = [0, 1, 7, 13, 14]
    cap = int(sys.argv[1]) if len(sys.argv) > 1 else 400_000
    # positive control: interval tile
    q, nodes, capped = mrv_cover(list(range(10)), n, [0], node_cap=cap)
    print("pos interval10:", q is not None, nodes, capped)
    # negative control: {0,1,3} in Z_60
    q, nodes, capped = mrv_cover([0, 1, 3], 60, [0], node_cap=cap)
    print("neg 013 Z60:", q is None, nodes, capped)
    for P in ((0, 3, 8, 11, 132, 264, 275, 396, 407, 539), (0, 3, 8, 11, 33, 88, 198, 253, 418, 473, 583, 638),
              (0, 3, 8, 11, 63, 68, 123, 128, 183, 188, 243, 248, 303, 368, 423, 428, 483, 488, 543, 548, 603, 608)):
        t = time.time()
        q, nodes, capped = mrv_cover(P, n, Y, node_cap=cap)
        print(len(P), "pure MRV ->", "FOUND" if q is not None else ("CAPPED" if capped else "NONE"), "nodes", nodes, round(time.time() - t, 1), "s")
        sys.stdout.flush()
