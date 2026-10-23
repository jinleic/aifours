#!/usr/bin/env python3
"""Bound literal audit for the table Lean package: the pinned raw certificates and seeds equal the objects the Lean
roots are about (orders 112, 136, 160, 196).

Usage: python3 -B audit_binding.py NEW_RECEIPT.json      (refuses to overwrite)

Python standard library only; no Lean, and no code imported from the lane's code/ directory. The Lean literals
`cert<v>` are read from the frozen modules PCTableKernelR2/Data<v>.lean (their SHA-256 must equal those pinned in
manifest.json when the manifest exists). The semantic objects are recomputed exactly as the Lean definitions state
them (PC100Kernel/Check.lean): pt n = n mod v; blk (a,b,c,d) = {pt a, pt b, pt c, pt d}; blocks = {blk e : e listed};
classOf c = {blk e : e in raw class c}; classes = {classOf c : c a raw class}.

Checks per order (each must hold):
  1. the raw certificate has its pinned SHA-256 and the strict layout `POINT-CYCLIC-RESOLUTION v 4 r n` followed by
     r*n lines `i a b c d` (decimal, single spaces, class indices nondecreasing, n per class, a < b < c < d < v);
  2. cert<v> equals the raw certificate exactly (same classes, same blocks, same order, same numbers), and the SHA-256
     strings recorded in the Lean module are the actual ones;
  3. the compact seed has its pinned SHA-256 and the strict PC-SEED layout, and satisfies (R1), (R2), (D) of
     GENERAL-REDUCTION.md. Its expansion R(t, K, X, Y) of Theorem C', re-implemented here and rendered in the strict
     certificate format (blocks sorted in a class, classes sorted), is byte-identical to the raw certificate;
  4. the Lean semantic objects recomputed from the literal equal the certificate's block set and class set
     (b distinct blocks, r distinct classes of n blocks);
  5. a stdlib mirror of `certCheck` (ranges, pair-code insertion, class point insertion, shift test) returns true
     (informational; the kernel evaluations are the proof).
Controls: the audit is re-run on in-memory corruptions (a certificate number changed; a block moved between classes;
a seed number changed; a number of the Lean literal changed; an extra byte appended to the certificate); each must be
rejected, by the intended check.
"""
import ast
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
LANE = HERE.parent
PINS = {
    112: ('certs/v112/pc112_t1.cert', '96265b66f4495e5927224599c941993d96bed85fb3d008b7dd53b925224a440d',
          'certs/v112/pc112_t1.seed', '9836c5030b61ad3c2bef183a4145a9029c605bdec7258e24c51e0236be22d4b1'),
    136: ('certs/v136/pc136_t3.cert', '61874100bd9333a6df83fbbecbbc807e139d985187ddcab6919ea4f815895c56',
          'certs/v136/pc136_t3.seed', '7f5057833fb25edabd3e6ad78d6dae81bed94a1a4a0aef4ef070ea484280da5b'),
    160: ('certs/v160/pc160_t3.cert', '8928dd9bd61c77da974d352f26f1980248445c5912428d943d4db3e22141a923',
          'certs/v160/pc160_t3.seed', 'd81b4af2546c7130c6288c305c6cf948c87569aa2dfd953addfb4d0374f219f7'),
    196: ('certs/v196/pc196_t2.cert', '0828bf23d3bcd8a00a544cf7b8f1ae9e3a39279bc71a98fedd229eda5c6d8db5',
          'certs/v196/pc196_t2.seed', '2709520472d8941518674a584560e26c782fce663040de2cfd6f63338ba36d26'),
}
NUM = r'(0|[1-9][0-9]*)'


class AuditError(ValueError):
    def __init__(self, check, message):
        super().__init__(f'check {check}: {message}')
        self.check = check


