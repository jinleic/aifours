#!/usr/bin/env python3
"""Fail-before / pass-after regressions for the 2026-10-16 validation-only fix.

Each malformed fixture is offered to the archived PRE-FIX code (code/archive/:
certify-f6eaa1a8.py, check_coverage-d4949917.py, exact bytes) and to the current
code.  A regression passes only if the pre-fix code ACCEPTS it (exit 0, so the
defect is real) and the current code REJECTS it (exit 1, explicit
'CHECK FAILED: <expected reason>').  Provenance cases (tampered archived
producer bytes) exist only for the current code.  Positive cases replay
authentic receipts with the current code.

Fixtures are written to a fresh controls/fixtures/<UTC>-<pid>/regressions/ run
directory and kept; the real receipts are only read; nothing is deleted.
"""
import argparse
import copy
import gzip
import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PY = sys.executable
OLD_CERTIFY = HERE / 'archive' / 'certify-f6eaa1a8.py'
OLD_COVERAGE = HERE / 'archive' / 'check_coverage-d4949917.py'
NEW_CERTIFY = HERE / 'certify.py'
NEW_COVERAGE = HERE / 'check_coverage.py'
PINS = {OLD_CERTIFY: 'f6eaa1a80c4112d7af3caa54901f5451a88f9527bb9f23c4be54e89b897941a6',
        OLD_COVERAGE: 'd494991761188902f74433882100d53163a210a5d47198a0187f30188ae5cb9a'}
DEFAULT_ATTACK = (BASE / 'inputs' if (BASE / 'inputs').is_dir() else
                  HERE.parents[3] / 'institute/runs/hard-2026-10-15/problems/math-p0039/attack-e2')


def run(cmd):
    began = time.monotonic()
    done = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, timeout=290)
    err = done.stderr.strip().splitlines()[-1] if done.stderr.strip() else ''
    return dict(command=[Path(str(c)).name if str(c).endswith('.py') or c == PY else str(c) for c in cmd],
                returncode=done.returncode, stderr_last=err, seconds=round(time.monotonic() - began, 3))


def read_receipts(src):
    src = Path(src)
    rows = [json.loads(p.read_text()) for p in sorted(src.glob('*/*.json'))]
    for path in sorted(src.glob('*.jsonl.gz')):
        with gzip.open(path, 'rt') as f:
            rows.extend(json.loads(x) for x in f)
    return rows


