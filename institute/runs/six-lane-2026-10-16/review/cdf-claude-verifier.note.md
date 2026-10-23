```python
#!/usr/bin/env python3
"""Independent verifier for a cyclic (v,5,1) difference family.

Usage: python3 checker.py EXPECTED_V FILE EXPECTED_SHA256
Prints exactly one line: "VALID ..." (exit 0) or "INVALID: <reason>" (exit 1).
"""
import hashlib
import re
import sys

K = 5
INT = re.compile(r"0|[1-9][0-9]*")   # canonical decimal: ASCII digits, no sign/leading zero/_
SHA = re.compile(r"[0-9a-f]{64}")    # lowercase hex SHA-256


def fail(msg):
    print("INVALID: " + msg)
    sys.exit(1)


def show(s, n=60):
    """Single-line, printable-ASCII, length-capped rendering of untrusted text."""
    return ascii(s if len(s) <= n else s[:n] + "...")


def main(argv):
    if len(argv) != 4:
        fail("usage: python3 checker.py EXPECTED_V FILE EXPECTED_SHA256")
    v_arg, path, want_sha = argv[1:]
    if not INT.fullmatch(v_arg):
        fail(f"EXPECTED_V {show(v_arg)} is not a canonical decimal integer")
    if not SHA.fullmatch(want_sha):
        fail(f"EXPECTED_SHA256 {show(want_sha)} is not 64 lowercase hex digits")
    v = int(v_arg)

    # FILE is read exactly once; the hash and the parse see the same bytes.
    try:
        with open(path, "rb") as f:
            data = f.read()
    except (OSError, ValueError) as e:
        fail(f"cannot read FILE: {show(str(e), 200)}")
    sha = hashlib.sha256(data).hexdigest()
    if sha != want_sha:
        fail(f"sha256 mismatch: FILE has {sha}, expected {want_sha}")
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError as e:
        fail(f"non-ASCII byte at offset {e.start}")

    header = False
    blocks = []                                   # (line number, elements)
    for lineno, line in enumerate(text.split("\n"), 1):
        if line == "" or line[0] == "#":          # empty line, or comment at column 0
            continue
        toks = line.split(" ")                    # any extra space yields a '' token
        if toks[0] == "CDF":
            if header:
                fail(f"line {lineno}: second header line")
            if len(toks) != 3 or not all(INT.fullmatch(t) for t in toks[1:]):
                fail(f"line {lineno}: malformed header {show(line)}")
            if toks[1] != v_arg:                  # both canonical, so string == int equality
                fail(f"line {lineno}: header v={show(toks[1])} differs from EXPECTED_V={v_arg}")
            if toks[2] != str(K):
                fail(f"line {lineno}: header k={show(toks[2])}, required k={K}")
            if v < 2 or (v - 1) % (K * (K - 1)):
                fail(f"line {lineno}: need v > 1 and v = 1 (mod {K * (K - 1)}), got v={v}")
            header = True
            continue
        if not all(INT.fullmatch(t) for t in toks):
            fail(f"line {lineno}: malformed line {show(line)}")
        if not header:
            fail(f"line {lineno}: block before header")
        if len(toks) != K:
            fail(f"line {lineno}: block has {len(toks)} elements, expected {K}")
        for t in toks:
            if len(t) > len(v_arg) or int(t) >= v:      # length test avoids huge int()
                fail(f"line {lineno}: element {show(t)} outside [0, {v - 1}]")
        B = [int(t) for t in toks]
        for x in B:
            if B.count(x) > 1:
                fail(f"line {lineno}: element {x} repeated inside block")
        blocks.append((lineno, B))
    if not header:
        fail("no header line 'CDF v k'")
    n = (v - 1) // (K * (K - 1))
    if len(blocks) != n:
        fail(f"{len(blocks)} blocks found, expected (v-1)/{K * (K - 1)} = {n}")

    # Check 1: ordered differences within blocks hit each nonzero residue once.
    count = [0] * v
    for _, B in blocks:
        for i in range(K):
            for j in range(K):
                if i != j:
                    count[(B[i] - B[j]) % v] += 1
    if count[0]:
        fail(f"residue 0 occurs {count[0]} times as a difference")
    bad = [r for r in range(1, v) if count[r] != 1]
    if bad:
        fail(f"residue {bad[0]} occurs {count[bad[0]]} times as a difference "
             f"(expected exactly 1); {len(bad)} residues wrong in total")

    # Check 2 (independent): develop the design (all v translates of every
    # block) and require each unordered pair {a, b}, a < b, of Z_v to lie in
    # exactly one developed block; covered[a*v + b] marks that pair.
    covered = bytearray(v * v)
    for lineno, B in blocks:
        for t in range(v):
            D = sorted((x + t) % v for x in B)
            for i in range(K):
                for j in range(i + 1, K):
                    idx = D[i] * v + D[j]
                    if covered[idx]:
                        fail(f"cross-check: pair ({D[i]},{D[j]}) lies in a second developed "
                             f"block (line {lineno} shifted by {t})")
                    covered[idx] = 1
    for a in range(v):
        row = covered[a * v + a + 1:(a + 1) * v]  # pairs (a, b) with b > a
        if 0 in row:
            fail(f"cross-check: pair ({a},{a + 1 + row.index(0)}) lies in no developed block")

    print(f"VALID v={v} k={K} blocks={n} sha256={sha}")
    sys.exit(0)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:                        # fail closed on anything unexpected
        fail(f"internal error {type(e).__name__}: {show(str(e), 200)}")
```
