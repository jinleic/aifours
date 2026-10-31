#!/usr/bin/env python3
"""Merge the reviewer per-leaf outputs of one batch and decide every leaf.
usage: reviewer-f180-merge.py RECEIPTS_JSON [CERTPATH]
Checks: each job exit 0 and output hash == receipt; every leaf of every cover
decided exactly once per required polynomial (rules from the packet text);
unsorted leaves by an own exact interval test; coverage proofs; label counts."""
import sys, os, json, hashlib, importlib.util
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('rlib', os.path.join(HERE, 'reviewer-f180-lib.py'))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
CERT = '/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261029-ph7-threshold-z3-certificate-v1.json'
NB_RULES = {'unsorted': (), 'F': ('F',), 'A': ('A',), 'Q': ('Q',), 'E4v6': ('mA', 'mE46'),
            'Y2v6': ('mA', 'mG6', 'mD6'), 'Y2tan': ('mA', 'Fm', 'mGq', 'T2'),
            'Y2E': ('mA', 'mGE', 'mDE'), 'Disc': ('mA', 'mDl')}
NB_NONSTRICT = {('Y2v6', 'mD6'), ('Y2E', 'mDE')}
MC_RULES = {'unsorted': (), 'mA': ('mA',), 'D': ('D',), 'H': ('H',), 'Y1end': ('A', 'mD', 'c2', 'mendL', 'mendH')}

def unsorted_box(path):
    ivs = L.path_intervals(path, 6)
    lo = [Fr(n, 1 << l) for n, l in ivs]; hi = [Fr(n + 1, 1 << l) for n, l in ivs]
    return any(lo[i] > hi[j] for i in range(6) for j in range(i + 1, 6))

def main():
    rec = json.load(open(sys.argv[1]))
    certpath = sys.argv[2] if len(sys.argv) > 2 else CERT
    raw = open(certpath, 'rb').read(); cert = json.loads(raw.decode('utf-8')); csha = hashlib.sha256(raw).hexdigest()
    problems = []
    outs = {}
    for j in rec['jobs']:
        if j['exit'] != 0:
            problems.append('job %s exit %s' % (j['argv'], j['exit'])); continue
        fn = os.path.join(HERE, j['out_file'])
        h = hashlib.sha256(open(fn, 'rb').read()).hexdigest()
        if h != j['out_sha256']:
            problems.append('hash mismatch %s' % fn)
        o = json.load(open(fn))
        if o['cert_sha256'] != csha:
            problems.append('cert hash in %s' % fn)
        key = (o['cover'], o['poly'])
        outs.setdefault(key, {})
        for p, r in o['results'].items():
            if p in outs[key]:
                problems.append('leaf decided twice %s %s' % (key, p))
            outs[key][p] = r
    summary = {}
    for cov in ('QO', 'HO'):
        lv = cert[cov]['leaves']; res = outs.get((cov, 'ALL'), {})
        if set(res) != {p for p, _ in lv}:
            problems.append('%s result set != leaf set' % cov)
        cnt = {}
        for p, lab in lv:
            r = res.get(p)
            if r is None or r[0] != lab or r[1] is not True:
                problems.append('%s leaf %s %s failed %s' % (cov, p, lab, r))
            else:
                cnt[lab] = cnt.get(lab, 0) + 1
        summary[cov] = cnt
    for cov, rules in (('NB', NB_RULES), ('MC', MC_RULES)):
        lv = cert[cov]['leaves']; cnt = {}
        for poly in sorted({k for r in rules.values() for k in r}):
            want = {p for p, lab in lv if poly in rules[lab]}
            got = set(outs.get((cov, poly), {}))
            if want != got:
                problems.append('%s %s decided-set mismatch (%d vs %d)' % (cov, poly, len(want), len(got)))
        for p, lab in lv:
            if lab not in rules:
                problems.append('%s unknown label %s' % (cov, lab)); continue
            if lab == 'unsorted':
                good = unsorted_box(p)
            else:
                good = True
                for poly in rules[lab]:
                    r = outs.get((cov, poly), {}).get(p)
                    if r is None:
                        good = False; break
                    sgn = r[1]
                    if (lab, poly) in NB_NONSTRICT and cov == 'NB':
                        good &= sgn >= 0
                    else:
                        good &= sgn > 0
            if not good:
                problems.append('%s leaf %s %s failed' % (cov, p, lab))
            else:
                cnt[lab] = cnt.get(lab, 0) + 1
        summary[cov] = cnt
    lv = cert['residual']['leaves']; res = outs.get(('residual', 'ALL'), {}); cnt = {}
    name_of = {'Abar<=0': 'Abar', 'Dbar<=0': 'Dbar', 'f1-4<0': 'f1minus4'}
    if set(res) != {p for p, _ in lv}:
        problems.append('residual result set != leaf set')
    for p, lab in lv:
        r = res.get(p)
        if r is None or r[0] != name_of.get(lab) or r[1] is not True:
            problems.append('residual leaf %s %s failed %s' % (p, lab, r))
        else:
            cnt[lab] = cnt.get(lab, 0) + 1
    summary['residual'] = cnt
    for cov in ('QO', 'HO', 'NB', 'MC', 'residual'):
        okc, info = L.coverage_proof([p for p, _ in cert[cov]['leaves']])
        if not okc:
            problems.append('%s coverage: %s' % (cov, info))
        summary[cov + '_coverage'] = info
    nonstrict_zero = sum(1 for (cov, poly), d in outs.items() if cov == 'NB' and poly in ('mD6', 'mDE') for r in d.values() if r[1] == 0)
    resid_zero = sum(1 for r in outs.get(('residual', 'ALL'), {}).values() if r[2] == 0)
    print(json.dumps(summary, sort_keys=True))
    print('NB nonstrict polys with min coefficient exactly 0:', nonstrict_zero, '; residual leaves with max coefficient exactly 0:', resid_zero)
    if problems:
        print('MERGE FAIL: %d problems; first: %s' % (len(problems), problems[:5]))
        sys.exit(1)
    print('MERGE PASS: every leaf of QO, HO, NB, MC, residual verified by reviewer per-leaf direct method; coverage proved')

if __name__ == '__main__':
    main()
