#!/usr/bin/env python3
"""Automorphisms of the explicit small T2(n) squares found earlier in this root.

For each input square (rows of a JSON file) this re-checks the T2 property and
lists every nontrivial symbol permutation h with h(row set) = row set, and every
h with h(reverse(row set)) = row set, by trying all images of row 0. It also
lists the row-orbit blocks {R, hR, ...} contained in the square. These are
exact checks of finitely many explicit squares; completeness of the n=8 list is
NOT claimed here (its enumeration ended in an unverified UNSAT).
Usage: SCRIPT OUTPUT.json
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INPUTS = [('frontier-20261028-channel-n4-run-01.json', None), ('frontier-20261028-channel-n6-run-01.json', None),
          ('frontier-20261028-channel-n8-enumeration.json', 'solutions')]


def cycle_type(h):
    seen, out = set(), []
    for x in range(len(h)):
        if x not in seen:
            size, y = 0, x
            while y not in seen:
                seen.add(y); y = h[y]; size += 1
            out.append(size)
    return sorted(out, reverse=True)


def is_t2(rows):
    n = len(rows)
    d1 = {(r[i], r[i + 1]) for r in rows for i in range(n - 1)}
    d2 = {(r[i], r[i + 2]) for r in rows for i in range(n - 2)}
    return all(sorted(r) == list(range(n)) for r in rows) and len(d1) == n * (n - 1) and len(d2) == n * (n - 2)


def automorphisms(rows, reverse):
    n, rowset = len(rows), {tuple(r) for r in rows}
    src = tuple(rows[0])[::-1] if reverse else tuple(rows[0])
    found = []
    for target in sorted(rowset):
        h = [0] * n
        for c in range(n):
            h[src[c]] = target[c]
        image = {tuple(h[x] for x in (r[::-1] if reverse else r)) for r in rowset}
        if image == rowset and (reverse or h != list(range(n))):
            found.append({'h': h, 'cycle_type': cycle_type(h)})
    return found


def main(argv):
    if len(argv) != 2:
        raise SystemExit('usage: SCRIPT OUTPUT.json')
    results = []
    for name, key in INPUTS:
        data = json.loads((ROOT / name).read_text())
        squares = data[key] if key else [data]
        for index, square in enumerate(squares):
            rows = square['rows'] if isinstance(square, dict) else square
            results.append({'source': name, 'source_sha256': hashlib.sha256((ROOT / name).read_bytes()).hexdigest(),
                            'index': index, 'n': len(rows), 'is_t2': is_t2(rows),
                            'symbol_automorphisms': automorphisms(rows, False),
                            'reversal_automorphisms': automorphisms(rows, True)})
    with Path(argv[1]).open('x', encoding='utf-8') as stream:
        json.dump({'results': results, 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
                  stream, indent=2, sort_keys=True)
        stream.write('\n')
    for r in results:
        print(r['n'], r['index'], r['is_t2'], [a['cycle_type'] for a in r['symbol_automorphisms']],
              [a['cycle_type'] for a in r['reversal_automorphisms']])


if __name__ == '__main__':
    main(sys.argv)
