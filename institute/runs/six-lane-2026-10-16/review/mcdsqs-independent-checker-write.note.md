```python
#!/usr/bin/env python3
"""Independent verifier for mcDSQS(v) certificates (definitions of Tan-Zhou 2025).

Usage: checker.py EXPECTED_V FILE EXPECTED_SHA256

Prints exactly one JSON object on stdout and exits 0 iff the certificate is
valid, 1 otherwise (usage errors included).  Standard library only; no asserts
(every check survives python -O), no file writes, no network, no subprocesses.
FILE is read exactly once and its SHA-256 is compared with EXPECTED_SHA256
before any parsing.

Checked directly from the definitions:
  * SQS(v): exactly v(v-1)(v-2)/24 distinct 4-subsets of V = {0..v-1}; every
    3-subset lies in exactly one block, compared against all C(v,3) 3-subsets.
  * The derived design at each x has D = (v-1)(v-2)/6 triples and is an STS on
    V - {x}: every pair of V - {x} lies in exactly one derived triple.
  * Minimality is established here, not trusted: a partial parallel class on
    v-1 points has at most M = floor((v-1)/3) triples, so every STS(v-1) needs
    at least L = ceil(D/M) colours.  COLOURS r must equal L; since each derived
    design is an STS(v-1), an explicit L-colouring of it shows that L is the
    minimum chromatic index over all STS(v-1).  (Sound but incomplete: if no
    STS(v-1) attains L, no certificate can pass.)
  * For each x = 0..v-1, every class triple is a derived triple at x that
    excludes x, the triples of each class are pairwise disjoint, and every
    derived triple at x lies in exactly one of the r classes.

Format: LF line endings with a final LF and no CR anywhere.  Lines starting
with '#' are comments anywhere and must be valid UTF-8 (otherwise free-form).
All other lines are printable ASCII without leading or trailing whitespace,
with single-space separators and canonical decimals; blank data lines, leading
zeros and empty classes are rejected.  Points on a line may come in any order;
blocks and triples are compared as sets.
"""
import sys

sys.dont_write_bytecode = True  # the imports below must not create __pycache__

import hashlib
import json
from itertools import combinations

HEX_DIGITS = frozenset("0123456789abcdefABCDEF")
PRINTABLE = bytes(range(0x20, 0x7F))
MAX_V_DIGITS = 18  # a larger v would need more than 10^52 block lines


class Invalid(Exception):
    """A violated invariant: machine-readable name, precise reason, optional line number."""

    def __init__(self, invariant, reason, line=None):
        Exception.__init__(self, reason)
        self.invariant = invariant
        self.reason = reason
        self.line = line


def show(text, limit=60):
    """Untrusted text, truncated for use in a message."""
    if len(text) <= limit:
        return text
    return "%s...(%d chars)" % (text[:limit], len(text))


def fmt(points):
    return "{" + ",".join(str(p) for p in points) + "}"


def unkey(key, v):
    """Inverse of key = (a*v + b)*v + c."""
    ab, c = divmod(key, v)
    a, b = divmod(ab, v)
    return a, b, c


def require_canonical(tok, what, line):
    """Raise unless tok is a canonical decimal: ASCII digits only, no leading zero."""
    if not (tok.isascii() and tok.isdigit()):
        raise Invalid("format.decimal", "%s %r is not a decimal integer" % (what, show(tok)), line)
    if len(tok) > 1 and tok[0] == "0":
        raise Invalid("format.leading_zero", "%s %r has a leading zero" % (what, show(tok)), line)


def data_lines(data):
    """Check the byte-level format; return [(line number, text)] for the non-comment lines."""
    if not data:
        raise Invalid("format.final_lf", "FILE is empty")
    cr = data.find(b"\r")
    if cr >= 0:
        raise Invalid("format.cr", "CR byte at offset %d; only LF line endings are allowed" % cr,
                      data.count(b"\n", 0, cr) + 1)
    if not data.endswith(b"\n"):
        raise Invalid("format.final_lf", "FILE does not end with LF", data.count(b"\n") + 1)
    out = []
    for ln, raw in enumerate(data[:-1].split(b"\n"), 1):
        if raw.startswith(b"#"):
            try:
                raw.decode("utf-8")
            except UnicodeDecodeError as exc:
                raise Invalid("format.comment_utf8",
                              "comment is not valid UTF-8 at byte %d of the line" % (exc.start + 1), ln)
            continue
        if not raw.strip():
            raise Invalid("format.blank_line", "blank data line", ln)
        if raw[-1:].isspace():
            raise Invalid("format.trailing_whitespace", "trailing whitespace on a data line", ln)
        if raw[:1].isspace():
            raise Invalid("format.leading_whitespace", "leading whitespace on a data line", ln)
        bad = raw.translate(None, PRINTABLE)
        if bad:
            kind = "non-ASCII byte" if bad[0] >= 0x80 else "control character"
            raise Invalid("format.ascii", "%s 0x%02x at column %d; data lines must be printable ASCII"
                          % (kind, bad[0], raw.index(bad[:1]) + 1), ln)
        out.append((ln, raw.decode("ascii")))
    return out


def header_value(lines, idx, keyword, name):
    """(line, token) of data line idx+1, which must read 'KEYWORD token' with a canonical decimal."""
    if idx >= len(lines):
        raise Invalid("format.header", "missing data line %d '%s %s'" % (idx + 1, keyword, name))
    ln, text = lines[idx]
    fields = text.split(" ")
    if len(fields) != 2 or fields[0] != keyword:
        raise Invalid("format.header", "data line %d must be '%s %s', got %r"
                      % (idx + 1, keyword, name, show(text)), ln)
    require_canonical(fields[1], "%s in the %s line" % (name, keyword), ln)
    return ln, fields[1]


def parse_points(text, k, v, width, line, what):
    """The k distinct points of V listed on one data line, sorted ascending."""
    toks = text.split(" ")
    if "" in toks:
        raise Invalid("format.spacing", "%s line has consecutive spaces" % what, line)
    if len(toks) != k:
        raise Invalid("format.arity", "%s line must have exactly %d points, found %d fields"
                      % (what, k, len(toks)), line)
    pts = []
    for tok in toks:
        require_canonical(tok, what + " point", line)
        p = int(tok) if len(tok) <= width else v  # longer canonical tokens are >= v anyway
        if p >= v:
            raise Invalid("range.point", "%s point %s is not in V = {0..%d}" % (what, show(tok), v - 1), line)
        pts.append(p)
    if len(set(pts)) != k:
        raise Invalid("format.distinct_points", "%s line repeats a point: %r" % (what, text), line)
    pts.sort()
    return tuple(pts)


def expect_point(lines, i, x, v):
    """Line number of lines[i], which must be 'POINT x'."""
    if i >= len(lines):
        raise Invalid("colour.all_points",
                      "only %d of the %d points are coloured: 'POINT %d' is missing" % (x, v, x))
    ln, text = lines[i]
    fields = text.split(" ")
    if len(fields) != 2 or fields[0] != "POINT":
        raise Invalid("format.unexpected_line", "expected 'POINT %d', got %r" % (x, show(text)), ln)
    require_canonical(fields[1], "point in the POINT line", ln)
    if fields[1] != str(x):
        raise Invalid("colour.point_order",
                      "expected 'POINT %d' (points are coloured in order 0..%d), got 'POINT %s'"
                      % (x, v - 1, show(fields[1])), ln)
    return ln


def expect_class(lines, i, x, j, r):
    """Line number of lines[i], which must be 'CLASS j' (inside the section of POINT x)."""
    if i >= len(lines):
        raise Invalid("colour.class_count",
                      "point %d has only %d of the r = %d colour classes (end of file)" % (x, j, r))
    ln, text = lines[i]
    fields = text.split(" ")
    if fields[0] == "POINT":
        raise Invalid("colour.class_count",
                      "point %d has only %d of the r = %d colour classes" % (x, j, r), ln)
    if len(fields) != 2 or fields[0] != "CLASS":
        raise Invalid("format.unexpected_line", "expected 'CLASS %d' of POINT %d, got %r"
                      % (j, x, show(text)), ln)
    require_canonical(fields[1], "class index in the CLASS line", ln)
    if fields[1] != str(j):
        raise Invalid("colour.class_order",
                      "expected 'CLASS %d' of POINT %d (classes are numbered 0..%d in order), got 'CLASS %s'"
                      % (j, x, r - 1, show(fields[1])), ln)
    return ln


def verify(argv, stats):
    if len(argv) != 4:
        raise Invalid("argument.count", "usage: checker.py EXPECTED_V FILE EXPECTED_SHA256 (got %d arguments)"
                      % (len(argv) - 1))
    v_arg, path, sha_arg = argv[1:]
    if (not (v_arg.isascii() and v_arg.isdigit()) or (len(v_arg) > 1 and v_arg[0] == "0")
            or len(v_arg) > MAX_V_DIGITS):
        raise Invalid("argument.expected_v", "EXPECTED_V must be a canonical decimal of at most %d digits, got %r"
                      % (MAX_V_DIGITS, show(v_arg)))
    v = int(v_arg)
    if v < 4 or v % 6 not in (2, 4):
        raise Invalid("argument.expected_v",
                      "EXPECTED_V = %d is not admissible: an SQS(v) whose derived STS(v-1) has M >= 1 "
                      "requires v >= 4 and v = 2 or 4 (mod 6)" % v)
    if len(sha_arg) != 64 or not all(c in HEX_DIGITS for c in sha_arg):
        raise Invalid("argument.expected_sha256", "EXPECTED_SHA256 must be exactly 64 hexadecimal digits")
    expected_sha = sha_arg.lower()

    try:
        with open(path, "rb") as fh:
            data = fh.read()  # the only read of FILE
    except OSError as exc:
        raise Invalid("io.read", "cannot read FILE: %s" % exc)
    actual_sha = hashlib.sha256(data).hexdigest()
    stats["sha256"] = actual_sha
    if actual_sha != expected_sha:
        raise Invalid("sha256.mismatch", "SHA-256 of FILE is %s, expected %s; nothing was parsed"
                      % (actual_sha, expected_sha))

    lines = data_lines(data)
    n = len(lines)
    D = (v - 1) * (v - 2) // 6  # triples of any STS(v-1), in particular of each derived design
    M = (v - 1) // 3            # a partial parallel class on v-1 points has at most M triples
    L = -(-D // M)              # ceil(D/M): every STS(v-1) needs at least L colours
    stats.update(v=v, D=D, M=M, L=L)

    ln, tok = header_value(lines, 0, "MCDSQS", "v")
    if tok != str(v):
        raise Invalid("header.v", "certificate declares v = %s but EXPECTED_V = %d" % (show(tok), v), ln)
    ln, tok = header_value(lines, 1, "COLOURS", "r")
    if tok != str(L):
        if len(tok) < len(str(L)) or (len(tok) == len(str(L)) and tok < str(L)):
            why = "r < L, so r*M < D and no STS(v-1) can be r-coloured"
        else:
            why = "r > L, so minimality of r is not established by the counting bound (r must equal L)"
        raise Invalid("colours.r_equals_L", "COLOURS r = %s but L = ceil(D/M) = ceil(%d/%d) = %d: %s"
                      % (show(tok), D, M, L, why), ln)
    r = L
    stats["r"] = r
    if n < 3:
        raise Invalid("format.header", "missing data line 3 'BLOCKS'")
    if lines[2][1] != "BLOCKS":
        raise Invalid("format.header", "data line 3 must be 'BLOCKS', got %r" % show(lines[2][1]), lines[2][0])

    # Blocks: the data lines after BLOCKS up to the next keyword (letter-initial) line.
    expected_blocks = v * (v - 1) * (v - 2) // 24
    stats["expected_blocks"] = expected_blocks
    width = len(str(v - 1))
    block_line = {}  # 4-subset key -> line number
    blocks = []      # (a, b, c, d, line) with a < b < c < d
    i = 3
    while i < n and not lines[i][1][0].isalpha():
        ln, text = lines[i]
        a, b, c, d = parse_points(text, 4, v, width, ln, "block")
        key = ((a * v + b) * v + c) * v + d
        if key in block_line:
            raise Invalid("blocks.distinct", "block %s repeats the block on line %d"
                          % (fmt((a, b, c, d)), block_line[key]), ln)
        block_line[key] = ln
        blocks.append((a, b, c, d, ln))
        i += 1
    stats["blocks"] = len(blocks)
    if len(blocks) != expected_blocks:
        raise Invalid("blocks.count", "found %d block lines, need exactly v(v-1)(v-2)/24 = %d"
                      % (len(blocks), expected_blocks))

    # SQS: each 3-subset in at most one block, then compared with all C(v,3) 3-subsets of V.
    # Memory proportional to v is allocated only now, once the block count has bounded v by FILE size.
    total = v * (v - 1) * (v - 2) // 6
    stats["total_3_subsets"] = total
    covered = {}                         # 3-subset key -> line of the block containing it
    derived = [set() for _ in range(v)]  # derived[x] = keys of B - {x} over the blocks B containing x
    for a, b, c, d, ln in blocks:
        for x, t in ((d, (a, b, c)), (c, (a, b, d)), (b, (a, c, d)), (a, (b, c, d))):
            key = (t[0] * v + t[1]) * v + t[2]
            if key in covered:
                raise Invalid("sqs.exactly_once", "3-subset %s lies in more than one block (lines %d and %d)"
                              % (fmt(t), covered[key], ln), ln)
            covered[key] = ln
            derived[x].add(key)
    for t in combinations(range(v), 3):
        if (t[0] * v + t[1]) * v + t[2] not in covered:
            raise Invalid("sqs.exactly_once", "3-subset %s lies in no block" % fmt(t))
    if len(covered) != total:
        raise Invalid("sqs.exactly_once", "blocks cover %d distinct 3-subsets, but V has C(v,3) = %d"
                      % (len(covered), total))
    stats["triples_covered"] = len(covered)

    # Derived designs: D triples each, forming an STS on V - {x}.
    pair_count = (v - 1) * (v - 2) // 2
    for x in range(v):
        if len(derived[x]) != D:
            raise Invalid("derived.size", "derived design at %d has %d triples, expected D = %d"
                          % (x, len(derived[x]), D))
        pairs = set()
        for key in derived[x]:
            a, b, c = unkey(key, v)
            for pk in (a * v + b, a * v + c, b * v + c):
                if pk in pairs:
                    raise Invalid("derived.sts", "derived design at %d is not an STS: pair {%d,%d} lies in "
                                  "two triples" % (x, pk // v, pk % v))
                pairs.add(pk)
        if len(pairs) != pair_count:
            raise Invalid("derived.sts", "derived design at %d covers %d of the %d pairs of V - {%d}"
                          % (x, len(pairs), pair_count, x))
    stats["derived_sts_checked"] = v

    # Colourings: POINT 0..v-1 in order, each with CLASS 0..r-1 in order.
    stats["points_coloured"] = 0
    class_sizes = []
    for x in range(v):
        point_ln = expect_point(lines, i, x, v)
        i += 1
        dx = derived[x]
        coloured = {}  # derived triple key at x -> (class index, line)
        sizes = []
        for j in range(r):
            class_ln = expect_class(lines, i, x, j, r)
            i += 1
            used = {}  # point -> line of the triple of this class containing it
            size = 0
            while i < n and not lines[i][1][0].isalpha():
                ln, text = lines[i]
                t = parse_points(text, 3, v, width, ln, "class triple")
                if x in t:
                    raise Invalid("colour.excludes_x", "triple %s in CLASS %d of POINT %d contains the point %d"
                                  % (fmt(t), j, x, x), ln)
                key = (t[0] * v + t[1]) * v + t[2]
                if key not in dx:
                    raise Invalid("colour.derived_triple",
                                  "triple %s in CLASS %d of POINT %d is not a derived triple at %d: %s is not a block"
                                  % (fmt(t), j, x, x, fmt(sorted(t + (x,)))), ln)
                if key in coloured:
                    pj, pln = coloured[key]
                    raise Invalid("colour.exactly_once",
                                  "derived triple %s at point %d occurs twice: CLASS %d (line %d) and CLASS %d (line %d)"
                                  % (fmt(t), x, pj, pln, j, ln), ln)
                for p in t:
                    if p in used:
                        raise Invalid("colour.disjoint",
                                      "CLASS %d of POINT %d is not a partial parallel class: point %d is in the "
                                      "triples on lines %d and %d" % (j, x, p, used[p], ln), ln)
                for p in t:
                    used[p] = ln
                coloured[key] = (j, ln)
                size += 1
                i += 1
            if size == 0:
                raise Invalid("format.empty_class", "CLASS %d of POINT %d has no triples" % (j, x), class_ln)
            if size > M:  # implied by disjointness on V - {x}; checked directly as the bound behind L
                raise Invalid("colour.ppc_bound", "CLASS %d of POINT %d has %d > M = %d triples"
                              % (j, x, size, M), class_ln)
            sizes.append(size)
        if i < n and lines[i][1].split(" ")[0] == "CLASS":
            raise Invalid("colour.class_count", "point %d has more than r = %d colour classes: %r"
                          % (x, r, show(lines[i][1])), lines[i][0])
        missing = dx.difference(coloured)
        if missing:
            raise Invalid("colour.exactly_once",
                          "%d of the D = %d derived triples at point %d are in no class, e.g. %s"
                          % (len(missing), D, x, ", ".join(fmt(unkey(k, v)) for k in sorted(missing)[:5])),
                          point_ln)
        class_sizes.append(sizes)
        stats["points_coloured"] = x + 1
    if i < n:
        raise Invalid("format.trailing_data", "unexpected data line after the colouring of the last point %d: %r"
                      % (v - 1, show(lines[i][1])), lines[i][0])

    multisets = []
    for x, sizes in enumerate(class_sizes):
        mult = {}
        for size in sizes:
            mult[size] = mult.get(size, 0) + 1
        multisets.append({"point": x, "class_size_counts": {str(s): mult[s] for s in sorted(mult)}})
    stats["class_size_multiset_per_point"] = multisets
    return stats


def main(argv):
    stats = {}
    try:
        report = verify(argv, stats)
    except Invalid as exc:
        out = {"valid": False, "invariant": exc.invariant, "reason": exc.reason}
        if exc.line is not None:
            out["line"] = exc.line
        out.update(stats)
        return out, 1
    except Exception as exc:  # fail closed: any unexpected error is a rejection
        out = {"valid": False, "invariant": "internal",
               "reason": "unexpected %s: %s" % (type(exc).__name__, exc)}
        out.update(stats)
        return out, 1
    out = {"valid": True}
    out.update(report)
    return out, 0


if __name__ == "__main__":
    result, status = main(sys.argv)
    sys.stdout.write(json.dumps(result) + "\n")
    sys.stdout.flush()
    sys.exit(status)
```
