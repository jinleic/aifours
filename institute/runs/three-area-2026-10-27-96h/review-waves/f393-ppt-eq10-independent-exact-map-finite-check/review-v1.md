# author-candidate-v1.md — Independent exact finite audit of the literal Eq. (10) map

**Wave:** f393-ppt-eq10-independent-exact-map-finite-check  
**Role:** FINITE  
**Disposition:** AUTHOR CANDIDATE / UNREVIEWED; parent disposition required.  
**Execution:** **NOT RUN.** Exact values below are written derivations, not computational output.  
**Original PPT/Schmidt-number target:** **NOT CLOSED.**

This complete delivery includes the additional parent clock observation. No scientific execution occurred between deliveries.

## 1. Inputs, chronology, and attribution

I read the complete manifest, freeze receipt, and all seven status/permission controls before the scientific packet. The controls were used only for permissions and exclusions. I then read the complete ordered packet, LF 1–731, in raw windows of at most 20 LF:

- **S1:** complete allowed range LF 1–663, including its ending. The author checker at LF 664–823 was **not read**.
- **S2:** LF 1–66, including its ending.
- After that ordered pass, I reread S2 LF 53–59 and S1 LF 547–566 to bind the literal map and scalar population formulas.

No current sibling outcome or authored checker was consulted. All held scientific payloads and their consumers remained NONINPUT.

The following are **parent-supplied metadata**, not independently executed child hashes or clocks:

| Artifact | SHA-256 |
|---|---|
| Manifest | c242d2838f3520bf8dd210240e3acf1ad3d2f64646396009a2b8a9c135b496fc |
| Freeze receipt | 996ad7300fb337eef3e5ac6d611d29c3cb34c5055c00a6527b16d89e349b16a8 |
| Packet | 98f147239669017e34d3bb5c8a25769e52d9ca19192ac4b354574724025f28cf |
| S1 | 1365bde68234dff06aabd798acd0c740040e6560abb3da708404af43dad99dd6 |
| S2 | 2f9fb815902e8271bc04f927c5e8aa7c68fbb55e4344c36401553083c66ee1ba |

Parent supplied observations:

- `2026-10-30T10:34:20-0700 PDT`, with the live metadata record;
- `2026-10-30T10:47:18-0700 PDT`, explicitly described as an actual parent `/bin/date` observation.

Neither is my native start, derivation, checkpoint-send, or completion time. The substantive checkpoint was sent without a native clock; the later parent observation does not establish its exact send time.

No scientific executable, build, solver, random scan, installation, external-model CLI, remote job, or working-tree write was performed. No filesystem or execution bypass was attempted. The complete independent source below is **NOT RUN**: no stdout, exit status, runtime, mutation rejection, or computational PASS is claimed.

## 2. Claimwise disposition

| Claim or obligation | Disposition | Boundary |
|---|---|---|
| Literal matrix-unit map, Choi indexing, full block decomposition | **SUPPORTED — written exact reconstruction** | All 16 matrix units; fixed convention |
| Seed fails \(2\)-positivity | **SUPPORTED** | Explicit rank-two quadratic \(-1/3\) |
| Rational \(3/5\) negative control | **SUPPORTED** | Exact \(-1/125\) at \(\delta=1/5\) |
| Genuinely complex negative control | **SUPPORTED** | Exact \(-1/375\), not a real-only test |
| Rational \(5/24\) positive controls | **SUPPORTED** | Pair determinant, diagonal-sector leading minors, selected complex Schur additions |
| \(\lambda=0\), singular, and genuinely complex PSD Schur cases | **SUPPORTED** | Explicit selected cases below |
| Explicit complex-\(K\) drift Choi identity and fixed sign | **SUPPORTED — written exact reconstruction** | Complete operator identity and exact probes |
| All 13 Taylor coefficient matrices, orders 0–12 | **SUPPORTED — written coefficient derivation** | Complete matrices specified below |
| Computational replay and five scientific mutation rejections | **INCONCLUSIVE / NOT RUN** | Full source supplied; execution unpaid |
| Universal \(2\)-positivity/CP equivalence over the full family | **INCONCLUSIVE at this FINITE gate** | Selected cases do not replace the universal proof |
| Uniform complex-\(K\) or analytic \(K=0\) time interval | **INCONCLUSIVE at this FINITE gate** | Finite Taylor matching is not an interval certificate |
| Ordinary positivity of the original seed | **INCONCLUSIVE** | Rank-two negativity does not refute ordinary positivity |
| Actual \(4\times4\) PPT/SN-\(\ge3\) state–detector pair | **NOT OBTAINED** | Original positive target not closed |
| All-\(4\times4\)-PPT SN-\(\le2\) theorem | **NOT OBTAINED** | No unrestricted obstruction established |
| Novelty or priority | **INCONCLUSIVE** | No exhaustive literature audit |

