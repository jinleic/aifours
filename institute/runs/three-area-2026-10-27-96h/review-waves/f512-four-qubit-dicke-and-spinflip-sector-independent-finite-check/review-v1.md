# F512 FINITE — complete return

**Status: WRITTEN RECONSTRUCTION COMPLETE; INDEPENDENT FINITE EXECUTION NOT RUN.**

This is the complete body for parent materialization as `author-candidate-v1.md`. No repository or scratch file was written. The higher-priority read-only review role permits inspection but prohibits scientific execution; I did not attempt an execution or a write bypass. The complete executable source and exact argv are supplied below.

## 1. Input binding and chronology

I completely read:

- `manifest-v1.json`, including its FINITE assignment and all 110 lines.
- `freeze-receipt-v1.json`, through line 47.
- The dispatch receipt and complete parent metadata supply.
- Every listed status/permission control, through its ending.
- After a **direct pre-body acknowledgment delivered to Main**, the entire literal packet in ordered, exact raw chunks of at most 20 lines: 1–20 through 541–560, then 561–564.

This included the ending of S1 at logical source line 523 and the ending of S2 at source line 39.

Pins supplied by the parent:

- Manifest: `ed8e0ba32f83476c0a98b694d2b2d5075520fada9236e077d2d8d097599931ab`
- Receipt: `0f7c0e0ac7d983f9bffdce0b6907a107ae174d500ee29c003b7923382138a1f3`
- Packet: `2e71ba4fd85f30c704d7b7de6d79bf11022a70e607d5545143552975d0e8f191`

These are **parent-attributed metadata**, not independently computed child hashes. No native clock was executed.

The historical held episodes and all their consumers remained NONINPUT; only their status controls were read. F481/F483’s local-only acknowledgment qualification and F480’s transcript-only transport qualification are retained. No direct delivery is retrospectively attributed to those authors, and no automatic mathematical invalidity is inferred from the transport defect.

A read-only `git diff` restricted to the two frozen input paths returned no output. No patch-anchored defect is reported.

## 2. Written reconstruction

### 2.1 Actual Dicke marginals and ranks

For the six weight-two strings, the Dicke density has entries \(1/6\); all other entries vanish. Thus no executable representation of \(1/\sqrt6\) is necessary.

Every pair marginal is
\[
P=
\begin{pmatrix}
1/6&0&0&0\\
0&1/3&1/3&0\\
0&1/3&1/3&0\\
0&0&0&1/6
\end{pmatrix},
\]
with spectrum
\[
(2/3,1/6,1/6,0).
\]
Consequently its exact rank is **3**, not 2, and its determinant is zero.

Every triple marginal has entries \(1/6\) within the weight-one block and within the weight-two block, and zero elsewhere. Its spectrum is
\[
(1/2,1/2,0^{\times6}).
\]
Every single marginal is \(I_2/2\).

Across the four singleton cuts the Schmidt rank is 2. Across the three distinct balanced cuts it is 3. Since the global density is pure, this proves genuine four-party entanglement and exclusion from the biseparable set. It does **not** show that every spin-flip-invariant density, or every mixture of Dicke-orbit states, is genuinely entangled.

### 2.2 Compatible layer identities and full characteristic polynomials

The actual six-pair and four-triple sums give
\[
H_1=2I_{16},\qquad H_2=I_{16}+H_3.
\]

Writing \(\chi_A(x)=\det(xI-A)\), the reconstructed characteristic polynomials are
\[
\begin{aligned}
\chi_{\rho_D}(x)&=(x-1)x^{15},\\
\chi_{H_1}(x)&=(x-2)^{16},\\
\chi_{H_2}(x)&=(x-3)(x-5/2)^2(x-5/3)^3(x-7/6)^6(x-1)^4,\\
\chi_{H_3}(x)&=(x-2)(x-3/2)^2(x-2/3)^3(x-1/6)^6x^4.
\end{aligned}
\]

In particular,
\[
\det H_2
=3(5/2)^2(5/3)^3(7/6)^6>0,
\qquad \det H_3=0.
\]

These multiplicities follow from the actual Hamming-weight blocks. The off-diagonal contribution is \(A_w/3\); the diagonal entries are respectively
\[
(1,3/2,5/3,3/2,1)
\quad\text{and}\quad
(0,1/2,2/3,1/2,0)
\]
for \(H_2\) and \(H_3\). This reconstructs the author’s spectra without independent marginal optimization.

### 2.3 Complete prefix tables

The following combines the invariant-sector relaxation table with the exact Dicke table. Here
\[
A_k=R_3(k)-\min(2k,8),\quad
B_k=R_2(k)-k-\min(2k,8),\quad
C_k=R_1(k)-2k.
\]

