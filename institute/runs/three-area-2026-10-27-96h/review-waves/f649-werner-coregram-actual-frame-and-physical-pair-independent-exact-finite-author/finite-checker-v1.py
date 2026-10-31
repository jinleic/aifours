#!/usr/bin/env python3
"""Proposed exact f649 check; NOT RUN by its author.

One process, fixed input, stdlib only; no file/network/subprocess operations.
All displayed operator entries are exact Gaussian rationals, with sqrt(101)
factored out of x1 and R. Named checks are active under python -O as well.
"""
from fractions import Fraction as F
from time import monotonic

START = monotonic()


class CheckError(Exception):
    def __init__(self, code):
        self.code = code
        super().__init__(code)


def require(condition, code):
    if not condition:
        raise CheckError(code)


def tick():
    require(monotonic() - START < 54, "DEADLINE_INCOMPLETE")


class G:
    """Exact complex number with rational real and imaginary parts."""
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r, self.i = F(r), F(i)

    def __bool__(self):
        return bool(self.r or self.i)

    def __eq__(self, other):
        o = ga(other)
        return self.r == o.r and self.i == o.i

    def __neg__(self):
        return G(-self.r, -self.i)

    def __add__(self, other):
        o = ga(other)
        return G(self.r + o.r, self.i + o.i)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-ga(other))

    def __rsub__(self, other):
        return ga(other) - self

    def __mul__(self, other):
        o = ga(other)
        return G(self.r * o.r - self.i * o.i,
                 self.r * o.i + self.i * o.r)

    __rmul__ = __mul__

    def conj(self):
        return G(self.r, -self.i)

    def abs2(self):
        return self.r * self.r + self.i * self.i

    def __str__(self):
        if not self.i:
            return str(self.r)
        if not self.r:
            return str(self.i) + "i"
        return "(" + str(self.r) + ("+" if self.i > 0 else "") + str(self.i) + "i)"


def ga(x):
    return x if isinstance(x, G) else G(x)


I = G(0, 1)


def zeros(rows, cols):
    return [[G() for _ in range(cols)] for _ in range(rows)]


def eye(n):
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = G(1)
    return out


def diag(values):
    out = zeros(len(values), len(values))
    for i, x in enumerate(values):
        out[i][i] = ga(x)
    return out


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def scale(s, a):
    return [[ga(s) * x for x in row] for row in a]


def adj(a):
    return [[a[j][i].conj() for j in range(len(a))]
            for i in range(len(a[0]))]


def mm(a, b):
    require(len(a[0]) == len(b), "MATRIX_DIMENSION")
    out = zeros(len(a), len(b[0]))
    for i in range(len(a)):
        tick()
        for k in range(len(b)):
            if a[i][k]:
                for j in range(len(b[0])):
                    if b[k][j]:
                        out[i][j] = out[i][j] + a[i][k] * b[k][j]
    return out


def kron(a, b):
    out = zeros(len(a) * len(b), len(a[0]) * len(b[0]))
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b)):
                for ell in range(len(b[0])):
                    out[i * len(b) + k][j * len(b[0]) + ell] = a[i][j] * b[k][ell]
    return out


def outer(u, v):
    return [[u[i] * v[j].conj() for j in range(len(v))] for i in range(len(u))]


def vdot(u, v):
    return sum((x.conj() * y for x, y in zip(u, v)), G())


def vscale(s, u):
    return [ga(s) * x for x in u]


def mv(a, v):
    return [sum((a[i][j] * v[j] for j in range(len(v))), G())
            for i in range(len(a))]


def hs(a, b):
    return sum((a[i][j].conj() * b[i][j]
                for i in range(len(a)) for j in range(len(a[0]))), G())


def norm2(a):
    return sum((x.abs2() for row in a for x in row), F(0))


def trace(a):
    return sum((a[i][i] for i in range(len(a))), G())


def partials(a):
    """Return Tr_B, Tr_A, using the physical index 4*i+j."""
    require(len(a) == 16 and all(len(row) == 16 for row in a), "PARTIAL_DIMENSION")
    tb, ta = zeros(4, 4), zeros(4, 4)
    for i in range(4):
        for j in range(4):
            tb[i][j] = sum((a[4 * i + k][4 * j + k] for k in range(4)), G())
            ta[i][j] = sum((a[4 * k + i][4 * k + j] for k in range(4)), G())
    return tb, ta


