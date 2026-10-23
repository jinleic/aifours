#!/usr/bin/env python3
"""Generate the Lean data modules Gc80/Data*.lean from the two pinned raw certificates.

Usage: python3 -B gen_lean80.py OUT_DIR
  Writes OUT_DIR/Gc80/Data{Gc,Mc}{B,P0..P7,}.lean (20 files); refuses to overwrite any of them.
  The raw certificates are read from the review directory: $GC80_REVIEW if set, else the parent
  directory of this script; each must have its pinned SHA-256.

The Lean literals are the raw certificates copied verbatim in raw order; nothing is sorted,
repaired, deduplicated or reduced modulo 80:
  * gcDCQS  `groupsGc80`  = the 4 GROUPS lines (entry i = line i as a list of numbers);
            `blocksGc80`  = the BLOCKS section (entry i = block line i), split into chunks
                            `blocksGc80_k` of 500 lines, `List.flatten`ed in order;
            `colGc80_x`   = the `POINT x` section (entry j = the triple lines after `CLASS j`);
            `colourGc80`  = [colGc80_0, ..., colGc80_79].
  * mcDSQS  `blocksMc80`, `colMc80_x`, `colourMc80` in the same way.
Accepted raw format (anything else is an error): ASCII, `\\n` line ends, leading `#` comment
lines, then
  gcDCQS: `GCDCQS 80 4 20`, `COLOURS 40`, `HOLEFREE 10`, `GROUPS`, 4 lines of 20 numbers,
          `BLOCKS`, exactly 19400 lines of 4 numbers,
  mcDSQS: `MCDSQS 80`, `COLOURS 40`, `BLOCKS`, exactly 20540 lines of 4 numbers,
then `POINT x` for x = 0..79 in order, each with `CLASS 0`..`CLASS 39` in order, each followed by
at least one line of 3 numbers, and nothing after `POINT 79`.  Numbers have no leading zeros and
are separated by single spaces.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
REVIEW = Path(os.environ.get('GC80_REVIEW', HERE.parent)).resolve()
V, COLOURS, POINT_CHUNK, BLOCK_CHUNK = 80, 40, 10, 500
NUM = r'(0|[1-9][0-9]*)'
QUAD = re.compile(' '.join([NUM] * 4))
TRIPLE = re.compile(' '.join([NUM] * 3))
GROUP = re.compile(' '.join([NUM] * 20))
DESIGNS = {
    'Gc': {
        'raw': 'gcdcqs20-parent-inputs-v1/gcdcqs20-e1s1_p10.txt',
        'sha256': '58b51b50b5281df613c5fae0a3b0178a374554a2f062e55bd8fc25250922a0ca',
        'header': ['GCDCQS 80 4 20', 'COLOURS 40', 'HOLEFREE 10', 'GROUPS'],
        'groups': 4,
        'blocks': 19400,
        'name': 'gcDCQS(20^4 : 0) certificate A',
    },
    'Mc': {
        'raw': 'mcdsqs80-parent-inputs-v1/mcdsqs80_c21_A.txt',
        'sha256': '49f500c5eedd9a79553e1228d0232e203a749bbda04e3a891c52778dbe9d44a3',
        'header': ['MCDSQS 80', 'COLOURS 40'],
        'groups': 0,
        'blocks': 20540,
        'name': 'mcDSQS(80) certificate',
    },
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parse(raw_text, spec):
    """Return the parsed sections with their 1-based raw line numbers."""
    require(raw_text.endswith('\n') and '\r' not in raw_text, 'noncanonical line endings')
    lines = raw_text.split('\n')[:-1]
    i = 0
    comments = []
    while i < len(lines) and lines[i].startswith('#'):
        comments.append(lines[i])
        i += 1
    n_head = len(spec['header'])
    require(lines[i:i + n_head] == spec['header'], f'header lines {i + 1}-{i + n_head}')
    i += n_head
    groups = []
    groups_first = i + 1
    for _ in range(spec['groups']):
        m = GROUP.fullmatch(lines[i])
        require(m is not None, f'invalid GROUPS line {i + 1}')
        groups.append([int(x) for x in m.groups()])
        i += 1
    require(lines[i] == 'BLOCKS', f'expected BLOCKS at line {i + 1}')
    i += 1
    blocks_first = i + 1
    blocks = []
    for _ in range(spec['blocks']):
        m = QUAD.fullmatch(lines[i])
        require(m is not None, f'invalid block line {i + 1}')
        blocks.append(tuple(int(x) for x in m.groups()))
        i += 1
    points = []
    for x in range(V):
        require(i < len(lines) and lines[i] == f'POINT {x}', f'expected POINT {x} at line {i + 1}')
        first = i + 1
        i += 1
        classes = []
        for j in range(COLOURS):
            require(i < len(lines) and lines[i] == f'CLASS {j}',
                    f'expected CLASS {j} of POINT {x} at line {i + 1}')
            i += 1
            cls = []
            while i < len(lines):
                m = TRIPLE.fullmatch(lines[i])
                if m is None:
                    break
                cls.append(tuple(int(t) for t in m.groups()))
                i += 1
            require(cls, f'empty CLASS {j} at POINT {x}')
            classes.append(cls)
        points.append({'first_line': first, 'last_line': i, 'classes': classes})
    require(i == len(lines), f'unexpected line {i + 1} after POINT {V - 1}')
    return {'comments': comments, 'groups': groups, 'groups_first_line': groups_first,
            'blocks': blocks, 'blocks_first_line': blocks_first, 'points': points,
            'n_lines': len(lines)}


def triples_body(cls, indent):
    return (',\n' + indent).join(', '.join(f'({a}, {b}, {c})' for a, b, c in cls[t:t + 6])
                                 for t in range(0, len(cls), 6))


def header_comment(spec, raw_bytes, parsed, what):
    sha = hashlib.sha256(raw_bytes).hexdigest()
    first = raw_bytes.decode('ascii').split('\n')[0]
    return f'''/-
GENERATED FILE - do not edit.  Produced by gen_lean80.py from the raw {spec['name']}
review/{spec['raw']}
({len(raw_bytes)} bytes, SHA-256 {sha}, {parsed['n_lines']} lines),
first line `{first}`.
{what}
Nothing is assumed about these numbers here: Gc80.Check80 states the checkers and their
soundness theorems, and the Gc80.Cert* modules run them in the Lean kernel.
-/
'''


def render(key, spec, raw_bytes, parsed):
    """Return {module name: text}."""
    files = {}
    blocks, points = parsed['blocks'], parsed['points']
    nb = len(blocks)
    b0 = parsed['blocks_first_line']
    # blocks (and groups) module
    what = (f'`blocks{key}80` is the BLOCKS section (raw lines {b0}-{b0 + nb - 1}), verbatim in raw order\n'
            f'(chunks `blocks{key}80_k` of at most {BLOCK_CHUNK} lines, flattened in order).')
    if parsed['groups']:
        g0 = parsed['groups_first_line']
        what += (f'\n`groups{key}80` is the GROUPS section (raw lines {g0}-{g0 + len(parsed["groups"]) - 1}),'
                 ' verbatim (entry i = raw line i as a list of numbers).')
    out = ['import McdKernel.Check\n\n', header_comment(spec, raw_bytes, parsed, what),
           '\nnamespace Mcd.Kernel\n',
           f'\n/-- SHA-256 of the raw certificate bytes, recorded by gen_lean80.py (documentation only). -/\n'
           f'def raw{key}80Sha256 : String := "{hashlib.sha256(raw_bytes).hexdigest()}"\n']
    if parsed['groups']:
        g0 = parsed['groups_first_line']
        body = ',\n  '.join('[' + ', '.join(str(n) for n in g) + ']' for g in parsed['groups'])
        out.append(f'\n/-- The raw GROUPS lines {g0}-{g0 + len(parsed["groups"]) - 1}, verbatim. -/\n'
                   f'def groups{key}80 : List (List ℕ) := [\n  {body}]\n')
    names = []
    for k in range(0, nb, BLOCK_CHUNK):
        chunk = blocks[k:k + BLOCK_CHUNK]
        body = ',\n  '.join(', '.join(f'({a}, {b}, {c}, {d})' for a, b, c, d in chunk[j:j + 6])
                             for j in range(0, len(chunk), 6))
        name = f'blocks{key}80_{k // BLOCK_CHUNK}'
        names.append(name)
        out.append(f'\n/-- Raw block lines {b0 + k}-{b0 + k + len(chunk) - 1}, verbatim. -/\n'
                   f'def {name} : List RawQuad := [\n  {body}]\n')
    joined = ',\n    '.join(', '.join(names[j:j + 6]) for j in range(0, len(names), 6))
    out.append(f'\n/-- The {nb} raw block lines, in raw order. -/\n'
               f'def blocks{key}80 : List RawQuad :=\n  List.flatten [\n    {joined}]\n')
    out.append('\nend Mcd.Kernel\n')
    files[f'Data{key}B'] = ''.join(out)
    # point modules
    for m in range(V // POINT_CHUNK):
        xs = range(m * POINT_CHUNK, (m + 1) * POINT_CHUNK)
        what = (f'`col{key}80_x` (x = {xs[0]}..{xs[-1]}) is the raw `POINT x` section, entry j being the triple\n'
                'lines after `CLASS j`, verbatim in raw order.')
        out = ['import McdKernel.Check\n\n', header_comment(spec, raw_bytes, parsed, what),
               '\nnamespace Mcd.Kernel\n']
        for x in xs:
            p = points[x]
            rows = [f'  -- CLASS {j}\n  [{triples_body(cls, "    ")}]' for j, cls in enumerate(p['classes'])]
            data = ',\n'.join(rows)
            out.append(f'\n/-- The raw `POINT {x}` section (raw lines {p["first_line"]}-{p["last_line"]}), verbatim. -/\n'
                       f'def col{key}80_{x} : List (List RawTriple) := [\n{data}]\n')
        out.append('\nend Mcd.Kernel\n')
        files[f'Data{key}P{m}'] = ''.join(out)
    # collecting module
    what = f'`colour{key}80` lists the {V} raw `POINT` sections in raw order (`POINT 0`, ..., `POINT {V - 1}`).'
    imports = [f'import Gc80.Data{key}B\n'] + [f'import Gc80.Data{key}P{m}\n' for m in range(V // POINT_CHUNK)]
    joined = ',\n    '.join(', '.join(f'col{key}80_{x}' for x in range(j, min(j + 8, V)))
                           for j in range(0, V, 8))
    out = [''.join(imports), '\n', header_comment(spec, raw_bytes, parsed, what), '\nnamespace Mcd.Kernel\n',
           f'\n/-- The {V} raw `POINT` sections, in raw order. -/\n'
           f'def colour{key}80 : List (List (List RawTriple)) := [\n    {joined}]\n',
           '\nend Mcd.Kernel\n']
    files[f'Data{key}'] = ''.join(out)
    return files


def main(argv):
    require(len(argv) == 1, __doc__)
    out_dir = Path(argv[0]) / 'Gc80'
    out_dir.mkdir(parents=True, exist_ok=True)
    report = {'review_dir': str(REVIEW), 'designs': {}}
    for key, spec in DESIGNS.items():
        raw_bytes = (REVIEW / spec['raw']).read_bytes()
        sha = hashlib.sha256(raw_bytes).hexdigest()
        require(sha == spec['sha256'], f'{spec["raw"]}: SHA-256 {sha} is not the pinned {spec["sha256"]}')
        parsed = parse(raw_bytes.decode('ascii'), spec)
        files = render(key, spec, raw_bytes, parsed)
        written = {}
        for name, text in files.items():
            path = out_dir / f'{name}.lean'
            with path.open('x') as stream:
                stream.write(text)
            written[f'Gc80/{name}.lean'] = hashlib.sha256(text.encode()).hexdigest()
        report['designs'][key] = {
            'raw': f'review/{spec["raw"]}', 'raw_sha256': sha, 'raw_lines': parsed['n_lines'],
            'groups': len(parsed['groups']), 'blocks': len(parsed['blocks']),
            'blocks_first_line': parsed['blocks_first_line'],
            'points': len(parsed['points']),
            'classes': sum(len(p['classes']) for p in parsed['points']),
            'triples': sum(len(c) for p in parsed['points'] for c in p['classes']),
            'written': written}
    print(json.dumps(report, indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
