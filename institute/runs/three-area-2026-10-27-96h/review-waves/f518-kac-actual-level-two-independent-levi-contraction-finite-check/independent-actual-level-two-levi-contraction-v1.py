from fractions import Fraction as Q
from time import monotonic

START = monotonic()
LIMIT = 54.0
ZERO, ONE = Q(0), Q(1)
GAPS = []


def tick():
    if monotonic() - START > LIMIT:
        print('TIMEOUT: no overall verification result', flush=True)
        raise SystemExit(3)


def require(condition, label):
    tick()
    if not condition:
        print('FAIL: ' + label, flush=True)
        raise SystemExit(1)


def zeros(m, n):
    return [[ZERO] * n for _ in range(m)]


def eye(n):
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = ONE
    return out


def unit(n, i):
    return tuple(ONE if j == i else ZERO for j in range(n))


def column(a, j):
    return tuple(row[j] for row in a)


def columns(vectors, n):
    if not vectors:
        return zeros(n, 0)
    require(all(len(v) == n for v in vectors), 'column dimensions')
    return [list(row) for row in zip(*vectors)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def select(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def vlin(*terms):
    n = len(terms[0][1])
    out = [ZERO] * n
    for c, v in terms:
        for i, x in enumerate(v):
            if c and x:
                out[i] += c * x
    return tuple(out)


def mlin(*terms):
    first = terms[0][1]
    out = zeros(len(first), len(first[0]))
    for c, a in terms:
        for i, row in enumerate(a):
            for j, x in enumerate(row):
                if c and x:
                    out[i][j] += c * x
    return out


def mv(a, v):
    tick()
    return tuple(sum((x * y for x, y in zip(row, v) if x and y), ZERO)
                 for row in a)


def mm(a, b):
    tick()
    require(len(a[0]) == len(b), 'matrix product dimensions')
    out = zeros(len(a), len(b[0]))
    for i, row in enumerate(a):
        tick()
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[i][j] += x * y
    return out


def bracket(a, b):
    return mlin((ONE, mm(a, b)), (-ONE, mm(b, a)))


def rref(a, n=None):
    tick()
    n = len(a[0]) if a else (0 if n is None else n)
    out = [list(row) for row in a]
    pivots = []
    row = 0
    for col in range(n):
        tick()
        pivot = next((i for i in range(row, len(out)) if out[i][col]), None)
        if pivot is None:
            continue
        out[row], out[pivot] = out[pivot], out[row]
        scale = out[row][col]
        out[row] = [x / scale for x in out[row]]
        for i in range(len(out)):
            if i != row and out[i][col]:
                scale = out[i][col]
                out[i] = [x - scale * y for x, y in zip(out[i], out[row])]
        pivots.append(col)
        row += 1
        if row == len(out):
            break
    return out, pivots


def rank(a, n=None):
    return len(rref(a, n)[1])


def inverse(a):
    n = len(a)
    augmented = [row[:] + eye(n)[i] for i, row in enumerate(a)]
    reduced, pivots = rref(augmented)
    require(pivots == list(range(n)), 'inverse has full left rank')
    return [row[n:] for row in reduced]


def nullspace(a, n):
    reduced, pivots = rref(a, n)
    free = [j for j in range(n) if j not in pivots]
    answer = []
    for j in free:
        v = [ZERO] * n
        v[j] = ONE
        for i, p in enumerate(pivots):
            v[p] = -reduced[i][j]
        answer.append(tuple(v))
    return answer


def determinant(a):
    if not a:
        return ONE
    out = [row[:] for row in a]
    result = ONE
    for col in range(len(out)):
        tick()
        pivot = next((i for i in range(col, len(out)) if out[i][col]), None)
        if pivot is None:
            return ZERO
        if pivot != col:
            out[col], out[pivot] = out[pivot], out[col]
            result = -result
        scale = out[col][col]
        result *= scale
        for i in range(col + 1, len(out)):
            if out[i][col]:
                factor = out[i][col] / scale
                for j in range(col + 1, len(out)):
                    out[i][j] -= factor * out[col][j]
                out[i][col] = ZERO
    return result


class Span:
    def __init__(self, n):
        self.n = n
        self.pivots = {}
        self.vectors = []
        self.tags = []

    def residual(self, v):
        tick()
        out = list(v)
        for p in sorted(self.pivots):
            c = out[p]
            if c:
                out = [x - c * y for x, y in zip(out, self.pivots[p])]
        return tuple(out)

    def contains(self, v):
        return not any(self.residual(v))

    def add(self, v, tag=''):
        out = self.residual(v)
        p = next((i for i, x in enumerate(out) if x), None)
        if p is None:
            return False
        self.pivots[p] = tuple(x / out[p] for x in out)
        self.vectors.append(tuple(v))
        self.tags.append(tag)
        return True


def span_of(vectors, n):
    answer = Span(n)
    for v in vectors:
        answer.add(v)
    return answer


def cyclic(seed, operators):
    space = Span(len(seed))
    space.add(seed, 'seed')
    index = 0
    while index < len(space.vectors):
        tick()
        v, tag = space.vectors[index], space.tags[index]
        for name, a in operators:
            space.add(mv(a, v), name + '(' + tag + ')')
        index += 1
    return space


def require_stable(space, operators, label):
    for name, a in operators:
        for v in space.vectors:
            require(space.contains(mv(a, v)), label + ' stable under ' + name)


def exterior_pairs(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def wedge(v, w, pairs):
    return tuple(v[i] * w[j] - v[j] * w[i] for i, j in pairs)


def exterior_action(a, pairs):
    n = len(a)
    standard = [unit(n, i) for i in range(n)]
    return columns([
        vlin((ONE, wedge(column(a, i), standard[j], pairs)),
             (ONE, wedge(standard[i], column(a, j), pairs)))
        for i, j in pairs
    ], len(pairs))


def homogeneous(v, degrees):
    support = {degrees[i] for i, x in enumerate(v) if x}
    require(len(support) == 1, 'nonzero homogeneous cyclic basis vector')
    return next(iter(support))


def mutant(label, witness):
    tick()
    if witness is None:
        GAPS.append(label)
        print('NOT_TESTED: ' + label + ': no separating witness', flush=True)
    else:
        print('DETECTED: ' + label + ': ' + witness, flush=True)


def cell(i, j):
    out = zeros(3, 3)
    out[i][j] = ONE
    return out


# The eight source letters are constructed, not imported as action tables.
e1, e2, f1, f2 = cell(0, 1), cell(1, 2), cell(1, 0), cell(2, 1)
u0 = cell(2, 0)
u1, u2 = bracket(e1, u0), bracket(e2, u0)
u3, u4 = bracket(e1, u2), bracket(e2, u1)
u5 = mlin((-Q(1, 2), bracket(e1, u3)))
u6 = mlin((Q(1, 2), bracket(e2, u4)))
u7 = bracket(e1, u6)
U = [u0, u1, u2, u3, u4, u5, u6, u7]
DEGREES = [(0, 0), (1, 0), (0, 1), (1, 1), (1, 1),
           (2, 1), (1, 2), (2, 2)]
FLAT = [tuple(x for row in a for x in row) for a in U]
P = columns(FLAT, 9)
row_space, selected_rows = Span(8), []
for i, row in enumerate(P):
    if row_space.add(row):
        selected_rows.append(i)
require(len(selected_rows) == 8, 'adjoint letters have dimension eight')
P_INV = inverse(select(P, selected_rows, list(range(8))))


def coordinates(a):
    flat = tuple(x for row in a for x in row)
    out = mv(P_INV, tuple(flat[i] for i in selected_rows))
    require(mv(P, out) == flat, 'matrix lies in adjoint span')
    return out


def adjoint(a):
    return columns([coordinates(bracket(a, u)) for u in U], 8)


EV = [adjoint(e1), adjoint(e2)]
FV = [adjoint(f1), adjoint(f2)]
HV = [bracket(EV[i], FV[i]) for i in range(2)]
A12 = [[2, -1], [-1, 2]]
for i in range(2):
    for j in range(2):
        require(bracket(HV[i], EV[j]) == mlin((A12[i][j], EV[j])),
                'adjoint Cartan/raising relation')
        require(bracket(HV[i], FV[j]) == mlin((-A12[i][j], FV[j])),
                'adjoint Cartan/lowering relation')
        if i != j:
            require(not any(map(any, bracket(EV[i], FV[j]))),
                    'adjoint mixed Chevalley relation')
            require(not any(map(any, bracket(EV[i], bracket(EV[i], EV[j])))),
                    'adjoint positive A2 Serre')
            require(not any(map(any, bracket(FV[i], bracket(FV[i], FV[j])))),
                    'adjoint negative A2 Serre')
GRAM = [[sum((x * y for x, y in zip(a, b)), ZERO) for b in FLAT]
        for a in FLAT]
GRAM_INV = inverse(GRAM)
expected_gram = eye(8)
expected_gram[3][3] = expected_gram[4][4] = Q(2)
expected_gram[3][4] = expected_gram[4][3] = ONE
require(GRAM == expected_gram, 'derived trace-transpose Gram block')
require(GRAM_INV[3][3] == Q(2, 3) and GRAM_INV[3][4] == -Q(1, 3),
        'derived inverse Gram thirds')
for i in range(2):
    require(mm(transpose(EV[i]), GRAM) == mm(GRAM, FV[i]),
            'derived contravariant form')
PAIRS = exterior_pairs(8)
PAIR_INDEX = {p: i for i, p in enumerate(PAIRS)}
D28 = len(PAIRS)
require(D28 == 28, 'exterior source dimension')
EH = [exterior_action(a, PAIRS) for a in EV]
FH = [exterior_action(a, PAIRS) for a in FV]
OPS = [('E1', EH[0]), ('E2', EH[1]), ('F1', FH[0]), ('F2', FH[1])]
PAIR_DEGREES = [(DEGREES[i][0] + DEGREES[j][0],
                 DEGREES[i][1] + DEGREES[j][1]) for i, j in PAIRS]
qr = unit(D28, PAIR_INDEX[(0, 1)])
qs = unit(D28, PAIR_INDEX[(0, 2)])
y = vlin((ONE, unit(D28, PAIR_INDEX[(0, 3)])),
         (-ONE, unit(D28, PAIR_INDEX[(0, 4)])),
         (-ONE, unit(D28, PAIR_INDEX[(1, 2)])))
for seed in [qr, qs, y]:
    for a in FH:
        require(not any(mv(a, seed)), 'three seeds are Levi-lowest')
CYCLIC = [cyclic(seed, OPS[:2]) for seed in [qr, qs, y]]
require([len(s.vectors) for s in CYCLIC] == [10, 10, 8],
        'independently generated complete cyclic dimensions')
for i, space in enumerate(CYCLIC):
    require_stable(space, OPS, 'complete summand ' + str(i))
BASIS_VECTORS = [v for space in CYCLIC for v in space.vectors]
B = columns(BASIS_VECTORS, D28)
B_INV = inverse(B)
B_DEGREES = [homogeneous(v, PAIR_DEGREES) for v in BASIS_VECTORS]
B_TAGS = [tag for space in CYCLIC for tag in space.tags]
EMIT = [columns([wedge(unit(8, i), unit(8, j), PAIRS)
                 for j in range(8)], D28) for i in range(8)]
MU = [[x for a in EMIT for x in a[i]] for i in range(D28)]


def f3_matrix(r, s):
    h3 = zeros(8, 8)
    for i, (a, b) in enumerate(DEGREES):
        h3[i][i] = Q(2 - r * a - s * b)
    require(bracket(h3, EV[0]) == mlin((-r, EV[0])), 'h3 row/r parameter')
    require(bracket(h3, EV[1]) == mlin((-s, EV[1])), 'h3 row/s parameter')

    def raise_extended(value, e, p):
        x, t = value
        return mlin((ONE, bracket(e, x)), (t * p, e)), ZERO

    def scale_extended(c, value):
        x, t = value
        return mlin((c, x)), c * t

    # F3u0=-h3; [F3,E1]=[F3,E2]=0.  On Levi12,
    # [e1,h3]=r e1 and [e2,h3]=s e2.
    b0 = (zeros(3, 3), -ONE)
    b1 = raise_extended(b0, e1, r)
    b2 = raise_extended(b0, e2, s)
    b3 = raise_extended(b2, e1, r)
    b4 = raise_extended(b1, e2, s)
    b5 = scale_extended(-Q(1, 2), raise_extended(b3, e1, r))
    b6 = scale_extended(Q(1, 2), raise_extended(b4, e2, s))
    b7 = raise_extended(b6, e1, r)
    values = [b0, b1, b2, b3, b4, b5, b6, b7]
    actions = [mlin((ONE, adjoint(x)), (t, h3)) for x, t in values]
    return columns([vlin((ONE, column(actions[i], j)),
                         (-ONE, column(actions[j], i))) for i, j in PAIRS], 8)


def dual_words(d, gv, rv, gh, rh):
    def comm(w, av, ah):
        return mlin((ONE, mm(w, ah)), (-ONE, mm(av, w)))
    w0 = d
    w1, w2 = comm(w0, gv, gh), comm(w0, rv, rh)
    w3, w4 = comm(w2, gv, gh), comm(w1, rv, rh)
    w5 = mlin((-Q(1, 2), comm(w3, gv, gh)))
    w6 = mlin((Q(1, 2), comm(w4, rv, rh)))
    w7 = comm(w6, gv, gh)
    return [w0, w1, w2, w3, w4, w5, w6, w7]


def contraction(words, gram_inverse):
    blocks = [mlin(*[(gram_inverse[i][j], words[j]) for j in range(8)
                     if gram_inverse[i][j]]) for i in range(8)]
    c = [row[:] for block in blocks for row in block]
    a = mlin(*[(ONE, mm(EMIT[i], blocks[i])) for i in range(8)])
    require(a == mm(MU, c), 'all eight coevaluation blocks reach consuming bracket')
    return a, c


def spectral_witness(a, active, lambdas, raised_only=False):
    for j in active:
        if raised_only and B_TAGS[j] == 'seed':
            continue
        residual = mv(B_INV, vlin((ONE, mv(a, BASIS_VECTORS[j])),
                                 (-lambdas[j], BASIS_VECTORS[j])))
        visible = [(i, str(residual[i])) for i in active if residual[i]]
        if visible:
            return ('basis=' + str(j) + ', degree=' + str(B_DEGREES[j]) +
                    ', word=' + B_TAGS[j] + ', quotient residual=' + str(visible))
    return None


for r, s in [(1, 2), (1, 3), (2, 3), (3, 4)]:
    label = 'r=' + str(r) + ',s=' + str(s)
    d = f3_matrix(r, s)
    for i in range(2):
        require(mm(d, EH[i]) == mm(EV[i], d), 'F3 commutes with E' + str(i + 1))
    for j, degree in enumerate(PAIR_DEGREES):
        require(all(not d[i][j] or DEGREES[i] == degree for i in range(8)),
                'F3 retains both horizontal degrees')
    require(mv(d, qr) == vlin((2 * (r - 1), unit(8, 1))), 'actual F3 qr')
    require(mv(d, qs) == vlin((2 * (s - 1), unit(8, 2))), 'actual F3 qs')
    require(mv(d, y) == vlin((3 * r + 2 * s - 2, unit(8, 3)),
                            (-(2 * r + 3 * s - 2), unit(8, 4))), 'actual F3 y')
    words = dual_words(d, FV[0], FV[1], FH[0], FH[1])
    a, c = contraction(words, GRAM_INV)
    for name, op in OPS:
        require(mm(a, op) == mm(op, a), 'all-four full Levi equivariance ' + name)
    lr, ls, l0 = Q(4 * (r - 1)), Q(4 * (s - 1)), Q(5 * (r + s) - 4)
    lambdas = [lr] * 10 + [ls] * 10 + [l0] * 8
    expected = zeros(D28, D28)
    for j, value in enumerate(lambdas):
        expected[j][j] = value
    in_basis = mm(B_INV, mm(a, B))
    require(in_basis == expected, 'full independently constructed spectrum ' + label)
    active = list(range(10 if r == 1 else 0, D28))
    relation = CYCLIC[0] if r == 1 else Span(D28)
    for v in relation.vectors:
        require(not any(mv(d, v)), 'whole relation killed by F3')
        for w in words:
            require(not any(mv(w, v)), 'whole relation killed by each dual channel')
        require(not any(mv(c, v)), 'coevaluation descends through entire relation')
    kernel = nullspace(a, D28)
    require(len(kernel) == len(relation.vectors), 'full contraction kernel dimension')
    require(all(relation.contains(v) for v in kernel), 'kernel equals entire relation')
    aq = select(in_basis, active, active)
    require(rank(aq) == len(active), 'actual quotient invertibility')
    require(all(lambdas[j] > 0 for j in active), 'all surviving scalars positive')
    cq = mm(c, columns([BASIS_VECTORS[j] for j in active], D28))
    require(rank(cq) == len(active), 'actual coevaluation has zero kernel')
    require(rank(mm(MU, cq)) == rank(cq), 'image C meets kernel mu trivially')
    for name, op in OPS:
        oq_full = mm(B_INV, mm(op, B))
        if r == 1:
            require(not any(oq_full[i][j] for i in active for j in range(10)),
                    'complete relation ideal stability ' + name)
        oq = select(oq_full, active, active)
        require(mm(aq, oq) == mm(oq, aq), 'quotient equivariance ' + name)
    slice_determinant = ONE
    slice_dimension = 0
    maximum_a = max(degree[0] for degree in PAIR_DEGREES)
    for horizontal in range(maximum_a + 1):
        indices = [j for j in active if B_DEGREES[j] == (horizontal, 2)]
        block = select(in_basis, indices, indices)
        actual_dimension = len(indices)
        actual_determinant = determinant(block)
        if horizontal in (1, 2, 3):
            middle = horizontal == 2
            predicted_dimension = (2 if r == 1 else 3) + int(middle)
            predicted_determinant = l0 ** (2 if middle else 1) * ls
            if r != 1:
                predicted_determinant *= lr
        else:
            predicted_dimension, predicted_determinant = 0, ONE
        require(actual_dimension == predicted_dimension, 'complete b2 component dimension')
        require(actual_determinant == predicted_determinant, 'complete b2 determinant')
        slice_dimension += actual_dimension
        slice_determinant *= actual_determinant
        print('COMPONENT ' + label + ',a=' + str(horizontal) + ',b=2,n=2: dim=' +
              str(actual_dimension) + ',det=' + str(actual_determinant), flush=True)
    predicted_total = l0 ** 4 * ls ** 3 * (lr ** 3 if r != 1 else ONE)
    require(slice_determinant == predicted_total, 'whole b2 determinant')
    require(slice_dimension == (7 if r == 1 else 10), 'whole b2 dimension')
    print('BASELINE ' + label + ': whole level2 dim=' + str(len(active)) +
          ',full-kernel-dim=' + str(len(kernel)), flush=True)
    for omitted in (5, 6, 7):
        broken = words[:]
        broken[omitted] = zeros(8, D28)
        bad, unused = contraction(broken, GRAM_INV)
        mutant(label + ' omit W' + str(omitted) + ' on raised actual vectors',
               spectral_witness(bad, active, lambdas, True))
    broken_gram = [row[:] for row in GRAM_INV]
    broken_gram[3][4] = broken_gram[4][3] = Q(1, 3)
    bad, unused = contraction(words, broken_gram)
    mutant(label + ' wrong mixed inverse-Gram signs', spectral_witness(bad, active, lambdas))
    transposed_words = dual_words(d, transpose(FV[0]), transpose(FV[1]),
                                 transpose(FH[0]), transpose(FH[1]))
    bad, unused = contraction(transposed_words, GRAM_INV)
    mutant(label + ' wrong lowering transpose', spectral_witness(bad, active, lambdas))
    for name, mr, ms in [('transposed Cartan row', 1, 1), ('swapped r,s', s, r)]:
        wrong_d = f3_matrix(mr, ms)
        delta = vlin((ONE, mv(wrong_d, qs)), (-ONE, mv(d, qs)))
        if not any(delta):
            delta = vlin((ONE, mv(wrong_d, qr)), (-ONE, mv(d, qr)))
        mutant(label + ' ' + name,
               ('actual F3 seed difference=' + str(delta)) if any(delta) else None)
    if r == 1:
        seed_only = span_of([qr], D28)
        outside = mv(EH[1], qr)
        mutant(label + ' remove only relation seed',
               ('E2(qr) outside rank-one relation; full rank=' +
                str(len(relation.vectors))) if not seed_only.contains(outside) else None)
    # This is a logical scope guard, not a model of the actual radical.
    ys = CYCLIC[2]
    antecedent = determinant(aq) != 0 and len(ys.vectors) > 0
    antecedent = antecedent and all(ys.contains(mv(a, v)) for v in ys.vectors)
    mutant(label + ' infer radical vanishing from invertibility alone',
           ('nonzero eight-dimensional A-stable y-summand coexists with invertible A; '
            'its F3(y) is nonzero, so ideal exclusion needs the separate lower-grade premise')
           if antecedent and any(mv(d, y)) else None)


for s in (3, 4):
    n = s + 1
    pairs = exterior_pairs(n)
    index = {pair: i for i, pair in enumerate(pairs)}
    size = len(pairs)
    t, lower = zeros(n, n), zeros(n, n)
    for i in range(n):
        if i < s:
            t[i + 1][i] = ONE
        if i:
            lower[i - 1][i] = Q(i * (s - i + 1))
    h = zeros(n, n)
    for i in range(n):
        h[i][i] = Q(2 * i - s)
    require(bracket(t, lower) == h, 'boundary node3 string Chevalley action')
    th, lh = exterior_action(t, pairs), exterior_action(lower, pairs)
    relation = cyclic(unit(size, index[(0, 1)]), [('T', th)])
    require(len(relation.vectors) == 2 * s - 1, 'whole boundary relation dimension')
    require_stable(relation, [('T', th), ('F3', lh)], 'boundary relation')
    # Derive F2(T^i v) recursively: F2v=-h2,
    # [e3,h2]=e3 and [e3,e3]=0.  Pairs hold h2/e3 coefficients.
    values = [(-ONE, ZERO)]
    for i in range(s):
        values.append((ZERO, values[-1][0]))

    def action(value, j):
        a0, b0 = value
        out = vlin((a0 * (2 - j), unit(n, j)))
        if j < s:
            out = vlin((ONE, out), (b0, unit(n, j + 1)))
        return out

    f2_boundary = columns([
        vlin((ONE, action(values[i], j)), (-ONE, action(values[j], i)))
        for i, j in pairs
    ], n)
    require(mm(f2_boundary, th) == mm(t, f2_boundary), 'boundary F2 commutes with E3')
    require(all(not any(mv(f2_boundary, v)) for v in relation.vectors),
            'boundary F2 annihilates complete relation closure')
    strings = []
    f2_mutation_witness = None
    for k in range(3, s + 1, 2):
        support = [j for j, (a0, b0) in enumerate(pairs) if a0 + b0 == k]
        targets = [j for j, (a0, b0) in enumerate(pairs) if a0 + b0 == k - 1]
        kernels = nullspace(select(lh, targets, support), len(support))
        require(len(kernels) == 1, 'unique boundary lowest line from independent kernel')
        coefficients = kernels[0]
        leading = support.index(index[(0, k)])
        require(coefficients[leading] != 0, 'boundary lowest vector leading normalization')
        coefficients = tuple(x / coefficients[leading] for x in coefficients)
        lowest = [ZERO] * size
        for i, j in enumerate(support):
            lowest[j] = coefficients[i]
        lowest = tuple(lowest)
        require(not any(mv(lh, lowest)), 'boundary yk is F3-lowest')
        require(not relation.contains(lowest), 'boundary lowest survives actual quotient')
        coefficient = ONE
        for i in range((k - 1) // 2 + 1):
            require(lowest[index[(i, k - i)]] == coefficient, 'author yk recurrence matches kernel')
            if i < (k - 1) // 2:
                coefficient *= -Q((k - i) * (s - k + i + 1), (i + 1) * (s - i))
        actual = mv(f2_boundary, lowest)
        expected_coefficient = Q((k - 1) * (2 * s - k), s)
        require(actual == vlin((expected_coefficient, unit(n, k))), 'actual nonzero F2 yk')
        require(any(actual), 'actual F2 yk does not vanish')
        f2_mutation_witness = 's=' + str(s) + ',k=' + str(k) + ',F2yk=' + str(actual)
        z = unit(n, k)
        for i in range(k):
            z = mv(lower, z)
        factor = ONE
        for i in range(1, k + 1):
            factor *= i * (s - i + 1)
        require(z == vlin((factor, unit(n, 0))), 'nonzero finite node3 return to v')
        string = cyclic(lowest, [('T', th)])
        length = 2 * s - 2 * k + 1
        require(len(string.vectors) == length, 'complete boundary survivor string dimension')
        for j, v in enumerate(string.vectors):
            require(homogeneous(v, [a0 + b0 for a0, b0 in pairs]) == k + j,
                    'boundary survivor exact grade')
            previous = string.vectors[j - 1] if j else (ZERO,) * size
            require(mv(lh, v) == vlin((j * (length - j), previous)),
                    'complete boundary survivor lowering coefficients')
        require(not any(mv(th, string.vectors[-1])), 'complete boundary string top')
        strings.append(string)
        print('BOUNDARY s=' + str(s) + ',k=' + str(k) + ',string-dim=' + str(length) +
              ',F2-coefficient=' + str(expected_coefficient), flush=True)
    all_vectors = relation.vectors + [v for string in strings for v in string.vectors]
    require(len(all_vectors) == size and rank(columns(all_vectors, size)) == size,
            'boundary relation plus complete survivors exhaust exterior source')
    degrees = [a0 + b0 for a0, b0 in pairs]
    relation_degrees = [homogeneous(v, degrees) for v in relation.vectors]
    actual_degrees = [homogeneous(v, degrees) for string in strings for v in string.vectors]
    dimensions = []
    for grade in range(2 * s + 1):
        raw = sum(degree == grade for degree in degrees)
        removed = sum(degree == grade for degree in relation_degrees)
        actual_dim = sum(degree == grade for degree in actual_degrees)
        formula = sum(k <= grade <= 2 * s - k for k in range(3, s + 1, 2))
        require(raw - removed == actual_dim == formula, 'complete boundary component dimension')
        dimensions.append(actual_dim)
    mutant('boundary forced-zero F2 coefficient', f2_mutation_witness)
    print('BOUNDARY s=' + str(s) + ': dimensions n=0..' + str(2 * s) + ': ' +
          str(dimensions), flush=True)

print('SCOPE: exact finite models conditional on frozen actual-source interfaces; '
      'no universal negative-Serre bridge or actual tau/J computed', flush=True)
if GAPS:
    print('BASELINES_PASS; MUTATION_GAPS: ' + '; '.join(GAPS), flush=True)
    raise SystemExit(2)
print('BASELINES_PASS; ALL_LISTED_MUTATIONS_DETECTED; elapsed=' +
      format(monotonic() - START, '.6f') + 's', flush=True)
