```python
#!/usr/bin/env python3
"""Strict checker for a symmetric weighing matrix SW(n, w).

Usage (positional arguments only):

    checker.py EXPECTED_N EXPECTED_W FILE EXPECTED_SHA256

Definition: W is an n x n matrix with entries in {-1, 0, 1}, W = W^T and
W W^T = w I exactly; so every row has exactly w nonzero entries and every
pair of distinct rows has integer inner product 0.

FILE is read exactly once; the SHA-256 of those bytes must equal
EXPECTED_SHA256 exactly (64 lowercase hex digits) and every later check
uses the same bytes.  Required format: strict ASCII, LF line endings with
a final LF, and nothing else:

    SW n w
    <n rows, each of n tokens '-1', '0' or '1' separated by single spaces>

The header n and w are positive decimal integers without sign or leading
zeros and must equal EXPECTED_N and EXPECTED_W (1 <= w <= n).

The mathematics is computed from the parsed matrix with no assumed
structure: every symmetry equality W[i][j] == W[j][i] (i < j), every row
weight, and all n*n entries of the integer Gram matrix W W^T against w I.

Rejection: one line "INVALID <CATEGORY>: <reason>" on stderr, exit 1.
Categories in precedence order: CLI (bad arguments, unreadable FILE),
DIGEST, FORMAT/HEADER (HEADER for the content of line 1, FORMAT
otherwise), ENTRIES, SYMMETRY, WEIGHT, ORTHO.  A token that is a decimal
number whose exact value lies outside {-1, 0, 1} ('2', '-3', '0.5') is
ENTRIES; any other token that is not exactly '-1', '0' or '1' ('x', or a
non-canonical spelling of a ternary value such as '+1', '01', '-0',
'1.0') is FORMAT.  The whole file must pass FORMAT/HEADER before an
ENTRIES verdict is given.

Success: "VALID" and one line of compact JSON on stdout, exit 0.
"""

import hashlib
import json
import sys

TOKEN_VALUES = {"-1": -1, "0": 0, "1": 1}
DIGITS = "0123456789"
LOWER_HEX = "0123456789abcdef"

NONNUMERIC = "nonnumeric"
TERNARY_VALUE = "ternary value"
NONTERNARY_VALUE = "nonternary value"


class Reject(Exception):
    """A failed check: its category and a precise single-line reason."""

    def __init__(self, category, reason):
        Exception.__init__(self, category, reason)
        self.category = category
        self.reason = reason


def show(text, limit=40):
    """repr() of text, truncated so that reasons stay short."""
    if len(text) > limit:
        return "%s...(%d chars)" % (repr(text[:limit]), len(text))
    return repr(text)


def is_digits(text):
    """True iff text is a non-empty run of ASCII decimal digits."""
    return len(text) > 0 and all(ch in DIGITS for ch in text)


def is_canonical_positive(text):
    """True iff text is a positive decimal integer: no sign, no leading 0."""
    return is_digits(text) and text[0] != "0"


def numeric_kind(token):
    """Classify a token that is not exactly '-1', '0' or '1'.

    Numeric tokens are plain decimal literals: optional sign, digits with
    at most one '.', optional e/E exponent with optional sign.  Returns
    NONNUMERIC for anything else, TERNARY_VALUE if the exact value lies in
    {-1, 0, 1} and NONTERNARY_VALUE otherwise.  Decided textually, so it
    is exact for any token length (no float rounding, no int limits).
    """
    body = token[1:] if token[:1] in ("+", "-") else token
    mantissa, has_exponent, exponent = body.lower().partition("e")
    negative_exponent = False
    if has_exponent:
        if exponent[:1] in ("+", "-"):
            negative_exponent = exponent[0] == "-"
            exponent = exponent[1:]
        if not is_digits(exponent):
            return NONNUMERIC
    else:
        exponent = "0"
    int_part, _, frac_part = mantissa.partition(".")
    if not (int_part or frac_part):
        return NONNUMERIC
    for part in (int_part, frac_part):
        if part and not is_digits(part):
            return NONNUMERIC
    digits = int_part + frac_part
    significant = digits.lstrip("0")
    if not significant:
        return TERNARY_VALUE  # exactly zero: '-0', '00', '0.0', ...
    if significant.rstrip("0") != "1":
        return NONTERNARY_VALUE  # |value| is not a power of ten
    # |value| = 10 ** (place + shift): place is the decimal place of the
    # single significant '1', shift the exponent; |value| = 1 iff they
    # cancel exactly.
    place = len(int_part) - 1 - (len(digits) - len(significant))
    exponent = exponent.lstrip("0")
    if len(exponent) > len(str(abs(place))):
        return NONTERNARY_VALUE  # |shift| > |place|, cannot cancel
    shift = int(exponent) if exponent else 0
    if negative_exponent:
        shift = -shift
    return TERNARY_VALUE if place + shift == 0 else NONTERNARY_VALUE


def parse_expected(name, text):
    """CLI: EXPECTED_N / EXPECTED_W must be canonical positive integers."""
    if not is_canonical_positive(text):
        raise Reject("CLI", "%s must be a positive decimal integer without "
                     "sign or leading zeros, got %s" % (name, show(text)))
    try:
        return int(text)
    except ValueError:  # only the interpreter's integer digit limit
        raise Reject("CLI", "%s has too many digits (%d)" % (name, len(text)))


def read_once(path):
    """Read FILE exactly once; all later checks use these same bytes."""
    try:
        with open(path, "rb") as handle:
            return handle.read()
    except OSError as error:
        raise Reject("CLI", "cannot read FILE %s: %s"
                     % (show(path), error.strerror or error))


def check_digest(data, expected):
    """DIGEST: the SHA-256 of the bytes read must equal EXPECTED_SHA256."""
    actual = hashlib.sha256(data).hexdigest()
    if len(expected) != 64 or not all(ch in LOWER_HEX for ch in expected):
        raise Reject("DIGEST", "EXPECTED_SHA256 %s is not 64 lowercase hex "
                     "digits; FILE sha256 is %s" % (show(expected, 72), actual))
    if expected != actual:
        raise Reject("DIGEST", "sha256 mismatch: expected %s, FILE has %s"
                     % (expected, actual))
    return actual


def check_bytes(data):
    """FORMAT: non-empty, printable ASCII plus LF only, final LF."""
    if not data:
        raise Reject("FORMAT", "FILE is empty")
    for offset, byte in enumerate(data):
        if byte == 0x0A or 0x20 <= byte <= 0x7E:
            continue
        line = data.count(b"\n", 0, offset) + 1
        column = offset - data.rfind(b"\n", 0, offset)
        where = "line %d, column %d (byte offset %d)" % (line, column, offset)
        if byte == 0x0D:
            raise Reject("FORMAT", "CR byte at %s; CRLF/CR line endings are "
                         "not allowed, LF only" % where)
        if byte == 0x09:
            raise Reject("FORMAT", "TAB at %s; tokens must be separated by "
                         "single spaces" % where)
        if byte >= 0x80:
            raise Reject("FORMAT", "non-ASCII byte 0x%02X at %s; FILE must "
                         "be strict ASCII" % (byte, where))
        raise Reject("FORMAT", "control byte 0x%02X at %s" % (byte, where))
    if data[-1:] != b"\n":
        raise Reject("FORMAT", "FILE does not end with a final LF")


def check_header(line, n_text, w_text):
    """HEADER: line 1 must be exactly 'SW n w' with the expected n and w."""
    expected = "SW %s %s" % (n_text, w_text)
    if line == "":
        raise Reject("HEADER", "line 1 is blank; expected %s" % show(expected))
    if "#" in line:
        raise Reject("HEADER", "line 1 %s contains '#'; comments are not "
                     "allowed, expected %s" % (show(line), show(expected)))
    fields = line.split(" ")
    if "" in fields:
        raise Reject("HEADER", "line 1 %s has leading, trailing or repeated "
                     "spaces; expected %s" % (show(line), show(expected)))
    if len(fields) != 3:
        raise Reject("HEADER", "line 1 %s has %d fields, expected exactly 3: "
                     "'SW n w'" % (show(line), len(fields)))
    tag, n_field, w_field = fields
    if tag != "SW":
        raise Reject("HEADER", "line 1 must start with 'SW', found %s"
                     % show(tag))
    for name, field in (("n", n_field), ("w", w_field)):
        if not is_canonical_positive(field):
            raise Reject("HEADER", "header %s = %s is not a positive decimal "
                         "integer without sign or leading zeros"
                         % (name, show(field)))
    if n_field != n_text:
        raise Reject("HEADER", "header n = %s does not match EXPECTED_N = %s"
                     % (show(n_field), show(n_text)))
    if w_field != w_text:
        raise Reject("HEADER", "header w = %s does not match EXPECTED_W = %s"
                     % (show(w_field), show(w_text)))


def parse_matrix(data, n_text, w_text, n):
    """FORMAT/HEADER pass over the whole file, then the ENTRIES verdict.

    Returns the matrix as n lists of n ints from {-1, 0, 1}.
    """
    check_bytes(data)
    lines = data.decode("ascii")[:-1].split("\n")
    check_header(lines[0], n_text, w_text)
    matrix = []
    first_bad, bad_count = None, 0
    for r, line in enumerate(lines[1:]):
        lineno = r + 2
        if r >= n:
            what = "blank line" if line == "" else "line %s" % show(line)
            raise Reject("FORMAT", "unexpected %s at line %d after the %d "
                         "matrix rows" % (what, lineno, n))
        where = "line %d (row %d)" % (lineno, r + 1)
        if line.strip(" ") == "":
            raise Reject("FORMAT", "%s is blank; blank rows are not allowed"
                         % where)
        if "#" in line:
            raise Reject("FORMAT", "%s contains '#'; comments are not "
                         "allowed" % where)
        tokens = line.split(" ")
        if "" in tokens:
            if line[0] == " ":
                problem = "a leading space"
            elif line[-1] == " ":
                problem = "a trailing space"
            else:
                problem = "repeated spaces"
            raise Reject("FORMAT", "%s has %s; tokens must be separated by "
                         "single spaces" % (where, problem))
        row = []
        for c, token in enumerate(tokens):
            value = TOKEN_VALUES.get(token)
            if value is None:
                at = "row %d, column %d (line %d)" % (r + 1, c + 1, lineno)
                kind = numeric_kind(token)
                if kind == NONNUMERIC:
                    raise Reject("FORMAT", "%s: unrecognized token %s; "
                                 "entries must be exactly '-1', '0' or '1'"
                                 % (at, show(token)))
                if kind == TERNARY_VALUE:
                    raise Reject("FORMAT", "%s: token %s is a non-canonical "
                                 "spelling of a value in {-1, 0, 1}; entries "
                                 "must be exactly '-1', '0' or '1'"
                                 % (at, show(token)))
                bad_count += 1
                if first_bad is None:
                    first_bad = (at, token)
            row.append(value)
        if len(row) != n:
            raise Reject("FORMAT", "%s has %d tokens, expected exactly %d"
                         % (where, len(row), n))
        matrix.append(row)
    if len(matrix) != n:
        raise Reject("FORMAT", "FILE has %d matrix rows after the header, "
                     "expected exactly %d" % (len(matrix), n))
    if first_bad is not None:
        at, token = first_bad
        raise Reject("ENTRIES", "%s: numeric token %s is not in {-1, 0, 1}; "
                     "%d such token(s) in FILE" % (at, show(token), bad_count))
    return matrix


def check_symmetry(matrix, n):
    """SYMMETRY: every equality W[i][j] == W[j][i] with i < j."""
    first, failures = None, 0
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                failures += 1
                if first is None:
                    first = (i, j)
    if failures:
        i, j = first
        raise Reject("SYMMETRY", "W[%d][%d] = %d but W[%d][%d] = %d "
                     "(1-based); %d of %d symmetry equalities fail"
                     % (i + 1, j + 1, matrix[i][j], j + 1, i + 1,
                        matrix[j][i], failures, n * (n - 1) // 2))


def check_weights(matrix, n, w):
    """WEIGHT: every row has exactly w nonzero entries."""
    first, failures = None, 0
    for i in range(n):
        weight = sum(1 for value in matrix[i] if value != 0)
        if weight != w:
            failures += 1
            if first is None:
                first = (i, weight)
    if failures:
        i, weight = first
        raise Reject("WEIGHT", "row %d has %d nonzero entries, expected "
                     "w = %d; %d of %d rows have the wrong weight"
                     % (i + 1, weight, w, failures, n))


def check_gram(matrix, n, w):
    """ORTHO: every entry of the integer Gram matrix W W^T equals w I.

    All n*n entries are computed as exact integer dot products of rows.
    Returns the number of unordered off-diagonal pairs {i, j} checked;
    both Gram entries (i, j) and (j, i) of every such pair are verified.
    """
    first, failures, pairs = None, 0, 0
    for i in range(n):
        row_i = matrix[i]
        for j in range(n):
            entry = sum(a * b for a, b in zip(row_i, matrix[j]))
            expected = w if i == j else 0
            if entry != expected:
                failures += 1
                if first is None:
                    first = (i, j, entry, expected)
            if i < j:
                pairs += 1
    if failures:
        i, j, entry, expected = first
        raise Reject("ORTHO", "(W W^T)[%d][%d] = %d, expected %d (1-based); "
                     "%d of %d Gram entries differ from w I"
                     % (i + 1, j + 1, entry, expected, failures, n * n))
    return pairs


def run(args):
    """Run every check in category order; return the success report."""
    if len(args) != 4:
        raise Reject("CLI", "expected exactly 4 positional arguments "
                     "EXPECTED_N EXPECTED_W FILE EXPECTED_SHA256, got %d"
                     % len(args))
    n_text, w_text, path, expected_sha256 = args
    n = parse_expected("EXPECTED_N", n_text)
    w = parse_expected("EXPECTED_W", w_text)
    if w > n:
        raise Reject("CLI", "EXPECTED_W = %s exceeds EXPECTED_N = %s; need "
                     "1 <= w <= n" % (show(w_text), show(n_text)))
    data = read_once(path)
    sha256 = check_digest(data, expected_sha256)
    matrix = parse_matrix(data, n_text, w_text, n)
    check_symmetry(matrix, n)
    check_weights(matrix, n, w)
    pairs = check_gram(matrix, n, w)
    return {
        "n": n,
        "w": w,
        "sha256": sha256,
        "entry_count": sum(len(row) for row in matrix),
        "number_of_off_diagonal_pairs_checked": pairs,
        "trace": sum(matrix[i][i] for i in range(n)),
    }


def main(argv):
    try:
        report = run(argv[1:])
    except Reject as rejection:
        sys.stderr.write("INVALID %s: %s\n"
                         % (rejection.category, rejection.reason))
        return 1
    sys.stdout.write("VALID\n")
    sys.stdout.write(json.dumps(report, separators=(",", ":")) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```
