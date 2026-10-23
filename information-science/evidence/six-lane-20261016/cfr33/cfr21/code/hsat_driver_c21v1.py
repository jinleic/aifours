#!/usr/bin/env python3
"""Per-canonical-H SAT completion of the remaining pure row-action models (g06, g00, g10).
Usage: hsat_driver_c21v1.py OUTDIR MODEL N MU HLIST SECONDS PER_H_SECONDS [START_INDEX [all]]
The optional literal 'all' is for small calibration only: continue after SAT, writing
candidate-ORDINAL.dmraw for every SAT H, so per-H verdicts can be compared exactly.
MODEL cycle3: rows 0, t, mu*h^2(t), mu^2*h(t), g(t), mu*g(h^2(t)), mu^2*g(h(t)).
MODEL involution: rows 0, t, mu*h(t), g(t), mu*g(h(t)), j(t), mu*j(h(t)).
HLIST is the stdout of cycle3_pair_c21v4/involution_pair_c21v4 hlist mode: every canonical
column action H in the enumerators' calibrated deterministic order ('c hl ORD h ...').
Completeness per model is exactly the enumerators' (normal form, affine-canonical H, primary
gauge g(0)=j(0)=0); see their headers. This program adds NO pruning: for each H it encodes ALL
21 row pairs directly (one-hot values, a one-hot difference table for each unknown/unknown
pair with forward links, at-most-one for each known/unknown difference value) and asks native
CaDiCaL (stdin, -t PER_H) whether any g (and j) exists. The CNF lives only in RAM.
SAT: decode, rebuild the full DM, check all pairs mod N, exclusive candidate.dmraw, exit10.
UNSAT: uncertified solver claim for that H. Timeout/signal: UNKNOWN registry line; the model
stays UNKNOWN. Completed ordinals are contiguous from START_ORDINAL; resume at resume_ordinal.
One native child at a time; SIGTERM is forwarded; no Python timeout, kill or SIGKILL.
"""
import hashlib
from math import gcd
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

STOP = False
CHILD = None
FLOOR = 12_000_000_000


def term(signum, frame):
    global STOP
    STOP = True
    if CHILD is not None:
        try:
            CHILD.send_signal(signal.SIGTERM)
        except ProcessLookupError:
            pass


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dm_ok(D, n):
    return all(sorted((D[i][t] - D[j][t]) % n for t in range(n)) == list(range(n)) for i in range(len(D)) for j in range(i))


def rows_spec(model, n, mu, h):
    """Each row: ('K', values) or ('U', map, column permutation, scale)."""
    ident = list(range(n))
    h2 = [h[h[t]] for t in range(n)]
    mu2 = mu * mu % n
    if model == 'cycle3':
        if any(h[h2[t]] != t for t in range(n)):
            raise ValueError('h^3 != id')
        return 1, [('K', [0] * n), ('K', ident), ('K', [mu * h2[t] % n for t in range(n)]),
                   ('K', [mu2 * h[t] % n for t in range(n)]),
                   ('U', 0, ident, 1), ('U', 0, h2, mu), ('U', 0, list(h), mu2)]
    if model == 'involution':
        if any(h2[t] != t for t in range(n)) or h[0] != 0:
            raise ValueError('h is not an involution fixing0')
        return 2, [('K', [0] * n), ('K', ident), ('K', [mu * h[t] % n for t in range(n)]),
                   ('U', 0, ident, 1), ('U', 0, list(h), mu), ('U', 1, ident, 1), ('U', 1, list(h), mu)]
    raise ValueError('unknown model')


STATIC = {}


def static_block(model, n, m, rows):
    """H-independent clauses: one-hot maps/gauges and one-hot difference tables.
    Table numbering follows the fixed unknown/unknown pair order, independent of h."""
    key = (model, n, m)
    if key in STATIC:
        return STATIC[key]
    lines, nv, bases = [], m * n * n, {}
    def emit(vs):
        lines.append(' '.join(map(str, vs)) + ' 0\n')
    def one(vs):
        emit(vs)
        for a in range(len(vs)):
            for b in range(a):
                emit([-vs[a], -vs[b]])
    for mm in range(m):
        for t in range(n):
            one([1 + mm * n * n + t * n + v for v in range(n)])
        for v in range(n):
            one([1 + mm * n * n + t * n + v for t in range(n)])
        emit([1 + mm * n * n])  # primary gauge F(0)=0
    for i in range(len(rows)):
        for j in range(i):
            if rows[i][0] == 'U' and rows[j][0] == 'U':
                bases[i, j] = nv
                for t in range(n):
                    one([1 + nv + t * n + w for w in range(n)])
                for w in range(n):
                    vs = [1 + nv + t * n + w for t in range(n)]
                    for a in range(len(vs)):
                        for b in range(a):
                            emit([-vs[a], -vs[b]])
                nv += n * n
    STATIC[key] = (''.join(lines), len(lines), nv, bases)
    return STATIC[key]


