#!/usr/bin/env python3
"""Independent RDSQS(v) certificate verifier (Python 3 standard library only).

Usage:  checker.py EXPECTED_V FILE EXPECTED_SHA256

V = {0, ..., v-1}.  An SQS(v) is a set of 4-subsets (blocks) of V such that
every 3-subset of V lies in exactly one block.  The derived system at x is
{B - {x} : x in B}, an STS(v-1) on V - {x}.  An RDSQS(v) is an SQS(v) whose
derived system at every point x is resolvable: its triples split into (v-2)/2
parallel classes, each a partition of V - {x} into (v-1)/3 triples.  The
certificate lists the blocks and an explicit resolution for every point.

FILE is read exactly once and its SHA-256 is compared with EXPECTED_SHA256
before any parsing.  Exactly one JSON object is printed on stdout.  Exit
status is 0 iff the certificate is valid, otherwise 1 with an
invariant-specific reason.  No assert statements (identical under python -O),
no writes besides stdout, no network access, no subprocesses.
"""
import sys

sys.dont_write_bytecode = True

import hashlib  # noqa: E402
import json  # noqa: E402
from itertools import combinations  # noqa: E402

DIGITS = frozenset("0123456789")
HEX_DIGITS = frozenset("0123456789abcdef")
UPPER = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DATA_CHARS = DIGITS | UPPER | frozenset(" ")
WHITESPACE_BYTES = frozenset(b" \t\x0b\x0c")
KEYWORDS = frozenset(("RDSQS", "BLOCKS", "POINT", "CLASS"))
MAX_V_DIGITS = 1000  # a larger v would need more than 10^2990 block lines
CHECKS = (
    "parameters", "sha256", "format", "block_count", "distinct_blocks",
    "triple_coverage", "derived_sts", "points_resolved", "classes_per_point",
    "triples_per_class", "class_triple", "class_partition",
    "derived_triple_once",
)


class Invalid(Exception):
    """A violated invariant: check name, precise reason, optional line."""

    def __init__(self, check, reason, line=None):
        Exception.__init__(self, reason)
        self.check = check
        self.reason = reason
        self.line = line


def fail(check, reason, line=None):
    if line is not None:
        reason = "line %d: %s" % (line, reason)
    raise Invalid(check, reason, line)


def show(value, limit=60):
    text = str(value)
    return text if len(text) <= limit else text[:limit] + "..."


def fmt(points):
    return "{" + ",".join(str(p) for p in points) + "}"


def canonical_issue(token):
    """None if token is a canonical decimal numeral, else what is wrong."""
    if not token:
        return "empty"
    if not DIGITS.issuperset(token):
        return "non-digit character %r" % next(c for c in token
                                              if c not in DIGITS)
    if len(token) > 1 and token[0] == "0":
        return "leading zero"
    return None


def lex(data, counts):
    """Byte-level format; return [(line_number, fields)] for data lines."""
    if not data:
        fail("format", "file is empty (expected 'RDSQS v' and a final LF)")
    cr = data.find(b"\r")
    if cr >= 0:
        fail("format", "CR byte (0x0D) found; only LF line endings are "
             "allowed", data.count(b"\n", 0, cr) + 1)
    if not data.endswith(b"\n"):
        fail("format", "last line is not terminated by LF (final LF "
             "missing)", data.count(b"\n") + 1)
    lines = []
    comments = 0
    for number, raw in enumerate(data[:-1].split(b"\n"), 1):
        if raw.startswith(b"#"):
            try:
                raw.decode("utf-8")
            except UnicodeDecodeError as exc:
                fail("format", "comment line is not valid UTF-8 (%s at byte "
                     "%d)" % (exc.reason, exc.start + 1), number)
            comments += 1
            continue
        if not raw:
            fail("format", "blank data line", number)
        if max(raw) >= 0x80:
            column = next(i for i, byte in enumerate(raw, 1) if byte >= 0x80)
            fail("format", "non-ASCII byte 0x%02X at column %d of a data line"
                 % (raw[column - 1], column), number)
        if not raw.strip():
            fail("format", "blank data line (whitespace only)", number)
        if raw[-1] in WHITESPACE_BYTES:
            fail("format", "trailing whitespace on data line", number)
        if raw[0] in WHITESPACE_BYTES:
            fail("format", "leading whitespace on data line", number)
        text = raw.decode("ascii")
        if not DATA_CHARS.issuperset(text):
            column, char = next((i, c) for i, c in enumerate(text, 1)
                                if c not in DATA_CHARS)
            fail("format", "character %r at column %d is not allowed in a "
                 "data line (only digits, A-Z and single spaces)"
                 % (char, column), number)
        if "  " in text:
            fail("format", "consecutive spaces in data line (fields must be "
                 "separated by single spaces)", number)
        lines.append((number, text.split(" ")))
    counts["data_lines"] = len(lines)
    counts["comment_lines"] = comments
    return lines


