"""Exact Frobenius-metric Jacobian spectrum supporting the isolation-radius addendum."""
from datetime import datetime
import hashlib
from itertools import product
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo
from flint import fmpz_mat
import check_dualunitary_independent as parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    output = Path(sys.argv[1])
    if output.exists():
        raise ValueError('refusing overwrite')
    permutation = [3 * ((2 * a + b) % 3) + (a + b) % 3 for a, b in product(range(3), repeat=2)]
    identity = fmpz_mat([[int(i == j) for j in range(162)] for i in range(162)])
    cases = []
    for cuts in [('U', 'R'), ('U', 'Gamma')]:
        rows = parent.jacobian(3, permutation, cuts)
        # Hermitian Frobenius norm = sum diagonal^2 + 2 sum_{i<j}(Re^2+Im^2).
        weighted = [[v * (1 if i % 81 < 9 else 2) for v in row] for i, row in enumerate(rows)]
        matrix = fmpz_mat(rows)
        gram = matrix.transpose() * fmpz_mat(weighted)
        polynomial = gram * (gram - 2 * identity) * (gram - 6 * identity) * (gram - 8 * identity)
        symmetric = gram == gram.transpose()
        polynomial_zero = all(not x for x in polynomial.entries())
        rank = int(gram.rank())
        tangent = fmpz_mat(parent.tangent(3, permutation))
        annihilated = all(not x for x in (gram * tangent).entries())
        trank = int(tangent.rank())
        if not (symmetric and polynomial_zero and rank == 129 and trank == 33 and annihilated):
            raise ValueError('spectral certificate failed')
        cases.append({'cuts': cuts, 'gram_symmetric': symmetric, 'gram_rank': rank,
                      'tangent_rank': trank, 'gram_times_tangent_zero': annihilated,
                      'annihilating_polynomial': 'x(x-2)(x-6)(x-8)',
                      'polynomial_identity_zero': polynomial_zero,
                      'characteristic_factorization': str(gram.charpoly().factor()),
                      'gram_sha256': hashlib.sha256(json.dumps([[int(x) for x in row]
                          for row in gram.tolist()], separators=(',', ':')).encode()).hexdigest(),
                      'nonzero_eigenvalue_lower_bound': 2})
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'checker_sha256': sha(__file__), 'jacobian_builder_sha256': sha(parent.__file__),
              'status': 'EXACT_FROBENIUS_JACOBIAN_SPECTRAL_CERTIFICATE_PASS', 'cases': cases,
              'scope': 'Finite exact algebra only. The nonlinear radius >=1 requires the separately reviewed nearest-orbit normal-vector and quadratic-remainder argument.'}
    with output.open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
