"""Exact checks for the priority audit of arXiv:2401.05104v1, Proposition 1."""
from datetime import datetime
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo


def matrix(rows):
    return tuple(tuple(Q(x) for x in row) for row in rows)


def transpose(a):
    return tuple(zip(*a))


def multiply(a, b):
    return tuple(tuple(sum(x * y for x, y in zip(row, col))
                       for col in zip(*b)) for row in a)


def tensor(a, b):
    return tuple(tuple(x * y for x in row_a for y in row_b)
                 for row_a in a for row_b in b)


def twirl(a, unitaries):
    images = [multiply(multiply(u, a), transpose(u)) for u in unitaries]
    return tuple(tuple(sum(image[i][j] for image in images) / len(images)
                       for j in range(4)) for i in range(4))


def require(condition, label):
    if not condition:
        raise ValueError(label)


def main():
    if len(sys.argv) != 2:
        raise SystemExit('Usage: check_amosov_composition.py OUTPUT.json')
    out = Path(sys.argv[1])
    if out.exists():
        raise SystemExit('Refusing to overwrite prior evidence')
    identity = matrix([[1, 0], [0, 1]])
    real_paulis = [identity, matrix([[0, 1], [1, 0]]),
                   matrix([[1, 0], [0, -1]]), matrix([[0, -1], [1, 0]])]
    ua = [tensor(u, identity) for u in real_paulis]
    ub = [tensor(identity, u) for u in real_paulis]
    id4 = tensor(identity, identity)
    for u in ua + ub:
        require(multiply(u, transpose(u)) == id4, 'unitary mixture prerequisite')
    for r in range(4):
        for s in range(4):
            e = matrix([[int(i == r and j == s) for j in range(4)] for i in range(4)])
            expected = matrix([[Q(int(i // 2 == j // 2 and i % 2 == r % 2
                                      and j % 2 == s % 2 and r // 2 == s // 2), 2)
                                for j in range(4)] for i in range(4)])
            first = twirl(e, ua)
            require(first == expected, 'T_A(X) = I_A/2 tensor tr_A(X)')
            require(twirl(first, ua) == first, 'T_A is idempotent')
    rho = matrix([[int(i == 0 and j == 0) for j in range(4)] for i in range(4)])
    composed = twirl(twirl(rho, ua), ua)
    diag = [composed[i][i] for i in range(4)]
    require(all(composed[i][j] == 0 for i in range(4) for j in range(4) if i != j),
            'output is diagonal')
    spectrum = sorted(diag, reverse=True)
    require(spectrum == [Q(1, 2), Q(1, 2), Q(0), Q(0)], 'counterexample spectrum')
    require(spectrum[0] > Q(1, 4), 'rank-one Ky Fan inequality is violated')
    separate = twirl(twirl(rho, ua), ub)
    uniform = matrix([[Q(int(i == j), 4) for j in range(4)] for i in range(4)])
    require(separate == uniform, 'positive control: twirling different factors')
    condition_checks = []
    cosets = [(0, 2), (1, 3)]
    for p in [Q(0), Q(1, 2), Q(1), Q(4, 3)]:
        weights = [1 - 3 * p / 4, p / 4, p / 4, p / 4]
        marginal = [sum(weights[i] for i in c) for c in cosets]
        violations = [(u, v, i, j) for u in range(2) for v in range(2)
                      if marginal[u] <= marginal[v]
                      for i in cosets[u] for j in cosets[v]
                      if weights[i] > weights[j]]
        require(bool(violations) == (p != 1), 'literal condition (8) equality case')
        condition_checks.append({'p': str(p), 'weights': list(map(str, weights)),
                                 'literal_condition_8': not violations,
                                 'violations': violations})
    result = {
        'status': 'EXACT_COUNTEREXAMPLE_TO_PROPOSITION_1_AS_STATED',
        'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
        'source': 'https://arxiv.org/html/2401.05104v1#S3',
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'channel': 'Phi = Psi = T_A tensor id_B on C^2 tensor C^2',
        'all_input_hypothesis_proof': 'T_A(rho)=I_A/2 tensor rho_B; its largest eigenvalue is <=1/2 and top-two sum <=1, so Phi,Psi are each majorized by (1/2,1/2).',
        'dimension': 4, 'm': 2, 'n': 2,
        'matrix_units_checked': 16,
        'composed_output_spectrum': list(map(str, spectrum)),
        'claimed_majorizing_spectrum': ['1/4'] * 4,
        'rank_one_gap': str(spectrum[0] - Q(1, 4)),
        'positive_control_separate_factors': 'I_4/4',
        'literal_condition_8_checks': condition_checks,
        'limit': 'Refutes only Proposition 1 as stated; it does not refute tensor-product majorization or Theorem 2 under a repaired hypothesis/proof.'}
    with out.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