def qform(a):
    tb, ta = partials(a)
    return norm2(tb) + norm2(ta) - trace(a).abs2() / 2


def gform(a):
    tb, ta = partials(a)
    return norm2(a) + trace(a).abs2() - norm2(tb) - norm2(ta)


def real_rank(a):
    """Gaussian elimination over Q; complex entries are not silently discarded."""
    rows = []
    for row in a:
        require(all(x.i == 0 for x in row), "RANK_NOT_REAL")
        rows.append([x.r for x in row])
    if not rows:
        return 0
    r = 0
    for col in range(len(rows[0])):
        tick()
        pivot = next((k for k in range(r, len(rows)) if rows[k][col]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        d = rows[r][col]
        rows[r] = [x / d for x in rows[r]]
        for k in range(r + 1, len(rows)):
            f = rows[k][col]
            if f:
                rows[k] = [x - f * y for x, y in zip(rows[k], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


def commutant_rank(m):
    """Rank of [Z,M]=[Z,M^dagger]=0 in 16 complex variables."""
    equations = []
    for op in (m, adj(m)):
        for i in range(4):
            for j in range(4):
                row = []
                for a in range(4):
                    for b in range(4):
                        row.append((op[b][j] if i == a else G()) -
                                   (op[i][a] if j == b else G()))
                equations.append(row)
    return real_rank(equations)


def frame_check(u1, u2, v1_scaled, v2):
    require(vdot(u1, u2) == 0 and vdot(v1_scaled, v2) == 0,
            "FRAME_ORTHOGONALITY")
    require(vdot(u1, u1) == 1 and vdot(u2, u2) == 1 and
            vdot(v1_scaled, v1_scaled) == 101 and vdot(v2, v2) == 1,
            "FRAME_NORMALIZATION")


def core_failure_check(cross_scaled, p1, p2):
    require(cross_scaled.i == 0 and cross_scaled.r < 0, "CORE_SIGN")
    require(p1 > 0 and p2 > 0, "CORE_POSITIVE_GAPS")
    require(cross_scaled.abs2() / 101 > 16 * p1 * p2, "CORE_POSITIVE_SQUARE")


def partial_check(tb, ta):
    expected_tb = diag([F(-134, 25), F(4, 25), F(4, 25), F(1, 25)])
    expected_ta = diag([F(16, 25), F(-146, 25), F(4, 25), F(1, 25)])
    expected_ta[1][2] = G(-8)
    require(tb == expected_tb and ta == expected_ta, "PARTIAL_TRACE")


def phase_check(actual_cross, original_cross):
    require(actual_cross == -I * original_cross, "CONJUGATION")


def physical_norm_check(a, b, claimed_l):
    require(norm2(a) + norm2(b) == claimed_l, "PHYSICAL_NORM")


def irred_check(m):
    require(commutant_rank(m) == 15, "IRREDUCIBLE_COMMUTANT")


def claimed_q_violation(q, twice_norm):
    require(q > twice_norm, "FALSE_Q_COUNTEREXAMPLE")


def mutation(name, intended, fn):
    tick()
    try:
        fn()
    except CheckError as exc:
        require(exc.code == intended, "MUTATION_WRONG_REASON:" + name + ":" + exc.code)
        print("MUTATION", name, "REJECTED", exc.code)
        return
    raise CheckError("MUTATION_NOT_REJECTED:" + name)


def show_matrix(label, matrix):
    print("MATRIX", label, len(matrix), "x", len(matrix[0]))
    for row in matrix:
        print(" ".join(str(x) for x in row))


def main():
    tick()
    u1, v1, a = [G() for _ in range(16)], [G() for _ in range(16)], [G() for _ in range(16)]
    u1[1] = G(1)
    v1[1], v1[2], v1[4] = G(-6), G(-8), G(-1)
    b = (4, 2, 2, 1)
    for j in range(4):
        a[5 * j] = G(F(b[j], 5))
    frame_check(u1, a, v1, a)

    # x1 = x1_scaled/sqrt(101), x2 = projector, R = R_scaled/sqrt(101).
    x1_scaled, x2 = outer(u1, v1), outer(a, a)
    projector_independent = zeros(16, 16)
    for i in range(4):
        for j in range(4):
            projector_independent[5 * i][5 * j] = G(F(b[i] * b[j], 25))
    require(x2 == projector_independent and adj(x2) == x2 and mm(x2, x2) == x2 and
            trace(x2) == 1 and real_rank(x2) == 1, "PROJECTOR_CONSTRUCTION")
    r = add(x1_scaled, x2)
    r_independent = [row[:] for row in projector_independent]
    r_independent[1][1] = r_independent[1][1] - 6
    r_independent[1][2] = r_independent[1][2] - 8
    r_independent[1][4] = r_independent[1][4] - 1
    require(r == r_independent, "ACTUAL_MATRIX_CONSTRUCTION")
    require(real_rank(r) == 2 and mv(r, v1) == vscale(101, u1) and
            mv(r, a) == a and mv(adj(r), u1) == v1 and mv(adj(r), a) == a,
            "ACTUAL_SVD_AND_RANK")
    require(norm2(r) == 102 and trace(r) == -5, "R_TRACE_NORM")
    tb, ta = partials(r)
    partial_check(tb, ta)
    require(norm2(tb) == F(17989, 625) and norm2(ta) == F(61589, 625),
            "R_MARGINAL_NORMS")
    require(gform(r) == F(-203, 625), "R_G")
    require(qform(r) == F(143531, 1250) and qform(r) < 2 * norm2(r), "R_Q")

    tb1, ta1 = partials(x1_scaled)
    tb2, ta2 = partials(x2)
    c1, c2 = trace(x1_scaled), trace(x2)
    c12 = hs(tb1, tb2) + hs(ta1, ta2)
    require(c1 == -6 and c2 == 1 and c12 == G(F(-24, 5)), "FRAME_TRACES_AND_C12")
    p1 = (norm2(x1_scaled) + c1.abs2() - norm2(tb1) - norm2(ta1)) / (4 * 101)
    p2 = (norm2(x2) + c2.abs2() - norm2(tb2) - norm2(ta2)) / 4
    require(p1 == F(1, 404) and p2 == F(168, 625), "FRAME_P")
    cross_scaled = c1.conj() * c2 - c12
    require(cross_scaled == G(F(-6, 5)), "CORE_MIXED_VALUE")
    core_failure_check(cross_scaled, p1, p2)
    require(cross_scaled.abs2() / 101 == F(900, 63125) and
            16 * p1 * p2 == F(672, 63125), "CORE_SQUARE_VALUES")

    q1, q2 = qform(x1_scaled) / 101, qform(x2)
    h_scaled = c12 - F(1, 2) * c1.conj() * c2
    require(q1 == F(118, 101) and q2 == F(531, 1250) and
            h_scaled == G(F(-9, 5)), "Q_SPAN_ENTRIES")
    h2 = h_scaled.abs2() / 101
    qdet = q1 * q2 - h2
    alpha1, alpha2 = 2 - q1, 2 - q2
    residual_det = alpha1 * alpha2 - h2
    require(q1 > 0 and q2 > 0 and qdet == F(29304, 63125) and qdet > 0,
            "Q_GRAM_PRINCIPAL_MINORS")
    require(alpha1 == F(84, 101) and alpha2 == F(1969, 1250) and
            residual_det == F(80673, 63125) and residual_det > 0,
            "Q_RESIDUAL_PRINCIPAL_MINORS")
    require(q1 + q2 == F(201131, 126250) and q1 + q2 < 2, "Q_UNIFORM_REGION")

    # Physically rephase a singular vector; an unconjugated first slot fails.
    u1_phase = vscale(I, u1)
    frame_check(u1_phase, a, v1, a)
    x1_phase = outer(u1_phase, v1)
    tpb, tpa = partials(x1_phase)
    phase_h = hs(tpb, tb2) + hs(tpa, ta2) - F(1, 2) * trace(x1_phase).conj() * c2
    phase_check(phase_h, h_scaled)

    # Construct the physical matrices themselves, not their advertised norms.
    d = diag([3, -1, -1, -1])
    n = zeros(4, 4)
    n[0][1] = n[1][2] = n[2][3] = G(1)
    m = add(d, scale(F(1, 10), n))
    id4 = eye(4)
    x0 = add(kron(d, id4), kron(id4, d))
    x = add(kron(m, id4), kron(id4, m))
    delta = add(x, scale(-1, x0))
    require(delta == scale(F(1, 10), add(kron(n, id4), kron(id4, n))), "PHYSICAL_X")
    require(trace(m) == 0 and trace(x) == 0 and trace(x0) == 0, "TRACE_ZERO")
    physical_norm_check(m, m, F(1203, 50))
    nt_n = mm(adj(n), n)
    require(nt_n == diag([0, 1, 1, 1]) and mm(nt_n, nt_n) == nt_n and
            trace(nt_n) == 3, "N_OPERATOR_NORM")
    # The nonzero orthogonal projector N^dagger N has maximum eigenvalue 1.
    require(all(x0[i][j] == 0 for i in range(16) for j in range(16) if i != j),
            "X0_DIAGONAL")
    eigs = [x0[i][i].r for i in range(16)]
    require(all(x0[i][i].i == 0 for i in range(16)) and
            eigs.count(F(6)) == 1 and eigs.count(F(2)) == 6 and eigs.count(F(-2)) == 9,
            "X0_EIGENMULTIPLICITIES")
    require(F(11, 29) ** 2 == F(121, 841) and 3 * 121 < 841 and
            (1 + F(121, 841)) * F(3, 2) == F(1443, 841) < 2,
            "PHYSICAL_PAIR_RATIO_BOUND")
    require(F(31, 5) ** 2 + F(11, 5) ** 2 == F(1082, 25) < F(1203, 25),
            "PHYSICAL_PAIR_DIRECT_BOUND")

    # Real-coefficient 32-by-16 linear system: rank over Q equals rank over C.
    irred_check(m)
    e = [[G(int(i == j)) for i in range(4)] for j in range(4)]
    require(real_rank(add(m, scale(-3, id4))) == 3, "EIGENSPACE_3")
    md = adj(m)
    require(mv(add(md, scale(-3, id4)), e[0]) == vscale(F(1, 10), e[1]) and
            mv(add(md, id4), e[1]) == vscale(F(1, 10), e[2]) and
            mv(add(md, id4), e[2]) == vscale(F(1, 10), e[3]), "PROJECTION_CHAIN")
    m2 = mm(m, m)
    comm = add(mm(m2, adj(m2)), scale(-1, mm(adj(m2), m2)))
    require(m2[0][1] == G(F(1, 5)) and comm[0][0] == G(F(401, 10000)),
            "M_SQUARE_NONNORMAL")

    # Each mutation is supposed to fail a specific mathematical check, not just crash.
    mutation("core_sign", "CORE_SIGN", lambda: core_failure_check(-cross_scaled, p1, p2))
    mutation("complex_conjugate", "CONJUGATION", lambda: phase_check(I * h_scaled, h_scaled))
    mutation("partial_trace_swap", "PARTIAL_TRACE", lambda: partial_check(ta, tb))
    bad_u1 = [u1[j] + a[j] for j in range(16)]
    mutation("frame_overlap", "FRAME_ORTHOGONALITY", lambda: frame_check(bad_u1, a, v1, a))
    mutation("false_q_violation", "FALSE_Q_COUNTEREXAMPLE",
             lambda: claimed_q_violation(qform(r), 2 * norm2(r)))
    mutation("physical_norm", "PHYSICAL_NORM", lambda: physical_norm_check(m, m, F(1204, 50)))
    mutation("reducible_diagonal", "IRREDUCIBLE_COMMUTANT", lambda: irred_check(d))

    print("EXACT_FRAME p1", p1, "p2", p2, "sqrt101*C12", c12,
          "sqrt101*core_cross", cross_scaled)
    print("EXACT_R norm2", F(102, 101), "trace -5/sqrt(101)",
          "G", gform(r) / 101, "q", qform(r) / 101, "2norm2", F(204, 101))
    print("EXACT_SPAN q1", q1, "q2", q2, "sqrt101*h", h_scaled,
          "q_gram_det", qdet, "residual_det", residual_det)
    print("EXACT_PHYSICAL L", norm2(m) * 2, "commutant_rank", commutant_rank(m),
          "X0_eigenmultiplicities", "6:1,2:6,-2:9", "M2_comm00", comm[0][0])
    print("PHYSICAL_BOUNDS Weyl_sigma1=[29/5,31/5] sigma2<=11/5; S2<=1082/25<1203/25=2L")
    show_matrix("sqrt(101)*x1", x1_scaled)
    show_matrix("x2", x2)
    show_matrix("sqrt(101)*R", r)
    show_matrix("X0", x0)
    show_matrix("X", x)
    tick()
    print("COMPLETE: exact fixed instance only; no unrestricted Q/T2 conclusion")


if __name__ == "__main__":
    try:
        main()
    except CheckError as exc:
        print("INCOMPLETE", exc.code)
        raise SystemExit(1)
