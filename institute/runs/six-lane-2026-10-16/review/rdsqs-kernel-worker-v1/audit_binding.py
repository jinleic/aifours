#!/usr/bin/env python3
"""Bound literal audit: the raw RDSQS certificate equals the objects the Lean roots are about.

Usage: python3 -B audit_binding.py V NEW_RECEIPT.json      (V in {52, 76}; refuses to overwrite)

Python standard library only; no Lean.  The Lean literal `data{V}` / `mults{V}` is read from the
frozen module RdsqsKernel/Data{V}.lean (its SHA-256 is recorded and must equal the one pinned in
manifest.json when that manifest exists).  The semantic objects are recomputed exactly as the
Lean definitions state them (RdsqsKernel/Check.lean, RdsqsKernel/Generic.lean):

  pt n          = n mod V
  tri (a,b,c)   = {pt a, pt b, pt c}
  seedTriples   = {tri e : e a listed triple}
  seedClasses   = {{tri e : e in raw class i} : i}
  blocks        = {({0} ∪ t) + a : t in seedTriples, a in Z_V}          (Generic.blocksOf)
  resAt m x     = {{{m*y + x : y in T} : T in P} : P in seedClasses}

Checks (each must hold):
  1. the raw certificate has its pinned SHA-256, the strict layout `RDSQS V`, `BLOCKS`, exactly
     V(V-1)(V-2)/24 block lines, then `POINT x` for x = 0..V-1 in order, each with
     `CLASS 0..(V-2)/2-1` of (V-1)/3 triple lines; every line has distinct points below V;
  2. data{V} equals the raw `POINT 0` section exactly (same classes, same triples, same order,
     same numbers); the compact seed's classes_at_0 equal it too; mults{V} are the powers of the
     seed's multiplier generator, each with an inverse modulo V;
  3. the raw block lines are pairwise distinct and their set equals `blocks`;
  4. for every point x, the raw `POINT x` section, as a set of classes of triples, equals
     `resAt m x` for some listed multiplier m; class j of the raw section equals the image of
     class j of data{V} under that map (class order preserved); and m is the multiplier given by
     the seed's stated rule (least element g of G with g(0) = x, as a tuple of images).

Controls: the same audit is run on four in-memory corruptions of the raw text (one block line,
one POINT 0 triple, two points swapped between two triples of one class of POINT 7, and the
POINT 7 section replaced by the POINT 0 section); each must be rejected, by the intended check.
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
REVIEW = HERE.parent
INPUTS = {
    52: {'raw': 'rdsqs52-parent-inputs-v1/rdsqs52_z52_m23.txt',
         'raw_sha256': '7ae0a828b5af08b4bd9b423564981d85e3703886553638024fdc812f564989a6',
         'seed': 'rdsqs52-parent-replay-v1/rdsqs52_z52_m23_seed.json',
         'seed_sha256': 'a0fe9247f93d1f16007eff24b65c3dddf0f409c33f847f8a7382399b09dcefce'},
    76: {'raw': 'rdsqs76-parent-inputs-v1/rdsqs76_z76_m3_sample0.txt',
         'raw_sha256': '2f75b37c0439aa9f9c57861505a2e865997dd02249349b708880916d477a75aa',
         'seed': 'rdsqs76-parent-inputs-v1/rdsqs76_z76_m3_sample0_seed.json',
         'seed_sha256': '8d5860f640d1d49163496f996aad97af1e4674855cc2a1c6883327cb272ba0ad'},
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


def parse_lean_literal(text, v):
    """Return (data, mults) from the generated Data{v}.lean text."""
    m = re.search(r'def data%d : List \(List RawTriple\) := (\[.*?\n\])\n' % v, text, re.S)
    require(m is not None, 2, 'data literal not found')
    body = re.sub(r'--[^\n]*', '', m.group(1))
    data = ast.literal_eval(body)
    m2 = re.search(r'def mults%d : List \(ℕ × ℕ\) := (\[[^\n]*\])\n' % v, text)
    require(m2 is not None, 2, 'mults literal not found')
    mults = ast.literal_eval(m2.group(1))
    require(isinstance(data, list) and all(isinstance(c, list) for c in data), 2, 'data shape')
    require(all(isinstance(t, tuple) and len(t) == 3 and all(isinstance(x, int) for x in t)
                for c in data for t in c), 2, 'data entries are not triples of integers')
    return [[tuple(t) for t in c] for c in data], [tuple(p) for p in mults]


def parse_points(line, size, v, check):
    require(re.fullmatch(' '.join([NUM] * size), line) is not None, check, f'bad line {line!r}')
    pts = tuple(int(x) for x in line.split(' '))
    require(all(0 <= p < v for p in pts) and len(set(pts)) == size, check, f'bad points {line!r}')
    return pts


def parse_raw(text, v):
    require(text.endswith('\n') and '\r' not in text, 1, 'noncanonical line endings')
    lines = [l for l in text.split('\n')[:-1] if not l.startswith('#')]
    require(lines[:2] == [f'RDSQS {v}', 'BLOCKS'], 1, 'header')
    nblocks = v * (v - 1) * (v - 2) // 24
    blocks = [parse_points(l, 4, v, 1) for l in lines[2:2 + nblocks]]
    require(len(blocks) == nblocks, 1, 'truncated block list')
    rest = lines[2 + nblocks:]
    ncls, per = (v - 2) // 2, (v - 1) // 3
    points, pos = [], 0
    for x in range(v):
        require(pos < len(rest) and rest[pos] == f'POINT {x}', 1, f'POINT {x} header')
        pos += 1
        classes = []
        for j in range(ncls):
            require(pos < len(rest) and rest[pos] == f'CLASS {j}', 1, f'CLASS {j} header at {x}')
            pos += 1
            require(pos + per <= len(rest), 1, 'truncated class')
            classes.append([parse_points(l, 3, v, 1) for l in rest[pos:pos + per]])
            pos += per
        points.append(classes)
    require(pos == len(rest), 1, 'trailing lines')
    return blocks, points


def subgroup(gen, v):
    elements = [1]
    while (elements[-1] * gen) % v != 1:
        elements.append(elements[-1] * gen % v)
        require(len(elements) <= v, 2, 'generator is not a unit')
    return elements


def rule_multiplier(mults, x, v):
    """Seed rule: the least g in G = {y -> m*y + b} with g(0) = x, ordered as the tuple of images."""
    return min(mults, key=lambda m: tuple((m * y + x) % v for y in range(v)))


def audit(v, raw_bytes, seed_bytes, lean_text):
    spec = INPUTS[v]
    require(sha256(raw_bytes) == spec['raw_sha256'], 1, 'raw SHA-256 mismatch')
    require(sha256(seed_bytes) == spec['seed_sha256'], 2, 'seed SHA-256 mismatch')
    raw_blocks, raw_points = parse_raw(raw_bytes.decode('ascii'), v)
    data, mults = parse_lean_literal(lean_text, v)
    # 2. literal binding
    require(data == raw_points[0], 2, 'data literal differs from the raw POINT 0 section')
    seed = json.loads(seed_bytes)
    require(seed['v'] == v and [[tuple(t) for t in c] for c in seed['classes_at_0']] == data, 2,
            'seed classes_at_0 differ from the data literal')
    sub = subgroup(seed['multiplier_generator'], v)
    require([m for m, _ in mults] == sub, 2, 'mults are not the powers of the seed generator')
    require(all(m * mi % v == 1 for m, mi in mults), 2, 'a listed multiplier has a wrong inverse')
    # semantics, as in the Lean definitions
    pt = lambda n: n % v
    tri = lambda e: frozenset(pt(n) for n in e)
    seed_triples = {tri(e) for c in data for e in c}
    seed_classes = [frozenset(tri(e) for e in c) for c in data]
    gen_blocks = {frozenset((y + a) % v for y in ({0} | t)) for t in seed_triples for a in range(v)}
    # 3. blocks
    raw_block_sets = [frozenset(b) for b in raw_blocks]
    require(len(set(raw_block_sets)) == len(raw_block_sets), 3, 'duplicate raw block')
    require(set(raw_block_sets) == gen_blocks, 3, 'raw block set differs from the generated blocks')
    # 4. resolutions
    per_point = []
    for x in range(v):
        raw_classes = [frozenset(frozenset(t) for t in c) for c in raw_points[x]]
        raw_res = frozenset(raw_classes)
        matching = []
        for m, _ in mults:
            img = lambda P: frozenset(frozenset((m * y + x) % v for y in T) for T in P)
            if frozenset(img(P) for P in seed_classes) == raw_res:
                matching.append(m)
        require(matching, 4, f'POINT {x} equals resAt m {x} for no listed m')
        expected = rule_multiplier([m for m, _ in mults], x, v)
        require(expected in matching, 4, f'POINT {x}: the rule multiplier {expected} does not match')
        img = lambda P: frozenset(frozenset((expected * y + x) % v for y in T) for T in P)
        require(all(raw_classes[j] == img(seed_classes[j]) for j in range(len(seed_classes))), 4,
                f'POINT {x}: class order differs from the image of the POINT 0 class order')
        per_point.append({'x': x, 'matching_multipliers': matching, 'rule_multiplier': expected})
    return {
        'raw_blocks': len(raw_blocks), 'generated_blocks': len(gen_blocks),
        'seed_triples': len(seed_triples), 'seed_classes': len(seed_classes),
        'classes_per_point': len(raw_points[0]), 'triples_per_class': len(raw_points[0][0]),
        'points': v, 'mults': mults, 'per_point': per_point,
    }


def corrupt(v, text, kind):
    lines = text.split('\n')
    if kind == 'block_line':
        i = lines.index('BLOCKS') + 1
        a, b, c, d = map(int, lines[i].split(' '))
        lines[i] = ' '.join(map(str, sorted({a, b, c, (d + 1) % v if (d + 1) % v not in (a, b, c) else (d + 2) % v})))
        return '\n'.join(lines), 3
    if kind == 'point0_triple':
        i = lines.index('POINT 0') + 2
        lines[i], lines[i + 1] = lines[i + 1], lines[i]
        return '\n'.join(lines), 2
    if kind == 'point7_swap':
        i = lines.index('POINT 7') + 2
        t1, t2 = lines[i].split(' '), lines[i + 1].split(' ')
        t1[0], t2[0] = t2[0], t1[0]
        lines[i] = ' '.join(map(str, sorted(map(int, t1))))
        lines[i + 1] = ' '.join(map(str, sorted(map(int, t2))))
        return '\n'.join(lines), 4
    if kind == 'point7_copy0':
        i0, i1 = lines.index('POINT 0'), lines.index('POINT 1')
        i7, i8 = lines.index('POINT 7'), lines.index('POINT 8')
        lines[i7 + 1:i8] = lines[i0 + 1:i1]
        return '\n'.join(lines), 4
    raise ValueError(kind)


def run_controls(v, raw_bytes, seed_bytes, lean_text):
    results = {}
    text = raw_bytes.decode('ascii')
    for kind in ['block_line', 'point0_triple', 'point7_swap', 'point7_copy0']:
        bad_text, intended = corrupt(v, text, kind)
        bad = bad_text.encode('ascii')
        spec = dict(INPUTS[v])
        INPUTS[v]['raw_sha256'] = sha256(bad)   # the SHA pin is check 1; test the later checks
        try:
            audit(v, bad, seed_bytes, lean_text)
            outcome = {'rejected': False}
        except AuditError as exc:
            outcome = {'rejected': True, 'check': exc.check, 'reason': str(exc)}
        finally:
            INPUTS[v].update(spec)
        outcome['intended_check'] = intended
        outcome['as_intended'] = outcome['rejected'] and outcome.get('check') == intended
        outcome['corrupted_sha256'] = sha256(bad)
        results[kind] = outcome
    # the SHA pin itself
    try:
        audit(v, raw_bytes + b'\n', seed_bytes, lean_text)
        results['sha_pin'] = {'rejected': False, 'as_intended': False}
    except AuditError as exc:
        results['sha_pin'] = {'rejected': True, 'check': exc.check, 'reason': str(exc),
                              'as_intended': exc.check == 1}
    return results


def main(argv):
    if len(argv) != 2:
        raise SystemExit(__doc__)
    v, out = int(argv[0]), Path(argv[1])
    if out.exists():
        raise SystemExit('Refusing to overwrite receipt')
    spec = INPUTS[v]
    raw_bytes = (REVIEW / spec['raw']).read_bytes()
    seed_bytes = (REVIEW / spec['seed']).read_bytes()
    lean_path = HERE / 'RdsqsKernel' / f'Data{v}.lean'
    lean_bytes = lean_path.read_bytes()
    receipt = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
               'auditor_sha256': sha256(Path(__file__).read_bytes()), 'v': v,
               'raw': {'path': f"review/{spec['raw']}", 'sha256': sha256(raw_bytes)},
               'seed': {'path': f"review/{spec['seed']}", 'sha256': sha256(seed_bytes)},
               'lean_data_module': {'path': f'RdsqsKernel/Data{v}.lean', 'sha256': sha256(lean_bytes)}}
    manifest = HERE / 'manifest.json'
    if manifest.exists():
        pinned = json.loads(manifest.read_text())['files'].get(f'RdsqsKernel/Data{v}.lean')
        receipt['lean_data_module']['manifest_pin_matches'] = pinned == sha256(lean_bytes)
    rc = 0
    try:
        receipt['result'] = audit(v, raw_bytes, seed_bytes, lean_bytes.decode('utf-8'))
        receipt['status'] = 'BINDING_AUDIT_PASS'
    except AuditError as exc:
        receipt['status'] = 'BINDING_AUDIT_FAIL'
        receipt['error'] = str(exc)
        rc = 1
    receipt['controls'] = run_controls(v, raw_bytes, seed_bytes, lean_bytes.decode('utf-8'))
    if not all(c['as_intended'] for c in receipt['controls'].values()):
        receipt['status'] = 'BINDING_AUDIT_CONTROLS_FAIL'
        rc = 1
    if receipt['lean_data_module'].get('manifest_pin_matches') is False:
        receipt['status'] = 'BINDING_AUDIT_PIN_MISMATCH'
        rc = 1
    with out.open('x') as stream:
        json.dump(receipt, stream, indent=1)
        stream.write('\n')
    summary = {k: receipt[k] for k in ['status', 'v']}
    summary['controls'] = {k: c['as_intended'] for k, c in receipt['controls'].items()}
    if 'result' in receipt:
        r = receipt['result']
        summary['counts'] = [r['raw_blocks'], r['generated_blocks'], r['seed_triples'], r['seed_classes']]
        summary['rule_multipliers'] = sorted({p['rule_multiplier'] for p in r['per_point']})
    print(json.dumps(summary))
    return rc


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
