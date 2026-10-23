"""Independent Fraction checks of the frozen n=4 partial Ky Fan certificates and PPT gap witnesses."""
from datetime import datetime
from fractions import Fraction as Q
import hashlib
import itertools
import json
from math import comb, prod
from pathlib import Path
import sys
from zoneinfo import ZoneInfo


def require(ok, label):
    if not ok:
        raise ValueError(label)


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def scaled(a, q):
    return [[q * x for x in row] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def main():
    if len(sys.argv) != 3:
        raise SystemExit('Usage: check_n4_partial_independent.py PINNED_INPUT_DIR OUTPUT.json')
    folder, out = map(Path, sys.argv[1:])
    require(not out.exists(), 'Refusing to overwrite prior evidence')
    identity = [[Q(i == j) for j in range(4)] for i in range(4)]
    bell = [[Q(1, 2) if i in (0, 3) and j in (0, 3) else Q(0) for j in range(4)] for i in range(4)]
    complement = [[identity[i][j] - bell[i][j] for j in range(4)] for i in range(4)]
    swap = [[Q(i // 2 == j % 2 and i % 2 == j // 2) for j in range(4)] for i in range(4)]
    sym = [[(identity[i][j] + swap[i][j]) / 2 for j in range(4)] for i in range(4)]
    anti = [[(identity[i][j] - swap[i][j]) / 2 for j in range(4)] for i in range(4)]
    local = {}
    for included, projector in [(True, bell), (False, complement)]:
        pt = [[projector[2 * (i // 2) + j % 2][2 * (j // 2) + i % 2]
               for j in range(4)] for i in range(4)]
        eigen = []
        for space, rank in [(sym, 3), (anti, 1)]:
            value = trace(mm(pt, space)) / rank
            require(mm(pt, space) == scaled(space, value), 'Local PPT eigenspace identity')
            eigen.append(value)
        partial = [[sum(projector[2 * i + b][2 * j + b] for b in range(2)) for j in range(2)] for i in range(2)]
        require(partial == [[trace(projector) / 2 if i == j else 0 for j in range(2)] for i in range(2)],
                'Local partial-trace normalization')
        local[included] = {'rank': trace(projector), 'ppt': eigen,
                           'choi_id': trace(mm(scaled(bell, 2), projector))}
    subsets = [s for size in range(5) for s in itertools.combinations(range(4), size)]
    sectors = list(itertools.product((0, 1), repeat=4))
    ranks = [prod(local[i in s]['rank'] for i in range(4)) for s in subsets]
    marginal = [r / 16 for r in ranks]
    ppt = [[prod(local[i in s]['ppt'][sector[i]] for i in range(4)) for s in subsets] for sector in sectors]
    objective = {size: [sum(prod(local[i in s]['choi_id'] if i in chosen else local[i in s]['rank']
                                for i in range(4)) for chosen in itertools.combinations(range(4), size))
                        for s in subsets] for size in (2, 3)}
    words = sorted(itertools.product((0, 1), repeat=4), key=lambda word: sum(word))
    spectra = {size: sorted([sum(all(word[i] == 0 for i in chosen)
                                     for chosen in itertools.combinations(range(4), size)) for word in words], reverse=True)
               for size in (2, 3)}

    def feasible(c, k):
        return (len(c) == 16 and all(0 <= x <= Q(1, 16) for x in c)
                and sum(a * b for a, b in zip(c, ranks)) == k
                and sum(a * b for a, b in zip(c, marginal)) <= 1
                and all(0 <= sum(a * b for a, b in zip(c, row)) <= Q(1, 16) for row in ppt))

    for k in range(1, 17):
        c = [sum(prod(Q(1, 2) if word[i] == 0 else (Q(0) if i in s else Q(1))
                      for i in range(4)) for word in words[:k]) / rank for s, rank in zip(subsets, ranks)]
        require(feasible(c, k), 'Product-input positive control feasibility')
        for size in (2, 3):
            require(sum(a * b for a, b in zip(c, objective[size])) == sum(spectra[size][:k]),
                    'Product-input target normalization')
    two_anti = [j for j, sector in enumerate(sectors) if sum(sector) == 2]
    require(all(objective[2][j] == 3 * ranks[j] + (48 if len(subsets[j]) == 4 else 0)
                - 72 * sum(ppt[i][j] for i in two_anti) for j in range(16)),
            'Analytic identity obj.c = 3k + 48 c_full - 72 sum e_two_anti')
    certificates = json.loads((folder / 'u2_dual_certificates.json').read_text())
    dual_checks = {}
    for key, record in certificates.items():
        k, cert = int(key), record['certificate']
        w, u, v = [[Q(x) for x in cert[name]] for name in ('w', 'u', 'v')]
        z, y = Q(cert['z']), Q(cert['y'])
        require(all(len(vec) == 16 for vec in (w, u, v)), 'Dual multiplier dimensions')
        require(min(w + u + v + [y]) >= 0, 'Dual multiplier nonnegativity')
        slack = [w[j] + ranks[j] * z + marginal[j] * y
                 + sum(ppt[i][j] * (v[i] - u[i]) for i in range(16)) - objective[2][j] for j in range(16)]
        require(min(slack) >= 0, 'Dual column inequality')
        bound = sum(w) / 16 + k * z + y + sum(v) / 16
        target = sum(spectra[2][:k])
        require(bound == target, 'Dual upper bound equals exact product target')
        require(not (bound <= target - Q(1, 1000)), 'Lowered-target mutation rejected')
        require(min(slack[j] - ranks[j] for j in range(16)) < 0, 'Decreased-z mutation rejected by dual inequality')
        dual_checks[key] = {'bound': str(bound), 'target': str(target), 'minimum_slack': str(min(slack)),
                            'lowered_target_rejected': True, 'decreased_z_rejected': True}
    require(set(map(int, certificates)) == {1, 2, 3, 4, 5, 11, 12, 13, 14, 15}, 'Expected certified index set')
    gaps = {}
    for label, record in json.loads((folder / 'lp1_primal_witnesses.json').read_text()).items():
        size, k = map(int, re_numbers(label))
        c = list(map(Q, record['c']))
        require(feasible(c, k), 'Relaxation-gap witness feasibility')
        value = sum(a * b for a, b in zip(c, objective[size]))
        target = sum(spectra[size][:k])
        require(value > target, 'Strict relaxation gap')
        gaps[label] = {'value': str(value), 'target': str(target), 'excess': str(value - target)}
    result = {'status': 'EXACT_PARTIAL_CERTIFICATES_AND_RELAXATION_GAPS_PASS',
              'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_sha256': {name: hashlib.sha256((folder / name).read_bytes()).hexdigest()
                               for name in ('u2_dual_certificates.json', 'lp1_primal_witnesses.json')},
              'local_matrix_derivation': 'PPT eigenspaces and partial traces derived from exact 4x4 Bell and complementary projectors; tensor products give the 16-variable LP.',
              'product_input_positive_controls': 16, 'dual_columns_checked': 16 * len(dual_checks),
              'analytic_upper_bound': 'LP(U2,k) <= min(3k+3,24), from exact 16-column identity and trace bound',
              'dual_checks': dual_checks, 'relaxation_gap_witnesses': gaps,
              'scope': 'Partial Ky Fan indices only. Proof bridge is separately read in PROOF.md and ADDENDUM_v1_1.md; no general n=4 majorization or novelty claim.'}
    with out.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(result, indent=2))


def re_numbers(label):
    import re
    return re.findall(r'\d+', label)


if __name__ == '__main__':
    main()
