#!/usr/bin/env python3
"""Explicit finite 3-value-trade neighbourhood of the360 baseline P21 orthomorphisms.
Preparation only: writes f1 lists; never searches for a CFR. Native deadline/SIGTERM
or cache cap produces an explicitly labelled partial inventory, not full coverage.
Usage: gen_three_trades_c21v1.py OUTDIR [SECONDS=300]

For each baseline f, each a<b<c in Z21, rotate (f(a),f(b),f(c)) in either direction.
Keep iff the three differences with id have exactly their previous multiset;
outside these positions they are unchanged. Rotation preserves the value
permutation. Subtract the resulting value at0 to normalize, preserving every
row-pair permutation condition. Validate directly. Quotient by R1 (A,I,unit
conjugation) and retain the canonical function and a replay word.

Output NEW classes only, omitting the six baseline R1 classes already searched.
Their exclusion/reuse is explicit, not an unannounced assumption. This is only
one trade from a baseline map, never arbitrary orthomorphisms or whole CFRs.
"""
import hashlib
import itertools
import json
from math import gcd
import os
from pathlib import Path
import signal
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
STOP = False
CACHECAP = 200000


def stop(signum, frame):
    global STOP
    STOP = True


def clock():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def valid(f):
    return len(f) == 21 and f[0] == 0 and sorted(f) == list(range(21)) and len({(f[x] - x) % 21 for x in range(21)}) == 21


def op(f, name):
    if name == 'A':
        return tuple((f[-x % 21] + x) % 21 for x in range(21))
    if name == 'I':
        out = [0] * 21
        for x, y in enumerate(f):
            out[y] = x
        return tuple(out)
    u = int(name[1:])
    inv = pow(u, -1, 21)
    return tuple((u * f[inv * x % 21]) % 21 for x in range(21))


def orbit(seed):
    gens = ['A', 'I'] + ['C%d' % u for u in range(1, 21) if gcd(u, 21) == 1 and u != 1]
    parents = {seed: None}
    todo = [seed]
    for f in todo:
        for name in gens:
            g = op(f, name)
            if g not in parents:
                if not valid(g):
                    raise AssertionError('R1 image invalid')
                parents[g] = (f, name)
                todo.append(g)
                if len(parents) > 72:
                    raise AssertionError('R1 group size exceeds72')
    representative = min(parents)
    word, x = [], representative
    while parents[x] is not None:
        x, name = parents[x]
        word.append(name)
    return representative, parents, list(reversed(word))


def main():
    seconds = float(sys.argv[2]) if len(sys.argv) > 2 else 300.0
    out = Path(sys.argv[1])
    os.mkdir(out)
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    t0 = last = time.monotonic()
    source = ROOT / 'specs/full-seeds-v1/p21-detail.json'
    summary = ROOT / 'specs/full-seeds-v1/summary.json'
    detail = json.loads(source.read_text())
    expected = json.loads(summary.read_text())['files_sha256']['p21-detail.json']
    if sha(source) != expected:
        raise AssertionError('baseline provenance hash changed')
    functions = [tuple([0] + row['f']) for row in detail['inventory']]
    if len(functions) != 360 or any(not valid(f) for f in functions):
        raise AssertionError('baseline inventory is not360 valid functions')
    cache, baseline = {}, set()
    for f in functions:
        if f in cache:
            baseline.add(cache[f])
            continue
        rep, members, word = orbit(f)
        for g in members:
            cache[g] = rep
        baseline.add(rep)
    if len(baseline) != 6:
        raise AssertionError('baseline R1 count is not6')
    retained = {}
    proposals, trades, reused, cursor = 0, 0, 0, None
    why = None
    triples = list(itertools.combinations(range(21), 3))
    with open(out / 'progress.jsonl', 'x') as log:
        for si, f in enumerate(functions):
            for ti, points in enumerate(triples):
                a, b, c = points
                old = sorted(((f[a] - a) % 21, (f[b] - b) % 21, (f[c] - c) % 21))
                rotations = ((f[b], f[c], f[a]), (f[c], f[a], f[b]))
                for direction, values in enumerate(rotations):
                    cursor = [si, ti, direction]
                    if STOP or time.monotonic() - t0 >= seconds:
                        why = 'SIGTERM' if STOP else 'native preparation deadline'
                        break
                    proposals += 1
                    if sorted((v - x) % 21 for v, x in zip(values, points)) != old:
                        continue
                    raw = list(f)
                    for x, v in zip(points, values):
                        raw[x] = v
                    offset = raw[0]
                    traded = tuple((v - offset) % 21 for v in raw)
                    if not valid(traded):
                        raise AssertionError('kept trade is not an orthomorphism')
                    trades += 1
                    if traded in cache:
                        rep = cache[traded]
                        if rep in baseline:
                            reused += 1
                        continue
                    rep, members, word = orbit(traded)
                    if len(cache) + len(members) > CACHECAP:
                        why = 'R1 cache cap'
                        break
                    for g in members:
                        cache[g] = rep
                    if rep in baseline:
                        reused += 1
                        continue
                    if rep not in retained:
                        replay = traded
                        for name in word:
                            replay = op(replay, name)
                        if replay != rep:
                            raise AssertionError('provenance replay mismatch')
                        retained[rep] = {'source_inventory_index': si, 'source_occurrence': detail['inventory'][si]['occurrences'][0],
                                         'points': list(points), 'rotation': direction, 'normalizing_offset': offset,
                                         'word_from_trade': word, 'orbit_size': len(members)}
                if why:
                    break
            if why:
                break
            if time.monotonic() - last > 30:
                p = {'clock': clock(), 'source_maps_finished': si + 1, 'proposals': proposals,
                     'new_R1_representatives': len(retained), 'wall_s': time.monotonic() - t0}
                log.write(json.dumps(p) + '\n')
                log.flush()
                print(json.dumps(p), flush=True)
                last = time.monotonic()
    reps = sorted(retained)
    text = ''.join(' '.join(map(str, f[1:])) + '\n' for f in reps)
    with open(out / 'new-trade-R1-reps.txt', 'x') as file:
        file.write(text)
    with open(out / 'provenance.json', 'x') as file:
        json.dump([{'line': i + 1, 'f': list(f[1:]), **retained[f]} for i, f in enumerate(reps)], file, indent=1)
    report = {'clock': clock(), 'source_sha256': sha(source), 'program_sha256': sha(__file__),
              'preparation_limit_s': seconds, 'wall_s': time.monotonic() - t0,
              'source_functions': len(functions), 'source_R1_classes_reused': 6,
              'proposals': proposals, 'complete_proposal_count': 360 * 1330 * 2,
              'valid_trade_occurrences': trades, 'trades_reusing_baseline_classes': reused,
              'new_R1_representatives': len(reps), 'R1_cache_maps': len(cache), 'cursor': cursor,
              'status': 'COMPLETE FINITE GENERATION' if why is None else 'PARTIAL GENERATION: ' + why,
              'new_representatives_sha256': sha(out / 'new-trade-R1-reps.txt'),
              'scope': 'one3-value trade from a baseline inventory map, followed by R1; excludes reused baseline classes'}
    with open(out / 'summary.json', 'x') as file:
        json.dump(report, file, indent=1)
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
