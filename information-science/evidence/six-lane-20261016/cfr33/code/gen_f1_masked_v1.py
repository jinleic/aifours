#!/usr/bin/env python3
"""Random odd normalised orthomorphisms f_1 of Z_N from a value-mask family (lane cfr33/cfr27, worker InfoCFR27Lift).

Usage: gen_f1_masked_v1.py N FAMILY SEED COUNT OUT        (OUT written with mode 'x'; one line per f_1: M values a = 1..M)
Odd map on half-columns a = 1..M (M = (N-1)/2), values v in 1..N-1 with f(-a) = -f(a); orthomorphism = the +- classes
of v and of v - a are each all distinct. FAMILY restricts the allowed values per half-column a:
  any | pres3Z (v = 0 mod 3 iff a = 0 mod 3) | lin3 (v = -a mod 3)
  lin9on3Z:c (v = c a mod 9 when 3 | a)          lin9onU:c (v = c a mod 9 when 3 does not divide a)
  lin3+lin9on3Z:c (lin3 and lin9on3Z:c)          pres3Z+lin9onU:c
Randomised DFS (smallest candidate set first, random order); restarts until COUNT distinct maps are found. Not uniform.
"""
import random, sys


def main():
    N, fam, seed, count, out = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    M = (N - 1) // 2
    cls = lambda v: min(v % N, (-v) % N)
    rng = random.Random(seed)

    def allowed(a, v):
        parts = fam.split("+")
        for p in parts:
            if p == "any":
                continue
            if p == "pres3Z":
                if (a % 3 == 0) != (v % 3 == 0):
                    return False
            elif p == "lin3":
                if (v + a) % 3 != 0:
                    return False
            elif p.startswith("lin9on3Z:"):
                c = int(p.split(":")[1])
                if a % 3 == 0 and (v - c * a) % 9 != 0:
                    return False
            elif p.startswith("lin9onU:"):
                c = int(p.split(":")[1])
                if a % 3 != 0 and (v - c * a) % 9 != 0:
                    return False
            else:
                raise SystemExit("unknown family part " + p)
        return True

    cand0 = {a: [v for v in range(1, N) if allowed(a, v) and cls(v) != 0 and cls(v - a) != 0] for a in range(1, M + 1)}
    found = set()
    lines = []
    tries = 0
    sys.setrecursionlimit(10000)
    while len(found) < count and tries < 100000:
        tries += 1
        val = {}
        used1, used2 = set(), set()
        budget = [20000]

        def rec():
            if len(val) == M:
                return True
            budget[0] -= 1
            if budget[0] < 0:
                return False
            best, bl = None, None
            for a in range(1, M + 1):
                if a in val:
                    continue
                l = [v for v in cand0[a] if cls(v) not in used1 and cls(v - a) not in used2]
                if best is None or len(l) < len(bl):
                    best, bl = a, l
                    if not l:
                        return False
            rng.shuffle(bl)
            for v in bl:
                val[best] = v
                used1.add(cls(v)); used2.add(cls(v - best))
                if rec():
                    return True
                used1.discard(cls(v)); used2.discard(cls(v - best))
                del val[best]
            return False

        if rec():
            t = tuple(val[a] for a in range(1, M + 1))
            if t not in found:
                found.add(t)
                lines.append(" ".join(map(str, t)))
    with open(out, "x") as fh:
        fh.write("\n".join(lines) + "\n")
    print("family %s seed %d found %d tries %d" % (fam, seed, len(found), tries))


if __name__ == "__main__":
    main()
