#!/usr/bin/env python3
"""Controls for the SAT/DRAT pipeline (code/sat_run.py + code/drat_check.py).

Usage (lane root): python3 -B code/drat_gate_controls.py OUTDIR
Positive: pigeonhole PHP(7 pigeons, 6 holes) is UNSAT for kissat and CaDiCaL with proofs; both proofs VERIFIED.
Negatives (must NOT verify): (a) satisfiable CNF 'p cnf 1 1 / 1 0' with an empty-clause binary proof;
(b) the kissat PHP proof truncated to its first half; (c) the kissat PHP proof checked against a different
satisfiable CNF (PHP(6,6)).  Writes OUTDIR/drat-gate-controls.json.
"""
import json
import os
import subprocess
import sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = [sys.executable, "-B"]


def php(p, h):
    v = lambda i, j: 1 + i * h + j  # noqa: E731
    cls = [[v(i, j) for j in range(h)] for i in range(p)]
    for j in range(h):
        for a in range(p):
            for b in range(a + 1, p):
                cls.append([-v(a, j), -v(b, j)])
    return f"p cnf {p * h} {len(cls)}\n" + "".join(" ".join(map(str, c)) + " 0\n" for c in cls)


def zst_write(path, raw):
    with open(path, "xb") as f:
        subprocess.run(["zstd", "-q", "-c"], input=raw, stdout=f, check=True)


def main():
    out = sys.argv[1]
    os.mkdir(out)
    J = lambda *a: os.path.join(out, *a)  # noqa: E731
    with open(J("php7-6.cnf"), "x") as f:
        f.write(php(7, 6))
    with open(J("php6-6.cnf"), "x") as f:
        f.write(php(6, 6))
    with open(J("sat1.cnf"), "x") as f:
        f.write("p cnf 1 1\n1 0\n")
    res = {}
    for s in ("kissat", "cadical"):
        r = subprocess.run(PY + [os.path.join(LANE, "code/sat_run.py"), s, J("php7-6.cnf"), "600",
                                 J(f"php7-6-{s}"), "--proof"], capture_output=True, text=True)
        res[f"solve-{s}"] = r.stdout.strip()
        r = subprocess.run(PY + [os.path.join(LANE, "code/drat_check.py"), J("php7-6.cnf"), J(f"php7-6-{s}.drat.zst"),
                                 J(f"php7-6-{s}.drat-check.json")], capture_output=True, text=True)
        res[f"check-{s}"] = json.loads(r.stdout)
    # (a) empty clause binary proof on a satisfiable CNF: 'a' 0x61 then terminating 0
    zst_write(J("empty-clause.drat.zst"), b"a\x00")
    r = subprocess.run(PY + [os.path.join(LANE, "code/drat_check.py"), J("sat1.cnf"), J("empty-clause.drat.zst"),
                             J("neg-a-sat-empty.json")], capture_output=True, text=True)
    res["neg-a"] = json.loads(r.stdout)
    # (b) truncated kissat proof
    raw = subprocess.run(["zstd", "-dc", J("php7-6-kissat.drat.zst")], capture_output=True, check=True).stdout
    # cut at a clause boundary: binary DRAT clauses end with a 0x00 byte
    half = raw[: len(raw) // 2]
    cut = half.rfind(b"\x00") + 1
    zst_write(J("php7-6-kissat-truncated.drat.zst"), raw[:cut])
    r = subprocess.run(PY + [os.path.join(LANE, "code/drat_check.py"), J("php7-6.cnf"),
                             J("php7-6-kissat-truncated.drat.zst"), J("neg-b-truncated.json")],
                       capture_output=True, text=True)
    res["neg-b"] = json.loads(r.stdout)
    res["neg-b-bytes"] = {"full": len(raw), "truncated": cut}
    # (c) proof against a satisfiable CNF
    r = subprocess.run(PY + [os.path.join(LANE, "code/drat_check.py"), J("php6-6.cnf"), J("php7-6-kissat.drat.zst"),
                             J("neg-c-wrong-cnf.json")], capture_output=True, text=True)
    res["neg-c"] = json.loads(r.stdout)
    ok = (res["check-kissat"]["verified"] and res["check-cadical"]["verified"] and not res["neg-a"]["verified"]
          and not res["neg-b"]["verified"] and not res["neg-c"]["verified"])
    res["all_pass"] = ok
    with open(J("drat-gate-controls.json"), "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    print(json.dumps(res, indent=1))
    print("DRAT-GATE-CONTROLS", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
