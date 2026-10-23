#!/usr/bin/env python3
"""verify_btd.py -- strict definition-first verifier for balanced ternary designs (lane btd12-15, README 1.5).

Certificate format (strict):
    line 1: "BTD V B p1 p2 R K L"   (decimal integers, no sign, no leading zeros; V, B >= 1)
    then exactly V lines, each with exactly B entries from {0, 1, 2} separated by single spaces;
    a final LF, no CR, nothing else.
Conditions (Francel-Hurd 2008 definition; contract info-2-btd12-15):
    header consistency R = p1 + 2 p2;
    (D1) every entry in {0, 1, 2};
    (D2) every row has exactly p1 entries equal to 1 and exactly p2 entries equal to 2;
    (D3) every column sums to K;
    (D4) every two distinct rows have inner product L.
Duplicate (repeated) columns are ALLOWED and are reported separately (never a rejection).
Usage: verify_btd.py CERT [--expect V B p1 p2 R K L] [--sha256 HEX] [--json OUT]   exit 0 iff VALID
Stdlib only; shares no code with code/btd_check.c or with any CPro1 verifier. Writes only OUT (exclusive).
"""
import hashlib
import json
import re
import sys

NUM = r"(0|[1-9][0-9]*)"


class Invalid(Exception):
    pass


def need(cond, msg):
    if not cond:
        raise Invalid(msg)


def parse(data):
    need(data.endswith(b"\n"), "format: missing final LF")
    need(b"\r" not in data, "format: carriage return")
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError:
        raise Invalid("format: non-ASCII byte")
    lines = text[:-1].split("\n")
    m = re.fullmatch("BTD" + (" " + NUM) * 7, lines[0])
    need(m is not None, f"format: bad header {lines[0]!r}")
    V, B, p1, p2, R, K, L = (int(x) for x in m.groups())
    need(V >= 1 and B >= 1, "format: V and B must be >= 1")
    need(len(lines) == V + 1, f"format: expected {V} matrix lines, found {len(lines) - 1}")
    rows = []
    for i, line in enumerate(lines[1:]):
        toks = line.split(" ")
        need(len(toks) == B, f"format: row {i} has {len(toks)} tokens, expected {B}")
        for t in toks:
            need(re.fullmatch(r"[0-9]+", t) is not None, f"format: row {i} has a non-numeric token {t!r}")
        rows.append([int(t) for t in toks])
    return (V, B, p1, p2, R, K, L), rows


def check(params, rows):
    V, B, p1, p2, R, K, L = params
    need(R == p1 + 2 * p2, f"header: R = {R} != p1 + 2 p2 = {p1 + 2 * p2}")
    for i in range(V):
        for j in range(B):
            need(rows[i][j] in (0, 1, 2), f"range: entry ({i},{j}) = {rows[i][j]} not in {{0,1,2}}")
    for i in range(V):
        ones = sum(1 for x in rows[i] if x == 1)
        twos = sum(1 for x in rows[i] if x == 2)
        need(ones == p1 and twos == p2, f"row-count: row {i} has {ones} ones and {twos} twos, expected {p1} and {p2}")
    for j in range(B):
        s = sum(rows[i][j] for i in range(V))
        need(s == K, f"column-sum: column {j} sums to {s}, expected {K}")
    for i in range(V):
        for k in range(i + 1, V):
            d = sum(rows[i][j] * rows[k][j] for j in range(B))
            need(d == L, f"pair-product: rows {i},{k} have inner product {d}, expected {L}")


def main(argv):
    args = argv[1:]
    if not args:
        print(__doc__, file=sys.stderr)
        return 2
    path = args.pop(0)
    expect, pin, jout = None, None, None
    while args:
        opt = args.pop(0)
        if opt == "--expect" and len(args) >= 7:
            expect = tuple(int(args.pop(0)) for _ in range(7))
        elif opt == "--sha256" and args and re.fullmatch(r"[0-9a-f]{64}", args[0]):
            pin = args.pop(0)
        elif opt == "--json" and args:
            jout = args.pop(0)
        else:
            print(f"bad option {opt}", file=sys.stderr)
            return 2
    data = open(path, "rb").read()
    res = {"certificate": path, "sha256": hashlib.sha256(data).hexdigest(),
           "verifier_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}
    try:
        if pin is not None:
            need(res["sha256"] == pin, f"binding: sha256 {res['sha256']} != pinned {pin}")
        params, rows = parse(data)
        res["params"] = list(params)
        if expect is not None:
            need(params == expect, f"binding: parameters {params} != expected {expect}")
        check(params, rows)
        cols = [tuple(rows[i][j] for i in range(params[0])) for j in range(params[1])]
        dup = {}
        for j, c in enumerate(cols):
            dup.setdefault(c, []).append(j)
        res["duplicate_column_groups"] = [g for g in dup.values() if len(g) > 1]
        res["distinct_columns"] = len(dup)
        twos = [sum(1 for i in range(params[0]) if rows[i][j] == 2) for j in range(params[1])]
        res["column_two_counts"] = twos
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
