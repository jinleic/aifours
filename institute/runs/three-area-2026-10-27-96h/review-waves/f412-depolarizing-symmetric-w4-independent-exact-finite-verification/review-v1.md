# F412 FINITE — complete materializable return

**Status: independent written reconstruction completed; executable supplied, NOT RUN. Parent disposition remains required.** No scientific executable, child process, package installation, file modification, or external-model call was performed.

## Input and method boundary

I read the complete manifest and receipt, all seven status/permission controls, the parent dispatch and metadata-supply records, and then the complete ordered literal packet, S1 lines 1–101, including its ending.

The following hashes are **parent-supplied metadata, not child-computed hash observations**:

- Manifest: `472828666b87e4c74d019b4fd52ae9bd4275e556fb8d30a9ce849290efb415b5`.
- Receipt: `b67be2638b414ffe6f59d2675011b71f338cbea506f9ce8a77d99f8f32168f10`.
- Packet: `b38d708c42fcd490931170b7cbb65c8242e4779f6b652323258d04f7f1820f9c`.
- S1: `8802cec012ddeac98128311040f5a14fb3067dc17eb8833d9f34deca15894b12`.

I did not read linked parent programs, linked computation receipts/results, sibling returns, or held mathematical payloads or consumers. S1 itself exposes the author’s formulas and table: this reconstruction is **not blinded**. Independence here means separately derived algebra and separately authored code, not an assertion about unobservable cognition or model-family independence.

The review-role restriction prevents executing or materializing the scientific program in this child. Consequently, the calculations below are **written exact derivations**; there is no child runtime receipt, native completion clock, or execution PASS claim.

## 1. Physical channel reconstruction

Write \(D_t(X)=tX+(1-t)\operatorname{Tr}(X)I/2\), with \(0\leq t\leq1\), and put \(a=(1+t)/2\), \(b=(1-t)/2\).

Its matrix-unit action is

\[
D_t(E_{00})=aE_{00}+bE_{11},\quad
D_t(E_{11})=bE_{00}+aE_{11},\quad
D_t(E_{01})=tE_{01},\quad
D_t(E_{10})=tE_{10}.
\]

Since \(\rho_W=\frac14\sum_{i,j=1}^4 E_{e_i,e_j}\), these four rules determine every one of the 256 output entries.

For a diagonal output index of weight \(k\), an occupied input site lies in its support in exactly \(k\) terms and outside it in exactly \(4-k\) terms. This gives

\[
d_k=\frac{k a^{5-k}b^{k-1}+(4-k)a^{3-k}b^{k+1}}4
\]

for \(1\leq k\leq3\), and \(d_0=a^3b,\ d_4=ab^3\).

An off-diagonal input term has precisely two differing sites. Their matrix units remain off-diagonal and contribute \(t^2\); the other two sites remain diagonal. Thus:

- Different output weights have zero matrix entry.
- Equal-weight, distinct outputs have a nonzero entry only when their supports differ by one exchange.
- That entry is \(g_k=t^2a^{3-k}b^{k-1}/4\).

This is an exhaustive entry classification, not a selected-entry test.

### Independent Johnson-spectrum derivation

For weights 1 and 3, the graph is \(K_4\), whose adjacency matrix is \(J-I\), giving eigenvalues \(3,-1,-1,-1\).

For weight 2, label vertices by two-subsets of four sites. Let \(R\) interchange each two-subset with its disjoint complement. Then

\[
A=J_6-I_6-R.
\]

The \(R\)-even subspace has dimension 3; its all-ones direction has \(A\)-eigenvalue 4 and its two-dimensional orthogonal complement has eigenvalue \(-2\). The \(R\)-odd subspace has dimension 3 and eigenvalue 0. Therefore the spectrum is \(4,0,0,0,-2,-2\).

This derivation does not use the author’s incidence-matrix argument. The supplied program additionally derives the characteristic polynomials from exact matrix traces and factors them over the integers.

## 2. Independently expanded eigenvalue polynomials

