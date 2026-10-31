#!/usr/bin/env python3
"""f62 reviewer: exact positive-definiteness of all saved corrected d=4 multipliers by Sylvester's
criterion (every leading principal minor > 0), computed as exact integer determinants of the
denominator-cleared matrices with python-flint fmpz_mat.det. Distinct from the author's
characteristic-polynomial sign test, the first reviewer's Fraction/fmpq Schur eliminations and
Bareiss pivots, and the parent's Fraction Schur check. Also records a float64 eigenvalue floor
(diagnostic only). PD implies PSD; PSD alone would suffice for the certificate.
Reads only the pinned corrected bytes; writes only into this review directory."""
import hashlib, json, lzma, math, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
import numpy as np
OWN = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart')
sys.path.insert(0, str(OWN / 'frontier-20261028-python-deps'))
import flint
CORRECTED = OWN / 'frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz'
EXPECTED = 'c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94'
OUT = Path(__file__).resolve().parent / 'f62-independent-sylvester-pd-check-results.json'


def integer_matrix(values, r):
    """values: r*r (num, den) pairs row-major -> (symmetric?, integer matrix list, common denominator)."""
    L = 1
    for _, d in values:
        if d <= 0: raise ValueError('nonpositive denominator')
        L = L * d // math.gcd(L, d)
    M = [n * (L // d) for n, d in values]
    sym = all(M[a * r + b] == M[b * r + a] for a in range(r) for b in range(r))
    return sym, M, L


def sylvester_pd(M, r):
    """All leading principal minors positive (exact). Returns (pd, first failing order or None)."""
    for k in range(1, r + 1):
        sub = flint.fmpz_mat(k, k, [M[a * r + b] for a in range(k) for b in range(k)])
        if sub.det() <= 0: return False, k
    return True, None


def main():
    t0 = time.monotonic()
    raw = CORRECTED.read_bytes()
    if hashlib.sha256(raw).hexdigest() != EXPECTED: raise ValueError('corrected data hash mismatch')
    data = json.loads(lzma.decompress(raw, memlimit=256 * 1024 * 1024))
    mats = data['matrices']
    failures, nonsym, minors_checked, eig_floor = [], [], 0, None
    for i, m in enumerate(mats):
        r = m['r']; vals = [(int(a), int(b)) for a, b in m['values']]
        if len(vals) != r * r: raise ValueError('shape')
        sym, M, L = integer_matrix(vals, r)
        if not sym: nonsym.append(i); continue
        pd, k = sylvester_pd(M, r); minors_checked += r if pd else k
        if not pd: failures.append({'index': i, 'r': r, 'first_nonpositive_minor_order': k})
        # diagnostic float floor of the rational matrix (scaled by its largest diagonal entry)
        A = np.array([a / b for a, b in vals], dtype=np.float64).reshape(r, r)
        scale = max(abs(A).max(), 1e-300)
        ev = np.linalg.eigvalsh(A / scale).min()
        eig_floor = ev if eig_floor is None else min(eig_floor, ev)
    # intended-reason controls (in memory only)
    controls = {}
    c1 = [(int(a), int(b)) for a, b in mats[0]['values']]; c1 = [(-c1[0][0], c1[0][1])]
    controls['first_1x1_negated_rejected'] = not sylvester_pd(integer_matrix(c1, 1)[1], 1)[0]
    controls['indefinite_2x2_[[1,2],[2,1]]_rejected'] = not sylvester_pd([1, 2, 2, 1], 2)[0]
    controls['singular_psd_2x2_[[1,1],[1,1]]_rejected_as_not_PD'] = not sylvester_pd([1, 1, 1, 1], 2)[0]
    controls['zero_diagonal_nonzero_row_[[0,1],[1,0]]_rejected'] = not sylvester_pd([0, 1, 1, 0], 2)[0]
    controls['pd_3x3_[[2,-1,0],[-1,2,-1],[0,-1,2]]_accepted'] = sylvester_pd([2, -1, 0, -1, 2, -1, 0, -1, 2], 3)[0]
    g = next(i for i, m in enumerate(mats) if m['r'] >= 3)
    vals = [(int(a), int(b)) for a, b in mats[g]['values']]; r = mats[g]['r']
    sym, M, L = integer_matrix(vals, r); M2 = list(M); M2[1] = -M2[1]   # break symmetry of entry (0,1)
    controls['asymmetric_mutation_detected_by_symmetry_check'] = not all(M2[a * r + b] == M2[b * r + a] for a in range(r) for b in range(r))
    M3 = list(M); M3[r + 1] = -M3[r + 1]   # negate diagonal (1,1) of a real r>=3 multiplier
    controls['negated_diagonal_entry_of_real_multiplier_rejected'] = {'index': g, 'rejected': not sylvester_pd(M3, r)[0]}
    result = {'kind': 'f62_independent_sylvester_leading_minor_positive_definiteness',
              'corrected_data_sha256': EXPECTED, 'matrix_count': len(mats),
              'nonsymmetric_indices': nonsym, 'not_positive_definite': failures,
              'leading_minors_checked': minors_checked,
              'size_sum': sum(m['r'] for m in mats),
              'float64_min_scaled_eigenvalue_diagnostic': eig_floor,
              'controls': controls, 'all_controls_behaved': all(v if isinstance(v, bool) else v['rejected'] for v in controls.values()),
              'flint_version': flint.__version__, 'numpy_version': np.__version__,
              'elapsed_seconds': round(time.monotonic() - t0, 3),
              'scope': 'Exact strict PD of every saved corrected multiplier via leading principal minors (python-flint fmpz_mat.det on denominator-cleared integer matrices). Shares the Python/FLINT runtime; not a kernel proof. PSD would suffice for the certificate.',
              'verdict': 'PASS' if not failures and not nonsym else 'FAIL'}
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result['verdict'] == 'PASS' and result['all_controls_behaved'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
