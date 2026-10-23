#!/usr/bin/env python3
"""Independent GMP recomputation of the Fermat residues of fermat_power_two.py.

Uses the installed GNU MP library through ctypes (mpz_powm with GMP's own
multiplication and reduction; nothing is installed) to compute 3^(p_t - 1) mod p_t
for p_t = 2^(2a) + 2^a + 1, a = 3^t, and compares the residue's low 64 bits and
SHA-256 with evidence/fermat-t<t>.json.  For small t it also compares with
CPython's pow.  It shares no arithmetic with the staged CPython computation.
"""
import argparse
import ctypes
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
CANDIDATES = ['/opt/homebrew/lib/libgmp.10.dylib', '/usr/local/lib/libgmp.10.dylib', 'libgmp.so.10']


class Mpz(ctypes.Structure):
    _fields_ = [('alloc', ctypes.c_int), ('size', ctypes.c_int), ('d', ctypes.c_void_p)]


def gmp():
    for path in CANDIDATES:
        try:
            lib = ctypes.CDLL(path)
            break
        except OSError:
            continue
    else:
        raise SystemExit('CHECK FAILED: GNU MP library not found')
    P = ctypes.POINTER(Mpz)
    lib.__gmpz_init.argtypes = [P]
    lib.__gmpz_set_str.argtypes = [P, ctypes.c_char_p, ctypes.c_int]
    lib.__gmpz_powm.argtypes = [P, P, P, P]
    lib.__gmpz_sizeinbase.argtypes = [P, ctypes.c_int]
    lib.__gmpz_sizeinbase.restype = ctypes.c_size_t
    lib.__gmpz_get_str.argtypes = [ctypes.c_char_p, ctypes.c_int, P]
    lib.__gmpz_get_str.restype = ctypes.c_char_p
    lib.__gmpz_clear.argtypes = [P]
    return lib, path


def powm(lib, b, e, m):
    vals = [Mpz() for _ in range(4)]
    for v in vals:
        lib.__gmpz_init(ctypes.byref(v))
    for v, x in zip(vals[1:], (b, e, m)):
        if lib.__gmpz_set_str(ctypes.byref(v), format(x, 'x').encode(), 16) != 0:
            raise SystemExit('CHECK FAILED: mpz_set_str')
    lib.__gmpz_powm(*(ctypes.byref(v) for v in vals))
    size = lib.__gmpz_sizeinbase(ctypes.byref(vals[0]), 16) + 2
    buf = ctypes.create_string_buffer(size)
    out = int(lib.__gmpz_get_str(buf, 16, ctypes.byref(vals[0])).decode(), 16)
    for v in vals:
        lib.__gmpz_clear(ctypes.byref(v))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--t', type=int, default=10)
    ap.add_argument('--base', type=int, default=3)
    ap.add_argument('--small', type=int, default=7, help='also compare t = 1..small with CPython pow')
    ap.add_argument('--output')
    args = ap.parse_args()
    lib, path = gmp()
    controls = []
    for t in range(1, args.small + 1):
        a = 3 ** t
        p = (1 << 2 * a) + (1 << a) + 1
        r = powm(lib, args.base, p - 1, p)
        if r != pow(args.base, p - 1, p):
            raise SystemExit('CHECK FAILED: GMP differs from CPython at t=%d' % t)
        controls.append(dict(t=t, residue_is_1=r == 1))
    a = 3 ** args.t
    p = (1 << 2 * a) + (1 << a) + 1
    r = powm(lib, args.base, p - 1, p)
    rec = json.loads((BASE / 'evidence' / ('fermat-t%d.json' % args.t)).read_text())
    sha = hashlib.sha256(r.to_bytes((p.bit_length() + 7) // 8, 'little')).hexdigest()
    same = (rec['base'] == args.base and rec['fermat_residue_low64'] == r & ((1 << 64) - 1)
            and rec['fermat_residue_sha256'] == sha)
    out = dict(t=args.t, a=a, base=args.base, library=path, residue_is_1=r == 1, residue_low64=r & ((1 << 64) - 1),
               residue_sha256=sha, equals_staged_cpython_result=same, small_controls=controls)
    if args.output:
        Path(args.output).write_text(json.dumps(out, indent=1) + '\n')
    print(json.dumps(out))
    if not same or r == 1:
        print('CHECK FAILED: GMP residue does not confirm the staged Fermat witness', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