def parse(lines, v, v_str, n_blocks, n_classes, n_triples, counts):
    """Line grammar; return block lines and per-point resolutions."""
    total = len(lines)
    max_len = len(v_str)

    def text(fields):
        return show(" ".join(fields))

    def points(fields, k, number, what):
        if fields[0][0] in UPPER:
            fail("format", "found '%s' where a %s of %d points was expected"
                 % (text(fields), what, k), number)
        if len(fields) != k:
            fail("format", "%s has %d fields, expected exactly %d points"
                 % (what, len(fields), k), number)
        values = []
        for token in fields:
            issue = canonical_issue(token)
            if issue is not None:
                fail("format", "'%s' is not a canonical decimal point (%s)"
                     % (show(token), issue), number)
            if len(token) > max_len or int(token) >= v:
                fail("format", "point %s is not in V = {0..%d}"
                     % (show(token), v - 1), number)
            values.append(int(token))
        if len(set(values)) != k:
            fail("format", "%s '%s' repeats a point (its %d points must be "
                 "distinct)" % (what, text(fields), k), number)
        return tuple(sorted(values))

    def label(fields, keyword, value, number, where):
        if fields[0] != keyword or len(fields) != 2:
            fail("format", "expected '%s %d'%s, found '%s'"
                 % (keyword, value, where, text(fields)), number)
        issue = canonical_issue(fields[1])
        if issue is not None:
            fail("format", "%s label '%s' is not a canonical decimal (%s)"
                 % (keyword, show(fields[1]), issue), number)
        if fields[1] != str(value):
            fail("format", "expected '%s %d'%s, found '%s %s' (%s labels "
                 "must run 0, 1, 2, ... in order)"
                 % (keyword, value, where, keyword, show(fields[1]), keyword),
                 number)

    # Header line and BLOCKS keyword.
    if total == 0:
        fail("format", "no data lines (expected header 'RDSQS %s')" % v_str)
    number, fields = lines[0]
    if fields[0] != "RDSQS" or len(fields) != 2:
        fail("format", "first data line must be 'RDSQS %s', found '%s'"
             % (v_str, text(fields)), number)
    issue = canonical_issue(fields[1])
    if issue is not None:
        fail("format", "header value '%s' is not a canonical decimal (%s)"
             % (show(fields[1]), issue), number)
    if fields[1] != v_str:
        fail("format", "header declares v=%s but EXPECTED_V=%s"
             % (show(fields[1]), v_str), number)
    if total < 2:
        fail("format", "missing 'BLOCKS' line after the header")
    number, fields = lines[1]
    if fields != ["BLOCKS"]:
        fail("format", "second data line must be 'BLOCKS', found '%s'"
             % text(fields), number)
    blocks_line = number

    # Block lines: everything up to the first POINT line.
    pos = 2
    blocks = []
    while pos < total and lines[pos][1][0] != "POINT":
        number, fields = lines[pos]
        if fields[0] in KEYWORDS:
            fail("format", "unexpected '%s' after %d block lines (expected %d "
                 "block lines, then 'POINT 0')"
                 % (text(fields), len(blocks), n_blocks), number)
        blocks.append((number, points(fields, 4, number, "block line")))
        pos += 1
    counts["blocks"] = len(blocks)
    if len(blocks) != n_blocks:
        fail("block_count", "BLOCKS section has %d block lines, expected "
             "exactly v(v-1)(v-2)/24 = %d" % (len(blocks), n_blocks),
             blocks_line)

    # One POINT section per point, in order 0..v-1.
    resolutions = []
    for x in range(v):
        if pos >= total:
            fail("points_resolved", "file ends after %d of %d POINT sections "
                 "(missing 'POINT %d')" % (x, v, x))
        number, fields = lines[pos]
        if x > 0 and fields[0] == "CLASS":
            fail("classes_per_point", "POINT %d has more than (v-2)/2 = %d "
                 "classes (unexpected '%s')"
                 % (x - 1, n_classes, text(fields)), number)
        label(fields, "POINT", x, number, "")
        point_line = number
        pos += 1
        classes = []
        for j in range(n_classes):
            if pos >= total:
                fail("classes_per_point", "file ends inside POINT %d after %d "
                     "of %d classes" % (x, j, n_classes))
            number, fields = lines[pos]
            if fields[0] == "POINT":
                fail("classes_per_point", "POINT %d has only %d classes, "
                     "expected (v-2)/2 = %d" % (x, j, n_classes), number)
            label(fields, "CLASS", j, number, " in POINT %d" % x)
            class_line = number
            pos += 1
            triples = []
            while pos < total and lines[pos][1][0] not in ("POINT", "CLASS"):
                number, fields = lines[pos]
                triples.append((number, points(fields, 3, number,
                                               "class triple line")))
                pos += 1
            if len(triples) != n_triples:
                fail("triples_per_class", "CLASS %d of POINT %d has %d triple "
                     "lines, expected exactly (v-1)/3 = %d"
                     % (j, x, len(triples), n_triples), class_line)
            classes.append((j, class_line, triples))
        resolutions.append((x, point_line, classes))
    if pos < total:
        number, fields = lines[pos]
        if fields[0] == "CLASS":
            fail("classes_per_point", "POINT %d has more than (v-2)/2 = %d "
                 "classes (unexpected '%s')"
                 % (v - 1, n_classes, text(fields)), number)
        fail("points_resolved", "unexpected '%s' after the last POINT section "
             "(exactly %d POINT sections, 0..%d, are allowed)"
             % (text(fields), v, v - 1), number)
    return blocks, resolutions


