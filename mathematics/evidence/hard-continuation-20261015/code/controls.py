#!/usr/bin/env python3
"""Positive and discriminating negative controls for certify.py and check_coverage.py.

Every negative control must exit 1 with an explicit 'CHECK FAILED: <reason>'
containing the expected reason (not an import error or timeout).  Every file a
control writes goes to a fresh, uniquely named run directory under
controls/fixtures/ (override with --fixtures) and is retained; nothing is ever
deleted, and the real receipts are only read.  Coverage mutations are applied to
in-memory copies of a reduced receipt set (all low receipts plus the first main
receipt), written as one gzip JSONL fixture per case.  A missing receipt is
simulated by omitting it from the copy, recorded in OMITTED.json.
Groups: tiny (tiny-task positive, writes one fixture), injections (certify.py
injections and replays, write nothing), coverage (receipt mutations), arithmetic
(tiny + injections), all.
"""
import argparse
import copy
import gzip
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
CERTIFY = str(HERE / 'certify.py')
COVERAGE = str(HERE / 'check_coverage.py')
DEFAULT_ATTACK = (BASE / 'inputs' if (BASE / 'inputs').is_dir() else
                  HERE.parents[3] / 'institute/runs/hard-2026-10-15/problems/math-p0039/attack-e2')


def run(cmd, expect_ok, reason=None, timeout=290):
    began = time.monotonic()
    done = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    err = done.stderr.strip().splitlines()[-1] if done.stderr.strip() else ''
    if expect_ok:
        passed = done.returncode == 0
    else:
        passed = done.returncode == 1 and err.startswith('CHECK FAILED: ') and reason in err
    return dict(command=[Path(c).name if c in (PY, CERTIFY, COVERAGE) else c for c in cmd],
                expect='pass' if expect_ok else 'reject: ' + reason, returncode=done.returncode,
                stderr_last=err, passed=passed, seconds=round(time.monotonic() - began, 3))


def tiny(logs, run_dir):
    d = run_dir / 'tiny'
    d.mkdir(parents=True)
    receipt = d / 'tiny.json'
    out = [run([PY, CERTIFY, 'run', '--task', 'tiny', '--first', '0', '--last', '0',
                '--receipt', str(receipt), '--logs', logs], True)]
    r = json.loads(receipt.read_text())['blocks'][0]
    kinds = {x['n']: x['resolution'] for x in r['resolutions']}
    out.append(dict(command=['inspect ' + str(receipt.relative_to(BASE))], expect='survivors 2,8,24,90,512 resolved',
                    passed=r['survivors'] == [2, 8, 24, 90, 512] and kinds == {
                        2: 'classical-order-at-most-8', 8: 'classical-order-at-most-8',
                        24: 'difference-collision', 90: 'difference-collision',
                        512: 'difference-collision'}, observed=kinds))
    return out


def injections(receipts, logs):
    out = []
    io = ['--logs', logs]
    cases = [('tiny', 'q-equals-p', 'factor is not proper (q >= p) at n=2'),
             ('tiny', 'wrong-factor', 'factor mark does not divide p'),
             ('tiny', 'false-factor', 'factor mark does not divide p'),
             ('tiny', 'wrong-residue-sampled', 'libmpdec residue differs'),
             ('tiny', 'wrong-residue-unsampled', 'full decision digest differs from scan32'),
             ('tiny', 'expected-digest', 'full decision digest differs from scan32'),
             ('main', 'residue-one', 'unresolved base-two survivor'),
             ('main', 'false-factor', 'factor mark does not divide p'),
             ('main', 'wrong-residue-unsampled', 'full decision digest differs from scan32'),
             ('low', 'wrong-residue-unsampled', 'libmpdec residue differs')]
    for task, kind, reason in cases:  # no --receipt: these runs write nothing
        block = {'tiny': '0', 'main': '256', 'low': '0'}[task]
        out.append(run([PY, CERTIFY, 'run', '--task', task, '--first', block, '--last', block,
                        '--inject', kind] + io, False, reason))
    rep = [PY, CERTIFY, 'replay', '--receipts', receipts] + io
    out.append(run(rep + ['--task', 'low', '--blocks', '0'], True))
    out.append(run(rep + ['--task', 'low', '--blocks', '0', '--inject', 'stored-digest'],
                   False, 'recomputed block 0 differs from the stored receipt'))
    out.append(run(rep + ['--task', 'main', '--blocks', '256', '--inject', 'wrong-residue-unsampled'],
                   False, 'full decision digest differs from scan32'))
    return out


def read_receipts(src):
    """All receipts under src (per-chunk JSON or *.jsonl.gz), read only."""
    src = Path(src)
    rows = [json.loads(p.read_text()) for p in sorted(src.glob('*/*.json'))]
    for path in sorted(src.glob('*.jsonl.gz')):
        with gzip.open(path, 'rt') as f:
            rows.extend(json.loads(x) for x in f)
    return rows


