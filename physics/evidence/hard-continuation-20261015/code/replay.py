#!/usr/bin/env python3
"""Replay every certificate, cross-check and control of this package; write logs/replay.json.

Run from the package root:  python3 code/replay.py [--with-epoch2] [--quick]

Checks (each records argv, return code, expected code, elapsed seconds, log hash):
  1. certify_a.py and certify_b.py on certificates/trials.json (must exit 0)
     and the A/B enclosures must agree (overlap; endpoint gap reported).
  2. Both certifiers on certificates/reference-trials.json: k=2 at 1.1 and
     the k=3 reference must certify; k=2 at 0.95 must be rejected with a
     rigorous positive lower bound.
  3. Same-law controls (controls/same-law-controls.json): both certifiers
     must exit 1 AND print a rigorous lower bound Psi > 0.
  4. Tamper controls (controls/tamper-controls.json): exit code must equal the
     trial's 'expect' field (1 = rejected premise, 2 = malformed law).
  5. transfer_constants.py (exit 0); finite_audit.py (exit 0) and its
     --break-comparison mutation (exit 1, message 'comparison fails').
  6. --with-epoch2: the immutable epoch-2 checkers (read-only snapshot code)
     on the T=128 compatibility trials (must exit 0).
Gating uses explicit checks; the script exits 1 if any expectation fails.
"""
import argparse
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EPOCH2 = Path('/Users/jinleic/repos/aifours/institute/runs/hard-2026-10-15/problems/phys-p0422/attack-e2')
PIN_FILES = ['code/certify_a.py', 'code/certify_b.py', 'code/transfer_constants.py', 'code/finite_audit.py',
             'code/replay.py', 'certificates/trials.json', 'certificates/reference-trials.json',
             'controls/same-law-controls.json', 'controls/tamper-controls.json']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class Runner:
    def __init__(self):
        self.records = []
        self.ok = True

    def run(self, label, argv, expect, log, markers=(), timeout=1800):
        t0 = time.monotonic()
        p = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                           timeout=timeout, env={**os.environ, 'PYTHONHASHSEED': '0'})
        dt = round(time.monotonic() - t0, 2)
        text = p.stdout + ('\n[stderr]\n' + p.stderr if p.stderr else '')
        logp = ROOT / 'logs' / log
        logp.write_text(text)
        good = p.returncode == expect and all(m in text for m in markers)
        rec = dict(label=label, argv=argv, cwd=str(ROOT), rc=p.returncode, expected_rc=expect,
                   markers=list(markers), passed=good, seconds=dt, log=f'logs/{log}', log_sha256=sha(logp))
        self.records.append(rec)
        self.ok &= good
        print(f"{'PASS' if good else 'FAIL'} [{label}] rc={p.returncode} (expected {expect}) {dt}s", flush=True)
        return text, rec


