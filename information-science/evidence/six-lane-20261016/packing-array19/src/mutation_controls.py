#!/usr/bin/env python3
"""Verifier controls: the CPro1 PA(18,8,6) copy must pass both verifiers; each
mutated copy must be rejected by both, for the intended reason.
Usage: mutation_controls.py BASE_FILE OUTDIR  -> writes OUTDIR/mutation-controls.json
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)


def run(path, N, k, q):
    v1 = subprocess.run([sys.executable, os.path.join(HERE, "verify_pa.py"), path, str(N), str(k), str(q)],
                        capture_output=True, text=True)
    v2 = subprocess.run([os.path.join(LANE, "bin", "verify_pa2"), path, str(N), str(k), str(q)],
                        capture_output=True, text=True)
    return v1.returncode, v1.stdout.strip(), v2.returncode, v2.stdout.strip()


def main():
    base, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    rows = [list(map(int, l.split())) for l in open(base).read().strip("\n").split("\n")]
    N, k, q = len(rows), len(rows[0]), 6
    fmt = lambda rs: "".join(" ".join(map(str, r)) + "\n" for r in rs)  # noqa: E731
    muts = {}
    # 1: make rows 0 and 1 agree in two extra columns where they differ
    m = [r[:] for r in rows]
    diff = [c for c in range(k) if m[0][c] != m[1][c]][:2]
    for c in diff:
        m[1][c] = m[0][c]
    muts["two_more_agreements_rows01"] = (fmt(m), "rows 0,1 agree")
    # 2: duplicate row 0 over row N-1
    m = [r[:] for r in rows]
    m[N - 1] = m[0][:]
    muts["duplicate_row"] = (fmt(m), "agree in 8")
    # 3: single cell change creating a repeat: copy A[r][1] so (col0,col1) pair repeats
    m = [r[:] for r in rows]
    target = None
    for r in range(1, N):
        if m[r][0] == m[0][0]:
            target = r
            break
    m[target][1] = m[0][1]
    muts["single_cell_repeat_pair_cols01"] = (fmt(m), "repeat (col0,col1)")
    # 4: symbol out of range
    m = [r[:] for r in rows]
    m[5][3] = 6
    muts["symbol_out_of_range"] = (fmt(m), "out of range")
    # 5: missing row
    muts["missing_row"] = (fmt(rows[:-1]), "row count")
    # 6: extra column on one row
    m = [r[:] for r in rows]
    m[2] = m[2] + [0]
    muts["extra_column"] = (fmt(m), "entries")
    # 7: non-digit token
    txt = fmt(rows).replace("\n", " x\n", 1)
    muts["non_digit_token"] = (txt, "token/byte")
    # 8: negative symbol
    txt = fmt(rows).replace("\n", "\n-", 1)
    muts["negative_sign"] = (txt, "token/byte")
    res = {"base": base, "base_sha256": hashlib.sha256(open(base, "rb").read()).hexdigest()}
    b = run(base, N, k, q)
    res["base_result"] = {"v1_rc": b[0], "v2_rc": b[2], "v1": b[1], "v2": b[3]}
    ok = b[0] == 0 and b[2] == 0
    res["mutations"] = {}
    for name, (txt, why) in muts.items():
        p = os.path.join(outdir, "mut_" + name + ".txt")
        open(p, "w").write(txt)
        r = run(p, N, k, q)
        res["mutations"][name] = {"intended": why, "v1_rc": r[0], "v2_rc": r[2], "v1": r[1], "v2": r[3],
                                  "sha256": hashlib.sha256(txt.encode()).hexdigest()}
        ok = ok and r[0] != 0 and r[2] != 0
    res["all_controls_behaved"] = ok
    json.dump(res, open(os.path.join(outdir, "mutation-controls.json"), "w"), indent=1)
    print(json.dumps({"all_controls_behaved": ok}))
    for name, r in res["mutations"].items():
        print(name, r["v1_rc"], r["v2_rc"], r["v1"][-90:], "|", r["v2"])


if __name__ == "__main__":
    main()
