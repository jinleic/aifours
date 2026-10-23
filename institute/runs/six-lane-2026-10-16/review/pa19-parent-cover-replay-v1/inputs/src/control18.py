#!/usr/bin/env python3
"""PA(18,8,6) positive control for the skeleton encoders (contract item: PA18 control).

The CPro1 18-row array (data/cpro1-pa-18-8-6.txt) has five (3^6) columns and three
(4,3,3,3,3,2) columns. 18 = 3*6 rows, so the base profile has no size-4 block: the encoders
are run in their 18-row variant (base columns with no fixed cells, empty skeleton) on that
multiset. The array is brought to the encoder's normal form by repairing violated
lex-leader generators (value swaps of equal-count labels, row transpositions of identical
rows, swaps of identical columns), each strictly decreasing the array in the encoder's
reading order, so the loop terminates. The CNF plus unit clauses fixing every cell must be
SAT; corrupted arrays fixed the same way must be UNSAT.
Usage: control18.py which(m1|m2) OUTDIR
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
LANE = os.path.dirname(HERE)
KISSAT = "/opt/homebrew/bin/kissat"


def load():
    rows = [list(map(int, l.split())) for l in open(os.path.join(LANE, "data", "cpro1-pa-18-8-6.txt"))]
    return rows


def relabel_by_count(A, q):
    N, k = len(A), len(A[0])
    for c in range(k):
        cnt = [sum(1 for r in range(N) if A[r][c] == s) for s in range(q)]
        order = sorted(range(q), key=lambda s: (-cnt[s], min([r for r in range(N) if A[r][c] == s] or [N])))
        mp = {s: i for i, s in enumerate(order)}
        for r in range(N):
            A[r][c] = mp[A[r][c]]
    return A


def counts(A, c, q):
    return [sum(1 for r in range(len(A)) if A[r][c] == s) for s in range(q)]


def repair(A, q, cols_groups, row_major=True, row_swaps=True):
    """apply violated generators until none; cols_groups: list of lists of interchangeable
    consecutive column indices (identical profile)."""
    N, k = len(A), len(A[0])
    changed = True
    steps = 0
    while changed:
        changed = False
        for c in range(k):
            cnt = counts(A, c, q)
            for s in range(q - 1):
                if cnt[s] != cnt[s + 1] or cnt[s] == 0:
                    continue
                f1 = min(r for r in range(N) if A[r][c] == s)
                f2 = min(r for r in range(N) if A[r][c] == s + 1)
                if f2 < f1:
                    for r in range(N):
                        if A[r][c] == s:
                            A[r][c] = s + 1
                        elif A[r][c] == s + 1:
                            A[r][c] = s
                    changed = True
                    steps += 1
        if row_swaps:
            for r in range(N - 1):
                if A[r] > A[r + 1]:
                    A[r], A[r + 1] = A[r + 1], A[r]
                    changed = True
                    steps += 1
        for g in cols_groups:
            for a, b in zip(g, g[1:]):
                ca = [A[r][a] for r in range(N)]
                cb = [A[r][b] for r in range(N)]
                if ca > cb:
                    for r in range(N):
                        A[r][a], A[r][b] = A[r][b], A[r][a]
                    changed = True
                    steps += 1
    return A, steps


def solve_with_units(nv, clauses, units):
    parts = ["p cnf %d %d\n" % (nv, len(clauses) + len(units))]
    parts.extend(" ".join(map(str, c)) + " 0\n" for c in clauses)
    parts.extend("%d 0\n" % u for u in units)
    p = subprocess.run([KISSAT, "-q", "-n"], input="".join(parts).encode(), capture_output=True)
    return p.returncode


def main():
    which, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    A0 = load()
    N, k, q = 18, 8, 6
    prof = [sorted(counts(A0, c, q), reverse=True) for c in range(k)]
    base = [c for c in range(k) if prof[c] == [3] * 6]
    spec_cols = [c for c in range(k) if prof[c] != [3] * 6]
    assert len(base) == 5 and len(spec_cols) == 3 and all(prof[c] == [4, 3, 3, 3, 3, 2] for c in spec_cols)
    A = [[row[c] for c in base + spec_cols] for row in A0]
    A = relabel_by_count(A, q)
    res = {"which": which, "source_sha256": hashlib.sha256(open(os.path.join(LANE, "data", "cpro1-pa-18-8-6.txt"), "rb").read()).hexdigest()}
    if which == "m1":
        import encode_skel
        spec = {"N": 18, "k": 8, "q": 6, "c0": 5, "special": [[4, 3, 3, 3, 3, 2]] * 3, "L": 6,
                "skeleton": {"edges": [], "hyper": [], "empty": 18}, "base_quad": False}
        A, steps = repair(A, q, [[5, 6, 7]], row_swaps=True)
        F, X, _ = encode_skel.build(spec)
        nv, clauses = F.nv, F.clauses
        units_of = lambda B: [X[r][c][B[r][c]] for r in range(N) for c in range(k)]  # noqa: E731
    else:
        import encode_skel_b
        A, steps = repair(A, q, [[5, 6, 7]], row_swaps=False)
        nv, clauses, Xv = encode_skel_b.build_variant18()
        units_of = lambda B: [Xv(r, c, B[r][c]) for r in range(N) for c in range(k)]  # noqa: E731
    canon = "".join(" ".join(map(str, row)) + "\n" for row in A)
    open(os.path.join(outdir, "cpro1-canonical-%s.txt" % which), "w").write(canon)
    v1 = subprocess.run([sys.executable, os.path.join(HERE, "verify_pa.py"), os.path.join(outdir, "cpro1-canonical-%s.txt" % which), "18", "8", "6"], capture_output=True, text=True)
    res.update({"repair_steps": steps, "canonical_sha256": hashlib.sha256(canon.encode()).hexdigest(),
                "canonical_verify1_rc": v1.returncode})
    rc = solve_with_units(nv, clauses, units_of(A))
    res["canonical_with_units_rc"] = rc
    res["canonical_satisfies_cnf"] = rc == 10
    muts = {}
    B = [row[:] for row in A]
    B[1][5] = B[0][5]
    B[1][6] = B[0][6]
    muts["rows01_two_extra_agreements"] = B
    B = [row[:] for row in A]
    B[17] = B[0][:]
    muts["duplicate_row"] = B
    B = [row[:] for row in A]
    x = B[3][2]
    B[3][2] = (x + 1) % 6
    muts["single_cell_change"] = B
    res["mutations"] = {}
    for name, Bm in muts.items():
        res["mutations"][name] = solve_with_units(nv, clauses, units_of(Bm))
    res["all_mutations_unsat"] = all(v == 20 for v in res["mutations"].values())
    res["ok"] = res["canonical_satisfies_cnf"] and res["all_mutations_unsat"] and v1.returncode == 0
    json.dump(res, open(os.path.join(outdir, "control18-%s.json" % which), "w"), indent=1)
    print(json.dumps(res))


if __name__ == "__main__":
    main()
