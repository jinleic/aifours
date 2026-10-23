#!/usr/bin/env python3
"""checker_controls.py -- calibration of the two lane checkers (README 1.6), stdlib only.

Positives (must be VALID for both checkers):
  P-rosin15   Rosin arXiv:2505.23881v1 Figure 3 (sources/rosin-2505.23881v1.layout.txt lines 833-874, transposed):
              BRD(15,42,14,5,4);
  P-paley6    Paley conference matrix of order 6 over GF(5): BRD(6,6,5,5,4);
  P-paley26   Paley conference matrix of order 26 over GF(25) = GF(5)[t]/(t^2-2): BRD(26,26,25,25,24);
  P-conf4     skew Paley conference matrix of order 4 over GF(3): BRD(4,4,3,3,2).
Negatives (both checkers must reject for the intended reason), applied to P-rosin15 and P-paley26:
  sign flip of one nonzero entry -> PAIRS; nonzero moved within its row to a zero cell -> COLUMNS; nonzero moved
  within its column to a zero cell -> ROWS; header with a wrong lambda checked with --expect -> HEADER; odd lambda
  in the header -> HEADER; CRLF, missing final LF, trailing space, tab separator, U+2212 minus, '+1' token, missing
  last row, extra blank line, leading zero in the header -> FORMAT.
Usage: checker_controls.py OUTDIR   (OUTDIR must not exist; all files created exclusively). Exit 0 iff PASS.
"""
import hashlib
import json
import os
import subprocess
import sys

CODE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(CODE)
PY = [sys.executable, "-B", os.path.join(CODE, "verify_brd.py")]
CBIN = os.path.join(LANE, "bin", "brd_check")


def text_of(params, rows):
    return "BRD " + " ".join(map(str, params)) + "\n" + "".join(" ".join(map(str, r)) + "\n" for r in rows)


def rosin15():
    lines = open(os.path.join(LANE, "sources", "rosin-2505.23881v1.layout.txt"), encoding="utf-8").read().split("\n")
    block = lines[832:874]  # file lines 833..874 (1-based)
    cols = []
    for ln in block:
        toks = ln.replace("\u2212", "-").split()
        assert len(toks) == 15, (ln, len(toks))
        cols.append([int(t) for t in toks])
    assert len(cols) == 42
    rows = [[cols[j][i] for j in range(42)] for i in range(15)]
    return [15, 42, 14, 5, 4], rows


def paley(q_elems, mul, sub, chi, skew):
    """Conference matrix C = [[0, 1^T], [+-1, Q]] with Q[a][b] = chi(b - a)."""
    n = len(q_elems) + 1
    rows = [[0] * n for _ in range(n)]
    for j in range(1, n):
        rows[0][j] = 1
        rows[j][0] = -1 if skew else 1
    for a in range(len(q_elems)):
        for b in range(len(q_elems)):
            rows[a + 1][b + 1] = chi(sub(q_elems[b], q_elems[a]))
    return rows


def gf5():
    el = list(range(5))
    sq = {(x * x) % 5 for x in range(1, 5)}
    chi = lambda x: 0 if x == 0 else (1 if x in sq else -1)
    return paley(el, None, lambda a, b: (a - b) % 5, chi, False)


def gf3():
    el = list(range(3))
    chi = lambda x: 0 if x == 0 else (1 if x == 1 else -1)
    return paley(el, None, lambda a, b: (a - b) % 3, chi, True)


def gf25():
    # elements (a, b) = a + b t, t^2 = 2 (2 is a non-square mod 5, so t^2 - 2 is irreducible)
    el = [(a, b) for a in range(5) for b in range(5)]

    def mul(x, y):
        a, b = x
        c, d = y
        return ((a * c + 2 * b * d) % 5, (a * d + b * c) % 5)

    def power(x, e):
        r = (1, 0)
        for _ in range(e):
            r = mul(r, x)
        return r

    def chi(x):
        if x == (0, 0):
            return 0
        p = power(x, 12)
        assert p in ((1, 0), (4, 0))
        return 1 if p == (1, 0) else -1

    return paley(el, mul, lambda x, y: ((x[0] - y[0]) % 5, (x[1] - y[1]) % 5), chi, False)


def run_both(path, expect=None):
    a = PY + [path] + (["--expect"] + [str(x) for x in expect] if expect else [])
    c = [CBIN, path] + ([str(x) for x in expect] if expect else [])
    pa = subprocess.run(a, capture_output=True, text=True)
    pc = subprocess.run(c, capture_output=True, text=True)
    return (pa.returncode, pa.stdout.strip()), (pc.returncode, pc.stdout.strip())


def reason_of(out):
    rc, s = out
    if rc == 0 and s.startswith("VALID"):
        return "VALID"
    if s.startswith("INVALID "):
        return s.split()[1].rstrip(":")
    return f"ERROR(rc={rc})"


