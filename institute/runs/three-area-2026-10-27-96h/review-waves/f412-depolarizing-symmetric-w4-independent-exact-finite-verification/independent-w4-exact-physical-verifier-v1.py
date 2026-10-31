from fractions import Fraction as F
from math import comb
from time import monotonic

START = monotonic()

class AuditError(RuntimeError):
    pass

class BudgetExceeded(RuntimeError):
    pass

def tick():
    if monotonic() - START > 54:
        raise BudgetExceeded("TIME_LIMIT_NO_VERDICT")

def need(ok, tag):
    if not ok:
        raise AuditError(tag)

def poly(xs):
    a = [F(x) for x in xs]
    if not a:
        a = [F(0)]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)

Z = poly([0])
O = poly([1])
T = poly([0, 1])
AA = poly([F(1, 2), F(1, 2)])
BB = poly([F(1, 2), F(-1, 2)])

def padd(p, q):
    return poly([
        (p[i] if i < len(p) else 0) +
        (q[i] if i < len(q) else 0)
        for i in range(max(len(p), len(q)))
    ])

def pscale(p, c):
    return poly([x * c for x in p])

def psub(p, q):
    return padd(p, pscale(q, -1))

def pmul(p, q):
    a = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            a[i + j] += x * y
    return poly(a)

def ppow(p, n):
    a = O
    for unused in range(n):
        a = pmul(a, p)
    return a

def psum(ps):
    a = Z
    for p in ps:
        a = padd(a, p)
    return a

def peval(p, x):
    a = F(0)
    for c in reversed(p):
        a = a * x + c
    return a

def bern(p):
    need(len(p) <= 5, "BERNSTEIN_DEGREE")
    return tuple(
        sum(
            (p[r] * F(comb(j, r), comb(4, r))
             for r in range(min(j, len(p) - 1) + 1)),
            F(0)
        )
        for j in range(5)
    )

def wrong_bern(p):
    need(len(p) <= 5, "BERNSTEIN_DEGREE")
    return tuple(
        sum(
            (p[r] * F(comb(j, r), comb(5, r))
             for r in range(min(j, len(p) - 1) + 1)),
            F(0)
        )
        for j in range(5)
    )

def unbern(bs):
    need(len(bs) == 5, "BERNSTEIN_LENGTH")
    return psum([
        pscale(
            pmul(ppow(T, j), ppow(psub(O, T), 4 - j)),
            bs[j] * comb(4, j)
        )
        for j in range(5)
    ])

def check_bern(converter, polynomials):
    for p in polynomials:
        tick()
        need(unbern(converter(p)) == p, "BERNSTEIN_ROUNDTRIP")

def prefix(xs):
    out = [F(0)]
    for x in xs:
        out.append(out[-1] + x)
    return tuple(out)

def integer_scaled(xs, scale=192):
    out = [F(x) * scale for x in xs]
    need(all(x.denominator == 1 for x in out), "INTEGER_SCALING")
    return tuple(int(x) for x in out)

E = [1, 2, 4, 8]

def physical_poly(inputs):
    out = [[Z for y in range(16)] for x in range(16)]
    for r, s, amplitude in inputs:
        tick()
        states = [(0, 0, O)]
        for bit in range(4):
            u = (r >> bit) & 1
            v = (s >> bit) & 1
            if u == v:
                choices = [
                    (u, u, AA),
                    (1 - u, 1 - u, BB)
                ]
            else:
                choices = [(u, v, T)]
            nxt = []
            for x, y, c in states:
                for xb, yb, local in choices:
                    nxt.append((
                        x | (xb << bit),
                        y | (yb << bit),
                        pmul(c, local)
                    ))
            states = nxt
        for x, y, c in states:
            out[x][y] = padd(out[x][y], pscale(c, amplitude))
    return out

