```python
#!/usr/bin/env python3
"""Check a balanced ternary design (BTD) witness file.

Usage: checker.py V B RHO1 RHO2 R K LAMBDA FILE EXPECTED_SHA256

A BTD(V,B;rho1,rho2,R;K,Lambda) (Francel-Hurd; repeated blocks allowed) is a
V x B matrix over {0,1,2} in which every row has exactly rho1 entries 1 and
exactly rho2 entries 2 (row sum R = rho1 + 2 rho2), every column sums to K,
and every two distinct rows have inner product Lambda.

The witness file is the line "BTD V B rho1 rho2 R K Lambda", then exactly V
lines of exactly B tokens from {0,1,2} separated by single spaces, with
exactly one final LF and no other bytes. Numbers are canonical decimals (no
sign, no leading zeros), so the header must be byte-identical to the one
built from the command line. EXPECTED_SHA256 is 64 hex digits.

Prints "VALID" and exits 0 if every check passes. Otherwise prints
"INVALID: <reason>" to stderr and exits 1, naming the first failed check in
the order sha256, final-LF, forbidden-byte, line-count, header, row-length,
alphabet, row-composition, row-sum, column-sum, inner-product. Blank lines
and leading, trailing or repeated spaces count as forbidden bytes. A
malformed command line fails the check it makes impossible to pass: header
for the parameter list, sha256 for the digest or an unreadable FILE.
"""

import hashlib
import sys

DECIMAL_DIGITS = frozenset("0123456789")
HEX_DIGITS = frozenset("0123456789abcdefABCDEF")
# Every byte value that occurs anywhere in a well-formed witness file.
FORMAT_BYTES = b"BTD0123456789 \n"
# A blank line, or a leading, trailing or repeated space; a blank or
# space-led first line is caught by looking at the first byte.
MISPLACED_PAIRS = (b"\n\n", b"\n ", b" \n", b"  ")
ENTRY_VALUES = {b"0": 0, b"1": 1, b"2": 2}


def parse_parameter(text):
    """Return the value of a canonical non-negative decimal, else None."""
    if not text or not set(text) <= DECIMAL_DIGITS:
        return None
    if len(text) > 1 and text[0] == "0":
        return None
    try:
        return int(text)
    except ValueError:  # beyond the interpreter's int conversion limit
        return None


def check(argv):
    """Return None if the witness is valid, else the first failed check."""
    if len(argv) != 10:
        return "header"
    parameter_texts = argv[1:8]
    parameters = [parse_parameter(text) for text in parameter_texts]
    if None in parameters:
        return "header"
    v, b, rho1, rho2, r, k, lam = parameters
    path, expected_sha256 = argv[8], argv[9]
    if len(expected_sha256) != 64 or not set(expected_sha256) <= HEX_DIGITS:
        return "sha256"

    # The only read of the witness file; every check below uses these bytes.
    try:
        with open(path, "rb") as handle:
            data = handle.read()
    except (OSError, ValueError):
        return "sha256"

    if hashlib.sha256(data).hexdigest() != expected_sha256.lower():
        return "sha256"

    if not data.endswith(b"\n") or data.endswith(b"\n\n"):
        return "final-LF"

    if data.translate(None, FORMAT_BYTES):
        return "forbidden-byte"
    if data[:1] in (b"\n", b" ") or any(p in data for p in MISPLACED_PAIRS):
        return "forbidden-byte"

    lines = data[:-1].split(b"\n")
    if len(lines) != v + 1:
        return "line-count"

    if lines[0] != ("BTD " + " ".join(parameter_texts)).encode("ascii"):
        return "header"

    # Every token is non-empty: blank lines and stray spaces were rejected.
    token_rows = [line.split(b" ") for line in lines[1:]]
    for tokens in token_rows:
        if len(tokens) != b:
            return "row-length"
    for tokens in token_rows:
        for token in tokens:
            if token not in ENTRY_VALUES:
                return "alphabet"
    rows = [[ENTRY_VALUES[token] for token in tokens] for tokens in token_rows]

    for row in rows:
        if row.count(1) != rho1 or row.count(2) != rho2:
            return "row-composition"
    for row in rows:
        if sum(row) != r:
            return "row-sum"
    for col in range(b):
        if sum(row[col] for row in rows) != k:
            return "column-sum"
    for i in range(v):
        for j in range(i + 1, v):
            if sum(x * y for x, y in zip(rows[i], rows[j])) != lam:
                return "inner-product"
    return None


def main():
    reason = check(sys.argv)
    if reason is not None:
        print("INVALID: " + reason, file=sys.stderr)
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```
