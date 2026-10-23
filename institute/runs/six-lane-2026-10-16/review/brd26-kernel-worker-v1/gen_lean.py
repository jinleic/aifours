#!/usr/bin/env python3
"""Generate Brd26/Data.lean from the raw BRD(26,130,25,5,4) witness (deterministic, byte-exact).

Usage:
  python3 -B gen_lean.py --write OUT.lean [RAW]   create OUT.lean (exclusive; refuses an existing file)
  python3 -B gen_lean.py --check OUT.lean [RAW]   regenerate in memory and compare with OUT.lean byte for byte

RAW defaults to $BRD26_REVIEW/brd26-parent-inputs-v1/brd26-130-witness-v1.brd, where BRD26_REVIEW
defaults to the parent directory of the directory holding this script (the six-lane review/).
The raw file must have SHA-256 EXPECTED_SHA256 and the strict layout of the parent checker
(review/brd26-parent-inputs-v1/check_brd_parent.py): header line `BRD 26 130 25 5 4`, then exactly
26 lines of exactly 130 tokens from {-1, 0, 1} separated by single spaces, final LF, no CR/TAB.
Every token is copied into the Lean literal verbatim and in raw order: row i of `brd26Rows` is raw
line i + 2 and entry j of that row is the j-th token of that line.  No validity property is assumed or
checked here; the Lean kernel checks the BRD property of these literals.
"""
import hashlib
import os
import sys
from pathlib import Path

EXPECTED_SHA256 = 'eb15cba18110e8c2e4ba7798838fc0a8fd508310d8a73a04132abb49977d71fe'
RAW_REL = 'brd26-parent-inputs-v1/brd26-130-witness-v1.brd'
PARAMS = (26, 130, 25, 5, 4)
PER_LINE = 26


def default_raw():
    here = Path(__file__).resolve().parent
    review = Path(os.environ.get('BRD26_REVIEW', here.parent))
    return review / RAW_REL


def parse(raw):
    v, b = PARAMS[0], PARAMS[1]
    if hashlib.sha256(raw).hexdigest() != EXPECTED_SHA256:
        raise SystemExit('raw witness SHA-256 mismatch')
    if not raw.endswith(b'\n') or raw.endswith(b'\n\n') or b'\r' in raw or b'\t' in raw:
        raise SystemExit('raw witness layout: final LF / CR / TAB')
    lines = raw[:-1].split(b'\n')
    if len(lines) != v + 1:
        raise SystemExit('raw witness line count')
    if lines[0] != ('BRD ' + ' '.join(map(str, PARAMS))).encode():
        raise SystemExit('raw witness header')
    rows = []
    for line in lines[1:]:
        toks = line.split(b' ')
        if len(toks) != b or any(t not in (b'-1', b'0', b'1') for t in toks):
            raise SystemExit('raw witness row layout')
        rows.append([t.decode() for t in toks])
    return lines[0].decode(), rows


def render(raw):
    header, rows = parse(raw)
    nlines = raw.count(b'\n')
    out = [
        '/-',
        'GENERATED FILE - do not edit.  Produced by gen_lean.py from the raw BRD(26,130,25,5,4) witness',
        'review/' + RAW_REL,
        f'({len(raw)} bytes, SHA-256 {EXPECTED_SHA256}, {nlines} lines),',
        f'header line `{header}`.',
        '`brd26Header` is the five header numbers.  `brd26Rows` is the list of the 26 raw rows in raw',
        'order (row i is raw line i + 2); row i is the list of the 130 tokens of that line, verbatim and in',
        'raw order, read as integers.  Nothing is assumed about these numbers here: Brd26.Proof checks',
        'the BRD property of `Brd26.brdM` (Brd26.Witness), which reads its entries from `brd26Rows`.',
        '-/',
        '',
        'namespace Brd26',
        '',
        f'/-- The raw header numbers (raw line 1 is `{header}`). -/',
        'def brd26Header : List Nat := [' + ', '.join(header.split(' ')[1:]) + ']',
        '',
        '/-- The 26 raw rows (raw lines 2-27), verbatim, as integers. -/',
        'def brd26Rows : List (List Int) := [',
    ]
    for i, row in enumerate(rows):
        out.append(f'  -- row {i} = raw line {i + 2}')
        chunks = [', '.join(row[s:s + PER_LINE]) for s in range(0, len(row), PER_LINE)]
        body = ',\n    '.join(chunks)
        out.append('  [' + body + (']' if i == len(rows) - 1 else '],'))
    out += [']', '', 'end Brd26', '']
    return '\n'.join(out)


def main(argv):
    if len(argv) not in (3, 4) or argv[1] not in ('--write', '--check'):
        raise SystemExit(__doc__)
    mode, target = argv[1], Path(argv[2])
    raw_path = Path(argv[3]) if len(argv) == 4 else default_raw()
    text = render(raw_path.read_bytes())
    if mode == '--write':
        with open(target, 'x') as f:
            f.write(text)
        print(f'wrote {target} sha256={hashlib.sha256(text.encode()).hexdigest()}')
        return 0
    same = target.read_bytes() == text.encode()
    print(f'{"MATCH" if same else "MISMATCH"} {target} regenerated_sha256={hashlib.sha256(text.encode()).hexdigest()}')
    return 0 if same else 1


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
