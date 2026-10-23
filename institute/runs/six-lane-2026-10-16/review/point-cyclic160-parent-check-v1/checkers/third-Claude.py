#!/usr/bin/env python3
"""Independent verifier: point-cyclic resolution of a cyclic 2-(v,4,1) design.

Usage: checker.py EXPECTED_V FILE EXPECTED_SHA256

Certificate format (ASCII only, LF line endings, final LF, no comments, no
blank lines, no leading/trailing whitespace, single spaces, no leading zeros):
    POINT-CYCLIC-RESOLUTION v 4 c b        with c = (v-1)/3 and b = v/4
followed by exactly c*b block lines
    j p1 p2 p3 p4                          with 0 <= p1 < p2 < p3 < p4 < v
where the k-th block line (k = 0, 1, ...) carries class index j = k // b.

Checked directly: SHA-256 of the bytes (before any parsing); the exact
format; v = EXPECTED_V and v mod 12 = 4; block count v(v-1)/12; distinct
blocks; every block in exactly one class; every class a partition of
V = Z_v; every 2-subset of V in exactly one block (against all C(v,2)
pairs); the block collection invariant under s(x) = x+1 mod v; s mapping
every class onto a listed class.  Reports the orbit lengths (sorted, one
entry per orbit) of the classes and of the blocks under s.

Prints exactly one JSON object.  Exit status: 0 iff the certificate is
valid; 1 if it is invalid ("check" names the failed invariant, "reason"
gives the details); 2 on a usage error, an unreadable FILE or an internal
error.  Standard library only, no asserts, FILE is read exactly once, and
nothing is written except the JSON object on stdout.
"""

import hashlib
import json
import sys

USAGE = "checker.py EXPECTED_V FILE EXPECTED_SHA256"
KEYWORD = "POINT-CYCLIC-RESOLUTION"
K = 4
PAIR_POSITIONS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
DIGITS = frozenset("0123456789")
HEX_DIGITS = frozenset("0123456789abcdefABCDEF")
HEADER_CHARS = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZ-0123456789 ")
BLOCK_LINE_CHARS = frozenset("0123456789 ")
MAX_V_DIGITS = 18
CHECKS = ("sha256", "encoding", "format", "header", "class_index",
          "class_sequence", "point_range", "point_order", "line_count",
          "block_count", "distinct_blocks", "block_in_one_class",
          "parallel_class", "pair_coverage", "block_invariance",
          "class_invariance")


class Usage(Exception):
    """Bad command line (exit 2)."""


class Invalid(Exception):
    """Certificate rejected (exit 1)."""

    def __init__(self, check, reason, **extra):
        Exception.__init__(self, reason)
        self.check = check
        self.reason = reason
        self.extra = extra


def short(s, limit=32):
    """Truncate a possibly huge string for use in a message."""
    return s if len(s) <= limit else s[:limit] + "...[%d chars]" % len(s)


def fmt_block(block):
    return "{" + ",".join(str(x) for x in block) + "}"


def is_decimal(tok):
    return tok != "" and all(ch in DIGITS for ch in tok)


def shift(block, v):
    """s(B) = {x+1 mod v : x in B}, as a sorted tuple."""
    return tuple(sorted((x + 1) % v for x in block))


def parse_args(argv):
    if len(argv) != 4:
        raise Usage("expected 3 arguments, got %d" % (len(argv) - 1))
    v_arg, path, sha_arg = argv[1], argv[2], argv[3]
    if not is_decimal(v_arg) or v_arg[0] == "0" or len(v_arg) > MAX_V_DIGITS:
        raise Usage("EXPECTED_V must be a positive decimal integer without "
                    "leading zeros (at most %d digits), got %r"
                    % (MAX_V_DIGITS, short(v_arg)))
    if len(sha_arg) != 64 or not HEX_DIGITS.issuperset(sha_arg):
        raise Usage("EXPECTED_SHA256 must be 64 hexadecimal digits, got %r"
                    % short(sha_arg))
    return int(v_arg), path, sha_arg.lower()


def split_fields(line, lineno, allowed):
    """Check the character-level shape of one line and split it on spaces."""
    if line == "":
        raise Invalid("format", "line %d is blank" % lineno, line=lineno)
    if not allowed.issuperset(line):
        col, ch = next((i, x) for i, x in enumerate(line, 1)
                       if x not in allowed)
        if ch == "#":
            hint = "; comments are not allowed"
        elif ch in "\t\x0b\x0c":
            hint = "; fields must be separated by single spaces"
        elif ch in "+-":
            hint = "; numbers must be unsigned"
        else:
            hint = ""
        raise Invalid("format", "line %d, column %d: character %r is not "
                      "allowed%s" % (lineno, col, ch, hint),
                      line=lineno, column=col)
    if line.strip(" ") == "":
        raise Invalid("format", "line %d is blank (spaces only)" % lineno,
                      line=lineno)
    if line[0] == " ":
        raise Invalid("format", "line %d has leading whitespace" % lineno,
                      line=lineno)
    if line[-1] == " ":
        raise Invalid("format", "line %d has trailing whitespace" % lineno,
                      line=lineno)
    if "  " in line:
        raise Invalid("format", "line %d has consecutive spaces; fields must "
                      "be separated by single spaces" % lineno, line=lineno)
    return line.split(" ")