def encode(model, n, mu, h):
    m, rows = rows_spec(model, n, mu, h)
    known = [r for r in rows if r[0] == 'K']
    for i in range(len(known)):
        for j in range(i):
            if sorted((known[i][1][t] - known[j][1][t]) % n for t in range(n)) != list(range(n)):
                raise ValueError('invalid canonical H: known rows are not a DM')
    static, nstatic, nv, bases = static_block(model, n, m, rows)
    inv = {s: pow(s, -1, n) for s in range(1, n) if gcd(s, n) == 1}
    def X(mm, t, v):
        return 1 + mm * n * n + t * n + v
    def lit(row, t, value):
        _, mm, perm, scale = row
        return X(mm, perm[t], inv[scale] * value % n)
    out = []
    for i in range(len(rows)):
        for j in range(i):
            ri, rj = rows[i], rows[j]
            if ri[0] == 'K' and rj[0] == 'K':
                continue
            if ri[0] == 'K' or rj[0] == 'K':
                kr, ur = (ri, rj) if ri[0] == 'K' else (rj, ri)
                for w in range(n):
                    vs = [lit(ur, t, (w + kr[1][t]) % n) for t in range(n)]
                    for a in range(n):
                        for b in range(a):
                            out.append('-%d -%d 0\n' % (vs[a], vs[b]))
                continue
            base = bases[i, j]
            for t in range(n):
                if ri[1] == rj[1] and ri[2][t] == rj[2][t]:
                    for v in range(n):
                        out.append('-%d %d 0\n' % (X(ri[1], ri[2][t], v), 1 + base + t * n + (ri[3] - rj[3]) * v % n))
                else:
                    las = [lit(ri, t, a) for a in range(n)]
                    lbs = [lit(rj, t, b) for b in range(n)]
                    for a in range(n):
                        for b in range(n):
                            out.append('-%d -%d %d 0\n' % (las[a], lbs[b], 1 + base + t * n + (a - b) % n))
    text = 'p cnf %d %d\n' % (nv, nstatic + len(out)) + static + ''.join(out)
    return text.encode('ascii'), m, rows


def decode(output, m, rows, n):
    values = {}
    for line in output.splitlines():
        if line.startswith('v '):
            for tok in line.split()[1:]:
                z = int(tok)
                if z:
                    values[abs(z)] = z > 0
    maps = []
    for mm in range(m):
        f = []
        for t in range(n):
            vs = [v for v in range(n) if values.get(1 + mm * n * n + t * n + v)]
            if len(vs) != 1:
                raise ValueError('assignment not one-hot')
            f.append(vs[0])
        maps.append(f)
    D = []
    for r in rows:
        if r[0] == 'K':
            D.append(list(r[1]))
        else:
            _, mm, perm, scale = r
            D.append([scale * maps[mm][perm[t]] % n for t in range(n)])
    return D