In the following table, the last column is the coefficient vector of \(16\lambda(t)\) in ascending powers \(1,t,t^2,t^3,t^4\).

| Group | Multiplicity | Power coefficient vector |
|---|---:|---|
| weight 0 | 1 | \(1,2,0,-2,-1\) |
| weight 1, adjacency 3 | 1 | \(1,1,3,7,4\) |
| weight 1, adjacency −1 | 3 | \(1,1,-1,-1,0\) |
| weight 2, adjacency 4 | 1 | \(1,0,4,0,-5\) |
| weight 2, adjacency 0 | 3 | \(1,0,0,0,-1\) |
| weight 2, adjacency −2 | 2 | \(1,0,-2,0,1\) |
| weight 3, adjacency 3 | 1 | \(1,-1,3,-7,4\) |
| weight 3, adjacency −1 | 3 | \(1,-1,-1,1,0\) |
| weight 4 | 1 | \(1,-2,0,2,-1\) |

Their multiplicity-weighted sum is the constant polynomial 1.

For \(p(t)=\sum_{r=0}^4c_rt^r\), the degree-four Bernstein coefficients are

\[
\beta_j(p)=\sum_{r=0}^j c_r\frac{\binom jr}{\binom4r}.
\]

Indeed, substituting this expression and using
\(\binom4j\binom jr=\binom4r\binom{4-r}{j-r}\)
recovers \(t^r\) exactly. This also supplies an exact round-trip invariant for the implementation.

For a polynomial whose power vector is \(P/16\), its scaled coefficients are especially easy to reconstruct:

\[
\begin{aligned}
192\beta_0&=12P_0,\\
192\beta_1&=12P_0+3P_1,\\
192\beta_2&=12P_0+6P_1+2P_2,\\
192\beta_3&=12P_0+9P_1+6P_2+3P_3,\\
192\beta_4&=12(P_0+P_1+P_2+P_3+P_4).
\end{aligned}
\]

### Maximal coefficient vectors

Sorting the sixteen individual W coefficients separately for each \(j\) gives the following vectors. Every entry here is scaled by 192; superscripts indicate repetitions.

- \(j=0:\quad 12^{\times16}\).
- \(j=1:\quad 18,\ 15^{\times4},\ 12^{\times6},\ 9^{\times4},\ 6\).
- \(j=2:\quad 24^{\times2},\ 20,\ 16^{\times3},\ 12^{\times4},\ 8^{\times2},\ 4^{\times3},\ 0\).
- \(j=3:\quad 60,\ 36,\ 24,\ 12^{\times6},\ 0^{\times7}\).
- \(j=4:\quad 192,\ 0^{\times15}\).

Let \(M_{j,k}\) be their \(k\)-prefix sum, still scaled by 192. The complete nontrivial rows, for \(k=0,\ldots,16\), are:

- \(M_{1,k}\):  
  0, 18, 33, 48, 63, 78, 90, 102, 114, 126, 138, 150, 159, 168, 177, 186, 192.
- \(M_{2,k}\):  
  0, 24, 48, 68, 84, 100, 116, 128, 140, 152, 164, 172, 180, 184, 188, 192, 192.
- \(M_{3,k}\):  
  0, 60, 96, 120, 132, 144, 156, 168, 180, 192, 192, 192, 192, 192, 192, 192, 192.

The other two complete rows are specified by
\(M_{0,k}=12k\), and \(M_{4,0}=0,\ M_{4,k}=192\) for \(1\leq k\leq16\).

The ordered reference coefficients, independently obtained from \(a^{4-h}b^h\), are:

- \(j=0:\ 12^{\times16}\).
- \(j=1:\ 24,\ 18^{\times4},\ 12^{\times6},\ 6^{\times4},\ 0\).
- \(j=2:\ 48,\ 24^{\times4},\ 8^{\times6},\ 0^{\times5}\).
- \(j=3:\ 96,\ 24^{\times4},\ 0^{\times11}\).
- \(j=4:\ 192,\ 0^{\times15}\).