def write_fixture(d, rows, omitted=None):
    d.mkdir(parents=True)
    raw = ''.join(json.dumps(r, separators=(',', ':')) + '\n' for r in rows).encode()
    (d / 'receipts.jsonl.gz').write_bytes(gzip.compress(raw, mtime=0))
    if omitted is not None:
        (d / 'OMITTED.json').write_text(json.dumps(omitted, indent=1) + '\n')


def coverage(receipts, attack, run_dir):
    base = [PY, COVERAGE, '--attack', attack, '--checker', CERTIFY]
    out = [run(base + ['--receipts', receipts], True)]  # the real receipts, read only
    rows = read_receipts(receipts)
    lows = sorted((r for r in rows if r['task'] == 'low'), key=lambda r: r['first'])
    mains = sorted((r for r in rows if r['task'] == 'main'), key=lambda r: r['first'])
    if len(lows) < 3 or not mains:
        return out + [dict(command=['coverage mutations'], passed=False, expect='needs low and main receipts')]
    reduced = lows + mains[:1]
    key = lambda r: (r['task'], r['first'])
    LOW0, LOWMID, MAIN0 = key(lows[0]), key(lows[1]), key(mains[0])
    root = run_dir / 'coverage'
    write_fixture(root / 'pristine', reduced)
    out.append(dict(run(base + ['--receipts', str(root / 'pristine')], True), mutation='pristine-reduced'))

    def pick(rs, k):
        return next(r for r in rs if key(r) == k)

    def drop(rs):
        victim = pick(rs, LOWMID)
        rs.remove(victim)
        return dict(omitted_receipt=dict(task=victim['task'], first=victim['first'], last=victim['last']),
                    note='simulated missing receipt: omitted from this copy; the real receipt is untouched')

    def dup(rs):
        r = copy.deepcopy(pick(rs, LOWMID))
        r['blocks'] = r['blocks'][:1]
        r['last'] = r['first']
        r['blocks'][0]['sha256'] = '1' * 64
        rs.insert(0, r)

    def shift(rs):
        pick(rs, LOWMID)['blocks'][0]['start'] += 24

    def checker(rs):
        pick(rs, LOWMID)['checker_sha256'] = '0' * 64

    def survivor(rs):
        b = pick(rs, MAIN0)['blocks'][0]
        b['survivors'] = [b['start']]

    def unresolved(rs):
        pick(rs, LOW0)['blocks'][0].pop('resolutions')

    def witness(rs):
        pick(rs, LOW0)['blocks'][0]['resolutions'][1]['pairs'][1][0] += 1

    def books(rs):
        pick(rs, LOWMID)['blocks'][0]['sieved'] += 1

    def digest(rs):
        pick(rs, MAIN0)['blocks'][0]['sha256'] = '2' * 64

    def mpdec(rs):
        pick(rs, LOWMID)['blocks'][0]['mpdec_residues'] = 0

    cases = [(drop, 'gap-free prefix ends at', ['--require-through', '200000000000']),
             (dup, 'conflicting duplicate block', []),
             (shift, 'block geometry differs', []),
             (checker, 'receipt from another checker', []),
             (survivor, 'survivor in', []),
             (unresolved, 'unresolved survivor', []),
             (witness, 'collision witness', []),
             (books, 'count bookkeeping', []),
             (digest, 'digest differs from a C log', []),
             (mpdec, 'libmpdec subset size', [])]
    for fn, reason, extra in cases:
        rs = copy.deepcopy(reduced)
        note = fn(rs)
        d = root / fn.__name__
        write_fixture(d, rs, note)
        row = run(base + ['--receipts', str(d)] + extra, False, reason)
        row['mutation'] = fn.__name__
        out.append(row)
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    p.add_argument('--group', choices=['tiny', 'injections', 'coverage', 'arithmetic', 'all'], default='all')
    p.add_argument('--receipts', default=str(BASE / 'receipts'))
    p.add_argument('--attack', default=str(DEFAULT_ATTACK), help='directory holding logs/ and evidence/epoch2/prefix-groups/')
    p.add_argument('--fixtures', default=str(BASE / 'controls' / 'fixtures'))
    p.add_argument('--output')
    args = p.parse_args()
    began = time.monotonic()
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-%d' % os.getpid()
    run_dir = Path(args.fixtures) / run_id
    run_dir.mkdir(parents=True)  # fails rather than reuse an existing run directory
    logs = str(Path(args.attack) / 'logs')
    rows = []
    if args.group in ('tiny', 'arithmetic', 'all'):
        rows += tiny(logs, run_dir)
    if args.group in ('injections', 'arithmetic', 'all'):
        rows += injections(args.receipts, logs)
    if args.group in ('coverage', 'all'):
        rows += coverage(args.receipts, args.attack, run_dir)
    result = dict(group=args.group, fixtures=str(run_dir), controls=rows, passed=sum(r['passed'] for r in rows),
                  total=len(rows), all_passed=all(r['passed'] for r in rows),
                  seconds=round(time.monotonic() - began, 3))
    text = json.dumps(result, indent=1)
    (run_dir / 'controls-result.json').write_text(text + '\n')
    if args.output:
        Path(args.output).write_text(text + '\n')
    print(text)
    sys.exit(0 if result['all_passed'] else 1)


if __name__ == '__main__':
    main()
