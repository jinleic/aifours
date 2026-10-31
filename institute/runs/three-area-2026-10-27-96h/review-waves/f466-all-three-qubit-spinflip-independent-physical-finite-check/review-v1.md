# F466 — Independent physical finite-check deliverable

**Role:** FINITE  
**Execution status:** **NOT_RUN — runtime-restricted.**  
**Scientific status:** Independent written reconstruction and complete, unexecuted diagnostic source. **No self-acceptance, computational PASS, or parent disposition is asserted.**

## 1. Input and method audit

I read, before opening the scientific packet:

- The complete manifest, freeze receipt, dispatch receipt, and parent live-metadata supply.
- All ten listed permission/status controls, through their endings.
- The quarantine controls only as exclusions; no held scientific payload or downstream scientific consumer was followed.

I then read the complete literal packet sequentially, in raw ranges of at most 20 lines, through its ending:

- **S1:** all 783 logical lines of the F463 author candidate.
- **S2:** all 48 lines of the prior four-qubit sector disposition.
- Packet coverage: lines **1–833**, including both source endings.

Binding metadata:

| Item | SHA-256 |
|---|---|
| Manifest | `08f2744cc2ced12b3143ea195ebd6583feee04b8187a643c0275a82b9c5f3e5c` |
| Freeze receipt | `931b4862215c149990ac5a989cd934b5f53e3a5c5dfce1375c60740c776e9d00` |
| Literal packet | `1d7fc4b2db09fef3f0db14edbd487b6ffb44d43cdae633b4f1aee95b018e809d` |
| S1 author candidate | `3e2cab0b74bc61af6179c442d0098a56d1f209e8dc7f39b6dd601cf1b0025907` |
| S2 prior disposition | `8522551e1088a796288c73c9b1aad8fa40e197d74b6f7d41447392d07370d6c0` |

These hashes, byte/LF observations, and the supplied clock are **parent-attributed**, not independently executed child observations.

After the complete read, I independently reconstructed the algebra below and designed the fresh diagnostic source. I did not read an author implementation, sibling return, additional scientific source, or held episode. No scientific executable, shell workaround, model CLI, installation, file mutation, or delegated execution was used.

The active runtime review-role instructions restrict Bash to specified read-only review commands and prohibit file editing. Consequently, I did **not** execute or materialize the diagnostic through another tool. The complete source and invocation are returned below without fabricated output.

## 2. Independent written audit

### 2.1 The new H2 lemma

I found no defect in the paired-projection argument.

For a pure three-qubit density, the full spin flip has square \(-I\) on vectors. Consequently, \(\rho\) and \(\widetilde\rho\) are orthogonal rank-one projections, so \(P=\rho+\widetilde\rho\) is an invariant rank-two projection.

The actual lifted marginal identities give

\[
H_2+\widetilde H_2=I+2P.
\]

Writing \(G=I+2P\), its square root and inverse square root are

\[
G^{1/2}=I-P+\sqrt3\,P,\qquad
G^{-1/2}=I-P+\frac{\sqrt3}{3}P.
\]

Thus \(Z=G^{-1/2}H_2G^{-1/2}\) and its spin flip are positive and sum to the identity.

The spectral pairing step includes the potentially delicate half-eigenspace: because it is invariant under an antiunitary squaring to \(-I\), it has an orthonormal paired basis. Selecting one vector from every pair therefore gives actual rank-four projectors satisfying \(\widetilde\Pi=I-\Pi\), not merely projectors with the desired rank or trace.

For every such projector,

\[
\operatorname{Tr}(P\Pi)=1.
\]

The compression \(R=\Pi P\Pi|_{\operatorname{ran}\Pi}\) is positive, has trace one, and rank at most two. Its spectrum is therefore \((\eta,1-\eta,0,0)\). The actual matrix \(G^{1/2}\Pi G^{1/2}\) has four nonzero eigenvalues equal to those of \(I_4+2R\). This establishes the claimed \((3,1,1,1,0,0,0,0)\) majorant at every prefix.

The rank-two projection hypothesis is restricted correctly to pure inputs. The mixed-input result follows instead by linearity and convexity.

### 2.2 Channel expansion and consuming projectors

The coefficients in the positive-parameter expansion are nonnegative. Its H2, H1, pure-state, and identity reference matrices are genuinely co-ordered by Hamming weight. Thus the sum of their prefix bounds equals the product-reference prefix, rather than a larger independently optimized relaxation.

For the negative physical branch, the transformation is a **full transpose** followed by conjugation with \(Y^{\otimes n}\). The consuming projector is transported to \(Y^{\otimes n}Q^TY^{\otimes n}\). The author includes this transport; neither a partial transpose nor an unchanged complex projector is substituted.

### 2.3 Assigned exact example

The displayed example has all three one-qubit marginals

\[
m=\begin{pmatrix}3/4&1/4\\1/4&1/4\end{pmatrix}.
\]

Its determinant is \(1/8\), so its eigenvalue discriminant is \(1/2\), and its marginal eigenbasis is nondegenerate. A local parity stabilizer would therefore require each local axis to be \(\pm(X+Z)/\sqrt2\).

The unnormalized Hadamard-sign expectation is \(5/2\). Dividing its square by eight gives \(25/32<1\), excluding those parity stabilizers. This is a written exact reconstruction, not program output.

At \(t=3/4,\ b=1/8\), the same-projector expectation is

\[
\frac{432}{1024}+\frac{189}{1024}+\frac{2}{1024}
=\frac{623}{1024},
\]

whereas the product-reference largest eigenvalue is \(686/1024\). This expectation is not substituted for the largest actual output eigenvalue.

### 2.4 Four-qubit scope

The consumer argument correctly covers all \(1|3\)-separable states and their convex hull across the four single-qubit cuts, at all sixteen prefixes.

**Conditional scope consequence:** if the new three-qubit candidate is accepted and the prior S2 balanced-cut result retains its stated scope, convexity combines their four \(1|3\) and three \(2|2\) cut classes into **all biseparable four-qubit states**. This does **not** establish the unrestricted four-qubit theorem or cover genuinely four-party-entangled states generally.

No novelty or priority conclusion follows from this audit.

## 3. Finite-check coverage and results

**All execution results remain NOT_RUN.** The source has not received a syntax, runtime, performance, or numerical validation run.

Its prescribed coverage is:

