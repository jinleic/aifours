"""Positive-side cross-check: d-vectors that DO have interval-feasible lifts (taken from a census dump
SOL lines), full solution sets compared between rstar.phi_solutions and xcheck (theta domain, Lemma GR Ach).
Usage: python3 xcheck_pos.py DUMPFILE p M seed
"""
import sys, re, random, json, time
import rstar, xcheck


def main():
    path, p, M, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    ds = set()
    for line in open(path):
        if not line.startswith("SOL"):
            continue
        m = re.search(r" d=([-\d,]+) ", line)
        ds.add(tuple(int(x) for x in m.group(1).split(",")))
    ds = sorted(ds)
    rng = random.Random(seed)
    smp = rng.sample(ds, min(M, len(ds)))
    t0 = time.time()
    st = {"file": path, "p": p, "distinct_d": len(ds), "sampled": len(smp), "solutions": 0, "mismatches": 0}
    for d in smp:
        S1 = set(rstar.phi_solutions(list(d), p))
        S2 = {xcheck.lifts(list(d), th, p) for th in xcheck.interval_feasible_thetas(list(d), p)}
        st["solutions"] += len(S1)
        if S1 != S2 or not S1:
            st["mismatches"] += 1
            print("MISMATCH", d, len(S1), len(S2), flush=True)
    st["seconds"] = round(time.time() - t0, 1)
    print(json.dumps(st), flush=True)


if __name__ == "__main__":
    main()
