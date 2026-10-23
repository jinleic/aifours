#!/usr/bin/env python3
"""checker_c.py - route C definition-level checker for a raw (Z_n,k;1) difference matrix.

Author: ContinueCFR21.CheckerRouteC, 2026-10-19.  Python 3 standard library only.
Written from the task-contract definitions alone; no other checker, encoder or
search code was read.  The mathematics behind every check is in report.md.

Usage
    python3 -I -B checker_c.py --n N --k K [--sha256 HEX] [--output NEW_PATH] FILE

Input contract ("raw DM")
    Plain ASCII.  Exactly K non-empty lines; a line made only of ASCII whitespace
    counts as empty and is ignored.  Every non-empty line holds exactly N
    whitespace-separated unsigned decimal integers in [0, N).  The i-th non-empty
    line (0-based) is row D_i and its c-th token (0-based) is D_i(c).

Checks, each computed separately from the parsed matrix D
    oa_strength2   The N^2 x (K+1) array A with one row per (x, y) in Z_N x Z_N,
                       A(x, y) = (x, D_0(x)+y, D_1(x)+y, ..., D_{K-1}(x)+y) mod N.
                   Coordinate 0 is x and coordinate 1+i is D_i(x)+y; y itself is
                   not a coordinate.  PASS iff for every two of the K+1
                   coordinates every ordered pair (a, b) of symbols occurs in
                   exactly one row (strength 2, index 1), counted with the key
                   a*N+b in a bytearray of size N*N.
    cfr            The CPro1 circular Florentine rectangle predicate on the K-1
                   rows of the contract bridge: tau_t(s) = (D_t(s) - D_0(s)) mod N
                   and row t (t = 1..K-1) holds at position p the symbol s with
                   tau_t(s) = p.  PASS iff every row is a permutation of 0..N-1
                   and, for all distinct symbols a, b and every m in 1..N-1, at
                   most one row has b exactly m positions cyclically to the right
                   of a.
    dm_definition  The literal definition: for every i < j the N values
                   (D_i(c) - D_j(c)) mod N, c = 0..N-1, are pairwise distinct.
    bridge_consistent
                   The three failure patterns must stand in the exact relation
                   proved in report.md; false would expose an implementation bug.

Output
    Exactly one JSON line on stdout.  With --output the same line is also written
    to NEW_PATH, created with mode "x" (an existing file is never overwritten).

Exit status
    0  input well-formed, all three checks PASS and bridge_consistent is true
    1  input well-formed and some check FAILs
    2  input not evaluable: malformed or unreadable file, --sha256 mismatch,
       invalid command line, or the --output file cannot be created
    3  internal error
"""

import hashlib
import json
import os
import sys

CHECKER = "checker_c"
VERSION = 1
MAX_EXAMPLES = 5
OPTIONS = ("--n", "--k", "--sha256", "--output")
USAGE = "usage: checker_c.py --n N --k K [--sha256 HEX] [--output NEW_PATH] FILE"


class UsageError(Exception):
    """The command line is invalid."""


class InputError(Exception):
    """The input bytes do not follow the raw DM contract."""

    def __init__(self, kind, detail, line=None):
        Exception.__init__(self, detail)
        self.kind = kind
        self.detail = detail
        self.line = line


def parse_cli(argv):
    """Return (n, k, path, expected_sha256 or None, output_path or None)."""
    values = {}
    path = None
    index = 0
    while index < len(argv):
        arg = argv[index]
        if arg in OPTIONS:
            if arg in values:
                raise UsageError("%s given twice; %s" % (arg, USAGE))
            if index + 1 >= len(argv):
                raise UsageError("%s needs a value; %s" % (arg, USAGE))
            values[arg] = argv[index + 1]
            index += 2
        elif arg.startswith("-"):
            raise UsageError("unknown option %r; %s" % (arg, USAGE))
        elif path is not None:
            raise UsageError("more than one input file; %s" % USAGE)
        else:
            path = arg
            index += 1
    if "--n" not in values or "--k" not in values or path is None:
        raise UsageError(USAGE)
    numbers = []
    for name in ("--n", "--k"):
        text = values[name]
        if not (text.isascii() and text.isdigit() and len(text) <= 9):
            raise UsageError("%s value %r is not an unsigned decimal integer below 10^9" % (name, text))
        if int(text) < 2:
            raise UsageError("%s must be at least 2" % name)
        numbers.append(int(text))
    want = values.get("--sha256")
    if want is not None:
        want = want.lower()
        if len(want) != 64 or any(ch not in "0123456789abcdef" for ch in want):
            raise UsageError("--sha256 needs exactly 64 hexadecimal digits")
    output = values.get("--output")
    if output is not None and os.path.lexists(output):
        raise UsageError("--output %r already exists; refusing to overwrite" % output)
    return numbers[0], numbers[1], path, want, output


def show(token):
    text = token.decode("ascii")
    return text if len(text) <= 40 else text[:40] + "..."