- Exact Gaussian-rational physical input construction and positivity checks.
- Direct physical partial traces and embeddings.
- Three separately implemented tensor-channel routes:
  1. local matrix-unit tensor expansion;
  2. partial-trace/erasure expansion;
  3. Pauli-unitary expansion.
- Exact spin-flip, H1/H2, rank-two, whitening, and inverse identities.
- Exact paired-projector checks against actual pure-input \(P\), including compression rank, trace, and factorization.
- Numerical reconstruction of paired projectors from the actual whitened effect, explicitly separated from exact checks.
- Six three-qubit inputs and eight four-qubit biseparable inputs.
- Eight physical parameter values, including \(p=0,1,4/3\), negative-parameter cases, and their positive mirrors.
- All eight or sixteen output prefixes, respectively, and exact expectations for the same fixed complex projectors.
- Eight named mutation controls.

The prescribed channel grid contains **112 physical cases and 1,408 prefix comparisons**. These are source-defined counts, **not observed completed counts**.

General eigenvalue comparisons are floating-point diagnostics with declared tolerances and independently measured eigenpair/orthogonality residuals. They are neither exact spectral certificates nor a uniform proof.

## 4. Invocation

The complete source between the delimiters below is the value of the final argument:

- argv[0]: `python3`
- argv[1]: `-I`
- argv[2]: `-B`
- argv[3]: `-c`
- argv[4]: the complete source below

No source-file access is required. The program imports only standard-library modules, starts no children, accesses no network, and performs no file reads or writes. A cooperative deadline returns **INCOMPLETE**, never success. Actual elapsed time and completion are unobserved.

BEGIN PYTHON SOURCE
import sys
import time
import math
import itertools
from fractions import Fraction as F

START = time.monotonic()
LIMIT = 54.0
TOL = 2.0e-9
EIG_STOP = 2.0e-14
EIG_RESID = 3.0e-10
PAIR_TOL = 3.0e-8
STAGE = "initialization"
COUNTS = {
    "states": 0,
    "physical_cases": 0,
    "prefixes": 0,
    "exact_paired_vertices": 0,
    "numeric_paired_vertices": 0,
    "mutations": 0,
}
MAXIMA = {
    "eigenpair_residual": 0.0,
    "orthogonality_residual": 0.0,
    "paired_reconstruction": 0.0,
    "numeric_prefix_excess": 0.0,
}
MUTATIONS = []


class CheckFailure(Exception):
    pass


class Deadline(Exception):
    pass


def pulse():
    if time.monotonic() - START >= LIMIT:
        raise Deadline(STAGE)


def ok(condition, reason):
    if not condition:
        raise CheckFailure(reason)


