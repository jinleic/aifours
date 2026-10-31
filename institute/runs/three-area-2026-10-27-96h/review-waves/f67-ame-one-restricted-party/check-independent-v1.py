#!/usr/bin/env python3
"""Independent exact checks of the frozen Pandya-table review inputs.

No author code is imported.  Finite-field and selected exact-complex controls
are evidence, not an exhaustive proof over C.  The mathematical proof belongs
in review-v1.md, not in these bounded computations.
"""
import hashlib
import itertools
import json
import random
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path('/Users/jinleic/repos/aifours')
SOURCE = ROOT / 'physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-pandya-table-v1.txt'
CANDIDATE = ROOT / 'physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-one-restricted-party-60-barrier-v1.md'
OUT = ROOT / 'institute/runs/three-area-2026-10-27-96h/review-waves/f67-ame-one-restricted-party'
MANIFEST = OUT / 'manifest-v1.json'
RECEIPT = OUT / 'receipt-independent-v1.json'
SOURCE_HASH = 'cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38'
CANDIDATE_HASH = 'c69c98287440eb9d0e19ff7960044ea8ab3e27e0efc1b8f64dee73e17602b443'
H = (1, 2)
K = (0, 3, 4, 5)
P = 17
PAULIS = {
    'I': (1, 0, 0, 1),
    'X': (0, 1, 1, 0),
    'Z': (1, 0, 0, -1),
    'J': (0, 1, -1, 0),
}


class CheckError(Exception):
    pass


class StructuralZeroError(CheckError):
    pass


def need(condition, message):
    if not condition:
        raise CheckError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def parse_table(data):
    need(sha(data) == SOURCE_HASH, 'table SHA-256 mismatch')
    need(len(data) == 523 and data.count(b'\n') == 38, 'table byte/LF count mismatch')
    tensor = {}
    rows = 0
    for raw in data.decode('utf-8').splitlines():
        if not raw or raw.startswith('#'):
            continue
        parts = raw.split()
        need(len(parts) in (3, 4), 'table row arity')
        a, b = map(int, parts[:2])
        need((a, b) == divmod(rows, 6), 'table a,b row order')
        rows += 1
        for token in parts[2:]:
            need(len(token) == 3 and token[0] in '+-s' and token[1:] in
                 {str(c) + str(d) for c in range(6) for d in range(6)}, 'table token')
            index = (a, b, int(token[1]), int(token[2]))
            need(index not in tensor, 'duplicate tensor entry')
            # 2 is a sentinel for +sqrt(2), not the rational number 2.
            tensor[index] = {'+': 1, '-': -1, 's': 2}[token[0]]
    need(rows == 36 and len(tensor) == 60, 'source shape or support')
    need(sum(2 if v == 2 else 1 for v in tensor.values()) == 72, 'source norm')
    for ix, val in tensor.items():
        h = tuple(i for i in range(4) if ix[i] in H)
        need(len(h) in (0, 2), 'source has a forbidden H/K pattern')
        need((len(h) == 0 and val == 2) or (len(h) == 2 and val in (-1, 1)),
             'source sector coefficient type')
    return tensor


def sector_view(tensor, active, spectators):
    """Rebuild one active 2x2 sector in the requested axis ordering."""
    active_set = set(active)
    entries = [(ix, val) for ix, val in tensor.items()
               if {i for i in range(4) if ix[i] in H} == active_set]
    label = 'E' + ''.join(map(str, sorted(active)))
    need(len(entries) == 8, label + ': expected eight entries')
    mats = {}
    for ix, val in entries:
        need(val in (-1, 1), label + ': non-Pauli coefficient')
        pair = tuple(ix[i] for i in spectators)
        cell = (H.index(ix[active[0]]), H.index(ix[active[1]]))
        mat = mats.setdefault(pair, [[0, 0], [0, 0]])
        need(mat[cell[0]][cell[1]] == 0, label + ': duplicate matrix cell')
        mat[cell[0]][cell[1]] = val
    need(len(mats) == 4 and {x for x, _ in mats} == set(K) and
         {y for _, y in mats} == set(K), label + ': spectator is not a perfect matching')
    result = []
    names = []
    for pair, matrix in sorted(mats.items()):
        flat = tuple(matrix[0] + matrix[1])
        hits = [(name, sign) for name, base in PAULIS.items() for sign in (1, -1)
                if flat == tuple(sign * x for x in base)]
        need(len(hits) == 1, label + ': matrix is not a signed Pauli')
        name, sign = hits[0]
        names.append(name)
        need(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] in (-1, 1),
             label + ': matrix is singular')
        result.append({'spectator_pair': list(pair), 'matrix': matrix,
                       'pauli': ('+' if sign == 1 else '-') + name})
    need(set(names) == set(PAULIS), label + ': Pauli family has duplicates or omissions')
    return {'active': list(active), 'spectators': list(spectators), 'entries': result}


