#!/usr/bin/env python3
"""Generate PC100Kernel/Data100.lean and PC100Kernel/Data64.lean from pinned raw certificates (stdlib only).

Usage: python3 -B gen_lean.py OUTDIR      (writes OUTDIR/Data100.lean and OUTDIR/Data64.lean; refuses to
                                           overwrite either file)

Inputs (strict POINT-CYCLIC-RESOLUTION format; SHA-256 pinned below):
* Data100: the lane's witness certificate certs/v100/pc100_t2.cert and, for the documentation header only,
  the compact seed certs/v100/pc100_t2.seed.  `cert100` is the certificate copied verbatim in raw order.
* Data64 (controls only): controls/v64/tz64.cert, the published point-cyclic 2-(64,4,1) resolution of
  Topalova-Zhelezova 2026 as expanded by code/control64.py.  `tz64` is that certificate verbatim.
Class i of a literal is the list of the lines `i a b c d` (in file order), each as the raw block
(a, b, c, d).  No number is changed, sorted or reduced here; the Lean checker tests the ranges itself.
"""
import hashlib
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
LANE = HERE.parent
NUM = r'(0|[1-9][0-9]*)'
PER_LINE = 5
SPECS = {
    'Data100': {'cert': 'certs/v100/pc100_t2.cert',
                'cert_sha256': '971f722460020f5a572b4f17f1cffe249488b8de079badbfa0184b9a79b4f7c1',
                'seed': 'certs/v100/pc100_t2.seed',
                'seed_sha256': 'ac727835e2f15075e0697206d81482b634ed76c5f7ff000adc58bef43b256245',
                'v': 100, 'ncl': 33, 'bpc': 25, 'name': 'cert100'},
    'Data64': {'cert': 'controls/v64/tz64.cert',
               'cert_sha256': 'd8c1173596cc60f0276c7aab77bfb2c5c162cedd682f32365b628bf11d9a4b2f',
               'v': 64, 'ncl': 21, 'bpc': 16, 'name': 'tz64'},
}


def fail(msg):
    raise SystemExit(f'gen_lean.py: {msg}')


def parse_cert(raw, v, ncl, bpc):
    if not raw.endswith(b'\n') or b'\r' in raw:
        fail('noncanonical line endings')
    lines = raw.decode('ascii').split('\n')[:-1]
    if lines[0] != f'POINT-CYCLIC-RESOLUTION {v} 4 {ncl} {bpc}':
        fail(f'header {lines[0]!r}')
    classes = [[] for _ in range(ncl)]
    for ln, line in enumerate(lines[1:], start=2):
        if not re.fullmatch(' '.join([NUM] * 5), line):
            fail(f'line {ln}: {line!r}')
        c, a, b, x, y = (int(t) for t in line.split(' '))
        if not 0 <= c < ncl:
            fail(f'line {ln}: class index')
        classes[c].append(((a, b, x, y), ln))
    if len(lines) != 1 + ncl * bpc or any(len(c) != bpc for c in classes):
        fail('shape')
    index = [int(line.split(' ')[0]) for line in lines[1:]]
    if index != sorted(index):
        fail('class indices not in nondecreasing file order')
    return classes


def render_literal(name, classes, doc):
    out = [f'/-- {doc} -/', f'def {name} : List (List RawBlock) := [']
    for i, cls in enumerate(classes):
        out.append(f'  -- CLASS {i} (raw lines {cls[0][1]}-{cls[-1][1]})')
        items = [f'({a}, {b}, {c}, {d})' for (a, b, c, d), _ in cls]
        rows = [', '.join(items[k:k + PER_LINE]) for k in range(0, len(items), PER_LINE)]
        for k, row in enumerate(rows):
            prefix = '  [' if k == 0 else '    '
            if k < len(rows) - 1:
                out.append(prefix + row + ',')
            else:
                out.append(prefix + row + ']' + (',' if i < len(classes) - 1 else ''))
    out.append(']')
    return out