def check_sqs(blocks, v, n_blocks, counts):
    """SQS(v): distinct blocks; every 3-subset of V in exactly one block."""
    first_line = {}
    covered = {}
    for number, block in blocks:
        if block in first_line:
            fail("distinct_blocks", "block %s repeats the block at line %d"
                 % (fmt(block), first_line[block]), number)
        first_line[block] = number
        for triple in combinations(block, 3):
            if triple in covered:
                other_line, other = covered[triple]
                fail("triple_coverage", "3-subset %s lies in block %s and also "
                     "in block %s at line %d (must lie in exactly one block)"
                     % (fmt(triple), fmt(block), fmt(other), other_line),
                     number)
            covered[triple] = (number, block)
    counts["distinct_blocks"] = len(first_line)
    if len(first_line) != n_blocks:
        fail("distinct_blocks", "%d distinct blocks, expected %d"
             % (len(first_line), n_blocks))
    n_all = v * (v - 1) * (v - 2) // 6
    all_triples = set(combinations(range(v), 3))
    if len(all_triples) != n_all:
        fail("internal", "enumerated %d 3-subsets of V, expected C(v,3) = %d"
             % (len(all_triples), n_all))
    got = set(covered)
    counts["triples_covered"] = len(got)
    counts["triples_total"] = n_all
    if got != all_triples:
        missing = all_triples - got
        if missing:
            fail("triple_coverage", "%d of the C(v,3) = %d 3-subsets of V lie "
                 "in no block, e.g. %s"
                 % (len(missing), n_all, fmt(min(missing))))
        fail("triple_coverage", "blocks cover sets that are not 3-subsets of "
             "V, e.g. %s" % fmt(min(got - all_triples)))
    return list(first_line)