def parse_raw_dm(data, n, k):
    """Return (D, blank_lines) for well-formed bytes, else raise InputError."""
    if not data.isascii():
        offset = next(i for i, byte in enumerate(data) if byte >= 0x80)
        raise InputError("NON_ASCII", "byte offset %d holds 0x%02x, which is not ASCII" % (offset, data[offset]))
    pieces = data.split(b"\n")
    if pieces[-1] == b"":
        pieces.pop()  # terminator of the last line, not a line of its own
    rows = []
    blank = 0
    for lineno, piece in enumerate(pieces, start=1):
        tokens = piece.split()
        if tokens:
            rows.append((lineno, tokens))
        else:
            blank += 1
    if len(rows) != k:
        raise InputError("LINE_COUNT", "expected exactly %d non-empty lines, found %d" % (k, len(rows)))
    width = len(str(n - 1))
    matrix = []
    for lineno, tokens in rows:
        if len(tokens) != n:
            raise InputError("TOKEN_COUNT", "line %d: expected exactly %d integers, found %d tokens" % (lineno, n, len(tokens)), lineno)
        values = []
        for index, token in enumerate(tokens, start=1):
            if any(byte < 0x30 or byte > 0x39 for byte in token):
                raise InputError("NOT_INTEGER", "line %d token %d %r is not an unsigned decimal integer" % (lineno, index, show(token)), lineno)
            digits = token.lstrip(b"0")
            if len(digits) > width or (digits and int(digits) >= n):
                raise InputError("OUT_OF_RANGE", "line %d token %d %r is not in [0, %d)" % (lineno, index, show(token), n), lineno)
            values.append(int(digits) if digits else 0)
        matrix.append(values)
    return matrix, blank


def coordinate_meaning(p, q):
    """MOLS and DM meaning of the coordinate pair (p, q), p < q, of the array A."""
    if p == 0 and q == 1:
        return "cells (c,g) of the squares; holds for every D"
    if p == 0:
        return "rows of L_%d are permutations; holds for every D" % (q - 1)
    if p == 1:
        return "columns of L_%d are permutations <=> DM rows (0,%d)" % (q - 1, q - 1)
    return "L_%d orthogonal to L_%d <=> DM rows (%d,%d)" % (p - 1, q - 1, p - 1, q - 1)


def check_oa_strength2(D, n, k):
    """Strength 2 / index 1 of A(x,y) = (x, D_0(x)+y, ..., D_{k-1}(x)+y) mod n."""
    width = k + 1
    array = []
    for x in range(n):
        column = [D[i][x] for i in range(k)]
        for y in range(n):
            array.append((x,) + tuple((value + y) % n for value in column))
    size = n * n
    failing = []
    checked = 0
    for p in range(width):
        for q in range(p + 1, width):
            checked += 1
            seen = bytearray(size)  # occurrences of key a*n+b, saturating at 2
            for row in array:
                key = row[p] * n + row[q]
                if seen[key] < 2:
                    seen[key] += 1
            once = seen.count(1)
            if once != size:
                failing.append({
                    "coordinates": [p, q],
                    "meaning": coordinate_meaning(p, q),
                    "pairs_exactly_once": once,
                    "missing_pairs": seen.count(0),
                    "repeated_pairs": seen.count(2),
                })
    return {
        "verdict": "FAIL" if failing else "PASS",
        "array": "A(x,y) = (x, D_0(x)+y, ..., D_%d(x)+y) mod %d, (x,y) in Z_%d^2" % (k - 1, n, n),
        "rows": len(array),
        "coordinates": width,
        "coordinate_pairs_checked": checked,
        "failing_coordinate_pairs": failing,
    }


def check_cfr(D, n, k):
    """CPro1 CFR(k-1, n) predicate on the inverse-permutation rows of the bridge."""
    rows = {}
    not_permutation = []
    for t in range(1, k):
        tau = [(D[t][s] - D[0][s]) % n for s in range(n)]
        holders = [[] for _ in range(n)]  # holders[p] = symbols s with tau_t(s) = p
        for s in range(n):
            holders[tau[s]].append(s)
        row = [cell[0] for cell in holders if len(cell) == 1]
        if len(row) == n and sorted(row) == list(range(n)):
            rows[t] = row
        else:
            not_permutation.append({
                "row": t,
                "empty_positions": sum(1 for cell in holders if not cell),
                "multiply_filled_positions": sum(1 for cell in holders if len(cell) > 1),
            })
    tested = sorted(rows)
    position = {}
    for t in tested:
        where = [0] * n
        for p, s in enumerate(rows[t]):
            where[s] = p
        position[t] = where
    conflicting = 0
    pairs = set()
    examples = []
    for a in range(n):
        for b in range(n):
            if b == a:
                continue
            for m in range(1, n):
                hits = [t for t in tested if position[t][b] == (position[t][a] + m) % n]
                if len(hits) > 1:
                    conflicting += 1
                    for i in range(len(hits)):
                        for j in range(i + 1, len(hits)):
                            pairs.add((hits[i], hits[j]))
                    if len(examples) < MAX_EXAMPLES:
                        examples.append({"a": a, "b": b, "m": m, "rows": hits})
    return {
        "verdict": "FAIL" if (not_permutation or conflicting) else "PASS",
        "bridge": "row t (t=1..%d) holds at position p the symbol s with (D_t(s)-D_0(s)) mod %d = p" % (k - 1, n),
        "rows": k - 1,
        "rows_not_permutation": not_permutation,
        "rows_tested_for_triples": tested,
        "triples_tested": n * (n - 1) * (n - 1),
        "conflicting_triples": conflicting,
        "conflicting_row_pairs": [list(pair) for pair in sorted(pairs)],
        "conflict_examples": examples,
    }


