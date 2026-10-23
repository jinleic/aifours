#!/usr/bin/env python3
"""Staged base-b Fermat test of p_t = 2^(2a)+2^a+1, a = 3^t (math-p0039 power-of-two family).

If p_t were prime, b^(p_t-1) = 1 (mod p_t) for gcd(b, p_t) = 1 (Fermat).  A residue
other than 1 is therefore an exact proof that p_t is composite, so (Kantor /
Thas-Zagier: p must be prime) n = 2^a is not the order of a non-Desarguesian
flag-transitive plane.  Base 2 is useless: 2 has order 3a | n+1 | p_t - 1 modulo
p_t, so 2^(p_t-1) = 1 always (shown by the `liar` control).

Arithmetic: CPython integers modulo M = 2^(3a) - 1 = (2^a - 1) p_t, reduced by
the identity 2^(3a) = 1 (mod M); the final residue is reduced mod p_t.  The
exponent p_t - 1 = 2^(2a) + 2^a has two one-bits, so left-to-right binary
exponentiation is 2a squarings and two multiplications by b.  Work is split into
stages, each a separate command below 300 s, with gzip checkpoints of the full
residue mod M.  Re-running a stage whose checkpoint exists recomputes it from
the previous checkpoint and must reproduce it byte for byte.
"""
import argparse
import gzip
import hashlib
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def need(ok, message):
    if not ok:
        raise ValueError(message)


def params(t):
    a = 3 ** t
    return a, (1 << 3 * a) - 1, (1 << 2 * a) + (1 << a) + 1


def reduce(x, a, M):
    L = 3 * a
    x = (x & M) + (x >> L)
    x = (x & M) + (x >> L)
    return x - M if x >= M else x


def steps(a):
    """Exponent bits of p-1 = 2^(2a)+2^a from the top: index i in [0, 2a] is bit 2a-i."""
    return 2 * a + 1


def advance(r, i0, i1, a, M, b):
    for i in range(i0, i1):
        bit = 2 * a - i
        r = reduce(r * r, a, M)
        if bit == 2 * a or bit == a:
            r = reduce(r * b, a, M)
    return r


def ckpt_path(d, t, b, k):
    return Path(d) / ('t%02d-b%d-stage%02d.gz' % (t, b, k))


def load(path, a):
    data = gzip.decompress(Path(path).read_bytes())
    need(len(data) == (3 * a + 7) // 8, 'checkpoint width')
    return int.from_bytes(data, 'little')


def dump(path, r, a):
    raw = r.to_bytes((3 * a + 7) // 8, 'little')
    Path(path).write_bytes(gzip.compress(raw, mtime=0))
    return hashlib.sha256(raw).hexdigest()


def stage(args):
    a, M, p = params(args.t)
    total = steps(a)
    bounds = [total * k // args.stages for k in range(args.stages + 1)]
    k = args.stage
    need(0 <= k < args.stages, 'stage index')
    r = 1 if k == 0 else load(ckpt_path(args.dir, args.t, args.base, k - 1), a)
    began = time.monotonic()
    r = advance(r, bounds[k], bounds[k + 1], a, M, args.base)
    out = ckpt_path(args.dir, args.t, args.base, k)
    raw = r.to_bytes((3 * a + 7) // 8, 'little')
    digest = hashlib.sha256(raw).hexdigest()
    if out.exists():
        need(gzip.decompress(out.read_bytes()) == raw, 'stage %d does not reproduce its checkpoint' % k)
        mode = 'replayed'
    else:
        Path(args.dir).mkdir(parents=True, exist_ok=True)
        dump(out, r, a)
        mode = 'written'
    print(json.dumps(dict(t=args.t, a=a, base=args.base, stage=k, of=args.stages, bits=[bounds[k], bounds[k + 1]],
                          residue_mod_M_sha256=digest, mode=mode, seconds=round(time.monotonic() - began, 3))))


def final(args):
    a, M, p = params(args.t)
    r = load(ckpt_path(args.dir, args.t, args.base, args.stages - 1), a) % p
    need(p % args.base != 0, 'base divides p')
    composite = r != 1
    out = dict(t=args.t, a=a, n='2^%d' % a, p_bits=p.bit_length(), base=args.base,
               fermat_residue_low64=r & ((1 << 64) - 1), fermat_residue_sha256=hashlib.sha256(
                   r.to_bytes((p.bit_length() + 7) // 8, 'little')).hexdigest(),
               composite=composite,
               conclusion=('p_t is composite (Fermat witness), so n = 2^a is excluded under the premises'
                           if composite else 'no conclusion: residue 1 (p_t may be prime)'))
    if args.output:
        Path(args.output).write_text(json.dumps(out, indent=1) + '\n')
    print(json.dumps(out))


def controls(args):
    """Small t: staged result equals pow(); t=2 (prime 262657) gives 1; base 2 is a liar."""
    rows = []
    for t in range(1, args.max_t + 1):
        a, M, p = params(t)
        r = advance(1, 0, steps(a), a, M, 3) % p
        need(r == pow(3, p - 1, p), 'staged arithmetic differs from pow at t=%d' % t)
        liar = pow(2, p - 1, p) == 1
        need(liar, 'base 2 not a Fermat liar at t=%d' % t)
        rows.append(dict(t=t, a=a, p_bits=p.bit_length(), base3_residue_is_1=r == 1, base2_liar=liar))
    need([r['base3_residue_is_1'] for r in rows][:2] == [True, True], 't=1,2 (p=73, 262657) are prime')
    need(not rows[2]['base3_residue_is_1'], 't=3: p = 2593*71119*97685839 must fail')
    print(json.dumps(dict(controls=rows)))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='action', required=True)
    for name in ('stage', 'final'):
        s = sub.add_parser(name)
        s.add_argument('--t', type=int, required=True)
        s.add_argument('--base', type=int, default=3)
        s.add_argument('--stages', type=int, default=4)
        s.add_argument('--dir', default=str(BASE / 'evidence' / 'fermat'))
        if name == 'stage':
            s.add_argument('--stage', type=int, required=True)
        else:
            s.add_argument('--output')
    c = sub.add_parser('controls')
    c.add_argument('--max-t', type=int, default=6)
    args = ap.parse_args()
    {'stage': stage, 'final': final, 'controls': controls}[args.action](args)


if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print('CHECK FAILED: ' + str(e), file=sys.stderr)
        sys.exit(1)
