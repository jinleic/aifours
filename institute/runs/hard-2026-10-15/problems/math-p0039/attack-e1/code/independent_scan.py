#!/usr/bin/env python3
"""Independent exact segmented Python scan; no producing C code is imported.

Unlike the C cube-root sieve, roots come from Tonelli-Shanks sqrt(-3).
Unlike the C Montgomery exponentiation, Python's arbitrary-precision pow is used.
Bytearray extended slices mark mathematically specified proper-factor classes.
One CPU only. The output protocol allows the independent trial-division checker
to recompute all explicitly recorded full residues and actual factor witnesses.
"""
import argparse
import json
from math import isqrt
from pathlib import Path
import time


def primes_to(bound):
    composite = bytearray(bound+1)
    for a in range(2, isqrt(bound)+1):
        if not composite[a]:
            for v in range(a*a, bound+1, a):
                composite[v] = 1
    return [a for a in range(2, bound+1) if not composite[a]]


def square_root(value, prime):
    value %= prime
    if not value:
        return 0
    assert pow(value, (prime-1)//2, prime) == 1
    if prime % 4 == 3:
        return pow(value, (prime+1)//4, prime)
    odd = prime-1; s = 0
    while odd % 2 == 0:
        odd //= 2; s += 1
    z = 2
    while pow(z, (prime-1)//2, prime) == 1:
        z += 1
    c = pow(z, odd, prime)
    x = pow(value, (odd+1)//2, prime)
    t = pow(value, odd, prime)
    m = s
    while t != 1:
        i = 1; v = t*t % prime
        while v != 1:
            v = v*v % prime; i += 1
        assert i < m
        b = pow(c, 1 << (m-i-1), prime)
        x = x*b % prime
        c = b*b % prime
        t = t*c % prime
        m = i
    assert x*x % prime == value
    return x


def progression_roots(start, step, primes):
    roots = []
    for q in primes:
        if q == 3:
            values = [1]
        elif q % 3 == 1:
            r = square_root(-3, q)
            half = pow(2, -1, q)
            values = [(-1+r)*half % q, (-1-r)*half % q]
        else:
            continue
        assert all((r*r+r+1) % q == 0 for r in values)
        if step % q == 0:
            if start % q in values:
                roots.append((q, [0], 1))
        else:
            inv = pow(step, -1, q)
            offsets = sorted({(r-start)*inv % q for r in values})
            roots.append((q, offsets, q))
    return roots


def proper_factor(n, bound, primes):
    p = n*n+n+1
    for q in primes:
        if q > bound or q*q > p:
            return 0
        if p % q == 0:
            assert 1 < q < p
            return q
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--start', type=int, required=True)
    parser.add_argument('--stop', type=int, required=True)
    parser.add_argument('--step', type=int, default=24)
    parser.add_argument('--bound', type=int, default=1000000)
    parser.add_argument('--block', type=int, default=1048576)
    parser.add_argument('--cap', type=float, default=6000)
    parser.add_argument('--prefix', required=True)
    parser.add_argument('--window-every', type=int, default=256)
    parser.add_argument('--window-len', type=int, default=256)
    args = parser.parse_args()
    assert 2 <= args.start < args.stop and args.step > 0 and 0 <= args.bound <= 1000000
    assert args.block > 0 and 0 <= args.window_len <= args.block and args.cap > 0
    total = len(range(args.start, args.stop, args.step))
    nblocks = (total+args.block-1)//args.block
    primes = primes_to(args.bound)
    root_classes = progression_roots(args.start, args.step, primes)
    metadata = dict(kind='header', version=1, start=args.start, stop=args.stop,
                    step=args.step, total=total, block_size=args.block, blocks=nblocks,
                    sieve_bound=args.bound, sieve_primes=len(root_classes),
                    threads=1, cap_seconds=args.cap, window_every=args.window_every,
                    window_len=args.window_len, arithmetic='Python arbitrary precision; Tonelli-Shanks roots; no producing C imports')
    done = 0
    with Path(args.prefix+'.blocks.jsonl').open('x') as out, \
            Path(args.prefix+'.records.jsonl').open('x') as rec:
        out.write(json.dumps(metadata)+'\n'); out.flush()
        begin = time.monotonic()
        for block in range(nblocks):
            if time.monotonic()-begin >= args.cap:
                break
            t0 = time.monotonic()
            base = block*args.block
            length = min(args.block, total-base)
            n0 = args.start+args.step*base
            marked = bytearray(length)
            all_proper = n0*n0+n0+1 > args.bound
            for q, offsets, stride in root_classes:
                for offset in offsets:
                    first = (offset-base) % stride
                    if first >= length:
                        continue
                    if all_proper:
                        count = (length-1-first)//stride+1
                        marked[first::stride] = b'\1'*count
                    else:
                        for j in range(first, length, stride):
                            n = n0+args.step*j
                            if 1 < q < n*n+n+1:
                                marked[j] = 1
            zero_count = marked.count(0)
            has_window = args.window_every and (block % args.window_every == 0 or block+1 == nblocks)
            edges = {j for j in (0, 1, length-2, length-1) if 0 <= j < length}
            audit = edges | (set(range(min(length, args.window_len))) if has_window else set())
            audit_values = {}
            tested = 0; survivors = []
            j = marked.find(b'\0')
            while j != -1:
                n = n0+args.step*j
                residue = pow(2, n+1, n*n+n+1)
                tested += 1
                if j in audit:
                    audit_values[j] = residue
                if residue == 1:
                    survivors.append(n)
                    audit.add(j); audit_values[j] = residue
                j = marked.find(b'\0', j+1)
            assert tested == zero_count
            for j in sorted(audit):
                n = n0+args.step*j; p = n*n+n+1
                q = proper_factor(n, args.bound, primes) if marked[j] else 0
                assert bool(q) == bool(marked[j])
                residue = audit_values[j] if j in audit_values else pow(2, n+1, p)
                decision = 'factor' if q else ('survivor' if residue == 1 else 'base2-fail')
                record = dict(block=block, index=base+j, n=n, p=str(p),
                              decision=decision, factor=q, residue=str(residue),
                              window=bool(has_window and j < args.window_len), edge=j in edges)
                rec.write(json.dumps(record)+'\n')
            row = dict(kind='block', id=block, index=base, start=n0,
                       end=n0+args.step*length, count=length,
                       sieved=length-tested, tested=tested, hits=len(survivors),
                       seconds=time.monotonic()-t0, survivors=survivors)
            out.write(json.dumps(row)+'\n'); out.flush(); rec.flush()
            done += 1
            if block % 128 == 0:
                print(json.dumps(dict(block=block, end=row['end'], survivors=survivors,
                                      elapsed=time.monotonic()-begin)), flush=True)
        footer = dict(kind='footer', assigned_blocks=done, planned_blocks=nblocks,
                      seconds=time.monotonic()-begin, completed_plan=done == nblocks)
        out.write(json.dumps(footer)+'\n')
        print(json.dumps(footer), flush=True)


if __name__ == '__main__':
    main()