def matching(view):
    return {tuple(e['spectator_pair']) for e in view['entries']}


def p_entries(tensor):
    return [(ix, v) for ix, v in tensor.items() if all(ix[i] in K for i in range(4))]


def ordered_contexts(tensor):
    pe = p_entries(tensor)
    need(len(pe) == 12, 'P has wrong number of entries')
    all_k_pairs = set(itertools.product(K, repeat=2))
    contexts = []
    for c, b in itertools.permutations(range(4), 2):
        a, d = sorted(set(range(4)) - {c, b})
        specifications = {
            'AB': ((a, b), (c, d)),
            'BD': ((b, d), (c, a)),
            'BC': ((b, c), (a, d)),
            'AC': ((a, c), (b, d)),
            'CD': ((c, d), (b, a)),
            'AD': ((a, d), (c, b)),
        }
        views = {key: sector_view(tensor, *spec) for key, spec in specifications.items()}
        cb_ad = [((ix[c], ix[b]), (ix[a], ix[d])) for ix, _ in pe]
        cb = [x for x, _ in cb_ad]
        ad = [y for _, y in cb_ad]
        need(len(set(cb)) == 12 and len(set(ad)) == 12,
             'P repeated a 2|2 projected pair')
        need(all_k_pairs - set(cb) == matching(views['AD']), 'P CB complement differs from E_AD')
        need(all_k_pairs - set(ad) == matching(views['BC']), 'P AD complement differs from E_BC')
        map_d = dict(matching(views['AB']))
        map_a = dict(matching(views['BD']))
        pi = dict(matching(views['AD']))
        zeroes = []
        for level in K:
            ai, di = map_a[level], map_d[level]
            need((ai, di) in matching(views['BC']), 'composed spectator pair not in E_BC matching')
            zeroes.append({'c': level, 'a': ai, 'd': di, 'matched_b': pi[level]})
        contexts.append({'C': c, 'B': b, 'A': a, 'D': d, 'sectors': views,
                         'P_CB_to_AD': [[list(x), list(y)] for x, y in sorted(cb_ad)],
                         'structural_zeroes': zeroes})
    return contexts


def validate_zero_for_choice(tensor, ctx, zero):
    a, d = ctx['A'], ctx['D']
    collisions = [list(ix) for ix, _ in p_entries(tensor)
                  if ix[a] == zero['a'] and ix[d] == zero['d']]
    if collisions:
        raise StructuralZeroError('structural-zero P entry at C=%d B=%d c=%d: %s' %
                                  (ctx['C'], ctx['B'], zero['c'], collisions))


def check_zeroes(tensor, contexts):
    for ctx in contexts:
        for zero in ctx['structural_zeroes']:
            validate_zero_for_choice(tensor, ctx, zero)


def gram_checks(tensor):
    # Source coefficients lie in Z[sqrt(2)]; Gram entries are pairs a+b*sqrt(2).
    checks = []
    for left in ((0, 1), (0, 2), (0, 3)):
        right = tuple(i for i in range(4) if i not in left)
        rows = {}
        for ix, coeff in tensor.items():
            row = tuple(ix[i] for i in left)
            col = tuple(ix[i] for i in right)
            rows.setdefault(row, {})[col] = coeff
        need(len(rows) == 36, 'missing 2|2 row')
        for x in itertools.product(range(6), repeat=2):
            for y in itertools.product(range(6), repeat=2):
                rational = radical = 0
                for col in set(rows[x]) & set(rows[y]):
                    u, v = rows[x][col], rows[y][col]
                    if u == 2 and v == 2:
                        rational += 2
                    elif u == 2:
                        radical += v
                    elif v == 2:
                        radical += u
                    else:
                        rational += u * v
                need((rational, radical) == ((2, 0) if x == y else (0, 0)),
                     'exact bipartite Gram mismatch')
        checks.append({'left': list(left), 'right': list(right), 'gram': '2 I_36 over Z[sqrt(2)]'})
    return checks


