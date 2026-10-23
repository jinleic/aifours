#!/usr/bin/env python3
"""Exploratory location-aware next-bit parity probe; not used in the exclusion proof."""
import gzip
import hashlib
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
ALL = (1 << 256) - 1


def d(a):
    return ((a & 1) * ((a >> 1) & 1)) ^ (((a >> 2) & 1) * ((a >> 3) & 1)) ^ ((a >> 4) & 1)


def main():
    started = time.monotonic()
    raw = (ROOT / 'results/classification.json.gz').read_bytes()
    data = json.loads(gzip.decompress(raw))
    D = sum(d(a) << a for a in range(256))
    monomials = [m for m in range(256) if m.bit_count() <= 3]
    moments = [sum(int(a & m == m) << a for a in range(256)) for m in monomials]
    results = []
    for family in data['canonical_families']:
        Z = set(family['representative_points'])
        unknown = [a for a in range(256) if not d(a) and a not in Z]
        pivots, consistency = {}, []
        for i, monomial in enumerate(monomials):
            row = sum(int(a & monomial == monomial) << j for j, a in enumerate(unknown))
            combination = 1 << i
            for p in sorted(pivots, reverse=True):
                if row >> p & 1:
                    row ^= pivots[p][0]
                    combination ^= pivots[p][1]
            if row:
                pivots[row.bit_length() - 1] = (row, combination)
            else:
                consistency.append(combination)
        E0 = int(family['E0_truth_hex'], 16)
        kernel = [int(v, 16) for v in family['kernel_truth_hex']]
        passing = 0
        for parameters in range(8192):
            E = E0
            for j, v in enumerate(kernel):
                if parameters >> j & 1:
                    E ^= v
            fixed_F = D & (ALL ^ E)
            rhs = 0
            for i, moment in enumerate(moments):
                numerator = (D & moment).bit_count() + 2 * (E & moment).bit_count()
                if numerator % 4:
                    raise ValueError('E-extension violates required carry integrality')
                bit = ((numerator // 4) & 1) ^ ((fixed_F & moment).bit_count() & 1)
                rhs |= bit << i
            if all((rhs & c).bit_count() % 2 == 0 for c in consistency):
                passing += 1
        results.append({'tau': family['tau'], 'E_candidates': 8192, 'E_passing_parity_test': passing,
                        'unknown_F_positions': len(unknown), 'moment_equations': len(monomials),
                        'moment_matrix_rank': len(pivots), 'left_nullity': len(consistency),
                        'remaining_F_parity_dimension': len(unknown) - len(pivots),
                        'exclusions_from_this_probe': 0})
    out = {'status': 'COMPLETED_NO_ADDITIONAL_E_EXCLUSION', 'classification_sha256': hashlib.sha256(raw).hexdigest(),
           'scope': 'Necessary parity moments only, not full Fourier quantization or Boolean realization.',
           'derivation': 'p=D+2E-4F; moments of p of coordinate degree<=3 are0mod8, fixing parity moments of F. F=1+E on D=1, F=0 on Z.',
           'results': results, 'elapsed_seconds': time.monotonic() - started,
           'stop': 'All E pass this parity consistency test; do not expand it into unrestricted sign SAT. The character-projection proof is a different, stronger obstruction.'}
    path = ROOT / 'results/carry-probe.json'
    if path.exists():
        raise ValueError('Preserve the existing carry probe')
    path.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, sort_keys=True))


if __name__ == '__main__':
    main()
