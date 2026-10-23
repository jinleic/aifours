#!/usr/bin/env python3
"""Shared strict validation of stored receipt rows and survivor witnesses (math-p0039).

Imported by certify.py (replay and the survivor resolver) and by
check_coverage.py so both apply exactly the same rules:

* integers are Python ints, never bool or float;
* digests are 64-character lowercase hex strings;
* block fields are exactly the documented ones, with geometry, bookkeeping and
  libmpdec subset size equal to the values the caller derives from the task;
* survivors are integers; in tasks that permit survivors each one carries a
  resolution, otherwise none may appear;
* a resolution is the classical order n <= 8, an integer proper divisor of p, or
  a difference collision whose four coordinates are canonical representatives
  1..p-1 of elements of D = mu_(n+1) with a common nonzero difference 1..p-1;
* stored and recomputed rows are compared in canonical JSON, which keeps
  1, true and 1.0 distinct.

This module does no sieve or residue arithmetic and imports nothing local.
"""
import json


class CheckFailed(Exception):
    pass


def need(ok, message):
    if not ok:
        raise CheckFailed(message)


def is_int(x):
    return type(x) is int  # excludes bool and float


def is_hex64(x):
    return isinstance(x, str) and len(x) == 64 and all(c in '0123456789abcdef' for c in x)


def canonical(row):
    """Type-exact comparison form: JSON distinguishes 1, true and 1.0, unlike Python equality."""
    return json.dumps(row, sort_keys=True, separators=(',', ':'))


BLOCK_FIELDS = frozenset(('id', 'start', 'end', 'count', 'sieved', 'tested', 'survivors', 'sha256',
                          'mpdec_residues'))
OPTIONAL_FIELDS = frozenset(('resolutions', 'seconds'))
INT_FIELDS = ('id', 'start', 'end', 'count', 'sieved', 'tested', 'mpdec_residues')


def check_resolution(n, res):
    """Exact re-verification of one survivor resolution (small numbers only)."""
    need(is_int(n), 'survivor is not an integer')
    p = n * n + n + 1
    need(isinstance(res, dict) and is_int(res.get('n')) and is_int(res.get('p'))
         and res['n'] == n and res['p'] == p, 'resolution modulus')
    kind = res.get('resolution')
    if kind == 'classical-order-at-most-8':
        need(n in (2, 8) and set(res) == {'n', 'p', 'resolution'}, 'classical resolution only for n = 2, 8')
        return
    if kind == 'proper-factor':
        f = res.get('factor')
        need(set(res) == {'n', 'p', 'resolution', 'factor'}, 'resolution fields')
        need(is_int(f) and 1 < f < p and p % f == 0, 'resolution factor is not an integer proper divisor of p')
        return
    need(kind == 'difference-collision', 'unknown resolution kind')
    need(set(res) == {'n', 'p', 'resolution', 'pairs', 'difference'}, 'resolution fields')
    pairs, d = res['pairs'], res['difference']
    need(isinstance(pairs, list) and len(pairs) == 2
         and all(isinstance(x, list) and len(x) == 2 for x in pairs), 'collision witness shape')
    (a0, b0), (a1, b1) = pairs
    need(all(is_int(x) and 0 < x < p for x in (a0, b0, a1, b1)) and is_int(d) and 0 < d < p,
         'collision witness not in canonical representatives 1..p-1 with a nonzero difference')
    need(all(pow(x, n + 1, p) == 1 for x in (a0, b0, a1, b1)), 'collision witness outside D')
    need((a0, b0) != (a1, b1) and a0 != b0 and a1 != b1
         and (a0 - b0) % p == d and (a1 - b1) % p == d, 'collision witness pairs')


def check_block_row(row, block_id, geometry, step, stride, survivors_allowed, where):
    """Strict check of one stored block row; geometry = (start, end, count) derived by the caller.

    Returns the row's resolutions (empty when survivors are not allowed)."""
    need(isinstance(row, dict), 'block row is not an object: ' + where)
    keys = set(row)
    need(BLOCK_FIELDS <= keys <= BLOCK_FIELDS | OPTIONAL_FIELDS, 'missing or unexpected block fields: ' + where)
    need(all(is_int(row[k]) for k in INT_FIELDS), 'non-integer block field: ' + where)
    need(row['id'] == block_id, 'block id differs: ' + where)
    start, end, count = geometry
    need((row['start'], row['end'], row['count']) == (start, end, count), 'block geometry differs: ' + where)
    need(row['sieved'] >= 0 and row['tested'] >= 0 and row['sieved'] + row['tested'] == count,
         'count bookkeeping: ' + where)
    need(is_int(stride) and stride >= 1 and row['mpdec_residues'] == (row['tested'] + stride - 1) // stride,
         'libmpdec subset size: ' + where)
    need(is_hex64(row['sha256']), 'block digest is not a SHA-256 hex string: ' + where)
    need('seconds' not in row or (type(row['seconds']) in (int, float) and row['seconds'] >= 0),
         'block seconds: ' + where)
    survivors = row['survivors']
    need(isinstance(survivors, list) and all(is_int(n) for n in survivors), 'survivor list: ' + where)
    if not survivors_allowed:
        need(survivors == [] and 'resolutions' not in row, 'survivor in ' + where)
        return []
    res = row.get('resolutions', [])
    need(('resolutions' in row) == bool(survivors) and isinstance(res, list)
         and [x.get('n') if isinstance(x, dict) else None for x in res] == survivors,
         'unresolved survivor (each survivor needs exactly one resolution): ' + where)
    for n, x in zip(survivors, res):
        need(start <= n < end and (n - start) % step == 0, 'survivor outside block: ' + where)
        check_resolution(n, x)
    return res
