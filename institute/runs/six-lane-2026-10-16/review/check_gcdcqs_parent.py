#!/usr/bin/env python3
"""Parent definition-first checker for a gcDCQS(g^n : 0) certificate.

Standard library only; imports no worker code; assumes no symmetry. Written by the parent from the source
definitions in Tan-Zhou, arXiv:2503.11934v1 (pinned text:
mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt):
  (1.1), l.110-125   chi'(w) = (w-1)/2 if w = 3 (mod 6); (w+1)/2 if w = 1 (mod 6), w not in {7, 13};
                     chi'(7) = 7, chi'(13) = 8.
  l.211-215          gcSTS(w, h): the blocks of an incomplete STS(w, h) (X, H, B) are partitioned into
                     r := chi'(w) partial parallel classes (PPCs) of X, among which s := chi'(w) - (w-h)/2
                     are PPCs of X minus H.
  l.256-266          candelabra system CS(3, {4}, v), stem S, groups G: every 3-subset not inside S u G for a
                     group G lies in exactly one block; no 3-subset of S u G lies in any block. Here S is empty.
  l.281-288          gcDCQS(g^n : s): for every x in a group G, (X - {x}, (G u S) - {x}, A_x) is a
                     gcSTS(gn + s - 1, g + s - 1), where A_x = {A - {x} : x in A}.
The colouring at x must therefore partition A_x into exactly r nonempty pairwise-disjoint triple classes,
exactly s of which contain no point of the hole H_x = G(x) - {x} (at most s is forced by counting; the
checker requires exactly s).

Certificate format (strict; '#' lines and blank lines ignored; single spaces; decimal integers):
  GCDCQS v n g / COLOURS r / HOLEFREE s / GROUPS + n lines of g points / BLOCKS + one 4-set per line /
  for every point: POINT x, then CLASS 0 .. CLASS r-1 in order, each followed by its triples (3 points).
Usage: check_gcdcqs_parent.py FILE V N G EXPECTED_SHA256 OUTPUT_JSON
Exit 0 with receipt status PASS, else exit 1 with status FAIL and reason '<CATEGORY>: detail'.
The receipt is created exclusively (never overwritten).
"""
import hashlib
import json
import re
import sys
from collections import Counter
from itertools import combinations
from math import comb

INT = re.compile(r'0|[1-9][0-9]*')


class CertificateError(Exception):
    pass


