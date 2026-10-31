#!/usr/bin/env python3
"""Parent direct-box replay of the f159 residual, written from its definitions.

No author/reviewer imports. Each leaf is recomputed by direct affine substitution
into a compactified polynomial, NOT by the supplied de Casteljau replay. Includes
strict prefix-tree coverage and intended-reason mutations. Modest stdlib-only run.
The already parent-replayed girth-four Q/H certificate is not rerun here.
"""
import hashlib
import itertools
import json
import math
import pathlib
import subprocess
import sys
import time
from collections import Counter
from fractions import Fraction as F

ROOT = pathlib.Path(__file__).resolve().parent
EXPECTED = '45256245ecda8aed8ec18150c642fd70c3665cd9af31c49dc59fb25e367ed6be'
START = time.monotonic()
DEADLINE = START + 120

class CheckError(Exception):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(reason)

def require(ok, why):
    if not ok:
        raise CheckError(why)

def guard():
    require(time.monotonic() < DEADLINE, 'TIME_LIMIT_UNKNOWN')

def sha(b):
    return hashlib.sha256(b).hexdigest()

def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

def plus(*polys):
    out = {}
    for poly in polys:
        for key, val in poly.items():
            out[key] = out.get(key, F(0)) + val
    return {key: val for key, val in out.items() if val}

def times(left, right):
    out = {}
    for a, u in left.items():
        for b, v in right.items():
            key = tuple(x+y for x, y in zip(a, b))
            out[key] = out.get(key, F(0)) + u*v
    return {key: val for key, val in out.items() if val}

def scaled(poly, factor):
    return {key: val*factor for key, val in poly.items() if val*factor}

def constant(value):
    return {(0, 0, 0): F(value)} if value else {}

def variable(axis):
    key = [0, 0, 0]
    key[axis] = 1
    return {tuple(key): F(1)}

def degree(poly):
    return tuple(max(key[i] for key in poly) for i in range(3))

def canon_hash(poly):
    require(all(value.denominator == 1 for value in poly.values()), 'NONINTEGER_POLYNOMIAL')
    obj = [[list(key), str(int(value))] for key, value in sorted(poly.items())]
    return sha(json.dumps(obj, separators=(',', ':')).encode())

def defining_polynomials():
    y, tau, gam = (variable(i) for i in range(3))
    y2 = times(y, y)
    a2 = scaled(times(tau, y2), F(3, 8))
    beta = plus(scaled(y, F(1, 2)), gam)
    abase = plus(a2, scaled(y, -4), constant(F(74, 9)))
    pa = scaled(plus(abase, times(beta, plus(y, constant(-4))), scaled(times(beta, beta), F(1, 4))), 144)
    dbase = plus(scaled(y2, 4), scaled(y, -16), constant(F(212, 9)), scaled(times(y, a2), F(-5, 6)))
    k2 = plus(a2, scaled(y2, -1), scaled(y, 4), constant(F(-70, 9)))
    pd = scaled(plus(dbase, times(beta, k2)), 144)
    pf = scaled(plus(y, beta, constant(-4)), 2)
    return {'Abar': pa, 'Dbar': pd, 'f1minus4': pf}

def compactify(poly):
    """Expand y=s/(1-s), gamma=g/(1-g), clearing positive denominators."""
    dy, dt, dg = degree(poly)
    out = {}
    for (iy, it, ig), value in poly.items():
        for jy in range(dy-iy+1):
            for jg in range(dg-ig+1):
                key = (iy+jy, it, ig+jg)
                coefficient = value * math.comb(dy-iy, jy) * math.comb(dg-ig, jg) * (-1)**(jy+jg)
                out[key] = out.get(key, F(0)) + coefficient
    return {key: val for key, val in out.items() if val}, (dy, dt, dg)

def box_coefficients(poly, degrees, box):
    """Directly substitute a dyadic box, then convert monomials to Bernstein."""
    work = dict(poly)
    for axis in range(3):
        lo, hi = box[axis]
        width = hi-lo
        out = {}
        for key, value in work.items():
            power = key[axis]
            for j in range(power+1):
                changed = list(key)
                changed[axis] = j
                changed = tuple(changed)
                term = value * math.comb(power, j) * lo**(power-j) * width**j
                out[changed] = out.get(changed, F(0)) + term
        work = {key: val for key, val in out.items() if val}
    for axis, d in enumerate(degrees):
        out = {}
        for key, value in work.items():
            power = key[axis]
            for j in range(power, d+1):
                changed = list(key)
                changed[axis] = j
                changed = tuple(changed)
                term = value * F(math.comb(j, power), math.comb(d, power))
                out[changed] = out.get(changed, F(0)) + term
        work = {key: val for key, val in out.items() if val}
    return {key: work.get(key, F(0)) for key in itertools.product(*(range(d+1) for d in degrees))}

def strict_tree(leaves):
    require(isinstance(leaves, list) and leaves, 'BAD_LEAF_LIST')
    trie = {}
    for row in leaves:
        require(isinstance(row, list) and len(row) == 2, 'BAD_LEAF_ROW')
        path, label = row
        require(isinstance(path, str) and len(path) <= 100 and set(path) <= {'0', '1'}, 'BAD_PATH')
        require(label in {'Abar<=0', 'Dbar<=0', 'f1-4<0'}, 'UNKNOWN_SELECTOR')
        node = trie
        for bit in path:
            require('$' not in node, 'PREFIX_COLLISION')
            node = node.setdefault(bit, {})
        require('$' not in node, 'DUPLICATE_LEAF')
        require(not node, 'PREFIX_COLLISION')
        node['$'] = label
    def walk(node):
        if '$' in node:
            require(set(node) == {'$'}, 'PREFIX_COLLISION')
            return
        require(set(node) == {'0', '1'}, 'COVER_GAP')
        walk(node['0'])
        walk(node['1'])
    walk(trie)
    return trie

