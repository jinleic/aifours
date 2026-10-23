#!/usr/bin/env python3
"""verify_cs.py -- strict verifier for covering-sequence witnesses (lane covering-sequence12-r3, README 1.5).

Certificate format (strict):
    line 1: "COVERING-SEQUENCE n R L" (decimal integers without sign or leading zeros; n >= 1, R >= 0, L >= 1)
    line 2: exactly L tokens, each "0" or "1", separated by single spaces
    a final newline, no carriage returns, nothing else.

Check (definition-first, no tricks): for EVERY target y in {0,1}^n (including all-zero and all-one), the minimum over
all L windows j of the number of positions t in 0..n-1 with y_t != x_{(j+t) mod L}, where L is the ACTUAL declared
length (equal to the token count; a window wraps repeatedly when L < n), must be <= R.
Reports the maximum nearest distance, the nearest-distance histogram, and the all-zero and all-one distances.

Usage: verify_cs.py CERT [--expect n R L] [--sha256 HEX] [--json OUT]    exit 0 iff the certificate is valid (VALID)
  --sha256 binds the certificate bytes to a pinned SHA-256 (64 lowercase hex digits); it is checked first.
Stdlib only; shares no code with code/cs_brute.c or code/cs_neck.c. Never writes anything except OUT (exclusive).
v2 (07:09 PDT 2026-10-17): adds --sha256 only; v1 is archive/code/verify_cs.v1.py (SHA-256 aa209ac5...9507).
"""
import hashlib
import json
import os
import re
import sys

NUM = r"(0|[1-9][0-9]*)"
MAX_N = 16


class Invalid(Exception):
    pass


def need(cond, msg):
    if not cond:
        raise Invalid(msg)


def parse(data):
    need(data.endswith(b"\n"), "format: missing final newline")
    need(b"\r" not in data, "format: carriage return")
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError:
        raise Invalid("format: non-ASCII byte")
    lines = text[:-1].split("\n")
    need(len(lines) == 2, f"format: expected exactly 2 lines, found {len(lines)}")
    m = re.fullmatch(r"COVERING-SEQUENCE " + NUM + " " + NUM + " " + NUM, lines[0])
    need(m is not None, f"format: bad header {lines[0]!r}")
    n, R, L = (int(x) for x in m.groups())
    need(1 <= n <= MAX_N, f"format: n = {n} outside 1..{MAX_N}")
    need(L >= 1, "format: L must be >= 1")
    toks = lines[1].split(" ")
    need(len(toks) == L, f"format: header says L = {L} but line 2 has {len(toks)} tokens")
    need(all(t in ("0", "1") for t in toks), "format: a token is not 0 or 1")
    return n, R, L, [int(t) for t in toks]


def nearest_distances(n, x):
    L = len(x)
    windows = [[x[(j + t) % L] for t in range(n)] for j in range(L)]
    out = []
    for y in range(2 ** n):
        ybits = [(y >> t) & 1 for t in range(n)]
        best = n + 1
        for w in windows:
            d = 0
            for t in range(n):
                if w[t] != ybits[t]:
                    d += 1
            if d < best:
                best = d
                if best == 0:
                    break
        out.append(best)
    return out


def main(argv):
    args = argv[1:]
    if not args:
        print(__doc__, file=sys.stderr)
        return 2
    path = args.pop(0)
    expect, jout, pin = None, None, None
    while args:
        opt = args.pop(0)
        if opt == "--expect" and len(args) >= 3:
            expect = tuple(int(args.pop(0)) for _ in range(3))
        elif opt == "--json" and args:
            jout = args.pop(0)
        elif opt == "--sha256" and args and re.fullmatch(r"[0-9a-f]{64}", args[0]):
            pin = args.pop(0)
        else:
            print(f"bad option {opt}", file=sys.stderr)
            return 2
    data = open(path, "rb").read()
    res = {"certificate": path, "sha256": hashlib.sha256(data).hexdigest(),
           "verifier_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}
    try:
        if pin is not None:
            need(res["sha256"] == pin, f"binding: sha256 {res['sha256']} != pinned {pin}")
        n, R, L, x = parse(data)
        res.update({"n": n, "R": R, "L": L})
        if expect is not None:
            need((n, R, L) == expect, f"binding: certificate is ({n},{R},{L}), expected {expect}")
        dist = nearest_distances(n, x)
        hist = {}
        for d in dist:
            hist[d] = hist.get(d, 0) + 1
        res["targets_checked"] = len(dist)
        res["max_nearest_distance"] = max(dist)
        res["nearest_distance_histogram"] = {str(k): hist[k] for k in sorted(hist)}
        res["all_zero_nearest_distance"] = dist[0]
        res["all_one_nearest_distance"] = dist[2 ** n - 1]
        bad = [y for y, d in enumerate(dist) if d > R]
        res["uncovered_count"] = len(bad)
        need(not bad, f"coverage: {len(bad)} target(s) at distance > R = {R}, first {bad[:3]} "
                      f"(as integers with bit t = y_t)")
        res["verdict"] = "VALID"
        rc = 0
    except Invalid as e:
        res["verdict"] = f"INVALID {e}"
        rc = 1
    for k in sorted(res):
        if k != "verdict":
            print(f"{k}: {res[k]}")
    print(res["verdict"])
    if jout:
        with open(jout, "x") as f:
            json.dump(res, f, indent=1, sort_keys=True)
            f.write("\n")
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
