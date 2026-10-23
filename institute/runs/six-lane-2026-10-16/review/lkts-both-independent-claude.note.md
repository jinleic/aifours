RESULT: VERIFIER-PROVIDED-NOT-EXECUTED

```python
#!/usr/bin/env python3
"""Independent checker for a large set of Kirkman triple systems, LKTS(v).

usage: python3 checker.py EXPECTED_V CERTIFICATE_FILE EXPECTED_SHA256

Prints a JSON summary and exits 0 only if every check passes.  Otherwise exits 1
with 'INVALID [tag] reason' on stderr for the first violated invariant, or 2 on a
usage/I-O error.  Standard library only; no asserts, file writes, network or
subprocesses.  Any other exception is a checker bug and propagates (nonzero exit).
"""
import hashlib
import itertools
import json
import sys

KEYWORDS = ('LKTS', 'KTS', 'CLASS')


class CertificateError(ValueError):
    """A violated format or mathematical invariant of the certificate."""


def fail(tag, msg):
    raise CertificateError('[%s] %s' % (tag, msg))


def usage(msg):
    sys.stderr.write('usage: python3 checker.py EXPECTED_V CERTIFICATE_FILE EXPECTED_SHA256\n' + msg + '\n')
    raise SystemExit(2)


def is_nat(tok):
    # canonical non-negative decimal: ASCII digits only; no sign, space, '_' or leading zero
    return tok == '0' or (tok != '' and tok[0] != '0' and set(tok) <= set('0123456789'))


def parse(v, data):
    """Return (systems, counts); systems[i][j] lists (line, a, b, c) for CLASS j of KTS i."""
    for off, byte in enumerate(data):
        if byte != 9 and byte != 10 and not 32 <= byte <= 126:
            fail('bytes', 'byte 0x%02x at offset %d is not printable ASCII, TAB or LF' % (byte, off))
    lines = data.decode('ascii').split('\n')
    if lines[-1] == '':
        lines.pop()  # the LF ending the last line does not begin another line
    body = []  # (line number, tokens) of every line that does not start with '#'
    for ln, line in enumerate(lines, 1):
        if not line.startswith('#'):
            toks = line.split()  # after the byte filter only SPACE and TAB can separate tokens
            if not toks:
                fail('blank', 'line %d is empty or whitespace-only; blank lines are rejected' % ln)
            body.append((ln, toks))
    counts = {'total': len(lines), 'comment': len(lines) - len(body), 'blank': 0,
              'header': 0, 'kts': 0, 'class': 0, 'triple': 0}
    pos = 0

    def take(kind, want):
        nonlocal pos
        if pos == len(body):
            fail('structure', 'unexpected end of file; expected %s' % want)
        pos += 1
        counts[kind] += 1
        return body[pos - 1]

    def heading(kind, word, idx, want):
        ln, toks = take(kind, want)
        if toks != [word, str(idx)]:
            fail('header' if kind == 'header' else 'structure',
                 "line %d: expected %s, found '%s'" % (ln, want, ' '.join(toks)))

    heading('header', 'LKTS', v, "header 'LKTS %d'" % v)
    label = {str(p): p for p in range(v)}  # the only accepted spellings of the points of X
    systems = []
    for i in range(v - 2):
        heading('kts', 'KTS', i, "'KTS %d'" % i)
        classes = []
        for j in range((v - 1) // 2):
            heading('class', 'CLASS', j, "'CLASS %d' of KTS %d" % (j, i))
            triples = []
            for k in range(v // 3):
                want = 'triple %d of %d in KTS %d CLASS %d' % (k + 1, v // 3, i, j)
                ln, toks = take('triple', want)
                if len(toks) != 3 or toks[0] in KEYWORDS:
                    fail('structure', "line %d: expected %s, found '%s'" % (ln, want, ' '.join(toks)))
                for t in toks:
                    if t not in label:
                        why = 'outside X = {0..%d}' % (v - 1) if is_nat(t) else 'not a canonical decimal'
                        fail('label', "line %d: label '%s' is %s" % (ln, t, why))
                triples.append((ln, label[toks[0]], label[toks[1]], label[toks[2]]))
            classes.append(triples)
        systems.append(classes)
    if pos != len(body):
        ln, toks = body[pos]
        fail('structure', "line %d: unexpected line after the last triple of KTS %d: '%s'"
             % (ln, v - 3, ' '.join(toks)))
    return systems, counts


def verify(v, systems):
    """Check every mathematical condition directly; return {block bitmask: (KTS, CLASS, line)}."""
    full = (1 << v) - 1
    home = {}  # key of block {a,b,c} is 2^a + 2^b + 2^c: order-free and injective on 3-subsets
    for i, classes in enumerate(systems):
        nbr = [0] * v  # bit y of nbr[x] is set iff pair {x,y} is already covered in KTS i
        for j, triples in enumerate(classes):
            used = 0  # bit p is set iff point p is already covered in CLASS j of KTS i
            for ln, a, b, c in triples:
                if a == b or a == c or b == c:
                    fail('triple', 'line %d: %d %d %d are not three distinct points' % (ln, a, b, c))
                blk = (1 << a) | (1 << b) | (1 << c)
                if blk in home:
                    i0, j0, ln0 = home[blk]
                    scope = 'within KTS %d' % i if i0 == i else 'between KTS %d and KTS %d' % (i0, i)
                    fail('repeat', 'line %d: block %s occurs twice, %s (first at line %d, CLASS %d)'
                         % (ln, sorted((a, b, c)), scope, ln0, j0))
                home[blk] = (i, j, ln)
                if used & blk:
                    fail('partition', 'line %d: KTS %d CLASS %d contains point(s) %s twice'
                         % (ln, i, j, [p for p in (a, b, c) if (used >> p) & 1]))
                used |= blk
                for x, y in ((a, b), (a, c), (b, c)):
                    if (nbr[x] >> y) & 1:
                        fail('pair', 'line %d: KTS %d covers pair {%d, %d} twice'
                             % (ln, i, min(x, y), max(x, y)))
                    nbr[x] |= 1 << y
                    nbr[y] |= 1 << x
            if used != full:
                fail('partition', 'KTS %d CLASS %d misses point(s) %s'
                     % (i, j, [p for p in range(v) if ((used >> p) & 1) == 0]))
        for x in range(v):
            if nbr[x] != full ^ (1 << x):
                fail('pair', 'KTS %d never covers the pairs {%d, y} for y in %s'
                     % (i, x, [y for y in range(v) if y != x and ((nbr[x] >> y) & 1) == 0]))
    for a, b, c in itertools.combinations(range(v), 3):
        if ((1 << a) | (1 << b) | (1 << c)) not in home:
            fail('coverage', '3-subset {%d, %d, %d} is a block of no KTS' % (a, b, c))
    return home


def main(argv):
    if len(argv) != 4:
        usage('expected exactly three arguments')
    v_arg, path, want = argv[1], argv[2], argv[3].lower()
    if not (is_nat(v_arg) and len(v_arg) <= 6 and int(v_arg) % 6 == 3):
        usage('EXPECTED_V must be a decimal integer v < 10**6 with v = 3 (mod 6)')
    if len(want) != 64 or not set(want) <= set('0123456789abcdef'):
        usage('EXPECTED_SHA256 must be 64 hexadecimal digits')
    v = int(v_arg)
    try:
        with open(path, 'rb') as fh:
            data = fh.read()  # the only read: exactly these bytes are hashed and then parsed
    except OSError as exc:
        usage('cannot read CERTIFICATE_FILE: %s' % exc)
    sha = hashlib.sha256(data).hexdigest()
    if sha != want:
        fail('sha256', 'file SHA-256 is %s, expected %s' % (sha, want))
    systems, counts = parse(v, data)
    home = verify(v, systems)
    occurrences = sum(len(triples) for classes in systems for triples in classes)
    noncomment = counts['header'] + counts['kts'] + counts['class'] + counts['triple']
    if not (occurrences == len(home) == v * (v - 1) * (v - 2) // 6
            and counts['total'] == counts['comment'] + noncomment):
        raise RuntimeError('checker self-consistency failure')  # unreachable if parse/verify are right
    print(json.dumps({
        'status': 'VALID_LKTS',
        'v': v,
        'sha256': sha,
        'bytes': len(data),
        'system_count': len(systems),
        'class_count_per_system': len(systems[0]),
        'class_count_total': sum(len(classes) for classes in systems),
        'triples_per_class': len(systems[0][0]),
        'blocks_per_system': sum(len(triples) for triples in systems[0]),
        'total_block_occurrences': occurrences,
        'distinct_triples': len(home),
        'line_counts': counts,
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    try:
        main(sys.argv)
    except CertificateError as exc:
        raise SystemExit('INVALID %s' % exc)
```