def main():
    global CHILD
    out, model, n, mu = Path(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    hlist, seconds, per_h = Path(sys.argv[5]), float(sys.argv[6]), int(sys.argv[7])
    start = int(sys.argv[8]) if len(sys.argv) > 8 else 0
    all_mode = len(sys.argv) > 9 and sys.argv[9] == 'all'
    if len(sys.argv) > 10 or (len(sys.argv) > 9 and not all_mode):
        raise SystemExit('bad trailing arguments')
    if not 0 < seconds <= 10800 or not 1 <= per_h <= 3600 or start < 0:
        raise SystemExit('bad bounds')
    os.mkdir(out)
    signal.signal(signal.SIGTERM, term)
    signal.signal(signal.SIGINT, term)
    solver = shutil.which('cadical')
    hs = []
    for line in hlist.read_text().splitlines():
        if line.startswith('c hl '):
            parts = line.split()
            hs.append((int(parts[2]), [int(x) for x in parts[4:]]))
    if not hs or any(len(h) != n or sorted(h) != list(range(n)) for _, h in hs):
        raise SystemExit('bad H list')
    ords = [o for o, _ in hs]
    if ords != list(range(ords[0], ords[0] + len(ords))):
        raise SystemExit('H ordinals not contiguous')
    t0, last = time.monotonic(), time.monotonic()
    meta = {'clock': stamp(), 'program_sha256': sha(__file__), 'model': model, 'n': n, 'mu': mu,
            'hlist': str(hlist), 'hlist_sha256': sha(hlist), 'h_total': len(hs), 'first_ordinal': ords[0],
            'start_index': start, 'per_h_seconds': per_h, 'seconds': seconds, 'solver_sha256': sha(solver),
            'calibration_all_mode': all_mode}
    with open(out / 'start.json', 'x') as f:
        json.dump(meta, f, indent=1)
    counts, unknown, candidate, done, stop_reason, sat_ordinals = {}, [], None, start, None, []
    with open(out / 'results.jsonl', 'x') as log:
        for idx in range(start, len(hs)):
            if STOP or time.monotonic() - t0 >= seconds:
                stop_reason = 'SIGTERM' if STOP else 'wall limit'
                break
            st = os.statvfs(out)
            if st.f_bavail * st.f_frsize < FLOOR + 64 * 1024 ** 2:
                stop_reason = 'disk floor margin'
                break
            ordinal, h = hs[idx]
            cnf, m, rows = encode(model, n, mu, h)
            begin = time.monotonic()
            CHILD = subprocess.Popen([solver, '--seed=1', '-t', str(per_h), '-'], stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output, _ = CHILD.communicate(cnf)
            rc = CHILD.returncode
            CHILD = None
            text = output.decode('ascii', 'replace')
            status = [l.strip() for l in text.splitlines() if l.startswith('s ')]
            if STOP and rc not in (10, 20):
                stop_reason = 'SIGTERM during H'
                break
            if rc == 10 and status == ['s SATISFIABLE']:
                D = decode(text, m, rows, n)
                if not dm_ok(D, n):
                    raise AssertionError('decoded assignment fails the DM definition')
                name = 'candidate-%d.dmraw' % ordinal if all_mode else 'candidate.dmraw'
                with open(out / name, 'x') as f:
                    f.write(''.join(' '.join(map(str, r)) + '\n' for r in D))
                sat_ordinals.append(ordinal)
                if not all_mode:
                    candidate = {'ordinal': ordinal, 'h': h, 'sha256': sha(out / name)}
                verdict = 'SAT-DM-VERIFIED'
            elif rc == 20 and status == ['s UNSATISFIABLE']:
                verdict = 'UNSAT-CLAIM'
            else:
                verdict = 'UNKNOWN'
                unknown.append(ordinal)
            counts[verdict] = counts.get(verdict, 0) + 1
            log.write(json.dumps({'ordinal': ordinal, 'verdict': verdict, 'rc': rc, 'wall_s': round(time.monotonic() - begin, 4),
                                  'cnf_sha256': hashlib.sha256(cnf).hexdigest()}) + '\n')
            log.flush()
            done = idx + 1
            if candidate:
                break
            if time.monotonic() - last >= 300:
                last = time.monotonic()
                print(json.dumps({'clock': stamp(), 'done_index': done, 'of': len(hs), 'counts': counts}), flush=True)
    complete = candidate is None and done == len(hs) and not unknown and not sat_ordinals
    status = ('CANDIDATE' if candidate else
              ('CALIBRATION-ALL-MODE-SAT-FOUND' + ('' if done == len(hs) and not unknown else '-INCOMPLETE')) if sat_ordinals else
              'ALL-H-UNSAT-CLAIMS' if complete and start == 0 else
              'RANGE-ALL-UNSAT-CLAIMS' if complete else 'UNKNOWN-INCOMPLETE')
    rec = {**meta, 'end_clock': stamp(), 'wall_s': time.monotonic() - t0, 'done_index': done,
           'resume_index': done, 'counts': counts, 'unknown_ordinals': unknown, 'candidate': candidate,
           'sat_ordinals': sat_ordinals,
           'status': status, 'signal': STOP, 'stop_reason': stop_reason,
           'scope': 'restricted pure row-action model only; UNSAT are uncertified solver claims'}
    with open(out / 'record.json', 'x') as f:
        json.dump(rec, f, indent=1)
    print(json.dumps(rec), flush=True)
    raise SystemExit(10 if candidate or sat_ordinals else 20 if complete else 0)


if __name__ == '__main__':
    main()