def pattern(mode="correct"):
    d = {
        0: pmul(ppow(AA, 3), BB),
        4: pmul(AA, ppow(BB, 3))
    }
    g = {}
    for k in range(1, 4):
        d[k] = pscale(
            padd(
                pscale(pmul(ppow(AA, 5-k), ppow(BB, k-1)), k),
                pscale(pmul(ppow(AA, 3-k), ppow(BB, k+1)), 4-k)
            ),
            F(1, 4)
        )
        coherence = T if mode == "coherence" else ppow(T, 2)
        if mode == "spectator":
            spectators = pmul(ppow(BB, 3-k), ppow(AA, k-1))
        else:
            spectators = pmul(ppow(AA, 3-k), ppow(BB, k-1))
        g[k] = pscale(pmul(coherence, spectators), F(1, 4))
    out = [[Z for y in range(16)] for x in range(16)]
    for x in range(16):
        k = x.bit_count()
        for y in range(16):
            if x == y:
                out[x][y] = d[k]
            elif k == y.bit_count() and (x ^ y).bit_count() == 2:
                out[x][y] = g[k]
    return d, g, out

def check_entries(actual, candidate):
    count = 0
    for x in range(16):
        for y in range(16):
            need(actual[x][y] == candidate[x][y], "W_CHANNEL_ENTRIES")
            count += 1
    return count

def imul(a, b):
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n))
         for j in range(n)]
        for i in range(n)
    ]

