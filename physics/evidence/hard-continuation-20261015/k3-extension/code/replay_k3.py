#!/usr/bin/env python3
"""One-command replay of the k=3 extension.  Run from k3-extension/:

    python3 code/replay_k3.py [--with-epoch2]

Every command's argv, return code, expected code, elapsed seconds and log
sha256 is recorded in logs/replay.json; afterwards SHA256SUMS is rewritten
for all package files outside scratch/ and logs-replay1-superseded/.
Expectations (explicit checks, no assert statements):

  1. Vorobyev control (certificates/vorobyev-control.json): certifiers A and
     B exit 0, and both enclosures contain the paper's cross-check value
     -0.000011202545238429759.
  2. Headline trials (certificates/trials.json): A and B exit 0; A and B
     enclosures overlap for every row; results_a.json / results_b.json written.
  3. transfer_constants.py on the headline trials exits 0 (constants.json).
  4. Compat rows for kernel checking (certificates/compat-trials.json, T=128
     and T=256): A and B exit 0 and agree; compat-constants.json written.
  5. Same-law controls (controls/same-law-controls.json and
     controls/compat-same-law-controls.json): A and B exit 1 and print a
     rigorous lower bound Psi > 0 for every row.
  6. Tamper controls (controls/tamper-controls.json): exit code equals the
     row's 'expect' field (1 = premise rejected, 2 = malformed law).
  7. python -O gating: the first same-law control and the first tamper row,
     rerun under python3 -O, still exit 1.
  8. code/precision_report.py exits 0: for every headline row, all mu_j and
     Psi enclosure widths of A and B are below 1e-40 (writes precision.json).
  9. --with-epoch2 only (immutable epoch-2 checkers, read-only): both certify
     the two T=128 compat rows (exit 0); the 384-bit epoch-2 producer rejects
     k3_T1024 (exit 1), i.e. a precision-starved implementation fails safe.
Exit status 0 iff every expectation holds.
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
EPOCH2 = Path('/Users/jinleic/repos/aifours/institute/runs/hard-2026-10-15/problems/phys-p0422/attack-e2/code')
VOROBYEV_VALUE = Fraction('-0.000011202545238429759')
SUM_EXCLUDE = ('scratch', 'logs-replay1-superseded', '__pycache__')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def enclosures(text):
    return {m.group(1): (Fraction(m.group(2)), Fraction(m.group(3)))
            for m in re.finditer(r'PSI_ENCLOSURE (\S+) (\S+) (\S+)', text)}


class Runner:
    def __init__(self):
        self.records = []
        self.ok = True

    def run(self, label, argv, expect, log, markers=()):
        t0 = time.monotonic()
        p = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                           timeout=3600, env={**os.environ, 'PYTHONHASHSEED': '0'})
        dt = round(time.monotonic() - t0, 2)
        text = p.stdout + ('\n[stderr]\n' + p.stderr if p.stderr else '')
        logp = ROOT / 'logs' / log
        logp.write_text(f'$ {" ".join(argv)}\n' + text + f'\n[rc={p.returncode} expected={expect} seconds={dt}]\n')
        good = p.returncode == expect and all(m in text for m in markers)
        rec = dict(label=label, argv=argv, rc=p.returncode, expected_rc=expect, markers=list(markers),
                   passed=good, seconds=dt, log=f'logs/{log}', log_sha256=sha(logp))
        self.records.append(rec)
        self.ok &= good
        print(f"{'PASS' if good else 'FAIL'} [{label}] rc={p.returncode} (expected {expect}) {dt}s", flush=True)
        return text, rec

    def require(self, cond, what, rec=None):
        if rec is not None:
            rec.setdefault('extra_checks', []).append(dict(check=what, passed=bool(cond)))
        if not cond:
            print(f'FAIL [{what}]', flush=True)
        self.ok &= bool(cond)


def certify_both(R, py, trials_file, tag, names):
    ta, _ = R.run(f'certify_a {tag}', [py, 'code/certify_a.py', '--trials', trials_file,
                                       '--output', f'certificates/{tag}results_a.json'], 0, f'{tag}certify-a.txt',
                  [f'CERTIFIED {n}' for n in names])
    tb, _ = R.run(f'certify_b {tag}', [py, 'code/certify_b.py', '--trials', trials_file,
                                       '--output', f'certificates/{tag}results_b.json'], 0, f'{tag}certify-b.txt',
                  [f'B-CERTIFIED {n}' for n in names])
    ea, eb = enclosures(ta), enclosures(tb)
    agreement = {}
    for n in names:
        if n not in ea or n not in eb:
            R.require(False, f'enclosure missing for {n}')
            continue
        (la, ha), (lb, hb) = ea[n], eb[n]
        overlap = max(la, lb) <= min(ha, hb)
        agreement[n] = dict(overlap=overlap, a=[str(la), str(ha)], b=[str(lb), str(hb)],
                            max_endpoint_gap=str(max(abs(la - lb), abs(ha - hb))))
        R.require(overlap, f'A/B enclosures overlap for {n}')
    return agreement


def same_law(R, py, controls_file, out):
    rows = json.loads((ROOT / controls_file).read_text())['trials']
    for t in rows:
        for c in ('a', 'b'):
            text, rec = R.run(f'same-law {c} {t["name"]}', [py, f'code/certify_{c}.py', '--trials',
                                                            controls_file, '--name', t['name']],
                              1, f'control-{c}-{t["name"]}.txt', ['REJECTED'])
            enc = enclosures(text).get(t['name'])
            pos = enc is not None and enc[0] > 0
            R.require(pos, f'{c}: rigorous lower bound > 0 for {t["name"]}', rec)
            out[f'{c}:{t["name"]}'] = dict(alpha=t['alpha'], T=t['T'], role=t.get('role'),
                                            enclosure=[str(enc[0]), str(enc[1])] if enc else None,
                                            rigorous_lower_bound_positive=pos)
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--with-epoch2', action='store_true')
    args = ap.parse_args()
    py = sys.executable
    R = Runner()
    start = time.monotonic()
    (ROOT / 'logs').mkdir(exist_ok=True)
    pins = {f: sha(ROOT / f) for f in (
        'code/certify_a.py', 'code/certify_b.py', 'code/transfer_constants.py', 'code/replay_k3.py',
        'code/precision_report.py', 'certificates/trials.json', 'certificates/compat-trials.json',
        'certificates/vorobyev-control.json', 'controls/same-law-controls.json',
        'controls/compat-same-law-controls.json', 'controls/tamper-controls.json')}

    # 1. Vorobyev control
    vor = {}
    for c in ('a', 'b'):
        text, rec = R.run(f'vorobyev control {c}', [py, f'code/certify_{c}.py', '--trials',
                                                    'certificates/vorobyev-control.json'],
                          0, f'vorobyev-control-{c}.txt')
        enc = enclosures(text).get('k3_vorobyev_4.268_T128')
        contained = enc is not None and enc[0] <= VOROBYEV_VALUE <= enc[1]
        R.require(contained, f'{c}: enclosure contains Vorobyev value -0.000011202545238429759', rec)
        vor[c] = [str(enc[0]), str(enc[1])] if enc else None

    # 2-3. headline trials and constants
    names = [t['name'] for t in json.loads((ROOT / 'certificates/trials.json').read_text())['trials']]
    agreement = certify_both(R, py, 'certificates/trials.json', '', names)
    R.run('transfer constants', [py, 'code/transfer_constants.py', '--trials', 'certificates/trials.json',
                                 '--output', 'certificates/constants.json'], 0, 'transfer-constants.txt',
          [f'CONSTANTS {n}' for n in names])

    # 4. compat rows (T=128, T=256) for kernel checking
    cnames = [t['name'] for t in json.loads((ROOT / 'certificates/compat-trials.json').read_text())['trials']]
    compat_agreement = certify_both(R, py, 'certificates/compat-trials.json', 'compat-', cnames)
    R.run('compat transfer constants', [py, 'code/transfer_constants.py', '--trials', 'certificates/compat-trials.json',
                                        '--output', 'certificates/compat-constants.json'], 0,
          'compat-transfer-constants.txt', [f'CONSTANTS {n}' for n in cnames])

    # 5. same-law controls
    same = {}
    rows = same_law(R, py, 'controls/same-law-controls.json', same)
    same_law(R, py, 'controls/compat-same-law-controls.json', same)

    # 6. tamper controls
    tam = json.loads((ROOT / 'controls/tamper-controls.json').read_text())['trials']
    for t in tam:
        for c in ('a', 'b'):
            R.run(f'tamper {c} {t["name"]}', [py, f'code/certify_{c}.py', '--trials', 'controls/tamper-controls.json',
                                              '--name', t['name']], int(t['expect']), f'tamper-{c}-{t["name"]}.txt')

    # 7. python -O gating
    first_reject = next(t for t in tam if int(t['expect']) == 1)
    for c in ('a', 'b'):
        R.run(f'python -O same-law {c}', [py, '-O', f'code/certify_{c}.py', '--trials', 'controls/same-law-controls.json',
                                          '--name', rows[0]['name']], 1, f'python-O-same-law-{c}.txt', ['REJECTED'])
        R.run(f'python -O tamper {c}', [py, '-O', f'code/certify_{c}.py', '--trials', 'controls/tamper-controls.json',
                                        '--name', first_reject['name']], 1, f'python-O-tamper-{c}.txt', ['REJECTED'])

    # 8. working-precision report
    R.run('precision report', [py, 'code/precision_report.py', '--trials', 'certificates/trials.json',
                               '--output', 'certificates/precision.json'], 0, 'precision-report.txt',
          [f'PRECISION {n}' for n in names])

    # 9. epoch-2 checkers (optional, read-only)
    epoch2 = None
    if args.with_epoch2:
        epoch2 = {'certify.py': sha(EPOCH2 / 'certify.py'), 'independent_check.py': sha(EPOCH2 / 'independent_check.py')}
        for n in [x for x in cnames if 'T128' in x]:
            R.run(f'epoch2 certify.py {n}', [py, '-X', 'int_max_str_digits=0', str(EPOCH2 / 'certify.py'),
                                             '--trials', 'certificates/compat-trials.json', '--name', n],
                  0, f'epoch2-certify-{n}.txt', [f'PASS {n}'])
            R.run(f'epoch2 independent_check.py {n}', [py, str(EPOCH2 / 'independent_check.py'),
                                                       '--trials', 'certificates/compat-trials.json', '--name', n],
                  0, f'epoch2-independent-{n}.txt', [f'ALTERNATE CHECK PASS {n}'])
        R.run('epoch2 certify.py k3_T1024 (384-bit grid: must fail safe)',
              [py, '-X', 'int_max_str_digits=0', str(EPOCH2 / 'certify.py'), '--trials', 'certificates/trials.json',
               '--name', 'k3_T1024'], 1, 'epoch2-certify-k3_T1024-failsafe.txt', ['claimed negative margin fails'])

    receipt = dict(package='physics/evidence/hard-continuation-20261015/k3-extension',
                   python=sys.version, platform=platform.platform(), with_epoch2=args.with_epoch2,
                   elapsed_seconds=round(time.monotonic() - start, 2), input_sha256=pins, epoch2_checker_sha256=epoch2,
                   vorobyev_control=vor, ab_agreement=agreement, compat_ab_agreement=compat_agreement,
                   same_law_controls=same, commands=R.records, all_expectations_met=R.ok)
    (ROOT / 'logs/replay.json').write_text(json.dumps(receipt, indent=1) + '\n')

    files = sorted(p for p in ROOT.rglob('*') if p.is_file() and p.name != 'SHA256SUMS'
                   and not any(part in SUM_EXCLUDE for part in p.relative_to(ROOT).parts))
    (ROOT / 'SHA256SUMS').write_text(''.join(f'{sha(p)}  {p.relative_to(ROOT)}\n' for p in files))
    print(f"{'ALL EXPECTATIONS MET' if R.ok else 'FAILURES PRESENT'} in {receipt['elapsed_seconds']} s; "
          f"{len(R.records)} commands; receipt logs/replay.json; SHA256SUMS over {len(files)} files", flush=True)
    sys.exit(0 if R.ok else 1)


if __name__ == '__main__':
    main()