The reference eigenvalue ordering is valid throughout the interval because each consecutive distinct group difference is \(t a^{3-h}b^h\geq0\).

### Complete independently reconstructed gap table

Subtracting the maximal W prefixes from the fixed reference prefixes gives \(192G_{j,k}\), for all 85 pairs \(0\leq j\leq4,\ 0\leq k\leq16\):

| \(j\) | \(192G_{j,k}\), \(k=0,\ldots,16\) |
|---:|---|
| 0 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |
| 1 | 0, 6, 9, 12, 15, 18, 18, 18, 18, 18, 18, 18, 15, 12, 9, 6, 0 |
| 2 | 0, 24, 24, 28, 36, 44, 36, 32, 28, 24, 20, 20, 12, 8, 4, 0, 0 |
| 3 | 0, 36, 24, 24, 36, 48, 36, 24, 12, 0, 0, 0, 0, 0, 0, 0, 0 |
| 4 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 |

These rows agree with S1 after independent power expansion, conversion, sorting, and prefix arithmetic. They are not reported as executed program output.

For any fixed subset \(S\) of \(k\) eigenvalue positions, its coefficient at each \(j\) is at most \(M_{j,k}/192\). Nonnegativity of the displayed gaps and of the Bernstein basis therefore bounds its sum by the reference \(k\)-prefix on the entire interval. Maximizing over subsets proves every Ky Fan prefix. Different coefficient rows need not have the same maximizing subset.

At \(t=0\), both spectra are uniform \(1/16\). At \(t=1\), both have one eigenvalue 1 and fifteen zeros. Thus the degenerate reference endpoints are included without assuming a persistent strict ordering.

## 3. Negative branch and genuinely complex consuming-projector control

For every qubit matrix,

\[
Y X^T Y=\operatorname{Tr}(X)I-X.
\]

Consequently \(D_{-t}=R\circ D_t\), where \(R(X)=YX^TY\), and

\[
D_{-t}^{\otimes4}(\rho)
=U[D_t^{\otimes4}(\rho)]^TU,\qquad U=Y^{\otimes4}.
\]

This is an all-matrix algebraic identity, not an extrapolation from selected states. Physical negative-branch parameters satisfy \(0\leq t\leq1/3\). Transposition and unitary conjugation preserve the spectrum. The consuming projector must be transported to

\[
Q'=UQ^TU,
\]

which is again an orthogonal projector of the same rank. Keeping \(Q\) unchanged is generally wrong.

Here is an exact selected control for that last boundary. Use local phases

\[
\alpha=(1,i,(3+4i)/5,(5+12i)/13),\qquad
|\psi\rangle=\tfrac12\sum_i\alpha_i|e_i\rangle.
\]

Let \(f_i\) be the bitwise complement of \(e_i\), and let \(Q\) project onto
\((|f_0\rangle+i|f_1\rangle)/\sqrt2\). Both the density and projector have genuinely nonreal entries.

At \(t=1/3\), write \(A=D_t^{\otimes4}(\rho_\psi)\) and \(B=D_{-t}^{\otimes4}(\rho_\psi)\). Exact matrix-unit arithmetic gives

