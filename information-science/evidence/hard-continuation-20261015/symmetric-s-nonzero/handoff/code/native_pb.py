#!/usr/bin/env python3
"""Materially smaller native weighted-PB formulation on the104 orbit bits.
UNSAT from this solver is uncertified; no negative claim follows.
"""
from pathlib import Path
import gzip
import hashlib
import json
import time
import z3

ROOT = Path(__file__).resolve().parents[1]


def main():
    start = time.monotonic()
    z3.set_param('memory_max_size', 3500)
    raw = (ROOT / 'inputs/orbits.json.gz').read_bytes()
    data = json.loads(gzip.decompress(raw))
    cls = data['classes']['3-dsbf']
    bits = [z3.Bool('orbit_' + str(j)) for j in range(104)]
    solver = z3.SolverFor('QF_FD')
    solver.set(timeout=120000)
    for row in cls['C']:
        L = sum(map(abs, row))
        weighted = [(bits[j] if c > 0 else z3.Not(bits[j]), abs(c)) for j, c in enumerate(row) if c]
        # W=L-2T exactly, including negative original character coefficients.
        lo, hi = (L - 28 + 1) // 2, (L + 28) // 2
        solver.add(z3.PbGe(weighted, lo), z3.PbLe(weighted, hi))
    sx = []
    for j in range(9):
        accum = z3.BoolVal(False)
        for i, v in enumerate(cls['orbit_xors']):
            if v >> j & 1:
                accum = z3.Xor(accum, bits[i])
        sx.append(accum)
    solver.add(z3.Or(sx), z3.Not(bits[0]))
    smt = solver.sexpr().encode()
    (ROOT / 'results/native-pb.smt2.gz').write_bytes(gzip.compress(smt, mtime=0))
    built = time.monotonic() - start
    outcome = solver.check()
    out = {'solver_status': str(outcome).upper(), 'certified_class_status': 'UNKNOWN',
           'negative_claim': False, 'z3_version': z3.get_version_string(),
           'scope': 'All3-DSBF104 orbit variables, all weight parities, |W|<=28, nonzero support XOR, harmless f(0)=0 normalization.',
           'input_sha256': hashlib.sha256(raw).hexdigest(), 'smt_sha256': hashlib.sha256(smt).hexdigest(),
           'native_primary_variables': 104, 'weighted_constraints': 208,
           'build_seconds': built, 'elapsed_seconds': time.monotonic() - start, 'solver_time_limit_seconds': 120,
           'reason_unknown': solver.reason_unknown() if outcome == z3.unknown else None,
           'certification_rule': 'Solver UNSAT is not an independently checked certificate; only positive full tables can be promoted by the direct/FWHT checker.'}
    if outcome == z3.sat:
        model = solver.model()
        result = [int(z3.is_true(model.eval(v))) for v in bits]
        text = ['?'] * 512
        for j, orbit in enumerate(cls['orbits']):
            for x in orbit:
                text[x] = str(result[j])
        out['candidate_bits'] = ''.join(text)
    (ROOT / 'results/native-pb-run.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ('solver_status', 'certified_class_status', 'elapsed_seconds', 'reason_unknown')}, sort_keys=True))


if __name__ == '__main__':
    main()
