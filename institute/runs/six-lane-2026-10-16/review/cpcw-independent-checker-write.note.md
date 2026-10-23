```python
#!/usr/bin/env python3
"""Independent verifier for finite optimal CPCW codes (Python 3 standard library only).

Usage: checker.py EXPECTED_V EXPECTED_K FILE EXPECTED_SHA256

VALID iff the file's SHA-256 equals EXPECTED_SHA256, the file obeys the strict
format with header parameters equal to EXPECTED_V / EXPECTED_K, and its
s = floor((v-1)/(k(k-1))) rows C_1..C_s are k-subsets of Z_v with
    auto-correlation  |C_i & (C_i+t)| <= 1  for all i and 1 <= t <= v-1,
    cross-correlation |C_i & (C_j+t)| <= 1  for all i < j and 0 <= t <= v-1.
Format: ASCII text, LF line endings, final LF; line 1 is "CPCW v k"; then
exactly s rows of k strictly increasing canonical decimal labels in [0, v)
separated by single spaces; nothing else.

Prints exactly one JSON object; exit status 0 iff VALID, else 1.  No assert
statements are used, so running under `python -O` skips no check.
"""
import hashlib
import json
import os
import stat
import sys

DIGITS = frozenset("0123456789")
HEXDIGITS = frozenset("0123456789abcdefABCDEF")
ROW_CHARS = DIGITS | {" "}
FIELDS = (
    "status", "reason", "file", "expected_v", "expected_k", "expected_sha256",
    "sha256", "v", "k", "s", "difference_count", "leave", "leave_size",
    "half_v_uncovered", "largest_auto_correlation", "largest_cross_correlation",
    "developed_block_count", "distinct_developed_block_count", "total_pair_count",
    "covered_pair_count", "uncovered_pair_count", "missing_pairs_match_leave",
    "checks_passed",
)


class Invalid(Exception):
    """An invariant failed; the message is the reported reason."""


def shown(tok):
    return tok if len(tok) <= 24 else tok[:24] + "..."


def canonical_int(tok, what, lo, hi=None):
    """Parse an unsigned ASCII decimal without leading zeros, lo <= n (<= hi)."""
    if tok == "" or any(c not in DIGITS for c in tok):
        raise Invalid(f"{what}: {shown(tok)!r} is not an unsigned ASCII decimal integer")
    if len(tok) > 1 and tok[0] == "0":
        raise Invalid(f"{what}: {shown(tok)!r} has a leading zero (non-canonical)")
    if hi is None:
        if len(tok) > 1000:
            raise Invalid(f"{what}: {len(tok)}-digit integer is too large")
    elif len(tok) > len(str(hi)) or int(tok) > hi:
        raise Invalid(f"{what}: {shown(tok)} is out of range {lo}..{hi}")
    n = int(tok)
    if n < lo:
        raise Invalid(f"{what}: must be >= {lo}, got {n}")
    return n


def read_once(path):
    """Return all bytes of a regular file using a single read()."""
    try:
        if not stat.S_ISREG(os.stat(path).st_mode):
            raise Invalid(f"input: {path!r} is not a regular file")
        with open(path, "rb") as fh:
            if not stat.S_ISREG(os.fstat(fh.fileno()).st_mode):
                raise Invalid(f"input: {path!r} is not a regular file")
            return fh.read()
    except (OSError, ValueError) as e:
        raise Invalid(f"input: cannot read {path!r}: {getattr(e, 'strerror', None) or e}") from None


def check_shape(line, n):
    if line == "":
        raise Invalid(f"format: line {n} is blank (blank lines are not allowed)")
    if line[0].isspace():
        raise Invalid(f"format: line {n} has leading whitespace")
    if line[-1].isspace():
        raise Invalid(f"format: line {n} has trailing whitespace")
    if "\t" in line:
        raise Invalid(f"format: line {n} contains a TAB; fields are separated by one ASCII space")
    if "  " in line:
        raise Invalid(f"format: line {n} has consecutive spaces; fields are separated by one ASCII space")


def parse(data, ev, ek, out):
    """Strictly parse the header and exactly s codeword rows; return (v, k, s, code)."""
    if not data:
        raise Invalid("format: file is empty")
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError as e:
        raise Invalid(f"format: non-ASCII byte 0x{data[e.start]:02x} at offset {e.start}") from None
    cr = text.find("\r")
    if cr >= 0:
        raise Invalid(f"format: CR byte at offset {cr}; CRLF/CR line endings are not allowed")
    if not text.endswith("\n"):
        raise Invalid("format: file does not end with LF")
    lines = text[:-1].split("\n")

    check_shape(lines[0], 1)
    toks = lines[0].split(" ")
    if toks[0] != "CPCW":
        raise Invalid(f"format: line 1 must be the header 'CPCW v k', found {shown(lines[0])!r}")
    if len(toks) != 3:
        raise Invalid(f"format: header must be exactly 'CPCW v k' (3 fields), found {len(toks)} fields")
    v = canonical_int(toks[1], "format: header v", 1)
    k = canonical_int(toks[2], "format: header k", 1)
    out["v"], out["k"] = v, k
    if v != ev:
        raise Invalid(f"parameters: header v={v} does not match EXPECTED_V={ev}")
    if k != ek:
        raise Invalid(f"parameters: header k={k} does not match EXPECTED_K={ek}")
    s = (v - 1) // (k * (k - 1))
    out["s"] = s
    out["checks_passed"].append("header_matches_expected_v_k")

    code = []
    for n, line in enumerate(lines[1:], 2):
        check_shape(line, n)
        if line.startswith("CPCW"):
            raise Invalid(f"format: line {n} repeats the header; only line 1 may be 'CPCW v k'")
        for col, c in enumerate(line, 1):
            if c not in ROW_CHARS:
                kind = "comment marker '#'" if c == "#" else f"unrecognised character {c!r}"
                raise Invalid(f"format: line {n} column {col}: {kind}; rows contain only decimal labels and single spaces")
        toks = line.split(" ")
        if len(toks) != k:
            raise Invalid(f"format: line {n} has {len(toks)} labels, expected exactly k={k}")
        pts = []
        for j, tok in enumerate(toks, 1):
            p = canonical_int(tok, f"format: line {n} label {j}", 0, v - 1)
            if pts and p <= pts[-1]:
                rel = "repeats" if p == pts[-1] else "is smaller than"
                raise Invalid(f"format: line {n} label {j}: point {p} {rel} the previous point {pts[-1]}; "
                              f"labels must be strictly increasing")
            pts.append(p)
        code.append(tuple(pts))
    if len(code) != s:
        raise Invalid(f"optimality: found {len(code)} codeword rows, expected exactly "
                      f"s = floor(({v}-1)/({k}*{k - 1})) = {s}")
    out["checks_passed"] += ["strict_format", "row_count_equals_bound_s"]
    return v, k, s, code


def verify(v, k, s, code, out):
    passed = out["checks_passed"]

    # 1. Difference criterion: every ordered difference x-y (x != y in one
    #    codeword) is nonzero and occurs at most once over the whole code.
    owner = {}
    for i, cw in enumerate(code, 1):
        for x in cw:
            for y in cw:
                if x == y:
                    continue
                d = (x - y) % v
                if d == 0:
                    raise Invalid(f"difference: codeword {i} has distinct points {x},{y} with x-y = 0 mod {v}")
                if 2 * d == v:
                    raise Invalid(f"auto-correlation: codeword {i} contains {min(x, y)} and {max(x, y)} at distance "
                                  f"v/2={d}, so x-y = y-x and |C{i} & (C{i}+{d})| >= 2; v/2 must stay uncovered")
                if d in owner:
                    j, x2, y2 = owner[d]
                    if j == i:
                        raise Invalid(f"auto-correlation: difference {d} occurs twice in codeword {i} "
                                      f"({x2}-{y2} and {x}-{y}), so |C{i} & (C{i}+{d})| >= 2")
                    raise Invalid(f"cross-correlation: difference {d} occurs in codeword {j} ({x2}-{y2}) and "
                                  f"codeword {i} ({x}-{y}), so |C{j} & (C{i}+{(x2 - x) % v})| >= 2")
                owner[d] = (i, x, y)
    nd = len(owner)
    if nd != s * k * (k - 1):
        raise Invalid(f"difference: {nd} distinct differences, expected s*k*(k-1) = {s * k * (k - 1)}")
    leave = [d for d in range(1, v) if d not in owner]
    lset = set(leave)
    out.update(difference_count=nd, leave=leave, leave_size=len(leave))
    for d in leave:
        if v - d not in lset:
            raise Invalid(f"leave: residue {d} is uncovered but its negative {v - d} is covered")
    if v % 2 == 0:
        if v // 2 not in lset:
            raise Invalid(f"leave: v is even and v/2 = {v // 2} is covered")
        out["half_v_uncovered"] = True
    passed.append("differences_nonzero_and_distinct")

    # 2. The definition itself: |C_i & (C_j+t)| > 0 forces t = x - y with
    #    x in C_i, y in C_j, so all remaining shifts contribute 0.
    sets = [frozenset(cw) for cw in code]
    best = {"auto": None, "cross": None}
    for i in range(s):
        for j in range(i, s):
            kind = "auto" if i == j else "cross"
            for t in sorted({(x - y) % v for x in code[i] for y in code[j]}):
                if i == j and t == 0:
                    continue
                m = sum(1 for y in code[j] if (y + t) % v in sets[i])
                if best[kind] is None or m > best[kind]:
                    best[kind] = m
                if m > 1:
                    raise Invalid(f"{kind}-correlation: |C{i + 1} & (C{j + 1}+{t})| = {m} > 1")
    out["largest_auto_correlation"] = best["auto"]
    out["largest_cross_correlation"] = best["cross"]
    passed.append("auto_and_cross_correlation_all_shifts")

    # 3. Developed packing {C_i + t}: for every point a list the s*k blocks
    #    through a (t = a - x for x in C_i).  Equal blocks share a point, as do
    #    the two blocks of a doubly covered pair, so both are caught here.
    incidences = uncovered_dirs = 0
    for a in range(v):
        cover = [-1] * v
        through = {}
        for i, cw in enumerate(code):
            for x in cw:
                t = (a - x) % v
                blk = tuple(sorted((y + t) % v for y in cw))
                bid = i * v + t
                if blk in through:
                    i2, t2 = divmod(through[blk], v)
                    raise Invalid(f"developed packing: blocks C{i2 + 1}+{t2} and C{i + 1}+{t} are both {list(blk)}")
                through[blk] = bid
                for b in blk:
                    if b == a:
                        continue
                    if cover[b] >= 0:
                        i2, t2 = divmod(cover[b], v)
                        raise Invalid(f"developed packing: pair {{{min(a, b)},{max(a, b)}}} is covered by both "
                                      f"C{i2 + 1}+{t2} and C{i + 1}+{t}")
                    cover[b] = bid
                    incidences += 1
        missing = [d for d in range(1, v) if cover[(a + d) % v] < 0]
        if missing != leave:
            mset = set(missing)
            d = min(mset ^ lset)
            lo, hi = sorted((a, (a + d) % v))
            if d in mset:
                raise Invalid(f"developed packing: pair {{{lo},{hi}}} is uncovered but its difference {d} "
                              f"is not in the leave {leave}")
            raise Invalid(f"developed packing: pair {{{lo},{hi}}} is covered but its difference {d} "
                          f"is in the leave {leave}")
        uncovered_dirs += len(missing)
    blocks = s * v
    total = v * (v - 1) // 2
    covered, uncovered = incidences // 2, uncovered_dirs // 2
    if incidences != blocks * k * (k - 1) or covered + uncovered != total:
        raise Invalid(f"developed packing: inconsistent pair counts (covered {covered}, uncovered {uncovered}, "
                      f"C(v,2) = {total})")
    out.update(developed_block_count=blocks, distinct_developed_block_count=blocks,
               total_pair_count=total, covered_pair_count=covered,
               uncovered_pair_count=uncovered, missing_pairs_match_leave=True)
    passed += ["developed_blocks_distinct", "developed_pairs_covered_at_most_once",
               "uncovered_pairs_equal_leave_translates"]


def main(argv):
    out = dict.fromkeys(FIELDS)
    out["status"] = "INVALID"
    out["checks_passed"] = []
    try:
        if len(argv) != 5:
            raise Invalid(f"usage: checker.py EXPECTED_V EXPECTED_K FILE EXPECTED_SHA256 "
                          f"(got {len(argv) - 1} arguments)")
        out["file"] = argv[3]
        ev = out["expected_v"] = canonical_int(argv[1], "CLI EXPECTED_V", 1)
        ek = out["expected_k"] = canonical_int(argv[2], "CLI EXPECTED_K", 1)
        if ek < 2:
            raise Invalid("CLI EXPECTED_K: must be >= 2 (s = floor((v-1)/(k(k-1))) is undefined for k = 1)")
        esha = argv[4]
        if len(esha) != 64 or any(c not in HEXDIGITS for c in esha):
            raise Invalid("CLI EXPECTED_SHA256: must be exactly 64 hexadecimal digits")
        esha = out["expected_sha256"] = esha.lower()
        out["checks_passed"].append("cli_arguments")
        data = read_once(argv[3])
        sha = out["sha256"] = hashlib.sha256(data).hexdigest()
        if sha != esha:
            raise Invalid(f"sha256: file digest {sha} does not match EXPECTED_SHA256 {esha}")
        out["checks_passed"].append("sha256_matches_expected")
        v, k, s, code = parse(data, ev, ek, out)
        verify(v, k, s, code, out)
        out["status"] = "VALID"
    except Invalid as e:
        out["reason"] = str(e)
    except Exception as e:  # never let an unexpected failure look VALID
        out["reason"] = f"internal checker error: {type(e).__name__}: {e}"
    print(json.dumps(out))
    return 0 if out["status"] == "VALID" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```
