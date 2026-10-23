```python
#!/usr/bin/env python3
"""Independent verifier for circular Florentine rectangles CFR(r,n) and difference matrices DM(k,n;1) over Z_n.

usage: checker.py cfr|dm EXPECTED_ROWS EXPECTED_N FILE EXPECTED_SHA256

CFR(r,n): r rows, each a permutation of 0..n-1, such that for every ordered pair of distinct symbols (a,b) the
circular distances (pos_i(b) - pos_i(a)) mod n over the rows i are nonzero and pairwise distinct (wraparound
included), i.e. every d in 1..n-1 occurs in at most one row.
DM(k,n;1) over cyclic Z_n: k rows of n entries in 0..n-1 such that for every ordered pair of distinct rows (i,j)
the column differences (D_i[c] - D_j[c]) mod n are exactly 0..n-1, each once. Rows need not be permutations.

dm mode decides validity from the DM definition alone. Only afterwards, as a cross-check, its lambda=1 image
(subtract row 0 columnwise, rows 1.. become position maps, relabel symbols by the first position map, invert
each map) must also pass the CFR routine; a disagreement is an internal failure.

EXPECTED_ROWS and EXPECTED_N are capped to bound the O(r*n^2) and O(k^2*n) work. In reasons, lines and fields
are 1-based; rows, columns, positions and symbols are 0-based. Prints exactly one JSON object.
Exit 0: valid; 1: invalid certificate or arguments; 2: unreadable FILE or internal failure.
"""
import hashlib
import json
import re
import sys

MAX_ROWS = 1024
MAX_N = 1024
MAX_FILE_BYTES = 1 << 24  # far above any well-formed file within the caps (at most 1024 * 1024 * 5 bytes)


def parse_dimension(text, cap):
    """Canonical decimal integer in 1..cap; the length is bounded before any conversion."""
    if len(text) <= len(str(cap)) and re.fullmatch(r"[1-9][0-9]*", text):
        value = int(text)
        if value <= cap:
            return value
    return None


def parse_matrix(data, rows, n):
    """Exactly `rows` LF-terminated lines of `n` single-space-separated canonical integers in 0..n-1."""
    bad = re.search(rb"[^0-9 \n]", data)
    if bad:
        offset = bad.start()
        line_no = data.count(b"\n", 0, offset) + 1
        return "format", (f"unrecognized byte 0x{data[offset]:02x} at offset {offset} (line {line_no}); "
                          "only ASCII digits, single spaces and LF are allowed"), None
    if not data:
        return "format", "FILE is empty", None
    if not data.endswith(b"\n"):
        return "format", "missing final LF", None
    framed = b"\n" + data  # a virtual LF before line 1, so every line start follows an LF
    for pattern, shift, what in ((rb"\n\n", 1, "blank line"),
                                 (rb"\n ", 1, "leading space"),
                                 (rb" \n", 0, "trailing space"),
                                 (rb"  ", 0, "repeated space"),
                                 (rb"(?<![0-9])0[0-9]", 0, "non-canonical integer with a leading zero")):
        found = re.search(pattern, framed)
        if found:
            line_no = framed.count(b"\n", 0, found.start() + shift)
            return "format", f"{what} on line {line_no}", None
    lines_found = data.count(b"\n")
    if lines_found != rows:
        return "row_count", f"expected {rows} rows (LF-terminated lines), found {lines_found}", None
    lines = data[:-1].split(b"\n")
    for line_no, line in enumerate(lines, 1):
        width = line.count(b" ") + 1
        if width != n:
            return "row_width", f"line {line_no} has {width} integers, expected {n}", None
    digits = len(str(n - 1))
    matrix = []
    for line_no, line in enumerate(lines, 1):
        row = []
        for field, token in enumerate(line.split(b" "), 1):
            value = int(token) if len(token) <= digits else n  # a longer canonical token already exceeds n-1
            if value >= n:
                shown = token[:24].decode() + ("..." if len(token) > 24 else "")
                return "range", f"line {line_no} field {field}: {shown} is outside 0..{n - 1}", None
            row.append(value)
        matrix.append(row)
    return None, None, matrix


def check_cfr(matrix, n, counts, prefix=""):
    """Every row a permutation; for EVERY ordered pair a != b the circular distances across rows are nonzero
    and pairwise distinct."""
    r = len(matrix)
    perms_key = prefix + "row_permutations_checked"
    pairs_key = prefix + "ordered_symbol_pairs_checked"
    dists_key = prefix + "circular_distances_checked"
    counts[perms_key] = 0
    counts[prefix + "ordered_symbol_pairs_total"] = n * (n - 1)
    counts[pairs_key] = 0
    counts[dists_key] = 0
    symbols = list(range(n))
    positions = []
    for i, row in enumerate(matrix):
        if sorted(row) != symbols:
            first = {}
            for c, s in enumerate(row):
                if s in first:
                    return "row_permutation", f"row {i}: symbol {s} at positions {first[s]} and {c} (0-based)"
                first[s] = c
            return "row_permutation", f"row {i} is not a permutation of 0..{n - 1}"
        pos = [0] * n
        for c, s in enumerate(row):
            pos[s] = c
        positions.append(pos)
        counts[perms_key] += 1
    by_symbol = [[pos[s] for pos in positions] for s in symbols]  # by_symbol[s][i] = pos_i(s)
    for a in symbols:
        for b in symbols:
            if a == b:
                continue
            dist = [(pb - pa) % n for pa, pb in zip(by_symbol[a], by_symbol[b])]
            counts[dists_key] += r
            if 0 in dist:
                return "cfr_distance_zero", f"ordered pair (a={a}, b={b}): row {dist.index(0)} has distance 0"
            if len(set(dist)) != r:
                first = {}
                for i, d in enumerate(dist):
                    if d in first:
                        return "cfr_distance_collision", (f"ordered pair (a={a}, b={b}): rows {first[d]} and {i} "
                                                          f"both have (pos(b)-pos(a)) mod {n} = {d} (0-based)")
                    first[d] = i
            counts[pairs_key] += 1
    return None, None


def check_dm(matrix, n, counts):
    """For EVERY ordered pair of distinct rows the column differences mod n are exactly 0..n-1, each once."""
    k = len(matrix)
    counts["ordered_row_pairs_total"] = k * (k - 1)
    counts["ordered_row_pairs_checked"] = 0
    counts["column_differences_checked"] = 0
    residues = list(range(n))
    for i in range(k):
        for j in range(k):
            if i == j:
                continue
            diff = [(x - y) % n for x, y in zip(matrix[i], matrix[j])]
            counts["column_differences_checked"] += n
            if sorted(diff) != residues:
                first = {}
                for c, v in enumerate(diff):
                    if v in first:
                        missing = min(set(residues).difference(diff))
                        return "dm_difference", (f"rows {i},{j}: (D_{i}[c] - D_{j}[c]) mod {n} = {v} at columns "
                                                 f"{first[v]} and {c}, so {missing} never occurs (0-based)")
                    first[v] = c
                return "dm_difference", f"rows {i},{j}: column differences are not exactly 0..{n - 1}"
            counts["ordered_row_pairs_checked"] += 1
    return None, None


def verify(argv, out):
    """Return (exit_code, invariant, reason), recording established facts in `out` along the way."""
    counts = out["counts"]
    if len(argv) != 6:
        return 1, "arg_count", (f"usage: checker.py cfr|dm EXPECTED_ROWS EXPECTED_N FILE EXPECTED_SHA256 "
                                f"(got {len(argv) - 1} arguments)")
    kind, rows_text, n_text, path, expected_sha = argv[1:]
    if kind not in ("cfr", "dm"):
        return 1, "arg_kind", f"kind must be cfr or dm, got {kind[:32]!r}"
    out["kind"] = kind
    rows = parse_dimension(rows_text, MAX_ROWS)
    if rows is None:
        return 1, "arg_rows", f"EXPECTED_ROWS must be a canonical decimal in 1..{MAX_ROWS}, got {rows_text[:32]!r}"
    out["expected_rows"] = rows
    n = parse_dimension(n_text, MAX_N)
    if n is None:
        return 1, "arg_n", f"EXPECTED_N must be a canonical decimal in 1..{MAX_N}, got {n_text[:32]!r}"
    out["expected_n"] = n
    if not re.fullmatch(r"[0-9a-f]{64}", expected_sha):
        return 1, "arg_sha256", f"EXPECTED_SHA256 must be 64 lowercase hex digits, got {expected_sha[:72]!r}"
    try:
        with open(path, "rb") as handle:
            data = handle.read(MAX_FILE_BYTES + 1)
    except (OSError, ValueError) as exc:
        return 2, "file_unreadable", f"cannot read FILE: {type(exc).__name__}: {str(exc)[:300]}"
    counts["bytes_read"] = len(data)
    if len(data) > MAX_FILE_BYTES:
        return 1, "file_size", f"FILE exceeds {MAX_FILE_BYTES} bytes, more than any well-formed certificate; not hashed"
    digest = hashlib.sha256(data).hexdigest()
    out["sha256"] = digest
    if digest != expected_sha:
        return 1, "sha256", f"expected {expected_sha}, FILE has {digest}"
    invariant, reason, matrix = parse_matrix(data, rows, n)
    if invariant:
        return 1, invariant, reason
    counts["rows_parsed"] = rows
    counts["entries_parsed"] = rows * n
    if kind == "cfr":
        invariant, reason = check_cfr(matrix, n, counts)
        if invariant:
            return 1, invariant, reason
        return 0, None, (f"CFR({rows},{n}): all {rows} rows are permutations of 0..{n - 1} and all {n * (n - 1)} "
                         "ordered symbol pairs have nonzero, pairwise distinct circular distances")
    invariant, reason = check_dm(matrix, n, counts)
    if invariant:
        return 1, invariant, reason
    # lambda=1 equivalence, used only to cross-check the verdict just reached from the raw DM definition:
    # subtract row 0 columnwise; rows 1.. are position maps (column c = symbol, entry = its position);
    # relabel symbols so the first position map becomes the identity; invert each map into a CFR row.
    maps = [[(x - y) % n for x, y in zip(row, matrix[0])] for row in matrix[1:]]
    if maps:
        symbol_of_label = [0] * n
        for c, p in enumerate(maps[0]):
            symbol_of_label[p] = c
        maps = [[m[symbol_of_label[s]] for s in range(n)] for m in maps]
    image = []
    for m in maps:
        row = [0] * n
        for s, p in enumerate(m):
            row[p] = s
        image.append(row)
    counts["derived_cfr_rows"] = len(image)
    invariant, reason = check_cfr(image, n, counts, "derived_cfr_")
    if invariant:
        return 2, "equivalence_cross_check", f"raw DM is valid but its lambda=1 CFR image fails {invariant}: {reason}"
    return 0, None, (f"DM({rows},{n};1) over Z_{n}: all {rows * (rows - 1)} ordered row pairs have column "
                     f"differences exactly 0..{n - 1}; lambda=1 image re-verified as CFR({rows - 1},{n})")


def main():
    out = {"valid": False, "kind": None, "expected_rows": None, "expected_n": None,
           "sha256": None, "invariant": None, "reason": None, "counts": {}}
    try:
        code, invariant, reason = verify(sys.argv, out)
    except Exception as exc:  # anything unexpected means no verdict could be reached
        code, invariant, reason = 2, "internal_error", f"{type(exc).__name__}: {str(exc)[:300]}"
    out["valid"] = code == 0
    out["invariant"] = invariant
    out["reason"] = reason
    print(json.dumps(out))
    return code


if __name__ == "__main__":
    sys.exit(main())
```
