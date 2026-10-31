#!/usr/bin/env python3
"""Exact factorization of a stored level-six minor polynomial (structure report).

Loads a minor JSON, factors it over Q with SymPy, checks the product, labels
factors strictly positive on the closed quadrant when all coefficients share one
sign and the constant term is nonzero, and stores every factor exactly.
"""
import argparse
import hashlib
import importlib.util
import json
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


S = load('sympyhelper', 'frontier-review-f18-ph7-independent-check.py').S


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--minor', required=True)
    args = ap.parse_args()
    raw = (ROOT / args.minor).read_bytes()
    M = json.loads(raw)
    out = ROOT / args.minor.replace('-v1.json', '-factors-v1.json')
    if out.exists():
        raise FileExistsError(out)
    x, y = S.symbols('x y')
    poly = S.Poly(sum(S.Rational(t['coefficient']) * x**t['x_power'] * y**t['y_power'] for t in M['coefficients']), x, y)
    t0 = time.monotonic()
    content, factors = S.factor_list(poly.as_expr())
    seconds = round(time.monotonic() - t0, 1)
    rebuilt = S.Poly(content, x, y)
    entries = []
    for g, m in factors:
        gp = S.Poly(g, x, y)
        rebuilt *= gp**m
        cs = gp.coeffs()
        positive = gp.coeff_monomial(1) != 0 and (all(c > 0 for c in cs) or all(c < 0 for c in cs))
        entries.append({'multiplicity': m, 'total_degree': gp.total_degree(), 'degree_x': gp.degree(x),
                        'degree_y': gp.degree(y), 'terms': len(cs), 'strictly_positive_on_quadrant': positive,
                        'coefficients': [{'x_power': i, 'y_power': j, 'coefficient': str(c)}
                                         for (i, j), c in sorted(zip(gp.monoms(), gp.coeffs()))]})
    assert rebuilt == poly
    result = {'minor': args.minor, 'minor_sha256': hashlib.sha256(raw).hexdigest(), 'content': str(content),
              'factor_seconds': seconds, 'factors': entries, 'product_checked': True}
    out.write_text(json.dumps(result, indent=2) + '\n')
    print('DONE factor', args.minor, 'secs', seconds,
          [(e['multiplicity'], e['total_degree'], e['strictly_positive_on_quadrant']) for e in entries], out.name, flush=True)


if __name__ == '__main__':
    main()