| \(k\) | \(A_k\) | \(B_k\) | \(C_k=\Delta_1(k)\) | \(6\Delta_2(k)\) | \(6\Delta_3(k)\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 3 | 2 | 18 | 12 |
| 2 | 1 | 3 | 3 | 21 | 9 |
| 3 | 0 | 3 | 4 | 24 | 6 |
| 4 | −1 | 3 | 5 | 32 | 8 |
| 5 | 0 | 5 | 6 | 40 | 10 |
| 6 | 0 | 5 | 6 | 36 | 6 |
| 7 | 0 | 5 | 6 | 35 | 5 |
| 8 | 0 | 5 | 6 | 34 | 4 |
| 9 | 0 | 5 | 6 | 33 | 3 |
| 10 | 0 | 5 | 6 | 32 | 2 |
| 11 | 0 | 5 | 6 | 31 | 1 |
| 12 | 0 | 4 | 5 | 24 | 0 |
| 13 | 0 | 3 | 4 | 18 | 0 |
| 14 | 0 | 2 | 3 | 12 | 0 |
| 15 | 0 | 1 | 2 | 6 | 0 |
| 16 | 0 | 0 | 0 | 0 | 0 |

For the Dicke state the exact output gap is
\[
t^3b\Delta_3(k)+t^2b^2\Delta_2(k)+tb^3\Delta_1(k).
\]
Every proper prefix is strictly positive for \(0<t<1\).

For the broader invariant sector the fourth-prefix relaxation is
\[
-t^3b+3t^2b^2+5tb^3
=\frac{tb}{4}(5-4t-5t^2).
\]
Its positive threshold is
\[
t_*=(\sqrt{29}-2)/5.
\]
The coefficient of \(t^3b\) at \(k=4\) is **negative**. At the permitted diagnostic \(t=4/5\), this relaxation is \(-7/250\), whereas the actual Dicke fourth-prefix gap is \(133/1250>0\). The former is a failed certificate, not a physical counterexample.

### 2.4 Selected exact physical output spectra

Multiplicities below are \(1,2,3,6,4\) whenever five values are displayed.

| Physical \(p\) | Exact decreasing Dicke output spectrum |
|---|---|
| \(0\) | \(1,0^{\times15}\) |
| \(1/2\) | \((49,27^{\times2},17^{\times3},11^{\times6},9^{\times4})/256\) |
| \(1\) | \((1/16)^{\times16}\) |
| \(4/3\) | \((27,21^{\times2},16^{\times3},13^{\times6},12^{\times4})/243\) |

The associated full characteristic polynomial is the product of \(x-\lambda\) over these displayed values and multiplicities.

All sixteen output-prefix gaps are zero at \(p=0,1\). For \(p=1/2\), their numerators over 256 are
\[
(32,32,32,42,52,44,42,40,38,36,34,26,20,14,8,0).
\]
For \(p=4/3\), their numerators over 243 are
\[
(21,24,27,35,43,39,38,37,36,35,34,27,21,15,9,0).
\]

These are written exact calculations, **not machine output**.

### 2.5 A complex fixed projector that detects an omitted transpose

Let
\[
u=(|0000\rangle+i|0011\rangle)/\sqrt2,\qquad
Q=|u\rangle\langle u|+|0101\rangle\langle0101|
  +|1010\rangle\langle1010|.
\]
This is an exact complex rank-three orthogonal projector.

For the Dicke input,
\[
\operatorname{Tr}(Q\rho_D)=5/12.
\]
At \(p=4/3\),
\[
\operatorname{Tr}(Q\Phi_{4/3}^{\otimes4}(\rho_D))=7/36,
\quad
K_3(\Phi_{4/3}^{\otimes4}(\rho_D))=23/81,
\quad K_3(D_{1/3})=32/81.
\]

To make the missing-transpose mutation observable, use the actual mixed invariant density
\[
\rho_C=\tfrac12\bigl(|u\rangle\langle u|
+\widetilde{|u\rangle\langle u|}\bigr).
\]
For the negative branch \(p=4/3\), transported from \(p=2/3\),
\[
Q'=W_4Q^TW_4
\]
gives the correct expectation \(31/162\). Replacing it with \(W_4QW_4\) gives \(13/81\); the discrepancy is exactly \(5/162\).

Thus the intended mutation is rejected because of **transport mismatch**, not because the mutated matrix ceases to be a projector. Both matrices remain valid rank-three projectors.

## 3. Scope and limitations

No evidence-backed mathematical defect was found in the reconstructed Dicke spectra, invariant-sector identities, prefix tables, or full-transpose transport.

This return does not independently certify the older Class A/B or symmetric-W hull definitions: their underlying bodies are not additional F512 inputs. The biseparable exclusion is independently reconstructed directly from the Dicke marginals.

The supplied executable independently constructs five physical invariant densities, including spin averages of deterministic full complex seeds, and compares physical Pauli and erasure constructions. It is designed to perform:

- 20 scoped physical output cases.
- 64 exact Dicke output-prefix comparisons.
- 320 numerical output-prefix comparisons.
- 22 exact characteristic-polynomial comparisons.
- Exact complex-projector and negative-branch transport checks.
- Eleven intended-reason mutation rejections.

**None of these execution counts is an observed run result.** No elapsed runtime, numerical residual, mutation PASS, or finite PASS is claimed.

The numerical path uses a standard-library real-symmetric Jacobi eigensolver on the \(32\times32\) realification. It explicitly checks eigenpair residuals, orthogonality and duplicated eigenvalues. Prefix tolerance is \(2\cdot10^{-9}\); eigenpair residual tolerance is \(10^{-10}\). Exact claims use Gaussian-rational arithmetic, not these tolerances.

## 4. Complete executable source — NOT RUN

Proposed materialization path:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f512-four-qubit-dicke-and-spinflip-sector-independent-finite-check/independent-four-qubit-dicke-spinflip-finite-v1.py`

Exact argv after materialization:

`python3 -B /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f512-four-qubit-dicke-and-spinflip-sector-independent-finite-check/independent-four-qubit-dicke-spinflip-finite-v1.py --seconds 55`

The source performs no file, network, child-process or installation operations. Its deadline is cooperative and fixed at 55 seconds; expiration is a non-success result. Actual runtime is unmeasured.

For literal materialization, retain the characters after the leading `PY|` on every following source line, join them with LF, and retain a final LF. There are no omitted source sections.

PY|from fractions import Fraction as F
PY|from itertools import combinations
PY|import math
PY|import sys
PY|import time
PY|
PY|START = time.monotonic()
PY|DEADLINE = START + 55.0
PY|PREFIX_TOL = 2e-9
PY|RESIDUAL_TOL = 1e-10
PY|PAIR_TOL = 1e-9
PY|POLY_CHECKS = 0
PY|MUTATIONS = 0
PY|
PY|class Failure(Exception):
PY|    def __init__(self, reason):
PY|        self.reason = reason
PY|        super().__init__(reason)
PY|
PY|def must(condition, reason):
PY|    if not condition:
PY|        raise Failure(reason)
PY|
PY|def tick():
PY|    if time.monotonic() >= DEADLINE:
PY|        raise Failure("DEADLINE_INCOMPLETE")
PY|
PY|class G:
PY|    __slots__ = ("r", "i")
PY|
PY|    def __init__(self, r=0, i=0):
PY|        self.r = F(r)
PY|        self.i = F(i)
PY|
PY|    def __add__(self, other):
PY|        other = cg(other)
PY|        return G(self.r + other.r, self.i + other.i)
PY|
PY|    __radd__ = __add__
PY|
PY|    def __neg__(self):
PY|        return G(-self.r, -self.i)
PY|
PY|    def __sub__(self, other):
PY|        return self + (-cg(other))
PY|
PY|    def __rsub__(self, other):
PY|        return cg(other) - self
PY|
PY|    def __mul__(self, other):
PY|        other = cg(other)
PY|        return G(self.r * other.r - self.i * other.i,
PY|                 self.r * other.i + self.i * other.r)
PY|
PY|    __rmul__ = __mul__
PY|
PY|    def __truediv__(self, other):
PY|        other = cg(other)
PY|        d = other.r * other.r + other.i * other.i
PY|        must(d != 0, "ZERO_DIVISOR")
PY|        return G((self.r * other.r + self.i * other.i) / d,
PY|                 (self.i * other.r - self.r * other.i) / d)
PY|
PY|    def __eq__(self, other):
PY|        other = cg(other)
PY|        return self.r == other.r and self.i == other.i
PY|
PY|    def __bool__(self):
PY|        return bool(self.r or self.i)
PY|
PY|    def conj(self):
PY|        return G(self.r, -self.i)
PY|
PY|    def __repr__(self):
PY|        if not self.i:
PY|            return str(self.r)
PY|        return "(" + str(self.r) + "," + str(self.i) + "i)"
PY|
PY|def cg(x):
PY|    return x if isinstance(x, G) else G(x)
PY|
PY|Z = G()
PY|ONE = G(1)
PY|II = G(0, 1)
PY|
PY|def weight(x):
PY|    return bin(x).count("1")
PY|
PY|def zero(n):
PY|    return [[Z for _ in range(n)] for _ in range(n)]
PY|
PY|def eye(n):
PY|    a = zero(n)
PY|    for i in range(n):
PY|        a[i][i] = ONE
PY|    return a
PY|
PY|def copy_m(a):
PY|    return [row[:] for row in a]
PY|
PY|def add(a, b):
PY|    return [[x + y for x, y in zip(ar, br)]
PY|            for ar, br in zip(a, b)]
PY|
PY|def scale(s, a):
PY|    s = cg(s)
PY|    return [[s * x for x in row] for row in a]
PY|
PY|def adjoint(a):
PY|    n = len(a)
PY|    return [[a[j][i].conj() for j in range(n)] for i in range(n)]
PY|
PY|def mm(a, b):
PY|    n = len(a)
PY|    c = zero(n)
PY|    for i in range(n):
PY|        tick()
PY|        for k in range(n):
PY|            x = a[i][k]
PY|            if x:
PY|                for j in range(n):
PY|                    if b[k][j]:
PY|                        c[i][j] = c[i][j] + x * b[k][j]
PY|    return c
PY|
PY|def tr(a):
PY|    return sum((a[i][i] for i in range(len(a))), Z)
PY|
PY|def expectation(q, a):
PY|    n = len(a)
PY|    return sum((q[i][j] * a[j][i]
PY|                for i in range(n) for j in range(n)
PY|                if q[i][j] and a[j][i]), Z)
PY|
PY|def density(v):
PY|    v = [cg(x) for x in v]
PY|    norm = sum((x.r * x.r + x.i * x.i for x in v), F(0))
PY|    must(norm > 0, "ZERO_SEED")
PY|    return [[x * y.conj() / norm for y in v] for x in v]
PY|
PY|def basis_projector(i, n=16):
PY|    a = zero(n)
PY|    a[i][i] = ONE
PY|    return a
PY|
PY|def check_density(a):
PY|    must(a == adjoint(a), "DENSITY_HERMITICITY")
PY|    must(tr(a) == ONE, "DENSITY_TRACE")
PY|
PY|def check_projector(q, rank):
PY|    must(q == adjoint(q), "PROJECTOR_HERMITICITY")
PY|    must(mm(q, q) == q, "PROJECTOR_IDEMPOTENCE")
PY|    must(tr(q) == G(rank), "PROJECTOR_RANK")
PY|
PY|def project_bits(x, positions):
PY|    y = 0
PY|    for site in positions:
PY|        y = (y << 1) | ((x >> (3 - site)) & 1)
PY|    return y
PY|
PY|def partial(a, positions):
PY|    positions = tuple(positions)
PY|    env = tuple(i for i in range(4) if i not in positions)
PY|    local = [project_bits(i, positions) for i in range(16)]
PY|    outside = [project_bits(i, env) for i in range(16)]
PY|    out = zero(1 << len(positions))
PY|    for i in range(16):
PY|        tick()
PY|        for j in range(16):
PY|            if outside[i] == outside[j] and a[i][j]:
PY|                x, y = local[i], local[j]
PY|                out[x][y] = out[x][y] + a[i][j]
PY|    return out
PY|
PY|def lift(a, positions):
PY|    positions = tuple(positions)
PY|    env = tuple(i for i in range(4) if i not in positions)
PY|    local = [project_bits(i, positions) for i in range(16)]
PY|    outside = [project_bits(i, env) for i in range(16)]
PY|    out = zero(16)
PY|    for i in range(16):
PY|        tick()
PY|        for j in range(16):
PY|            if outside[i] == outside[j]:
PY|                out[i][j] = a[local[i]][local[j]]
PY|    return out
PY|
PY|def layers(a):
PY|    h = [eye(16), zero(16), zero(16), zero(16), copy_m(a)]
PY|    for size in (1, 2, 3):
PY|        for positions in combinations(range(4), size):
PY|            h[size] = add(h[size], lift(partial(a, positions), positions))
PY|    return h
PY|
PY|def spin(a):
PY|    out = zero(16)
PY|    for i in range(16):
PY|        for j in range(16):
PY|            sign = -1 if (weight(i) + weight(j)) % 2 else 1
PY|            out[15 - j][15 - i] = sign * a[i][j]
PY|    return out
PY|
PY|def w_conjugate_without_transpose(a):
PY|    out = zero(16)
PY|    for i in range(16):
PY|        for j in range(16):
PY|            sign = -1 if (weight(i) + weight(j)) % 2 else 1
PY|            out[15 - i][15 - j] = sign * a[i][j]
PY|    return out
PY|
PY|def spin_average(a):
PY|    return scale(F(1, 2), add(a, spin(a)))
PY|
PY|def pauli_action(kind, x, site):
PY|    mask = 1 << (3 - site)
PY|    bit = bool(x & mask)
PY|    if kind == 0:
PY|        return x, ONE
PY|    if kind == 1:
PY|        return x ^ mask, ONE
PY|    if kind == 2:
PY|        return x ^ mask, -II if bit else II
PY|    return x, G(-1 if bit else 1)
PY|
PY|def pauli_channel(a, p):
PY|    p = F(p)
PY|    must(0 <= p <= F(4, 3), "UNPHYSICAL_PAULI_PARAMETER")
PY|    probabilities = [1 - 3 * p / 4, p / 4, p / 4, p / 4]
PY|    must(all(x >= 0 for x in probabilities), "NEGATIVE_PAULI_WEIGHT")
PY|    out = copy_m(a)
PY|    for site in range(4):
PY|        nxt = zero(16)
PY|        for kind, probability in enumerate(probabilities):
PY|            tick()
PY|            if not probability:
PY|                continue
PY|            mapping = [pauli_action(kind, i, site) for i in range(16)]
PY|            for i in range(16):
PY|                di, pi = mapping[i]
PY|                for j in range(16):
PY|                    if out[i][j]:
PY|                        dj, pj = mapping[j]
PY|                        value = probability * pi * out[i][j] * pj.conj()
PY|                        nxt[di][dj] = nxt[di][dj] + value
PY|        out = nxt
PY|    return out
PY|
PY|def erasure_channel(h, p):
PY|    p = F(p)
PY|    retained, noise = 1 - p, p / 2
PY|    out = zero(16)
PY|    for j in range(5):
PY|        out = add(out, scale(retained ** j * noise ** (4 - j), h[j]))
PY|    return out
PY|
PY|def real_matrix(a):
PY|    must(all(not z.i for row in a for z in row), "EXPECTED_REAL_MATRIX")
PY|    return [[z.r for z in row] for row in a]
PY|
PY|def charpoly(a):
PY|    r = real_matrix(a)
PY|    n = len(r)
PY|    b = [[F(i == j) for j in range(n)] for i in range(n)]
PY|    coefficients = [F(1)]
PY|    for degree in range(1, n + 1):
PY|        c = [[F(0) for _ in range(n)] for _ in range(n)]
PY|        for i in range(n):
PY|            tick()
PY|            for k in range(n):
PY|                if r[i][k]:
PY|                    for j in range(n):
PY|                        if b[k][j]:
PY|                            c[i][j] += r[i][k] * b[k][j]
PY|        coefficient = -sum((c[i][i] for i in range(n)), F(0)) / degree
PY|        coefficients.append(coefficient)
PY|        for i in range(n):
PY|            c[i][i] += coefficient
PY|        b = c
PY|    must(all(not x for row in b for x in row), "CAYLEY_HAMILTON")
PY|    return coefficients
PY|
PY|def root_polynomial(roots):
PY|    coefficients = [F(1)]
PY|    for root in roots:
PY|        out = [F(0)] * (len(coefficients) + 1)
PY|        for i, value in enumerate(coefficients):
PY|            out[i] += value
PY|            out[i + 1] -= root * value
PY|        coefficients = out
PY|    return coefficients
PY|
PY|def check_roots(a, roots, reason):
PY|    global POLY_CHECKS
PY|    coefficients = charpoly(a)
PY|    must(coefficients == root_polynomial(roots), reason)
PY|    POLY_CHECKS += 1
PY|    return coefficients
PY|
PY|def determinant(a):
PY|    r = real_matrix(a)
PY|    n = len(r)
PY|    result = F(1)
PY|    for k in range(n):
PY|        tick()
PY|        pivot = next((i for i in range(k, n) if r[i][k]), None)
PY|        if pivot is None:
PY|            return F(0)
PY|        if pivot != k:
PY|            r[k], r[pivot] = r[pivot], r[k]
PY|            result = -result
PY|        value = r[k][k]
PY|        result *= value
PY|        for i in range(k + 1, n):
PY|            if r[i][k]:
PY|                factor = r[i][k] / value
PY|                for j in range(k + 1, n):
PY|                    r[i][j] -= factor * r[k][j]
PY|                r[i][k] = F(0)
PY|    return result
PY|
PY|def rank_real(a):
PY|    r = real_matrix(a)
PY|    n = len(r)
PY|    row = 0
PY|    for column in range(n):
PY|        tick()
PY|        pivot = next((i for i in range(row, n) if r[i][column]), None)
PY|        if pivot is None:
PY|            continue
PY|        r[row], r[pivot] = r[pivot], r[row]
PY|        value = r[row][column]
PY|        for i in range(row + 1, n):
PY|            if r[i][column]:
PY|                factor = r[i][column] / value
PY|                for j in range(column + 1, n):
PY|                    r[i][j] -= factor * r[row][j]
PY|                r[i][column] = F(0)
PY|        row += 1
PY|        if row == n:
PY|            break
PY|    return row
PY|
PY|def prefixes(values):
PY|    total = F(0)
PY|    out = []
PY|    for value in values:
PY|        total += value
PY|        out.append(total)
PY|    return out
PY|
PY|def reference_layer(j):
PY|    a = zero(16)
PY|    for i in range(16):
PY|        zeros = 4 - weight(i)
PY|        a[i][i] = G(math.comb(zeros, j) if zeros >= j else 0)
PY|    return a
PY|
PY|def reference_roots(j):
PY|    a = reference_layer(j)
PY|    return sorted((a[i][i].r for i in range(16)), reverse=True)
PY|
PY|def reference_output_roots(t):
PY|    a, b = (1 + t) / 2, (1 - t) / 2
PY|    return [a ** (4 - w) * b ** w
PY|            for w in range(5) for _ in range(math.comb(4, w))]
PY|
PY|def dicke_output_roots(t):
PY|    b = (1 - t) / 2
PY|    rows = [(1, F(2), F(3), 1),
PY|            (0, F(3, 2), F(5, 2), 2),
PY|            (0, F(2, 3), F(5, 3), 3),
PY|            (0, F(1, 6), F(7, 6), 6),
PY|            (0, F(0), F(1), 4)]
PY|    out = []
PY|    for rho, h3, h2, multiplicity in rows:
PY|        value = t ** 4 * rho + t ** 3 * b * h3
PY|        value += t ** 2 * b ** 2 * h2 + 2 * t * b ** 3 + b ** 4
PY|        out.extend([value] * multiplicity)
PY|    must(out == sorted(out, reverse=True), "DICKE_OUTPUT_ORDER")
PY|    return out
PY|
PY|def numeric_eigenvalues(a):
PY|    n = len(a)
PY|    size = 2 * n
PY|    original = [[0.0] * size for _ in range(size)]
PY|    for i in range(n):
PY|        for j in range(n):
PY|            x, y = float(a[i][j].r), float(a[i][j].i)
PY|            original[i][j] = x
PY|            original[i][j + n] = -y
PY|            original[i + n][j] = y
PY|            original[i + n][j + n] = x
PY|    must(max(abs(original[i][j] - original[j][i])
PY|             for i in range(size) for j in range(size)) <= 1e-14,
PY|         "REALIFICATION_SYMMETRY")
PY|    r = [row[:] for row in original]
PY|    vectors = [[float(i == j) for j in range(size)] for i in range(size)]
PY|    converged = False
PY|    for _ in range(80):
PY|        tick()
PY|        off = max(abs(r[i][j]) for i in range(size) for j in range(i + 1, size))
PY|        if off <= 1e-14:
PY|            converged = True
PY|            break
PY|        for p in range(size):
PY|            tick()
PY|            for q in range(p + 1, size):
PY|                apq = r[p][q]
PY|                if abs(apq) <= 1e-16:
PY|                    continue
PY|                app, aqq = r[p][p], r[q][q]
PY|                tau = (aqq - app) / (2.0 * apq)
PY|                tangent = math.copysign(1.0, tau) / (
PY|                    abs(tau) + math.hypot(1.0, tau))
PY|                cosine = 1.0 / math.sqrt(1.0 + tangent * tangent)
PY|                sine = tangent * cosine
PY|                r[p][p] = app - tangent * apq
PY|                r[q][q] = aqq + tangent * apq
PY|                r[p][q] = r[q][p] = 0.0
PY|                for k in range(size):
PY|                    if k != p and k != q:
PY|                        x, y = r[k][p], r[k][q]
PY|                        r[k][p] = r[p][k] = cosine * x - sine * y
PY|                        r[k][q] = r[q][k] = sine * x + cosine * y
PY|                    x, y = vectors[k][p], vectors[k][q]
PY|                    vectors[k][p] = cosine * x - sine * y
PY|                    vectors[k][q] = sine * x + cosine * y
PY|    must(converged, "JACOBI_CONVERGENCE")
PY|    eigenvalues = [r[i][i] for i in range(size)]
PY|    must(all(math.isfinite(x) for x in eigenvalues), "NONFINITE_EIGENVALUE")
PY|    residual = 0.0
PY|    for k in range(size):
PY|        tick()
PY|        square = 0.0
PY|        for i in range(size):
PY|            error = sum(original[i][j] * vectors[j][k] for j in range(size))
PY|            error -= eigenvalues[k] * vectors[i][k]
PY|            square += error * error
PY|        residual = max(residual, math.sqrt(square))
PY|    orthogonality = max(
PY|        abs(sum(vectors[k][i] * vectors[k][j] for k in range(size))
PY|            - float(i == j))
PY|        for i in range(size) for j in range(size))
PY|    must(residual <= RESIDUAL_TOL, "EIGENPAIR_RESIDUAL")
PY|    must(orthogonality <= 1e-10, "EIGENVECTOR_ORTHOGONALITY")
PY|    eigenvalues.sort(reverse=True)
PY|    pair_gap = max(abs(eigenvalues[2 * i] - eigenvalues[2 * i + 1])
PY|                   for i in range(n))
PY|    must(pair_gap <= PAIR_TOL, "REALIFICATION_MULTIPLICITY")
PY|    values = [(eigenvalues[2 * i] + eigenvalues[2 * i + 1]) / 2
PY|              for i in range(n)]
PY|    return values, residual, pair_gap
PY|
PY|def assert_genuine_pure(a):
PY|    must(expectation(a, a) == ONE, "PURE_SCHMIDT_PRECONDITION")
PY|    cuts = [(0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3)]
PY|    for cut in cuts:
PY|        must(rank_real(partial(a, cut)) > 1, "GME_PRODUCT_CUT")
PY|
PY|def reject(name, reason, operation):
PY|    global MUTATIONS
PY|    try:
PY|        operation()
PY|    except Failure as error:
PY|        must(error.reason == reason, "WRONG_MUTATION_REASON:" + name)
PY|    else:
PY|        raise Failure("MUTATION_NOT_REJECTED:" + name)
PY|    MUTATIONS += 1
PY|    print("INTENDED_REJECTION", name, reason)
PY|
PY|def run():
PY|    must(sys.argv[1:] == ["--seconds", "55"], "ARGV_REQUIRES_SECONDS_55")
PY|    tick()
PY|    identity = eye(16)
PY|    maximally_mixed = scale(F(1, 16), identity)
PY|    product = basis_projector(0)
PY|    dicke = density([ONE if weight(i) == 2 else Z for i in range(16)])
PY|    hd = layers(dicke)
PY|    reference = layers(product)
PY|    for j in range(5):
PY|        must(reference[j] == reference_layer(j), "REFERENCE_H" + str(j))
PY|
PY|    pair = zero(4)
PY|    pair[0][0] = pair[3][3] = G(F(1, 6))
PY|    pair[1][1] = pair[2][2] = G(F(1, 3))
PY|    pair[1][2] = pair[2][1] = G(F(1, 3))
PY|    triple = zero(8)
PY|    for i in range(8):
PY|        for j in range(8):
PY|            if weight(i) == weight(j) and weight(i) in (1, 2):
PY|                triple[i][j] = G(F(1, 6))
PY|    for cut in combinations(range(4), 1):
PY|        marginal = partial(dicke, cut)
PY|        must(marginal == scale(F(1, 2), eye(2)), "DICKE_SINGLE")
PY|        check_roots(marginal, [F(1, 2)] * 2, "DICKE_SINGLE_POLYNOMIAL")
PY|    for cut in combinations(range(4), 2):
PY|        marginal = partial(dicke, cut)
PY|        must(marginal == pair, "PARTIAL_TRACE")
PY|        must(rank_real(marginal) == 3 and determinant(marginal) == 0,
PY|             "DICKE_PAIR_RANK")
PY|        check_roots(marginal, [F(2, 3), F(1, 6), F(1, 6), F(0)],
PY|                    "DICKE_PAIR_POLYNOMIAL")
PY|    for cut in combinations(range(4), 3):
PY|        marginal = partial(dicke, cut)
PY|        must(marginal == triple, "DICKE_TRIPLE")
PY|        check_roots(marginal, [F(1, 2)] * 2 + [F(0)] * 6,
PY|                    "DICKE_TRIPLE_POLYNOMIAL")
PY|
PY|    diagonal2 = [F(1), F(3, 2), F(5, 3), F(3, 2), F(1)]
PY|    diagonal3 = [F(0), F(1, 2), F(2, 3), F(1, 2), F(0)]
PY|    for j, diagonal in [(2, diagonal2), (3, diagonal3)]:
PY|        expected = zero(16)
PY|        for x in range(16):
PY|            for y in range(16):
PY|                if x == y:
PY|                    expected[x][y] = G(diagonal[weight(x)])
PY|                elif weight(x) == weight(y) and weight(x ^ y) == 2:
PY|                    expected[x][y] = G(F(1, 3))
PY|        must(hd[j] == expected, "DICKE_ACTUAL_BLOCK_H" + str(j))
PY|
PY|    spec2 = ([F(3)] + [F(5, 2)] * 2 + [F(5, 3)] * 3
PY|             + [F(7, 6)] * 6 + [F(1)] * 4)
PY|    spec3 = ([F(2)] + [F(3, 2)] * 2 + [F(2, 3)] * 3
PY|             + [F(1, 6)] * 6 + [F(0)] * 4)
PY|    check_roots(dicke, [F(1)] + [F(0)] * 15, "DICKE_DENSITY_POLYNOMIAL")
PY|    check_roots(hd[1], [F(2)] * 16, "DICKE_H1_POLYNOMIAL")
PY|    cp2 = check_roots(hd[2], spec2, "DICKE_H2_POLYNOMIAL")
PY|    check_roots(hd[3], spec3, "DICKE_H3_POLYNOMIAL")
PY|    det2 = determinant(hd[2])
PY|    product2 = F(1)
PY|    for value in spec2:
PY|        product2 *= value
PY|    must(det2 == product2 and cp2[-1] == det2, "DETERMINANT_CONSTANT")
PY|    assert_genuine_pure(dicke)
PY|
PY|    r1 = prefixes(reference_roots(1))
PY|    r2 = prefixes(reference_roots(2))
PY|    r3 = prefixes(reference_roots(3))
PY|    s2, s3 = prefixes(spec2), prefixes(spec3)
PY|    delta1 = [r1[k - 1] - 2 * k for k in range(1, 17)]
PY|    delta2 = [r2[k] - s2[k] for k in range(16)]
PY|    delta3 = [r3[k] - s3[k] for k in range(16)]
PY|    sector = [(r3[k - 1] - min(2 * k, 8),
PY|               r2[k - 1] - k - min(2 * k, 8),
PY|               r1[k - 1] - 2 * k) for k in range(1, 17)]
PY|    expected_sector = [
PY|        (2,3,2), (1,3,3), (0,3,4), (-1,3,5),
PY|        (0,5,6), (0,5,6), (0,5,6), (0,5,6),
PY|        (0,5,6), (0,5,6), (0,5,6), (0,4,5),
PY|        (0,3,4), (0,2,3), (0,1,2), (0,0,0)]
PY|    expected_dicke = [
PY|        (2,18,12), (3,21,9), (4,24,6), (5,32,8),
PY|        (6,40,10), (6,36,6), (6,35,5), (6,34,4),
PY|        (6,33,3), (6,32,2), (6,31,1), (5,24,0),
PY|        (4,18,0), (3,12,0), (2,6,0), (0,0,0)]
PY|    must(sector == expected_sector, "SECTOR_PREFIX_TABLE")
PY|    actual_dicke = [(delta1[k], 6 * delta2[k], 6 * delta3[k])
PY|                    for k in range(16)]
PY|    must(actual_dicke == expected_dicke, "DICKE_PREFIX_TABLE")
PY|    for k in range(16):
PY|        print("EXACT_LAYER_GAP", k + 1, sector[k], actual_dicke[k])
PY|
PY|    def sector_deficit(t):
PY|        b = (1 - t) / 2
PY|        value = -t ** 3 * b + 3 * t ** 2 * b ** 2 + 5 * t * b ** 3
PY|        factored = t * b * (5 - 4 * t - 5 * t ** 2) / 4
PY|        must(value == factored, "K4_FACTORIZATION")
PY|        return value
PY|
PY|    must(4 * 4 - 4 * 5 * (-5) == 4 * 29, "K4_ROOT_DISCRIMINANT")
PY|    must(sector_deficit(F(4, 5)) == F(-7, 250), "K4_HIGH_T_DEFICIT")
PY|    t, b = F(4, 5), F(1, 10)
PY|    dicke_k4 = t ** 3 * b * delta3[3] + t ** 2 * b ** 2 * delta2[3]
PY|    dicke_k4 += t * b ** 3 * delta1[3]
PY|    must(dicke_k4 == F(133, 1250), "DICKE_K4_NOT_A_COUNTEREXAMPLE")
PY|
PY|    u = [Z] * 16
PY|    u[0], u[3] = ONE, II
PY|    pure_u = density(u)
PY|    complex_invariant = spin_average(pure_u)
PY|    q = add(add(pure_u, basis_projector(5)), basis_projector(10))
PY|    qp = spin(q)
PY|    wrong_qp = w_conjugate_without_transpose(q)
PY|    for candidate in (q, qp, wrong_qp):
PY|        check_projector(candidate, 3)
PY|    must(expectation(q, dicke) == G(F(5, 12)), "FIXED_Q_DICKE_INPUT")
PY|
PY|    seed1 = density([G((i % 5) - 2, ((3 * i + 1) % 7) - 3)
PY|                     for i in range(16)])
PY|    seed2 = density([G(((i * i + 2) % 7) - 3, ((5 * i + 2) % 9) - 4)
PY|                     for i in range(16)])
PY|    mixed_seed = scale(F(1, 4),
PY|                       add(add(scale(2, seed1), seed2), maximally_mixed))
PY|    states = [
PY|        ("Dicke", dicke),
PY|        ("ComplexInvariant", complex_invariant),
PY|        ("DenseSpinAverage", spin_average(seed1)),
PY|        ("MixedSpinAverage", spin_average(mixed_seed)),
PY|        ("MaxMixed", maximally_mixed)]
PY|    parameters = [F(0), F(1, 2), F(1), F(4, 3)]
PY|    exact_spectra = {
PY|        F(0): [F(1)] + [F(0)] * 15,
PY|        F(1, 2): ([F(49, 256)] + [F(27, 256)] * 2
PY|                    + [F(17, 256)] * 3 + [F(11, 256)] * 6
PY|                    + [F(9, 256)] * 4),
PY|        F(1): [F(1, 16)] * 16,
PY|        F(4, 3): ([F(27, 243)] + [F(21, 243)] * 2
PY|                    + [F(16, 243)] * 3 + [F(13, 243)] * 6
PY|                    + [F(12, 243)] * 4)}
PY|    gap_numerators = {
PY|        F(1, 2): [32,32,32,42,52,44,42,40,38,36,34,26,20,14,8,0],
PY|        F(4, 3): [21,24,27,35,43,39,38,37,36,35,34,27,21,15,9,0]}
PY|    channel_cases = 0
PY|    exact_prefixes = 0
PY|    numeric_prefixes = 0
PY|    maximum_residual = 0.0
PY|    maximum_pair_gap = 0.0
PY|    dicke_negative_output = None
PY|    for name, rho in states:
PY|        tick()
PY|        check_density(rho)
PY|        must(spin(rho) == rho, "SPIN_INVARIANCE")
PY|        h = hd if name == "Dicke" else layers(rho)
PY|        must(h[1] == scale(2, identity), "INVARIANT_H1")
PY|        must(h[2] == add(identity, h[3]), "INVARIANT_H2_H3")
PY|        must([tr(h[j]) for j in (1, 2, 3)] == [G(32), G(24), G(8)],
PY|             "ACTUAL_LAYER_TRACES")
PY|        for p in parameters:
PY|            tick()
PY|            output = pauli_channel(rho, p)
PY|            must(output == erasure_channel(h, p), "PAULI_ERASURE_EQUALITY")
PY|            check_density(output)
PY|            must(spin(output) == output, "OUTPUT_SPIN_INVARIANCE")
PY|            if p == 1:
PY|                must(output == maximally_mixed, "EXACT_FULL_PAULI_TWIRL")
PY|            t = abs(1 - p)
PY|            reference_prefix = prefixes(reference_output_roots(t))
PY|            values, residual, pair_gap = numeric_eigenvalues(output)
PY|            maximum_residual = max(maximum_residual, residual)
PY|            maximum_pair_gap = max(maximum_pair_gap, pair_gap)
PY|            must(min(values) >= -PREFIX_TOL, "NUMERICAL_OUTPUT_PSD")
PY|            must(abs(sum(values) - 1.0) <= PREFIX_TOL, "NUMERICAL_TRACE")
PY|            numerical_sum = 0.0
PY|            for k, value in enumerate(values):
PY|                numerical_sum += value
PY|                must(float(reference_prefix[k]) - numerical_sum >= -PREFIX_TOL,
PY|                     "NUMERICAL_PREFIX:" + name + ":" + str(p) + ":" + str(k + 1))
PY|                numeric_prefixes += 1
PY|            print("NUMERICAL_OUTPUT", name, "p=" + str(p),
PY|                  "eigenvalues=" + ",".join(format(x, ".17g") for x in values),
PY|                  "residual=" + format(residual, ".6g"),
PY|                  "pair_gap=" + format(pair_gap, ".6g"))
PY|            channel_cases += 1
PY|            if name == "Dicke":
PY|                roots = dicke_output_roots(t)
PY|                must(roots == exact_spectra[p], "SELECTED_EXACT_SPECTRUM")
PY|                check_roots(output, roots, "DICKE_OUTPUT_CHARACTERISTIC")
PY|                actual_prefix = prefixes(roots)
PY|                b = (1 - t) / 2
PY|                gaps = []
PY|                for k in range(16):
PY|                    gap = reference_prefix[k] - actual_prefix[k]
PY|                    expected = t ** 3 * b * delta3[k]
PY|                    expected += t ** 2 * b ** 2 * delta2[k]
PY|                    expected += t * b ** 3 * delta1[k]
PY|                    must(gap == expected and gap >= 0, "EXACT_OUTPUT_PREFIX")
PY|                    gaps.append(gap)
PY|                    exact_prefixes += 1
PY|                if p in gap_numerators:
PY|                    denominator = 256 if p == F(1, 2) else 243
PY|                    must(gaps == [F(x, denominator) for x in gap_numerators[p]],
PY|                         "SELECTED_EXACT_GAP_TABLE")
PY|                else:
PY|                    must(gaps == [F(0)] * 16, "ENDPOINT_GAP_TABLE")
PY|                print("EXACT_DICKE_OUTPUT", p, roots, "gaps", gaps)
PY|                if p == F(4, 3):
PY|                    dicke_negative_output = output
PY|
PY|    must(expectation(q, dicke_negative_output) == G(F(7, 36)),
PY|         "FIXED_Q_DICKE_OUTPUT")
PY|    minus_c = None
PY|    plus_c = None
PY|    for label, rho in [("ComplexInvariant", complex_invariant),
PY|                       ("UnaveragedDenseSeed", seed1)]:
PY|        minus = pauli_channel(rho, F(4, 3))
PY|        plus = pauli_channel(rho, F(2, 3))
PY|        must(minus == spin(plus), "PHYSICAL_NEGATIVE_BRANCH_MATRIX")
PY|        must(expectation(q, minus) == expectation(qp, plus),
PY|             "Q_TRANSPOSE")
PY|        print("EXACT_NEGATIVE_TRANSPORT", label, expectation(q, minus))
PY|        if label == "ComplexInvariant":
PY|            minus_c, plus_c = minus, plus
PY|    must(expectation(q, minus_c) == G(F(31, 162)),
PY|         "COMPLEX_Q_EXACT_EXPECTATION")
PY|    must(expectation(wrong_qp, plus_c) == G(F(13, 81)),
PY|         "OMITTED_TRANSPOSE_EXACT_EXPECTATION")
PY|    must(expectation(q, minus_c) - expectation(wrong_qp, plus_c)
PY|         == G(F(5, 162)), "OMITTED_TRANSPOSE_WITNESS")
PY|    must(expectation(maximally_mixed, maximally_mixed) == G(F(1, 16)),
PY|         "MAXMIX_PURITY")
PY|
PY|    for j in (1, 2, 3):
PY|        bad = copy_m(reference[j])
PY|        bad[0][0] = bad[0][0] + 1
PY|        reason = "REFERENCE_H" + str(j)
PY|        reject(reason, reason,
PY|               lambda bad=bad, j=j, reason=reason:
PY|               must(bad == reference_layer(j), reason))
PY|    bad_pair = copy_m(pair)
PY|    bad_pair[0][0] = bad_pair[0][0] + F(1, 6)
PY|    reject("partial_trace_entry", "PARTIAL_TRACE",
PY|           lambda: must(bad_pair == partial(dicke, (0, 1)), "PARTIAL_TRACE"))
PY|    bad_roots = spec2[:]
PY|    bad_roots[-1] = F(0)
PY|    reject("characteristic_multiplicity", "CHARACTERISTIC_MULTIPLICITY",
PY|           lambda: must(cp2 == root_polynomial(bad_roots),
PY|                        "CHARACTERISTIC_MULTIPLICITY"))
PY|    reject("determinant_constant", "DETERMINANT_CONSTANT",
PY|           lambda: must(cp2[-1] + 1 == det2, "DETERMINANT_CONSTANT"))
PY|    bad_sector = sector[:]
PY|    bad_sector[3] = (F(1), F(3), F(5))
PY|    reject("fourth_prefix_sign", "K4_SIGN",
PY|           lambda: must(bad_sector == expected_sector, "K4_SIGN"))
PY|    reject("false_all_noise_relaxation", "K4_THRESHOLD",
PY|           lambda: must(sector_deficit(F(4, 5)) >= 0, "K4_THRESHOLD"))
PY|    reject("omitted_projector_transpose", "Q_TRANSPOSE",
PY|           lambda: must(expectation(q, minus_c)
PY|                        == expectation(wrong_qp, plus_c), "Q_TRANSPOSE"))
PY|    reject("mixed_sector_or_hull_is_not_a_pure_GME_argument",
PY|           "PURE_SCHMIDT_PRECONDITION",
PY|           lambda: assert_genuine_pure(maximally_mixed))
PY|    reject("pure_product_is_not_genuinely_entangled", "GME_PRODUCT_CUT",
PY|           lambda: assert_genuine_pure(product))
PY|
PY|    tick()
PY|    must(channel_cases == 20, "CHANNEL_CASE_COUNT")
PY|    must(exact_prefixes == 64, "EXACT_PREFIX_COUNT")
PY|    must(numeric_prefixes == 320, "NUMERICAL_PREFIX_COUNT")
PY|    must(POLY_CHECKS == 22, "CHARACTERISTIC_CHECK_COUNT")
PY|    must(MUTATIONS == 11, "MUTATION_COUNT")
PY|    print("PASS_SELECTED_FINITE_CASES_NOT_UNIVERSAL_PROOF")
PY|    print("channel_cases", channel_cases,
PY|          "exact_prefixes", exact_prefixes,
PY|          "numerical_prefixes", numeric_prefixes,
PY|          "exact_characteristic_checks", POLY_CHECKS,
PY|          "intended_reason_mutations", MUTATIONS)
PY|    print("maximum_numerical_eigenpair_residual", maximum_residual)
PY|    print("maximum_realification_pair_gap", maximum_pair_gap)
PY|    print("elapsed_seconds", time.monotonic() - START)
PY|
PY|if __name__ == "__main__":
PY|    try:
PY|        run()
PY|    except Failure as error:
PY|        deadline = error.reason == "DEADLINE_INCOMPLETE"
PY|        print("INCOMPLETE" if deadline else "FAIL", error.reason)
PY|        sys.exit(2 if deadline else 1)

**End of complete source.**

## 5. Disposition

The reachable read-only work is complete: controls, direct acknowledgment, full ordered packet reading, written reconstruction, exact selected tables, complex-projector transport witness, and complete bounded checker source.

The independent finite gate remains **NOT RUN**, specifically because this review role forbids scientific execution. Source correctness and runtime have not been established by execution. Neither the checker’s prospective success messages nor its expected counts are reported as observed evidence.

No unrestricted four-qubit theorem, all-genuinely-entangled-state theorem, independent-model-family review, human review, formal/kernel verification, novelty determination or automatic adoption is claimed.

Overall correctness: correct

Explanation: No evidence-backed defect was found in the supplied Dicke and invariant-sector mathematical claims within the reconstructed scope. Independent finite corroboration remains NOT RUN; the complete source is returned for parent-controlled materialization and execution, not represented as a completed finite PASS.

Confidence: 0.90