**Accepted grammar**

*Arguments*
- `EXPECTED_V` must be a canonical decimal with v ≡ 3 (mod 6). The bound v < 10⁶ is only a resource guard.
- `EXPECTED_SHA256` must be 64 hex digits, case-insensitive.

*Bytes and lines*
- Only TAB, LF and 0x20–0x7E are allowed.
- Lines are split on LF, and one terminating LF is optional.
- A line whose first byte is `#` is a comment. Comments may appear anywhere and are never parsed.
- Every other line is split on runs of SPACE/TAB and must be non-empty. Blank lines are rejected, so `blank` is always 0 on a PASS.

*Structure*
- Token lines must appear exactly in this order, with nothing left over:
  - `LKTS v`
  - for i = 0..v−3: `KTS i`
  - inside each system, for j = 0..(v−3)/2: `CLASS j`, then exactly v/3 lines of three labels.
- Keywords are case-sensitive.
- Indices must be canonical decimals. A label must literally equal one of `0`…`v−1`.
- The order of points within a line and of lines within a class is free.

*Exit codes*
- 0: VALID.
- 1: `INVALID [tag] …`, where tag is one of `sha256 bytes blank header structure label triple repeat partition pair coverage`.
- 2: usage or I/O error.
- A traceback means a checker bug; it can never produce VALID.

