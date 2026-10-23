#!/usr/bin/env python3
"""Generate PCTableKernelR2/Data<v>.lean for every pinned table certificate (stdlib only).

Usage: python3 -B gen_lean.py OUTDIR [V ...]   (writes OUTDIR/Data<v>.lean for the given orders, default every entry of
                                              PINS; refuses to overwrite)

Each `cert<v>` literal is the pinned certificate copied verbatim in raw order. Class i of the literal is the list of the
lines `i a b c d` (in file order), each as the raw block (a, b, c, d). No number is changed, sorted or reduced here;
the Lean checker `PC100.Kernel.certCheck` (byte copy of the accepted v = 100 module `PC100Kernel/Check.lean`) tests the
ranges itself. The compact seeds are recorded in the header only and are not used by any Lean proof.
"""
import hashlib
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
LANE = HERE.parent
NUM = r'(0|[1-9][0-9]*)'
PER_LINE = 5
# v: (certificate, SHA-256, seed, SHA-256, type description)
PINS = {
    112: ('certs/v112/pc112_t1.cert', '96265b66f4495e5927224599c941993d96bed85fb3d008b7dd53b925224a440d',
          'certs/v112/pc112_t1.seed', '9836c5030b61ad3c2bef183a4145a9029c605bdec7258e24c51e0236be22d4b1',
          'type T1, K = {7,1,1}'),
    136: ('certs/v136/pc136_t3.cert', '61874100bd9333a6df83fbbecbbc807e139d985187ddcab6919ea4f815895c56',
          'certs/v136/pc136_t3.seed', '7f5057833fb25edabd3e6ad78d6dae81bed94a1a4a0aef4ef070ea484280da5b',
          'type T3, t = 17, K = {1^7}'),
    160: ('certs/v160/pc160_t3.cert', '8928dd9bd61c77da974d352f26f1980248445c5912428d943d4db3e22141a923',
          'certs/v160/pc160_t3.seed', 'd81b4af2546c7130c6288c305c6cf948c87569aa2dfd953addfb4d0374f219f7',
          'type T3, t = 5, K = {10,2}'),
    196: ('certs/v196/pc196_t2.cert', '0828bf23d3bcd8a00a544cf7b8f1ae9e3a39279bc71a98fedd229eda5c6d8db5',
          'certs/v196/pc196_t2.seed', '2709520472d8941518674a584560e26c782fce663040de2cfd6f63338ba36d26',
          'type T2, t = 49, K = {1,1,1,1}'),
}


def fail(msg):
    raise SystemExit(f'gen_lean.py: {msg}')


def parse_cert(raw, v):
    n, r = v // 4, (v - 1) // 3
    if not raw.endswith(b'\n') or b'\r' in raw:
        fail(f'{v}: noncanonical line endings')
    lines = raw.decode('ascii').split('\n')[:-1]
    if lines[0] != f'POINT-CYCLIC-RESOLUTION {v} 4 {r} {n}':
        fail(f'{v}: header {lines[0]!r}')
    classes = [[] for _ in range(r)]
    for ln, line in enumerate(lines[1:], start=2):
        if not re.fullmatch(' '.join([NUM] * 5), line):
            fail(f'{v}: line {ln}: {line!r}')
        c, a, b, x, y = (int(t) for t in line.split(' '))
        if not 0 <= c < r:
            fail(f'{v}: line {ln}: class index')
        classes[c].append(((a, b, x, y), ln))
    if len(lines) != 1 + r * n or any(len(c) != n for c in classes):
        fail(f'{v}: shape')
    index = [int(line.split(' ')[0]) for line in lines[1:]]
    if index != sorted(index):
        fail(f'{v}: class indices not in nondecreasing file order')
    return classes


def render(v, classes, cert_rel, cert_bytes, seed_rel, seed_bytes, desc):
    n, r = v // 4, (v - 1) // 3
    out = ['import PC100Kernel.Check', '', '/-',
           'GENERATED FILE - do not edit.  Produced by lean-kernel/gen_lean.py from the raw certificate',
           f'information-science/evidence/six-lane-20261016/point-cyclic-table200/{cert_rel}',
           f'({len(cert_bytes)} bytes, SHA-256 {hashlib.sha256(cert_bytes).hexdigest()}),',
           f'first line `POINT-CYCLIC-RESOLUTION {v} 4 {r} {n}` ({desc}).',
           f'`cert{v}` is the certificate copied verbatim in raw order: entry j of class i is the j-th line `i a b c d`',
           f'of the file with class index i, as the raw block (a, b, c, d). The certificate was expanded by',
           f'code/pc_expand_general.py from the compact seed {seed_rel}',
           f'({len(seed_bytes)} bytes, SHA-256 {hashlib.sha256(seed_bytes).hexdigest()}); the seed is not used by any',
           'Lean proof. Nothing is assumed about these numbers here: PC100Kernel.Check states the checker and its',
           f'soundness theorem, and PCTableKernelR2.Cert{v} runs the checker in the Lean kernel.',
           'The elaborator recursion limit is raised (`set_option maxRecDepth 16384 in`) for the one large literal',
           'below; it is an elaboration resource limit, not a proof setting.',
           '-/', '', 'namespace PC100.Kernel', '',
           '/-- SHA-256 of the raw certificate bytes, recorded by gen_lean.py (documentation only). -/',
           f'def cert{v}RawSha256 : String := "{hashlib.sha256(cert_bytes).hexdigest()}"', '',
           '/-- SHA-256 of the compact seed bytes, recorded by gen_lean.py (documentation only). -/',
           f'def cert{v}SeedSha256 : String := "{hashlib.sha256(seed_bytes).hexdigest()}"', '',
           'set_option maxRecDepth 16384 in',
           f'/-- The {r} classes ({r * n} blocks) of the raw certificate, in raw order. -/',
           f'def cert{v} : List (List RawBlock) := [']
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
    out += [']', '', 'end PC100.Kernel', '']
    return '\n'.join(out)


def main(argv):
    if len(argv) < 1:
        raise SystemExit(__doc__)
    outdir = Path(argv[0])
    orders = [int(x) for x in argv[1:]] or list(PINS)
    texts = {}
    for v in orders:
        cert_rel, cert_sha, seed_rel, seed_sha, desc = PINS[v]
        cert_bytes, seed_bytes = (LANE / cert_rel).read_bytes(), (LANE / seed_rel).read_bytes()
        if hashlib.sha256(cert_bytes).hexdigest() != cert_sha:
            fail(f'{v}: certificate SHA-256 mismatch')
        if hashlib.sha256(seed_bytes).hexdigest() != seed_sha:
            fail(f'{v}: seed SHA-256 mismatch')
        texts[v] = render(v, parse_cert(cert_bytes, v), cert_rel, cert_bytes, seed_rel, seed_bytes, desc)
    outdir.mkdir(parents=True, exist_ok=True)
    for v in texts:
        if (outdir / f'Data{v}.lean').exists():
            fail(f'refusing to overwrite {outdir / f"Data{v}.lean"}')
    for v, text in texts.items():
        with (outdir / f'Data{v}.lean').open('x') as stream:
            stream.write(text)
        print(f'wrote {outdir / f"Data{v}.lean"} sha256 {hashlib.sha256(text.encode()).hexdigest()}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