def derived_systems(blocks, v, counts):
    """Derived system at every x, checked to be an STS(v-1) on V-{x}."""
    derived = [set() for _ in range(v)]
    for block in blocks:
        for x in block:
            derived[x].add(tuple(p for p in block if p != x))
    per_point = (v - 1) * (v - 2) // 6
    for x in range(v):
        triples = derived[x]
        if len(triples) != per_point:
            fail("derived_sts", "derived system at point %d has %d triples, "
                 "expected (v-1)(v-2)/6 = %d" % (x, len(triples), per_point))
        pairs = set()
        for triple in sorted(triples):
            for pair in combinations(triple, 2):
                if pair in pairs:
                    fail("derived_sts", "derived system at point %d is not an "
                         "STS(v-1): pair %s lies in two derived triples"
                         % (x, fmt(pair)))
                pairs.add(pair)
        wanted = set(combinations([y for y in range(v) if y != x], 2))
        if pairs != wanted:
            missing = wanted - pairs
            if missing:
                fail("derived_sts", "derived system at point %d is not an "
                     "STS(v-1): pair %s of V-{%d} lies in no derived triple"
                     % (x, fmt(min(missing)), x))
            fail("derived_sts", "derived system at point %d uses pair %s "
                 "outside V-{%d}" % (x, fmt(min(pairs - wanted)), x))
    counts["derived_triples_per_point"] = per_point
    return derived


def check_resolutions(resolutions, derived, v, n_classes, n_triples, counts):
    """Every POINT x section must be a resolution of the derived system at x."""
    everything = frozenset(range(v))
    resolved = 0
    checked = 0
    counts["points_resolved"] = 0
    for x, point_line, classes in resolutions:
        if x != resolved:
            fail("points_resolved", "POINT %d found where POINT %d was "
                 "expected" % (x, resolved), point_line)
        if len(classes) != n_classes:
            fail("classes_per_point", "POINT %d has %d classes, expected "
                 "(v-2)/2 = %d" % (x, len(classes), n_classes), point_line)
        rest = everything - {x}
        derived_x = derived[x]
        used = {}
        for j, class_line, triples in classes:
            if len(triples) != n_triples:
                fail("triples_per_class", "CLASS %d of POINT %d has %d "
                     "triples, expected (v-1)/3 = %d"
                     % (j, x, len(triples), n_triples), class_line)
            owner = {}
            for number, triple in triples:
                if x in triple:
                    fail("class_triple", "triple %s in CLASS %d of POINT %d "
                         "contains the point %d itself"
                         % (fmt(triple), j, x, x), number)
                if triple not in derived_x:
                    fail("class_triple", "triple %s in CLASS %d of POINT %d is "
                         "not a derived triple at %d (%s is not a block)"
                         % (fmt(triple), j, x, x,
                            fmt(sorted(triple + (x,)))), number)
                if triple in used:
                    first_class, first_line = used[triple]
                    fail("derived_triple_once", "derived triple %s at POINT "
                         "%d is in CLASS %d (line %d) and again in CLASS %d"
                         % (fmt(triple), x, first_class, first_line, j),
                         number)
                used[triple] = (j, number)
                for p in triple:
                    if p in owner:
                        fail("class_partition", "CLASS %d of POINT %d is not a "
                             "partition of V-{%d}: point %d lies in two of its "
                             "triples (lines %d and %d)"
                             % (j, x, x, p, owner[p], number), number)
                    owner[p] = number
                checked += 1
            if set(owner) != rest:
                fail("class_partition", "CLASS %d of POINT %d does not "
                     "partition V-{%d}: missing %s, extra %s"
                     % (j, x, x, show(sorted(rest - set(owner))),
                        show(sorted(set(owner) - rest))), class_line)
        if set(used) != derived_x:
            missing = sorted(derived_x - set(used))
            fail("derived_triple_once", "the classes of POINT %d miss %d "
                 "derived triple(s)%s"
                 % (x, len(missing),
                    ", e.g. " + fmt(missing[0]) if missing else ""),
                 point_line)
        resolved += 1
        counts["points_resolved"] = resolved
    if resolved != v:
        fail("points_resolved", "%d of %d points have a verified resolution"
             % (resolved, v))
    counts["classes_per_point"] = n_classes
    counts["triples_per_class"] = n_triples
    counts["class_triples_checked"] = checked


