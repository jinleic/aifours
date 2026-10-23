#!/usr/bin/env python3
"""Independent verifier for a gcDCQS(g^n : 0) certificate (Python 3 stdlib only).

usage: checker.py EXPECTED_V EXPECTED_N EXPECTED_G FILE EXPECTED_SHA256

Prints exactly one JSON object on stdout.  Exit status: 0 iff the certificate
is valid; 1 if it is invalid (SHA-256 mismatch, inadmissible expected
parameters, format, CQS or colouring violation); 2 if it could not be checked
at all (bad command line, unreadable FILE, internal error).  "line" in the
report is the 1-based line of FILE at fault (last line + 1 means end of file).
Per-point lists in the report are indexed by the point x = 0..v-1.

Every check is an explicit `if` (no asserts), so all of them survive
`python -O`.  FILE is read exactly once and its SHA-256 is verified before any
parsing.  Nothing is written except the report on stdout; no network, no
subprocesses.
"""

import hashlib
import json
import sys

KEYWORDS = frozenset((b"GCDCQS", b"COLOURS", b"HOLEFREE", b"GROUPS",
                      b"BLOCKS", b"POINT", b"CLASS"))
ALLOWED = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
ASCII_WS = b" \t\x0b\x0c"


class Invalid(Exception):
    """The certificate violates the definition or the file format."""

    def __init__(self, check, reason, line=None):
        Exception.__init__(self, reason)
        self.check = check
        self.reason = reason
        self.line = line


class Usage(Exception):
    """The check could not be carried out (command line or I/O problem)."""


def comb3(m):
    return m * (m - 1) * (m - 2) // 6


def chi_prime(w):
    """chi'(w) exactly as defined; None where it is undefined."""
    if w % 6 == 3:
        return (w - 1) // 2
    if w % 6 == 1:
        if w == 7:
            return 7
        if w == 13:
            return 8
        return (w + 1) // 2
    return None


