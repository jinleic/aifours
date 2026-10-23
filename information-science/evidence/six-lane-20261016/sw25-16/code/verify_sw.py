#!/usr/bin/env python3
"""Definition-first checker for a symmetric weighing matrix SW(n,w) (stdlib only).

Usage: python3 -B code/verify_sw.py FILE --expect N W [--sha256 HEX]

Strict file format: line 1 'SW n w'; then exactly n lines, each with n tokens separated by single spaces; every line
ends with LF (no CR), the file ends with LF and contains nothing else.  Tokens must be canonical decimal integers
with at most 4 digits, matching (0|-?[1-9][0-9]{0,3}) (FORMAT otherwise; so '-0', '+1', '01' are FORMAT); an integer
outside {-1,0,1} is an ENTRIES failure.

Definition checked: W = W^T, entries in {-1,0,1}, W W^T = w I (computed exactly over the integers), and every row has
exactly w nonzero entries.  Categories, in primary-reason order:
  FORMAT, HEADER (stop at the first of these), then ENTRIES, SYMMETRY, WEIGHT, ORTHO (all computed).
WEIGHT: some row has (W W^T)_ii != w or a number of nonzeros != w.  ORTHO: some (W W^T)_ij != 0 with i != j.
Prints one line 'RESULT VALID ...' or 'RESULT INVALID primary=<cat> failing=<cat,...> ...' and exits 0 / 1.
"""
import hashlib
import re
import sys

ORDER = ["FORMAT", "HEADER", "ENTRIES", "SYMMETRY", "WEIGHT", "ORTHO"]
TOKEN = re.compile(r"(0|-?[1-9][0-9]{0,3})\Z")
HEAD = re.compile(r"SW ([1-9][0-9]{0,3}) ([1-9][0-9]{0,3})\Z")


def fail(cat, detail, extra=""):
    print(f"RESULT INVALID primary={cat} failing={cat} detail={detail}{extra}")
    sys.exit(1)


def main(argv):
    if len(argv) < 5 or argv[2] != "--expect":
        print("usage: verify_sw.py FILE --expect N W [--sha256 HEX]")
        sys.exit(2)
    path, n_exp, w_exp = argv[1], int(argv[3]), int(argv[4])
    sha_exp = None
    if len(argv) >= 7 and argv[5] == "--sha256":
        sha_exp = argv[6].lower()
    data = open(path, "rb").read()
    sha = hashlib.sha256(data).hexdigest()
    extra = f" sha256={sha}"
    if sha_exp is not None and sha != sha_exp:
        fail("FORMAT", "sha256-mismatch", extra)
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError:
        fail("FORMAT", "non-ascii-byte", extra)
    if "\r" in text:
        fail("FORMAT", "CR-present", extra)
    if not text.endswith("\n"):
        fail("FORMAT", "no-final-LF", extra)
    lines = text[:-1].split("\n")
    m = HEAD.match(lines[0])
    if m is None:
        fail("FORMAT", "bad-header-line", extra)
    n, w = int(m.group(1)), int(m.group(2))
    if len(lines) != n + 1:
        fail("FORMAT", f"line-count-{len(lines) - 1}-expected-{n}", extra)
    W = []
    for r, line in enumerate(lines[1:]):
        toks = line.split(" ")
        if len(toks) != n:
            fail("FORMAT", f"row-{r}-has-{len(toks)}-tokens", extra)
        row = []
        for t in toks:
            if TOKEN.match(t) is None:
                fail("FORMAT", f"row-{r}-bad-token-{t!r}", extra)
            row.append(int(t))
        W.append(row)
    if (n, w) != (n_exp, w_exp):
        fail("HEADER", f"header-{n}-{w}-expected-{n_exp}-{w_exp}", extra)

    failing = set()
    details = []
    bad_entries = [(i, j) for i in range(n) for j in range(n) if W[i][j] not in (-1, 0, 1)]
    if bad_entries:
        failing.add("ENTRIES")
        details.append(f"non-ternary-cells={len(bad_entries)}")
    asym = [(i, j) for i in range(n) for j in range(i + 1, n) if W[i][j] != W[j][i]]
    if asym:
        failing.add("SYMMETRY")
        details.append(f"asymmetric-pairs={len(asym)}")
    gram = [[sum(W[i][k] * W[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
    bad_w = [i for i in range(n) if gram[i][i] != w or sum(1 for x in W[i] if x != 0) != w]
    if bad_w:
        failing.add("WEIGHT")
        details.append(f"bad-weight-rows={len(bad_w)}")
    bad_o = [(i, j) for i in range(n) for j in range(i + 1, n) if gram[i][j] != 0]
    if bad_o:
        failing.add("ORTHO")
        details.append(f"nonorthogonal-row-pairs={len(bad_o)}")
    trace = sum(W[i][i] for i in range(n))
    stats = f" n={n} w={w} trace={trace}{extra}"
    if failing:
        cats = [c for c in ORDER if c in failing]
        print(f"RESULT INVALID primary={cats[0]} failing={','.join(cats)} detail={';'.join(details)}{stats}")
        sys.exit(1)
    print(f"RESULT VALID SW({n},{w}){stats}")
    sys.exit(0)


if __name__ == "__main__":
    main(sys.argv)
