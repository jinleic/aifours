"""Independent parent checker for a large set of Kirkman triple systems, LKTS(v).

Definition checked (no symmetry or construction assumed):
- points are the integers 0..v-1;
- the certificate lists exactly v-2 constituent systems;
- each constituent lists exactly (v-1)/2 parallel classes, each a partition of all v points into
  v/3 triples of three distinct points;
- within each constituent every unordered pair of points occurs in exactly one block, i.e. the
  constituent is a Steiner triple system with the given resolution (a KTS);
- the block sets of distinct constituents are pairwise disjoint and together contain every
  3-subset of the point set exactly once.

The parser is strict: a header `LKTS v`, then `KTS i` (i = 0,1,... in order), `CLASS j`
(j = 0,1,... in order within each KTS), then triple lines of three integers. Lines starting with
`#` are comments. Standard library only; no code from the worker or prior dossier is imported.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import hashlib
from itertools import combinations
import json
from math import comb
from pathlib import Path
import time
from zoneinfo import ZoneInfo


class CertificateError(ValueError):
    pass


def parse(data: bytes) -> tuple[int, list[list[list[tuple[int, int, int]]]]]:
    v = None
    systems: list[list[list[tuple[int, int, int]]]] = []
    for line_no, raw in enumerate(data.decode('ascii').splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if parts[0] == 'LKTS':
            if v is not None or len(parts) != 2:
                raise CertificateError(f'line {line_no}: bad or repeated header')
            v = int(parts[1])
            continue
        if v is None:
            raise CertificateError(f'line {line_no}: data before LKTS header')
        if parts[0] == 'KTS':
            if len(parts) != 2 or int(parts[1]) != len(systems):
                raise CertificateError(f'line {line_no}: KTS index out of order')
            systems.append([])
            continue
        if parts[0] == 'CLASS':
            if not systems or len(parts) != 2 or int(parts[1]) != len(systems[-1]):
                raise CertificateError(f'line {line_no}: CLASS index out of order')
            systems[-1].append([])
            continue
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            raise CertificateError(f'line {line_no}: expected three nonnegative integers')
        if not systems or not systems[-1]:
            raise CertificateError(f'line {line_no}: triple outside a class')
        triple = tuple(int(p) for p in parts)
        if any(not 0 <= x < v for x in triple) or len(set(triple)) != 3:
            raise CertificateError(f'line {line_no}: invalid triple {triple}')
        systems[-1][-1].append(tuple(sorted(triple)))
    if v is None:
        raise CertificateError('missing header')
    return v, systems


def verify(path: Path) -> dict:
    started = time.monotonic()
    data = path.read_bytes()
    v, systems = parse(data)
    if v % 6 != 3:
        raise CertificateError('v must be 3 mod 6')
    if len(systems) != v - 2:
        raise CertificateError(f'expected {v-2} constituents, found {len(systems)}')
    points = set(range(v))
    seen_triples: dict[tuple[int, int, int], int] = {}
    pair_total = comb(v, 2)
    for s_index, classes in enumerate(systems):
        if len(classes) != (v - 1) // 2:
            raise CertificateError(f'KTS {s_index}: expected {(v-1)//2} classes, found {len(classes)}')
        pairs = Counter()
        blocks = set()
        for c_index, cls in enumerate(classes):
            if len(cls) != v // 3:
                raise CertificateError(f'KTS {s_index} class {c_index}: wrong number of triples')
            covered = [x for t in cls for x in t]
            if len(covered) != v or set(covered) != points:
                raise CertificateError(f'KTS {s_index} class {c_index}: not a partition of the points')
            for t in cls:
                if t in blocks:
                    raise CertificateError(f'KTS {s_index}: repeated block {t}')
                blocks.add(t)
                for pair in combinations(t, 2):
                    pairs[pair] += 1
        if len(pairs) != pair_total or any(count != 1 for count in pairs.values()):
            raise CertificateError(f'KTS {s_index}: pairs not covered exactly once')
        for t in blocks:
            if t in seen_triples:
                raise CertificateError(f'triple {t} in KTS {seen_triples[t]} and KTS {s_index}')
            seen_triples[t] = s_index
    if len(seen_triples) != comb(v, 3):
        raise CertificateError(f'union has {len(seen_triples)} triples, expected {comb(v, 3)}')
    # Explicit completeness, not merely the cardinality argument above.
    if set(seen_triples) != set(combinations(range(v), 3)):
        raise CertificateError('union is not the full set of triples')
    return {
        'status': 'VALID_LKTS',
        'v': v,
        'input_sha256': hashlib.sha256(data).hexdigest(),
        'constituents': len(systems),
        'classes_per_constituent': (v - 1) // 2,
        'triples_per_class': v // 3,
        'blocks_per_constituent': len(systems[0]) * (v // 3),
        'distinct_triples': len(seen_triples),
        'checked_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
        'duration_seconds': time.monotonic() - started,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'limits': 'Verifies the finite combinatorial certificate only. Novelty, construction method and the general book question are outside this check.',
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument('certificate', type=Path)
    p.add_argument('--output', type=Path)
    args = p.parse_args()
    if args.output and args.output.exists():
        raise SystemExit('Refusing to overwrite evidence output')
    report = verify(args.certificate)
    text = json.dumps(report, indent=2) + '\n'
    if args.output:
        args.output.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
