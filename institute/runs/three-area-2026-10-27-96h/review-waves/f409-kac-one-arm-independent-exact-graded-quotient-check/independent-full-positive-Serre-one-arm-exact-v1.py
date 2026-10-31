import sys
import time
from collections import deque
from fractions import Fraction as F
from math import gcd

START = time.monotonic()
DEADLINE = START + 53.0
MAX_POLY_TERMS = 100000
MAX_STORED_TERMS = 500000


class Incomplete(Exception):
    pass


class ScientificFailure(Exception):
    pass


def guard():
    if time.monotonic() >= DEADLINE:
        raise Incomplete("cooperative 53-second deadline")


def require(condition, label, witness=None):
    guard()
    if not condition:
        text = label
        if witness is not None:
            text += ": " + repr(witness)
        raise ScientificFailure(text)


def tidy(p):
    guard()
    q = {w: c for w, c in p.items() if c}
    if len(q) > MAX_POLY_TERMS:
        raise Incomplete("single-polynomial sparse-storage bound")
    return q


def lin(*terms):
    out = {}
    for factor, p in terms:
        guard()
        if not factor:
            continue
        for w, c in p.items():
            z = out.get(w, 0) + factor * c
            if z:
                out[w] = z
            else:
                out.pop(w, None)
    return tidy(out)


def bracket(p, q):
    guard()
    out = {}
    steps = 0
    for w, c in p.items():
        for z, d in q.items():
            value = c * d
            wz = w + z
            zw = z + w
            out[wz] = out.get(wz, 0) + value
            out[zw] = out.get(zw, 0) - value
            steps += 1
            if steps % 256 == 0:
                guard()
    return tidy(out)


GEN = [{(i,): 1} for i in range(3)]


def act(roots, p):
    for root in reversed(roots):
        p = bracket(root, p)
    return p


def ad_power(root, count, p):
    for unused in range(count):
        p = bracket(root, p)
    return p


def word_degree(w):
    return tuple(w.count(i) for i in range(3))


def poly_degree(p):
    if not p:
        raise Incomplete("degree requested for zero polynomial")
    d = word_degree(next(iter(p)))
    if any(word_degree(w) != d for w in p):
        raise Incomplete("inhomogeneous polynomial")
    return d