def parse_nat(tok, what, lineno, maximum, range_check):
    """Canonical decimal (no sign, no leading zero) in 0..maximum."""
    if not is_decimal(tok):
        raise Invalid("format", "line %d: %s %r is not a decimal integer"
                      % (lineno, what, short(tok)), line=lineno)
    if len(tok) > 1 and tok[0] == "0":
        raise Invalid("format", "line %d: %s %r has a leading zero"
                      % (lineno, what, short(tok)), line=lineno)
    # Length test first, so an over-long digit string is never converted.
    if len(tok) > len(str(maximum)) or int(tok) > maximum:
        raise Invalid(range_check, "line %d: %s %s is out of range 0..%d"
                      % (lineno, what, short(tok), maximum), line=lineno)
    return int(tok)


def parse_header(line, expected_v):
    toks = split_fields(line, 1, HEADER_CHARS)
    if len(toks) != 5:
        raise Invalid("header", "line 1: header must be '%s v 4 c b' "
                      "(5 fields), found %d field(s)" % (KEYWORD, len(toks)),
                      line=1)
    if toks[0] != KEYWORD:
        raise Invalid("header", "line 1: first field must be %r, found %r"
                      % (KEYWORD, short(toks[0])), line=1)
    for name, tok in zip(("v", "k", "c", "b"), toks[1:]):
        if not is_decimal(tok):
            raise Invalid("header", "line 1: header field %s=%r is not a "
                          "decimal integer" % (name, short(tok)), line=1)
        if len(tok) > 1 and tok[0] == "0":
            raise Invalid("header", "line 1: header field %s=%r has a "
                          "leading zero" % (name, short(tok)), line=1)
    # The fields are canonical decimals, so string equality is numeric
    # equality (and no over-long digit string is ever converted).
    if toks[1] != str(expected_v):
        raise Invalid("header", "line 1: header v=%s does not equal "
                      "EXPECTED_V=%d" % (short(toks[1]), expected_v), line=1)
    v = expected_v
    if v % 12 != 4:
        raise Invalid("header", "line 1: v=%d is not congruent to 4 mod 12 "
                      "(v mod 12 = %d)" % (v, v % 12), line=1)
    if toks[2] != str(K):
        raise Invalid("header", "line 1: block size field is %s, must be %d"
                      % (short(toks[2]), K), line=1)
    c, b = (v - 1) // 3, v // 4
    if toks[3] != str(c):
        raise Invalid("header", "line 1: c=%s, must be (v-1)/3 = %d"
                      % (short(toks[3]), c), line=1)
    if toks[4] != str(b):
        raise Invalid("header", "line 1: b=%s, must be v/4 = %d"
                      % (short(toks[4]), b), line=1)
    return v, c, b


def class_sequence_problem(j, k, b, prev):
    """Why class index j may not appear on block line k (0-based), or None.

    The only admissible sequence is b zeros, b ones, ..., b copies of c-1,
    i.e. block line k carries k // b.  prev is the index on block line k-1.
    """
    if j == k // b:
        return None
    if k == 0:
        return "the first block line has class index %d, must be 0" % j
    if j < prev:
        return ("class index %d follows %d; class indices must be "
                "nondecreasing" % (j, prev))
    if j == prev:
        return "class %d has more than b=%d blocks" % (j, b)
    if k % b:
        return ("class %d has only %d of b=%d blocks when class %d starts"
                % (prev, k % b, b, j))
    return ("class index jumps from %d to %d; class %d is missing"
            % (prev, j, prev + 1))


