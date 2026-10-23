#!/usr/bin/env python3
"""Independent exact block certificate for math-p0039 (continuation 2026-10-15).

For every member n = start + step*i of a numbered block, this program proves
exactly one of the following with its own arithmetic:

  (F) q | p for the stored q, where p = n^2+n+1 and 1 < q < p (q is the
      smallest prime <= 10^6 dividing p), so p is composite; or
  (R) the complete ordinary residue r = 2^(n+1) mod p, and r != 1.

A member with neither (no prime factor <= 10^6 and r == 1) is a SURVIVOR and
makes its block fail.  Nothing from the earlier visit is imported and no
binary is executed.  Arithmetic used:

* primes: a numpy Eratosthenes sieve;
* roots of x^2+x+1 mod q: primitive cube roots of unity g^((q-1)/3)
  (q = 1 mod 3), the double root 1 (q = 3), and none otherwise (a root has
  multiplicative order 3, so 3 | q-1);
* every factor mark is re-verified member by member: (n mod q)^2+(n mod q)+1
  = 0 (mod q) in int64 arithmetic whose bounds are proved below, and q < p;
* every residue is CPython's arbitrary-precision pow(2, n+1, p);
* a deterministic subset of residues (every --mpdec-stride-th unsieved member,
  always including the first) is recomputed with the decimal module's
  libmpdec modular power, a separate arbitrary-precision library.

The 32-byte record of every member (n:u64, q:u32, tag:u32, residue:u128,
little endian; tag 1 factor with residue 0 meaning "not computed", tag 2
residue != 1, tag 3 residue == 1) is hashed exactly as in the preserved C
logs, and each block digest must equal BOTH preserved C digests.  The digest
comparison is a cross-implementation consistency check; the certificate is the
arithmetic above, never the stored hash.
"""
import argparse
import hashlib
import json
import os
import platform
import resource
import sys
import time
from datetime import datetime, timezone
from decimal import (Context, Decimal, DivisionByZero, Inexact, InvalidOperation,
                     Overflow, Rounded)
from math import isqrt
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]  # .../aifours
DEFAULT_LOGS = ROOT / 'institute/runs/hard-2026-10-15/problems/math-p0039/attack-e2/logs'
SCHEMA = 'math-p0039-cert-receipt/1'
SIEVE_BOUND = 1000000
SUBCHUNK = 1 << 20

# (start, stop, step, block_size) of the preserved C task scopes.
TASKS = {
    'tiny': (2, 20000, 2, 10000),
    'main': (200000000000, 2000000000000, 24, 8388608),
    'extension': (2000000000000, 4000000000000, 24, 8388608),
}
# SHA-256 of the preserved, read-only C block logs (attack-e2/logs).
LOG_SHA256 = {
    'e2-main-scan32.blocks.jsonl': '74e8a84b5bb34f26f00600ceb9570c942e922f92382a99d9de9981e4d1b0b036',
    'e2-main-scan128_digest.blocks.jsonl': 'ffae5842bae87f84eb35006c1a86e659b2e2888f8ac952980bf92c1217b12b0d',
    'e2-extension-scan32.blocks.jsonl': '3b54ff6b9a2e3d4bf2e7ca9f285cbac81f8b91160bd6c628a75e4f8cb2a858fd',
    'e2-extension-scan128_digest.blocks.jsonl': '0e61292cc48886e1ea35a5f47d528d583b006e552561600a2f98415b84156acf',
    'e2-tiny-scan32.blocks.jsonl': '30c5afe1fb21741c9ca8111bb610176846f8c3dda2a82405d0f1a35b7e200eb6',
    'e2-tiny-scan128_digest.blocks.jsonl': '2097d9db3f3e69e74aee0bf34398cc7280523b5038839f6a6d3ef93daf007982',
}
RECORD = np.dtype([('n', '<u8'), ('q', '<u4'), ('tag', '<u4'), ('lo', '<u8'), ('hi', '<u8')])
INJECTIONS = ('q-equals-p', 'wrong-factor', 'false-factor', 'wrong-residue-sampled',
              'wrong-residue-unsampled', 'residue-one', 'expected-digest')


