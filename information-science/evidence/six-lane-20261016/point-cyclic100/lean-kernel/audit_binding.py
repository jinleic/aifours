#!/usr/bin/env python3
"""Bound literal audit: the pinned raw certificate and seed equal the objects the Lean roots are about.

Usage: python3 -B audit_binding.py NEW_RECEIPT.json      (refuses to overwrite)

Python standard library only; no Lean, and no code imported from the lane's code/ directory.  The Lean
literals `cert100` / `tz64` are read from the frozen modules PC100Kernel/Data100.lean and
PC100Kernel/Data64.lean (their SHA-256 are recorded and must equal the ones pinned in manifest.json when
that manifest exists).  The semantic objects are recomputed exactly as the Lean definitions state them
(PC100Kernel/Check.lean): pt n = n mod v; blk (a,b,c,d) = {pt a, pt b, pt c, pt d}; blocks = {blk e : e
listed}; classOf c = {blk e : e in raw class c}; classes = {classOf c : c a raw class}.

Checks (each must hold):
  1. the raw certificate has its pinned SHA-256 and the strict layout `POINT-CYCLIC-RESOLUTION 100 4 33 25`
     followed by 825 lines `i a b c d` (decimal, single spaces, class indices nondecreasing, 25 per class,
     a < b < c < d < 100); the same for the v = 64 control certificate (`... 64 4 21 16`, 336 lines);
  2. cert100 equals the raw certificate exactly (same classes, same blocks, same order, same numbers), and
     tz64 equals the control certificate; the SHA-256 strings recorded in the Lean modules are the actual
     ones;
  3. the compact seed has its pinned SHA-256, the strict layout `PC-T2-SEED 100`, `H`, 6 `X`, 2 `Y` lines,
     satisfies (S1)-(S3) of REDUCTION.md, and its expansion by Theorem C (re-implemented here:
     P0 = {H} u {X_i + h : h in <25>}, classes P0 + t (t < 25), {Y_j + 4m : m < 25} + t (t < 4)), rendered
     in the strict certificate format (blocks sorted in a class, classes sorted), is byte-identical to the
     raw certificate;
  4. the Lean semantic objects recomputed from cert100 equal the raw certificate's block set and class set:
     825 distinct blocks, 33 distinct classes of 25 blocks;
  5. a stdlib mirror of the Lean checker `certCheck` (range, pair-code insertion, class point insertion,
     shift test of the classes) returns true on cert100 and on tz64 (informational cross-check of the
     kernel evaluations, not a substitute for them).

Controls: the audit is re-run on in-memory corruptions (one certificate number changed; one block moved
between classes; one seed number changed; one number of the Lean literal changed; one number of the v = 64
control certificate changed; an extra byte appended to the certificate); each must be rejected, by the
intended check.
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
    'cert': ('certs/v100/pc100_t2.cert', '971f722460020f5a572b4f17f1cffe249488b8de079badbfa0184b9a79b4f7c1'),
    'seed': ('certs/v100/pc100_t2.seed', 'ac727835e2f15075e0697206d81482b634ed76c5f7ff000adc58bef43b256245'),
    'tz64': ('controls/v64/tz64.cert', 'd8c1173596cc60f0276c7aab77bfb2c5c162cedd682f32365b628bf11d9a4b2f'),
}
NUM = r'(0|[1-9][0-9]*)'


class AuditError(ValueError):
    def __init__(self, check, message):
        super().__init__(f'check {check}: {message}')
        self.check = check


def require(condition, check, message):
    if not condition:
        raise AuditError(check, message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def parse_cert(raw, v, ncl, bpc, check):
    require(raw.endswith(b'\n') and b'\r' not in raw, check, 'noncanonical line endings')
    lines = raw.decode('ascii').split('\n')[:-1]
    require(lines[0] == f'POINT-CYCLIC-RESOLUTION {v} 4 {ncl} {bpc}', check, 'header')
    require(len(lines) == 1 + ncl * bpc, check, 'line count')
    classes = [[] for _ in range(ncl)]
    last = -1
    for line in lines[1:]:
        require(re.fullmatch(' '.join([NUM] * 5), line) is not None, check, f'bad line {line!r}')
        c, a, b, x, y = (int(t) for t in line.split(' '))
        require(0 <= c < ncl and c >= last, check, f'class index order at {line!r}')
        last = c
        require(a < b < x < y < v, check, f'points not ascending below v at {line!r}')
        classes[c].append((a, b, x, y))
    require(all(len(c) == bpc for c in classes), check, 'blocks per class')
    return classes


def parse_lean_literal(text, name, check):
    m = re.search(r'def %s : List \(List RawBlock\) := (\[.*?\n\])\n' % name, text, re.S)
    require(m is not None, check, f'{name} literal not found')
    body = re.sub(r'--[^\n]*', '', m.group(1))
    data = ast.literal_eval(body)
    require(isinstance(data, list) and all(isinstance(c, list) for c in data), check, 'literal shape')
    require(all(isinstance(t, tuple) and len(t) == 4 and all(isinstance(x, int) for x in t)
                for c in data for t in c), check, 'literal entries are not 4-tuples of integers')
    return [[tuple(t) for t in c] for c in data]


def parse_seed(raw):
    require(raw.endswith(b'\n') and b'\r' not in raw, 3, 'seed line endings')
    lines = raw.decode('ascii').split('\n')[:-1]
    require(lines[0] == 'PC-T2-SEED 100' and len(lines) == 10, 3, 'seed header/length')
    tags = ['H'] + ['X'] * 6 + ['Y'] * 2
    blocks = []
    for line, tag in zip(lines[1:], tags):
        require(re.fullmatch(tag + ' ' + ' '.join([NUM] * 4), line) is not None, 3, f'seed line {line!r}')
        pts = [int(t) for t in line.split(' ')[1:]]
        require(pts == sorted(set(pts)) and all(0 <= p < 100 for p in pts), 3, f'seed points {line!r}')
        blocks.append(tuple(pts))
    return blocks[0], blocks[1:7], blocks[7:9]


def expand_seed(H, X, Y):
    """Theorem C of REDUCTION.md, independently re-implemented; returns the strict certificate bytes."""
    v, q = 100, 25
    Hq = (0, 25, 50, 75)
    require(sorted(H) == sorted((H[0] + h) % v for h in Hq), 3, 'H is not a coset of <25>')
    diffs = sorted((a - b) % v for B in X + Y for a in B for b in B if a != b)
    require(diffs == sorted(set(range(v)) - set(Hq)), 3, '(S1) fails')
    res = sorted([p % q for B in X for p in B] + [H[0] % q])
    require(res == list(range(q)) and all(len({p % q for p in B}) == 4 for B in X), 3, '(S2) fails')
    require(all(sorted(p % 4 for p in B) == [0, 1, 2, 3] for B in Y), 3, '(S3) fails')

    def tr(B, d):
        return tuple(sorted((p + d) % v for p in B))
    P0 = [tuple(H)] + [tr(B, h) for B in X for h in Hq]
    classes = [sorted(tr(B, t) for B in P0) for t in range(q)]
    for B in Y:
        Q = [tr(B, 4 * m) for m in range(q)]
        classes += [sorted(tr(C, t) for C in Q) for t in range(4)]
    classes.sort()
    lines = [f'POINT-CYCLIC-RESOLUTION {v} 4 {len(classes)} {q}']
    lines += [f'{c} ' + ' '.join(map(str, B)) for c, P in enumerate(classes) for B in P]
    return ('\n'.join(lines) + '\n').encode('ascii')


def mirror_check(v, d):
    """Stdlib mirror of PC100Kernel.Check.certCheck (informational)."""
    flat = [e for c in d for e in c]
    if not all(e[0] < e[1] < e[2] < e[3] < v for e in flat):
        return {'range': False}
    codes = [a * v + b for e in flat for i, a in enumerate(e) for b in e[i + 1:]]
    pairs_ok = len(codes) == len(set(codes)) and set(codes) == {p * v + q for p in range(v) for q in range(p + 1, v)}
    classes_ok = all(sorted(p for e in c for p in e) == list(range(v)) for c in d)
    code = lambda pts: frozenset(pts)
    shifted = lambda c: frozenset(code(((p + 1) % v for p in e)) for e in c)
    plain = [frozenset(code(e) for e in c) for c in d]
    shift_ok = all(shifted(c) in plain for c in d)
    return {'range': True, 'pairs': pairs_ok, 'classes': classes_ok, 'shift': shift_ok,
            'certCheck': pairs_ok and classes_ok and shift_ok}


def audit(cert_raw, seed_raw, tz_raw, lean100, lean64):
    require(sha256(cert_raw) == PINS['cert'][1], 1, 'certificate SHA-256 mismatch')
    require(sha256(tz_raw) == PINS['tz64'][1], 1, 'v = 64 control certificate SHA-256 mismatch')
    cert = parse_cert(cert_raw, 100, 33, 25, 1)
    tz = parse_cert(tz_raw, 64, 21, 16, 1)
    # 2. literal binding
    lit = parse_lean_literal(lean100, 'cert100', 2)
    require(lit == cert, 2, 'cert100 differs from the raw certificate')
    lit64 = parse_lean_literal(lean64, 'tz64', 2)
    require(lit64 == tz, 2, 'tz64 differs from the control certificate')
    require(f'def cert100RawSha256 : String := "{sha256(cert_raw)}"' in lean100, 2, 'recorded cert SHA')
    require(f'def tz64RawSha256 : String := "{sha256(tz_raw)}"' in lean64, 2, 'recorded tz64 SHA')
    # 3. seed binding
    require(sha256(seed_raw) == PINS['seed'][1], 3, 'seed SHA-256 mismatch')
    require(f'def cert100SeedSha256 : String := "{sha256(seed_raw)}"' in lean100, 3, 'recorded seed SHA')
    H, X, Y = parse_seed(seed_raw)
    require(expand_seed(H, X, Y) == cert_raw, 3, 'Theorem C expansion of the seed differs from the certificate')
    # 4. semantic objects as the Lean definitions state them
    pt = lambda n: n % 100
    blk = lambda e: frozenset(pt(n) for n in e)
    blocks = {blk(e) for c in lit for e in c}
    classes = {frozenset(blk(e) for e in c) for c in lit}
    raw_blocks = [frozenset(e) for c in cert for e in c]
    require(len(blocks) == 825 and blocks == set(raw_blocks) and len(raw_blocks) == 825, 4, 'block set')
    require(len(classes) == 33 and all(len(P) == 25 for P in classes), 4, 'class set')
    require(classes == {frozenset(frozenset(e) for e in c) for c in cert}, 4, 'class set differs')
    # 5. mirror of the checker (informational, must agree with the kernel evaluations)
    m100, m64 = mirror_check(100, lit), mirror_check(64, lit64)
    require(m100.get('certCheck') is True and m64.get('certCheck') is True, 5, f'mirror checker {m100} {m64}')
    return {'cert_blocks': len(raw_blocks), 'distinct_blocks': len(blocks), 'classes': len(classes),
            'blocks_per_class': sorted({len(P) for P in classes}), 'seed': {'H': H, 'X': X, 'Y': Y},
            'mirror_check_100': m100, 'mirror_check_64': m64,
            'expansion_byte_identical': True}


def corrupt(kind, cert_raw, seed_raw, tz_raw, lean100, lean64):
    cert, seed, tz, l100, l64 = cert_raw, seed_raw, tz_raw, lean100, lean64
    if kind == 'cert_number':
        lines = cert.decode().split('\n')
        t = lines[1].split(' ')   # "0 0 1 12 92" -> "0 0 1 12 93"
        t[4] = str(int(t[4]) + 1)
        lines[1] = ' '.join(t)
        cert, intended = '\n'.join(lines).encode(), 2
    elif kind == 'cert_move_block':
        lines = cert.decode().split('\n')
        t = lines[25].split(' ')   # last block line of class 0 -> class 1 (order stays nondecreasing)
        lines[25] = ' '.join(['1'] + t[1:])
        cert, intended = '\n'.join(lines).encode(), 1
    elif kind == 'seed_number':
        lines = seed.decode().split('\n')
        t = lines[2].split(' ')
        t[1] = str(int(t[1]) + 1)
        lines[2] = ' '.join(t)
        seed, intended = '\n'.join(lines).encode(), 3
        # keep the Lean module's recorded seed SHA consistent, so that the expansion test is what rejects
        l100 = lean100.replace(sha256(seed_raw), sha256(seed))
    elif kind == 'lean_literal':
        l100, intended = lean100.replace('(0, 1, 12, 92)', '(0, 1, 12, 93)', 1), 2
    elif kind == 'tz64_number':
        lines = tz.decode().split('\n')
        t = lines[1].split(' ')
        t[4] = str(int(t[4]) + 1)   # "0 0 1 3 7" -> "0 0 1 3 8": still ascending and below 64
        lines[1] = ' '.join(t)
        tz, intended = '\n'.join(lines).encode(), 2
    elif kind == 'sha_pin':
        cert, intended = cert_raw + b'\n', 1
    else:
        raise ValueError(kind)
    return cert, seed, tz, l100, l64, intended


def run_controls(cert_raw, seed_raw, tz_raw, lean100, lean64):
    results = {}
    for kind in ['cert_number', 'cert_move_block', 'seed_number', 'lean_literal', 'tz64_number', 'sha_pin']:
        cert, seed, tz, l100, l64, intended = corrupt(kind, cert_raw, seed_raw, tz_raw, lean100, lean64)
        saved = dict(PINS)
        if kind != 'sha_pin':   # the SHA pins are checks 1 and 3; test the later checks on corrupted bytes
            PINS['cert'] = (PINS['cert'][0], sha256(cert))
            PINS['tz64'] = (PINS['tz64'][0], sha256(tz))
            PINS['seed'] = (PINS['seed'][0], sha256(seed))
        try:
            audit(cert, seed, tz, l100, l64)
            outcome = {'rejected': False}
        except AuditError as exc:
            outcome = {'rejected': True, 'check': exc.check, 'reason': str(exc)}
        finally:
            PINS.update(saved)
        outcome['intended_check'] = intended
        outcome['as_intended'] = outcome['rejected'] and outcome.get('check') == intended
        results[kind] = outcome
    return results


def main(argv):
    if len(argv) != 1:
        raise SystemExit(__doc__)
    out = Path(argv[0])
    if out.exists():
        raise SystemExit('Refusing to overwrite receipt')
    cert_raw = (LANE / PINS['cert'][0]).read_bytes()
    seed_raw = (LANE / PINS['seed'][0]).read_bytes()
    tz_raw = (LANE / PINS['tz64'][0]).read_bytes()
    p100, p64 = HERE / 'PC100Kernel' / 'Data100.lean', HERE / 'PC100Kernel' / 'Data64.lean'
    lean100, lean64 = p100.read_text(), p64.read_text()
    receipt = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
               'auditor_sha256': sha256(Path(__file__).read_bytes()),
               'inputs': {k: {'path': f'point-cyclic100/{p}', 'sha256': sha256((LANE / p).read_bytes())}
                          for k, (p, _) in PINS.items()},
               'lean_data_modules': {'PC100Kernel/Data100.lean': sha256(p100.read_bytes()),
                                     'PC100Kernel/Data64.lean': sha256(p64.read_bytes())}}
    manifest = HERE / 'manifest.json'
    if manifest.exists():
        pinned = json.loads(manifest.read_text())['files']
        receipt['manifest_pins_match'] = all(pinned.get(k) == v for k, v in receipt['lean_data_modules'].items())
    rc = 0
    try:
        receipt['result'] = audit(cert_raw, seed_raw, tz_raw, lean100, lean64)
        receipt['status'] = 'BINDING_AUDIT_PASS'
    except AuditError as exc:
        receipt['status'] = 'BINDING_AUDIT_FAIL'
        receipt['error'] = str(exc)
        rc = 1
    receipt['controls'] = run_controls(cert_raw, seed_raw, tz_raw, lean100, lean64)
    if not all(c['as_intended'] for c in receipt['controls'].values()):
        receipt['status'] = 'BINDING_AUDIT_CONTROLS_FAIL'
        rc = 1
    if receipt.get('manifest_pins_match') is False:
        receipt['status'] = 'BINDING_AUDIT_PIN_MISMATCH'
        rc = 1
    with out.open('x') as stream:
        json.dump(receipt, stream, indent=1)
        stream.write('\n')
    summary = {'status': receipt['status'],
               'controls': {k: (c['as_intended'], c.get('check')) for k, c in receipt['controls'].items()}}
    if 'result' in receipt:
        r = receipt['result']
        summary['counts'] = [r['cert_blocks'], r['distinct_blocks'], r['classes'], r['blocks_per_class']]
    print(json.dumps(summary))
    return rc


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