**F/M/m: 0 / 0 / 0** supported defects in the checked literal finite identities. This is not acceptance of unrun code, universal positivity, analytic intervals, novelty, or the original target.

## 3. Literal map and complete Choi decomposition

Use
\[
\operatorname{vec}(X)=\sum_{i,j}X_{ij}|ij\rangle,\qquad
C(\Phi)=\sum_{i,j}|i\rangle\langle j|\otimes\Phi(E_{ij}).
\]

The literal map is
\[
\Phi(X)=\frac13
\begin{pmatrix}
x_{11}+x_{22}+x_{33}&x_{12}&x_{13}&x_{14}\\
x_{21}&x_{22}+x_{33}+x_{44}&x_{23}&x_{24}\\
x_{31}&x_{32}&x_{33}+x_{44}+x_{11}&x_{43}\\
x_{41}&x_{42}&x_{34}&x_{44}+x_{11}+x_{22}
\end{pmatrix}.
\]

The consuming-side indexing is explicitly
\[
C(\Phi)_{4i+a,\,4j+b}
=\Phi(E_{ij})_{ab}
=T_{\Phi;\,4a+b,\,4i+j},
\]
with zero-based indices in this equation. The superoperator is **not** already the Choi matrix.

For
\(\mathcal D=(|11\rangle,|22\rangle,|33\rangle,|44\rangle)\) and
\(\mathcal B=(|34\rangle,|43\rangle)\),
\[
C(\Phi)|_{\mathcal D}=\frac13M,\quad
M=\begin{pmatrix}
1&1&1&1\\1&1&1&1\\1&1&1&0\\1&1&0&1
\end{pmatrix},
\]
\[
C(\Phi)|_{\mathcal B}
=\frac13\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]

The ten remaining singleton blocks have:

- weight \(0\): \(|12\rangle,|23\rangle,|41\rangle\);
- weight \(1/3\): \(|13\rangle,|14\rangle,|21\rangle,|24\rangle,|31\rangle,|32\rangle,|42\rangle\).

There are no additional couplings.

For
\[
\Psi_{\lambda,\delta,S}
=\lambda\Phi+\delta\Delta+\mathcal M_S,\qquad
\Delta(X)=\operatorname{Tr}(X)I,\quad\mathcal M_S(X)=S\circ X,
\]
the complete blocks are
\[
C(\Psi)|_{\mathcal D}=\delta I+\lambda M/3+S,\qquad
C(\Psi)|_{\mathcal B}
=\begin{pmatrix}\delta&\lambda/3\\\lambda/3&\delta+\lambda/3\end{pmatrix},
\]
with singleton weights \(\delta\) or \(\delta+\lambda/3\) in the positions listed above. Complex Schur entries are retained literally.

**Source LF:** S1 139–181, 229–277; S2 53–59.

## 4. Exact negative and positive controls

Let
\[
p=|34\rangle-|43\rangle,\qquad
w=|34\rangle-\frac35|43\rangle,
\]
\[
v=|34\rangle+\left(-\frac35+\frac{i}{10}\right)|43\rangle.
\]
All three coefficient matrices have rank exactly two and are orthogonal to \(\Omega=\sum_i|ii\rangle\). The last vector has genuinely nonreal relative coefficients.

Support separation gives
\[
\begin{aligned}
\langle p,C(\Psi)p\rangle&=2\delta-\lambda/3,\\
\langle w,C(\Psi)w\rangle&=\frac{34}{25}\delta-\frac7{25}\lambda,\\
\langle v,C(\Psi)v\rangle&=\frac{137}{100}\delta-\frac{83}{300}\lambda.
\end{aligned}
\]

| Parameters | \(p\) quadratic | \(w\) quadratic | \(v\) quadratic |
|---|---:|---:|---:|
| \((\lambda,\delta)=(1,0)\) | \(-1/3\) | \(-7/25\) | \(-83/300\) |
| \((1,1/5)\) | \(1/15\) | **\(-1/125\)** | **\(-1/375\)** |
| \((1,5/24)\) | \(1/12\) | \(1/300\) | \(7/800\) |

Thus the elementary antisymmetric vector alone would miss the negative repaired case at \(\delta=1/5\).