class CheckFailed(Exception):
    pass


def need(ok, message):
    if not ok:
        raise CheckFailed(message)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def task_geometry(task):
    start, stop, step, size = TASKS[task]
    total = (stop - start + step - 1) // step
    return start, step, size, total, (total + size - 1) // size


def block_geometry(task, bid):
    start, step, size, total, nblocks = task_geometry(task)
    need(0 <= bid < nblocks, 'block id outside task: %s %d' % (task, bid))
    count = min(size, total - bid * size)
    first = start + step * bid * size
    return dict(id=bid, index=bid * size, start=first, end=first + step * count, count=count)


# ---------------------------------------------------------------- sieve ---

def primes_upto(bound):
    flags = np.ones(bound + 1, dtype=bool)
    flags[:2] = False
    for k in range(2, isqrt(bound) + 1):
        if flags[k]:
            flags[k * k::k] = False
    return [int(x) for x in np.flatnonzero(flags)]


def cubic_roots(q):
    """All roots of x^2+x+1 modulo the prime q."""
    if q == 2:
        return []  # x^2+x = x(x+1) is even, so x^2+x+1 is odd
    if q == 3:
        return [1]  # x^2+x+1 = (x-1)^2 mod 3
    if q % 3 == 2:
        return []  # a root has order 3 in F_q^*, forcing 3 | q-1
    g = 2
    while True:
        w = pow(g, (q - 1) // 3, q)
        if w != 1:
            break
        g += 1
    roots = [w, q - 1 - w]  # w^2 = -1-w
    need(roots[0] != roots[1], 'cube roots coincide')
    return roots


def root_classes(task, primes):
    """(q, class of the task index i, period) for every q | n_i^2+n_i+1."""
    start, step = TASKS[task][0], TASKS[task][2]
    rows = []
    for q in primes:
        roots = cubic_roots(q)
        for r in roots:
            need((r * r + r + 1) % q == 0, 'bad root %d mod %d' % (r, q))
        if step % q == 0:
            if start % q in roots:
                rows.append((q, 0, 1))
        else:
            inv = pow(step, q - 2, q)
            need(step * inv % q == 1, 'bad inverse')
            rows.extend((q, (r - start) * inv % q, q) for r in roots)
    rows.sort(key=lambda row: -row[0])  # descending: smaller q overwrite later
    return (np.array([r[0] for r in rows], dtype=np.int64),
            np.array([r[1] for r in rows], dtype=np.int64),
            np.array([r[2] for r in rows], dtype=np.int64))


def selftest(primes):
    """Brute-force the root sets for every prime < 3000 and the sieve rule."""
    for q in primes:
        if q >= 3000:
            break
        brute = sorted(x for x in range(q) if (x * x + x + 1) % q == 0)
        need(brute == sorted(cubic_roots(q)), 'root set differs from brute force at q=%d' % q)
    need(len(primes) == 78498 and primes[-1] == 999983, 'prime count below 10^6')
    return dict(primes=len(primes), brute_force_root_sets_below=3000)


# ------------------------------------------------------------- per block ---

def mark_block(classes, g):
    qs, cs, periods = classes
    firsts = ((cs - g['index']) % periods).tolist()
    q = np.zeros(g['count'], dtype=np.uint32)
    count = g['count']
    for qq, f, per in zip(qs.tolist(), firsts, periods.tolist()):
        if f < count:
            q[f::per] = qq
    return q


def certify_block(task, bid, classes, expected, mpdec_stride, inject=None):
    began = time.monotonic()
    g = block_geometry(task, bid)
    start, step, count = g['start'], TASKS[task][2], g['count']
    q = mark_block(classes, g)
    # Proper-divisor guard.  For n >= 1000, p = n^2+n+1 >= 1001001 > 10^6 >= q.
    # Only members n <= 999 can have p <= 10^6; they are checked exactly below.
    small = range(0) if start > 999 else range(min(count, (999 - start) // step + 1))
    for j in small:
        n = start + step * j
        if int(q[j]) == n * n + n + 1 and inject != 'q-equals-p':
            q[j] = 0  # p itself is a prime <= 10^6: not a proper factor
    if inject == 'wrong-factor':
        j = int(np.flatnonzero(q)[0]); n = start + step * j
        q[j] = next(x for x in (7, 13, 19, 31, 37) if (n * n + n + 1) % x and x != int(q[j]))
    if inject == 'false-factor':  # an unsieved member with p > 10^6, so only divisibility can fail
        j = int(next(x for x in np.flatnonzero(q == 0) if start + step * int(x) > 999)); n = start + step * j
        q[j] = next(x for x in (7, 13, 19, 31, 37) if (n * n + n + 1) % x)
    for j in small:
        n = start + step * j
        need(q[j] == 0 or int(q[j]) < n * n + n + 1, 'factor is not proper (q >= p) at n=%d' % n)
    need(start + step * (count - 1) < 1 << 42, 'int64 bound for factor verification')
    sieved = tested = mpdec = 0
    survivors = []
    ctx = Context(prec=80, traps=[Inexact, Rounded, InvalidOperation, Overflow, DivisionByZero])
    two = Decimal(2)
    digest = hashlib.sha256()
    for a in range(0, count, SUBCHUNK):
        b = min(count, a + SUBCHUNK)
        qs = q[a:b]
        # (F) member-by-member verification of every factor mark:
        # n < 2^42 and q <= 10^6 < 2^20 keep every int64 intermediate below 2^41.
        mk = np.flatnonzero(qs)
        nm = start + step * (mk.astype(np.int64) + a)
        qm = qs[mk].astype(np.int64)
        rm = nm % qm
        need(bool(np.all((rm * rm + rm + 1) % qm == 0)), 'factor mark does not divide p')
        need(bool(np.all(qm > 1)) and int(qm.max(initial=0)) <= SIEVE_BOUND, 'factor outside (1,10^6]')
        sieved += int(mk.size)
        del nm, qm, rm, mk
        rec = np.zeros(b - a, dtype=RECORD)
        rec['n'] = start + step * np.arange(a, b, dtype=np.uint64)
        rec['q'] = qs
        rec['tag'] = np.where(qs != 0, 1, 2)
        local = np.flatnonzero(qs == 0)
        ns = (start + step * (local.astype(np.int64) + a)).tolist()
        # (R) complete ordinary residues with CPython integers.
        res = [pow(2, n + 1, n * n + n + 1) for n in ns]
        if tested == 0 and len(res) > 1:
            if inject == 'wrong-residue-sampled':      # position 0 is in the libmpdec subset
                res[0] = (res[0] + 1) % (ns[0] * ns[0] + ns[0] + 1)
            elif inject == 'wrong-residue-unsampled':  # position 1 is not (stride > 1)
                res[1] = (res[1] + 1) % (ns[1] * ns[1] + ns[1] + 1)
            elif inject == 'residue-one':
                res[1] = 1
        # Separate libmpdec arithmetic on every mpdec_stride-th unsieved member.
        for k in range((-tested) % mpdec_stride, len(ns), mpdec_stride):
            n = ns[k]
            other = int(ctx.power(two, Decimal(n + 1), Decimal(n * n + n + 1)))
            need(other == res[k], 'libmpdec residue differs at n=%d' % n)
            mpdec += 1
        if res:
            packed = np.frombuffer(b''.join(r.to_bytes(16, 'little') for r in res),
                                   dtype='<u8').reshape(-1, 2)
            rec['lo'][local] = packed[:, 0]
            rec['hi'][local] = packed[:, 1]
            hit = np.flatnonzero((packed[:, 0] == 1) & (packed[:, 1] == 0))
            rec['tag'][local[hit]] = 3
            survivors.extend(ns[int(k)] for k in hit)
        tested += len(ns)
        digest.update(memoryview(rec))
        del rec, res, ns, local
    need(sieved + tested == count, 'sieved+tested != count')
    if task != 'tiny':  # the tiny control range contains the published small hits
        need(not survivors, 'unresolved base-two survivor %s' % survivors)
    sha = digest.hexdigest()
    row = dict(id=bid, start=g['start'], end=g['end'], count=count, sieved=sieved,
               tested=tested, survivors=survivors, sha256=sha, mpdec_residues=mpdec)
    # Cross-implementation consistency with both preserved C executions.
    for name, logged in expected.items():
        e = logged.get(bid)
        need(e is not None, '%s has no block %d' % (name, bid))
        want = '0' * 64 if inject == 'expected-digest' else e['decision_sha256']
        need((e['start'], e['end'], e['count']) == (g['start'], g['end'], count),
             'C block geometry differs at %d' % bid)
        need((e['sieved'], e['tested'], e['survivors']) == (sieved, tested, survivors),
             'C decision counts differ at block %d (%s)' % (bid, name))
        need(want == sha, 'full decision digest differs from %s at block %d' % (name, bid))
    row['seconds'] = round(time.monotonic() - began, 3)
    return row


# ----------------------------------------------------------- C log data ---

def load_expected(task, logs):
    out = {}
    for exe in ('scan32', 'scan128_digest'):
        name = 'e2-%s-%s.blocks.jsonl' % (task, exe)
        path = Path(logs) / name
        need(sha256_file(path) == LOG_SHA256[name], 'pinned C log hash differs: ' + name)
        rows = [json.loads(x) for x in path.read_text().splitlines() if x.strip()]
        h = rows[0]
        need(h['kind'] == 'header', 'C log header')
        need((h['start'], h['stop'], h['step'], h['block_size'], h['sieve_bound'])
             == TASKS[task] + (SIEVE_BOUND,), 'C log task scope differs')
        blocks = {}
        for r in rows[1:]:
            if r['kind'] == 'block':
                need(r['id'] not in blocks, 'duplicate C block')
                blocks[r['id']] = r
        out[exe] = blocks
    return out


def environment():
    import decimal
    try:
        import _decimal
    except ImportError:
        _decimal = None
    # The pure-Python _pydecimal would reuse CPython integers; require libmpdec.
    need(_decimal is not None and decimal.Decimal is _decimal.Decimal, 'decimal is not libmpdec-backed')
    rss_unit = 1 if sys.platform == 'darwin' else 1024
    return dict(python=sys.version.split()[0], implementation=platform.python_implementation(),
                numpy=np.__version__, platform=platform.platform(), machine=platform.machine(),
                libmpdec=getattr(decimal, '__libmpdec_version__', None), ru_maxrss_unit_bytes=rss_unit)


def run(args):
    began = time.monotonic()
    t0 = datetime.now(timezone.utc).isoformat()
    need(args.first <= args.last, 'empty block range')
    env = environment()
    primes = primes_upto(SIEVE_BOUND)
    test = selftest(primes)
    classes = root_classes(args.task, primes)
    expected = load_expected(args.task, args.logs)
    rows = []
    for bid in range(args.first, args.last + 1):
        rows.append(certify_block(args.task, bid, classes, expected, args.mpdec_stride, args.inject))
    receipt = dict(
        schema=SCHEMA, task=args.task, first=args.first, last=args.last,
        task_scope=dict(zip(('start', 'stop', 'step', 'block_size'), TASKS[args.task])),
        sieve_bound=SIEVE_BOUND, mpdec_stride=args.mpdec_stride,
        checker_sha256=sha256_file(__file__),
        c_logs={('e2-%s-%s.blocks.jsonl' % (args.task, e)): LOG_SHA256['e2-%s-%s.blocks.jsonl' % (args.task, e)]
                for e in ('scan32', 'scan128_digest')},
        selftest=test, blocks=rows,
        members=sum(r['count'] for r in rows), sieved=sum(r['sieved'] for r in rows),
        tested=sum(r['tested'] for r in rows), mpdec_residues=sum(r['mpdec_residues'] for r in rows),
        survivors=[n for r in rows for n in r['survivors']],
        interval=[rows[0]['start'], rows[-1]['end']],
        started_utc=t0, finished_utc=datetime.now(timezone.utc).isoformat(),
        seconds=round(time.monotonic() - began, 3),
        max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * env['ru_maxrss_unit_bytes'],
        environment=env, argv=sys.argv[1:])
    need(args.inject is None, 'injection %s was not detected' % args.inject)
    if args.receipt:
        path = Path(args.receipt)
        tmp = path.with_name(path.name + '.tmp-%d' % os.getpid())
        with open(tmp, 'w') as f:
            json.dump(receipt, f, separators=(',', ':'))
            f.write('\n')
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    summary = {k: receipt[k] for k in ('task', 'first', 'last', 'interval', 'members', 'sieved',
                                       'tested', 'mpdec_residues', 'survivors', 'seconds',
                                       'max_rss_bytes')}
    print(json.dumps(summary))


def replay(args):
    """Recompute blocks of an existing receipt and require identical results."""
    receipt = json.loads(Path(args.receipt).read_text())
    need(receipt['schema'] == SCHEMA, 'receipt schema')
    ids = ([int(x) for x in args.blocks.split(',')] if args.blocks
           else [r['id'] for r in receipt['blocks']])
    by_id = {r['id']: r for r in receipt['blocks']}
    environment()
    primes = primes_upto(SIEVE_BOUND)
    selftest(primes)
    classes = root_classes(receipt['task'], primes)
    expected = load_expected(receipt['task'], args.logs)
    out = []
    for bid in ids:
        need(bid in by_id, 'block %d is not in the receipt' % bid)
        row = certify_block(receipt['task'], bid, classes, expected, receipt['mpdec_stride'], args.inject)
        old = dict(by_id[bid])
        old.pop('seconds'); seconds = row.pop('seconds')
        need(row == old, 'recomputed block %d differs from the receipt' % bid)
        out.append(dict(id=bid, sha256=row['sha256'], seconds=seconds))
    need(args.inject is None, 'injection %s was not detected' % args.inject)
    print(json.dumps(dict(receipt=str(args.receipt), replayed=out, checker_sha256=sha256_file(__file__),
                          receipt_checker_sha256=receipt['checker_sha256'])))


def main():
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = p.add_subparsers(dest='action', required=True)
    r = sub.add_parser('run', help='certify blocks first..last and write a receipt')
    r.add_argument('--task', choices=sorted(TASKS), required=True)
    r.add_argument('--first', type=int, required=True)
    r.add_argument('--last', type=int, required=True)
    r.add_argument('--receipt')
    r.add_argument('--mpdec-stride', type=int, default=32)
    r.add_argument('--inject', choices=INJECTIONS)
    r.add_argument('--logs', default=str(DEFAULT_LOGS))
    v = sub.add_parser('replay', help='recompute blocks of a receipt')
    v.add_argument('receipt')
    v.add_argument('--blocks')
    v.add_argument('--inject', choices=INJECTIONS)
    v.add_argument('--logs', default=str(DEFAULT_LOGS))
    sub.add_parser('selftest', help='root sets and prime count only')
    args = p.parse_args()
    if args.action == 'run':
        need(args.mpdec_stride >= 1, 'mpdec stride')
        run(args)
    elif args.action == 'replay':
        replay(args)
    else:
        print(json.dumps(selftest(primes_upto(SIEVE_BOUND))))


if __name__ == '__main__':
    try:
        main()
    except CheckFailed as e:
        print('CHECK FAILED: ' + str(e), file=sys.stderr)
        sys.exit(1)