def mutations(name, params, rows):
    """Yield (mut_name, intended_reason, file_bytes, expect_or_None)."""
    v, b = params[0], params[1]
    base = text_of(params, rows)
    i0 = 0
    j0 = next(j for j in range(b) if rows[i0][j] != 0)
    m = [r[:] for r in rows]
    m[i0][j0] = -m[i0][j0]
    yield "sign-flip", "PAIRS", text_of(params, m).encode(), None
    jz = next(j for j in range(b) if rows[i0][j] == 0)
    m = [r[:] for r in rows]
    m[i0][jz], m[i0][j0] = m[i0][j0], 0
    yield "move-within-row", "COLUMNS", text_of(params, m).encode(), None
    iz = next(i for i in range(v) if rows[i][j0] == 0)
    m = [r[:] for r in rows]
    m[iz][j0], m[i0][j0] = m[i0][j0], 0
    yield "move-within-column", "ROWS", text_of(params, m).encode(), None
    wrong = list(params)
    wrong[4] = params[4] + 2
    yield "header-wrong-lambda-expect", "HEADER", text_of(wrong, rows).encode(), wrong[:4] + [params[4]]
    odd = list(params)
    odd[4] = params[4] + 1
    yield "header-odd-lambda", "HEADER", text_of(odd, rows).encode(), None
    yield "crlf", "FORMAT", base.replace("\n", "\r\n").encode(), None
    yield "no-final-lf", "FORMAT", base[:-1].encode(), None
    lines = base.split("\n")
    yield "trailing-space", "FORMAT", ("\n".join([lines[0], lines[1] + " "] + lines[2:])).encode(), None
    yield "tab-separator", "FORMAT", ("\n".join([lines[0], lines[1].replace(" ", "\t", 1)] + lines[2:])).encode(), None
    k = lines[1].find("-1")
    if k < 0:
        k = lines[2].find("-1")
        alt = lines[2][:k] + "\u22121" + lines[2][k + 2:]
        yield "unicode-minus", "FORMAT", ("\n".join(lines[:2] + [alt] + lines[3:])).encode("utf-8"), None
    else:
        alt = lines[1][:k] + "\u22121" + lines[1][k + 2:]
        yield "unicode-minus", "FORMAT", ("\n".join([lines[0], alt] + lines[2:])).encode("utf-8"), None
    k = (" " + lines[1] + " ").find(" 1 ")
    alt = (" " + lines[1] + " ")[:k] + " +1 " + (" " + lines[1] + " ")[k + 3:]
    yield "plus-token", "FORMAT", ("\n".join([lines[0], alt.strip(" ")] + lines[2:])).encode(), None
    yield "missing-last-row", "FORMAT", ("\n".join(lines[:-2]) + "\n").encode(), None
    yield "extra-blank-line", "FORMAT", (base + "\n").encode(), None
    yield "header-leading-zero", "FORMAT", base.replace("BRD ", "BRD 0", 1).encode(), None


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    out = argv[1]
    os.makedirs(out)
    positives = {
        "P-rosin15": rosin15(),
        "P-paley6": ([6, 6, 5, 5, 4], gf5()),
        "P-paley26": ([26, 26, 25, 25, 24], gf25()),
        "P-conf4": ([4, 4, 3, 3, 2], gf3()),
    }
    results, ok = [], True
    for name, (params, rows) in positives.items():
        path = os.path.join(out, name + ".brd")
        data = text_of(params, rows).encode()
        with open(path, "xb") as f:
            f.write(data)
        a, c = run_both(path, params)
        ra, rc = reason_of(a), reason_of(c)
        good = ra == "VALID" and rc == "VALID"
        ok &= good
        results.append({"case": name, "intended": "VALID", "verify_brd": a[1], "brd_check": c[1],
                        "sha256": hashlib.sha256(data).hexdigest(), "pass": good})
    for name in ("P-rosin15", "P-paley26"):
        params, rows = positives[name]
        for mname, intended, data, expect in mutations(name, params, rows):
            path = os.path.join(out, f"{name}--{mname}.brd")
            with open(path, "xb") as f:
                f.write(data)
            a, c = run_both(path, expect)
            ra, rc = reason_of(a), reason_of(c)
            good = ra == intended and rc == intended
            ok &= good
            results.append({"case": f"{name}--{mname}", "intended": intended, "verify_brd": a[1],
                            "brd_check": c[1], "sha256": hashlib.sha256(data).hexdigest(), "pass": good})
    summary = {"verdict": "CHECKER-CONTROLS PASS" if ok else "CHECKER-CONTROLS FAIL",
               "verify_brd_sha256": hashlib.sha256(open(os.path.join(CODE, "verify_brd.py"), "rb").read()).hexdigest(),
               "brd_check_c_sha256": hashlib.sha256(open(os.path.join(CODE, "brd_check.c"), "rb").read()).hexdigest(),
               "brd_check_bin_sha256": hashlib.sha256(open(CBIN, "rb").read()).hexdigest(),
               "cases": len(results), "results": results}
    with open(os.path.join(out, "checker-controls.json"), "x") as f:
        json.dump(summary, f, indent=1)
        f.write("\n")
    for r in results:
        print(("ok  " if r["pass"] else "BAD ") + r["case"], "|", r["verify_brd"][:70], "|", r["brd_check"][:70])
    print(summary["verdict"], len(results), "cases")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
