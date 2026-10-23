#!/usr/bin/env python3
"""compare_runs.py -- run and/or compare Impl B (cs_brute) and Impl A (cs_neck) for one (n, R, L), with exact
accounting checks, set agreement, and strict verification of found witnesses (README 1.4-1.6).

Usage:
  compare_runs.py run OUTDIR n R L [JOBS_B] [SECONDS]
      runs B as JOBS_B consecutive equal ranges of [0, 2^L) (sequentially, one process at a time) and A once, writing
      only into OUTDIR (fresh directory), then compares.
  compare_runs.py compare OUTDIR n R L B_PREFIX[,B_PREFIX...] A_PREFIX
      compares existing receipts (B ranges must partition [0, 2^L)); writes OUTDIR/compare.json (OUTDIR fresh).
Checks: every B receipt COMPLETE, B ranges disjoint and covering [0, 2^L) exactly, sum of examined = 2^L; A receipt
COMPLETE with counts_ok 1 and selfcheck_flags 0; the set of lex-minimal rotations of B's covering strings equals A's
covering representatives; |B covering| = sum of A periods; every A representative (up to MAXV) passes verify_cs.py
with --expect n R L.  Nothing is deleted or overwritten.
"""
import json
import os
import subprocess
import sys

CODE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(CODE)
MAXV = 200


def receipt(path):
    d = {}
    for line in open(path):
        k, _, v = line.rstrip("\n").partition(" ")
        d[k] = v
    return d


def lexmin_r(s, L):
    xs = [(s >> i) & 1 for i in range(L)]
    best = None
    for t in range(L):
        r = 0
        for i in range(L):
            r = (r << 1) | xs[(t + i) % L]
        if best is None or r < best:
            best = r
    return best


def compare(out, n, R, L, bpres, apre):
    res = {"n": n, "R": R, "L": L, "B": [], "A": None}
    ok = True
    ranges, examined, bset, bcount = [], 0, set(), 0
    for bp in bpres:
        rb = receipt(bp + ".txt")
        ok &= rb.get("status") == "COMPLETE" and int(rb["n"]) == n and int(rb["R"]) == R and int(rb["L"]) == L
        lo, hi = int(rb["lo"]), int(rb["hi"])
        ranges.append((lo, hi))
        examined += int(rb["examined"])
        found = [int(x, 16) for x in open(bp + ".found").read().split()]
        ok &= len(found) == int(rb["covering"])
        bcount += len(found)
        for s in found:
            bset.add(lexmin_r(s, L))
        res["B"].append({"prefix": bp, "lo": lo, "hi": hi, "examined": int(rb["examined"]),
                         "covering": int(rb["covering"]), "status": rb.get("status"),
                         "seconds": float(rb["seconds"])})
    ranges.sort()
    contiguous = ranges[0][0] == 0 and ranges[-1][1] == 2 ** L and all(
        ranges[i][1] == ranges[i + 1][0] for i in range(len(ranges) - 1))
    ok &= contiguous and examined == 2 ** L
    ra = receipt(apre + ".txt")
    alines = [l.split() for l in open(apre + ".found").read().strip().split("\n") if l.strip()]
    aset = {int(r, 16) for r, _, _ in alines}
    asum = sum(int(p) for _, _, p in alines)
    a_ok = (ra.get("status") == "COMPLETE" and ra.get("counts_ok") == "1" and ra.get("selfcheck_flags", "").startswith("0")
            and int(ra["covering_representatives"]) == len(alines))
    ok &= a_ok
    res["A"] = {"prefix": apre, "status": ra.get("status"), "necklaces": int(ra["necklaces_generated"]),
                "formula": int(ra["necklace_number_formula"]), "sum_of_periods": int(ra["sum_of_periods"]),
                "covering_representatives": len(alines), "seconds": float(ra["seconds"])}
    agree = (bset == aset) and (bcount == asum)
    ok &= agree
    res.update({"B_ranges_partition_0_2L": contiguous, "B_examined_total": examined, "two_to_L": 2 ** L,
                "B_covering_strings": bcount, "B_classes": len(bset), "A_classes": len(aset),
                "A_sum_periods_of_found": asum, "sets_agree": agree})
    # strict verification of A's representatives (all classes, up to MAXV)
    vdir = os.path.join(out, "verified")
    os.makedirs(vdir)
    verified, vfail = 0, 0
    for r, s_hex, _ in alines[:MAXV]:
        s = int(s_hex, 16)
        bits = [(s >> i) & 1 for i in range(L)]
        path = os.path.join(vdir, f"cs_{n}_{R}_{L}_{r}.cs")
        with open(path, "x") as f:
            f.write(f"COVERING-SEQUENCE {n} {R} {L}\n" + " ".join(map(str, bits)) + "\n")
        p = subprocess.run([sys.executable, os.path.join(CODE, "verify_cs.py"), path, "--expect", str(n), str(R),
                            str(L)], capture_output=True, text=True)
        if p.returncode == 0 and p.stdout.strip().endswith("VALID"):
            verified += 1
        else:
            vfail += 1
    ok &= vfail == 0
    res.update({"verified_witnesses": verified, "verify_failures": vfail, "verify_cap": MAXV, "all_ok": ok})
    with open(os.path.join(out, "compare.json"), "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    print(f"n={n} R={R} L={L}: B examined={examined} (2^L={2 ** L}) covering_strings={bcount} classes={len(bset)}; "
          f"A necklaces={res['A']['necklaces']} classes={len(aset)} sum_periods={asum}; agree={agree}; "
          f"verified={verified} fail={vfail}; {'OK' if ok else 'NOT-OK'}")
    return ok


def main(argv):
    if len(argv) < 6:
        print(__doc__, file=sys.stderr)
        return 2
    mode, out, n, R, L = argv[1], argv[2], int(argv[3]), int(argv[4]), int(argv[5])
    if mode == "run":
        jobs = int(argv[6]) if len(argv) > 6 else 1
        secs = argv[7] if len(argv) > 7 else "3600"
        os.makedirs(out)
        total = 2 ** L
        bpres = []
        for k in range(jobs):
            lo, hi = total * k // jobs, total * (k + 1) // jobs
            bp = os.path.join(out, f"B-{n}-{R}-{L}-{k:03d}")
            subprocess.run([os.path.join(LANE, "bin", "cs_brute"), str(n), str(R), str(L), str(lo), str(hi), secs, bp],
                           capture_output=True, text=True)
            bpres.append(bp)
        apre = os.path.join(out, f"A-{n}-{R}-{L}")
        subprocess.run([os.path.join(LANE, "bin", "cs_neck"), str(n), str(R), str(L), secs, apre],
                       capture_output=True, text=True)
        return 0 if compare(out, n, R, L, bpres, apre) else 1
    if mode == "compare":
        bpres = argv[6].split(",")
        apre = argv[7]
        os.makedirs(out)
        return 0 if compare(out, n, R, L, bpres, apre) else 1
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