**Soundness: VALID ⇒ the hashed bytes encode an LKTS(v)**

Let r = (v−1)/2 and b = v/3.

1. **Control flow.** The JSON `print` is the last statement. Every check raises `CertificateError` (a `ValueError`) before reaching it, and only that class is caught. There are no `assert` statements, so `-O` changes nothing.
2. **Identity.** The file is read once in binary mode. The same `bytes` object is hashed and parsed, with no newline translation and no second read.
3. **Shape.**
   - Lines are consumed in a fixed order derived from EXPECTED_V alone, and the header must restate v.
   - Declared indices are compared with loop counters and never used as keys. So a skipped, repeated, reordered or overwriting header, a short or long class, truncation, or trailing data each stops the parse.
   - Hence there are exactly v−2 × r × b triples, and the line identity total = comment + header + kts + class + triple is re-checked.
4. **Blocks.** Each block has three distinct points of X. It is encoded as m = 2^a + 2^b + 2^c, which is injective and order-free on 3-subsets.
5. **Parallel classes.** Each insertion requires `used & m == 0` (each point at most once), and each class must end with `used == 2^v−1` (each point at least once). So every class partitions X.
6. **STS per constituent.**
   - Each system gets a fresh `nbr`. Every pair is tested and then set (at most once), and every `nbr[x]` must end as X∖{x} (at least once).
   - So each system's block set is an STS(v). By 5 and 7, its r classes are block-disjoint and their union is that block set, so it is a KTS(v) with the file's resolution.
   - No group or automorphism condition is assumed.
7. **Disjointness.** `home` rejects any second occurrence of a block anywhere, both within one system and between systems. So the v−2 systems are pairwise block-disjoint.
8. **Coverage.** All C(v,3) 3-subsets are enumerated and each must be in `home`. Occurrences = |home| = (v−2)·v(v−1)/6 = C(v,3) is also re-checked.

The "at least once" halves of 5, 6 and 8 follow from the "at most once" halves plus exact counts. This is a pigeonhole argument: v points, C(v,2) = 3·v(v−1)/6 pairs, C(v,3) = (v−2)·v(v−1)/6 blocks. So those halves can never be the first failure; they are kept as count-independent confirmations. Realistic first-failure tags for mathematical corruptions are therefore `triple`, `repeat`, `partition` and `pair`.

**False-PASS pitfalls closed**

