#!/usr/bin/env python3
"""Deterministic stdlib generator of the SW(25,16) Lean literal modules, with byte-exact check mode.

Usage:
  python3 -B gen_lean.py --write MODE OUT.lean [INPUT]   create OUT.lean (exclusive: refuses an existing file)
  python3 -B gen_lean.py --check MODE OUT.lean [INPUT]   regenerate in memory and compare with OUT.lean byte for byte
  python3 -B gen_lean.py --facts [RAW]                   print raw/fixture facts as JSON (writes nothing)

MODE:
  data  module SW25.Data: the raw witness.  `SW25.rows` holds the 25 raw rows verbatim and in raw order (row i is
        raw line i + 2, entry j of row i is token j of that line, read as an integer), and
        `SW25.W : Fin 25 -> Fin 25 -> Int` reads entry j of row i.
  flip  module SW25Flip.Data: NEGATIVE-CONTROL FIXTURE.  The same rows except that the entries at (a, b) and (b, a)
        are negated, where (a, b) is the first strictly-upper-triangular nonzero position of the raw matrix in
        row-major order.  This symmetric sign flip keeps the alphabet, symmetry and every row weight.
  twin  module SW25Flip.GramFails: EXPECTED-FAILURE TWIN.  A fixed comment header followed by the text of
        SW25/Main.lean with the prefix `SW25` replaced by `SW25Flip` (`SW25.` -> `SW25Flip.`, `namespace SW25`,
        `end SW25`), i.e. the identical statements and proof scripts applied to the fixture.

INPUT for data/flip is the raw witness, default <review>/sw25-parent-inputs-v1/sw25-16-witness-v1.sw, where
<review> is $SW25_REVIEW or the parent of this script's directory.  It must have SHA-256 EXPECTED_SHA256,
EXPECTED_BYTES bytes and the strict layout of the parent checker: header line `SW 25 16`, then exactly 25 lines
of exactly 25 tokens from {-1, 0, 1} separated by single spaces, final LF, no CR, TAB or blank line.
INPUT for twin is SW25/Main.lean, default <OUT's package root>/SW25/Main.lean.
No mathematical property of the matrix is assumed or checked here; the Lean kernel checks the property.
"""
import hashlib
import json
import os
import re
import sys
from pathlib import Path

EXPECTED_SHA256 = 'bfadf44596bc5138106432690bf507a8ff9c36cd3c40eb8eeb08195a9b2d4ab0'
EXPECTED_BYTES = 1459
RAW_REL = 'sw25-parent-inputs-v1/sw25-16-witness-v1.sw'
N, WEIGHT = 25, 16
HEADER = f'SW {N} {WEIGHT}'


def default_raw():
    here = Path(__file__).resolve().parent
    return Path(os.environ.get('SW25_REVIEW', here.parent)) / RAW_REL


def parse(raw):
    if hashlib.sha256(raw).hexdigest() != EXPECTED_SHA256 or len(raw) != EXPECTED_BYTES:
        raise SystemExit('raw witness SHA-256/size mismatch')
    if not raw.endswith(b'\n') or raw.endswith(b'\n\n') or b'\r' in raw or b'\t' in raw:
        raise SystemExit('raw witness layout: final LF / blank line / CR / TAB')
    lines = raw[:-1].split(b'\n')
    if len(lines) != N + 1 or lines[0] != HEADER.encode():
        raise SystemExit('raw witness line count or header')
    rows = []
    for line in lines[1:]:
        toks = line.split(b' ')
        if len(toks) != N or any(t not in (b'-1', b'0', b'1') for t in toks):
            raise SystemExit('raw witness row layout')
        rows.append([t.decode() for t in toks])
    return rows


def flip_position(rows):
    for a in range(N):
        for b in range(a + 1, N):
            if rows[a][b] != '0':
                return a, b
    raise SystemExit('no off-diagonal nonzero entry')


def negate(tok):
    return {'1': '-1', '-1': '1'}[tok]


def render_rows(namespace, rows, flipped, header_lines):
    out = ['/-'] + header_lines + ['-/', '', f'namespace {namespace}', '',
                                   f'/-- The {N} rows (raw lines 2-{N + 1}), in raw order, as integers. -/',
                                   'def rows : List (List Int) := [']
    for i, row in enumerate(rows):
        note = ''.join(f' (entry {j} negated)' for (r, j) in flipped if r == i)
        out.append(f'  -- row {i} = raw line {i + 2}{note}')
        out.append('  [' + ', '.join(row) + (']' if i == N - 1 else '],'))
    out += [']', '',
            f'/-- The matrix as a function `Fin {N} → Fin {N} → Int`: `W i j` is entry `j` of row `i` of `rows`. -/',
            f'def W : Fin {N} → Fin {N} → Int := fun i j => (rows.getD i.val []).getD j.val 0',
            '', f'end {namespace}', '']
    return '\n'.join(out)


def provenance(raw):
    return [f'review/{RAW_REL}',
            f'({len(raw)} bytes, SHA-256 {EXPECTED_SHA256}, {raw.count(chr(10).encode())} lines), '
            f'header line `{HEADER}`.']


