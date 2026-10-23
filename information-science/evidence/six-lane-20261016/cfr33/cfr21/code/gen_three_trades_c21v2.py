#!/usr/bin/env python3
"""Exact one-3-value-trade neighbourhood of SUPPLIED normalized Z21 orthomorphisms.
Usage: gen_three_trades_c21v2.py OUTDIR SECONDS SOURCE_F1FILE [KNOWN_F1FILE ...]
F1 files: one line per map, values f(1)..f(20) (f(0)=0 implicit), as consumed by the
calibrated full-permutation engines. Preparation only; never searches for a CFR.

Version2 differs from v1 only in its inputs and quotient:
* sources are every map in SOURCE_F1FILE together with its complete R1 orbit;
* classes are the R1 group (A, I, unit conjugation, exactly v1's op/orbit code)
  EXTENDED by point translation T_e(f)(x)=f(x+e)-f(e). Closure is exact:
  A T_e = T_-e A, I T_e = T_f(e) I, C_u T_e = T_ue C_u. Each is a common DM column
  relabelling/normalization, so equivalent first rows have identical search outcome.
* classes of SOURCE or any KNOWN file are omitted explicitly, never silently.
A trade rotates the values at points a<b<c in either direction and is kept exactly
when the three differences with id keep their multiset; the result is renormalized.
Native deadline/SIGTERM produces PARTIAL output that is never called complete.
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

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
STOP = False
spec = importlib.util.spec_from_file_location('c21_trade_v1_ops', ROOT / 'code/gen_three_trades_c21v1.py')
v1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v1)


def stop(signum, frame):
    global STOP
    STOP = True


def clock():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read_f1(path):
    maps = []
    for line in Path(path).read_text().splitlines():
        if line.strip():
            f = tuple([0] + [int(v) for v in line.split()])
            if not v1.valid(f):
                raise ValueError('invalid normalized orthomorphism in ' + str(path))
            maps.append(f)
    return maps


CACHE = {}


def ext_class(f):
    if f in CACHE:
        return CACHE[f]
    _, members, _ = v1.orbit(f)
    images = {tuple((g[(x + e) % 21] - g[e]) % 21 for x in range(21)) for g in members for e in range(21)}
    rep = min(images)
    for g in images:
        if not v1.valid(g):
            raise AssertionError('extended image invalid')
        CACHE[g] = rep
    return rep


def main():
    out, seconds, source = Path(sys.argv[1]), float(sys.argv[2]), Path(sys.argv[3])
    known_files = [Path(p) for p in sys.argv[4:]]
    if not 0 < seconds <= 3600:
        raise SystemExit('bad preparation bound')
    os.mkdir(out)
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    t0 = time.monotonic()
    seeds = read_f1(source)
    sources = sorted({g for f in seeds for g in v1.orbit(f)[1]})
    omitted = {ext_class(f) for f in seeds}
    known = set()
    for p in known_files:
        known |= {ext_class(f) for f in read_f1(p)}
    omitted |= known
    retained, proposals, kept, why = {}, 0, 0, None
    triples = list(itertools.combinations(range(21), 3))
    for si, f in enumerate(sources):
        for points in triples:
            a, b, c = points
            old = sorted(((f[a] - a) % 21, (f[b] - b) % 21, (f[c] - c) % 21))
            for direction, values in enumerate(((f[b], f[c], f[a]), (f[c], f[a], f[b]))):
                if STOP or time.monotonic() - t0 >= seconds:
                    why = 'SIGTERM' if STOP else 'native preparation deadline'
                    break
                proposals += 1
                if sorted((v - x) % 21 for v, x in zip(values, points)) != old:
                    continue
                raw = list(f)
                for x, v in zip(points, values):
                    raw[x] = v
                traded = tuple((v - raw[0]) % 21 for v in raw)
                if not v1.valid(traded):
                    raise AssertionError('kept trade is not an orthomorphism')
                kept += 1
                rep = ext_class(traded)
                if rep not in omitted and rep not in retained:
                    retained[rep] = {'source_map': list(f[1:]), 'points': list(points), 'rotation': direction}
            if why:
                break
        if why:
            break
    reps = sorted(retained)
    with open(out / 'new-trade-classes.txt', 'x') as fh:
        fh.write(''.join(' '.join(map(str, f[1:])) + '\n' for f in reps))
    with open(out / 'provenance.json', 'x') as fh:
        json.dump([{'line': i + 1, 'f': list(f[1:]), **retained[f]} for i, f in enumerate(reps)], fh, indent=1)
    report = {'clock': clock(), 'program_sha256': sha(__file__), 'v1_ops_sha256': sha(ROOT / 'code/gen_three_trades_c21v1.py'),
              'source_file': str(source), 'source_sha256': sha(source),
              'known_files': {str(p): sha(p) for p in known_files}, 'seed_maps': len(seeds),
              'source_maps_with_R1_orbits': len(sources), 'proposals': proposals,
              'complete_proposal_count': len(sources) * len(triples) * 2, 'valid_trades': kept,
              'omitted_classes': len(omitted), 'new_extended_classes': len(reps),
              'status': 'COMPLETE FINITE GENERATION' if why is None else 'PARTIAL GENERATION: ' + why,
              'new_classes_sha256': sha(out / 'new-trade-classes.txt'), 'wall_s': time.monotonic() - t0,
              'scope': 'one3-value trade from supplied maps/R1 orbits; extended-class quotient; omits source/known classes'}
    with open(out / 'summary.json', 'x') as fh:
        json.dump(report, fh, indent=1)
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
