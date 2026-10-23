#!/usr/bin/env python3
"""Generate McdKernel/Data38.lean from the pinned raw mcDSQS(38) certificate.

Usage: python3 -B gen_lean.py OUT_DIR      (refuses to overwrite OUT_DIR/Data38.lean)

The Lean literals are the raw certificate copied verbatim in raw order:
  * `blocks38` is the BLOCKS section: entry i is raw block line i + 1 (after `BLOCKS`), split
    into the chunks `blocks38_k` of at most 300 lines (concatenated in order);
  * `col38_x` is the `POINT x` section: entry j is the list of triple lines after `CLASS j`;
    `colour38` lists `col38_0, ..., col38_37` in order.
Nothing is sorted, repaired or reduced modulo 38.  The raw file must have its pinned SHA-256,
ASCII text with `\\n` line ends, leading `#` comment lines only, `MCDSQS 38`, `COLOURS 19`,
`BLOCKS`, exactly C(38,3)/4 = 2109 block lines of four numbers, then `POINT x` for x = 0..37 in
order, each with `CLASS 0`..`CLASS 18` in order, each followed by at least one line of three
numbers.  Numbers are written without leading zeros.
"""
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent
RAW = 'mcdsqs38-parent-inputs-v1/mcdsqs38_g342_s0.txt'
RAW_SHA256 = '973f93e4646e48df64b70b3a64811afcdc87b10a1767222f54ffe65d3a303f1c'
V, COLOURS, NBLOCKS, CHUNK = 38, 19, 2109, 300
NUM = r'(0|[1-9][0-9]*)'
QUAD = re.compile(' '.join([NUM] * 4))
TRIPLE = re.compile(' '.join([NUM] * 3))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parse(raw_text):
    """Return (header line numbers, blocks with line numbers, points) of the raw certificate."""
    require(raw_text.endswith('\n') and '\r' not in raw_text, 'noncanonical line endings')
    lines = raw_text.split('\n')[:-1]
    i = 0
    while lines[i].startswith('#'):
        i += 1
    require(lines[i:i + 3] == [f'MCDSQS {V}', f'COLOURS {COLOURS}', 'BLOCKS'], 'header')
    i += 3
    first_block = i + 1
    blocks = []
    for k in range(NBLOCKS):
        m = QUAD.fullmatch(lines[i + k])
        require(m is not None, f'invalid block line {i + k + 1}')
        blocks.append(tuple(int(x) for x in m.groups()))
    i += NBLOCKS
    points = []
    for x in range(V):
        require(lines[i] == f'POINT {x}', f'expected POINT {x} at line {i + 1}')
        start = i + 1
        i += 1
        classes = []
        for j in range(COLOURS):
            require(i < len(lines) and lines[i] == f'CLASS {j}', f'expected CLASS {j} at line {i + 1}')
            i += 1
            cls = []
            while i < len(lines) and TRIPLE.fullmatch(lines[i]):
                cls.append(tuple(int(x) for x in lines[i].split(' ')))
                i += 1
            require(cls, f'empty CLASS {j} at POINT {x}')
            classes.append(cls)
        points.append({'first_line': start, 'last_line': i, 'classes': classes})
    require(i == len(lines), 'trailing lines')
    return first_block, blocks, points


def render(raw_bytes, first_block, blocks, points):
    raw_sha = hashlib.sha256(raw_bytes).hexdigest()
    header = raw_bytes.decode('ascii').split('\n')[0]
    out = [f'''import McdKernel.Check

/-
GENERATED FILE - do not edit.  Produced by gen_lean.py from the raw certificate
review/{RAW}
({len(raw_bytes)} bytes, SHA-256 {raw_sha}),
first line `{header}`.
`blocks38` is the BLOCKS section (raw lines {first_block}-{first_block + NBLOCKS - 1}), copied verbatim in raw
order (chunks `blocks38_k` of at most {CHUNK} lines); `col38_x` is the `POINT x` section, entry j
being the triple lines after `CLASS j`, copied verbatim in raw order; `colour38` lists
`col38_0, ..., col38_37`.  Nothing is assumed about these numbers here: McdKernel.Check states
the checkers and their soundness theorems, and McdKernel.Cert38 runs them in the Lean kernel.
-/

namespace Mcd.Kernel

/-- SHA-256 of the raw certificate bytes, recorded by gen_lean.py (documentation only). -/
def data38RawSha256 : String := "{raw_sha}"
''']
    names = []
    for k in range(0, NBLOCKS, CHUNK):
        chunk = blocks[k:k + CHUNK]
        body = ',\n  '.join(', '.join(f'({a}, {b}, {c}, {d})' for a, b, c, d in chunk[j:j + 6])
                             for j in range(0, len(chunk), 6))
        name = f'blocks38_{k // CHUNK}'
        names.append(name)
        out.append(f'''
/-- Raw block lines {first_block + k}-{first_block + k + len(chunk) - 1}, verbatim. -/
def {name} : List RawQuad := [
  {body}]
''')
    out.append(f'''
/-- The {NBLOCKS} raw block lines, in raw order. -/
def blocks38 : List RawQuad :=
  {' ++ '.join(names)}
''')
    for x, p in enumerate(points):
        rows = []
        for j, cls in enumerate(p['classes']):
            body = ',\n    '.join(', '.join(f'({a}, {b}, {c})' for a, b, c in cls[t:t + 6])
                                  for t in range(0, len(cls), 6))
            rows.append(f'  -- CLASS {j}\n  [{body}]')
        data = ',\n'.join(rows)
        out.append(f'''
/-- The raw `POINT {x}` section (raw lines {p['first_line']}-{p['last_line']}), verbatim. -/
def col38_{x} : List (List RawTriple) := [
{data}]
''')
    out.append(f'''
/-- The {V} raw `POINT` sections, in raw order (`POINT 0`, ..., `POINT {V - 1}`). -/
def colour38 : List (List (List RawTriple)) :=
  [{', '.join(f'col38_{x}' for x in range(V))}]

end Mcd.Kernel
''')
    return ''.join(out)


def main(argv):
    require(len(argv) == 1, __doc__)
    out = Path(argv[0]) / 'Data38.lean'
    raw_bytes = (REVIEW / RAW).read_bytes()
    require(hashlib.sha256(raw_bytes).hexdigest() == RAW_SHA256, 'raw certificate SHA-256 mismatch')
    first_block, blocks, points = parse(raw_bytes.decode('ascii'))
    text = render(raw_bytes, first_block, blocks, points)
    with out.open('x') as stream:
        stream.write(text)
    print(json.dumps({'written': str(out), 'sha256': hashlib.sha256(text.encode()).hexdigest(),
                      'blocks': len(blocks), 'first_block_line': first_block,
                      'point_lines': [[p['first_line'], p['last_line']] for p in points[:2]] + ['...'],
                      'triples': sum(len(c) for p in points for c in p['classes'])}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