\[
\operatorname{Tr}(QB)=\operatorname{Tr}(Q'A)=2/27.
\]

The stale-projector expression is instead

\[
\operatorname{Tr}(QA)=1/27.
\]

Omitting the transpose gives

\[
\operatorname{Tr}(Q\,UAU)=8/81,
\]

rather than \(2/27=6/81\). These controls test the actual transport identity; merely checking the final majorization bound would not necessarily detect these mistakes.

## 4. Controls and their intended rejection invariants

The supplied program includes positive prerequisites and eight targeted mutations:

| Mutation | Prerequisite | Intended rejection |
|---|---|---|
| Replace coherence \(t^2\) by \(t\) | Mutated matrix is a Hermitian, trace-one PSD density at physical \(t=1/3\) | `W_CHANNEL_ENTRIES` |
| Swap the spectator \(a,b\) powers | Same physical-density prerequisite | `W_CHANNEL_ENTRIES` |
| Toggle one symmetric \(J(4,2)\) edge | Same vertices; symmetric, zero-diagonal 0/1 adjacency | `JOHNSON_CHARPOLY` |
| Use \(\binom5r\) instead of \(\binom4r\) in conversion | Valid degree-at-most-four input polynomials | `BERNSTEIN_ROUNDTRIP` |
| Exchange first and last reference positions | Exactly the same reference eigenvalue multiset | `REFERENCE_ORDER` |
| Omit full transpose in reflection | Valid complex physical density and projector; wrong reflected matrix remains a density | `SPIN_TRANSPOSE` |
| Replace full transpose by one-site partial transpose | At \(t=1/3\), the resulting matrix is also checked PSD | `SPIN_TRANSPOSE` |
| Reuse stale \(Q\) | Both \(Q\) and correctly transported \(Q'\) are rank-one orthogonal projectors | `PROJECTOR_TRANSPORT` |

The two polynomial channel mutations are not rejected merely because they produce an invalid density: at the selected physical point they remain positive. For example, in units of \(1/324\), the unaltered diagonal values are \(32,28,20,13,8\). The \(t\)-coherence mutation has \(g_1,g_2,g_3=12,6,3\), and the spectator mutation has \(1,2,4\); their Johnson-block eigenvalues remain positive.

For the partial-transpose control, \(D_{1/3}\) is the average of measurement-and-preparation channels in the three Pauli bases. Its fourfold output is fully separable, so a one-site partial transpose remains PSD. The program nevertheless checks this prerequisite directly with exact arithmetic.

The control harness counts only the named invariant rejection. An unrelated exception, failed prerequisite, or elapsed-time exception cannot be counted as a successful mutation rejection.

## 5. State-class and priority ceiling

Local-unitary covariance proves the same bound for each physical local-unitary image of W4. Linearity of each fixed-projector expectation then proves it for their finite convex mixtures. Combining with an already valid Class A/B bound uses the same reference, not a common basis or projector.

The product-ray separation argument stated in S1 is sound for the stated A/B support descriptions: the W pair support has determinant \(-y^2\) and exactly one product ray, whereas the described rank-two A/B supports contain two independent product rays. This property survives local product unitaries and applies to all three pairings. A positive decomposition of a rank-one density can contain only parallel pure components, giving the claimed convex-hull separation. I did not import or re-audit the linked earlier Class A/B disposition.

This establishes neither unequal-amplitude W states nor arbitrary four-qubit inputs. No primary-literature search or priority certificate was performed in this FINITE duty. The source/novelty ceiling remains unchanged.

## 6. Full independent executable — NOT RUN

Main may materialize the following source as `finite-independent-v1.py`, pin its exact bytes, and run it once.

**Argv, NOT RUN:** `python3 -B finite-independent-v1.py`

The program uses only the standard library, no explicit file access, network, children, installations, or writes. It constructs the actual matrix-unit channel independently of the pattern formula, computes exact characteristic polynomials, derives the coefficient certificate without embedding the author’s gap table, and uses exact Gaussian rationals for the complex controls. A cooperative 54-second guard raises an exception without a success verdict.

BEGIN SOURCE: finite-independent-v1.py
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
END SOURCE

## Review disposition

**Findings:** none. Scientific F/M/m: **0/0/0**. No patch-anchored mathematical defect was established.

**Execution status:** NOT RUN. Main must materialize and hash the supplied source and obtain its actual execution result before recording the independent executable gate as passed. No parent or author computation is substituted for that missing receipt.

**overall_correctness:** correct

**explanation:** The independently reconstructed physical blocks, Johnson spectra, power expansions, and all 85 coefficientwise prefix gaps support the candidate at its exact W4-orbit convex-hull scope, including the physical negative branch and complex projector transport. The executable remains unexecuted, and this return neither supplies the separate public-source gate nor authorizes parent adoption.

**confidence:** 0.91