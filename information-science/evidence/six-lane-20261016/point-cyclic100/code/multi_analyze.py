#!/usr/bin/env python3
"""multi_analyze.py -- expand and check additional R1 seeds and sort them into affine equivalence classes
(x -> u x + t, u a unit mod v) of the pair (design, resolution); informational only (not acceptance).
Usage: multi_analyze.py OUTDIR SEED...
"""
import math
import os
import subprocess
import sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def classes_of(cert):
    lines = open(cert).read().rstrip("\n").split("\n")
    v = int(lines[0].split()[1])
    cl = {}
    for line in lines[1:]:
        t = list(map(int, line.split()))
        cl.setdefault(t[0], []).append(tuple(t[1:]))
    return v, frozenset(frozenset(P) for P in cl.values())


def main(argv):
    out = argv[1]
    os.makedirs(out, exist_ok=True)
    reps = []
    for seed in argv[2:]:
        cert = os.path.join(out, os.path.basename(seed).replace(".seed", "") + ".cert")
        p1 = subprocess.run([sys.executable, os.path.join(LANE, "code", "pc_expand.py"), seed, cert],
                            capture_output=True, text=True)
        p2 = subprocess.run([sys.executable, os.path.join(LANE, "code", "pc_check.py"), cert],
                            capture_output=True, text=True)
        verdict = p2.stdout.strip().split("\n")[-1]
        v, R = classes_of(cert)
        units = [u for u in range(1, v) if math.gcd(u, v) == 1]
        found = None
        for idx, (name, R0) in enumerate(reps):
            for u in units:
                for t in range(v):
                    img = frozenset(frozenset(tuple(sorted((u * x + t) % v for x in B)) for B in P) for P in R)
                    if img == R0:
                        found = (idx, u, t)
                        break
                if found:
                    break
            if found:
                break
        if not found:
            reps.append((seed, R))
        print(f"{seed}: expand_rc={p1.returncode} check={verdict} "
              f"{'new class #%d' % (len(reps) - 1) if not found else 'equivalent to #%d (u=%d, t=%d)' % found}")
    print(f"{len(argv) - 2} seeds, {len(reps)} affine classes of (design, resolution)")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
