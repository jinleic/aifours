#!/usr/bin/env python3
"""verify_brd.py -- strict definition-first verifier for Bhaskar Rao designs BRD(v,b,r,k,lambda) (lane brd26-130,
README 1.6).

Certificate format (strict):
    line 1: "BRD v b r k L"   (five decimal integers, no sign, no leading zeros, single spaces)
    then exactly v lines, each with exactly b entries from {-1, 0, 1} written as "-1", "0", "1", separated by single
    spaces; every line ends with LF; no CR, no tab, no other byte, nothing after the last row.
Definition (contract info-2-brd26; CPro1 problem_def):
    (H) v, b >= 1 and L even (each product sign must occur L/2 times);
    (R) every row has exactly r nonzero entries;
    (C) every column has exactly k nonzero entries;
    (P) every two distinct rows have exactly L/2 columns with product +1 and exactly L/2 columns with product -1.
Repeated (equal) columns and columns equal up to sign are ALLOWED; they are counted and reported, never rejected.
Exit 0 iff VALID; on failure prints "INVALID <REASON>: detail" with REASON in FORMAT, HEADER, ROWS, COLUMNS, PAIRS.
Usage: verify_brd.py CERT [--expect v b r k L] [--sha256 HEX] [--json OUT]
Stdlib only; shares no code with code/brd_check.c, with any encoder in this lane, or with any CPro1 verifier.
Writes only OUT (exclusive create).
"""
import hashlib
import json
import re
import sys

NUM = r"(?:0|[1-9][0-9]*)"
HEADER_RE = re.compile(r"BRD " + NUM + " " + NUM + " " + NUM + " " + NUM + " " + NUM)
ENTRY = {"-1": -1, "0": 0, "1": 1}


class Invalid(Exception):
    def __init__(self, reason, detail):
        super().__init__(f"{reason}: {detail}")
        self.reason = reason
        self.detail = detail


def parse(data):
    """Return (params, rows) or raise Invalid; data is bytes."""
    if not data:
        raise Invalid("FORMAT", "empty file")
    for byte in data:
        if not (byte == 0x0A or 0x20 <= byte <= 0x7E):
            raise Invalid("FORMAT", f"byte 0x{byte:02x} is not printable ASCII or LF")
    text = data.decode("ascii")
    if not text.endswith("\n"):
        raise Invalid("FORMAT", "file does not end with LF")
    lines = text[:-1].split("\n")
    if not HEADER_RE.fullmatch(lines[0]):
        raise Invalid("FORMAT", f"bad header line {lines[0][:60]!r}")
    params = [int(x) for x in lines[0].split(" ")[1:]]
    v, b, r, k, lam = params
    if v < 1 or b < 1:
        raise Invalid("HEADER", "v and b must be positive")
    if lam % 2 != 0:
        raise Invalid("HEADER", f"lambda = {lam} is odd")
    body = lines[1:]
    if len(body) != v:
        raise Invalid("FORMAT", f"{len(body)} matrix lines, expected v = {v}")
    rows = []
    for i, line in enumerate(body):
        toks = line.split(" ")
        if len(toks) != b:
            raise Invalid("FORMAT", f"row {i}: {len(toks)} tokens, expected b = {b}")
        row = []
        for j, t in enumerate(toks):
            if t not in ENTRY:
                raise Invalid("FORMAT", f"row {i} column {j}: token {t[:12]!r} not in {{-1,0,1}}")
            row.append(ENTRY[t])
        rows.append(row)
    return params, rows


def check(params, rows):
    """Definition-first checks; returns a dict of counts, raises Invalid on the first violated condition."""
    v, b, r, k, lam = params
    for i in range(v):
        nz = sum(1 for x in rows[i] if x != 0)
        if nz != r:
            raise Invalid("ROWS", f"row {i} has {nz} nonzero entries, expected r = {r}")
    for j in range(b):
        nz = sum(1 for i in range(v) if rows[i][j] != 0)
        if nz != k:
            raise Invalid("COLUMNS", f"column {j} has {nz} nonzero entries, expected k = {k}")
    half = lam // 2
    for i in range(v):
        for i2 in range(i + 1, v):
            plus = minus = 0
            for j in range(b):
                p = rows[i][j] * rows[i2][j]
                if p == 1:
                    plus += 1
                elif p == -1:
                    minus += 1
            if plus != half or minus != half:
                raise Invalid("PAIRS", f"rows {i},{i2}: {plus} products +1 and {minus} products -1, "
                                       f"expected {half} and {half}")
    cols = [tuple(rows[i][j] for i in range(v)) for j in range(b)]
    seen, dup = set(), 0
    for c in cols:
        if c in seen:
            dup += 1
        seen.add(c)
    seen_abs, dup_abs = set(), 0
    for c in cols:
        a = tuple(abs(x) for x in c)
        if a in seen_abs:
            dup_abs += 1
        seen_abs.add(a)
    return {"columns_equal_to_an_earlier_column": dup,
            "columns_with_support_equal_to_an_earlier_column": dup_abs}


def main(argv):
    args = argv[1:]
    if not args:
        print(__doc__, file=sys.stderr)
        return 2
    path, expect, want_sha, out = args[0], None, None, None
    rest = args[1:]
    while rest:
        o = rest.pop(0)
        if o == "--expect":
            expect = [int(rest.pop(0)) for _ in range(5)]
        elif o == "--sha256":
            want_sha = rest.pop(0).lower()
        elif o == "--json":
            out = rest.pop(0)
        else:
            print(f"unknown option {o}", file=sys.stderr)
            return 2
    data = open(path, "rb").read()
    sha = hashlib.sha256(data).hexdigest()
    rec = {"file": path, "sha256": sha, "verifier": "verify_brd.py"}
    try:
        if want_sha is not None and sha != want_sha:
            raise Invalid("HEADER", f"sha256 {sha} differs from expected {want_sha}")
        params, rows = parse(data)
        rec["params"] = params
        if expect is not None and params != expect:
            raise Invalid("HEADER", f"header parameters {params} differ from expected {expect}")
        rec.update(check(params, rows))
        rec["verdict"] = "VALID"
        msg = f"VALID BRD{tuple(params)} sha256={sha}"
    except Invalid as e:
        rec["verdict"] = "INVALID"
        rec["reason"] = e.reason
        rec["detail"] = e.detail
        msg = f"INVALID {e.reason}: {e.detail}"
    if out:
        with open(out, "x") as f:
            json.dump(rec, f, indent=1)
            f.write("\n")
    print(msg)
    return 0 if rec["verdict"] == "VALID" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