def primitive(p):
    p = tidy(p)
    if not p:
        return {}
    denominator = 1
    for c in p.values():
        d = F(c).denominator
        denominator = denominator * d // gcd(denominator, d)
    out = {w: int(F(c) * denominator) for w, c in p.items()}
    common = 0
    for c in out.values():
        common = gcd(common, abs(c))
    if common != 1:
        out = {w: c // common for w, c in out.items()}
    if out[min(out)] < 0:
        out = {w: -c for w, c in out.items()}
    return out


class TensorSpan:
    def __init__(self, rows=None):
        self.rows = {} if rows is None else dict(rows)

    def insert(self, p):
        p = primitive(p)
        while p:
            guard()
            pivot = min(p)
            row = self.rows.get(pivot)
            if row is None:
                self.rows[pivot] = p
                return p
            a = p[pivot]
            b = row[pivot]
            common = gcd(abs(a), abs(b))
            p = primitive(lin((b // common, p), (-a // common, row)))
        return None


class QuotientReducer:
    def __init__(self, ideal):
        self.span = TensorSpan(ideal.rows)
        self.labels = {}
        self.basis = []

    def insert(self, p):
        row = self.span.insert(p)
        if row is not None:
            pivot = min(row)
            self.labels[pivot] = len(self.basis)
            self.basis.append(row)

    def coordinates(self, p):
        p = {w: F(c) for w, c in p.items() if c}
        result = [F(0) for unused in self.basis]
        while p:
            guard()
            pivot = min(p)
            row = self.span.rows.get(pivot)
            if row is None:
                raise Incomplete(
                    "positive Lie vector outside constructed span: "
                    + repr((pivot, p[pivot]))
                )
            factor = p[pivot] / row[pivot]
            label = self.labels.get(pivot)
            if label is not None:
                result[label] += factor
            p = lin((1, p), (-factor, row))
        return result


def cartan(r, s):
    return ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))


def all_seeds(A):
    seeds = []
    for i in range(3):
        for j in range(3):
            if i != j:
                p = ad_power(GEN[i], 1 - A[i][j], GEN[j])
                seeds.append(((i, j), poly_degree(p), p))
    require(len(seeds) == 6, "six distinct positive seed identities")
    return seeds


class PositiveQuotient:
    def __init__(self, A, bounds, omit=None):
        self.A = A
        self.bounds = tuple(bounds)
        self.ideal = {}
        self.reducers = {}
        self.seed_metadata = []
        seeds_at = {}
        for name, d, p in all_seeds(A):
            present = all(d[i] <= self.bounds[i] for i in range(3))
            self.seed_metadata.append((name, d, present, name == omit))
            if present and name != omit:
                seeds_at.setdefault(d, []).append(p)
        degrees = [
            (a, b, n)
            for a in range(bounds[0] + 1)
            for b in range(bounds[1] + 1)
            for n in range(bounds[2] + 1)
            if a + b + n
        ]
        degrees.sort(key=lambda d: (sum(d), d))
        stored = 0
        for d in degrees:
            guard()
            ideal = TensorSpan()
            for p in seeds_at.get(d, []):
                ideal.insert(p)
            for i in range(3):
                if d[i] == 0:
                    continue
                previous = list(d)
                previous[i] -= 1
                previous = tuple(previous)
                old = self.ideal.get(previous)
                if old is not None:
                    for row in old.rows.values():
                        ideal.insert(bracket(GEN[i], row))
            quotient = QuotientReducer(ideal)
            if sum(d) == 1:
                quotient.insert(GEN[d.index(1)])
            for i in range(3):
                if d[i] == 0:
                    continue
                previous = list(d)
                previous[i] -= 1
                old = self.reducers.get(tuple(previous))
                if old is not None:
                    for row in old.basis:
                        quotient.insert(bracket(GEN[i], row))
            self.ideal[d] = ideal
            self.reducers[d] = quotient
            stored += sum(len(p) for p in ideal.rows.values())
            stored += sum(len(p) for p in quotient.basis)
            if stored > MAX_STORED_TERMS:
                raise Incomplete("stored sparse tensor-term bound")

    def basis(self, d):
        if any(d[i] < 0 or d[i] > self.bounds[i] for i in range(3)):
            raise Incomplete("quotient basis requested outside constructed box")
        reducer = self.reducers.get(tuple(d))
        return [] if reducer is None else reducer.basis

    def coordinates(self, p, d):
        guard()
        if any(x < 0 for x in d):
            require(not p, "negative-coordinate support", (d, p))
            return []
        if any(d[i] > self.bounds[i] for i in range(3)):
            raise Incomplete("coordinate target outside constructed box")
        if p:
            require(poly_degree(p) == tuple(d), "homogeneous target", (d, p))
        reducer = self.reducers.get(tuple(d))
        if reducer is None:
            require(not p, "nonzero degree-zero positive target", p)
            return []
        return reducer.coordinates(p)


def lower_raw(i, p, A):
    positive = {}
    right_cartan = {}
    for w, c in p.items():
        guard()
        suffix_weight = 0
        for k in range(len(w) - 1, -1, -1):
            if w[k] == i:
                deleted = w[:k] + w[k + 1:]
                right_cartan[deleted] = right_cartan.get(deleted, 0) - c
                positive[deleted] = (
                    positive.get(deleted, 0) - c * suffix_weight
                )
            suffix_weight += A[i][w[k]]
    return tidy(positive), tidy(right_cartan)


def lower(i, p, A):
    positive, right_cartan = lower_raw(i, p, A)
    if right_cartan:
        raise Incomplete(
            "unexpected right-Cartan target in positive-only action: "
            + repr((i, right_cartan))
        )
    return positive


def theta(p):
    return tidy({tuple(reversed(w)): c for w, c in p.items()})


def apply_negative(op, p, A):
    out = {}
    for word, coefficient in op.items():
        guard()
        term = p
        for i in reversed(word):
            term = lower(i, term, A)
            if not term:
                break
        out = lin((1, out), (coefficient, term))
    return out


def normal_order_controls(A):
    for i in range(3):
        for j in range(3):
            positive, tail = lower_raw(i, GEN[j], A)
            require(not positive, "simple negative action positive part")
            wanted = {(): -1} if i == j else {}
            require(tail == wanted, "[f_i,e_j] Cartan control", (i, j, tail))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                positive, tail = lower_raw(i, bracket(GEN[j], GEN[k]), A)
                require(not tail, "Lie commutator right-Cartan cancellation")
                if positive:
                    require(
                        all(len(w) == 1 for w in positive),
                        "degree-two lowering degree",
                        positive,
                    )


def columns_matrix(columns, height):
    return [[F(c[i]) for c in columns] for i in range(height)]


def column(A, j):
    return [row[j] for row in A]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def mv(A, v):
    guard()
    if A:
        require(len(A[0]) == len(v), "matrix/vector dimensions")
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in A]


def multiply(A, B):
    guard()
    if not A:
        return []
    require(len(A[0]) == len(B), "matrix product dimensions")
    width = len(B[0]) if B else 0
    return [
        [
            sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
            for j in range(width)
        ]
        for i in range(len(A))
    ]


def rref(A, variable_columns):
    R = [[F(x) for x in row] for row in A]
    pivots = []
    row = 0
    for j in range(variable_columns):
        guard()
        pivot = next((i for i in range(row, len(R)) if R[i][j]), None)
        if pivot is None:
            continue
        R[row], R[pivot] = R[pivot], R[row]
        value = R[row][j]
        R[row] = [x / value for x in R[row]]
        for i in range(len(R)):
            if i != row and R[i][j]:
                value = R[i][j]
                R[i] = [x - value * y for x, y in zip(R[i], R[row])]
        pivots.append(j)
        row += 1
        if row == len(R):
            break
    return R, pivots


def rank(A, width):
    return len(rref(A, width)[1])


def coordinates_in_columns(C, y):
    require(len(C) == len(y), "rectangular coordinate target dimension")
    width = len(C[0]) if C else 0
    augmented = [list(row) + [value] for row, value in zip(C, y)]
    R, pivots = rref(augmented, width)
    for row in R:
        require(
            any(row[:width]) or not row[width],
            "vector outside prescribed independent subspace",
            row,
        )
    require(len(pivots) == width, "dependent prescribed basis")
    out = [F(0) for unused in range(width)]
    for i, j in enumerate(pivots):
        out[j] = R[i][width]
    return out


def inverse(A):
    n = len(A)
    require(all(len(row) == n for row in A), "square inverse input")
    augmented = [list(row) + unit for row, unit in zip(A, identity(n))]
    R, pivots = rref(augmented, n)
    require(len(pivots) == n, "singular generated Gram matrix")
    return [row[n:] for row in R]


def determinant(A):
    n = len(A)
    require(all(len(row) == n for row in A), "square determinant input")
    R = [[F(x) for x in row] for row in A]
    value = F(1)
    for j in range(n):
        guard()
        pivot = next((i for i in range(j, n) if R[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            R[j], R[pivot] = R[pivot], R[j]
            value = -value
        p = R[j][j]
        value *= p
        for i in range(j + 1, n):
            factor = R[i][j] / p
            if factor:
                for k in range(j + 1, n):
                    R[i][k] -= factor * R[j][k]
                R[i][j] = F(0)
    return value


def characteristic(A):
    n = len(A)
    B = identity(n)
    coefficients = [F(1)]
    for k in range(1, n + 1):
        B = multiply(A, B)
        coefficient = -sum((B[i][i] for i in range(n)), F(0)) / k
        coefficients.append(coefficient)
        for i in range(n):
            B[i][i] += coefficient
    require(not any(x for row in B for x in row), "Cayley-Hamilton control")
    return coefficients


def polynomial_from_roots(roots):
    coefficients = [F(1)]
    for root in roots:
        result = [F(0)] * (len(coefficients) + 1)
        for i, c in enumerate(coefficients):
            result[i] += c
            result[i + 1] -= root * c
        coefficients = result
    return coefficients


def block_diagonal(A, B):
    m = len(A)
    n = len(B)
    return [
        list(A[i]) + [F(0)] * n if i < m
        else [F(0)] * m + list(B[i - m])
        for i in range(m + n)
    ]


def letters_and_gram(A):
    e, v, t = GEN
    u = [None] * 8
    u[0] = t
    u[1] = bracket(e, t)
    u[2] = bracket(v, t)
    u[3] = bracket(e, u[2])
    u[4] = bracket(v, u[1])
    u[5] = lin((F(-1, 2), bracket(e, u[3])))
    u[6] = lin((F(1, 2), bracket(v, u[4])))
    u[7] = bracket(e, u[6])
    raising = [
        ((), F(1)),
        ((0,), F(1)),
        ((1,), F(1)),
        ((0, 1), F(1)),
        ((1, 0), F(1)),
        ((0, 0, 1), F(-1, 2)),
        ((1, 1, 0), F(1, 2)),
        ((0, 1, 1, 0), F(1, 2)),
    ]
    G = [[F(0)] * 8 for unused in range(8)]
    for i in range(8):
        sequence, factor = raising[i]
        for j in range(8):
            if poly_degree(u[i]) != poly_degree(u[j]):
                continue
            p = u[j]
            for node in sequence:
                p = lower(node, p, A)
            require(
                not p or set(p) == {(2,)},
                "generated Levi Gram terminal vector",
                (i, j, p),
            )
            G[i][j] = factor * p.get((2,), 0)
    require(G == [list(row) for row in zip(*G)], "generated Gram symmetry")
    Gi = inverse(G)
    require(multiply(G, Gi) == identity(8), "generated inverse Gram identity")
    for i in range(8):
        for j in range(8):
            if Gi[i][j]:
                require(
                    poly_degree(u[i]) == poly_degree(u[j]),
                    "inverse Gram consuming charge",
                    (i, j),
                )
    return u, [theta(p) for p in u], G, Gi


MUTANTS = ("omit_W2", "drop_cross", "omit_W1R", "reverse_W1", "omit_W5")


def contraction(p, A, u, dual, Gi, mutant=None):
    if mutant is not None and mutant not in MUTANTS:
        raise Incomplete("unknown scientific mutant")
    lowering = [apply_negative(op, p, A) for op in dual]
    if mutant == "omit_W2":
        lowering[2] = {}
    elif mutant == "omit_W5":
        lowering[5] = {}
    elif mutant == "omit_W1R":
        lowering[4] = lin(
            (-1, lower(1, apply_negative(dual[1], p, A), A))
        )
    elif mutant == "reverse_W1":
        for j in (1, 4, 6, 7):
            lowering[j] = lin((-1, lowering[j]))
    out = {}
    for i in range(8):
        for j in range(8):
            guard()
            coefficient = Gi[i][j]
            if mutant == "drop_cross" and (i, j) in ((3, 4), (4, 3)):
                coefficient = F(0)
            if coefficient and lowering[j]:
                out = lin(
                    (1, out),
                    (coefficient, bracket(u[i], lowering[j])),
                )
    return out


def basis_coordinates(model, d, vectors):
    height = len(model.basis(d))
    C = columns_matrix([model.coordinates(p, d) for p in vectors], height)
    require(rank(C, len(vectors)) == len(vectors), "prescribed basis independence")
    return C


def restriction(model, d, vectors, u, dual, Gi):
    C = basis_coordinates(model, d, vectors)
    result = []
    for p in vectors:
        image = contraction(p, model.A, u, dual, Gi)
        y = model.coordinates(image, d)
        result.append(coordinates_in_columns(C, y))
    return columns_matrix(result, len(vectors))


class VectorSpan:
    def __init__(self, dimension):
        self.dimension = dimension
        self.rows = {}

    def add(self, vector):
        require(len(vector) == self.dimension, "coverage vector dimension")
        p = [F(x) for x in vector]
        for pivot in sorted(self.rows):
            if p[pivot]:
                factor = p[pivot]
                p = [x - factor * y for x, y in zip(p, self.rows[pivot])]
        pivot = next((j for j, x in enumerate(p) if x), None)
        if pivot is None:
            return None
        value = p[pivot]
        p = [x / value for x in p]
        self.rows[pivot] = p
        return p


def tensor_listing(p):
    return tuple(
        ("".join(str(i + 1) for i in word), str(c))
        for word, c in sorted(p.items())
    )


def construct_vectors(r, n):
    e, v, t = GEN
    z = bracket(e, t)
    d = bracket(t, z)
    p = bracket(t, d)
    q = bracket(z, d)
    w = bracket(e, v)
    L = lin((1, bracket(t, w)), (-1, bracket(z, v)))
    x = lin((-1, bracket(d, L)))
    if n == 3:
        pbw = [
            act([t, z, z], v),
            act([z, d], v),
            act([t, t, z], w),
            act([t, d], w),
        ]
        if r == 2:
            missing = [x]
        else:
            pbw += [bracket(q, v), bracket(p, w)]
            missing = [x, lin((1, bracket(p, w)), (-1, bracket(q, v)))]
    elif r == 3 and n == 4:
        pbw = [
            act([t, t, z, z], v),
            act([t, z, d], v),
            act([d, d], v),
            act([t, q], v),
            act([z, p], v),
            act([t, t, t, z], w),
            act([t, t, d], w),
            act([t, p], w),
        ]
        missing = [
            act([d, t], L),
            act([d, d], v),
            bracket(p, L),
            lin((1, act([t, q], v)), (-1, act([z, p], v))),
        ]
    else:
        raise Incomplete("unassigned case in vector construction")
    horizontal = [
        bracket(ad_power(t, i, e), ad_power(t, n - i, v))
        for i in range(r + 1)
    ]
    return pbw, missing, horizontal


def derive_case(model, r, s, n, u, dual, G, Gi, mutant_witnesses):
    guard()
    amax = model.bounds[0]
    dims = [len(model.basis((a, 1, n))) for a in range(amax + 1)]
    require(
        all(dims[a] == 0 for a in range(n + 2, amax + 1)),
        "unexpected horizontal support beyond finite node-1 strings",
        dims,
    )
    actions = {}
    raising = {}
    lowering = {}
    for a in range(amax + 1):
        d = (a, 1, n)
        basis = model.basis(d)
        images = [
            model.coordinates(contraction(p, model.A, u, dual, Gi), d)
            for p in basis
        ]
        actions[a] = columns_matrix(images, len(basis))
        if a < amax:
            target = (a + 1, 1, n)
            raising[a] = columns_matrix(
                [model.coordinates(bracket(GEN[0], p), target) for p in basis],
                dims[a + 1],
            )
        else:
            require(not basis, "box must include the top-raise zero target")
        if a > 0:
            target = (a - 1, 1, n)
            lowering[a] = columns_matrix(
                [model.coordinates(lower(0, p, model.A), target) for p in basis],
                dims[a - 1],
            )
        else:
            for p in basis:
                require(not lower(0, p, model.A), "bottom F1 target")
            lowering[a] = []

    for a in range(amax + 1):
        for j in range(dims[a]):
            source_action = column(actions[a], j)
            if a < amax:
                require(
                    mv(actions[a + 1], column(raising[a], j))
                    == mv(raising[a], source_action),
                    "full contraction E1 equivariance",
                    (r, s, n, a, j),
                )
            if a > 0:
                require(
                    mv(actions[a - 1], column(lowering[a], j))
                    == mv(lowering[a], source_action),
                    "full contraction F1 equivariance",
                    (r, s, n, a, j),
                )

    decomposition = []
    reconstructed = [0] * len(dims)
    for a, dimension in enumerate(dims):
        multiplicity = dimension - rank(lowering[a], dimension)
        if multiplicity:
            k = n + 1 - 2 * a
            require(k >= 0, "positive-weight node-1 lowest vector", (a, k))
            decomposition.append((k, multiplicity))
            for b in range(a, a + k + 1):
                require(b < len(dims), "node-1 string exceeds box")
                reconstructed[b] += multiplicity
    require(reconstructed == dims, "derived complete node-1 character", dims)

    pbw, missing, horizontal = construct_vectors(r, n)
    d = (2, 1, n)
    P = basis_coordinates(model, d, pbw)
    require(len(pbw) == dims[2], "alternative PBW basis completeness")
    X = basis_coordinates(model, d, missing)
    require(
        dims[2] - rank(lowering[2], dims[2]) == len(missing),
        "complete missing lowest space",
    )
    for p in missing:
        require(
            not any(model.coordinates(lower(0, p, model.A), (1, 1, n))),
            "missing vector is node-1 lowest",
        )
    H = basis_coordinates(model, (1, 1, n), horizontal)
    require(len(horizontal) == dims[1], "complete horizontal source basis")

    K = restriction(model, d, missing, u, dual, Gi)
    horizontal_matrix = restriction(
        model, (1, 1, n), horizontal, u, dual, Gi
    )
    PBW_matrix = restriction(model, d, pbw, u, dual, Gi)
    combined = [bracket(GEN[0], p) for p in horizontal] + missing
    C = basis_coordinates(model, d, combined)
    require(len(combined) == dims[2], "raised plus missing component completeness")
    combined_matrix = restriction(model, d, combined, u, dual, Gi)
    require(
        combined_matrix == block_diagonal(horizontal_matrix, K),
        "independent raised/missing block decomposition",
        combined_matrix,
    )
    for j, p in enumerate(combined):
        direct = model.coordinates(contraction(p, model.A, u, dual, Gi), d)
        require(
            direct == mv(actions[2], column(C, j)),
            "chosen-representative contraction agreement",
            j,
        )

    spans = [VectorSpan(dimension) for dimension in dims]
    queue = deque()

    def admit(a, vector):
        added = spans[a].add(vector)
        if added is not None:
            queue.append((a, added))

    for j in range(len(horizontal)):
        admit(1, column(H, j))
    for j in range(len(missing)):
        admit(2, column(X, j))
    while queue:
        guard()
        a, vector = queue.popleft()
        if a < amax:
            admit(a + 1, mv(raising[a], vector))
        if a > 0:
            admit(a - 1, mv(lowering[a], vector))
    require(
        [len(span.rows) for span in spans] == dims,
        "whole-grade horizontal and missing-vector saturation",
        dims,
    )

    raised_W5 = []
    if (r, s, n) == (3, 4, 4):
        raised_columns = [mv(raising[2], column(X, j)) for j in range(4)]
        require(
            rank(columns_matrix(raised_columns, dims[3]), 4) == 4,
            "four independent raised missing vectors",
        )
        for p in missing:
            raised = bracket(GEN[0], p)
            target = apply_negative(dual[5], raised, model.A)
            raised_W5.append(model.coordinates(target, (1, 0, 3)))
        require(
            any(any(vector) for vector in raised_W5),
            "nonzero W5 on raised G2 grade-four missing space",
        )

    mutation_inputs = list(model.basis(d))
    if (r, s, n) == (3, 4, 4):
        mutation_inputs += [bracket(GEN[0], p) for p in missing]
    for index, p in enumerate(mutation_inputs):
        pd = poly_degree(p)
        correct = model.coordinates(
            contraction(p, model.A, u, dual, Gi), pd
        )
        for name in MUTANTS:
            if name in mutant_witnesses:
                continue
            changed = model.coordinates(
                contraction(p, model.A, u, dual, Gi, name), pd
            )
            difference = [x - y for x, y in zip(correct, changed)]
            if any(difference):
                mutant_witnesses[name] = (
                    (r, s, pd, index),
                    tuple(difference),
                )

    change_to_combined = columns_matrix(
        [coordinates_in_columns(P, column(C, j)) for j in range(len(combined))],
        len(pbw),
    )
    actual = actions[2]
    charpoly = characteristic(actual)
    det = determinant(actual)
    require(
        det == ((-1) ** len(actual)) * charpoly[-1],
        "determinant/characteristic consistency",
    )
    require(
        det == determinant(horizontal_matrix) * determinant(K),
        "full component determinant factorization",
    )
    return {
        "key": (r, s, n),
        "dimensions": dims,
        "decomposition": decomposition,
        "quotient_basis": [tensor_listing(p) for p in model.basis(d)],
        "full_matrix": actual,
        "PBW_matrix": PBW_matrix,
        "horizontal_matrix": horizontal_matrix,
        "missing_matrix": K,
        "missing_determinant": determinant(K),
        "component_determinant": det,
        "characteristic": charpoly,
        "PBW_to_combined_columns": change_to_combined,
        "raised_W5_coordinates": raised_W5,
        "generated_Gram": G,
    }


def compare_claims(records):
    expected = {
        (2, 3, 3): {
            "dimensions": [1, 3, 4, 3, 1],
            "decomposition": [(4, 1), (2, 2), (0, 1)],
            "horizontal_matrix": [[3, 2, 0], [0, 11, 0], [0, 0, 12]],
            "missing_matrix": [[14]],
            "missing_determinant": 14,
            "component_determinant": 5544,
        },
        (3, 4, 3): {
            "dimensions": [1, 4, 6, 4, 1],
            "decomposition": [(4, 1), (2, 3), (0, 2)],
            "horizontal_matrix": [
                [6, 3, 0, 0], [0, 18, 0, 0],
                [0, 0, 19, 0], [0, 0, 4, 3],
            ],
            "missing_matrix": [[23, 0], [-10, 3]],
            "missing_determinant": 69,
            "component_determinant": 424764,
        },
        (3, 4, 4): {
            "dimensions": [1, 4, 8, 8, 4, 1],
            "decomposition": [(5, 1), (3, 3), (1, 4)],
            "horizontal_matrix": [
                [4, 3, 0, 0], [0, 19, 0, 0],
                [0, 6, 10, 3], [0, 0, 0, 20],
            ],
            "missing_matrix": [
                [19, 0, 3, 0], [10, 8, 0, -3],
                [-1, 0, 27, -2], [3, 0, -1, 30],
            ],
            "missing_determinant": 123392,
            "component_determinant": 1875558400,
        },
    }
    expected_gram = identity(8)
    expected_gram[3][3] = F(2)
    expected_gram[4][4] = F(2)
    expected_gram[3][4] = F(1)
    expected_gram[4][3] = F(1)
    for record in records:
        key = record["key"]
        wanted = expected[key]
        dimensions = list(record["dimensions"])
        while dimensions and dimensions[-1] == 0:
            dimensions.pop()
        require(
            dimensions == wanted["dimensions"],
            "claimed finite character comparison",
            (key, dimensions),
        )
        for field in (
            "decomposition", "horizontal_matrix", "missing_matrix",
            "missing_determinant", "component_determinant",
        ):
            require(
                record[field] == wanted[field],
                "claimed finite comparison " + field,
                (key, record[field]),
            )
        require(
            record["generated_Gram"] == expected_gram,
            "generated-versus-displayed Gram comparison",
            key,
        )
        if key == (2, 3, 3):
            written_pbw = [
                [7, 0, -4, 0], [7, 13, 2, -1],
                [-4, 0, 7, 0], [4, -1, 5, 13],
            ]
            written_change = [
                [6, -2, 0, 0], [-6, 3, -1, 1],
                [6, -1, 0, 0], [-6, 2, -1, -1],
            ]
            require(record["PBW_matrix"] == written_pbw, "independent B2 PBW matrix")
            require(
                record["PBW_to_combined_columns"] == written_change,
                "distinct B2 basis equivalence",
            )
            require(
                determinant(written_change) == -12,
                "B2 change-of-basis determinant",
            )
            require(
                record["characteristic"]
                == polynomial_from_roots((3, 11, 12, 14)),
                "explicit candidate finite eigenvalue comparison",
            )


def positive_seed_mutants():
    witnesses = []
    for r, s in ((2, 3), (3, 4)):
        A = cartan(r, s)
        for name, degree, seed in all_seeds(A):
            full = PositiveQuotient(A, degree)
            full_value = full.coordinates(seed, degree)
            require(
                not any(full_value),
                "included raw Serre seed vanishes in complete closure",
                (r, s, name),
            )
            full = None
            omitted = PositiveQuotient(A, degree, omit=name)
            omitted_value = omitted.coordinates(seed, degree)
            require(
                any(omitted_value),
                "omitted Serre seed must have an exact nonzero residual",
                (r, s, name, omitted_value),
            )
            witnesses.append(
                ((r, s), name, degree, tuple(omitted_value))
            )
            omitted = None
    return witnesses


def main():
    if len(sys.argv) != 1:
        raise Incomplete("this frozen checker accepts no additional arguments")
    print("SCOPE: positive quotient conditional on named f276 bridge;")
    print("       contraction at f306 normalization; no uniform theorem.")
    print("LIMITS: cooperative 53 seconds; no file/network/child-process I/O.")
    records = []
    mutant_witnesses = {}
    for r, s, maximum_grade, grades in (
        (2, 3, 3, (3,)),
        (3, 4, 4, (3, 4)),
    ):
        A = cartan(r, s)
        normal_order_controls(A)
        model = PositiveQuotient(A, (maximum_grade + 2, 1, maximum_grade))
        u, dual, G, Gi = letters_and_gram(A)
        print("SIX_SEEDS:", (r, s), model.seed_metadata)
        for n in grades:
            records.append(
                derive_case(
                    model, r, s, n, u, dual, G, Gi, mutant_witnesses
                )
            )
        model = None

    require(
        set(mutant_witnesses) == set(MUTANTS),
        "every operator mutant needs a nonzero exact identity witness",
        sorted(mutant_witnesses),
    )
    seed_witnesses = positive_seed_mutants()

    compare_claims(records)
    for record in records:
        print("CASE:", record["key"])
        for field in (
            "dimensions", "decomposition", "quotient_basis",
            "full_matrix", "PBW_matrix", "horizontal_matrix",
            "missing_matrix", "missing_determinant",
            "component_determinant", "characteristic",
            "PBW_to_combined_columns", "raised_W5_coordinates",
            "generated_Gram",
        ):
            print(field + ":", repr(record[field]))
    for name in MUTANTS:
        print(
            "MUTANT_REJECTED_BY_NONZERO_IDENTITY:",
            name, repr(mutant_witnesses[name]),
        )
    for witness in seed_witnesses:
        print("SEED_MUTANT_REJECTED_BY_NONZERO_IDENTITY:", repr(witness))
    guard()
    print("RESULT: PASS_FINITE_ONLY")
    print("NOT_PROVED: negative ideal closure, uniform r/s/n/a theorem,")
    print("            global J=tau, B8, novelty, or a spectral theorem.")
    print("elapsed_seconds:", time.monotonic() - START)


if __name__ == "__main__":
    try:
        main()
    except ScientificFailure as exc:
        print("RESULT: FAIL")
        print("EXACT_FAILURE:", str(exc))
        sys.exit(1)
    except Incomplete as exc:
        print("RESULT: INCOMPLETE")
        print("REASON:", str(exc))
        sys.exit(2)
    except Exception as exc:
        print("RESULT: INCOMPLETE")
        print("IMPLEMENTATION_EXCEPTION:", type(exc).__name__, str(exc))
        sys.exit(2)
