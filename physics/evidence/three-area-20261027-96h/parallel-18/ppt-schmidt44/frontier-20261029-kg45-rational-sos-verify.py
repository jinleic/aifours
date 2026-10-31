#!/usr/bin/env python3
"""Exact verifier for a strict 2-block-positive witness of the fixed KG 4x5 state.

Usage: python3 FILE --self-check
       python3 FILE --check CERTIFICATE.json

A certificate is a JSON object with exactly these keys:
  w: sparse upper-triangle entries [i,j,real,imag], 0<=i<=j<20;
  sos0: list of rational real polynomials;
  sos_ball: list of rational real polynomials;
  h: exactly five rational real polynomials.
Each polynomial is a list [coefficient, [variable indices]] of monomials,
where a coefficient is an integer or a fraction string and indices are in
0..35 (repeated indices denote powers). A and B are complex matrices of shape
4x2 and 5x2. Each entry uses consecutive real/imaginary variables; A occupies
0..15 and B occupies 16..35, both in row-major order.

The program checks the exact identity f_W-1/124 = sum sos0^2 +
(3-||A,B||^2) sum sos_ball^2 + sum h_j*g_j, where g_j are the four real
entries of A^*A-I_2 and ||B||_F^2-1. It also checks T^2 invariance and
Tr(W rho_KG)<-1/4. A passing certificate proves W is 2-block positive and
strictly detects the fixed PPT state; it does NOT prove the 4x4 target.
"""
import argparse
import json
import sys
from fractions import Fraction as F

NVAR = 36
ONE = {(): F(1)}
ZERO = {}
MARGIN = F(1, 124)


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (str, int)):
        raise ValueError('rational must be an integer or fraction string')
    return F(value)


def add(*parts):
    out = {}
    for part in parts:
        for mon, val in part.items():
            out[mon] = out.get(mon, F(0)) + val
            if out[mon] == 0:
                del out[mon]
    return out


def scale(poly, value):
    value = F(value)
    return {m: value * c for m, c in poly.items() if value * c}


def mul(left, right):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            m = tuple(sorted(lm + rm))
            out[m] = out.get(m, F(0)) + lc * rc
            if out[m] == 0:
                del out[m]
    return out


def var(i):
    return {(i,): F(1)}


def poly_input(value):
    if not isinstance(value, list):
        raise ValueError('polynomial must be a list of monomials')
    out = {}
    for term in value:
        if not isinstance(term, list) or len(term) != 2:
            raise ValueError('monomial must be [coefficient, variable-indices]')
        c, idx = term
        c = rational(c)
        if not isinstance(idx, list) or any(isinstance(i, bool) or not isinstance(i, int) or not 0 <= i < NVAR for i in idx):
            raise ValueError('variable index outside 0..35')
        mon = tuple(sorted(idx))
        out[mon] = out.get(mon, F(0)) + c
        if out[mon] == 0:
            del out[mon]
    return out


def poly_export(poly):
    return [[str(c), list(m)] for m, c in sorted(poly.items())]


def norm2(re, im):
    return add(mul(re, re), mul(im, im))


def data_polynomials():
    ar = [[var(2 * (2 * i + j)) for j in range(2)] for i in range(4)]
    ai = [[var(2 * (2 * i + j) + 1) for j in range(2)] for i in range(4)]
    br = [[var(16 + 2 * (2 * i + j)) for j in range(2)] for i in range(5)]
    bi = [[var(17 + 2 * (2 * i + j)) for j in range(2)] for i in range(5)]
    bn = [add(*(norm2(br[i][j], bi[i][j]) for i in range(5))) for j in range(2)]
    an = [add(*(norm2(ar[i][j], ai[i][j]) for i in range(4))) for j in range(2)]
    g3 = add(*(add(mul(ar[i][0], ar[i][1]), mul(ai[i][0], ai[i][1])) for i in range(4)))
    g4 = add(*(add(mul(ar[i][0], ai[i][1]), scale(mul(ai[i][0], ar[i][1]), -1)) for i in range(4)))
    sbr = add(*(add(mul(br[i][0], br[i][1]), mul(bi[i][0], bi[i][1])) for i in range(5)))
    sbi = add(*(add(mul(bi[i][0], br[i][1]), scale(mul(br[i][0], bi[i][1]), -1)) for i in range(5)))
    g = [add(an[0], scale(ONE, -1)), add(an[1], scale(ONE, -1)), g3, g4, add(*bn, scale(ONE, -1))]
    ball = add(scale(ONE, 3), scale(add(*an, *bn), -1))
    xr, xi = [], []
    for i in range(4):
        for j in range(5):
            xr.append(add(*(add(mul(ar[i][k], br[j][k]), scale(mul(ai[i][k], bi[j][k]), -1)) for k in range(2))))
            xi.append(add(*(add(mul(ar[i][k], bi[j][k]), mul(ai[i][k], br[j][k])) for k in range(2))))
    return g, ball, xr, xi, bn, sbr, sbi


def form(w, xr, xi):
    terms = []
    for (i, j), (re, im) in w.items():
        if i == j:
            terms.append(scale(norm2(xr[i], xi[i]), re))
        else:
            rr = add(mul(xr[i], xr[j]), mul(xi[i], xi[j]))
            ii = add(mul(xr[i], xi[j]), scale(mul(xi[i], xr[j]), -1))
            terms.append(scale(add(scale(rr, re), scale(ii, -im)), 2))
    return add(*terms) if terms else ZERO


