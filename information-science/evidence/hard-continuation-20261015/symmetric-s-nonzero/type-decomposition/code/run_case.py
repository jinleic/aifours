#!/usr/bin/env python3
"""One exact native weighted-PB visit per balanced dihedral support type."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time
import z3

ROOT = Path(__file__).resolve().parents[1]


def fwht(bits):
    W = [1 - 2 * b for b in bits]
    h = 1
    while h < 512:
        for base in range(0, 512, 2 * h):
            for j in range(h):
                u, v = W[base + j], W[base + h + j]
                W[base + j], W[base + h + j] = u + v, u - v
        h *= 2
    return W


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--s', type=int, required=True)
    ap.add_argument('--seconds', type=int, default=600)
    args = ap.parse_args()
    start = time.monotonic()
    raw_input = (ROOT / 'inputs/orbits.json.gz').read_bytes()
    data = json.loads(gzip.decompress(raw_input))
    decomp = json.loads((ROOT / 'inputs/decomposition.json').read_text())
    assert args.s in decomp['nonzero_types']
    encoded = (ROOT / f'inputs/target-s{args.s}.smt2.gz').read_bytes()
    smt = gzip.decompress(encoded)
    meta = json.loads((ROOT / f'inputs/target-s{args.s}.encoding.json').read_text())
    assert hashlib.sha256(smt).hexdigest() == meta['smt_sha256']
    assert meta['s'] == args.s and meta['nominal_bound'] == 28 and meta['balance_weight'] == 256
    # Process-local bounds: three simultaneous visits have <=3.3GiB Z3 cap
    # combined. Z3's default native SAT/PB solver uses one thread per visit.
    z3.set_param('memory_max_size', 1100)
    z3.set_param('parallel.enable', False)
    solver = z3.SolverFor('QF_FD')
    solver.set(timeout=args.seconds * 1000)
    solver.from_string(smt.decode())
    build_seconds = time.monotonic() - start
    outcome = solver.check()
    out = {'s': args.s, 'solver_status': str(outcome).upper(), 'certified_class_status': 'UNKNOWN',
           'negative_claim': False, 'z3_version': z3.get_version_string(),
           'input_sha256': hashlib.sha256(raw_input).hexdigest(), 'smt_sha256': hashlib.sha256(smt).hexdigest(),
           'compressed_smt_sha256': hashlib.sha256(encoded).hexdigest(),
           'seconds_limit': args.seconds, 'z3_memory_cap_mib': 1100, 'threads': 1,
           'build_seconds': build_seconds, 'elapsed_seconds': time.monotonic() - start,
           'reason_unknown': solver.reason_unknown() if outcome == z3.unknown else None,
           'scope': 'Balanced3-DSBF104 orbit bits, exact weight256, fixed nonzero support XOR, Walsh caps24/28 froma.dot.s; f(0)=0 up to output complement.',
           'certification_rule': 'Solver-only UNSAT is uncertified and does not exclude this branch. SAT requires full512-bit direct/FWHT checks.'}
    if outcome == z3.sat:
        model = solver.model()
        orbit_bits = [int(z3.is_true(model.eval(z3.Bool('x' + str(j)), model_completion=True))) for j in range(104)]
        bits = [None] * 512
        for j, orbit in enumerate(data['classes']['3-dsbf']['orbits']):
            for x in orbit:
                bits[x] = orbit_bits[j]
        W = fwht(bits)
        direct = [sum(1 - 2 * (b ^ ((a & x).bit_count() & 1)) for x, b in enumerate(bits)) for a in range(512)]
        sx = 0
        for x, b in enumerate(bits):
            if b:
                sx ^= x
        assert W == direct and sum(bits) == 256 and sx == args.s and max(map(abs, W)) <= 28
        text = ''.join(map(str, bits))
        out.update(candidate_bits=text, candidate_orbit_bits=''.join(map(str, orbit_bits)), candidate_walsh=W,
                   candidate_weight=sum(bits), candidate_support_xor=sx, candidate_sha256_ascii_bits=hashlib.sha256(text.encode()).hexdigest(),
                   producer_positive_check='PASS direct character sums and FWHT; independent replay still required.')
    (ROOT / f'results/s{args.s}-run.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ('s', 'solver_status', 'certified_class_status', 'elapsed_seconds', 'reason_unknown')}, sort_keys=True))


if __name__ == '__main__':
    main()