### Explicit complex PSD Schur controls

Set
\[
a=(1,i,1+i,0)^T,\quad b=(0,1,i,1-i)^T,\quad
S_*=aa^\dagger+\tfrac12bb^\dagger.
\]
Explicitly,
\[
S_*=
\begin{pmatrix}
1&-i&1-i&0\\
i&3/2&1+i/2&(1+i)/2\\
1+i&1-i/2&5/2&(-1+i)/2\\
0&(1-i)/2&(-1-i)/2&1
\end{pmatrix}.
\]
Its two Gram columns are independent, so \(S_*\ge0\), is singular, and has rank two. Let \(S_+=S_*+I/7\), positive definite of rank four.

The source below covers **14 selected cases**:

- \((1,0,0)\);
- \((1,1/5,S)\), for \(S=0,S_*,S_+\): not PSD;
- \((1,5/24,S)\), for those three \(S\): positive definite;
- \((0,0,S)\), for those three \(S\): PSD of ranks \(0,2,4\);
- \((0,1/7,S_*)\): positive definite;
- \((0,-1/7,S_*)\): not PSD;
- \((2,5/12,S_*)\): positive definite;
- \((1/2,5/48,S_*)\): positive definite.

For the base \(5/24\) positive control,
\[
B=\frac1{24}\begin{pmatrix}5&8\\8&13\end{pmatrix},
\qquad \det B=1/576.
\]
Its diagonal block is \(Q/24\), where
\[
Q=\begin{pmatrix}
13&8&8&8\\8&13&8&8\\8&8&13&0\\8&8&0&13
\end{pmatrix}.
\]
The leading principal determinants of \(Q\) are
\[
13,\quad105,\quad725,\quad1105,
\]
all positive. Sylvester’s criterion, the positive pair block, and positive singleton blocks establish positive definiteness. Adding either explicit PSD Schur matrix preserves it. Positive scaling establishes the two scaled controls.

These are selected exact cases, not a finite-testing proof of a uniform family.

**Source LF:** S1 183–218, 389–405. The complex vector \(v\), explicit Gram matrices, and their selected cases are fresh calculations here, without a literature-novelty claim.

## 5. Explicit complex-\(K\) drift and sign-sensitive check

Take
\[
K=\begin{pmatrix}
1+i&2-i&0&0\\
0&-1/2+i/3&0&0\\
0&0&0&1+2i\\
0&0&-2+i&3/4-i
\end{pmatrix},\qquad D_K(X)=KX+XK^\dagger.
\]
Matrix-unit substitution gives
\[
C(D_K)=|v_K\rangle\langle\Omega|
+|\Omega\rangle\langle v_K|,\qquad
(v_K)_{ia}=K_{ai}.
\]
With the fixed row-major convention, \(v_K=\operatorname{vec}(K^T)\), **not** \(\operatorname{vec}(K)\).

Every \(z\perp\Omega\) therefore has zero drift quadratic. The program checks the complete identity and four exact rank-two probes: \(p,w,v\), and \(|12\rangle+i|21\rangle\). It also checks
\[
\langle v,C(D_K+\Psi_{1,1/5,S_*})v\rangle=-1/375.
\]

For the source’s
\[
\eta=(|34\rangle-q|43\rangle)/\sqrt{1+q^2},
\qquad q=(\sqrt5-1)/2,
\]
the same operator identity gives zero drift quadratic because \(\eta\perp\Omega\). The Gaussian-rational program does not pretend to encode this irrational vector; it verifies the complete rational-complex operator identity and exact rational-complex probes.

Orthogonal probes alone cannot detect a global drift-sign error. The required sign anchor is
\[
\langle\Omega,C(D_K)\Omega\rangle
=8\operatorname{Re}\operatorname{Tr}K=10.
\]
The negative-drift mutant gives \(-10\).

**Source LF:** S1 415–473. No finite drift check is promoted to a uniform semigroup interval.

## 6. All 13 full Taylor coefficient matrices

Let \(T\) be the literal superoperator, \(P e_i=e_{i+1}\), \(A=J-P\), and
\[
d_n=3^n n!,\qquad k_n=\frac{3^n-(-1)^n}{4}.
\]
Using \(J^2=4J\) and \(JP=PJ=J\),
\[
A^n=(-1)^nP^n+k_nJ.
\]

