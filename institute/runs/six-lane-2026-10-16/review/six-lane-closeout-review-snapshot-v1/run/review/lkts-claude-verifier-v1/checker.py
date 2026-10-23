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