def render100(classes, cert_bytes, seed_bytes):
    out = ['import PC100Kernel.Check', '', '/-',
           'GENERATED FILE - do not edit.  Produced by gen_lean.py from the raw certificate',
           'information-science/evidence/six-lane-20261016/point-cyclic100/certs/v100/pc100_t2.cert',
           f'({len(cert_bytes)} bytes, SHA-256 {hashlib.sha256(cert_bytes).hexdigest()}),',
           'first line `POINT-CYCLIC-RESOLUTION 100 4 33 25`.',
           '`cert100` is the certificate copied verbatim in raw order: entry j of class i is the j-th line',
           '`i a b c d` of the file with class index i, as the raw block (a, b, c, d) (class i occupies raw',
           'lines 25 i + 2 to 25 i + 26).  The certificate was expanded by code/pc_expand.py from the compact',
           'seed certs/v100/pc100_t2.seed',
           f'({len(seed_bytes)} bytes, SHA-256 {hashlib.sha256(seed_bytes).hexdigest()});',
           'the seed is not used by any Lean proof (audit_binding.py checks the expansion externally).',
           'Nothing is assumed about these numbers here: PC100Kernel.Check states the checker and its',
           'soundness theorem, and PC100Kernel.Cert100 runs the checker in the Lean kernel.',
           '-/', '', 'namespace PC100.Kernel', '',
           '/-- SHA-256 of the raw certificate bytes, recorded by gen_lean.py (documentation only). -/',
           f'def cert100RawSha256 : String := "{hashlib.sha256(cert_bytes).hexdigest()}"', '',
           '/-- SHA-256 of the compact seed bytes, recorded by gen_lean.py (documentation only). -/',
           f'def cert100SeedSha256 : String := "{hashlib.sha256(seed_bytes).hexdigest()}"', '']
    out += render_literal('cert100', classes, 'The 33 classes (825 blocks) of the raw certificate, in raw order.')
    out += ['', 'end PC100.Kernel', '']
    return '\n'.join(out)


def render64(classes, cert_bytes):
    out = ['import PC100Kernel.Check', '', '/-',
           'GENERATED FILE - do not edit.  Produced by gen_lean.py from the raw control certificate',
           'information-science/evidence/six-lane-20261016/point-cyclic100/controls/v64/tz64.cert',
           f'({len(cert_bytes)} bytes, SHA-256 {hashlib.sha256(cert_bytes).hexdigest()}),',
           'first line `POINT-CYCLIC-RESOLUTION 64 4 21 16`: the published point-cyclic resolution of a',
           '2-(64,4,1) design (Topalova-Zhelezova, Axioms 15 (2026) 762, PDF pp.6-7, type T1), machine-parsed',
           'from the PDF text layer and expanded by code/control64.py of the lane (CONTROL ONLY: used by',
           'PC100Kernel.Controls100, never by a root).  `tz64` is the file verbatim in raw order: entry j of',
           'class i is the j-th line `i a b c d` of the file with class index i.',
           '-/', '', 'namespace PC100.Kernel', '',
           '/-- SHA-256 of the raw control certificate bytes, recorded by gen_lean.py (documentation only). -/',
           f'def tz64RawSha256 : String := "{hashlib.sha256(cert_bytes).hexdigest()}"', '']
    out += render_literal('tz64', classes, 'The 21 classes (336 blocks) of the v = 64 control certificate, in raw order.')
    out += ['', 'end PC100.Kernel', '']
    return '\n'.join(out)


def main(argv):
    if len(argv) != 1:
        raise SystemExit(__doc__)
    outdir = Path(argv[0])
    texts = {}
    for module, spec in SPECS.items():
        cert_bytes = (LANE / spec['cert']).read_bytes()
        if hashlib.sha256(cert_bytes).hexdigest() != spec['cert_sha256']:
            fail(f'{module}: certificate SHA-256 mismatch')
        classes = parse_cert(cert_bytes, spec['v'], spec['ncl'], spec['bpc'])
        if module == 'Data100':
            seed_bytes = (LANE / spec['seed']).read_bytes()
            if hashlib.sha256(seed_bytes).hexdigest() != spec['seed_sha256']:
                fail('seed SHA-256 mismatch')
            texts[module] = render100(classes, cert_bytes, seed_bytes)
        else:
            texts[module] = render64(classes, cert_bytes)
    outdir.mkdir(parents=True, exist_ok=True)
    for module, text in texts.items():
        if (outdir / f'{module}.lean').exists():
            fail(f'refusing to overwrite {outdir / (module + ".lean")}')
    for module, text in texts.items():
        with (outdir / f'{module}.lean').open('x') as stream:
            stream.write(text)
        print(f'wrote {outdir / (module + ".lean")} sha256 {hashlib.sha256(text.encode()).hexdigest()}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