def check_dm_definition(D, n, k):
    """Literal (Z_n,k;1) difference-matrix definition."""
    failing = []
    checked = 0
    for i in range(k):
        for j in range(i + 1, k):
            checked += 1
            differences = [(D[i][c] - D[j][c]) % n for c in range(n)]
            distinct = len(set(differences))
            if distinct != len(differences):
                failing.append({"rows": [i, j], "distinct_differences": distinct})
    return {
        "verdict": "FAIL" if failing else "PASS",
        "row_pairs_checked": checked,
        "failing_row_pairs": failing,
    }


def bridges_agree(oa, cfr, dm):
    """True iff the three failure patterns relate exactly as proved in report.md."""
    dm_pairs = set(tuple(entry["rows"]) for entry in dm["failing_row_pairs"])
    oa_pairs = set(tuple(entry["coordinates"]) for entry in oa["failing_coordinate_pairs"])
    bad_rows = set(entry["row"] for entry in cfr["rows_not_permutation"])
    conflicts = set(tuple(pair) for pair in cfr["conflicting_row_pairs"])
    if oa_pairs != set((i + 1, j + 1) for (i, j) in dm_pairs):
        return False
    if bad_rows != set(j for (i, j) in dm_pairs if i == 0):
        return False
    expected = set((i, j) for (i, j) in dm_pairs if i >= 1 and i not in bad_rows and j not in bad_rows)
    return conflicts == expected


def own_sha256():
    try:
        with open(os.path.abspath(__file__), "rb") as handle:
            return hashlib.sha256(handle.read()).hexdigest()
    except OSError:
        return None


def evaluate(argv):
    """Return (verdict object, --output path or None)."""
    out = {"checker": CHECKER, "version": VERSION, "checker_sha256": own_sha256()}
    try:
        n, k, path, want, output = parse_cli(argv)
    except UsageError as exc:
        out.update(verdict="USAGE_ERROR", exit_code=2, detail=str(exc))
        return out, None
    out.update(file=path, n=n, k=k)
    try:
        with open(path, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        out.update(verdict="MALFORMED", exit_code=2,
                   malformed={"kind": "UNREADABLE", "line": None, "detail": "%s: %s" % (type(exc).__name__, exc)})
        return out, output
    digest = hashlib.sha256(data).hexdigest()
    out.update(file_sha256=digest, file_bytes=len(data))
    if want is not None:
        out["expected_sha256"] = want
        if digest != want:
            out.update(verdict="SHA256_MISMATCH", exit_code=2)
            return out, output
    try:
        D, blank = parse_raw_dm(data, n, k)
    except InputError as exc:
        out.update(verdict="MALFORMED", exit_code=2,
                   malformed={"kind": exc.kind, "line": exc.line, "detail": exc.detail})
        return out, output
    oa = check_oa_strength2(D, n, k)
    cfr = check_cfr(D, n, k)
    dm = check_dm_definition(D, n, k)
    agree = bridges_agree(oa, cfr, dm)
    passed = agree and all(check["verdict"] == "PASS" for check in (oa, cfr, dm))
    out.update(blank_lines_ignored=blank,
               checks={"oa_strength2": oa, "cfr": cfr, "dm_definition": dm},
               bridge_consistent=agree,
               verdict="PASS" if passed else "FAIL",
               exit_code=0 if passed else 1)
    return out, output


def main(argv):
    out, output = evaluate(argv)
    if output is not None:
        try:
            with open(output, "x", encoding="ascii") as handle:
                handle.write(json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n")
        except OSError as exc:
            out.update(output_error="%s: %s" % (type(exc).__name__, exc), exit_code=2)
    sys.stdout.write(json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n")
    sys.stdout.flush()
    return out["exit_code"]


if __name__ == "__main__":
    try:
        STATUS = main(sys.argv[1:])
    except Exception as exc:  # a crash must never look like a verdict
        sys.stdout.write(json.dumps({"checker": CHECKER, "version": VERSION, "verdict": "INTERNAL_ERROR",
                                     "exit_code": 3, "detail": "%s: %s" % (type(exc).__name__, exc)},
                                    sort_keys=True, separators=(",", ":")) + "\n")
        sys.stdout.flush()
        STATUS = 3
    sys.exit(STATUS)