def path_box(path):
    box = [(F(0), F(1)) for _ in range(3)]
    for depth, bit in enumerate(path):
        axis = depth % 3
        lo, hi = box[axis]
        mid = (lo+hi)/2
        box[axis] = (lo, mid) if bit == '0' else (mid, hi)
    return box

def check_sign(values, strict):
    require(max(values) < 0 if strict else max(values) <= 0, 'SELECTOR_SIGN')

def reject(why, fn):
    try:
        fn()
    except CheckError as error:
        require(error.reason == why, 'WRONG_MUTATION_REASON:'+error.reason)
        return why
    raise CheckError('MUTATION_NOT_REJECTED:'+why)

def main():
    require(len(sys.argv) == 3, 'USAGE_EXPECT_CERT_OUTPUT')
    cert = pathlib.Path(sys.argv[1])
    dest = pathlib.Path(sys.argv[2])
    require(not dest.exists(), 'OUTPUT_EXISTS')
    started = clock()
    raw = cert.read_bytes()
    require(sha(raw) == EXPECTED, 'INPUT_SHA256')
    data = json.loads(raw)
    require(set(data) == {'z','variables','compactification','polynomials','split_axis','selectors','leaf_counts','leaves','imported'}, 'SCHEMA')
    require(data['z'] == '8/9', 'RATIO')
    polys = defining_polynomials()
    for name, poly in polys.items():
        require(canon_hash(poly) == data['polynomials'][name]['sha256'], 'POLYNOMIAL_BINDING:'+name)
        require(list(degree(poly)) == data['polynomials'][name]['degrees'], 'DEGREE_BINDING:'+name)
    strict_tree(data['leaves'])
    require(len(data['leaves']) == 1653, 'EXPECTED_LEAF_COUNT')
    compact = {name: compactify(poly) for name, poly in polys.items()}
    selector = {'Abar<=0': ('Abar', False), 'Dbar<=0': ('Dbar', False), 'f1-4<0': ('f1minus4', True)}
    counts = Counter()
    coefficient_count = 0
    for path, label in data['leaves']:
        guard()
        name, strict = selector[label]
        poly, deg = compact[name]
        vals = box_coefficients(poly, deg, path_box(path))
        check_sign(vals.values(), strict)
        coefficient_count += len(vals)
        counts[label] += 1
    require(dict(counts) == data['leaf_counts'], 'LABEL_COUNTS')
    # Positive analytic polynomial: -(1+s^2+tau^2+g^2) is strictly negative
    # on every point, and all its Bernstein coefficients are negative.
    negative = constant(-1)
    for i in range(3):
        negative = plus(negative, scaled(times(variable(i), variable(i)), -1))
    values = box_coefficients(negative, (2,2,2), [(F(0),F(1))]*3)
    check_sign(values.values(), True)
    controls = {}
    controls['drop_leaf'] = reject('COVER_GAP', lambda: strict_tree(data['leaves'][:-1]))
    controls['duplicate_leaf'] = reject('DUPLICATE_LEAF', lambda: strict_tree(data['leaves']+[data['leaves'][0]]))
    controls['prefix_leaf'] = reject('PREFIX_COLLISION', lambda: strict_tree(data['leaves']+[[data['leaves'][0][0]+'0','Abar<=0']]))
    controls['bad_selector'] = reject('UNKNOWN_SELECTOR', lambda: strict_tree([['','not-a-rule']]))
    controls['wrong_sign'] = reject('SELECTOR_SIGN', lambda: check_sign((-value for value in values.values()), True))
    changed = dict(polys['Abar'])
    changed[(0,0,0)] = changed.get((0,0,0),F(0))+1
    controls['changed_polynomial'] = reject('POLYNOMIAL_BINDING', lambda: require(canon_hash(changed) == data['polynomials']['Abar']['sha256'], 'POLYNOMIAL_BINDING'))
    require(cert.read_bytes() == raw, 'INPUT_DRIFT')
    output = {'kind':'PARENT_INDEPENDENT_DIRECT_BOX_CERTIFICATE_REPLAY','started_native_clock':started,
              'finished_native_clock':clock(),'source_sha256':sha(pathlib.Path(__file__).read_bytes()),
              'input_path':str(cert),'input_sha256':EXPECTED,'input_bytes':len(raw),'input_lf':raw.count(b'\n'),
              'leaves':len(data['leaves']),'selector_counts':dict(counts),'bernstein_coefficients_checked':coefficient_count,
              'mutations':controls,'all_checks_passed':True,'elapsed_seconds':time.monotonic()-START,
              'limits':'Residual certificate only; no full PH theorem or prior Q/H replay, formal/kernel, novelty or cross-model claim. Trusted stdlib Fraction, JSON, integers and implementation. Nonblind supplied-source parent check.'}
    with dest.open('x') as stream:
        json.dump(output,stream,indent=2)
        stream.write('\n')
    print(json.dumps({'status':'PASS','output':str(dest),'sha256':sha(dest.read_bytes()),'leaves':output['leaves'],'coefficients':coefficient_count,'controls':controls}))

if __name__ == '__main__':
    try:
        main()
    except CheckError as error:
        print(json.dumps({'status':'UNKNOWN' if error.reason == 'TIME_LIMIT_UNKNOWN' else 'REJECT','reason':error.reason}),file=sys.stderr)
        raise SystemExit(2)
