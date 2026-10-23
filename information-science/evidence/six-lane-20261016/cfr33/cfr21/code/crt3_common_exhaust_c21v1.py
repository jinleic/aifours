#!/usr/bin/env python3
"""Finite common-slope polynomial CRT family, exactly2401 beta patterns.
Usage: crt3_common_exhaust_c21v1.py START STOP SECONDS OUTDIR
0<=START<=STOP<=2401, lexicographic index of (u1,v1,u2,v2) in F7^4.
For row i, block t, c in F7:
 beta_i(0,c)=i*c;
 beta_i(t,c)=i*c+u_t*(i^2-i)+v_t*(i^3-i) mod7, t=1,2.
This is precisely family2 of crt3_affine_sample_c21v1.py, not all CRT patterns.
Each pattern is passed to the calibrated exact F3 lift solver, with10s maximum
per pattern and the remaining chunk deadline. Timed-out patterns remain UNKNOWN
and their inputs are preserved. A complete zero-result scan is one-program
restricted evidence until independently cross-checked, not CFR nonexistence.
Every output uses exclusive creation. SIGTERM retains settled cases and record.
"""
import collections
import hashlib
import itertools
import json
import os
from pathlib import Path
import signal
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import crt3_lift_c21v1 as lift


def clock():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def pattern(coefs):
    u1, v1, u2, v2 = coefs
    offsets = [[0] * 7]
    for u, v in ((u1, v1), (u2, v2)):
        offsets.append([(u * (i * i - i) + v * (i ** 3 - i)) % 7 for i in range(7)])
    beta = [[(i * c + offsets[t][i]) % 7 for t in range(3) for c in range(7)] for i in range(7)]
    return {'q': 7, 'beta': beta, 'coefficients': list(coefs), 'family': 'common-slope-polynomial23'}


def main():
    start, stop, seconds, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    if not (0 <= start <= stop <= 2401):
        raise SystemExit('bad range')
    os.mkdir(out)
    signal.signal(signal.SIGTERM, lift.on_term)
    signal.signal(signal.SIGINT, lift.on_term)
    combos = list(itertools.product(range(7), repeat=4))
    # Independent cardinality check of the polynomial coefficient parametrisation.
    fingerprints = {tuple(x for row in pattern(cs)['beta'] for x in row) for cs in combos}
    if len(fingerprints) != 2401:
        raise AssertionError('not2401 distinct patterns')
    del fingerprints
    t0 = last = time.monotonic()
    metadata = {'clock': clock(), 'start': start, 'stop': stop, 'total_family': 2401, 'seconds': seconds,
                'program_sha256': sha(__file__), 'solver_sha256': sha(lift.__file__)}
    with open(out + '/start.json', 'x') as f:
        json.dump(metadata, f, indent=1)
    hist, verdicts = collections.Counter(), collections.Counter()
    settled, unknown = [], []
    candidate = False
    with open(out + '/cases.jsonl', 'x') as cases:
        for index in range(start, stop):
            if lift.STOP or time.monotonic() - t0 >= seconds:
                break
            obj = pattern(combos[index])
            rec, dm = lift.solve_pattern(7, obj['beta'], min(10.0, seconds - (time.monotonic() - t0)))
            rec.update(index=index, coefficients=list(combos[index]), clock=clock())
            if index == 0 and (rec['rank'], rec['kernel_dimension'], rec['verdict']) != (42, 78, 'EXHAUSTED-PATTERN'):
                raise AssertionError('known repeated-field negative control mismatch')
            cases.write(json.dumps(rec) + '\n')
            cases.flush()
            settled.append(index)
            verdicts[rec['verdict']] += 1
            hist[(rec['kernel_dimension'], rec.get('inequality_rank'), rec['verdict'])] += 1
            if rec['verdict'] == 'UNKNOWN':
                unknown.append(index)
                with open(out + '/unknown-%04d.json' % index, 'x') as f:
                    json.dump(obj, f)
            if dm is not None:
                with open(out + '/pattern.json', 'x') as f:
                    json.dump(obj, f, indent=1)
                rec['pattern_sha256'] = sha(out + '/pattern.json')
                lift.write_solution(out + '/candidate', rec, dm)
                candidate = True
                break
            if time.monotonic() - last >= 30:
                print(json.dumps({'clock': clock(), 'cases': len(settled), 'last_index': index,
                                  'wall_s': time.monotonic() - t0, 'verdicts': dict(verdicts)}), flush=True)
                last = time.monotonic()
    complete = len(settled) == stop - start and not unknown
    status = ('CANDIDATE' if candidate else
              'EXHAUSTED-RESTRICTED (one-program evidence; independent cross-check pending)' if complete and start == 0 and stop == 2401 else
              'RANGE-COMPLETE (restricted range only)' if complete else 'UNKNOWN (unfinished cases retained)')
    final = {**metadata, 'end_clock': clock(), 'wall_s': time.monotonic() - t0, 'settled_cases': len(settled),
             'last_index': settled[-1] if settled else None, 'unknown_indices': unknown, 'verdicts': dict(verdicts),
             'histogram': [{'signature': key, 'count': count} for key, count in sorted(hist.items(), key=lambda kv: str(kv[0]))],
             'status': status, 'signal': lift.STOP}
    with open(out + '/record.json', 'x') as f:
        json.dump(final, f, indent=1)
    print(json.dumps(final), flush=True)
    raise SystemExit(10 if candidate else 20 if complete and start == 0 and stop == 2401 else 0)


if __name__ == '__main__':
    main()
