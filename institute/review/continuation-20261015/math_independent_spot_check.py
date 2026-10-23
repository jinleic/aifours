#!/usr/bin/env python3
"""Stratified sample audit with GMP; this is NOT an exhaustive range certificate."""
import argparse
import ctypes
import hashlib
import json
import random
import time
from datetime import datetime
from decimal import Context, Decimal, Inexact, InvalidOperation, Rounded
from math import isqrt
from pathlib import Path
from zoneinfo import ZoneInfo

GMP_PATH = Path('/opt/homebrew/lib/libgmp.10.dylib')


class Failed(Exception):
    pass


def need(condition, message):
    if not condition:
        raise Failed(message)


class Mpz(ctypes.Structure):
    _fields_ = [('allocated', ctypes.c_int), ('size', ctypes.c_int),
                ('limbs', ctypes.POINTER(ctypes.c_ulong))]


class Gmp:
    def __init__(self):
        self.lib = ctypes.CDLL(str(GMP_PATH))
        for name, args, result in [
            ('init', [ctypes.POINTER(Mpz)], None),
            ('clear', [ctypes.POINTER(Mpz)], None),
            ('set_str', [ctypes.POINTER(Mpz), ctypes.c_char_p, ctypes.c_int], ctypes.c_int),
            ('powm', [ctypes.POINTER(Mpz)] * 4, None),
            ('get_str', [ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(Mpz)], ctypes.c_char_p),
        ]:
            function = getattr(self.lib, '__gmpz_' + name)
            function.argtypes, function.restype = args, result
            setattr(self, name, function)
        self.version = ctypes.c_char_p.in_dll(self.lib, '__gmp_version').value.decode()

    def power(self, base, exponent, modulus):
        values = [Mpz() for _ in range(4)]
        for value in values:
            self.init(ctypes.byref(value))
        try:
            for value, number in zip(values[:3], (base, exponent, modulus)):
                need(self.set_str(ctypes.byref(value), str(number).encode(), 10) == 0,
                     'GMP integer conversion')
            a, e, m, result = map(ctypes.byref, values)
            self.powm(result, a, e, m)
            buffer = ctypes.create_string_buffer(len(str(modulus)) + 2)
            self.get_str(buffer, 10, result)
            return int(buffer.value)
        finally:
            for value in values:
                self.clear(ctypes.byref(value))


def primes(bound):
    flags = bytearray(b'\x01') * (bound + 1)
    flags[0:2] = b'\x00\x00'
    for q in range(2, isqrt(bound) + 1):
        if flags[q]:
            flags[q*q::q] = b'\x00' * ((bound - q*q) // q + 1)
    return [q for q, flag in enumerate(flags) if flag]


def first_factor(n, prime_list):
    p = n*n + n + 1
    return next((q for q in prime_list if q < p and p % q == 0), 0)


def verify(n, q, residue, gmp, decimal):
    p = n*n + n + 1
    if q:
        need(1 < q < p and p % q == 0, 'invalid proper-factor witness')
        return 'proper-factor'
    need(gmp.power(2, n+1, p) == residue, 'GMP residue mismatch')
    need(int(decimal.power(Decimal(2), Decimal(n+1), Decimal(p))) == residue,
         'libmpdec residue mismatch')
    if residue != 1:
        return 'base-two-failure'
    if n == 8:
        return 'classical-order-8'
    need(n == 512, 'unexpected survivor in a sample')
    pairs = [(1, 89785), (4, 89788)]
    need(all(gmp.power(x, n+1, p) == 1 for pair in pairs for x in pair),
         'collision entry outside D')
    need(pairs[0] != pairs[1] and pairs[0][0] != pairs[0][1]
         and (pairs[0][0]-pairs[0][1]) % p == (pairs[1][0]-pairs[1][1]) % p,
         'invalid difference collision')
    return 'difference-collision'


def rejected(call):
    try:
        call()
    except Failed:
        return True
    raise Failed('a corruption control was accepted')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--coverage', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--residues-per-segment', type=int, default=128)
    args = parser.parse_args()
    began = time.monotonic()
    coverage_bytes = args.coverage.read_bytes()
    coverage = json.loads(coverage_bytes)
    need(coverage['paired_c_range_complete'] and coverage['first_missing'] is None,
         'full gap-free coverage is not yet recorded')
    need(args.residues_per_segment >= 1, 'positive sample size required')
    gmp = Gmp()
    decimal = Context(prec=80, traps=[Inexact, Rounded, InvalidOperation])
    prime_list = primes(1000000)
    need(len(prime_list) == 78498 and prime_list[-1] == 999983, 'prime sieve control')
    rows, segments = [], []
    for segment in coverage['segments']:
        if segment['segment'] == 'prior':
            continue
        lo, hi = segment['start'], segment['end']
        count = (hi-lo) // 24
        need(segment['complete'] and count > 0 and lo % 24 == 8 and hi % 24 == 8,
             'segment geometry')
        rng = random.Random(int(hashlib.sha256(f'{lo}:{hi}:GMP-audit'.encode()).hexdigest(), 16))
        indices = list(dict.fromkeys([0, 1, count//2, count-2, count-1]))
        done, residuals, factors = set(), 0, 0
        while indices or residuals < args.residues_per_segment:
            index = indices.pop(0) if indices else rng.randrange(count)
            if index in done:
                continue
            done.add(index)
            n = lo + 24*index
            q = first_factor(n, prime_list)
            residue = None if q else pow(2, n+1, n*n+n+1)
            kind = verify(n, q, residue, gmp, decimal)
            residuals += not bool(q)
            factors += bool(q)
            rows.append(dict(segment=segment['segment'], n=n, factor=q,
                             residue=residue, result=kind))
            need(len(done) < count or residuals >= args.residues_per_segment,
                 'segment has fewer unsieved members than requested')
        segments.append(dict(segment=segment['segment'], start=lo, end=hi,
                             sampled=len(done), residues=residuals, factors=factors))
    controls = {
        'factor_equal_to_modulus': rejected(lambda: verify(8, 73, None, gmp, decimal)),
        'nondividing_factor': rejected(lambda: verify(512, 7, None, gmp, decimal)),
        'wrong_residue': rejected(lambda: verify(8, 0, 2, gmp, decimal)),
        'classical_order_8': verify(8, 0, 1, gmp, decimal),
        'order_512_collision': verify(512, 0, 1, gmp, decimal),
        'order_2pow27_proper_factor': verify(2**27, 2593, None, gmp, decimal),
    }
    result = dict(status='PASS', local_date=datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
                  scope='Sample audit only. It neither recomputes all blocks nor certifies the full range.',
                  coverage_sha256=hashlib.sha256(coverage_bytes).hexdigest(),
                  claimed_range_end=coverage['gap_free_bound'], gmp_version=gmp.version,
                  gmp_library=str(GMP_PATH), gmp_sha256=hashlib.sha256(GMP_PATH.read_bytes()).hexdigest(),
                  checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  arithmetic='Trial division of p by an independently generated prime list; CPython pow, GMP mpz_powm, and libmpdec for every unsieved sample.',
                  segments=segments, controls=controls, samples=rows,
                  seconds=round(time.monotonic()-began, 3))
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'samples'}, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Failed as error:
        raise SystemExit('CHECK FAILED: '+str(error))