Order the superoperator basis into four diagonal units, ten ordinary off-diagonal units, and the special pair \(E_{34},E_{43}\). Then
\[
\frac{T^n}{n!}
=\frac1{d_n}\left(
\operatorname{Circ}_P(a^{(n)})\oplus I_{10}\oplus H_n
\right),
\]
where \(H_n=I_2\) for even \(n\), and \(H_n=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\) for odd \(n\). Here column \(i\) of \(\operatorname{Circ}_P(a)\) is the forward cyclic shift by \(i\) of \(a\).

This table specifies every entry of all 13 matrices:

| \(n\) | \(k_n\) | \(a^{(n)}\) |
|---:|---:|---|
| 0 | 0 | (1, 0, 0, 0) |
| 1 | 1 | (1, 0, 1, 1) |
| 2 | 2 | (2, 2, 3, 2) |
| 3 | 7 | (7, 7, 7, 6) |
| 4 | 20 | (21, 20, 20, 20) |
| 5 | 61 | (61, 60, 61, 61) |
| 6 | 182 | (182, 182, 183, 182) |
| 7 | 547 | (547, 547, 547, 546) |
| 8 | 1640 | (1641, 1640, 1640, 1640) |
| 9 | 4921 | (4921, 4920, 4921, 4921) |
| 10 | 14762 | (14762, 14762, 14763, 14762) |
| 11 | 44287 | (44287, 44287, 44287, 44286) |
| 12 | 132860 | (132861, 132860, 132860, 132860) |

The corresponding Choi coefficient matrices have:

- \(\mathcal D\) diagonal \(a_0^{(n)}/d_n\), ordinary off-diagonal entries \(1/d_n\), and special \(34/43\) entries \(1/d_n\) for even \(n\), zero for odd \(n\);
- \(\mathcal B\) block
  \[
  d_n^{-1}\begin{pmatrix}
  a_1^{(n)}&\mathbf1_{n\text{ odd}}\\
  \mathbf1_{n\text{ odd}}&a_3^{(n)}
  \end{pmatrix};
  \]
- remaining singleton \(|ij\rangle\) weight \(a_{j-i\bmod4}^{(n)}/d_n\).

The code’s closed side is independently formed from the scalar series
\[
c=(e^{3u}-e^{-u})/4,\quad
(p_0,p_1,p_2,p_3)=
\left(c+\frac{\cosh u+\cos u}{2},
c-\frac{\sinh u+\sin u}{2},
c+\frac{\cosh u-\cos u}{2},
c+\frac{-\sinh u+\sin u}{2}\right),
\]
with \(u=t/3\), ordinary coherence \(e^u\), and special coherences \(\cosh u,\sinh u\). It compares every entry against direct superoperator powers and checks the Choi rendering.

**Source LF:** S1 547–590. Finite coefficient agreement is not an analytic sign certificate.

## 7. Scientific mutations

| Actual mathematical mutation | Mutated diagnostic | Required diagnostic |
|---|---:|---:|
| Omit \(34/43\) transpose | \(p\) quadratic \(1/3\) | \(-1/3\) |
| Omit \(1/3\) scale | \(C_{11,11}=1\) | \(1/3\) |
| Reverse population cycle | \(C_{12,12}=1/3\) | \(0\) |
| Treat superoperator as Choi | purported \(C_{12,12}=1/3\) | \(0\) |
| Negate fixed-\(K\) drift | \(\Omega\) quadratic \(-10\) | \(10\) |

The code requires rejection through the named exact scientific equality check. An arbitrary exception is not counted. **No rejection has been executed here.**

## 8. Complete independent source — NOT RUN

Materialize as `check_f393.py`.

**Argv:** `python3 -B check_f393.py --seconds 50`

Standard library only; exact Gaussian rationals; no candidate-code imports, file I/O, network, subprocess, randomness, or installed dependencies. The cooperative deadline is capped at 55 seconds and raises failure rather than printing PASS. Actual runtime remains unmeasured.

BEGIN FILE check_f393.py

import argparse
import time
from fractions import Fraction as F
from math import factorial

END = float("inf")


class AuditError(Exception):
    pass


def need(condition, reason):
    if not condition:
        raise AuditError(reason)


def tick():
    need(time.monotonic() <= END, "BUDGET_EXCEEDED_NO_PASS")