def charpoly(a):
    n = len(a)
    h = [[int(i == j) for j in range(n)] for i in range(n)]
    traces = [0]
    for k in range(1, n + 1):
        tick()
        h = imul(h, a)
        traces.append(sum(h[i][i] for i in range(n)))
    coefficients = [1]
    for k in range(1, n + 1):
        numerator = -sum(
            coefficients[j] * traces[k-j] for j in range(k)
        )
        need(numerator % k == 0, "NEWTON_INTEGRAL")
        coefficients.append(numerator // k)
    return tuple(coefficients)

def integer_roots(coefficients):
    a = list(coefficients)
    n = len(a) - 1
    found = []
    for root in range(-n, n + 1):
        while len(a) > 1:
            q = [a[0]]
            for c in a[1:]:
                q.append(c + root * q[-1])
            if q[-1] != 0:
                break
            found.append(root)
            a = q[:-1]
    need(a == [1], "INCOMPLETE_INTEGER_FACTORIZATION")
    return tuple(sorted(found, reverse=True))

def johnson(k):
    vertices = [x for x in range(16) if x.bit_count() == k]
    a = [
        [int(x != y and (x & y).bit_count() == k-1)
         for y in vertices]
        for x in vertices
    ]
    return vertices, a

def theoretical_char(k):
    roots = [4, 0, 0, 0, -2, -2] if k == 2 else [3, -1, -1, -1]
    p = O
    for r in roots:
        p = pmul(p, poly([-r, 1]))
    return integer_scaled(reversed(p), 1)

def graph_prerequisite(a):
    n = len(a)
    need(
        all(
            a[i][j] in (0, 1) and a[i][j] == a[j][i]
            for i in range(n) for j in range(n)
        ) and all(a[i][i] == 0 for i in range(n)),
        "CONTROL_GRAPH_PREREQUISITE"
    )

def check_reference(rs):
    need(len(rs) == 16 and psum(rs) == O, "REFERENCE_TRACE")
    for i in range(15):
        need(
            all(x >= 0 for x in bern(psub(rs[i], rs[i+1]))),
            "REFERENCE_ORDER"
        )

class G:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r = F(r)
        self.i = F(i)

    def __add__(self, other):
        other = cg(other)
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-cg(other))

    def __rsub__(self, other):
        return cg(other) - self

    def __mul__(self, other):
        other = cg(other)
        return G(
            self.r * other.r - self.i * other.i,
            self.r * other.i + self.i * other.r
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = cg(other)
        norm = other.r * other.r + other.i * other.i
        need(norm != 0, "GAUSSIAN_DIVISION_ZERO")
        return G(
            (self.r * other.r + self.i * other.i) / norm,
            (self.i * other.r - self.r * other.i) / norm
        )

    def conj(self):
        return G(self.r, -self.i)

    def __bool__(self):
        return bool(self.r or self.i)

    def __eq__(self, other):
        other = cg(other)
        return self.r == other.r and self.i == other.i

    def __repr__(self):
        return "(" + str(self.r) + "," + str(self.i) + ")"

def cg(x):
    return x if isinstance(x, G) else G(x)

def zero_matrix(n=16):
    return [[G() for j in range(n)] for i in range(n)]

def trace(a):
    return sum((a[i][i] for i in range(len(a))), G())

def hermitian(a):
    n = len(a)
    return all(a[i][j] == a[j][i].conj()
               for i in range(n) for j in range(n))

def gmul(a, b):
    n = len(a)
    out = zero_matrix(n)
    for i in range(n):
        for k in range(n):
            if a[i][k]:
                for j in range(n):
                    if b[k][j]:
                        out[i][j] = out[i][j] + a[i][k] * b[k][j]
    return out

def positive_semidefinite(a):
    need(hermitian(a), "DENSITY_HERMITIAN")
    b = [row[:] for row in a]
    n = len(b)
    for k in range(n):
        tick()
        pivot = b[k][k]
        need(pivot.i == 0 and pivot.r >= 0, "DENSITY_PSD")
        if pivot.r == 0:
            need(all(b[k][j] == 0 for j in range(k+1, n)), "DENSITY_PSD")
            continue
        for i in range(k+1, n):
            for j in range(i, n):
                value = b[i][j] - b[i][k] * b[k][j] / pivot
                b[i][j] = value
                b[j][i] = value.conj()
        for i in range(k+1, n):
            b[i][k] = G()
            b[k][i] = G()

def density(a):
    need(hermitian(a), "DENSITY_HERMITIAN")
    need(trace(a) == 1, "DENSITY_TRACE")
    positive_semidefinite(a)

def projector(q, rank):
    need(hermitian(q), "PROJECTOR_HERMITIAN")
    need(gmul(q, q) == q, "PROJECTOR_IDEMPOTENT")
    need(trace(q) == rank, "PROJECTOR_RANK")

def evaluated_matrix(a, t):
    return [[G(peval(p, t)) for p in row] for row in a]

def rational_channel(rho, lam):
    out = zero_matrix()
    for r in range(16):
        for s in range(16):
            if not rho[r][s]:
                continue
            tick()
            states = [(0, 0, F(1))]
            for bit in range(4):
                u = (r >> bit) & 1
                v = (s >> bit) & 1
                if u == v:
                    choices = [
                        (u, u, (1 + lam) / 2),
                        (1-u, 1-u, (1-lam) / 2)
                    ]
                else:
                    choices = [(u, v, lam)]
                nxt = []
                for x, y, c in states:
                    for xb, yb, local in choices:
                        nxt.append((
                            x | (xb << bit),
                            y | (yb << bit),
                            c * local
                        ))
                states = nxt
            for x, y, c in states:
                out[x][y] = out[x][y] + rho[r][s] * c
    return out

def transpose(a):
    return [[a[j][i] for j in range(16)] for i in range(16)]

def spin(a):
    return [
        [
            a[x ^ 15][y ^ 15] *
            (-1 if (x.bit_count() + y.bit_count()) % 2 else 1)
            for y in range(16)
        ]
        for x in range(16)
    ]

def partial_transpose(a, mask):
    need(0 < mask < 15, "PARTIAL_TRANSPOSE_MASK")
    keep = 15 ^ mask
    return [
        [
            a[(x & keep) | (y & mask)][(y & keep) | (x & mask)]
            for y in range(16)
        ]
        for x in range(16)
    ]

def expectation(q, a):
    value = sum(
        (q[i][j] * a[j][i] for i in range(16) for j in range(16)),
        G()
    )
    need(value.i == 0, "EXPECTATION_REAL")
    return value.r

def main():
    controls = []

    def reject(tag, action):
        try:
            action()
        except AuditError as error:
            need(str(error) == tag, "CONTROL_WRONG_REASON:" + tag)
            controls.append(tag)
        else:
            raise AuditError("CONTROL_NOT_REJECTED:" + tag)

    winputs = [(r, s, F(1, 4)) for r in E for s in E]
    actual = physical_poly(winputs)
    d, g, predicted = pattern()
    entries_checked = check_entries(actual, predicted)

    root_data = {}
    characteristic_data = {}
    graph_data = {}
    for k in range(1, 4):
        vertices, adjacency = johnson(k)
        graph_prerequisite(adjacency)
        characteristic = charpoly(adjacency)
        need(characteristic == theoretical_char(k), "JOHNSON_CHARPOLY")
        roots = integer_roots(characteristic)
        need(len(roots) == len(vertices), "JOHNSON_MULTIPLICITY")
        root_data[k] = roots
        characteristic_data[k] = characteristic
        graph_data[k] = adjacency

    eigenvalues = [d[0]]
    for k in range(1, 4):
        for root in root_data[k]:
            eigenvalues.append(padd(d[k], pscale(g[k], root)))
    eigenvalues.append(d[4])
    need(len(eigenvalues) == 16, "SPECTRUM_SIZE")
    need(psum(eigenvalues) == O, "SPECTRUM_TRACE")

    product_output = physical_poly([(0, 0, F(1))])
    order = sorted(range(16), key=lambda x: (x.bit_count(), x))
    reference = [product_output[x][x] for x in order]
    for x in range(16):
        for y in range(16):
            if x != y:
                need(product_output[x][y] == Z, "PRODUCT_REFERENCE_DIAGONAL")
        k = x.bit_count()
        need(
            product_output[x][x] == pmul(ppow(AA, 4-k), ppow(BB, k)),
            "PRODUCT_REFERENCE_ENTRIES"
        )
    check_reference(reference)
    check_bern(bern, eigenvalues + reference + [ppow(T, 2)])
    need(
        all(c >= 0 for p in eigenvalues for c in bern(p)),
        "SPECTRUM_NONNEGATIVE"
    )

    need(
        sorted(peval(p, F(0)) for p in eigenvalues) == [F(1,16)] * 16,
        "T0_SPECTRUM"
    )
    need(
        sorted(peval(p, F(1)) for p in eigenvalues) == [F(0)] * 15 + [F(1)],
        "T1_SPECTRUM"
    )
    need(
        sorted(peval(p, F(0)) for p in reference) == [F(1,16)] * 16,
        "T0_REFERENCE"
    )
    need(
        sorted(peval(p, F(1)) for p in reference) == [F(0)] * 15 + [F(1)],
        "T1_REFERENCE"
    )
    for x in range(16):
        for y in range(16):
            need(
                peval(actual[x][y], F(0)) == (F(1,16) if x == y else F(0)),
                "T0_MATRIX"
            )
            need(
                peval(actual[x][y], F(1)) ==
                (F(1,4) if x in E and y in E else F(0)),
                "T1_MATRIX"
            )
    density(evaluated_matrix(actual, F(0)))
    density(evaluated_matrix(actual, F(1)))

    wbern = [bern(p) for p in eigenvalues]
    rbern = [bern(p) for p in reference]
    table = []
    for j in range(5):
        maxima = tuple(sorted((b[j] for b in wbern), reverse=True))
        mp = prefix(maxima)
        rp = prefix([b[j] for b in rbern])
        gaps = tuple(rp[k] - mp[k] for k in range(17))
        need(all(x >= 0 for x in gaps), "BERNSTEIN_PREFIX_CERTIFICATE")
        need(gaps[0] == 0 and gaps[16] == 0, "PREFIX_ENDPOINTS")
        table.append((
            j,
            integer_scaled(maxima),
            integer_scaled(mp),
            integer_scaled(rp),
            integer_scaled(gaps)
        ))

    for mode in ("coherence", "spectator"):
        unused_d, unused_g, mutated = pattern(mode)
        density(evaluated_matrix(mutated, F(1,3)))
        reject(
            "W_CHANNEL_ENTRIES",
            lambda mutated=mutated: check_entries(actual, mutated)
        )

    bad_graph = [row[:] for row in graph_data[2]]
    bad_graph[0][1] = 1 - bad_graph[0][1]
    bad_graph[1][0] = bad_graph[0][1]
    graph_prerequisite(bad_graph)
    reject(
        "JOHNSON_CHARPOLY",
        lambda: need(
            charpoly(bad_graph) == theoretical_char(2),
            "JOHNSON_CHARPOLY"
        )
    )

    reject(
        "BERNSTEIN_ROUNDTRIP",
        lambda: check_bern(
            wrong_bern, eigenvalues + reference + [ppow(T, 2)]
        )
    )

    bad_reference = reference[:]
    bad_reference[0], bad_reference[-1] = (
        bad_reference[-1], bad_reference[0]
    )
    need(
        sorted(bad_reference) == sorted(reference),
        "CONTROL_REFERENCE_MULTISET"
    )
    reject("REFERENCE_ORDER", lambda: check_reference(bad_reference))

    phases = [
        G(1),
        G(0, 1),
        G(F(3,5), F(4,5)),
        G(F(5,13), F(12,13))
    ]
    need(all(z * z.conj() == 1 for z in phases), "PHASE_NORMALIZATION")
    rho = zero_matrix()
    for i, r in enumerate(E):
        for j, s in enumerate(E):
            rho[r][s] = phases[i] * phases[j].conj() / 4
    density(rho)
    projector(rho, 1)

    q = zero_matrix()
    f0, f1 = E[0] ^ 15, E[1] ^ 15
    q[f0][f0] = G(F(1,2))
    q[f1][f1] = G(F(1,2))
    q[f0][f1] = G(0, F(-1,2))
    q[f1][f0] = q[f0][f1].conj()
    projector(q, 1)
    transported = spin(transpose(q))
    projector(transported, 1)
    need(any(z.i != 0 for row in rho for z in row), "COMPLEX_STATE")
    need(any(z.i != 0 for row in q for z in row), "COMPLEX_PROJECTOR")
    need(transported != q, "NONSTALE_PROJECTOR_PREREQUISITE")

    reflection_cases = []
    selected_a = None
    selected_b = None
    for t in (F(0), F(1,5), F(1,3)):
        tick()
        a = rational_channel(rho, t)
        b = rational_channel(rho, -t)
        density(a)
        density(b)
        need(b == spin(transpose(a)), "SPIN_TRANSPOSE")
        left = expectation(q, b)
        right = expectation(transported, a)
        need(left == right, "PROJECTOR_TRANSPORT")
        reflection_cases.append((t, left, right))
        if t == F(1,3):
            selected_a, selected_b = a, b

    need(selected_a is not None and selected_b is not None, "SELECTED_CASE")
    need(selected_a != transpose(selected_a), "NONREAL_OUTPUT_PREREQUISITE")
    correct_value = expectation(q, selected_b)
    stale_value = expectation(q, selected_a)
    need(correct_value == F(2,27), "COMPLEX_CONTROL_VALUE")
    need(stale_value == F(1,27), "STALE_CONTROL_VALUE")

    no_transpose = spin(selected_a)
    density(no_transpose)
    need(expectation(q, no_transpose) == F(8,81), "NO_TRANSPOSE_CONTROL_VALUE")
    reject(
        "SPIN_TRANSPOSE",
        lambda: need(selected_b == no_transpose, "SPIN_TRANSPOSE")
    )

    one_site_transpose = spin(partial_transpose(selected_a, 1))
    density(one_site_transpose)
    reject(
        "SPIN_TRANSPOSE",
        lambda: need(selected_b == one_site_transpose, "SPIN_TRANSPOSE")
    )

    reject(
        "PROJECTOR_TRANSPORT",
        lambda: need(
            correct_value == expectation(q, selected_a),
            "PROJECTOR_TRANSPORT"
        )
    )

    need(len(controls) == 8, "CONTROL_COUNT")
    groups = {}
    for p in eigenvalues:
        groups[p] = groups.get(p, 0) + 1

    tick()
    print("ENTRY_CHECK_COUNT", entries_checked)
    for k in range(1, 4):
        print("JOHNSON", k, "CHARPOLY", characteristic_data[k],
              "ROOTS", root_data[k])
    for p, multiplicity in groups.items():
        padded = list(p) + [F(0)] * (5-len(p))
        print("SPECTRUM_GROUP", multiplicity,
              "POWER_COEFFICIENTS_TIMES_16", integer_scaled(padded, 16))
    for j, maxima, mp, rp, gaps in table:
        print("BERNSTEIN_J", j)
        print("MAXIMAL_COEFFICIENTS_TIMES_192", maxima)
        print("MAXIMAL_PREFIXES_TIMES_192", mp)
        print("REFERENCE_PREFIXES_TIMES_192", rp)
        print("GAPS_TIMES_192", gaps)
    for case in reflection_cases:
        print("EXACT_COMPLEX_REFLECTION_CASE", case)
    print("EXACT_COMPLEX_CORRECT_STALE_NO_TRANSPOSE",
          correct_value, stale_value, expectation(q, no_transpose))
    print("CONTROLS_REJECTED_FOR_INTENDED_INVARIANTS", tuple(controls))
    print("RUNTIME_SECONDS", monotonic() - START)
    tick()
    print("STATUS PASS")

if __name__ == "__main__":
    main()