def decode3(key, v):
    """Inverse of key = (a*v + b)*v + c for a < b < c."""
    return (key // (v * v), key // v % v, key % v)


def fmt(points):
    return "{" + ",".join(str(p) for p in sorted(points)) + "}"


def show(raw, limit=40):
    text = raw.decode("ascii", "replace")
    return repr(text if len(text) <= limit else text[:limit] + "...")


def show_line(tokens):
    return "end of file" if tokens is None else show(b" ".join(tokens), 60)


def cli_uint(text, name):
    if (not text or len(text) > 9 or any(c not in "0123456789" for c in text)
            or (len(text) > 1 and text[0] == "0")):
        raise Usage("%s must be a canonical decimal integer of at most 9 "
                    "digits, got %r" % (name, text))
    return int(text)


def lex_data_line(ln, lineno):
    """Lexical rules for a non-comment line: ASCII tokens, single spaces."""
    if not ln.strip(ASCII_WS):
        raise Invalid("format", "blank (whitespace-only) line", lineno)
    if ln[-1] in ASCII_WS:
        raise Invalid("format", "trailing whitespace", lineno)
    if ln[0] in ASCII_WS:
        raise Invalid("format", "leading whitespace", lineno)
    bad = ln.translate(None, ALLOWED)
    if bad:
        c = bad[0]
        if c >= 0x80:
            why = "non-ASCII byte 0x%02X in a non-comment line" % c
        elif c in b"+-":
            why = "sign %r is not allowed" % chr(c)
        elif c in ASCII_WS:
            why = "whitespace byte 0x%02X; tokens are separated by single spaces" % c
        else:
            why = ("invalid character %r (non-comment lines contain only A-Z, "
                   "0-9 and single spaces)" % chr(c))
        raise Invalid("format", why, lineno)
    if b"  " in ln:
        raise Invalid("format", "tokens must be separated by single spaces", lineno)
    for tok in ln.split(b" "):
        if tok.isdigit():
            if len(tok) > 1 and tok[0] == 0x30:
                raise Invalid("format", "number %s has a leading zero" % show(tok),
                              lineno)
        elif tok.isalpha():
            if tok not in KEYWORDS:
                raise Invalid("format", "unknown keyword %s" % show(tok), lineno)
        else:
            raise Invalid("format", "malformed token %s" % show(tok), lineno)


class Lines:
    """Cursor over the lexically checked non-comment lines."""

    def __init__(self, raw, rows):
        self.raw = raw
        self.rows = rows
        self.k = 0

    def peek(self):
        """(line number, tokens) of the next data line; tokens is None at EOF."""
        if self.k >= len(self.rows):
            return len(self.raw) + 1, None
        i = self.rows[self.k]
        return i + 1, self.raw[i].split(b" ")

    def numeric_next(self):
        """True iff a next data line exists and starts with a number."""
        return self.k < len(self.rows) and self.raw[self.rows[self.k]][:1].isdigit()

    def advance(self):
        self.k += 1

    def expect(self, want, label):
        ln, t = self.peek()
        if t != want:
            raise Invalid("format", "expected %s, got %s" % (label, show_line(t)), ln)
        self.advance()


def run(argv, out):
    if len(argv) != 6:
        raise Usage("expected 5 arguments: EXPECTED_V EXPECTED_N EXPECTED_G "
                    "FILE EXPECTED_SHA256")
    v = cli_uint(argv[1], "EXPECTED_V")
    n = cli_uint(argv[2], "EXPECTED_N")
    g = cli_uint(argv[3], "EXPECTED_G")
    path, want = argv[4], argv[5]
    if len(want) != 64 or any(c not in "0123456789abcdefABCDEF" for c in want):
        raise Usage("EXPECTED_SHA256 must be 64 hexadecimal digits, got %r" % want)
    want = want.lower()
    out["expected"] = {"v": v, "n": n, "g": g, "sha256": want}
    out["file"] = path

    # The single read of FILE; its hash is verified before any parsing.
    try:
        with open(path, "rb") as fh:
            data = fh.read()
    except OSError as e:
        raise Usage("cannot read FILE %r: %s" % (path, e))
    got = hashlib.sha256(data).hexdigest()
    out["sha256"] = got
    if got != want:
        raise Invalid("sha256", "SHA-256 mismatch: FILE hashes to %s, expected %s"
                      % (got, want))

    # Parameters derived from the expected v, n, g.
    if n < 3:
        raise Invalid("parameters", "n = %d < 3" % n)
    if g < 1:
        raise Invalid("parameters", "g = %d < 1" % g)
    if v != n * g:
        raise Invalid("parameters", "v = %d != n*g = %d" % (v, n * g))
    w, h = v - 1, g - 1
    r = chi_prime(w)
    if r is None:
        raise Invalid("parameters", "chi'(w) is undefined for w = v-1 = %d "
                      "(w = %d mod 6, need 1 or 3)" % (w, w % 6))
    if (w - h) % 2:
        raise Invalid("parameters", "s = r - (w-h)/2 is not an integer "
                      "(w-h = %d is odd)" % (w - h))
    s = r - (w - h) // 2
    if s < 0:
        raise Invalid("parameters", "s = r - (w-h)/2 = %d - %d is negative"
                      % (r, (w - h) // 2))
    total = comb3(v) - n * comb3(g)  # number of non-group 3-subsets of X
    if total % 4:
        raise Invalid("parameters", "block count (C(v,3) - n*C(g,3))/4 = %d/4 "
                      "is not an integer" % total)
    nblocks = total // 4
    out["parameters"] = {"w": w, "h": h, "r": r, "s": s, "blocks": nblocks,
                         "non_group_triples": total}
    counts = out["counts"] = {
        "blocks": None,
        "non_group_triples_covered": None,
        "group_triples_covered": None,
        "points_coloured": 0,
        "derived_triples_per_point": [],
        "classes_per_point": [],
        "class_size_multiset_per_point": [],
        "hole_free_classes_per_point": [],
    }
    width = len(str(v - 1))

    def points(tokens, k, lineno, what):
        """Exactly k distinct canonical points of X = {0..v-1}."""
        if len(tokens) != k:
            raise Invalid("format", "%s must list exactly %d points, found %d "
                          "tokens" % (what, k, len(tokens)), lineno)
        pts = []
        for tok in tokens:
            if not tok.isdigit():
                raise Invalid("format", "%s: expected a point, found keyword %s"
                              % (what, show(tok)), lineno)
            p = int(tok) if len(tok) <= width else v
            if p >= v:
                raise Invalid("format", "%s: %s is not a point of X = {0..%d}"
                              % (what, show(tok), v - 1), lineno)
            pts.append(p)
        if len(set(pts)) != k:
            dup = next(p for i, p in enumerate(pts) if p in pts[:i])
            raise Invalid("format", "%s: point %d is repeated (points must be "
                          "distinct)" % (what, dup), lineno)
        return pts

    # Lexical layer: LF only, final LF, no blank lines, UTF-8 comments,
    # non-comment lines made only of canonical tokens and single spaces.
    if not data:
        raise Invalid("format", "empty file")
    cr = data.find(b"\r")
    if cr >= 0:
        raise Invalid("format", "CR byte found (only LF line endings are allowed)",
                      data.count(b"\n", 0, cr) + 1)
    if data[-1] != 0x0A:
        raise Invalid("format", "missing final LF", data.count(b"\n") + 1)
    raw = data.split(b"\n")
    raw.pop()  # the empty remainder after the final LF
    del data
    rows = []
    for i, ln in enumerate(raw):
        if not ln:
            raise Invalid("format", "blank line", i + 1)
        if ln[0] == 0x23:  # '#': comment line, any UTF-8
            try:
                ln.decode("utf-8")
            except UnicodeDecodeError as e:
                raise Invalid("format", "comment line is not valid UTF-8 (%s at "
                              "byte %d)" % (e.reason, e.start), i + 1)
            continue
        lex_data_line(ln, i + 1)
        rows.append(i)
    lines = Lines(raw, rows)

    # Header: GCDCQS v n g / COLOURS r / HOLEFREE s.
    ln, t = lines.peek()
    if t is None or t[0] != b"GCDCQS":
        raise Invalid("header", "first data line must be 'GCDCQS v n g', got %s"
                      % show_line(t), ln)
    if len(t) != 4 or not all(tok.isdigit() for tok in t[1:]):
        raise Invalid("header", "malformed header %s (expected 'GCDCQS v n g')"
                      % show_line(t), ln)
    for tok, name, val in zip(t[1:], "vng", (v, n, g)):
        if tok != b"%d" % val:
            raise Invalid("header", "header %s = %s does not equal EXPECTED_%s = %d"
                          % (name, show(tok), name.upper(), val), ln)
    lines.advance()
    for word, name, val, why in (
            (b"COLOURS", "r", r, "chi'(w) = chi'(%d)" % w),
            (b"HOLEFREE", "s", s, "r - (w-h)/2 = %d - %d" % (r, (w - h) // 2))):
        ln, t = lines.peek()
        if t is None or t[0] != word or len(t) != 2 or not t[1].isdigit():
            raise Invalid("header", "expected '%s %s', got %s"
                          % (word.decode(), name, show_line(t)), ln)
        if t[1] != b"%d" % val:
            raise Invalid("header", "%s %s does not equal %s = %s = %d"
                          % (word.decode(), show(t[1]), name, why, val), ln)
        lines.advance()

    # Groups: exactly n lines of g distinct points that partition X.
    lines.expect([b"GROUPS"], "'GROUPS'")
    groups, group_ln = [], []
    while lines.numeric_next():
        ln, t = lines.peek()
        if len(groups) == n:
            raise Invalid("format", "more than n = %d group lines (or the "
                          "'BLOCKS' line is missing)" % n, ln)
        groups.append(points(t, g, ln, "group line"))
        group_ln.append(ln)
        lines.advance()
    if len(groups) != n:
        raise Invalid("format", "GROUPS has %d lines, expected exactly n = %d"
                      % (len(groups), n), lines.peek()[0])
    grp = [-1] * v
    for gi, pts in enumerate(groups):
        for p in pts:
            if grp[p] >= 0:
                raise Invalid("groups_partition", "groups do not partition X: "
                              "point %d is in the groups at lines %d and %d"
                              % (p, group_ln[grp[p]], group_ln[gi]), group_ln[gi])
            grp[p] = gi
    for p in range(v):
        if grp[p] < 0:
            raise Invalid("groups_partition", "groups do not partition X: point "
                          "%d is in no group" % p)

    # Blocks: exactly (C(v,3) - n*C(g,3))/4 lines of 4 distinct points.
    lines.expect([b"BLOCKS"], "'BLOCKS'")
    blocks, block_ln = [], []
    while lines.numeric_next():
        ln, t = lines.peek()
        if len(blocks) == nblocks:
            raise Invalid("block_count", "more than (C(v,3) - n*C(g,3))/4 = %d "
                          "block lines" % nblocks, ln)
        blocks.append(tuple(sorted(points(t, 4, ln, "block"))))
        block_ln.append(ln)
        lines.advance()
    if len(blocks) != nblocks:
        raise Invalid("block_count", "%d block lines, expected (C(v,3) - "
                      "n*C(g,3))/4 = %d" % (len(blocks), nblocks), lines.peek()[0])
    counts["blocks"] = len(blocks)

    first = {}
    for blk, ln in zip(blocks, block_ln):
        a, b, c, d = blk
        key = ((a * v + b) * v + c) * v + d
        if key in first:
            raise Invalid("distinct_blocks", "block %s at line %d repeats the "
                          "block at line %d" % (fmt(blk), ln, first[key]), ln)
        first[key] = ln
    del first

    for blk, ln in zip(blocks, block_ln):
        a, b, c, d = blk
        for tri in ((a, b, c), (a, b, d), (a, c, d), (b, c, d)):
            if grp[tri[0]] == grp[tri[1]] == grp[tri[2]]:
                raise Invalid("group_triple_in_block", "block %s contains the "
                              "3-subset %s of the group at line %d"
                              % (fmt(blk), fmt(tri), group_ln[grp[tri[0]]]), ln)

    # Every non-group 3-subset in exactly one block: collect the covered
    # 3-subsets (rejecting repeats) and compare them with the explicitly
    # enumerated set of all 3-subsets of X that are not inside a group.
    covered = {}
    for blk, ln in zip(blocks, block_ln):
        a, b, c, d = blk
        for tri in ((a, b, c), (a, b, d), (a, c, d), (b, c, d)):
            key = (tri[0] * v + tri[1]) * v + tri[2]
            if key in covered:
                raise Invalid("triple_coverage", "3-subset %s lies in more than "
                              "one block (lines %d and %d)"
                              % (fmt(tri), covered[key], ln), ln)
            covered[key] = ln
    nongroup = set()
    for a in range(v):
        ga = grp[a]
        for b in range(a + 1, v):
            base = (a * v + b) * v
            if grp[b] != ga:
                nongroup.update(range(base + b + 1, base + v))
            else:
                nongroup.update(base + c for c in range(b + 1, v) if grp[c] != ga)
    if len(nongroup) != total:
        raise RuntimeError("enumerated %d non-group 3-subsets, formula gives %d"
                           % (len(nongroup), total))
    if covered.keys() != nongroup:
        extra = [key for key in covered if key not in nongroup]
        if extra:
            key = min(extra)
            raise Invalid("group_triple_in_block", "3-subset %s inside a group "
                          "lies in the block at line %d"
                          % (fmt(decode3(key, v)), covered[key]), covered[key])
        missing = nongroup.difference(covered)
        raise Invalid("triple_coverage", "non-group 3-subset %s lies in no block "
                      "(%d of %d non-group 3-subsets uncovered)"
                      % (fmt(decode3(min(missing), v)), len(missing), total))
    counts["non_group_triples_covered"] = len(covered)
    counts["group_triples_covered"] = 0
    del covered, nongroup

    # Good colouring of A_x = {B \ {x} : x in B} at every point x.
    inc = [[] for _ in range(v)]  # inc[x]: keys of the derived triples at x
    for a, b, c, d in blocks:
        inc[a].append((b * v + c) * v + d)
        inc[b].append((a * v + c) * v + d)
        inc[c].append((a * v + b) * v + d)
        inc[d].append((a * v + b) * v + c)
    for x in range(v):
        ln, t = lines.peek()
        if t is not None and t[0] == b"CLASS" and x > 0:
            raise Invalid("class_count", "point %d has more than r = %d classes "
                          "(found %s)" % (x - 1, r, show_line(t)), ln)
        if t != [b"POINT", b"%d" % x]:
            raise Invalid("points_coloured", "expected 'POINT %d' (points 0..%d "
                          "in increasing order; %d of %d coloured so far), got %s"
                          % (x, v - 1, x, v, show_line(t)), ln)
        point_ln = ln
        lines.advance()
        derived = set(inc[x])
        hole = set(groups[grp[x]])
        hole.discard(x)
        where = {}  # derived-triple key -> (class, line) at this point
        sizes = []
        holefree = 0
        for j in range(r):
            ln, t = lines.peek()
            if t is None or t[0] == b"POINT":
                raise Invalid("class_count", "point %d has only %d classes, "
                              "expected exactly r = %d" % (x, j, r), ln)
            if t != [b"CLASS", b"%d" % j]:
                raise Invalid("format", "point %d: expected 'CLASS %d' (classes "
                              "0..%d in order), got %s"
                              % (x, j, r - 1, show_line(t)), ln)
            class_ln = ln
            lines.advance()
            used = {}  # point -> line of the triple of this class containing it
            size = 0
            meets_hole = False
            while lines.numeric_next():
                ln, t = lines.peek()
                tri = sorted(points(t, 3, ln, "triple"))
                if x in tri:
                    raise Invalid("derived_triple", "point %d, class %d: triple %s "
                                  "contains %d itself" % (x, j, fmt(tri), x), ln)
                a, b, c = tri
                key = (a * v + b) * v + c
                if key not in derived:
                    raise Invalid("derived_triple", "point %d, class %d: %s is not "
                                  "a derived triple at %d (%s is not a block)"
                                  % (x, j, fmt(tri), x, fmt(tri + [x])), ln)
                if key in where:
                    j0, ln0 = where[key]
                    raise Invalid("exactly_one_class", "point %d: derived triple "
                                  "%s is listed more than once (class %d at line "
                                  "%d, class %d at line %d)"
                                  % (x, fmt(tri), j0, ln0, j, ln), ln)
                for p in tri:
                    if p in used:
                        raise Invalid("class_disjoint", "point %d, class %d: "
                                      "triples are not pairwise disjoint (point "
                                      "%d is in the triples at lines %d and %d)"
                                      % (x, j, p, used[p], ln), ln)
                for p in tri:
                    used[p] = ln
                where[key] = (j, ln)
                size += 1
                if a in hole or b in hole or c in hole:
                    meets_hole = True
                lines.advance()
            if size == 0:
                raise Invalid("class_nonempty", "point %d: class %d is empty (each "
                              "class needs one or more triples)" % (x, j), class_ln)
            sizes.append(size)
            if not meets_hole:
                holefree += 1
        missing = [key for key in inc[x] if key not in where]
        if missing:
            tri = decode3(min(missing), v)
            raise Invalid("exactly_one_class", "point %d: derived triple %s (from "
                          "block %s) is in no class (%d of %d derived triples "
                          "uncoloured)" % (x, fmt(tri), fmt(tri + (x,)),
                                           len(missing), len(inc[x])), point_ln)
        if holefree != s:
            raise Invalid("hole_free_count", "point %d: %d classes contain no point "
                          "of H_x = %s, expected exactly s = %d"
                          % (x, holefree, fmt(hole), s), point_ln)
        counts["points_coloured"] += 1
        counts["derived_triples_per_point"].append(len(inc[x]))
        counts["classes_per_point"].append(len(sizes))
        counts["class_size_multiset_per_point"].append(
            {str(z): sizes.count(z) for z in sorted(set(sizes))})
        counts["hole_free_classes_per_point"].append(holefree)
    ln, t = lines.peek()
    if t is not None:
        if t[0] == b"CLASS":
            raise Invalid("class_count", "point %d has more than r = %d classes "
                          "(found %s)" % (v - 1, r, show_line(t)), ln)
        raise Invalid("format", "unexpected line after the colouring of point %d: %s"
                      % (v - 1, show_line(t)), ln)
    out["valid"] = True


def main(argv):
    out = {"valid": False, "check": None, "reason": None, "line": None}
    code = 2
    try:
        run(argv, out)
        code = 0 if out["valid"] is True else 2
        if code:
            out["check"], out["reason"] = "internal", "verification did not complete"
    except Invalid as e:
        out["check"], out["reason"], out["line"] = e.check, e.reason, e.line
        code = 1
    except Usage as e:
        out["check"], out["reason"] = "usage", str(e)
        code = 2
    except Exception as e:  # a crash must never look like a pass
        out["check"] = "internal"
        out["reason"] = "internal error: %s: %s" % (type(e).__name__, e)
        code = 2
    if code:
        out["valid"] = False
    print(json.dumps(out))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