def verify(data, expected_v):
    """Return the report for a valid certificate; raise Invalid otherwise."""
    # Byte level: ASCII only, no CR, final LF.
    if not data:
        raise Invalid("format", "file is empty")
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError as exc:
        off = exc.start
        raise Invalid("encoding", "non-ASCII byte 0x%02x at byte offset %d "
                      "(line %d)" % (data[off], off,
                                     data.count(b"\n", 0, off) + 1),
                      offset=off)
    off = data.find(b"\r")
    if off >= 0:
        raise Invalid("encoding", "CR byte at byte offset %d (line %d); line "
                      "endings must be LF only"
                      % (off, data.count(b"\n", 0, off) + 1), offset=off)
    if not text.endswith("\n"):
        raise Invalid("format", "file does not end with LF")
    lines = text.split("\n")[:-1]

    v, c, b = parse_header(lines[0], expected_v)

    # Block lines: c*b of them, block line k in class k // b.
    blocks = []    # blocks[i]: the 4-tuple on file line i+2
    class_of = []  # class_of[i]: its class index
    prev = -1
    for k, line in enumerate(lines[1:]):
        lineno = k + 2
        toks = split_fields(line, lineno, BLOCK_LINE_CHARS)
        if len(toks) != 1 + K:
            raise Invalid("format", "line %d: expected 5 fields "
                          "'j p1 p2 p3 p4', found %d" % (lineno, len(toks)),
                          line=lineno)
        j = parse_nat(toks[0], "class index", lineno, c - 1, "class_index")
        problem = class_sequence_problem(j, k, b, prev)
        if problem is not None:
            raise Invalid("class_sequence", "line %d: %s" % (lineno, problem),
                          line=lineno)
        pts = [parse_nat(t, "point", lineno, v - 1, "point_range")
               for t in toks[1:]]
        for i in range(K - 1):
            if pts[i] >= pts[i + 1]:
                raise Invalid("point_order", "line %d: points must satisfy "
                              "p1<p2<p3<p4, but p%d=%d is not less than "
                              "p%d=%d" % (lineno, i + 1, pts[i], i + 2,
                                          pts[i + 1]), line=lineno)
        blocks.append(tuple(pts))
        class_of.append(j)
        prev = j
    n = len(blocks)
    if n != c * b:
        # More than c*b block lines already failed the class-sequence check.
        if n == 0:
            detail = "there are no block lines"
        elif n % b:
            detail = ("the file ends while class %d has only %d of b=%d "
                      "blocks" % (prev, n % b, b))
        elif prev + 2 == c:
            detail = ("the file ends after class %d; class %d is missing"
                      % (prev, c - 1))
        else:
            detail = ("the file ends after class %d; classes %d..%d are "
                      "missing" % (prev, prev + 1, c - 1))
        raise Invalid("line_count", "%s (%d block lines, expected c*b = %d)"
                      % (detail, n, c * b))

    # Block count; distinct blocks, each listed in exactly one class.
    if n != v * (v - 1) // 12:
        raise Invalid("block_count", "%d blocks, but a 2-(%d,4,1) design has "
                      "v(v-1)/12 = %d" % (n, v, v * (v - 1) // 12))
    first = {}  # block -> index of the line listing it
    for i, blk in enumerate(blocks):
        i0 = first.get(blk)
        if i0 is not None:
            if class_of[i0] == class_of[i]:
                raise Invalid("distinct_blocks", "block %s is listed twice in "
                              "class %d (lines %d and %d)"
                              % (fmt_block(blk), class_of[i], i0 + 2, i + 2),
                              line=i + 2)
            raise Invalid("block_in_one_class", "block %s is listed in class "
                          "%d (line %d) and in class %d (line %d); blocks must "
                          "be distinct, each in exactly one class"
                          % (fmt_block(blk), class_of[i0], i0 + 2,
                             class_of[i], i + 2), line=i + 2)
        first[blk] = i
    block_set = frozenset(first)

    # Every class is a parallel class: its b blocks partition V.
    for j in range(c):
        owner = [-1] * v
        for i in range(j * b, (j + 1) * b):
            for x in blocks[i]:
                if owner[x] >= 0:
                    raise Invalid("parallel_class", "class %d is not a "
                                  "partition of V: point %d lies in %s (line "
                                  "%d) and in %s (line %d)"
                                  % (j, x, fmt_block(blocks[owner[x]]),
                                     owner[x] + 2, fmt_block(blocks[i]), i + 2),
                                  line=i + 2)
                owner[x] = i
        if -1 in owner:
            raise Invalid("parallel_class", "class %d is not a partition of "
                          "V: point %d lies in none of its blocks"
                          % (j, owner.index(-1)))

    # Every 2-subset of V lies in exactly one block.
    npairs = v * (v - 1) // 2
    hit = bytearray(v * v)  # hit[x*v + y] = 1 once {x,y} (x < y) is covered
    for i, blk in enumerate(blocks):
        for p, q in PAIR_POSITIONS:
            x, y = blk[p], blk[q]
            if hit[x * v + y]:
                i0 = next(h for h in range(i)
                          if x in blocks[h] and y in blocks[h])
                raise Invalid("pair_coverage", "pair {%d,%d} lies in more "
                              "than one block: %s (line %d) and %s (line %d)"
                              % (x, y, fmt_block(blocks[i0]), i0 + 2,
                                 fmt_block(blk), i + 2), pair=[x, y])
            hit[x * v + y] = 1
    for x in range(v):  # compare against the full set of C(v,2) pairs
        for y in range(x + 1, v):
            if not hit[x * v + y]:
                raise Invalid("pair_coverage", "pair {%d,%d} lies in no block"
                              % (x, y), pair=[x, y])
    pairs_covered = hit.count(1)
    if pairs_covered != npairs:
        raise Invalid("pair_coverage", "%d pairs covered, but V has C(v,2) = "
                      "%d pairs" % (pairs_covered, npairs))

    # s(x) = x+1 mod v maps the block collection onto itself.
    for i, blk in enumerate(blocks):
        img = shift(blk, v)
        if img not in block_set:
            raise Invalid("block_invariance", "s maps block %s (line %d, "
                          "class %d) to %s, which is not a block"
                          % (fmt_block(blk), i + 2, class_of[i],
                             fmt_block(img)), line=i + 2)
    if frozenset(shift(blk, v) for blk in blocks) != block_set:
        raise Invalid("block_invariance", "s does not map the block "
                      "collection onto itself")

    # s maps every class onto a listed class (compared as sets of blocks).
    classes = [frozenset(blocks[j * b:(j + 1) * b]) for j in range(c)]
    index_of = {C: j for j, C in enumerate(classes)}
    sigma = []  # sigma[j] = index of the class s(C_j)
    for j, C in enumerate(classes):
        img = frozenset(shift(blk, v) for blk in C)
        t = index_of.get(img)
        if t is None:
            lie_in = sorted(set(class_of[first[blk]] for blk in img))
            raise Invalid("class_invariance", "s maps class %d onto a set of "
                          "blocks that is not a listed class (its image blocks "
                          "lie in classes %s)" % (j, lie_in), class_index=j)
        sigma.append(t)
    if sorted(sigma) != list(range(c)):
        raise Invalid("class_invariance", "s does not permute the classes "
                      "(induced class map %s)" % sigma)

    # Orbits under <s>: cycles of sigma on classes and of s on blocks.
    done = [False] * c
    class_orbits = []
    for j in range(c):
        length, t = 0, j
        while not done[t]:
            done[t] = True
            t = sigma[t]
            length += 1
        if length:
            class_orbits.append(length)
    class_orbits.sort()
    visited = set()
    block_orbits = []
    for blk in blocks:
        length, cur = 0, blk
        while cur not in visited:
            visited.add(cur)
            cur = shift(cur, v)
            length += 1
        if length:
            block_orbits.append(length)
    block_orbits.sort()

    return {
        "v": v,
        "k": K,
        "classes": c,
        "blocks_per_class": b,
        "blocks": n,
        "distinct_blocks": len(block_set),
        "pairs_total": npairs,
        "pairs_covered": pairs_covered,
        "class_orbits": len(class_orbits),
        "class_orbit_lengths": class_orbits,
        "block_orbits": len(block_orbits),
        "block_orbit_lengths": block_orbits,
        "class_map_under_s": sigma,
        "checks_passed": list(CHECKS),
    }


def main(argv):
    try:
        expected_v, path, expected_sha = parse_args(argv)
    except Usage as exc:
        return {"valid": False, "check": "usage", "reason": str(exc),
                "usage": USAGE}, 2
    try:
        with open(path, "rb") as fh:
            data = fh.read()  # the only read of FILE
    except OSError as exc:
        return {"valid": False, "check": "io",
                "reason": "cannot read FILE: %s" % exc, "file": path}, 2
    digest = hashlib.sha256(data).hexdigest()
    info = {"file": path, "bytes": len(data), "sha256": digest}
    if digest != expected_sha:
        result = {"valid": False, "check": "sha256",
                  "reason": "SHA-256 of FILE is %s, expected %s"
                            % (digest, expected_sha),
                  "expected_sha256": expected_sha}
        result.update(info)
        return result, 1
    try:
        report = verify(data, expected_v)
    except Invalid as exc:
        result = {"valid": False, "check": exc.check, "reason": exc.reason}
        result.update(exc.extra)
        result.update(info)
        return result, 1
    result = {"valid": True}
    result.update(info)
    result.update(report)
    return result, 0


def run():
    try:
        result, status = main(sys.argv)
    except Exception as exc:  # internal error: still one JSON object, never 0
        result = {"valid": False, "check": "internal",
                  "reason": "internal error: %s: %s"
                            % (type(exc).__name__, exc)}
        status = 2
    sys.stdout.write(json.dumps(result) + "\n")
    return status


if __name__ == "__main__":
    sys.exit(run())
