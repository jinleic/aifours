#!/usr/bin/env python3
"""Strict witness checker for Bhaskar Rao designs BRD(V, B, R, K, Lambda).

Usage: checker.py V B R K LAMBDA FILE EXPECTED_SHA256

A BRD(V, B, R, K, Lambda) is a V x B matrix over {-1, 0, 1} in which every
row has exactly R nonzeros, every column has exactly K nonzeros, and every
pair of distinct rows has exactly Lambda/2 columns with product +1 and exactly
Lambda/2 columns with product -1 (the other B - Lambda products are 0).
Repeated columns are allowed. The +1 and -1 counts are checked directly,
because W W^T = R I alone does not imply them.

FILE must be, byte for byte:
    BRD V B R K Lambda      header, canonical decimals equal to the CLI values
    V rows of B tokens      each token -1, 0 or 1, separated by single spaces
Every line ends in LF, the file ends in exactly one LF, and no other bytes
are allowed (no comments, blank lines, tabs, CR, ...).

Exit status:
    0  stdout "VALID"
    1  stderr "INVALID: <reason>", naming the first failing check in the order
       sha256, final-LF, forbidden-byte, line-count, header, row-length,
       alphabet, row-weight, column-weight, pair-sign-balance
    2  usage error or unreadable FILE (no verdict given)

Only sys and hashlib are imported and no check uses assert, so the result
is identical under python -O.
"""

import hashlib
import sys

USAGE = "usage: checker.py V B R K LAMBDA FILE EXPECTED_SHA256"
DECIMAL_DIGITS = "0123456789"
LOWER_HEX_DIGITS = "0123456789abcdef"

# Every byte that can occur anywhere in a well-formed witness.
ALLOWED_BYTES = frozenset(b"BRD0123456789- \n")
TOKEN_VALUES = {b"-1": -1, b"0": 0, b"1": 1}


def parse_param(text):
    """Return the value of a canonical positive decimal (ASCII digits, no sign,
    no leading zero), or None."""
    if not text or text[0] == "0" or any(c not in DECIMAL_DIGITS for c in text):
        return None
    try:
        return int(text)
    except ValueError:  # longer than the interpreter's int digit limit
        return None


def nonzeros(entries):
    return sum(1 for x in entries if x != 0)


def first_violation(data, expected_sha256, V, B, R, K, LAMBDA):
    """Return the reason of the first failing check, or None if data is valid."""
    if hashlib.sha256(data).hexdigest() != expected_sha256:
        return "sha256"
    if not data.endswith(b"\n") or data.endswith(b"\n\n"):
        return "final-LF"
    if not ALLOWED_BYTES.issuperset(data):
        return "forbidden-byte"

    lines = data[:-1].split(b"\n")
    if len(lines) != V + 1:
        return "line-count"
    if lines[0] != b"BRD %d %d %d %d %d" % (V, B, R, K, LAMBDA):
        return "header"

    rows = [line.split(b" ") for line in lines[1:]]
    if any(len(tokens) != B for tokens in rows):
        return "row-length"
    if any(tok not in TOKEN_VALUES for tokens in rows for tok in tokens):
        return "alphabet"
    matrix = [[TOKEN_VALUES[tok] for tok in tokens] for tokens in rows]

    if any(nonzeros(row) != R for row in matrix):
        return "row-weight"
    if any(nonzeros(column) != K for column in zip(*matrix)):
        return "column-weight"

    for i in range(V):
        for j in range(i + 1, V):
            products = [x * y for x, y in zip(matrix[i], matrix[j])]
            # #(+1) == #(-1) == Lambda/2 in integer form; odd Lambda never passes.
            if 2 * products.count(1) != LAMBDA or 2 * products.count(-1) != LAMBDA:
                return "pair-sign-balance"
    return None


def usage_error(message):
    sys.stderr.write(f"{USAGE}\nerror: {message}\n")
    return 2


def main(argv):
    if len(argv) != 8:
        return usage_error("expected exactly 7 arguments")
    params = [parse_param(arg) for arg in argv[1:6]]
    if None in params:
        return usage_error("V B R K LAMBDA must be canonical positive decimal integers")
    path, expected_sha256 = argv[6], argv[7]
    if len(expected_sha256) != 64 or any(c not in LOWER_HEX_DIGITS for c in expected_sha256):
        return usage_error("EXPECTED_SHA256 must be 64 lowercase hex digits")

    try:
        with open(path, "rb") as f:
            data = f.read()  # the only read: every check uses these same bytes
    except OSError as exc:
        sys.stderr.write(f"error: cannot read FILE: {exc}\n")
        return 2

    reason = first_violation(data, expected_sha256, *params)
    if reason is not None:
        sys.stderr.write(f"INVALID: {reason}\n")
        return 1
    sys.stdout.write("VALID\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