def contract_mod(tensor, ctx, t, u):
    m = [[0] * 6 for _ in range(6)]
    for ix, coeff in tensor.items():
        factor = 6 if coeff == 2 else coeff  # 6^2=2 in F_17.
        i, j = ix[ctx['A']], ix[ctx['D']]
        m[i][j] = (m[i][j] + factor * t[ix[ctx['C']]] * u[ix[ctx['B']]]) % P
    return m


def rank_mod(matrix):
    m = [[v % P for v in row] for row in matrix]
    r = 0
    for col in range(len(m[0])):
        pivot = next((i for i in range(r, len(m)) if m[i][col]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        inv = pow(m[r][col], -1, P)
        for i in range(r + 1, len(m)):
            f = m[i][col] * inv % P
            if f:
                for j in range(col, len(m[0])):
                    m[i][j] = (m[i][j] - f * m[r][j]) % P
        r += 1
        if r == len(m):
            break
    return r


def vector(indices, values):
    result = [0] * 6
    for i, value in zip(indices, values):
        result[i] = value
    return result


def check_minor_mod(m, zero):
    a, d = zero['a'], zero['d']
    need(m[a][d] == 0, 'mixed Z entry did not vanish')
    i = next((x for x in H if m[x][d]), None)
    j = next((x for x in H if m[a][x]), None)
    need(i is not None and j is not None, 'mixed X or Y vanished')
    determinant = (m[i][j] * m[a][d] - m[i][d] * m[a][j]) % P
    need(determinant != 0 and determinant == -m[i][d] * m[a][j] % P,
         'mixed 2x2 minor')
    return bool(m[i][j]), (i, j, determinant)


def bounded_field_controls(tensor, contexts):
    counts = {'H': 0, 'K': 0, 'K_rank_one': 0, 'mixed_minors': 0,
              'mixed_minors_with_nonzero_F_corner': 0, 'pure_H_complex_isotropic': 0}
    representative = None
    full_binary = [vector(range(6), v) for v in itertools.product((0, 1), repeat=6) if any(v)]
    h_binary = [vector(H, v) for v in itertools.product((0, 1), repeat=2) if any(v)]
    k_binary = [vector(K, v) for v in itertools.product((0, 1), repeat=4) if any(v)]
    for ctx in contexts:
        for t in h_binary:
            for u in full_binary:
                need(rank_mod(contract_mod(tensor, ctx, t, u)) >= 2, 'H contraction rank < 2')
                counts['H'] += 1
        # 4^2=-1 in F_17: genuine isotropic complex-like phase control.
        hm = contract_mod(tensor, ctx, vector(H, (1, 4)), vector(H, (1, 4)))
        need(rank_mod(hm) == 2, 'isotropic pure-H contraction')
        counts['pure_H_complex_isotropic'] += 1
        for t in k_binary:
            for u in full_binary:
                m = contract_mod(tensor, ctx, t, u)
                rank = rank_mod(m)
                need(rank >= 1, 'zero K contraction')
                counts['K'] += 1
                if u[H[0]] or u[H[1]]:
                    need(rank >= 2, 'mixed K contraction rank < 2')
                    for z in ctx['structural_zeroes']:
                        if t[z['c']]:
                            nonzero_f, chosen = check_minor_mod(m, z)
                            counts['mixed_minors'] += 1
                            if nonzero_f:
                                counts['mixed_minors_with_nonzero_F_corner'] += 1
                                if representative is None:
                                    representative = {'C': ctx['C'], 'B': ctx['B'],
                                        't': t, 'u': u, 'zero': z, 'i': chosen[0],
                                        'j': chosen[1], 'F_ij': m[chosen[0]][chosen[1]],
                                        'X': m[chosen[0]][z['d']], 'Y': m[z['a']][chosen[1]],
                                        'determinant_mod_17': chosen[2]}
                elif rank == 1:
                    counts['K_rank_one'] += 1
                    for z in ctx['structural_zeroes']:
                        if t[z['c']]:
                            need(u[z['matched_b']] == 0, 'rank-one vector outside W_t')
    need(representative is not None, 'no nonzero-F mixed minor found')
    return {'counts': counts, 'nonzero_F_corner_example': representative}


class Q:
    """Exact Q(i,sqrt(2)) element a+b*sqrt(2)+i(c+d*sqrt(2))."""
    def __init__(self, a=0, b=0, c=0, d=0):
        self.v = tuple(Fraction(x) for x in (a, b, c, d))

    def __bool__(self):
        return any(self.v)

    def __add__(self, other):
        return Q(*(x + y for x, y in zip(self.v, other.v)))

    def __neg__(self):
        return Q(*(-x for x in self.v))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        a, b, c, d = self.v
        e, f, g, h = other.v
        return Q(a*e + 2*b*f - c*g - 2*d*h,
                 a*f + b*e - c*h - d*g,
                 a*g + 2*b*h + c*e + 2*d*f,
                 a*h + b*g + c*f + d*e)

    def __truediv__(self, other):
        a, b, c, d = other.v
        n0 = a*a + 2*b*b + c*c + 2*d*d
        n1 = 2*(a*b + c*d)
        den = n0*n0 - 2*n1*n1
        need(den != 0, 'division by zero in exact complex field')
        v = self * Q(a, b, -c, -d) * Q(n0, -n1)
        return Q(*(x / den for x in v.v))

    def __eq__(self, other):
        return isinstance(other, Q) and self.v == other.v


def contract_q(tensor, ctx, t, u):
    m = [[Q() for _ in range(6)] for _ in range(6)]
    for ix, coeff in tensor.items():
        factor = Q(0, 1) if coeff == 2 else Q(coeff)
        i, j = ix[ctx['A']], ix[ctx['D']]
        m[i][j] = m[i][j] + factor * t[ix[ctx['C']]] * u[ix[ctx['B']]]
    return m


def rank_q(matrix):
    m = [row[:] for row in matrix]
    r = 0
    for col in range(len(m[0])):
        pivot = next((i for i in range(r, len(m)) if m[i][col]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        for i in range(r + 1, len(m)):
            if m[i][col]:
                f = m[i][col] / m[r][col]
                for j in range(col, len(m[0])):
                    m[i][j] = m[i][j] - f * m[r][j]
        r += 1
        if r == len(m):
            break
    return r


def qvec(indices, values):
    v = [Q() for _ in range(6)]
    for i, x in zip(indices, values):
        v[i] = x
    return v


def complex_controls(tensor, contexts):
    one, imag = Q(1), Q(0, 0, 1)
    need(imag * imag == Q(-1) and Q(0, 1) * Q(0, 1) == Q(2), 'exact field identities')
    counts = {'isotropic_pure_H_rank_two': 0, 'dense_mixed': 0,
              'mixed_zero_minors': 0, 'mixed_cases_with_nonzero_F': 0,
              'pure_K_matched_rank_two': 0, 'pure_K_nonmatched_rank_one': 0}
    for ctx in contexts:
        h = qvec(H, (one, imag))
        need(rank_q(contract_q(tensor, ctx, h, h)) == 2, 'complex isotropic H rank')
        counts['isotropic_pure_H_rank_two'] += 1
        t = qvec(K, (one, imag, one + imag, -one))
        u = qvec(range(6), (one, one, imag, -imag, imag, one - imag))
        m = contract_q(tensor, ctx, t, u)
        need(rank_q(m) >= 2, 'complex mixed contraction rank')
        counts['dense_mixed'] += 1
        if any(m[i][j] for i in H for j in H):
            counts['mixed_cases_with_nonzero_F'] += 1
        for z in ctx['structural_zeroes']:
            a, d = z['a'], z['d']
            need(not m[a][d], 'complex structural P zero')
            i = next((x for x in H if m[x][d]), None)
            j = next((x for x in H if m[a][x]), None)
            need(i is not None and j is not None, 'complex mixed X or Y zero')
            determinant = m[i][j] * m[a][d] - m[i][d] * m[a][j]
            need(bool(determinant) and determinant == -(m[i][d] * m[a][j]),
                 'complex mixed exact minor')
            counts['mixed_zero_minors'] += 1
        for z in ctx['structural_zeroes']:
            t = qvec((z['c'],), (one + imag,))
            for b in K:
                u = qvec((b,), (imag,))
                m = contract_q(tensor, ctx, t, u)
                if b == z['matched_b']:
                    need(all(not m[a][d] for a in K for d in K), 'matched pure-K Z nonzero')
                    need(rank_q(m) == 2, 'matched pure-K rank')
                    counts['pure_K_matched_rank_two'] += 1
                else:
                    need(all(not m[a][d] for a in H for d in H), 'nonmatched pure-K F nonzero')
                    need(rank_q(m) == 1, 'nonmatched pure-K rank')
                    counts['pure_K_nonmatched_rank_one'] += 1
    need(counts['mixed_cases_with_nonzero_F'] == len(contexts), 'complex mixed F control absent')
    return counts


def basis_controls(tensor, contexts):
    rng = random.Random(67028)
    bases = []
    for trial in range(13):
        basis = [[int(i == j) for j in range(6)] for i in range(6)]
        if trial:
            for _ in range(24):
                i, j = rng.sample(range(6), 2)
                k = rng.randrange(1, P)
                basis[i] = [(x + k*y) % P for x, y in zip(basis[i], basis[j])]
        need(rank_mod(basis) == 6, 'generated B rows not a basis')
        bases.append(basis)
    k_tests = [vector(K, v) for v in ((1,0,0,0), (0,1,0,0), (0,0,1,0),
                                      (0,0,0,1), (1,4,1,4))]
    h_tests = [vector(H, v) for v in ((1,0), (0,1), (1,4))]
    min_k_sum = 99
    min_h_sum = 99
    max_rank_one = 0
    cases = 0
    for ctx in contexts:
        for basis in bases:
            for t in k_tests:
                ranks = [rank_mod(contract_mod(tensor, ctx, t, u)) for u in basis]
                need(sum(ranks) >= 9, 'six B basis rank sum < 9')
                z = next(z for z in ctx['structural_zeroes'] if t[z['c']])
                rank_one_vectors = [u for u, r in zip(basis, ranks) if r == 1]
                for u in rank_one_vectors:
                    need(not u[1] and not u[2] and not u[z['matched_b']], 'basis rank-one W_t')
                need(len(rank_one_vectors) <= 3, 'too many rank-one basis vectors')
                min_k_sum = min(min_k_sum, sum(ranks))
                max_rank_one = max(max_rank_one, len(rank_one_vectors))
                cases += 1
            for t in h_tests:
                s = sum(rank_mod(contract_mod(tensor, ctx, t, u)) for u in basis)
                need(s >= 12, 'six H contractions rank sum < 12')
                min_h_sum = min(min_h_sum, s)
    return {'seed': 67028, 'bases': len(bases), 'ordered_orientations': len(contexts),
            'K_basis_cases': cases, 'minimum_K_rank_sum': min_k_sum,
            'minimum_H_rank_sum': min_h_sum, 'maximum_rank_one_vectors': max_rank_one}


def mutation_controls(tensor, contexts):
    inserted = 0
    for ctx in contexts:
        for z in ctx['structural_zeroes']:
            ix = [None] * 4
            ix[ctx['C']], ix[ctx['B']] = z['c'], K[0]
            ix[ctx['A']], ix[ctx['D']] = z['a'], z['d']
            ix = tuple(ix)
            need(ix not in tensor, 'inserted-P position already occupied')
            mutant = dict(tensor)
            mutant[ix] = 2
            try:
                validate_zero_for_choice(mutant, ctx, z)
            except StructuralZeroError as exc:
                need(str(exc).startswith('structural-zero P entry'), 'wrong insertion error')
            else:
                raise CheckError('inserted P was not rejected by structural-zero check')
            t = vector((z['c'],), (1,))
            u = vector((K[0], H[0]), (1, 1))
            before = contract_mod(tensor, ctx, t, u)[z['a']][z['d']]
            after = contract_mod(mutant, ctx, t, u)[z['a']][z['d']]
            need(before == 0 and after == 6, 'inserted P does not alter claimed full entry')
            inserted += 1
    # Independent sector-count and Pauli-family mutation controls.
    ctx = contexts[0]
    active, spectators = tuple(ctx['sectors']['AB']['active']), tuple(ctx['sectors']['AB']['spectators'])
    ix = next(ix for ix in tensor if {i for i in range(4) if ix[i] in H} == set(active))
    deleted = dict(tensor)
    del deleted[ix]
    try:
        sector_view(deleted, active, spectators)
    except CheckError as exc:
        need('expected eight entries' in str(exc), 'wrong deleted-E rejection reason')
    else:
        raise CheckError('deleted E coefficient accepted')
    flipped = dict(tensor)
    flipped[ix] = -flipped[ix]
    try:
        sector_view(flipped, active, spectators)
    except CheckError as exc:
        need('Pauli family has duplicates or omissions' in str(exc), 'wrong flipped-E rejection reason')
    else:
        raise CheckError('flipped E coefficient accepted')
    # Explicitly show why nonzero off-diagonal blocks, without the zero, do not force rank 2.
    need(rank_mod([[1, 1], [1, 1]]) == 1, 'naive mixed-block counterexample')
    return {'inserted_P_structural_zero_rejections_and_entry_changes': inserted,
            'deleted_E_rejected_for': 'expected eight entries',
            'flipped_E_rejected_for': 'Pauli family has duplicates or omissions',
            'naive_nonzero_X_Y_counterexample': {'matrix': [[1, 1], [1, 1]], 'rank': 1}}


def main():
    need(not RECEIPT.exists(), 'receipt already exists; refusing overwrite')
    table_bytes = SOURCE.read_bytes()  # Frozen source-read order: table, then candidate.
    tensor = parse_table(table_bytes)
    candidate_bytes = CANDIDATE.read_bytes()
    need(sha(candidate_bytes) == CANDIDATE_HASH, 'candidate SHA-256 mismatch')
    need(len(candidate_bytes) == 11896 and candidate_bytes.count(b'\n') == 85,
         'candidate byte/LF count mismatch')
    contexts = ordered_contexts(tensor)
    need(len(contexts) == 12 and sum(len(c['structural_zeroes']) for c in contexts) == 48,
         'orientation/zero incidence count')
    check_zeroes(tensor, contexts)
    receipt = {
        'kind': 'independent_same_harness_source_bound_controls',
        'table_sha256': sha(table_bytes), 'table_bytes': len(table_bytes),
        'candidate_sha256': sha(candidate_bytes), 'candidate_bytes': len(candidate_bytes),
        'manifest_sha256': sha(MANIFEST.read_bytes()),
        'checker_sha256': sha(Path(__file__).read_bytes()),
        'scope': 'Pinned table and repaired candidate only; no imported author code; no universal C proof from samples.',
        'source_entries': len(tensor), 'source_unnormalized_norm_squared': 72,
        'ordered_orientations': contexts,
        'exact_2_by_2_cut_gram_checks': gram_checks(tensor),
        'finite_field_controls': bounded_field_controls(tensor, contexts),
        'exact_complex_controls': complex_controls(tensor, contexts),
        'independent_B_basis_controls': basis_controls(tensor, contexts),
        'targeted_mutation_controls': mutation_controls(tensor, contexts),
    }
    # Detect drift before persisting evidence.  Rereads do not affect source ordering.
    need(sha(SOURCE.read_bytes()) == SOURCE_HASH and sha(CANDIDATE.read_bytes()) == CANDIDATE_HASH,
         'input drift before receipt')
    receipt['native_clock_immediately_before_receipt_write'] = subprocess.run(
        ['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], check=True, capture_output=True, text=True).stdout.strip()
    with RECEIPT.open('x', encoding='utf-8') as stream:
        json.dump(receipt, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({'status': 'PASS', 'receipt': str(RECEIPT),
                      'clock_before_receipt': receipt['native_clock_immediately_before_receipt_write'],
                      'finite': receipt['finite_field_controls']['counts'],
                      'exact_complex': receipt['exact_complex_controls'],
                      'bases': receipt['independent_B_basis_controls'],
                      'mutations': receipt['targeted_mutation_controls']}, sort_keys=True))


if __name__ == '__main__':
    main()