def require(cond, check, message):
    if not cond:
        raise AuditError(check, message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def parse_cert(raw, v):
    n, r = v // 4, (v - 1) // 3
    require(raw.endswith(b'\n') and b'\r' not in raw, 1, 'noncanonical line endings')
    lines = raw.decode('ascii').split('\n')[:-1]
    require(lines[0] == f'POINT-CYCLIC-RESOLUTION {v} 4 {r} {n}', 1, 'header')
    require(len(lines) == 1 + r * n, 1, 'line count')
    classes = [[] for _ in range(r)]
    last = -1
    for line in lines[1:]:
        require(re.fullmatch(' '.join([NUM] * 5), line) is not None, 1, f'bad line {line!r}')
        c, a, b, x, y = (int(t) for t in line.split(' '))
        require(0 <= c < r and c >= last, 1, f'class index order at {line!r}')
        last = c
        require(a < b < x < y < v, 1, f'points not ascending below v at {line!r}')
        classes[c].append((a, b, x, y))
    require(all(len(c) == n for c in classes), 1, 'blocks per class')
    return classes


def parse_literal(text, v):
    m = re.search(r'set_option maxRecDepth 16384 in\n/--[^\n]*-/\ndef cert%d : List \(List RawBlock\) := (\[.*?\n\])\n'
                  % v, text, re.S)
    require(m is not None, 2, 'literal not found')
    data = ast.literal_eval(re.sub(r'--[^\n]*', '', m.group(1)))
    require(isinstance(data, list) and all(isinstance(c, list) for c in data), 2, 'literal shape')
    require(all(isinstance(t, tuple) and len(t) == 4 and all(isinstance(x, int) for x in t) for c in data for t in c),
            2, 'literal entries are not 4-tuples of integers')
    return [[tuple(t) for t in c] for c in data]


def parse_seed(raw, v):
    require(raw.endswith(b'\n') and b'\r' not in raw, 3, 'seed line endings')
    lines = raw.decode('ascii').split('\n')[:-1]
    require(lines[0] == f'PC-SEED {v}', 3, 'seed header')
    m = re.fullmatch(r'SHORT ' + NUM, lines[1])
    require(m is not None, 3, 'SHORT line')
    t = int(m.group(1))
    n = v // 4
    require(t >= 1 and n % t == 0 and t % 4 == 1, 3, 't must divide n and be 1 mod 4')

    def blk(line, tag):
        require(re.fullmatch(tag + ' ' + ' '.join([NUM] * 4), line) is not None, 3, f'seed line {line!r}')
        pts = [int(x) for x in line.split(' ')[1:]]
        require(pts == sorted(set(pts)) and all(0 <= p < v for p in pts), 3, f'seed points {line!r}')
        return tuple(pts)
    pos = 2
    X = []
    for _ in range((t - 1) // 4):
        require(pos < len(lines), 3, 'missing X line')
        X.append(blk(lines[pos], 'X'))
        pos += 1
    groups = []
    while pos < len(lines):
        m = re.fullmatch(r'GROUP ' + NUM, lines[pos])
        require(m is not None, 3, f'expected GROUP at {lines[pos]!r}')
        k = int(m.group(1))
        require(k >= 1 and n % k == 0, 3, 'k must divide n')
        require(not groups or k <= groups[-1][0], 3, 'groups not nonincreasing')
        pos += 1
        Y = []
        for _ in range(k):
            require(pos < len(lines), 3, 'missing Y line')
            Y.append(blk(lines[pos], 'Y'))
            pos += 1
        groups.append((k, Y))
    return t, X, groups


def expand(v, t, X, groups):
    """Theorem C' of GENERAL-REDUCTION.md, independently re-implemented; returns strict certificate bytes."""
    n, r = v // 4, (v - 1) // 3
    H = {0, n, 2 * n, 3 * n}
    require(all(len({p % t for p in B}) == 4 for B in X) and sorted(p % t for B in X for p in B) == list(range(1, t)),
            3, '(R1) fails')
    for k, Y in groups:
        s = 4 * k
        require(all(len({p % s for p in B}) == 4 for B in Y) and
                sorted(p % s for B in Y for p in B) == list(range(s)), 3, '(R2) fails')
    base = X + [B for _, Y in groups for B in Y]
    diffs = sorted((a - b) % v for B in base for a in B for b in B if a != b)
    require(diffs == sorted(set(range(v)) - H), 3, '(D) fails')

    def tr(B, d):
        return tuple(sorted((p + d) % v for p in B))
    sub_t = [c for c in range(0, v, t)]
    P0 = [tuple(sorted((a + h) % v for h in H)) for a in sub_t if a < n] + [tr(B, c) for B in X for c in sub_t]
    classes = [sorted(tr(B, i) for B in P0) for i in range(t)]
    for k, Y in groups:
        s = 4 * k
        Q = [tr(B, c) for B in Y for c in range(0, v, s)]
        classes += [sorted(tr(B, i) for B in Q) for i in range(s)]
    classes.sort()
    require(len(classes) == r and all(len(P) == n for P in classes), 3, 'expansion shape')
    lines = [f'POINT-CYCLIC-RESOLUTION {v} 4 {r} {n}']
    lines += [f'{c} ' + ' '.join(map(str, B)) for c, P in enumerate(classes) for B in P]
    return ('\n'.join(lines) + '\n').encode('ascii')


def mirror_check(v, d):
    flat = [e for c in d for e in c]
    if not all(e[0] < e[1] < e[2] < e[3] < v for e in flat):
        return {'range': False}
    codes = [a * v + b for e in flat for i, a in enumerate(e) for b in e[i + 1:]]
    pairs_ok = len(codes) == len(set(codes)) and set(codes) == {p * v + q for p in range(v) for q in range(p + 1, v)}
    classes_ok = all(sorted(p for e in c for p in e) == list(range(v)) for c in d)
    plain = [frozenset(frozenset(e) for e in c) for c in d]
    shift_ok = all(frozenset(frozenset((p + 1) % v for p in e) for e in c) in plain for c in d)
    return {'range': True, 'pairs': pairs_ok, 'classes': classes_ok, 'shift': shift_ok,
            'certCheck': pairs_ok and classes_ok and shift_ok}


def audit_one(v, cert_raw, seed_raw, lean_text, pins):
    n, r = v // 4, (v - 1) // 3
    require(sha256(cert_raw) == pins[1], 1, 'certificate SHA-256 mismatch')
    cert = parse_cert(cert_raw, v)
    lit = parse_literal(lean_text, v)
    require(lit == cert, 2, f'cert{v} differs from the raw certificate')
    require(f'def cert{v}RawSha256 : String := "{sha256(cert_raw)}"' in lean_text, 2, 'recorded certificate SHA')
    require(sha256(seed_raw) == pins[3], 3, 'seed SHA-256 mismatch')
    require(f'def cert{v}SeedSha256 : String := "{sha256(seed_raw)}"' in lean_text, 3, 'recorded seed SHA')
    t, X, groups = parse_seed(seed_raw, v)
    require(expand(v, t, X, groups) == cert_raw, 3, "Theorem C' expansion of the seed differs from the certificate")
    blk = lambda e: frozenset(x % v for x in e)
    blocks = {blk(e) for c in lit for e in c}
    classes = {frozenset(blk(e) for e in c) for c in lit}
    raw_blocks = [frozenset(e) for c in cert for e in c]
    b = v * (v - 1) // 12
    require(len(raw_blocks) == b and blocks == set(raw_blocks) and len(blocks) == b, 4, 'block set')
    require(len(classes) == r and all(len(P) == n for P in classes), 4, 'class set')
    require(classes == {frozenset(frozenset(e) for e in c) for c in cert}, 4, 'class set differs')
    m = mirror_check(v, lit)
    require(m.get('certCheck') is True, 5, f'mirror checker {m}')
    return {'v': v, 't': t, 'K': [k for k, _ in groups], 'blocks': len(blocks), 'classes': len(classes),
            'expansion_byte_identical': True, 'mirror_check': m}


def audit(texts):
    out = {}
    for v, pins in PINS.items():
        cert_raw, seed_raw, lean_text = texts[v]
        out[v] = audit_one(v, cert_raw, seed_raw, lean_text, pins)
    return out


def run_controls(texts):
    results = {}
    v = 112
    cert_raw, seed_raw, lean_text = texts[v]

    def attempt(kind, cert, seed, lean, pin_override, intended):
        pins = dict(PINS)
        if pin_override:
            pins[v] = (PINS[v][0], sha256(cert), PINS[v][2], sha256(seed))
        try:
            audit_one(v, cert, seed, lean, pins[v])
            o = {'rejected': False}
        except AuditError as exc:
            o = {'rejected': True, 'check': exc.check, 'reason': str(exc)}
        o['intended_check'] = intended
        o['as_intended'] = o['rejected'] and o.get('check') == intended
        results[kind] = o

    lines = cert_raw.decode().split('\n')
    t = lines[1].split(' ')
    t[4] = str(int(t[4]) + 1)                    # one certificate number changed (still ascending, < v)
    l2 = list(lines); l2[1] = ' '.join(t)
    attempt('cert_number', '\n'.join(l2).encode(), seed_raw, lean_text, True, 2)
    l2 = list(lines)
    n = v // 4
    tt = l2[n].split(' ')                        # last block line of class 0 -> class 1
    l2[n] = ' '.join(['1'] + tt[1:])
    attempt('cert_move_block', '\n'.join(l2).encode(), seed_raw, lean_text, True, 1)
    sl = seed_raw.decode().split('\n')
    k = next(i for i, l in enumerate(sl) if l.startswith('Y '))
    st = sl[k].split(' ')
    pts = sorted(set(int(x) for x in st[1:]))
    newp = (pts[0] + 1) % v
    while newp in pts:
        newp = (newp + 1) % v
    sl2 = list(sl); sl2[k] = 'Y ' + ' '.join(map(str, sorted(pts[1:] + [newp])))
    seed2 = '\n'.join(sl2).encode()
    lean2 = lean_text.replace(sha256(seed_raw), sha256(seed2))   # keep the recorded seed SHA consistent
    attempt('seed_number', cert_raw, seed2, lean2, True, 3)
    first = re.search(r'def cert112 : List \(List RawBlock\) := \[\n  -- CLASS 0[^\n]*\n  \[\((\d+), (\d+), (\d+), (\d+)\)',
                      lean_text)
    a, b_, c, d = map(int, first.groups())
    lean3 = lean_text.replace(f'[({a}, {b_}, {c}, {d})', f'[({a}, {b_}, {c}, {d + 1})', 1)
    attempt('lean_literal', cert_raw, seed_raw, lean3, False, 2)
    attempt('sha_pin', cert_raw + b'\n', seed_raw, lean_text, False, 1)
    return results


def main(argv):
    if len(argv) != 1:
        raise SystemExit(__doc__)
    out = Path(argv[0])
    if out.exists():
        raise SystemExit('Refusing to overwrite receipt')
    texts, inputs, modules = {}, {}, {}
    for v, (crel, _, srel, _) in PINS.items():
        cert_raw, seed_raw = (LANE / crel).read_bytes(), (LANE / srel).read_bytes()
        mod = HERE / 'PCTableKernelR2' / f'Data{v}.lean'
        texts[v] = (cert_raw, seed_raw, mod.read_text())
        inputs[v] = {'cert': {'path': f'point-cyclic-table200/{crel}', 'sha256': sha256(cert_raw)},
                     'seed': {'path': f'point-cyclic-table200/{srel}', 'sha256': sha256(seed_raw)}}
        modules[f'PCTableKernelR2/Data{v}.lean'] = sha256(mod.read_bytes())
    receipt = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
               'auditor_sha256': sha256(Path(__file__).read_bytes()), 'inputs': inputs, 'lean_data_modules': modules}
    manifest = HERE / 'manifest.json'
    if manifest.exists():
        pinned = json.loads(manifest.read_text())['files']
        receipt['manifest_pins_match'] = all(pinned.get(k) == s for k, s in modules.items())
    rc = 0
    try:
        receipt['result'] = {str(k): x for k, x in audit(texts).items()}
        receipt['status'] = 'BINDING_AUDIT_PASS'
    except AuditError as exc:
        receipt['status'] = 'BINDING_AUDIT_FAIL'
        receipt['error'] = str(exc)
        rc = 1
    receipt['controls'] = run_controls(texts)
    if not all(c['as_intended'] for c in receipt['controls'].values()):
        receipt['status'] = 'BINDING_AUDIT_CONTROLS_FAIL'
        rc = 1
    if receipt.get('manifest_pins_match') is False:
        receipt['status'] = 'BINDING_AUDIT_PIN_MISMATCH'
        rc = 1
    with out.open('x') as stream:
        json.dump(receipt, stream, indent=1)
        stream.write('\n')
    print(json.dumps({'status': receipt['status'],
                      'controls': {k: [c['as_intended'], c.get('check')] for k, c in receipt['controls'].items()},
                      'orders': {k: [x['t'], x['K'], x['blocks'], x['classes']] for k, x in receipt.get('result', {}).items()}}))
    return rc


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