def run(argv, out, counts):
    if len(argv) != 4:
        fail("usage", "usage: checker.py EXPECTED_V FILE EXPECTED_SHA256 "
             "(got %d arguments)" % (len(argv) - 1))
    v_str, path, sha_arg = argv[1], argv[2], argv[3]
    out["file"] = path
    issue = canonical_issue(v_str)
    if issue is not None:
        fail("usage", "EXPECTED_V '%s' is not a canonical decimal (%s)"
             % (show(v_str), issue))
    if len(v_str) > MAX_V_DIGITS:
        fail("usage", "EXPECTED_V has %d digits (limit %d): no readable "
             "certificate can list v(v-1)(v-2)/24 blocks for such v"
             % (len(v_str), MAX_V_DIGITS))
    v = int(v_str)
    out["v"] = v
    expected_sha = sha_arg.lower()
    if len(expected_sha) != 64 or not HEX_DIGITS.issuperset(expected_sha):
        fail("usage", "EXPECTED_SHA256 must be 64 hexadecimal digits, got "
             "'%s'" % show(sha_arg))
    if v < 4 or (v - 1) % 3 or (v - 2) % 2 or v * (v - 1) * (v - 2) % 24:
        fail("parameters", "v=%d admits no RDSQS(v) certificate: (v-1)/3 "
             "triples per class, (v-2)/2 classes per point and "
             "v(v-1)(v-2)/24 blocks must be integers (v = 4 mod 6, v >= 4)"
             % v)
    n_blocks = v * (v - 1) * (v - 2) // 24
    n_classes = (v - 2) // 2
    n_triples = (v - 1) // 3
    out["expected"] = {
        "blocks": n_blocks,
        "triples_total": v * (v - 1) * (v - 2) // 6,
        "points": v,
        "classes_per_point": n_classes,
        "triples_per_class": n_triples,
    }

    try:
        with open(path, "rb") as handle:
            data = handle.read()  # the single read of FILE
    except OSError as exc:
        fail("io", "cannot read FILE: %s" % exc)
    digest = hashlib.sha256(data).hexdigest()
    out["sha256"] = digest
    out["bytes"] = len(data)
    if digest != expected_sha:
        fail("sha256", "SHA-256 mismatch: expected %s, FILE has %s"
             % (expected_sha, digest))

    lines = lex(data, counts)
    blocks, resolutions = parse(lines, v, v_str, n_blocks, n_classes,
                                n_triples, counts)
    block_list = check_sqs(blocks, v, n_blocks, counts)
    derived = derived_systems(block_list, v, counts)
    check_resolutions(resolutions, derived, v, n_classes, n_triples, counts)


def main(argv):
    out = {"valid": False}
    counts = {}
    valid = False
    try:
        run(argv, out, counts)
        valid = True
    except Invalid as exc:
        out["check"] = exc.check
        out["reason"] = exc.reason
        if exc.line is not None:
            out["line"] = exc.line
    except Exception as exc:  # fail closed on anything unexpected
        out["check"] = "internal"
        out["reason"] = "checker error: %s: %s" % (type(exc).__name__,
                                                   show(exc, 200))
    out["valid"] = valid
    if valid:
        out["checks_passed"] = list(CHECKS)
    out["counts"] = counts
    sys.stdout.write(json.dumps(out) + "\n")
    sys.stdout.flush()
    return 0 if valid else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
