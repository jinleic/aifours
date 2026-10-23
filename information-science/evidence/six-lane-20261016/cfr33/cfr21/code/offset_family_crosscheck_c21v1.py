#!/usr/bin/env python3
"""Independent second-program check of the common-parallel-line CRT offset family.
Usage: offset_family_crosscheck_c21v1.py OUTDIR SECONDS [START_INDEX]
Does NOT read the generator, catalogue or C batch logic. From notes/offset-arcs-protocol-v1.txt
definitions only, it re-enumerates normalized offsets f(0)=f(1)=0 over F7, applies the
proved ARC fibre condition, the252-action group T(f)(i)=l*(f(a*i+b)-f(b)-i*(f(a+b)-f(b)))
and the six block rebasings, and selects pairs equal to their lexicographic minimum over
all1512 transforms, excluding pairs with both offsets in P23=span{i^2-i,i^3-i}.
Each selected beta is solved by the separately written primary lift solver
crt3_lift_c21v1.solve_pattern (Gaussian elimination plus exact inequality search), not the
Gray-code engine. The case count and splitmix64 key checksum are compared with the C batch;
the mixer constants are copied only to compare diagnostic digests. A candidate is checked on
all21 mod21 row pairs before exclusive output and exit10. Per-pattern limit10s; any limit or
SIGTERM is UNKNOWN and resumable at START_INDEX. All outputs exclusive; no native children.
"""
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import signal
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import numpy as np

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('c21_primary_lift_for_offset_crosscheck', ROOT / 'code/crt3_lift_c21v1.py')
lift = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lift)
M64 = (1 << 64) - 1


def mix64(z):
    z = (z + 0x9E3779B97F4A7C15) & M64
    z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & M64
    z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & M64
    return z ^ (z >> 31)


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def arc(f):
    return all(max(np.bincount([(f[i] - s * i) % 7 for i in range(7)], minlength=7)) <= 3 for s in range(7))


def main():
    out, seconds = Path(sys.argv[1]), float(sys.argv[2])
    start_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    if not 0 < seconds <= 10800 or start_index < 0:
        raise SystemExit('bad bounds')
    os.mkdir(out)
    signal.signal(signal.SIGTERM, lift.on_term)
    signal.signal(signal.SIGINT, lift.on_term)
    t0 = time.monotonic()
    funcs = [(0, 0) + tail for tail in itertools.product(range(7), repeat=5)]
    arcs = [f for f in funcs if arc(f)]
    index = {f: i for i, f in enumerate(arcs)}
    N = len(arcs)
    p23 = {tuple((u * (i * i - i) + v * (i ** 3 - i)) % 7 for i in range(7)) for u in range(7) for v in range(7)}
    actions = [(a, b, l) for a in range(1, 7) for b in range(7) for l in range(1, 7)]
    # Table: action x function id -> image id (ARC is preserved; asserted).
    table = np.empty((len(actions), N), dtype=np.int32)
    for g, (a, b, l) in enumerate(actions):
        for j, f in enumerate(arcs):
            image = tuple(l * (f[(a * i + b) % 7] - f[b] - i * (f[(a + b) % 7] - f[b])) % 7 for i in range(7))
            table[g, j] = index[image]
    first_reps = [j for j in range(N) if int(table[:, j].min()) == j]
    def diff_id(x, y):
        h = tuple((x[i] - y[i]) % 7 for i in range(7))
        return index.get(h, -1)
    zero_id = index.get((0,) * 7, -1)
    if zero_id != -1:
        raise AssertionError('zero offset unexpectedly ARC')
    cases = []
    excluded_p23 = 0
    for f1 in first_reps:
        for f2 in range(N):
            if diff_id(arcs[f1], arcs[f2]) < 0:
                continue
            canonical = True
            offs = (None, arcs[f1], arcs[f2])
            for order in itertools.permutations(range(3)):
                base = (0,) * 7 if order[0] == 0 else offs[order[0]]
                imgs = []
                for t in (order[1], order[2]):
                    src = (0,) * 7 if t == 0 else offs[t]
                    imgs.append(diff_id(src, base))
                if imgs[0] < 0 or imgs[1] < 0:
                    raise AssertionError('rebasing left the ARC set')
                x, y = table[:, imgs[0]], table[:, imgs[1]]
                better = (x < f1) | ((x == f1) & (y < f2))
                if better.any():
                    canonical = False
                    break
            if not canonical:
                continue
            if arcs[f1] in p23 and arcs[f2] in p23:
                excluded_p23 += 1
                continue
            cases.append(f1 * N + f2)
    checksum = 0
    for key in cases:
        checksum = (checksum + mix64(key)) & M64
    selection = {'N': N, 'first_representatives': len(first_reps), 'cases': len(cases), 'p23_excluded': excluded_p23,
                 'case_keys_checksum': '0x%016x' % checksum, 'selection_wall_s': time.monotonic() - t0}
    print(json.dumps(selection), flush=True)
    verdicts, unknown, candidate = {}, [], None
    last = time.monotonic()
    done = start_index
    with open(out / 'cases.jsonl', 'x') as log:
        for pos in range(start_index, len(cases)):
            if lift.STOP or time.monotonic() - t0 >= seconds:
                break
            key = cases[pos]
            f1, f2 = arcs[key // N], arcs[key % N]
            offsets = ((0,) * 7, f1, f2)
            beta = [[(i * c + offsets[t][i]) % 7 for t in range(3) for c in range(7)] for i in range(7)]
            rec, dm = lift.solve_pattern(7, beta, min(10.0, seconds - (time.monotonic() - t0)))
            verdicts[rec['verdict']] = verdicts.get(rec['verdict'], 0) + 1
            if rec['verdict'] not in ('EXHAUSTED-PATTERN', 'CANDIDATE'):
                unknown.append(key)
                log.write(json.dumps({'pos': pos, 'key': key, 'verdict': rec['verdict']}) + '\n')
                log.flush()
            done = pos + 1
            if dm is not None:
                if not lift.dm_ok(dm, 21):
                    raise AssertionError('candidate failed direct DM definition')
                with open(out / 'candidate.dmraw', 'x') as fh:
                    fh.write(''.join(' '.join(map(str, row)) + '\n' for row in dm))
                candidate = {'key': key, 'f1': list(f1), 'f2': list(f2), 'sha256': sha(out / 'candidate.dmraw')}
                break
            if time.monotonic() - last >= 300:
                last = time.monotonic()
                print(json.dumps({'clock': stamp(), 'done': done, 'of': len(cases), 'verdicts': verdicts}), flush=True)
    complete = candidate is None and done == len(cases) and not unknown and start_index == 0
    status = ('CANDIDATE' if candidate else 'FAMILY-ZERO-SECOND-PROGRAM' if complete else 'UNKNOWN-INCOMPLETE')
    rec = {'clock': stamp(), 'program_sha256': sha(__file__), 'lift_solver_sha256': sha(ROOT / 'code/crt3_lift_c21v1.py'),
           'selection': selection, 'start_index': start_index, 'resume_index': done, 'verdicts': verdicts,
           'unknown_keys': unknown, 'candidate': candidate, 'status': status, 'signal': lift.STOP,
           'wall_s': time.monotonic() - t0,
           'scope': 'restricted common-parallel-line CRT family only; never unrestricted CFR6,21'}
    with open(out / 'record.json', 'x') as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec), flush=True)
    raise SystemExit(10 if candidate else 20 if complete else 0)


if __name__ == '__main__':
    main()