class G:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r, self.i = F(r), F(i)

    def __add__(self, other):
        other = g(other)
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-g(other))

    def __rsub__(self, other):
        return g(other) - self

    def __mul__(self, other):
        other = g(other)
        return G(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = g(other)
        denominator = other.r * other.r + other.i * other.i
        need(denominator != 0, "ZERO_DIVISOR")
        return G((self.r * other.r + self.i * other.i) / denominator,
                 (self.i * other.r - self.r * other.i) / denominator)

    def __rtruediv__(self, other):
        return g(other) / self

    def conjugate(self):
        return G(self.r, -self.i)

    def __bool__(self):
        return bool(self.r or self.i)

    def __eq__(self, other):
        other = g(other)
        return self.r == other.r and self.i == other.i

    def __str__(self):
        if not self.i:
            return str(self.r)
        if not self.r:
            return str(self.i) + "i"
        return "(" + str(self.r) + "+" + str(self.i) + "i)"

    __repr__ = __str__


def g(value):
    return value if isinstance(value, G) else G(value)


Z, ONE, II = G(), G(1), G(0, 1)


def zeros(n, m=None):
    return [[Z for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    result = zeros(n)
    for j in range(n):
        result[j][j] = ONE
    return result


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    c = g(c)
    return [[c * x for x in row] for row in a]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def mm(a, b):
    tick()
    result = zeros(len(a), len(b[0]))
    for i, row in enumerate(a):
        tick()
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        result[i][j] = result[i][j] + x * y
    return result


def inner(v, w):
    return sum((x.conjugate() * y for x, y in zip(v, w)), Z)


def outer(v, w):
    return [[x * y.conjugate() for y in w] for x in v]


def quadratic(a, v):
    return sum((x.conjugate() * a[i][j] * y
                for i, x in enumerate(v) if x
                for j, y in enumerate(v) if y and a[i][j]), Z)


def rank(a):
    b = [row[:] for row in a]
    r = 0
    for j in range(len(b[0])):
        tick()
        p = next((i for i in range(r, len(b)) if b[i][j]), None)
        if p is None:
            continue
        b[r], b[p] = b[p], b[r]
        pivot = b[r][j]
        b[r] = [x / pivot for x in b[r]]
        for i in range(len(b)):
            if i != r and b[i][j]:
                q = b[i][j]
                b[i] = [x - q * y for x, y in zip(b[i], b[r])]
        r += 1
        if r == len(b):
            break
    return r


def determinant(a):
    b = [row[:] for row in a]
    result = ONE
    for j in range(len(b)):
        tick()
        p = next((i for i in range(j, len(b)) if b[i][j]), None)
        if p is None:
            return Z
        if p != j:
            b[j], b[p] = b[p], b[j]
            result = -result
        pivot = b[j][j]
        result = result * pivot
        for i in range(j + 1, len(b)):
            q = b[i][j] / pivot
            for k in range(j + 1, len(b)):
                b[i][k] = b[i][k] - q * b[j][k]
            b[i][j] = Z
    return result


def is_psd(a):
    if a != dagger(a):
        return False
    b = [row[:] for row in a]
    for k in range(len(b)):
        tick()
        pivot = b[k][k]
        if pivot.i or pivot.r < 0:
            return False
        if not pivot:
            if any(b[k][j] for j in range(k + 1, len(b))):
                return False
            continue
        for i in range(k + 1, len(b)):
            for j in range(i, len(b)):
                value = b[i][j] - b[i][k] * b[k][j] / pivot
                b[i][j] = value
                b[j][i] = value.conjugate()
    return True


def unit(i, j):
    result = zeros(4)
    result[i][j] = ONE
    return result


def vector(items):
    result = [Z for _ in range(16)]
    for i, j, c in items:
        result[4 * i + j] = g(c)
    return result


def coefficient_matrix(v):
    return [v[4 * i:4 * i + 4] for i in range(4)]


def phi(x, mutation="literal"):
    y = [
        [x[0][0] + x[1][1] + x[2][2], x[0][1], x[0][2], x[0][3]],
        [x[1][0], x[1][1] + x[2][2] + x[3][3], x[1][2], x[1][3]],
        [x[2][0], x[2][1], x[2][2] + x[3][3] + x[0][0], x[3][2]],
        [x[3][0], x[3][1], x[2][3], x[3][3] + x[0][0] + x[1][1]],
    ]
    if mutation == "missing_transpose":
        y[2][3], y[3][2] = x[2][3], x[3][2]
    if mutation == "reverse_cycle":
        total = sum((x[i][i] for i in range(4)), Z)
        for i in range(4):
            y[i][i] = total - x[(i + 1) % 4][(i + 1) % 4]
    return scale(1 if mutation == "wrong_scale" else F(1, 3), y)


def repaired(x, lam, delta, schur):
    y = scale(lam, phi(x))
    tr = sum((x[i][i] for i in range(4)), Z)
    for i in range(4):
        for j in range(4):
            y[i][j] = y[i][j] + schur[i][j] * x[i][j]
        y[i][i] = y[i][i] + delta * tr
    return y


def superoperator(function):
    result = zeros(16)
    for i in range(4):
        for j in range(4):
            tick()
            y = function(unit(i, j))
            for a in range(4):
                for b in range(4):
                    result[4 * a + b][4 * i + j] = y[a][b]
    return result


def choi(function):
    result = zeros(16)
    for i in range(4):
        for j in range(4):
            tick()
            block = function(unit(i, j))
            for a in range(4):
                for b in range(4):
                    result[4 * i + a][4 * j + b] = block[a][b]
    return result


def reshuffle(t):
    result = zeros(16)
    for i in range(4):
        for j in range(4):
            for a in range(4):
                for b in range(4):
                    result[4 * i + a][4 * j + b] = t[4 * a + b][4 * i + j]
    return result


def reference_choi(lam, delta, schur):
    result = scale(delta, eye(16))
    for i in range(4):
        for j in range(4):
            m = 0 if (i, j) in ((2, 3), (3, 2)) else 1
            result[5 * i][5 * j] = (
                result[5 * i][5 * j] + lam * F(m, 3) + schur[i][j]
            )
            if i != j and j != (i + 1) % 4:
                q = 4 * i + j
                result[q][q] = result[q][q] + lam * F(1, 3)
    result[11][14] = result[11][14] + lam * F(1, 3)
    result[14][11] = result[14][11] + lam * F(1, 3)
    return result


def drift(x, k):
    return add(mm(k, x), mm(x, dagger(k)))


def scalar_coefficients(n):
    fac = factorial(n)
    e = F(1, 3 ** n * fac)
    common = (F(1) - (-F(1, 3)) ** n) / (4 * fac)
    h = e if n % 2 == 0 else F(0)
    s = e if n % 2 else F(0)
    co = e * (-1) ** (n // 2) if n % 2 == 0 else F(0)
    si = e * (-1) ** ((n - 1) // 2) if n % 2 else F(0)
    populations = [
        common + (h + co) / 2,
        common - (s + si) / 2,
        common + (h - co) / 2,
        common + (-s + si) / 2,
    ]
    return populations, e, h, s


def closed_superoperator_coefficient(n):
    populations, e, h, s = scalar_coefficients(n)
    result = zeros(16)
    for i in range(4):
        for shift in range(4):
            a = (i + shift) % 4
            result[5 * a][5 * i] = g(populations[shift])
        for j in range(4):
            if i != j and (i, j) not in ((2, 3), (3, 2)):
                q = 4 * i + j
                result[q][q] = g(e)
    result[11][11] = result[14][14] = g(h)
    result[14][11] = result[11][14] = g(s)
    return result


def closed_choi_coefficient(n):
    populations, e, h, s = scalar_coefficients(n)
    result = zeros(16)
    for i in range(4):
        for j in range(4):
            if i == j:
                result[5 * i][5 * j] = g(populations[0])
            else:
                result[5 * i][5 * j] = g(
                    h if (i, j) in ((2, 3), (3, 2)) else e
                )
                q = 4 * i + j
                result[q][q] = g(populations[(j - i) % 4])
    result[11][14] = result[14][11] = g(s)
    return result


def must_reject(tag, observed, correct):
    try:
        need(observed == correct, tag)
    except AuditError as error:
        need(str(error) == tag, "WRONG_MUTATION_REJECTION_REASON")
        print("MUTANT_REJECTED", tag, "observed", observed, "correct", correct)
    else:
        raise AuditError(tag + "_ESCAPED")


def main():
    global END
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=50)
    args = parser.parse_args()
    need(1 <= args.seconds <= 55, "INVALID_DEADLINE")
    started = time.monotonic()
    END = started + args.seconds

    need(II * II == -1, "GAUSSIAN_UNIT")
    a = [ONE, II, G(1, 1), Z]
    b = [Z, ONE, II, G(1, -1)]
    ss = add(outer(a, a), scale(F(1, 2), outer(b, b)))
    ss_literal = [
        [G(1), G(0, -1), G(1, -1), Z],
        [II, G(F(3, 2)), G(1, F(1, 2)), G(F(1, 2), F(1, 2))],
        [G(1, 1), G(1, -F(1, 2)), G(F(5, 2)), G(-F(1, 2), F(1, 2))],
        [Z, G(F(1, 2), -F(1, 2)), G(-F(1, 2), -F(1, 2)), ONE],
    ]
    need(ss == ss_literal, "COMPLEX_GRAM_ENTRIES")
    need(is_psd(ss) and rank(ss) == 2, "SINGULAR_COMPLEX_GRAM")
    sf = add(ss, scale(F(1, 7), eye(4)))
    need(is_psd(sf) and rank(sf) == 4, "FULL_RANK_COMPLEX_GRAM")
    s0 = zeros(4)

    p = vector([(2, 3, 1), (3, 2, -1)])
    w = vector([(2, 3, 1), (3, 2, -F(3, 5))])
    v = vector([(2, 3, 1), (3, 2, G(-F(3, 5), F(1, 10)))])
    chi = vector([(0, 1, 1), (1, 0, II)])
    omega = vector([(i, i, 1) for i in range(4)])
    for name, z in (("p", p), ("w", w), ("v", v), ("chi", chi)):
        need(rank(coefficient_matrix(z)) == 2, "RANK_TWO_" + name)
        need(inner(omega, z) == 0, "OMEGA_ORTHOGONAL_" + name)
    need(inner(v, v) == F(137, 100), "COMPLEX_VECTOR_NORM")

    cphi = choi(phi)
    tphi = superoperator(phi)
    need(cphi == reshuffle(tphi), "BASE_RESHUFFLE")
    need(cphi == reference_choi(F(1), F(0), s0), "BASE_FULL_BLOCKS")
    need(quadratic(cphi, p) == -F(1, 3), "SEED_NEGATIVE_QUADRATIC")
    need(quadratic(cphi, v) == -F(83, 300), "COMPLEX_SEED_QUADRATIC")

    cases = [("seed", F(1), F(0), s0, False, None)]
    for name, schur in (("zero", s0), ("singular_complex", ss),
                        ("full_complex", sf)):
        cases.append(("negative_1_5_" + name, F(1), F(1, 5),
                      schur, False, None))
        cases.append(("positive_5_24_" + name, F(1), F(5, 24),
                      schur, True, 16))
        cases.append(("lambda0_delta0_" + name, F(0), F(0),
                      schur, True, rank(schur)))
    cases.extend([
        ("lambda0_positive_complex", F(0), F(1, 7), ss, True, 16),
        ("lambda0_negative_complex", F(0), -F(1, 7), ss, False, None),
        ("lambda2_positive_complex", F(2), F(5, 12), ss, True, 16),
        ("lambda_half_positive_complex", F(1, 2), F(5, 48), ss, True, 16),
    ])
    need(len(cases) == 14, "SELECTED_CASE_COUNT")
    for name, lam, delta, schur, expected_psd, expected_rank in cases:
        function = lambda x, l=lam, d=delta, s=schur: repaired(x, l, d, s)
        c = choi(function)
        need(c == reference_choi(lam, delta, schur), "CASE_BLOCKS_" + name)
        need(c == reshuffle(superoperator(function)), "CASE_RESHUFFLE_" + name)
        need(is_psd(c) == expected_psd, "CASE_PSD_" + name)
        if expected_rank is not None:
            need(rank(c) == expected_rank, "CASE_RANK_" + name)
        qp, qw, qv = (quadratic(c, z) for z in (p, w, v))
        need(qp == 2 * delta - lam / 3, "CASE_P_QUADRATIC_" + name)
        need(qw == F(34, 25) * delta - F(7, 25) * lam,
             "CASE_W_QUADRATIC_" + name)
        need(qv == F(137, 100) * delta - F(83, 300) * lam,
             "CASE_V_QUADRATIC_" + name)
        print("CASE", name, "PSD", expected_psd,
              "q_p", qp, "q_w", qw, "q_complex", qv)

    positive = choi(lambda x: repaired(x, F(1), F(5, 24), s0))
    h0 = [[positive[5 * i][5 * j] for j in range(4)] for i in range(4)]
    for n, numerator in enumerate((13, 105, 725, 1105), start=1):
        minor = [row[:n] for row in h0[:n]]
        need(determinant(minor) == F(numerator, 24 ** n),
             "POSITIVE_D_LEADING_MINOR_" + str(n))
    pair = [[positive[i][j] for j in (11, 14)] for i in (11, 14)]
    need(determinant(pair) == F(1, 576), "POSITIVE_PAIR_DETERMINANT")

    k = [
        [G(1, 1), G(2, -1), Z, Z],
        [Z, G(-F(1, 2), F(1, 3)), Z, Z],
        [Z, Z, Z, G(1, 2)],
        [Z, Z, G(-2, 1), G(F(3, 4), -1)],
    ]
    dk = lambda x: drift(x, k)
    cd = choi(dk)
    vk = [k[a][i] for i in range(4) for a in range(4)]
    drift_formula = add(outer(vk, omega), outer(omega, vk))
    need(cd == drift_formula, "COMPLEX_K_DRIFT_OUTER_IDENTITY")
    need(cd == reshuffle(superoperator(dk)), "COMPLEX_K_DRIFT_RESHUFFLE")
    need(quadratic(cd, omega) == 10, "PLUS_K_DRIFT_SIGN")
    for name, z in (("p", p), ("w", w), ("v", v), ("chi", chi)):
        need(quadratic(cd, z) == 0, "ORTHOGONAL_DRIFT_ZERO_" + name)
    cl = choi(lambda x: add(dk(x), repaired(x, F(1), F(1, 5), ss)))
    need(cl == add(cd, choi(lambda x: repaired(x, F(1), F(1, 5), ss))),
         "COMPLEX_GENERATOR_LINEARITY")
    need(quadratic(cl, v) == -F(1, 375), "COMPLEX_GENERATOR_NEGATIVE")
    print("COMPLEX_K_IDENTITY_AND_SIGN_CHECKED")

    power = eye(16)
    for n in range(13):
        direct = scale(F(1, factorial(n)), power)
        closed = closed_superoperator_coefficient(n)
        need(direct == closed, "TAYLOR_FULL_SUPEROPERATOR_" + str(n))
        need(reshuffle(direct) == closed_choi_coefficient(n),
             "TAYLOR_FULL_CHOI_" + str(n))
        denominator = 3 ** n * factorial(n)
        first_column = [direct[5 * i][0] * denominator for i in range(4)]
        print("TAYLOR", n, "FULL_MATRICES_EQUAL",
              "scaled_population_column", first_column)
        if n < 12:
            power = mm(tphi, power)

    must_reject(
        "MISSING_34_43_TRANSPOSE",
        quadratic(choi(lambda x: phi(x, "missing_transpose")), p),
        -F(1, 3),
    )
    must_reject(
        "WRONG_ONE_THIRD_SCALE",
        choi(lambda x: phi(x, "wrong_scale"))[0][0],
        F(1, 3),
    )
    must_reject(
        "WRONG_CYCLIC_ORIENTATION",
        choi(lambda x: phi(x, "reverse_cycle"))[1][1],
        0,
    )
    must_reject(
        "INCORRECT_CHOI_RESHAPE",
        tphi[1][1],
        cphi[1][1],
    )
    must_reject(
        "NEGATIVE_K_DRIFT_CONVENTION",
        quadratic(choi(lambda x: scale(-1, dk(x))), omega),
        10,
    )

    tick()
    print("ALL_SPECIFIED_FINITE_CHECKS_PASSED",
          "elapsed_seconds", time.monotonic() - started)


if __name__ == "__main__":
    try:
        main()
    except AuditError as error:
        print("FAIL", error)
        raise SystemExit(1)

END FILE check_f393.py

## 9. Unpaid gates and original-target boundary

1. **Execution:** parent must materialize and pin the exact source, run the bounded argv, and retain actual output and exit status. The program’s conditional PASS string is not an observed result.
2. **Universal proof:** selected rational-complex cases do not discharge all complex rank-\(\le2\) vectors or all PSD Schur additions.
3. **Analytic intervals:** 13 exact Taylor matrices do not certify a sign throughout an interval or an all-\(K\) semigroup theorem.
4. **Ordinary versus \(2\)-positivity:** the rank-two negative quadratic refutes the \(2\)-positive-seed premise, not ordinary positivity.
5. **Original target:** neither a genuine \(4\times4\) PPT/SN-\(\ge3\) state–detector pair nor an all-PPT SN-\(\le2\) theorem is supplied.
6. **Novelty:** the public source is [arXiv:2508.21348v2, §4.2, Workflow 1 and Eq. (10)](https://arxiv.org/html/2508.21348v2#S4.E10). The preserved source explicitly describes ordinary positivity as unproved and numerically supported. No priority conclusion follows.
7. **Cross-target exclusions:** this audit makes no finding about fixed-\(F\) negativity, eight-strict-negative SPR assertions, or any excluded PH/AME claim.

**Overall correctness:** correct at the explicitly checked written finite/algebraic scope; no supported defect found. Computational replay, universal/analytic claims, novelty, and original-target acceptance remain unpaid.

**Confidence:** 0.96 for the written identities and scope distinctions; no computational verification claimed.