def rhs(sos0, sos_ball, h, g, ball):
    pieces = [mul(p, p) for p in sos0]
    pieces += [mul(ball, mul(p, p)) for p in sos_ball]
    pieces += [mul(p, gi) for p, gi in zip(h, g)]
    return add(*pieces) if pieces else ZERO


def kg_trace(w):
    vectors = [([0, 6, 12], [1, 1, 1], 1), ([1, 7], [1, 1], 1),
               ([5, 11], [1, -1], 1), ([2, 19], [1, 1], 3),
               ([10, 18], [1, 1], 3), ([4], [1], 3),
               ([13], [1], 3), ([15], [1], 3), ([17], [1], 3)]
    out = F(0)
    for inds, values, weight in vectors:
        for x, i in enumerate(inds):
            for y, j in enumerate(inds):
                key = (min(i, j), max(i, j))
                out += weight * values[x] * values[y] * w.get(key, (F(0), F(0)))[0]
    return out


def parse_candidate(obj):
    if not isinstance(obj, dict) or set(obj) != {'w', 'sos0', 'sos_ball', 'h'}:
        raise ValueError('certificate must have exactly keys w,sos0,sos_ball,h')
    # Effective T^2 characters in (delta,xi); diagonal indices always allowed.
    chars = [(0,0),(-1,0),(-2,0),(2,-1),(-2,-1),
             (1,0),(0,0),(-1,0),(3,-1),(-1,-1),
             (2,0),(1,0),(0,0),(4,-1),(0,-1),
             (0,1),(-1,1),(-2,1),(2,0),(-2,0)]
    w = {}
    if not isinstance(obj['w'], list):
        raise ValueError('w must be a sparse upper-triangle list')
    for item in obj['w']:
        if not isinstance(item, list) or len(item) != 4:
            raise ValueError('w entry must be [i,j,re,im]')
        i, j, re, im = item
        if any(isinstance(v, bool) or not isinstance(v, int) for v in (i,j)) or not 0 <= i <= j < 20:
            raise ValueError('w indices outside upper triangle')
        if (i,j) in w:
            raise ValueError('duplicate w entry')
        re, im = rational(re), rational(im)
        if i == j and im:
            raise ValueError('diagonal w entry must be real')
        if chars[i] != chars[j] and (re or im):
            raise ValueError('w is not T^2-invariant')
        w[(i,j)] = (re, im)
    if not isinstance(obj['sos0'], list) or not isinstance(obj['sos_ball'], list):
        raise ValueError('sum-of-squares fields must be lists')
    if not isinstance(obj['h'], list) or len(obj['h']) != 5:
        raise ValueError('h must contain exactly five polynomials')
    return w, [poly_input(p) for p in obj['sos0']], [poly_input(p) for p in obj['sos_ball']], [poly_input(p) for p in obj['h']]


def check_identity(w, sos0, sos_ball, h):
    g, ball, xr, xi, _, _, _ = data_polynomials()
    left = add(form(w, xr, xi), scale(ONE, -MARGIN))
    right = rhs(sos0, sos_ball, h, g, ball)
    return left == right, len(left), len(right)


def self_check():
    g, ball, xr, xi, bn, sbr, sbi = data_polynomials()
    w = {(i,i): (F(1), F(0)) for i in range(20)}
    # 123/124 = (30/31)^2+(7/31)^2+(2/31)^2+(1/62)^2.
    sos = [{():c} for c in (F(30,31), F(7,31), F(2,31), F(1,62))]
    h = [bn[0], bn[1], scale(sbr, 2), scale(sbi, 2), ONE]
    ok, nleft, nright = check_identity(w, sos, [], h)
    if not ok or kg_trace(w) != 31:
        raise AssertionError('identity witness control failed')
    bad_h = h[:]; bad_h[2] = add(bad_h[2], ONE)
    if check_identity(w, sos, [], bad_h)[0]:
        raise AssertionError('mutated identity unexpectedly passed')
    bad_w = dict(w); bad_w[(0,0)] = (F(2), F(0))
    if check_identity(bad_w, sos, [], h)[0]:
        raise AssertionError('mutated W unexpectedly passed')
    print(json.dumps({'exact_identity_control': 'PASS', 'lhs_monomials': nleft,
                      'rhs_monomials': nright, 'identity_mutations_rejected': 2,
                      'Tr_I_rho_KG': str(kg_trace(w)), 'detects_KG': False,
                      'scope': 'NONDETECTING control, not a target witness'}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--self-check', action='store_true')
    group.add_argument('--check', metavar='CERTIFICATE.json')
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    with open(args.check, encoding='utf-8') as f:
        obj = json.load(f)
    w, sos0, sos_ball, h = parse_candidate(obj)
    ok, nleft, nright = check_identity(w, sos0, sos_ball, h)
    if not ok:
        raise ValueError('exact polynomial identity does not hold')
    pairing = kg_trace(w)
    if pairing >= F(-1, 4):
        raise ValueError('Tr(W rho_KG) is not strictly below -1/4')
    print(json.dumps({'certificate': 'PASS_EXACT_RATIONAL_IDENTITY', 'strict_SR2_margin': str(MARGIN),
                      'Tr_W_rho_KG': str(pairing), 'lhs_monomials': nleft, 'rhs_monomials': nright,
                      'scope': 'detects fixed 4x5 PPT source; NOT a 4x4 target certificate'}, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, ZeroDivisionError, OSError, json.JSONDecodeError) as exc:
        print(f'REJECT: {exc}', file=sys.stderr)
        sys.exit(1)