def enclosures(text):
    out = {}
    for m in re.finditer(r'PSI_ENCLOSURE (\S+) (\S+) (\S+)', text):
        out[m.group(1)] = (Fraction(m.group(2)), Fraction(m.group(3)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--with-epoch2', action='store_true')
    args = ap.parse_args()
    py = sys.executable
    R = Runner()
    start = time.monotonic()
    pins = {f: sha(ROOT / f) for f in PIN_FILES}

    # 1. headline certificates
    ta, _ = R.run('certify_a trials', [py, 'code/certify_a.py', '--trials', 'certificates/trials.json',
                                       '--output', 'certificates/results_a.json'], 0, 'certify-a.txt',
                  ['CERTIFIED k4_T512', 'CERTIFIED k5_T512', 'CERTIFIED k4_T128', 'CERTIFIED k5_T128'])
    tb, _ = R.run('certify_b trials', [py, 'code/certify_b.py', '--trials', 'certificates/trials.json',
                                       '--output', 'certificates/results_b.json'], 0, 'certify-b.txt',
                  ['B-CERTIFIED k4_T512', 'B-CERTIFIED k5_T512', 'B-CERTIFIED k4_T128', 'B-CERTIFIED k5_T128'])
    ea, eb = enclosures(ta), enclosures(tb)
    agreement = {}
    for name in sorted(set(ea) | set(eb)):
        if name not in ea or name not in eb:
            agreement[name] = 'missing'
            R.ok = False
            continue
        (la, ha), (lb, hb) = ea[name], eb[name]
        overlap = max(la, lb) <= min(ha, hb)
        gap = max(abs(la - lb), abs(ha - hb))
        agreement[name] = dict(overlap=overlap, max_endpoint_gap=str(gap), a=[str(la), str(ha)], b=[str(lb), str(hb)])
        R.ok &= overlap
    print('A/B agreement:', json.dumps({k: v if isinstance(v, str) else v['overlap'] for k, v in agreement.items()}))

    # 2. reference trials
    ref_checks = {}
    for c in ('a', 'b'):
        for name, expect in (('k2_T128_at_1.1', 0), ('k3_reference', 0), ('k2_T128_at_0.95', 1)):
            text, rec = R.run(f'certify_{c} {name}', [py, f'code/certify_{c}.py', '--trials',
                                                     'certificates/reference-trials.json', '--name', name],
                              expect, f'reference-{c}-{name}.txt')
            enc = enclosures(text).get(name)
            ref_checks[f'{c}:{name}'] = [str(enc[0]), str(enc[1])] if enc else None
            if expect == 1:
                good = enc is not None and enc[0] > 0
                rec['lower_bound_positive'] = good
                R.ok &= good
    # Vorobyev (2026) published k=3 value, as quoted in the parent's adversarial review
    vor = Fraction('-0.000011202545238429759')
    for c in ('a', 'b'):
        enc = enclosures((ROOT / 'logs' / f'reference-{c}-k3_reference.txt').read_text())['k3_reference']
        contained = enc[0] <= vor <= enc[1]
        ref_checks[f'{c}:k3_contains_quoted_published_value'] = contained
        R.ok &= contained

    # 3. same-law controls
    controls = json.loads((ROOT / 'controls/same-law-controls.json').read_text())['trials']
    same_law = {}
    for t in controls:
        for c in ('a', 'b'):
            text, rec = R.run(f'control {c} {t["name"]}', [py, f'code/certify_{c}.py', '--trials',
                                                           'controls/same-law-controls.json', '--name', t['name']],
                              1, f'control-{c}-{t["name"]}.txt', ['REJECTED'])
            enc = enclosures(text).get(t['name'])
            pos = enc is not None and enc[0] > 0
            rec['lower_bound_positive'] = pos
            R.ok &= pos
            same_law[f'{c}:{t["name"]}'] = dict(alpha=t['alpha'], T=t['T'], role=t.get('role'),
                                                 enclosure=[str(enc[0]), str(enc[1])] if enc else None,
                                                 rigorous_lower_bound_positive=pos)

    # 4. tamper controls
    tampers = json.loads((ROOT / 'controls/tamper-controls.json').read_text())['trials']
    for t in tampers:
        for c in ('a', 'b'):
            R.run(f'tamper {c} {t["name"]}', [py, f'code/certify_{c}.py', '--trials', 'controls/tamper-controls.json',
                                              '--name', t['name']], int(t['expect']), f'tamper-{c}-{t["name"]}.txt')

    # 5. analytic constants and finite audit
    R.run('transfer constants', [py, 'code/transfer_constants.py', '--output', 'certificates/constants.json'], 0,
          'transfer-constants.txt', ['CONSTANTS k4_T512', 'CONSTANTS k5_T512'])
    R.run('finite audit', [py, 'code/finite_audit.py'], 0, 'finite-audit.txt', ['PASS finite exhaustive check'])
    R.run('finite audit mutation', [py, 'code/finite_audit.py', '--break-comparison'], 1,
          'finite-audit-mutation.txt', ['comparison fails'])

    # 6. epoch-2 checkers on the T=128 compatibility trials (read-only external code)
    epoch2 = None
    if args.with_epoch2:
        epoch2 = {'certify.py': sha(EPOCH2 / 'code/certify.py'),
                  'independent_check.py': sha(EPOCH2 / 'code/independent_check.py')}
        for name in ('k4_T128', 'k5_T128'):
            R.run(f'epoch2 certify.py {name}', [py, '-X', 'int_max_str_digits=0', str(EPOCH2 / 'code/certify.py'),
                                                '--trials', 'certificates/trials.json', '--name', name],
                  0, f'epoch2-certify-{name}.txt', [f'PASS {name}'])
            R.run(f'epoch2 independent_check.py {name}', [py, str(EPOCH2 / 'code/independent_check.py'),
                                                          '--trials', 'certificates/trials.json', '--name', name],
                  0, f'epoch2-independent-{name}.txt', [f'ALTERNATE CHECK PASS {name}'])

    receipt = dict(
        package='physics/evidence/hard-continuation-20261015',
        python=sys.version, platform=platform.platform(),
        started_unix=time.time() - (time.monotonic() - start),
        elapsed_seconds=round(time.monotonic() - start, 2),
        input_sha256=pins, epoch2_checker_sha256=epoch2,
        ab_agreement=agreement, reference_checks=ref_checks, same_law_controls=same_law,
        commands=R.records, all_expectations_met=R.ok)
    (ROOT / 'logs/replay.json').write_text(json.dumps(receipt, indent=1) + '\n')
    print(f"{'ALL REPLAY EXPECTATIONS MET' if R.ok else 'REPLAY FAILURES PRESENT'} in {receipt['elapsed_seconds']} s; "
          f"receipt logs/replay.json", flush=True)
    sys.exit(0 if R.ok else 1)


if __name__ == '__main__':
    main()
