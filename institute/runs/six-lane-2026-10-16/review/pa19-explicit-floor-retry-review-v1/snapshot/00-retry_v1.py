#!/usr/bin/env python3
"""One explicit parent-authorized re-attempt of PA19 M1 index 542 or 543.

No scientific evaluator is changed: execute the hash-pinned resolve_v4 source,
with isolated exclusive output paths and a stricter 17:57 stop. The earlier
UNKNOWN receipts stay immutable. Each index has exactly one new output directory;
repeated invocation refuses. Native launch additionally needs parent GO.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import types
from datetime import datetime
from zoneinfo import ZoneInfo

REVIEW = Path('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review')
DESK = REVIEW / 'pa19-explicit-floor-retry-v1'
OLD = REVIEW / 'pa19-final-stored-proof-replay-v1'
DRIVER = OLD / 'resolve_v4.py'
PLAN = OLD / 'resolve-plan-v2.jsonl'
PREVIOUS = OLD / 'RESOLVE-RESULT.json'
CONTROLS = OLD / 'resolve-controls-v2/RESULT-controls.json'
MONITOR = REVIEW / 'disk-monitor-v1-20261018T0722-to-1810.jsonl'
PINS = {
    DRIVER: 'f485b173f8bfe2bf1b2676a56fac6257de0e886881c2d87d13237eb6ac30eb9d',
    PLAN: '1ceb2204d9b72a139298c8f49958d91e14834cfcaf463cb7f0b3b8cbe3cbd38c',
    PREVIOUS: '3bcb6d583a6102f1370c43bb9dfe2fa2af76b8ae125a60eca59c3c2db0a4dc51',
    CONTROLS: 'fe5fdf607f7eb274a800ed92e81435385e3a6ace8974b5a9936b3ebd542a8e12',
}
TARGETS = {542: 'ms06_s00182', 543: 'ms06_s00183'}
TZ = ZoneInfo('America/Los_Angeles')
STOP_AT = datetime(2026, 10, 18, 17, 57, tzinfo=TZ).timestamp()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save(path, value):
    with path.open('x') as f:
        json.dump(value, f, indent=2, sort_keys=True)
        f.write('\n')


def authority(index):
    if index not in TARGETS:
        raise ValueError('only the two explicit floor-stop indices are authorized')
    raw = {p: p.read_bytes() for p in PINS}
    for p, expected in PINS.items():
        if sha(raw[p]) != expected:
            raise ValueError('immutable authority hash mismatch: ' + str(p))
    prior = json.loads(raw[PREVIOUS])
    unresolved = prior['unresolved']
    if len(unresolved) != 2 or {x['i'] for x in unresolved} != set(TARGETS):
        raise ValueError('previous result must name exactly the two floor UNKNOWNs')
    for x in unresolved:
        if (x['state'] != 'UNKNOWN' or x['tag'] != TARGETS[x['i']]
                or not any('disk_floor' in s for s in x['reasons'])):
            raise ValueError('previous UNKNOWN is not the authorized floor stop')
    plan = [json.loads(line) for line in raw[PLAN].splitlines()]
    if len(plan) != 737:
        raise ValueError('plan length mismatch')
    e = plan[index]
    if e['i'] != index or e['tag'] != TARGETS[index] or e['plan_state'] != 'READY':
        raise ValueError('selected original plan record mismatch')
    if e['source'] != 'base-file':
        raise ValueError('this authorization is for the two direct base-file records only')
    if not json.loads(raw[CONTROLS])['all_ok']:
        raise ValueError('original native controls did not pass')
    return raw[DRIVER], e


def stability(data, now):
    """Pure metadata gate; no polling, process creation or science here."""
    samples = []
    lines = data.split(b'\n')[:-1]  # an unterminated tail is not a record
    for line in lines:
        if not line.strip():
            continue
        obj = json.loads(line)
        if not isinstance(obj, dict):
            raise ValueError('monitor record must be an object')
        if 't' not in obj and 'free' not in obj:
            continue
        if 't' not in obj or type(obj.get('free')) is not int or obj['free'] < 0:
            raise ValueError('malformed monitor sample')
        stamp = datetime.fromisoformat(obj['t'])
        if stamp.utcoffset() is None:
            raise ValueError('monitor timestamp lacks timezone')
        if samples and stamp <= samples[-1][0]:
            raise ValueError('monitor timestamps are not strictly increasing')
        samples.append((stamp, obj['free']))
    if not samples:
        raise ValueError('monitor contains no complete samples')
    last, free = samples[-1]
    age = (now - last).total_seconds()
    window = [(t, f) for t, f in samples if 0 <= (last - t).total_seconds() <= 300]
    span = (window[-1][0] - window[0][0]).total_seconds()
    peak = window[0][1]
    drop = 0
    for _, val in window:
        drop = max(drop, peak - val)
        peak = max(peak, val)
    allowance = max(300000000, (free - 13500000000) // 12)
    ok = (0 <= age <= 30 and free >= 13500000000 and len(window) >= 25
          and span >= 290 and drop <= allowance)
    return {'ok': ok, 'last_sample': last.isoformat(), 'age_s': age,
            'free_last': free, 'samples': len(window), 'span_s': span,
            'max_drop': drop, 'drop_allowance': allowance}


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('index', type=int, choices=sorted(TARGETS))
    parser.add_argument('--check-only', action='store_true')
    args = parser.parse_args(argv)
    driver_bytes, entry = authority(args.index)
    if args.check_only:
        print(json.dumps({'authority': 'PASS', 'index': args.index, 'tag': entry['tag'],
                          'cnf_sha256': entry['expect_cnf_sha256'], 'wall_s': entry['wall_s']}))
        return
    out = DESK / ('index-%d-attempt-1' % args.index)
    out.mkdir(exist_ok=False)  # spent even on a later refusal; never auto-retry
    tmp = out / 'tmp'
    tmp.mkdir(exist_ok=False)
    mod = types.ModuleType('parent_frozen_resolve_v4')
    mod.__file__ = str(DRIVER)
    exec(compile(driver_bytes, str(DRIVER), 'exec'), mod.__dict__)
    mod.DESK, mod.TMP = str(out), str(tmp)
    mod.CHILD_ENV = dict(mod.CHILD_ENV, TMPDIR=str(tmp) + '/')
    mod.GLOBAL_STOP = STOP_AT
    original_resolve_one = mod.resolve_one

    def admitted_resolve_one(*call_args, **kwargs):
        # Called after original lane token/bigmem locks and before loading the
        # hash-pinned 1.5 MB base file; original fresh spawn gates still apply.
        try:
            decision = stability(MONITOR.read_bytes(), datetime.now(TZ))
        except Exception as error:
            decision = {'ok': False, 'error': repr(error)}
        decision['checked_at'] = datetime.now(TZ).isoformat()
        save(out / 'long-job-admission.json', decision)
        if not decision['ok']:
            return None, 'manual_retry_long_job_admission_refused'
        return original_resolve_one(*call_args, **kwargs)

    mod.resolve_one = admitted_resolve_one
    save(out / 'PRE-EXEC.json', {
        'at': datetime.now(TZ).isoformat(), 'index': args.index, 'tag': TARGETS[args.index],
        'wrapper': str(Path(__file__).resolve()), 'wrapper_sha256': sha(Path(__file__).read_bytes()),
        'frozen_driver_sha256': PINS[DRIVER], 'authority_pins': {str(p): v for p, v in PINS.items()},
        'original_plan_entry': entry, 'output_desk': str(out),
        'changes': ['isolated output paths', '17:57 native end', 'post-lock long-job metadata gate'],
        'no_claim': 'No old receipt is changed; result is one new attempt, not automatic retry or M2 evidence.'})
    os.chdir(tmp)
    os.environ['TMPDIR'] = str(tmp) + '/'
    os.nice(10)
    mod.install_signals()
    mod.cmd_run({'--lane': mod.LANE, '--plan': str(PLAN), '--plan-sha': PINS[PLAN],
                 '--script-sha': PINS[DRIVER], '--chunk': 'manual-floor-%d-a1' % args.index,
                 '--start': str(args.index), '--stop': str(args.index + 1), '--max-seconds': '10800'})


if __name__ == '__main__':
    main(sys.argv[1:])