def write_fixture(d, rows, note):
    d.mkdir(parents=True)
    raw = ''.join(json.dumps(r, separators=(',', ':')) + '\n' for r in rows).encode()
    (d / 'receipts.jsonl.gz').write_bytes(gzip.compress(raw, mtime=0))
    (d / 'CASE.json').write_text(json.dumps(note, indent=1) + '\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--receipts', default=str(BASE / 'receipts'))
    ap.add_argument('--attack', default=str(DEFAULT_ATTACK))
    ap.add_argument('--fixtures', default=str(BASE / 'controls' / 'fixtures'))
    ap.add_argument('--output')
    args = ap.parse_args()
    for path, pin in PINS.items():
        if hashlib.sha256(path.read_bytes()).hexdigest() != pin:
            sys.exit('CHECK FAILED: archived pre-fix source differs from its pin: %s' % path.name)
    began = time.monotonic()
    run_dir = Path(args.fixtures) / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-%d' % os.getpid()) / 'regressions'
    run_dir.mkdir(parents=True)
    logs = str(Path(args.attack) / 'logs')
    rows = read_receipts(args.receipts)
    lows = sorted((r for r in rows if r['task'] == 'low'), key=lambda r: r['first'])
    mains = sorted((r for r in rows if r['task'] == 'main'), key=lambda r: r['first'])
    reduced = lows + mains[:1]
    old_cov = [PY, OLD_COVERAGE, '--attack', args.attack, '--checker', OLD_CERTIFY]
    new_cov = [PY, NEW_COVERAGE, '--attack', args.attack]

    def collision(pairs, difference):
        def f(rs):
            b = rs[0]['blocks'][0]
            res = next(x for x in b['resolutions'] if x['n'] == 512)
            res['pairs'], res['difference'] = pairs, difference
        return f

    def fractional(rs):
        b = rs[0]['blocks'][0]
        i = next(k for k, x in enumerate(b['resolutions']) if x['n'] == 512)
        b['resolutions'][i] = dict(n=512, p=262657, resolution='proper-factor', factor=131328.5)

    def float_start(rs):
        rs[1]['blocks'][0]['start'] = float(rs[1]['blocks'][0]['start'])

    def negative_stride(rs):
        rs[0]['mpdec_stride'] = -1
        for b in rs[0]['blocks']:
            b['mpdec_residues'] = 0

    def foreign_stamp(rs):
        rs[0]['checker_sha256'] = '0' * 64

    cases = [
        ('alias-collision', 'defect 1: pairs [[1,2],[262658,262659]] are the same field pair (1,2) mod 262657',
         reduced, collision([[1, 2], [262658, 262659]], 262656), 'coverage',
         'collision witness not in canonical representatives'),
        ('zero-difference-alias', 'defect 1: pairs [[1,262658],[2,262659]] have difference 0 mod p',
         reduced, collision([[1, 262658], [2, 262659]], 0), 'coverage',
         'collision witness not in canonical representatives'),
        ('fractional-factor', 'defect 2: factor 131328.5 for prime p = 262657',
         reduced, fractional, 'coverage', 'resolution factor is not an integer proper divisor'),
        ('float-geometry', 'hardening: float block start equal to the integer geometry',
         reduced, float_start, 'coverage', 'non-integer block field'),
        ('negative-stride-replay', 'defect 3: stride -1 and mpdec_residues 0 skip every libmpdec check',
         mains[:1], negative_stride, 'replay', 'receipt libmpdec sampling policy'),
        ('foreign-stamp-replay', 'hardening: replay of a receipt stamped by an unknown checker',
         mains[:1], foreign_stamp, 'replay', 'receipt from an unrecognized checker'),
    ]
    out = []
    for name, why, base_rows, fn, kind, reason in cases:
        rs = copy.deepcopy(base_rows)
        fn(rs)
        d = run_dir / name
        write_fixture(d, rs, dict(case=name, why=why, expected_after_reason=reason))
        if kind == 'coverage':
            before = run(old_cov + ['--receipts', d])
            after = run(new_cov + ['--receipts', d])
        else:
            rep = ['replay', '--task', 'main', '--blocks', '256', '--receipts', d, '--logs', logs]
            before = run([PY, OLD_CERTIFY] + rep)
            after = run([PY, NEW_CERTIFY] + rep)
        ok = (before['returncode'] == 0 and after['returncode'] == 1
              and after['stderr_last'].startswith('CHECK FAILED: ') and reason in after['stderr_last'])
        out.append(dict(case=name, why=why, before_prefix_code=before, after_current_code=after,
                        expected_after_reason=reason, fail_before_pass_after=ok))
    # Provenance: tampered archived producer bytes must be rejected by the current coverage check.
    tampered = run_dir / 'tampered-producer-source'
    tampered.mkdir(parents=True)
    data = bytearray(OLD_CERTIFY.read_bytes())
    data[-2] ^= 1
    (tampered / 'certify-f6eaa1a8.py').write_bytes(bytes(data))
    (tampered / 'CASE.json').write_text(json.dumps(dict(case='tampered-producer-source',
                                                        why='one flipped bit in a copy of the archived producer'), indent=1) + '\n')
    t = run(new_cov + ['--receipts', args.receipts, '--producer-source', tampered / 'certify-f6eaa1a8.py'])
    out.append(dict(case='tampered-producer-source', after_current_code=t,
                    expected_after_reason='archived producer source differs from its pin',
                    fail_before_pass_after=t['returncode'] == 1 and 'archived producer source differs from its pin' in t['stderr_last']))
    # Positive: authentic receipts with the current code.
    positives = [
        ('coverage-authentic', new_cov + ['--receipts', args.receipts, '--require-through', '2582236504064']),
        ('replay-authentic-low', [PY, NEW_CERTIFY, 'replay', '--task', 'low', '--blocks', '0,993',
                                  '--receipts', args.receipts, '--logs', logs]),
        ('replay-authentic-main', [PY, NEW_CERTIFY, 'replay', '--task', 'main', '--blocks', '256,8940',
                                   '--receipts', args.receipts, '--logs', logs]),
        ('replay-authentic-extension', [PY, NEW_CERTIFY, 'replay', '--task', 'extension', '--blocks', '0,2891',
                                        '--receipts', args.receipts, '--logs', logs]),
    ]
    for name, cmd in positives:
        r = run(cmd)
        out.append(dict(case=name, after_current_code=r, fail_before_pass_after=r['returncode'] == 0))
    result = dict(fixtures=str(run_dir), cases=out, passed=sum(c['fail_before_pass_after'] for c in out),
                  total=len(out), all_passed=all(c['fail_before_pass_after'] for c in out),
                  pre_fix_sources={p.name: h for p, h in PINS.items()},
                  current_sources={NEW_CERTIFY.name: hashlib.sha256(NEW_CERTIFY.read_bytes()).hexdigest(),
                                   NEW_COVERAGE.name: hashlib.sha256(NEW_COVERAGE.read_bytes()).hexdigest()},
                  seconds=round(time.monotonic() - began, 3))
    text = json.dumps(result, indent=1)
    (run_dir / 'regressions-result.json').write_text(text + '\n')
    if args.output:
        Path(args.output).write_text(text + '\n')
    print(text)
    sys.exit(0 if result['all_passed'] else 1)


if __name__ == '__main__':
    main()
