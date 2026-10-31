#!/usr/bin/env python3
"""Reviewer wrong-z negative (digest level): rebuild every certified polynomial from the
written definitions at z = 83/100 (positive) and at z = 41/50, 21/25 (negatives) and
compare scale lcm + digest with the certificate.  Expected: all match at 83/100, none
of the z-dependent ones at the wrong z (z-free polynomials F, Fm are reported)."""
import sys, os, json, hashlib, importlib.util, time
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
L = _load('rlib', 'reviewer-f180-lib.py'); RD = _load('rdefs', 'reviewer-f180-defs.py')
CERT = '/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261029-ph7-threshold-z3-certificate-v1.json'
T0 = time.time(); raw = open(CERT, 'rb').read(); cert = json.loads(raw.decode('utf-8'))
print('cert sha256', hashlib.sha256(raw).hexdigest())
allgood = True
for zval, expect_match in ((Fr(83, 100), True), (Fr(41, 50), False), (Fr(21, 25), False)):
    nb, mc, _ = RD.selector_polys(zval); Q, H = RD.compact_polys(zval); rp = RD.residual_polys(zval)
    items = [('NB:' + k, P, cert['NB']['polynomials'][k]['sha256']) for k, P in nb.items()]
    items += [('MC:' + k, P, cert['MC']['polynomials'][k]['sha256']) for k, P in mc.items()]
    items += [('QO', Q, cert['QO']['sha256']), ('HO', H, cert['HO']['sha256'])]
    items += [('residual:' + k, P, cert['residual']['polynomials'][k]['sha256']) for k, P in rp.items()]
    match = []; zfree = []
    for name, P, dg in items:
        Pi, _ = L.integerize(P)
        if L.digest(Pi) == dg:
            match.append(name)
    if expect_match:
        good = len(match) == len(items)
    else:
        good = set(match) <= {'NB:F', 'NB:Fm', 'residual:f1minus4'}
    allgood &= good
    print('z=%s: %d/%d digests match (%s) -> %s' % (zval, len(match), len(items), ', '.join(match) if len(match) < len(items) else 'all',
                                                   'as intended' if good else 'NOT as intended'))
print('seconds', round(time.time() - T0, 1))
sys.exit(0 if allgood else 1)