class G:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        if isinstance(re, G):
            ok(im == 0, "GAUSSIAN_COERCION")
            self.re, self.im = re.re, re.im
        else:
            self.re, self.im = F(re), F(im)

    def __bool__(self):
        return bool(self.re or self.im)

    def __add__(self, other):
        other = G(other)
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-G(other))

    def __rsub__(self, other):
        return G(other) - self

    def __mul__(self, other):
        other = G(other)
        if not self or not other:
            return G()
        if not other.im:
            return G(self.re * other.re, self.im * other.re)
        if not self.im:
            return G(self.re * other.re, self.re * other.im)
        return G(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = G(other)
        den = other.re * other.re + other.im * other.im
        ok(den != 0, "GAUSSIAN_DIVISION_BY_ZERO")
        return G(
            (self.re * other.re + self.im * other.im) / den,
            (self.im * other.re - self.re * other.im) / den,
        )

    def __rtruediv__(self, other):
        return G(other) / self

    def __eq__(self, other):
        try:
            other = G(other)
        except (TypeError, ValueError):
            return False
        return self.re == other.re and self.im == other.im

    def conjugate(self):
        return G(self.re, -self.im)

    def __complex__(self):
        return complex(float(self.re), float(self.im))


J = G(0, 1)


def cj(x):
    return x.conjugate()


def real(x):
    x = G(x)
    ok(x.im == 0, "EXACT_REAL_REQUIRED")
    return x.re


def zero(r, c=None):
    if c is None:
        c = r
    return [[0 for _ in range(c)] for _ in range(r)]


def eye(n):
    return [[G(int(i == j)) for j in range(n)] for i in range(n)]


def neye(n):
    return [[complex(i == j) for j in range(n)] for i in range(n)]


def dag(a):
    return [[cj(a[i][j]) for i in range(len(a))]
            for j in range(len(a[0]))]


def ma(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def ms(a, s):
    return [[s * x for x in row] for row in a]


def sub(a, b):
    return ma(a, ms(b, -1))


def mm(a, b):
    ok(len(a[0]) == len(b), "MATRIX_DIMENSION")
    out = zero(len(a), len(b[0]))
    for i, row in enumerate(a):
        pulse()
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[i][j] = out[i][j] + x * y
    return out


def lin(terms):
    out = zero(len(terms[0][1]), len(terms[0][1][0]))
    for coefficient, matrix in terms:
        if coefficient:
            out = ma(out, ms(matrix, coefficient))
    return out


def tr(a):
    return sum((a[i][i] for i in range(len(a))), 0)


def trace_product(a, b):
    return sum(
        (a[i][j] * b[j][i]
         for i in range(len(a)) for j in range(len(a))),
        0,
    )


def dot(a, b):
    return sum((cj(x) * y for x, y in zip(a, b)), 0)


def outer(v):
    return [[x * cj(y) for y in v] for x in v]


def col(a, j):
    return [row[j] for row in a]


def columns(vectors):
    return [[vectors[j][i] for j in range(len(vectors))]
            for i in range(len(vectors[0]))]


def kron(a, b):
    return [
        [a[i][j] * b[k][l]
         for j in range(len(a[0])) for l in range(len(b[0]))]
        for i in range(len(a)) for k in range(len(b))
    ]


def vprod(a, b):
    return [x * y for x in a for y in b]


def density(v):
    v = [G(x) for x in v]
    norm = real(dot(v, v))
    ok(norm > 0, "NONZERO_STATE_VECTOR")
    return ms(outer(v), 1 / norm)


def rank_exact(a):
    a = [[G(x) for x in row] for row in a]
    r = 0
    for c in range(len(a[0])):
        pulse()
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        den = a[r][c]
        a[r] = [x / den for x in a[r]]
        for i in range(r + 1, len(a)):
            if a[i][c]:
                z = a[i][c]
                a[i] = [x - z * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def psd_exact(a, reason):
    ok(a == dag(a), reason + "_HERMITIAN")
    a = [[G(x) for x in row] for row in a]
    n = len(a)
    for k in range(n):
        pulse()
        d = real(a[k][k])
        ok(d >= 0, reason + "_NEGATIVE_PIVOT")
        if d == 0:
            ok(all(a[i][k] == 0 for i in range(k + 1, n)),
               reason + "_ZERO_PIVOT_COLUMN")
            continue
        column = [a[i][k] for i in range(n)]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (
                    a[i][j] - column[i] * cj(column[j]) / d
                )
    return True


def make_state(name, n, terms):
    d = 1 << n
    normalized = []
    for weight, raw in terms:
        weight = F(weight)
        raw = [G(x) for x in raw]
        ok(weight > 0 and len(raw) == d, "STATE_DECOMPOSITION")
        normalized.append((weight, raw))
    ok(sum(w for w, _ in normalized) == 1, "STATE_WEIGHTS")
    rho = lin([(w, density(v)) for w, v in normalized])
    ok(real(tr(rho)) == 1, "INPUT_TRACE_ONE")
    psd_exact(rho, "INPUT_PSD")
    COUNTS["states"] += 1
    return (name, n, normalized, rho)


def bit(i, axis, n):
    return (i >> (n - 1 - axis)) & 1


def pack(i, axes, n):
    out = 0
    for axis in axes:
        out = (out << 1) | bit(i, axis, n)
    return out


def permute_vector(v, old_for_new):
    n = len(old_for_new)
    ok(sorted(old_for_new) == list(range(n)), "PHYSICAL_PERMUTATION")
    out = []
    for new_index in range(1 << n):
        old_index = 0
        for new_axis, old_axis in enumerate(old_for_new):
            old_index |= bit(new_index, new_axis, n) << (n - 1 - old_axis)
        out.append(v[old_index])
    return out


def partial_trace(rho, keep, n):
    d = 1 << n
    rest = tuple(q for q in range(n) if q not in keep)
    rest_mask = sum(1 << (n - 1 - q) for q in rest)
    out = zero(1 << len(keep))
    indices = [pack(i, keep, n) for i in range(d)]
    for i in range(d):
        pulse()
        for j in range(d):
            if (i & rest_mask) == (j & rest_mask):
                out[indices[i]][indices[j]] += rho[i][j]
    return out


def lift(marginal, keep, n):
    d = 1 << n
    rest = tuple(q for q in range(n) if q not in keep)
    mask = sum(1 << (n - 1 - q) for q in rest)
    indices = [pack(i, keep, n) for i in range(d)]
    return [
        [
            marginal[indices[i]][indices[j]]
            if (i & mask) == (j & mask) else 0
            for j in range(d)
        ]
        for i in range(d)
    ]


def erasure_coefficients(rho, n):
    out = []
    for m in range(n + 1):
        total = zero(1 << n)
        for keep in itertools.combinations(range(n), m):
            total = ma(total, lift(partial_trace(rho, keep, n), keep, n))
        out.append(total)
    return out


def matrix_unit_coefficients(rho, n):
    d = 1 << n
    out = [zero(d) for _ in range(n + 1)]
    for i in range(d):
        pulse()
        for j in range(d):
            value = rho[i][j]
            if not value:
                continue
            diagonal_axes = [
                q for q in range(n) if bit(i, q, n) == bit(j, q, n)
            ]
            for count in range(len(diagonal_axes) + 1):
                for erased in itertools.combinations(diagonal_axes, count):
                    mask = sum(1 << (n - 1 - q) for q in erased)
                    base_i, base_j = i & ~mask, j & ~mask
                    for assignment in range(1 << count):
                        fill = 0
                        for r, axis in enumerate(erased):
                            fill |= (
                                ((assignment >> r) & 1)
                                << (n - 1 - axis)
                            )
                        out[count][base_i | fill][base_j | fill] += value
    return out


def pauli_coefficients(rho, n):
    d = 1 << n
    out = [zero(d) for _ in range(n + 1)]
    for x in range(d):
        pulse()
        for z in range(d):
            weight = (x | z).bit_count()
            target = out[weight]
            for i in range(d):
                for j in range(d):
                    value = rho[i][j]
                    if value:
                        sign = -1 if (z & (i ^ j)).bit_count() & 1 else 1
                        target[i ^ x][j ^ x] += sign * value
    return out


def unit_channel(coefficients, s, n):
    c = (1 - s) / 2
    return lin([
        (s ** (n - r) * c ** r, coefficients[r])
        for r in range(n + 1)
    ])


def erasure_channel(coefficients, s, n):
    c = (1 - s) / 2
    return lin([
        (s ** m * c ** (n - m), coefficients[m])
        for m in range(n + 1)
    ])


def pauli_channel(coefficients, s, n):
    qi, qn = (1 + 3 * s) / 4, (1 - s) / 4
    ok(qi >= 0 and qn >= 0 and qi + 3 * qn == 1,
       "PHYSICAL_PAULI_PROBABILITIES")
    return lin([
        (qi ** (n - w) * qn ** w, coefficients[w])
        for w in range(n + 1)
    ])


def spin(a, n):
    d, mask = 1 << n, (1 << n) - 1
    out = zero(d)
    for i in range(d):
        for j in range(d):
            sign = -1 if (i ^ j).bit_count() & 1 else 1
            out[mask ^ i][mask ^ j] = sign * cj(a[i][j])
    return out


def theta(v, n):
    phase = (G(1), J, G(-1), -J)[n % 4]
    mask = (1 << n) - 1
    out = [G() for _ in v]
    for i, x in enumerate(v):
        sign = -1 if i.bit_count() & 1 else 1
        out[mask ^ i] = phase * sign * cj(x)
    return out


def ntheta(v, n):
    phase = (1j) ** n
    mask = (1 << n) - 1
    out = [0j for _ in v]
    for i, x in enumerate(v):
        sign = -1 if i.bit_count() & 1 else 1
        out[mask ^ i] = phase * sign * x.conjugate()
    return out


def full_y(n):
    y = [[G(), -J], [J, G()]]
    out = [[G(1)]]
    for _ in range(n):
        out = kron(out, y)
    return out


def transpose_axes(a, axes, n):
    d = 1 << n
    out = zero(d)
    for i in range(d):
        for j in range(d):
            ii, jj = i, j
            for axis in axes:
                mask = 1 << (n - 1 - axis)
                if (i ^ j) & mask:
                    ii ^= mask
                    jj ^= mask
            out[ii][jj] = a[i][j]
    return out


def fembed(a):
    return (a, zero(len(a), len(a[0])))


def fadd(a, b):
    return (ma(a[0], b[0]), ma(a[1], b[1]))


def fmul(a, b):
    return (
        ma(mm(a[0], b[0]), ms(mm(a[1], b[1]), 3)),
        ma(mm(a[0], b[1]), mm(a[1], b[0])),
    )


def fdag(a):
    return (dag(a[0]), dag(a[1]))


def fspin(a, n):
    return (spin(a[0], n), spin(a[1], n))


def fcomplex(a):
    root = math.sqrt(3.0)
    return [
        [complex(a[0][i][j]) + root * complex(a[1][i][j])
         for j in range(len(a[0][0]))]
        for i in range(len(a[0]))
    ]


def as_complex(a):
    return [[complex(x) for x in row] for row in a]


def frobenius(a):
    return math.sqrt(sum(abs(complex(x)) ** 2 for row in a for x in row))


def distance(a, b):
    return frobenius(sub(a, b))


def eigh(a):
    original = as_complex(a)
    n = len(original)
    scale = max(1.0, frobenius(original))
    ok(distance(original, dag(original)) <= EIG_RESID * scale,
       "NUMERIC_HERMITIAN_INPUT")
    work = [row[:] for row in original]
    vectors = neye(n)
    stop = EIG_STOP * scale
    for _ in range(80):
        pulse()
        largest = 0.0
        for p in range(n):
            for q in range(p + 1, n):
                z = work[p][q]
                r = abs(z)
                largest = max(largest, r)
                if r <= stop:
                    continue
                a0, d0 = work[p][p].real, work[q][q].real
                phase = z / r
                tau = (d0 - a0) / (2.0 * r)
                tangent = (
                    (1.0 if tau >= 0.0 else -1.0)
                    / (abs(tau) + math.sqrt(1.0 + tau * tau))
                )
                cosine = 1.0 / math.sqrt(1.0 + tangent * tangent)
                sine = tangent * cosine
                for i in range(n):
                    if i != p and i != q:
                        ap, aq = work[i][p], work[i][q]
                        work[i][p] = cosine * ap - sine * phase.conjugate() * aq
                        work[i][q] = sine * phase * ap + cosine * aq
                        work[p][i] = work[i][p].conjugate()
                        work[q][i] = work[i][q].conjugate()
                work[p][p] = complex(a0 - tangent * r)
                work[q][q] = complex(d0 + tangent * r)
                work[p][q] = work[q][p] = 0j
                for i in range(n):
                    vp, vq = vectors[i][p], vectors[i][q]
                    vectors[i][p] = (
                        cosine * vp - sine * phase.conjugate() * vq
                    )
                    vectors[i][q] = sine * phase * vp + cosine * vq
        if largest <= stop:
            break
    remaining = max(
        (abs(work[i][j]) for i in range(n) for j in range(i + 1, n)),
        default=0.0,
    )
    ok(remaining <= 4.0 * stop, "EIGENSOLVER_NOT_CONVERGED")
    values = [work[i][i].real for i in range(n)]
    av = mm(original, vectors)
    vd = [[vectors[i][j] * values[j] for j in range(n)]
          for i in range(n)]
    residual = distance(av, vd)
    orthogonal = distance(mm(dag(vectors), vectors), neye(n))
    MAXIMA["eigenpair_residual"] = max(
        MAXIMA["eigenpair_residual"], residual
    )
    MAXIMA["orthogonality_residual"] = max(
        MAXIMA["orthogonality_residual"], orthogonal
    )
    ok(residual <= EIG_RESID * scale, "EIGENPAIR_RESIDUAL")
    ok(orthogonal <= EIG_RESID, "EIGENVECTOR_ORTHOGONALITY")
    order = sorted(range(n), key=lambda j: values[j], reverse=True)
    return (
        [values[j] for j in order],
        [[vectors[i][j] for j in order] for i in range(n)],
    )


def numeric_majorization(a, reference, reason):
    values, _ = eigh(a)
    running = target = 0.0
    for value, bound in zip(values, reference):
        running += value
        target += float(bound)
        MAXIMA["numeric_prefix_excess"] = max(
            MAXIMA["numeric_prefix_excess"], running - target
        )
        ok(running <= target + TOL, reason)
    ok(abs(running - target) <= TOL, reason + "_TRACE")
    return values


def exact_projectors(n):
    d = 1 << n
    v = [
        G(1 + j % 3, (1 if j % 2 == 0 else -1) * (1 + j % 2))
        for j in range(d)
    ]
    unitary = sub(eye(d), ms(outer(v), 2 / real(dot(v, v))))
    ok(mm(dag(unitary), unitary) == eye(d), "PROJECTOR_UNITARY")
    out, current = [], zero(d)
    for k in range(d):
        current = ma(current, outer(col(unitary, k)))
        ok(current == dag(current), "PROJECTOR_HERMITIAN")
        ok(mm(current, current) == current, "PROJECTOR_IDEMPOTENT")
        ok(real(tr(current)) == k + 1, "PROJECTOR_RANK_VIA_TRACE")
        out.append(current)
    ok(any(G(x).im for row in out[0] for x in row),
       "GENUINELY_COMPLEX_PROJECTOR")
    for q in out:
        transported = spin(q, n)
        ok(mm(transported, transported) == transported,
           "TRANSPORTED_PROJECTOR_IDEMPOTENT")
        ok(real(tr(transported)) == real(tr(q)),
           "TRANSPORTED_PROJECTOR_RANK")
    return out


def reference_values(n, t):
    a, b = (1 + t) / 2, (1 - t) / 2
    return sorted(
        [a ** (n - i.bit_count()) * b ** i.bit_count()
         for i in range(1 << n)],
        reverse=True,
    )


def local_symplectic_unitary():
    u = [[G(F(3, 5)), G(0, F(4, 5))],
         [G(0, F(4, 5)), G(F(3, 5))]]
    v = [[G(F(5, 13)), G(F(-12, 13))],
         [G(F(12, 13)), G(F(5, 13))]]
    w = [[G(F(3, 5), F(4, 5)), G()],
         [G(), G(F(3, 5), F(-4, 5))]]
    total = kron(kron(u, v), w)
    ok(mm(dag(total), total) == eye(8), "SYMPLECTIC_UNITARY")
    ok(spin(total, 3) == total, "SYMPLECTIC_THETA_COMMUTATION")
    return total


def exact_paired_vertices(p, unitary):
    for mask in range(16):
        pulse()
        chosen = [
            (7 ^ i) if (mask >> i) & 1 else i for i in range(4)
        ]
        v = columns([col(unitary, j) for j in chosen])
        pi = mm(v, dag(v))
        ok(mm(dag(v), v) == eye(4), "PAIRED_ORTHONORMAL_COLUMNS")
        ok(mm(pi, pi) == pi and real(tr(pi)) == 4,
           "PAIRED_PROJECTOR_RANK_FOUR")
        ok(spin(pi, 3) == sub(eye(8), pi),
           "PAIRED_THETA_COMPLEMENT")
        ok(real(trace_product(p, pi)) == 1, "PAIRED_P_OVERLAP_ONE")
        pv = mm(p, v)
        r = mm(dag(v), pv)
        ok(real(tr(r)) == 1 and rank_exact(r) <= 2,
           "ACTUAL_COMPRESSION_TRACE_RANK")
        psd_exact(r, "COMPRESSION_PSD")
        psd_exact(sub(eye(4), r), "COMPRESSION_LE_IDENTITY")
        c = ma(eye(4), ms(r, 2))
        ok(rank_exact(c) == 4 and real(tr(c)) == 6,
           "GRAM_COMPRESSION_RANK_TRACE")
        psd_exact(sub(ms(eye(4), 3), c), "GRAM_COMPRESSION_LE_THREE")
        bfield = (sub(v, pv), pv)
        xfield = fmul(bfield, fdag(bfield))
        ok(fmul(fdag(bfield), bfield) == fembed(c),
           "ACTUAL_RECTANGULAR_GRAM_COMPRESSION")
        pp = mm(p, pi)
        qp = mm(pi, p)
        pqp = mm(pp, p)
        expected = (
            lin([(1, pi), (-1, pp), (-1, qp), (4, pqp)]),
            lin([(1, pp), (1, qp), (-2, pqp)]),
        )
        ok(xfield == expected, "ACTUAL_SQRT_G_PROJECTOR_PRODUCT")
        ok(real(tr(xfield[0])) == 6 and tr(xfield[1]) == 0,
           "ACTUAL_VERTEX_TRACE_SIX")
        COUNTS["exact_paired_vertices"] += 1


def numeric_paired_effect(zfield, sfield, p, h2):
    z = fcomplex(zfield)
    s = fcomplex(sfield)
    values, vectors = eigh(z)
    ok(min(values) >= -PAIR_TOL and max(values) <= 1 + PAIR_TOL,
       "NUMERIC_EFFECT_INTERVAL")
    order = (
        [i for i, x in enumerate(values) if x > 0.5 + PAIR_TOL]
        + [i for i, x in enumerate(values)
           if abs(x - 0.5) <= PAIR_TOL]
    )
    pairs, used = [], []
    for index in order:
        candidate = col(vectors, index)
        for old in used:
            coefficient = dot(old, candidate)
            candidate = [
                x - coefficient * y for x, y in zip(candidate, old)
            ]
        norm = math.sqrt(sum(abs(x) ** 2 for x in candidate))
        if norm <= 1.0e-7:
            continue
        u = [x / norm for x in candidate]
        v = ntheta(u, 3)
        lam = dot(u, col(mm(z, columns([u])), 0)).real
        ok(-PAIR_TOL <= lam <= 1 + PAIR_TOL,
           "PAIRED_RAYLEIGH_INTERVAL")
        zu = col(mm(z, columns([u])), 0)
        zv = col(mm(z, columns([v])), 0)
        ok(math.sqrt(sum(abs(x - lam * y) ** 2
                         for x, y in zip(zu, u))) <= PAIR_TOL,
           "PAIRED_U_EIGEN_RESIDUAL")
        ok(math.sqrt(sum(abs(x - (1 - lam) * y) ** 2
                         for x, y in zip(zv, v))) <= PAIR_TOL,
           "PAIRED_THETA_EIGEN_RESIDUAL")
        pairs.append((u, v, lam))
        used.extend([u, v])
        if len(pairs) == 4:
            break
    ok(len(pairs) == 4, "COMPLETE_PAIRED_EIGENBASIS")
    basis = columns(used)
    ok(distance(mm(dag(basis), basis), neye(8)) <= PAIR_TOL,
       "PAIRED_BASIS_ORTHOGONALITY")
    zsum, hsum, weights = zero(8), zero(8), 0.0
    for mask in range(16):
        chosen, weight = [], 1.0
        for i, (u, v, lam) in enumerate(pairs):
            take_partner = (mask >> i) & 1
            chosen.append(v if take_partner else u)
            weight *= (1 - lam) if take_partner else lam
        ok(weight >= -PAIR_TOL, "PAIRED_NUMERIC_WEIGHT")
        vv = columns(chosen)
        pi = mm(vv, dag(vv))
        ok(distance(spin(pi, 3), sub(neye(8), pi)) <= PAIR_TOL,
           "NUMERIC_PAIRED_THETA_COMPLEMENT")
        ok(abs(complex(trace_product(as_complex(p), pi)) - 1)
           <= PAIR_TOL, "NUMERIC_PAIRED_P_OVERLAP")
        x = mm(mm(s, pi), s)
        numeric_majorization(
            x, [3, 1, 1, 1, 0, 0, 0, 0],
            "NUMERIC_ACTUAL_VERTEX_PREFIX",
        )
        zsum = ma(zsum, ms(pi, weight))
        hsum = ma(hsum, ms(x, weight))
        weights += weight
        COUNTS["numeric_paired_vertices"] += 1
    residual = max(
        distance(zsum, z),
        distance(hsum, as_complex(h2)),
        abs(weights - 1),
    )
    MAXIMA["paired_reconstruction"] = max(
        MAXIMA["paired_reconstruction"], residual
    )
    ok(residual <= PAIR_TOL, "PAIRED_EFFECT_RECONSTRUCTION")


def three_qubit_structure(state, erasures, symplectic):
    _, n, terms, rho = state
    ok(n == 3, "THREE_QUBIT_STRUCTURE_DIMENSION")
    h1, h2 = erasures[1], erasures[2]
    identity = eye(8)
    p = ma(rho, spin(rho, 3))
    ok(real(tr(h1)) == 12, "H1_TRACE_TWELVE")
    ok(real(tr(h2)) == 6, "H2_TRACE_SIX")
    ok(spin(rho, 3) == lin([
        (1, identity), (-1, h1), (1, h2), (-1, rho)
    ]), "ACTUAL_MARGINAL_SPIN_IDENTITY")
    ok(spin(h1, 3) == sub(ms(identity, 3), h1),
       "H1_SPIN_COMPLEMENT")
    ok(ma(h2, spin(h2, 3)) == ma(identity, ms(p, 2)),
       "H2_SPIN_COUPLING")
    psd_exact(h1, "H1_PSD")
    psd_exact(h2, "H2_PSD")
    psd_exact(spin(h2, 3), "SPIN_H2_PSD")
    numeric_majorization(
        h1, [3, 2, 2, 2, 1, 1, 1, 0], "H1_PREFIX"
    )
    numeric_majorization(
        h2, [3, 1, 1, 1, 0, 0, 0, 0], "H2_PREFIX"
    )
    if len(terms) != 1:
        return
    raw = terms[0][1]
    ok(theta(theta(raw, 3), 3) == [-x for x in raw],
       "THETA_SQUARE_MINUS_IDENTITY")
    ok(dot(raw, theta(raw, 3)) == 0, "PURE_THETA_ORTHOGONALITY")
    ok(mm(p, p) == p and rank_exact(p) == 2,
       "PURE_P_RANK_TWO_PROJECTOR")
    ok(spin(p, 3) == p, "PURE_P_THETA_INVARIANT")
    g = ma(identity, ms(p, 2))
    sfield = (sub(identity, p), p)
    inverse = (sub(identity, p), ms(p, F(1, 3)))
    ok(fmul(sfield, sfield) == fembed(g), "SQRT_G_SQUARE")
    ok(fmul(sfield, inverse) == fembed(identity), "SQRT_G_INVERSE")
    ok(fmul(inverse, sfield) == fembed(identity), "INVERSE_SQRT_G")
    zfield = fmul(fmul(inverse, fembed(h2)), inverse)
    szfield = fspin(zfield, 3)
    ok(fdag(zfield) == zfield, "EFFECT_HERMITIAN")
    ok(fadd(zfield, szfield) == fembed(identity),
       "EFFECT_SPIN_SUM_IDENTITY")
    ok(fmul(fmul(sfield, zfield), sfield) == fembed(h2),
       "EFFECT_POSITIVE_CONGRUENCE")
    ok(fmul(fmul(sfield, szfield), sfield)
       == fembed(spin(h2, 3)), "SPIN_EFFECT_POSITIVE_CONGRUENCE")
    exact_paired_vertices(p, symplectic)
    numeric_paired_effect(zfield, sfield, p, h2)


def assigned_example(star, erasures, coefficients):
    rho = star[3]
    m = [[G(F(3, 4)), G(F(1, 4))],
         [G(F(1, 4)), G(F(1, 4))]]
    pair = [
        [G(F(x, 4)) for x in row]
        for row in ((2, 1, 1, 0), (1, 1, 1, 0),
                    (1, 1, 1, 0), (0, 0, 0, 0))
    ]
    for axis in range(3):
        ok(partial_trace(rho, (axis,), 3) == m,
           "PSISTAR_SINGLE_MARGINAL")
    for keep in itertools.combinations(range(3), 2):
        ok(partial_trace(rho, keep, 3) == pair,
           "PSISTAR_PAIR_MARGINAL")
    det = real(m[0][0] * m[1][1] - m[0][1] * m[1][0])
    ok(det == F(1, 8) and 1 - 4 * det == F(1, 2),
       "PSISTAR_NONDEGENERATE_MARGINAL")
    had = [[G(1), G(1)], [G(1), G(-1)]]
    unnormalized = kron(kron(had, had), had)
    expectation = real(trace_product(rho, unnormalized))
    ok(expectation == F(5, 2), "PSISTAR_HADAMARD_SIGN_SUM")
    ok(expectation * expectation / 8 == F(25, 32),
       "PSISTAR_LOCAL_PARITY_EXCLUSION")
    ok(real(trace_product(rho, erasures[1])) == F(9, 4),
       "PSISTAR_H1_SAME_Q")
    ok(real(trace_product(rho, erasures[2])) == F(9, 4),
       "PSISTAR_H2_SAME_Q")
    output = unit_channel(coefficients, F(3, 4), 3)
    ok(real(trace_product(rho, output)) == F(623, 1024),
       "PSISTAR_CHANNEL_SAME_Q_623")
    ok(reference_values(3, F(3, 4))[0] == F(686, 1024),
       "PSISTAR_REFERENCE_686")


def expect_rejection(reason, operation):
    try:
        operation()
    except CheckFailure as exc:
        ok(str(exc) == reason, "MUTATION_WRONG_REJECTION_REASON")
        MUTATIONS.append(reason)
        COUNTS["mutations"] += 1
        return
    raise CheckFailure("MUTATION_NOT_REJECTED_" + reason)


def mutation_controls(star, generic, product_y, mixed_identity, caches):
    h2 = caches[generic[0]][1][2]
    expect_rejection(
        "MUT_NORMALIZATION_H2_TRACE_SIX",
        lambda: ok(real(tr(ms(h2, F(1, 2)))) == 6,
                   "MUT_NORMALIZATION_H2_TRACE_SIX"),
    )
    rho = generic[3]
    ac = partial_trace(rho, (0, 2), 3)
    bad_h2 = ma(
        sub(h2, lift(ac, (0, 2), 3)),
        lift(ac, (0, 1), 3),
    )
    psd_exact(bad_h2, "TENSOR_MUTANT_PSD_PREREQUISITE")
    ok(real(tr(bad_h2)) == 6, "TENSOR_MUTANT_TRACE_PREREQUISITE")
    expect_rejection(
        "MUT_AC_PHYSICAL_FACTOR_EMBEDDING",
        lambda: ok(bad_h2 == h2, "MUT_AC_PHYSICAL_FACTOR_EMBEDDING"),
    )
    y = full_y(3)
    yrho = product_y[3]
    wrong_spin = mm(mm(y, yrho), y)
    psd_exact(wrong_spin, "ANTICONJ_MUTANT_PSD_PREREQUISITE")
    expect_rejection(
        "MUT_ANTIUNITARY_CONJUGATION",
        lambda: ok(wrong_spin == spin(yrho, 3),
                   "MUT_ANTIUNITARY_CONJUGATION"),
    )
    units = caches[product_y[0]][0]
    plus = unit_channel(units, F(1, 3), 3)
    minus = unit_channel(units, F(-1, 3), 3)
    ok(minus == spin(plus, 3), "NEGATIVE_BRANCH_POSITIVE_CONTROL")
    partial = mm(mm(y, transpose_axes(plus, (0,), 3)), y)
    psd_exact(partial, "PARTIAL_MUTANT_PSD_PREREQUISITE")
    ok(real(tr(partial)) == 1, "PARTIAL_MUTANT_TRACE_PREREQUISITE")
    expect_rejection(
        "MUT_FULL_NOT_PARTIAL_TRANSPOSE",
        lambda: ok(partial == minus, "MUT_FULL_NOT_PARTIAL_TRANSPOSE"),
    )
    correct = real(trace_product(yrho, minus))
    transported = real(trace_product(spin(yrho, 3), plus))
    ok(correct == transported, "Q_TRANSPORT_POSITIVE_CONTROL")
    expect_rejection(
        "MUT_Q_SPIN_TRANSPORT_REQUIRED",
        lambda: ok(real(trace_product(yrho, plus)) == correct,
                   "MUT_Q_SPIN_TRANSPORT_REQUIRED"),
    )
    mixed_p = ma(mixed_identity[3], spin(mixed_identity[3], 3))
    ok(real(tr(mixed_p)) == 2 and rank_exact(mixed_p) == 8,
       "MIXED_P_COUNTERCONTROL_PREREQUISITE")
    expect_rejection(
        "MUT_MIXED_P_IS_NOT_PROJECTOR",
        lambda: ok(mm(mixed_p, mixed_p) == mixed_p,
                   "MUT_MIXED_P_IS_NOT_PROJECTOR"),
    )
    s, b = F(3, 4), F(1, 8)
    star_units, star_erasures, _ = caches[star[0]]
    actual = unit_channel(star_units, s, 3)
    omitted = sub(actual, ms(star_erasures[2], s * s * b))
    psd_exact(omitted, "OMITTED_H2_PSD_PREREQUISITE")
    expect_rejection(
        "MUT_H2_LAYER_REQUIRED",
        lambda: ok(omitted == actual, "MUT_H2_LAYER_REQUIRED"),
    )
    q = zero(8)
    for bits in range(8):
        if bits.bit_count() <= 1:
            vector = [G(1)]
            for axis in range(3):
                sign = -1 if bit(bits, axis, 3) else 1
                vector = vprod(vector, [G(1), sign * J])
            q = ma(q, density(vector))
    ok(q == dag(q) and mm(q, q) == q and real(tr(q)) == 4,
       "COORDER_MUTANT_PROJECTOR_PREREQUISITE")
    actual_product = unit_channel(units, s, 3)
    observed = real(trace_product(q, actual_product))
    true_bound = sum(reference_values(3, s)[:4])
    ok(observed == true_bound, "COORDER_PRODUCT_SATURATION_CONTROL")
    wrong_bound = s ** 3 + 6 * s * s * b + 8 * s * b * b + 4 * b ** 3
    expect_rejection(
        "MUT_COORDERED_REFERENCE_PREFIX",
        lambda: ok(observed <= wrong_bound,
                   "MUT_COORDERED_REFERENCE_PREFIX"),
    )


def build_states():
    star_raw = [1, 1, 1, 0, 1, 0, 0, 0]
    generic_raw = [G(1), G(1), J, G(2), -J, 1 + J, 2 - J, G(1)]
    plus_y = [G(1), J]
    product_raw = vprod(vprod(plus_y, plus_y), plus_y)
    bell_raw = vprod([G(1), G(), G(), G(1)], plus_y)
    star = make_state("psi_star", 3, [(1, star_raw)])
    generic = make_state("generic_complex", 3, [(1, generic_raw)])
    product_y = make_state("product_plus_y", 3, [(1, product_raw)])
    bell = make_state("bell_ab_plus_y_c", 3, [(1, bell_raw)])
    identity_terms = []
    for j in range(8):
        vector = [G(int(i == j)) for i in range(8)]
        identity_terms.append((F(1, 8), vector))
    mixed_identity = make_state("mixed_identity", 3, identity_terms)
    mixed_two = make_state(
        "mixed_two_nonparity", 3,
        [(F(1, 2), star_raw), (F(1, 2), generic_raw)],
    )
    triples = [star, generic, product_y, bell, mixed_identity, mixed_two]
    quads, hull = [], []
    spectator_product = vprod(plus_y, generic_raw)
    for spectator in range(4):
        order, rest = [], iter((1, 2, 3))
        for axis in range(4):
            order.append(0 if axis == spectator else next(rest))
        raw = permute_vector(spectator_product, order)
        quads.append(make_state(
            "cut_1_3_spectator_" + str(spectator), 4, [(1, raw)]
        ))
        hull.append((F(1, 7), raw))
    pair_a = [G(1), J, 1 + J, G(2)]
    pair_b = [G(1), 2 - J, J, 1 + J]
    pair_product = vprod(pair_a, pair_b)
    orders = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 2, 3, 1)]
    for index, order in enumerate(orders):
        raw = permute_vector(pair_product, order)
        quads.append(make_state(
            "cut_2_2_" + str(index), 4, [(1, raw)]
        ))
        hull.append((F(1, 7), raw))
    quads.append(make_state("mixed_all_seven_cuts", 4, hull))
    return triples, quads, star, generic, product_y, mixed_identity


def main():
    global STAGE
    STAGE = "physical input construction"
    triples, quads, star, generic, product_y, mixed_identity = build_states()
    projectors = {3: exact_projectors(3), 4: exact_projectors(4)}
    symplectic = local_symplectic_unitary()
    caches = {}
    parameters = [
        F(0), F(1, 4), F(1, 2), F(2, 3),
        F(5, 6), F(1), F(7, 6), F(4, 3),
    ]
    for state in triples + quads:
        name, n, terms, rho = state
        STAGE = "independent coefficients: " + name
        pulse()
        units = matrix_unit_coefficients(rho, n)
        erasures = erasure_coefficients(rho, n)
        paulis = pauli_coefficients(rho, n)
        caches[name] = (units, erasures, paulis)
        for r in range(n + 1):
            ok(units[r] == erasures[n - r],
               "MATRIX_UNIT_ERASURE_COEFFICIENT_EQUALITY")
            ok(real(tr(erasures[r]))
               == math.comb(n, r) * (1 << (n - r)),
               "ERASURE_TRACE_NORMALIZATION")
            ok(real(tr(paulis[r])) == math.comb(n, r) * 3 ** r,
               "PAULI_GROUP_TRACE_NORMALIZATION")
        if n == 3:
            STAGE = "actual H2 and paired geometry: " + name
            three_qubit_structure(state, erasures, symplectic)
        if name == star[0]:
            assigned_example(star, erasures, units)
        for p in parameters:
            STAGE = "physical channel and all prefixes: " + name + ":" + str(p)
            pulse()
            s, t = 1 - p, abs(1 - p)
            actual = unit_channel(units, s, n)
            erased = erasure_channel(erasures, s, n)
            kraus = pauli_channel(paulis, s, n)
            ok(actual == erased, "ACTUAL_CHANNEL_ERASURE_AGREEMENT")
            ok(actual == kraus, "ACTUAL_CHANNEL_PAULI_AGREEMENT")
            ok(actual == dag(actual) and real(tr(actual)) == 1,
               "ACTUAL_OUTPUT_DENSITY_NORMALIZATION")
            if s == 1:
                ok(actual == rho, "IDENTITY_CHANNEL_ENDPOINT")
            if s == 0:
                ok(actual == ms(eye(1 << n), F(1, 1 << n)),
                   "DEPOLARIZING_ENDPOINT")
            reference = reference_values(n, t)
            values, _ = eigh(actual)
            ok(min(values) >= -TOL, "NUMERIC_OUTPUT_POSITIVITY")
            eigen_prefix, reference_prefix = 0.0, F(0)
            plus = unit_channel(units, t, n) if s < 0 else None
            if s < 0:
                ok(actual == spin(plus, n), "FULL_NEGATIVE_BRANCH")
            for k, q in enumerate(projectors[n], 1):
                reference_prefix += reference[k - 1]
                eigen_prefix += values[k - 1]
                expectation = real(trace_product(q, actual))
                ok(F(0) <= expectation <= reference_prefix,
                   "EXACT_SAME_COMPLEX_Q_REFERENCE_BOUND")
                ok(float(expectation) <= eigen_prefix + TOL,
                   "SAME_Q_BELOW_ACTUAL_NUMERIC_PREFIX")
                excess = eigen_prefix - float(reference_prefix)
                MAXIMA["numeric_prefix_excess"] = max(
                    MAXIMA["numeric_prefix_excess"], excess
                )
                ok(excess <= TOL, "ACTUAL_NUMERIC_OUTPUT_PREFIX")
                if s < 0:
                    ok(expectation == real(trace_product(spin(q, n), plus)),
                       "EXACT_COMPLEX_Q_NEGATIVE_TRANSPORT")
                COUNTS["prefixes"] += 1
            ok(abs(eigen_prefix - 1.0) <= TOL, "NUMERIC_OUTPUT_TRACE")
            COUNTS["physical_cases"] += 1
    STAGE = "intended-reason mutation controls"
    mutation_controls(star, generic, product_y, mixed_identity, caches)
    ok(COUNTS["states"] == 14, "COMPLETE_STATE_COVERAGE")
    ok(COUNTS["physical_cases"] == 112, "COMPLETE_CHANNEL_COVERAGE")
    ok(COUNTS["prefixes"] == 1408, "COMPLETE_PREFIX_COVERAGE")
    ok(COUNTS["exact_paired_vertices"] == 64,
       "COMPLETE_EXACT_PAIRED_VERTEX_COVERAGE")
    ok(COUNTS["numeric_paired_vertices"] == 64,
       "COMPLETE_NUMERIC_PAIRED_VERTEX_COVERAGE")
    ok(COUNTS["mutations"] == 8, "COMPLETE_MUTATION_COVERAGE")
    pulse()
    print("STATUS=CHECKS_COMPLETED_NO_RECORDED_FAILURE")
    print("SCOPE=finite exact matrix checks plus numerical spectra; not a uniform proof")
    print("TOLERANCES=" + repr((TOL, EIG_STOP, EIG_RESID, PAIR_TOL)))
    for key, value in COUNTS.items():
        print("COUNT_" + key + "=" + str(value))
    for key, value in MAXIMA.items():
        print("MAX_" + key + "=" + repr(value))
    for reason in MUTATIONS:
        print("INTENDED_MUTATION_REJECTION=" + reason)
    print("ELAPSED_SECONDS=" + repr(time.monotonic() - START))


if __name__ == "__main__":
    try:
        main()
    except Deadline as exc:
        print("STATUS=INCOMPLETE_DEADLINE")
        print("STAGE=" + str(exc))
        for key, value in COUNTS.items():
            print("COMPLETED_" + key + "=" + str(value))
        sys.exit(2)
    except CheckFailure as exc:
        print("STATUS=CHECK_FAILURE_NOT_AUTOMATIC_THEOREM_COUNTEREXAMPLE")
        print("STAGE=" + STAGE)
        print("REASON=" + str(exc))
        sys.exit(1)
END PYTHON SOURCE

## 5. Disposition boundary

- **Observed execution output:** none.
- **Executed mutation rejections:** none.
- **Measured runtime, memory, numerical residuals, and completed-case counts:** none.
- **Source syntax/runtime correctness:** unverified.
- **Finite corroboration gate:** unfulfilled because execution is runtime-restricted.
- **Written audit:** no mathematical defect identified in the new paired-projection lemma or its stated consumers.
- **Adoption, independent-family assurance, human/kernel verification, novelty, and unrestricted four-qubit closure:** not asserted.

Findings: none.

Overall correctness: correct.

Explanation: No provable defect was identified in the fully read candidate’s stated three-qubit theorem or four-qubit separable consequences. This is a written-review conclusion only; the independent finite verification remains NOT_RUN, and the supplied source requires actual execution before any computational corroboration can be credited.

Confidence: 0.84.