def render_data(raw):
    rows = parse(raw)
    header = ['GENERATED FILE - do not edit.  Produced by `gen_lean.py --write data` from the raw SW(25,16) witness'
              ] + provenance(raw) + [
        '`rows` is the list of the 25 raw rows in raw order (row i is raw line i + 2); row i is the list of the 25',
        'tokens of that line, verbatim and in raw order, read as integers.  Nothing is assumed about these numbers',
        'here: module SW25.Main checks their properties in the Lean kernel.']
    return render_rows('SW25', rows, [], header)


def render_flip(raw):
    rows = parse(raw)
    a, b = flip_position(rows)
    old = rows[a][b]
    flipped = [list(r) for r in rows]
    flipped[a][b] = negate(flipped[a][b])
    flipped[b][a] = negate(flipped[b][a])
    header = ['GENERATED FILE - do not edit.  Produced by `gen_lean.py --write flip` from the raw SW(25,16) witness'
              ] + provenance(raw) + [
        'NEGATIVE-CONTROL FIXTURE, NOT the witness: identical to the raw rows except that the entries at',
        f'(row {a}, column {b}) and (row {b}, column {a}) are negated (raw values {old} and {rows[b][a]} become '
        f'{flipped[a][b]} and {flipped[b][a]}).',
        f'({a}, {b}) is the first strictly-upper-triangular nonzero position of the raw matrix in row-major order,',
        'so this symmetric sign flip keeps the alphabet, symmetry and every row weight.  Module SW25Flip.Facts and',
        'the expected-failure twin SW25Flip.GramFails test the exact Gram property on it.']
    return render_rows('SW25Flip', flipped, [(a, b), (b, a)], header)


def render_twin(main_bytes):
    text = main_bytes.decode()
    if 'SW25Flip' in text:
        raise SystemExit('Main.lean already mentions SW25Flip')
    for needle in ('namespace SW25\n', 'end SW25\n', 'import SW25.Data\n'):
        if text.count(needle) != 1:
            raise SystemExit(f'Main.lean must contain {needle!r} exactly once')
    twin = text.replace('SW25.', 'SW25Flip.').replace('namespace SW25\n', 'namespace SW25Flip\n').replace(
        'end SW25\n', 'end SW25Flip\n')
    if re.search(r'SW25(?!Flip)', twin):
        raise SystemExit('Main.lean has an occurrence of SW25 not covered by the twin substitution')
    header = [
        '-- EXPECTED-FAILURE TWIN (negative control).  GENERATED by `gen_lean.py --write twin` from SW25/Main.lean',
        f'-- (SHA-256 {hashlib.sha256(main_bytes).hexdigest()}): the identical text with the prefix SW25 replaced by',
        '-- SW25Flip, so every statement and proof script is the same but the matrix is the sign-flipped fixture',
        '-- SW25Flip.W.  Building this module must FAIL: `decide` must prove the Gram statement W_gram false.',
    ]
    return '\n'.join(header) + '\n' + twin


def facts(raw):
    rows = [[int(t) for t in r] for r in parse(raw)]
    a, b = flip_position([[str(x) for x in r] for r in rows])
    f = [list(r) for r in rows]
    f[a][b], f[b][a] = -f[a][b], -f[b][a]

    def gram(m, i, j):
        return sum(m[i][k] * m[j][k] for k in range(N))
    bad = [(i, j, gram(f, i, j)) for i in range(N) for j in range(N) if gram(f, i, j) != (WEIGHT if i == j else 0)]
    return {
        'raw_sha256': EXPECTED_SHA256, 'raw_bytes': len(raw), 'flip_position': [a, b],
        'raw_values_at_flip': [rows[a][b], rows[b][a]],
        'fixture_gram_violations_ordered_pairs': len(bad),
        'fixture_first_violation_i_j_value': list(bad[0]) if bad else None,
        'note': 'Python integer arithmetic on the fixture; informational cross-check of SW25Flip.Facts only.',
    }


def main(argv):
    if len(argv) in (2, 3) and argv[1] == '--facts':
        raw = Path(argv[2]).read_bytes() if len(argv) == 3 else default_raw().read_bytes()
        print(json.dumps(facts(raw), indent=1))
        return 0
    if len(argv) not in (4, 5) or argv[1] not in ('--write', '--check') or argv[2] not in ('data', 'flip', 'twin'):
        raise SystemExit(__doc__)
    action, mode, target = argv[1], argv[2], Path(argv[3])
    if mode == 'twin':
        src = Path(argv[4]) if len(argv) == 5 else target.resolve().parent.parent / 'SW25' / 'Main.lean'
        text = render_twin(src.read_bytes())
    else:
        raw = Path(argv[4]).read_bytes() if len(argv) == 5 else default_raw().read_bytes()
        text = render_data(raw) if mode == 'data' else render_flip(raw)
    data = text.encode()
    digest = hashlib.sha256(data).hexdigest()
    if action == '--write':
        with open(target, 'xb') as f:
            f.write(data)
        print(f'wrote {target} sha256={digest}')
        return 0
    same = target.read_bytes() == data
    print(f'{"MATCH" if same else "MISMATCH"} {mode} {target} regenerated_sha256={digest}')
    return 0 if same else 1


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