def chi_prime(w):
    if w % 6 == 3:
        return (w - 1) // 2
    if w % 6 == 1:
        return {7: 7, 13: 8}.get(w, (w + 1) // 2)
    raise CertificateError(f'PARAMS: derived order {w} is not 1 or 3 mod 6')


def numbers(tokens, count, lineno):
    if len(tokens) != count or not all(INT.fullmatch(t) for t in tokens):
        raise CertificateError(f'FORMAT: line {lineno} must hold exactly {count} decimal integers')
    return [int(t) for t in tokens]


def parse(text):
    lines = []
    for lineno, raw in enumerate(text.split('\n'), 1):
        if raw == '' or raw.startswith('#'):
            continue
        tokens = raw.split(' ')
        if '' in tokens:
            raise CertificateError(f'FORMAT: line {lineno} has leading, trailing or repeated spaces')
        lines.append((lineno, tokens))
    pos = 0

    def take(keyword, nargs):
        nonlocal pos
        if pos >= len(lines) or lines[pos][1][0] != keyword:
            got = lines[pos][1][0] if pos < len(lines) else 'EOF'
            raise CertificateError(f'FORMAT: expected {keyword}, found {got}')
        lineno, tokens = lines[pos]
        pos += 1
        return numbers(tokens[1:], nargs, lineno)

    v, n, g = take('GCDCQS', 3)
    (r,) = take('COLOURS', 1)
    (s,) = take('HOLEFREE', 1)
    take('GROUPS', 0)
    groups = []
    for _ in range(n):
        if pos >= len(lines):
            raise CertificateError('FORMAT: missing group line')
        lineno, tokens = lines[pos]
        groups.append(numbers(tokens, g, lineno))
        pos += 1
    take('BLOCKS', 0)
    blocks = []
    while pos < len(lines) and lines[pos][1][0] != 'POINT':
        lineno, tokens = lines[pos]
        blocks.append(numbers(tokens, 4, lineno))
        pos += 1
    sections = []
    while pos < len(lines):
        (x,) = take('POINT', 1)
        classes = []
        for j in range(r):
            (jj,) = take('CLASS', 1)
            if jj != j:
                raise CertificateError(f'FORMAT: point {x} lists CLASS {jj} where CLASS {j} is required')
            triples = []
            while pos < len(lines) and lines[pos][1][0] not in ('CLASS', 'POINT'):
                lineno, tokens = lines[pos]
                triples.append(numbers(tokens, 3, lineno))
                pos += 1
            classes.append(triples)
        if pos < len(lines) and lines[pos][1][0] == 'CLASS':
            raise CertificateError(f'FORMAT: point {x} has more than {r} classes')
        sections.append((x, classes))
    return v, n, g, r, s, groups, blocks, sections


def check(data, expect_v, expect_n, expect_g):
    try:
        text = data.decode('ascii')
    except UnicodeDecodeError:
        raise CertificateError('FORMAT: non-ASCII bytes')
    if '\r' in text or '\t' in text:
        raise CertificateError('FORMAT: carriage return or tab present')
    v, n, g, r, s, groups, blocks, sections = parse(text)
    if (v, n, g) != (expect_v, expect_n, expect_g) or v != n * g:
        raise CertificateError(f'PARAMS: header {(v, n, g)} differs from expected {(expect_v, expect_n, expect_g)} or v != n*g')
    if n < 3:
        raise CertificateError('PARAMS: a candelabra system needs at least three groups here')
    w, h = v - 1, g - 1
    if r != chi_prime(w):
        raise CertificateError(f'PARAMS: COLOURS {r} differs from chi\'({w}) = {chi_prime(w)}')
    if (w - h) % 2 or s != r - (w - h) // 2:
        raise CertificateError(f'PARAMS: HOLEFREE {s} differs from r - (w-h)/2 = {r - (w - h) // 2}')
    group_of = {}
    for i, grp in enumerate(groups):
        if len(set(grp)) != g:
            raise CertificateError(f'GROUPS: group {i} repeats a point')
        for p in grp:
            if not 0 <= p < v:
                raise CertificateError(f'GROUPS: point {p} out of range')
            if p in group_of:
                raise CertificateError(f'GROUPS: point {p} lies in two groups')
            group_of[p] = i
    if set(group_of) != set(range(v)):
        raise CertificateError('GROUPS: groups do not cover every point')
    block_set = set()
    pattern = Counter()
    for b in blocks:
        fb = frozenset(b)
        if len(fb) != 4:
            raise CertificateError(f'BLOCK: {b} repeats a point')
        if not all(0 <= p < v for p in b):
            raise CertificateError(f'BLOCK: {b} has a point out of range')
        mult = sorted(Counter(group_of[p] for p in b).values(), reverse=True)
        if mult[0] >= 3:
            raise CertificateError(f'BLOCK: {b} has three points in one group')
        if fb in block_set:
            raise CertificateError(f'BLOCK: {sorted(b)} repeated')
        block_set.add(fb)
        pattern['+'.join(map(str, mult))] += 1
    expected_blocks = (comb(v, 3) - n * comb(g, 3)) // 4
    if len(block_set) != expected_blocks:
        raise CertificateError(f'BLOCK: {len(block_set)} blocks, expected {expected_blocks}')
    covered = Counter()
    for fb in block_set:
        for t in combinations(sorted(fb), 3):
            covered[t] += 1
    twice = [t for t, c in covered.items() if c > 1]
    if twice:
        raise CertificateError(f'COVERAGE: triple {twice[0]} lies in {covered[twice[0]]} blocks')
    universe = {t for t in combinations(range(v), 3) if len({group_of[p] for p in t}) > 1}
    if set(covered) != universe:
        missing = sorted(universe - set(covered))
        extra = sorted(set(covered) - universe)
        raise CertificateError(f'COVERAGE: uncovered {missing[:1]} or group triple {extra[:1]}')
    seen_points = [x for x, _ in sections]
    if sorted(seen_points) != list(range(v)):
        dup = [x for x, c in Counter(seen_points).items() if c > 1]
        raise CertificateError(f'COMPLETENESS: POINT sections {"repeat " + str(dup[:1]) if dup else "do not match 0..v-1"}')
    derived_of = {x: set() for x in range(v)}
    for fb in block_set:
        for x in fb:
            derived_of[x].add(frozenset(fb - {x}))
    profiles = Counter()
    for x, classes in sections:
        hole = {p for p in groups[group_of[x]] if p != x}
        listed = set()
        holefree = 0
        sizes = []
        for j, triples in enumerate(classes):
            if not triples:
                raise CertificateError(f'COLOURING: point {x} class {j} is empty')
            used = set()
            for t in triples:
                ft = frozenset(t)
                if len(ft) != 3 or not all(0 <= p < v for p in t) or x in ft:
                    raise CertificateError(f'COLOURING: point {x} class {j} has invalid triple {t}')
                if used & ft:
                    raise CertificateError(f'COLOURING: point {x} class {j} is not a partial parallel class')
                used |= ft
                if ft in listed:
                    raise CertificateError(f'COLOURING: point {x} lists triple {sorted(t)} twice')
                if ft not in derived_of[x]:
                    raise CertificateError(f'COLOURING: point {x} triple {sorted(t)} plus {x} is not a block')
                listed.add(ft)
            if not used & hole:
                holefree += 1
            sizes.append(len(triples))
        if listed != derived_of[x]:
            raise CertificateError(f'COLOURING: point {x} misses {len(derived_of[x] - listed)} derived triples')
        if holefree != s:
            raise CertificateError(f'COLOURING: point {x} has {holefree} hole-free classes, expected {s}')
        pair_count = Counter()
        for ft in listed:
            for pr in combinations(sorted(ft), 2):
                pair_count[pr] += 1
        others = [p for p in range(v) if p != x]
        for pr in combinations(others, 2):
            want = 0 if (pr[0] in hole and pr[1] in hole) else 1
            if pair_count.get(pr, 0) != want:
                raise CertificateError(f'DERIVED: point {x} pair {pr} covered {pair_count.get(pr, 0)} times, expected {want}')
        profiles[' '.join(f'{k}^{c}' for k, c in sorted(Counter(sizes).items(), reverse=True))] += 1
    return {'v': v, 'n': n, 'g': g, 'r': r, 's': s, 'blocks': len(block_set), 'block_group_patterns': dict(pattern),
            'non_group_triples': len(universe), 'derived_triples_per_point': sorted({len(d) for d in derived_of.values()}),
            'class_size_profiles': dict(profiles)}


def main():
    if len(sys.argv) != 7:
        raise SystemExit('usage: check_gcdcqs_parent.py FILE V N G EXPECTED_SHA256 OUTPUT_JSON')
    path, ev, en, eg, expect_sha, out = sys.argv[1:]
    with open(path, 'rb') as f:
        data = f.read()
    digest = hashlib.sha256(data).hexdigest()
    with open(__file__, 'rb') as f:
        self_sha = hashlib.sha256(f.read()).hexdigest()
    receipt = {'file': path, 'sha256': digest, 'expected_sha256': expect_sha, 'checker_sha256': self_sha,
               'expected': {'v': int(ev), 'n': int(en), 'g': int(eg)}}
    try:
        if digest != expect_sha:
            raise CertificateError('INPUT: SHA-256 mismatch')
        receipt['structure'] = check(data, int(ev), int(en), int(eg))
        receipt['status'] = 'PASS'
    except CertificateError as exc:
        receipt['status'] = 'FAIL'
        receipt['reason'] = str(exc)
    with open(out, 'x') as f:
        json.dump(receipt, f, indent=2)
        f.write('\n')
    print(json.dumps({k: receipt[k] for k in ('status', 'sha256') if k in receipt} | ({'reason': receipt['reason']} if 'reason' in receipt else {})))
    return 0 if receipt['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