- **Union-only or count-only acceptance:** closed by the per-constituent pair check (control 7).
- **STS without resolution:** closed by the per-class partition check (control 8).
- **Valid constituents sharing blocks:** closed by the global registry (control 2).
- **Lenient integer parsing** (`int('+7')`, `' 7'`, `'0_7'`, `'07'`, non-ASCII digits): closed by the exact-string label table and the byte whitelist. `int()` is never applied to file data.
- **Index-keyed storage** that lets a repeated header overwrite an earlier one, or a missing one go unnoticed: closed by positional parsing.
- **Ignored or indented `#` lines, truncation, trailing data:** every line is classified and consumed, leftover lines are rejected, and the line identity is re-checked.
- **Hash computed over different bytes than those parsed:** closed by the single binary read.
- **`assert` disappearing under `-O`, or a broad `except` disguising a bug as a correct rejection:** neither is present.
- **Order-dependence, or out-of-range/repeated points hidden by encoding:** bitmasks are built only after the range and distinctness checks.
- **Header-trusted sizes or floating point:** all sizes come from EXPECTED_V, and only integers are used.

**Discriminating corruptions**

For every non-hash control, pass the corrupted file's own recomputed SHA-256. Otherwise `sha256` rejects everything and nothing is tested. Also require the stated tag, not just a nonzero exit.

1. **Point swap in one class, partition kept** ({a,b,c},{d,e,f} → {a,b,d},{c,e,f}): expect `pair` or `repeat`. In a valid original, {a,d} is already covered elsewhere in that KTS, and {a,b,d} belongs to another constituent.
2. **Duplicate constituent:**
   - Overwrite the body of `KTS 1` with `KTS 0`: expect `repeat` "between KTS 0 and KTS 1".
   - Append the copy as an extra `KTS v−2`: expect `structure`.
3. **Drop class** (`CLASS j` plus its v/3 lines, with or without renumbering, or the final class): expect `structure`.
4. **Out-of-range point:**
   - A label set to `57`/`87`: expect `label` (outside X).
   - `-1` or `07`: expect `label` (not canonical).
5. **Altered header:**
   - `LKTS 63`: expect `header`.
   - EXPECTED_V 63 on the genuine file: expect `header`.
   - EXPECTED_V 58: expect exit 2.
6. **Altered hash:**
   - One hex digit of EXPECTED_SHA256 flipped: expect `sha256`.
   - A comment byte edited while passing the original digest: expect `sha256`.
7. **Swap `CLASS j` of `KTS i` with `CLASS j′` of `KTS i′` (i ≠ i′):** expect `pair` only. Partitions, counts and the global block set are untouched, so a union-only checker would pass this.
8. **Within one KTS, exchange one triple between two classes:** expect `partition` only. All block sets are untouched, so an STS-plus-union checker would pass this.
9. **Within one KTS, overwrite a class body with an earlier class:** expect `repeat` "within KTS i".
10. **Format corruptions:**
    - Blank line: `blank`.
    - CRLF line endings: `bytes`.
    - `5 5 7`: `triple`.
    - An extra or missing triple line, or `CLASS 4` repeated in place of `CLASS 5`: `structure`.

**Positive controls** (each must still PASS with the same structural counts, using the recomputed SHA):
- Permute the points within lines.
- Shuffle lines within a class.
- Permute class bodies within a KTS, or whole KTS bodies, leaving the header lines in place.
- Relabel all points by one fixed permutation of X.
- Add comment lines anywhere.
- Use tabs or multiple spaces as separators.
- Drop the final LF.
- Run under `python3 -O` and expect identical output.

**Expected summaries, if the pinned files are valid in this grammar**

| Field | v = 57 | v = 87 |
|---|---|---|
| systems | 55 | 85 |
| classes per system | 28 | 43 |
| classes total | 1540 | 3655 |
| triples per class | 19 | 29 |
| blocks per system | 532 | 1247 |
| block occurrences = distinct triples | 29260 | 105995 |
| non-comment lines (1 + kts + class + triple) | 30856 | 109736 |

A file using CRLF, blank lines, zero-padded labels or indented comments would be rejected with a precise format tag (`bytes`, `blank`, `label` or `structure`). That is a false FAIL to investigate, never a false PASS.
