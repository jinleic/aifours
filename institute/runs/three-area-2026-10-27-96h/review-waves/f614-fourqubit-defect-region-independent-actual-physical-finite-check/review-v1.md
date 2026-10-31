# author-candidate-v1.md — f614 FINITE

**Result: COMPLETE SOURCE-ONLY FINITE RETURN; NOT RUN. No finite PASS is issued.**

The complete independent standard-library verifier is supplied below for Main materialization. It constructs the actual \(16\times16\) density matrices, physical partial traces, Pauli layers, channel outputs and complex consuming projectors. Its exact arithmetic is in \(\mathbb Q(\sqrt{15},i)\); its spectral comparisons are explicitly numerical.

Higher-priority role restrictions prohibited scientific execution and filesystem edits here. I did not bypass them. No program was run, no numerical residual or test result was observed, and no repository file was written.

## 1. Read chronology and provenance

Before reading the scientific packet or deriving anything, I completed the manifest, freeze receipt and all thirteen permission/status controls, including the entire f586 exclusion. I then delivered the required **PREBODYACK directly to `agent://Main`**.

After that acknowledgement, I read the entire literal packet in ordered raw calls, each at most 20 LF:

\(1\!-\!20,21\!-\!40,\ldots,801\!-\!820,821\!-\!835\).

This included S1’s final logical line 765, S2’s ending and S3’s ending. Derivation and source preparation followed that complete read.

The following are **parent-supplied/live-attested metadata**, not my own executed hash or native-clock observations:

- Manifest: `e29dbdf6f03d4e36a831df5883d5d44f3cef0e221803e6e58a10bfc77004da3b`.
- Receipt: `57682bae3ac06a94bd1d6d79f3cdbe0baaf0a39a7e8d51300edbcdd911dfd900`.
- Packet: `943c9370f473aeda673069d9ff95d546cba16269b5447987f5ebeb9c8691dccd`.
- Parent metadata observation: `2026-10-30T14:21:00-0700 PDT`.

I did not open linked scientific sources, author programs, sibling reviews or held scientific payloads. All held episodes and their consumers remain NONINPUT. This is an access/chronology account, not a cognitive-isolation certificate.

## 2. Written exact checks and disclosed selections

These are **written algebraic results**, not execution results.

Use the computational ordering \(0000,\ldots,1111\), with
\(\Theta v=Y^{\otimes4}\overline v\). On a computational ket,
\(\Theta|z\rangle=(-1)^{|z|}|\bar z\rangle\), followed by conjugation of its coefficient.

### Pure-only band witness

Define
\[
e_0^+=(|0000\rangle+|1111\rangle)/\sqrt2,\qquad
e_1^+=(|0011\rangle+|1100\rangle)/\sqrt2
\]
and
\[
\psi_q=\sqrt q\,e_0^++i\sqrt{1-q}\,e_1^+.
\]

Both basis vectors are \(\Theta\)-fixed. Thus
\[
\eta=(2q-1)^2,\qquad d^2=4q(1-q).
\]

At the assigned \(q=15/16\),
\[
\eta=\frac{49}{64},\quad d^2=\frac{15}{64},\quad S_1=0,\quad
\operatorname{Tr}H_3^2=\frac{305}{32}.
\]
In particular,
\[
\frac{15}{64}-\frac3{13}=\frac3{832}>0,\qquad
\frac{17}{72}-\frac{15}{64}=\frac1{576}>0.
\]

This is an actual state in the **larger pure region but outside the mixed sufficient defect region**. Its nonzero \(2\eta=49/32\) distinguishes the missing-\(2\eta\) mutation. The \(q=1/2\) state has \(\eta=0,d=1\); it is included only as an outside-region diagnostic, not as a counterexample or new-region witness.

### Two concrete Dicke perturbations

Let \(D\) have coefficient \(1/\sqrt6\) on the six weight-two strings. Specify each \(y\) by its numerator on the ordered support
\[
(0011,0101,0110,1001,1010,1100),
\]
with the common denominator \(\sqrt6\):

- \(y_A:\ (i,i,i,-i,-i,-i)\).
- \(y_B:\ (1+i,-1,0,0,-1,1-i)\).

Both satisfy \(\Theta y=y\), \(\langle D,y\rangle=0\) and \(\|y\|=1\). These are fresh, fully disclosed FINITE selections.

For
\[
\psi_B=(4D+i y_B)/\sqrt{17},
\]
the numerator on that support is
\[
(3+i,\ 4-i,\ 4,\ 4,\ 4-i,\ 5+i)
\]
with denominator \(\sqrt{102}\). Direct normalization and overlap give
\[
\eta=\frac{225}{289},\qquad d=\frac8{17},\qquad
S_1=\frac{256}{2601},\qquad
\operatorname{Tr}H_3^2=\frac{8542}{867}.
\]
Both perturbations have \(d^2=64/289<3/13\).

Each has squared overlap \(16/17\) with \(D\). The largest squared Schmidt coefficient of \(D\) over all seven cuts is \(2/3\); hence their fidelity with \(D\) proves genuine multipartite entanglement. Their intermediate \(\eta\) excludes the invariant/Dicke and coherent-vacuum–W4 pure classes. Rank-one positivity supplies the named-hull exclusion. This does not assert that arbitrary mixtures are genuinely entangled.

### Mixed states

The source includes:

- \((1-\delta)I/16+\delta|0000\rangle\langle0000|\), at \(\delta=6/13\) and \(1/2\). Here \(d=\delta\) exactly.
- \(3\rho_B/4+I/64\). This is the convex mixture of \(\rho_B\) with weight \(3/4\) and each computational pure state with weight \(1/64\). Here \(d=6/17\).
- \(3\rho_B/4+\rho_D/4\), again with \(d=6/17\).
- \(I/16\), whose \(H_3=I/2\) has rank 16.

The first complex mixture is nonproduct: all its one-site marginals are diagonal, while its \(0011,0101\) entry is \((11+7i)/136\ne0\). Rank 16 for the maximally mixed example is a **scope guard against applying the pure rank-13 argument to mixed inputs**, not a channel counterexample.

The old coherent control is
\[
(3|0000\rangle+2|0001\rangle+2|0010\rangle+
2|0100\rangle+2|1000\rangle)/5.
\]
Its \(\eta=0\), so it is not evidence for the coefficient \(2\eta\).

### Discriminating full-transpose consumer

For the complex \(\rho_B\), take
\[
v=(|0011\rangle+i|0101\rangle)/\sqrt2,\qquad Q=|v\rangle\langle v|.
\]
At \(p=4/3\), direct written arithmetic gives
\[
\operatorname{Tr}(Q\Phi_{4/3}^{\otimes4}(\rho_B))=\frac{77}{972},
\]
whereas omitting the transpose in the transported consumer gives
\[
\operatorname{Tr}\!\left((WQW)T_{1/3}^{\otimes4}(\rho_B)\right)
=\frac{1193}{16524}.
\]
The discrepancy is
\[
\frac{29}{4131}\ne0.
\]
The program checks these values exactly, using independently constructed physical channel matrices.

## 3. Uniform arithmetic and scope

Independent rational arithmetic reconstructs the Cauchy boundary moments:

- Rank 16: \(92/7,\ 160/13,\ 37/3\); minimum \(160/13\).
- Rank 13: \(293/22,\ 62/5,\ 445/36\); minimum \(445/36\).

Consequently,
\[
10(1+3/13)=160/13,\qquad
10(1+17/72)=445/36,\qquad
1-17/72=55/72.
\]

The source checks the entire \(H_2\) table at \(d=1/2\), including all sixteen prefixes, with exact rational arithmetic. It also reconstructs each product layer from the actual product density and checks its Hamming-weight diagonal entries. Thus its channel reference is the actual product-reference spectrum, not a larger independent-layer relaxation.

**All-\(p\) assurance remains written:** nonnegative channel coefficients, the common-\(Q\) inequalities and exact co-ordering give every prefix for the full positive branch; full-transpose transport gives the physical negative branch. A finite grid is not relabelled a continuum proof.

I found no defect in the supplied scoped written chain. This return does not close unrestricted four-qubit majorization.

## 4. Execution status and command

**NOT RUN.** No exit status, elapsed runtime, spectral residual, mutation pass count or numerical-prefix outcome is claimed.

Proposed argv after Main materializes the source:

`python3 -B independent-fourqubit-defect-physical-v1.py --seconds 55`

The source uses only the standard library, reads no files or stdin, creates no files, uses no network or child process, and has an internal cooperative deadline. The deadline is not an externally enforced hard-real-time guarantee. If reached, the program returns **INCOMPLETE**, never PASS.

There are eleven selected densities and seven channel parameters. Completion would produce **1,232 numerical output-prefix comparisons**; this is a designed count, not an observed result. Exact matrix identities and numerical spectral results are printed separately.

## 5. Complete source

Every following line beginning `PY|` is a source line. Remove exactly that three-character prefix, preserving the remainder and the line endings, to materialize the complete Python file. There are no omitted helpers or external inputs.

PY|#!/usr/bin/env python3
PY|"""Independent four-qubit defect verifier. SOURCE PREPARED; NOT RUN HERE."""
PY|import argparse
PY|import itertools
PY|import math
PY|import sys
PY|import time
PY|from fractions import Fraction as F
PY|
PY|N = 16
PY|ROOT = math.sqrt(15.0)
PY|TOL = 2e-9
PY|RES_TOL = 2e-11
PY|DEADLINE = None
PY|CHECKS = 0
PY|SPECTRA = 0
PY|PREFIX_COMPARISONS = 0
PY|CHANNEL_CASES = 0
PY|MAX_RESIDUAL = 0.0
PY|MAX_ORTHOGONALITY = 0.0
PY|MAX_ROW_RESIDUAL = 0.0
PY|
PY|class CheckFailure(Exception):
PY|    def __init__(self, reason):
PY|        super().__init__(reason)
PY|        self.reason = reason
PY|
PY|class Incomplete(Exception):
PY|    pass
PY|
PY|def tick():
PY|    if DEADLINE is not None and time.perf_counter() >= DEADLINE:
PY|        raise Incomplete("cooperative calculation deadline")
PY|
PY|def need(condition, reason):
PY|    global CHECKS
PY|    CHECKS += 1
PY|    if not condition:
PY|        raise CheckFailure(reason)
PY|
PY|def expect_rejection(reason, operation):
PY|    try:
PY|        operation()
PY|    except CheckFailure as exc:
PY|        need(exc.reason == reason, "WRONG_MUTATION_REJECTION_REASON")
PY|        print("CONTROL_REJECTED", reason)
PY|        return
PY|    raise CheckFailure("MUTATION_NOT_REJECTED:" + reason)
PY|
PY|class E:
PY|    """Exact a+b*sqrt(15)+i*(c+d*sqrt(15)); division only by rationals."""
PY|    __slots__ = ("a", "b", "c", "d")
PY|
PY|    def __init__(self, a=0, b=0, c=0, d=0):
PY|        self.a, self.b, self.c, self.d = F(a), F(b), F(c), F(d)
PY|
PY|    def __bool__(self):
PY|        return bool(self.a or self.b or self.c or self.d)
PY|
PY|    def __eq__(self, other):
PY|        if not isinstance(other, E):
PY|            try:
PY|                other = E(other)
PY|            except (TypeError, ValueError):
PY|                return NotImplemented
PY|        return (self.a, self.b, self.c, self.d) == (
PY|            other.a, other.b, other.c, other.d)
PY|
PY|    def __add__(self, other):
PY|        if not isinstance(other, E):
PY|            other = E(other)
PY|        if not self:
PY|            return other
PY|        if not other:
PY|            return self
PY|        return E(self.a + other.a, self.b + other.b,
PY|                 self.c + other.c, self.d + other.d)
PY|
PY|    __radd__ = __add__
PY|
PY|    def __neg__(self):
PY|        return E(-self.a, -self.b, -self.c, -self.d)
PY|
PY|    def __sub__(self, other):
PY|        return self + (-other if isinstance(other, E) else E(-other))
PY|
PY|    def __rsub__(self, other):
PY|        return -self + other
PY|
PY|    def __mul__(self, other):
PY|        if not isinstance(other, E):
PY|            s = F(other)
PY|            return E(self.a*s, self.b*s, self.c*s, self.d*s)
PY|        if not self or not other:
PY|            return Z
PY|        if not other.b and not other.c and not other.d:
PY|            return self * other.a
PY|        if not self.b and not self.c and not self.d:
PY|            return other * self.a
PY|        a, b, c, d = self.a, self.b, self.c, self.d
PY|        u, v, w, x = other.a, other.b, other.c, other.d
PY|        return E(a*u + 15*b*v - c*w - 15*d*x,
PY|                 a*v + b*u - c*x - d*w,
PY|                 a*w + 15*b*x + c*u + 15*d*v,
PY|                 a*x + b*w + c*v + d*u)
PY|
PY|    __rmul__ = __mul__
PY|
PY|    def __truediv__(self, scalar):
PY|        return self * (F(1) / F(scalar))
PY|
PY|    def conj(self):
PY|        return E(self.a, self.b, -self.c, -self.d)
PY|
PY|    def rotate(self, power):
PY|        p = power % 4
PY|        if p == 0:
PY|            return self
PY|        if p == 1:
PY|            return E(-self.c, -self.d, self.a, self.b)
PY|        if p == 2:
PY|            return -self
PY|        return E(self.c, self.d, -self.a, -self.b)
PY|
PY|    def approximate(self):
PY|        return complex(float(self.a) + float(self.b)*ROOT,
PY|                       float(self.c) + float(self.d)*ROOT)
PY|
PY|Z = E()
PY|O = E(1)
PY|II = E(c=1)
PY|SQ15 = E(b=1)
PY|
PY|def rq(value):
PY|    need(not value.b and not value.c and not value.d,
PY|         "EXPECTED_REAL_RATIONAL")
PY|    return value.a
PY|
PY|def zero(n=N):
PY|    return [[Z for _ in range(n)] for _ in range(n)]
PY|
PY|def identity(n=N):
PY|    out = zero(n)
PY|    for i in range(n):
PY|        out[i][i] = O
PY|    return out
PY|
PY|I = identity()
PY|
PY|def scale(A, s):
PY|    return [[x*s for x in row] for row in A]
PY|
PY|def add(*matrices):
PY|    n = len(matrices[0])
PY|    return [[sum((A[i][j] for A in matrices), Z)
PY|             for j in range(n)] for i in range(n)]
PY|
PY|def sub(A, B):
PY|    return add(A, scale(B, -1))
PY|
PY|def mm(A, B):
PY|    n = len(A)
PY|    out = zero(n)
PY|    for i in range(n):
PY|        for k, x in enumerate(A[i]):
PY|            if not x:
PY|                continue
PY|            for j, y in enumerate(B[k]):
PY|                if y:
PY|                    out[i][j] = out[i][j] + x*y
PY|    return out
PY|
PY|def trace(A):
PY|    return sum((A[i][i] for i in range(len(A))), Z)
PY|
PY|def trprod(A, B):
PY|    return sum((A[i][j]*B[j][i]
PY|                for i in range(len(A)) for j in range(len(A))
PY|                if A[i][j] and B[j][i]), Z)
PY|
PY|def adjoint(A):
PY|    return [[A[j][i].conj() for j in range(len(A))]
PY|            for i in range(len(A))]
PY|
PY|def vec(entries):
PY|    out = [Z for _ in range(N)]
PY|    for index, value in entries.items():
PY|        out[index] = value if isinstance(value, E) else E(value)
PY|    return out
PY|
PY|def dot(u, v):
PY|    return sum((a.conj()*b for a, b in zip(u, v)), Z)
PY|
PY|def outer(v):
PY|    return [[a*b.conj() for b in v] for a in v]
PY|
PY|def theta(v):
PY|    out = [Z for _ in range(N)]
PY|    for x, value in enumerate(v):
PY|        out[15-x] = value.conj() * (-1 if x.bit_count() % 2 else 1)
PY|    return out
PY|
PY|def spin(A):
PY|    return [[A[15-j][15-i] *
PY|             (-1 if (i.bit_count()+j.bit_count()) % 2 else 1)
PY|             for j in range(N)] for i in range(N)]
PY|
PY|def conjugate_W(A):
PY|    return [[A[15-i][15-j] *
PY|             (-1 if (i.bit_count()+j.bit_count()) % 2 else 1)
PY|             for j in range(N)] for i in range(N)]
PY|
PY|def pure(v):
PY|    norm = rq(dot(v, v))
PY|    need(norm > 0, "PURE_VECTOR_NONZERO")
PY|    rho = scale(outer(v), F(1)/norm)
PY|    overlap = dot(v, theta(v))/norm
PY|    eta = rq(overlap*overlap.conj())
PY|    need(mm(rho, rho) == rho, "ACTUAL_PURE_DENSITY")
PY|    return rho, eta
PY|
PY|def positions(x, sites):
PY|    answer = 0
PY|    for site in sites:
PY|        answer = 2*answer + ((x >> (3-site)) & 1)
PY|    return answer
PY|
PY|def lifted_marginal(rho, sites):
PY|    """Partial trace first; lift in the original physical tensor positions."""
PY|    sites = tuple(sites)
PY|    outside = tuple(s for s in range(4) if s not in sites)
PY|    small = zero(1 << len(sites))
PY|    inside_index = [positions(x, sites) for x in range(N)]
PY|    outside_index = [positions(x, outside) for x in range(N)]
PY|    for x in range(N):
PY|        for y in range(N):
PY|            if outside_index[x] == outside_index[y]:
PY|                a, b = inside_index[x], inside_index[y]
PY|                small[a][b] = small[a][b] + rho[x][y]
PY|    out = zero()
PY|    for x in range(N):
PY|        for y in range(N):
PY|            if outside_index[x] == outside_index[y]:
PY|                out[x][y] = small[inside_index[x]][inside_index[y]]
PY|    return out
PY|
PY|def layers(rho):
PY|    out = [I]
PY|    for j in range(1, 5):
PY|        tick()
PY|        pieces = [lifted_marginal(rho, sites)
PY|                  for sites in itertools.combinations(range(4), j)]
PY|        out.append(add(*pieces))
PY|    return out
PY|
PY|def action(labels):
PY|    """P|x> = i**phase[x] |permutation[x]>; I,X,Y,Z = 0,1,2,3."""
PY|    permutation, phases = [], []
PY|    for x in range(N):
PY|        y, phase = x, 0
PY|        for site, label in enumerate(labels):
PY|            bit = (x >> (3-site)) & 1
PY|            if label in (1, 2):
PY|                y ^= 1 << (3-site)
PY|            if label == 2:
PY|                phase += 1 if bit == 0 else 3
PY|            elif label == 3 and bit:
PY|                phase += 2
PY|        permutation.append(y)
PY|        phases.append(phase % 4)
PY|    return permutation, phases
PY|
PY|PAULIS = [(sum(label != 0 for label in labels), action(labels))
PY|          for labels in itertools.product(range(4), repeat=4)]
PY|LOCAL = []
PY|for site in range(4):
PY|    group = []
PY|    for label in (1, 2, 3):
PY|        labels = [0]*4
PY|        labels[site] = label
PY|        group.append(action(labels))
PY|    LOCAL.append(group)
PY|
PY|def conjugate_pauli(A, pauli):
PY|    permutation, phases = pauli
PY|    out = zero()
PY|    for x in range(N):
PY|        for y in range(N):
PY|            if A[x][y]:
PY|                out[permutation[x]][permutation[y]] = (
PY|                    A[x][y].rotate(phases[x]-phases[y]))
PY|    return out
PY|
PY|def pauli_layers(rho):
PY|    R = [zero() for _ in range(5)]
PY|    S = [Z for _ in range(5)]
PY|    for index, (weight, pauli) in enumerate(PAULIS):
PY|        if index % 32 == 0:
PY|            tick()
PY|        permutation, phases = pauli
PY|        coefficient = sum((rho[x][permutation[x]].rotate(phases[x])
PY|                           for x in range(N)), Z)
PY|        need(not coefficient.c and not coefficient.d,
PY|             "PHYSICAL_PAULI_EXPECTATION_REAL")
PY|        if weight == 0:
PY|            need(coefficient == 1, "PAULI_IDENTITY_COEFFICIENT")
PY|            continue
PY|        S[weight] = S[weight] + coefficient*coefficient
PY|        for x in range(N):
PY|            y = permutation[x]
PY|            R[weight][y][x] = R[weight][y][x] + coefficient.rotate(phases[x])
PY|    return R, [rq(s) for s in S]
PY|
PY|def channel_pauli(rho, p):
PY|    """Actual four local Pauli-sum channels, not a spectral surrogate."""
PY|    A = rho
PY|    for local in LOCAL:
PY|        tick()
PY|        A = add(scale(A, 1-F(3, 4)*p),
PY|                *(scale(conjugate_pauli(A, P), p/4) for P in local))
PY|    return A
PY|
PY|def channel_erasure(rho, H, p):
PY|    u, c = 1-p, p/2
PY|    return add(scale(rho, u**4), scale(H[3], u**3*c),
PY|               scale(H[2], u*u*c*c), scale(H[1], u*c**3),
PY|               scale(I, c**4))
PY|
PY|def prefixes(values):
PY|    out, total = [], F(0)
PY|    for x in values:
PY|        total += x
PY|        out.append(total)
PY|    return out
PY|
PY|def eigenvalues(A):
PY|    """Complex Hermitian Jacobi; NUMERICAL, never an exact-root certificate."""
PY|    global SPECTRA, MAX_RESIDUAL, MAX_ORTHOGONALITY, MAX_ROW_RESIDUAL
PY|    tick()
PY|    original = [[x.approximate() for x in row] for row in A]
PY|    n = len(A)
PY|    B = [row[:] for row in original]
PY|    V = [[complex(i == j) for j in range(n)] for i in range(n)]
PY|    need(max(abs(B[i][j]-B[j][i].conjugate())
PY|             for i in range(n) for j in range(n)) < 1e-12,
PY|         "NUMERICAL_INPUT_HERMITIAN")
PY|    for _ in range(80):
PY|        tick()
PY|        row_residual = max(sum(abs(B[i][j]) for j in range(n) if j != i)
PY|                           for i in range(n))
PY|        if row_residual <= 1e-13:
PY|            break
PY|        for p in range(n-1):
PY|            for q in range(p+1, n):
PY|                z = B[p][q]
PY|                az = abs(z)
PY|                if az <= 1e-16:
PY|                    continue
PY|                app, aqq = B[p][p].real, B[q][q].real
PY|                tau = (aqq-app)/(2*az)
PY|                t = math.copysign(1.0, tau)/(abs(tau)+math.hypot(1.0, tau))
PY|                c = 1/math.sqrt(1+t*t)
PY|                s = t*c
PY|                phase = z/az
PY|                for k in range(n):
PY|                    if k == p or k == q:
PY|                        continue
PY|                    u, v = B[k][p], B[k][q]
PY|                    B[k][p] = c*u-s*phase.conjugate()*v
PY|                    B[p][k] = B[k][p].conjugate()
PY|                    B[k][q] = s*phase*u+c*v
PY|                    B[q][k] = B[k][q].conjugate()
PY|                B[p][p] = complex(app-t*az)
PY|                B[q][q] = complex(aqq+t*az)
PY|                B[p][q] = B[q][p] = 0j
PY|                for k in range(n):
PY|                    u, v = V[k][p], V[k][q]
PY|                    V[k][p] = c*u-s*phase.conjugate()*v
PY|                    V[k][q] = s*phase*u+c*v
PY|    row_residual = max(sum(abs(B[i][j]) for j in range(n) if j != i)
PY|                       for i in range(n))
PY|    diagonal = [B[i][i].real for i in range(n)]
PY|    residual_squared = 0.0
PY|    orthogonality = 0.0
PY|    for i in range(n):
PY|        tick()
PY|        for j in range(n):
PY|            residual = (sum(original[i][k]*V[k][j] for k in range(n))
PY|                        - V[i][j]*diagonal[j])
PY|            residual_squared += abs(residual)**2
PY|            gram = sum(V[k][i].conjugate()*V[k][j] for k in range(n))
PY|            orthogonality = max(orthogonality, abs(gram-(i == j)))
PY|    residual = math.sqrt(residual_squared)
PY|    need(row_residual <= RES_TOL, "JACOBI_OFFDIAGONAL_RESIDUAL")
PY|    need(residual <= RES_TOL, "JACOBI_EIGENPAIR_RESIDUAL")
PY|    need(orthogonality <= RES_TOL, "JACOBI_ORTHOGONALITY_RESIDUAL")
PY|    need(abs(sum(diagonal)-rq(trace(A))) <= TOL,
PY|         "NUMERICAL_TRACE_RESIDUAL")
PY|    MAX_RESIDUAL = max(MAX_RESIDUAL, residual)
PY|    MAX_ORTHOGONALITY = max(MAX_ORTHOGONALITY, orthogonality)
PY|    MAX_ROW_RESIDUAL = max(MAX_ROW_RESIDUAL, row_residual)
PY|    SPECTRA += 1
PY|    return sorted(diagonal, reverse=True)
PY|
PY|def spectral_prefixes(A, reference, required, reason, count_output=False):
PY|    global PREFIX_COMPARISONS
PY|    values = eigenvalues(A)
PY|    s, r, worst = 0.0, 0.0, -float("inf")
PY|    for value, ref in zip(values, reference):
PY|        s += value
PY|        r += float(ref)
PY|        excess = s-r
PY|        worst = max(worst, excess)
PY|        if count_output:
PY|            PREFIX_COMPARISONS += 1
PY|        if required:
PY|            need(excess <= TOL, reason)
PY|    need(abs(s-r) <= TOL, "NUMERICAL_FULL_PREFIX_EQUALITY")
PY|    return values, worst
PY|
PY|def product_reference(p):
PY|    t = abs(1-p)
PY|    a, b = (1+t)/2, (1-t)/2
PY|    return sorted((a**(4-x.bit_count())*b**x.bit_count()
PY|                   for x in range(N)), reverse=True)
PY|
PY|def projectors():
PY|    # Complex v+, fourteen computational vectors, then its orthogonal v-.
PY|    first = scale(outer(vec({3: O, 5: II})), F(1, 2))
PY|    last = scale(outer(vec({3: O, 5: -II})), F(1, 2))
PY|    order = [0, 15, 6] + [x for x in range(N) if x not in (0, 15, 6, 3, 5)]
PY|    pieces = [first] + [outer(vec({x: O})) for x in order] + [last]
PY|    out, Q = [], zero()
PY|    for rank, piece in enumerate(pieces, 1):
PY|        Q = add(Q, piece)
PY|        need(Q == adjoint(Q) and mm(Q, Q) == Q and trace(Q) == rank,
PY|             "ACTUAL_COMPLEX_ORTHOGONAL_PROJECTOR")
PY|        out.append(Q)
PY|    need(out[-1] == I, "COMPLETE_PROJECTOR_FLAG")
PY|    return out
PY|
PY|def mixed_accept(d2):
PY|    return d2 <= F(3, 13)
PY|
PY|def pure_accept(eta):
PY|    return eta >= F(55, 72)
PY|
PY|def arithmetic_checks(product_H):
PY|    literal = {
PY|        1: [4]+[3]*4+[2]*6+[1]*4+[0],
PY|        2: [6]+[3]*4+[1]*6+[0]*5,
PY|        3: [4]+[1]*4+[0]*11,
PY|        4: [1]+[0]*15,
PY|    }
PY|    references = {}
PY|    for j in range(1, 5):
PY|        for x in range(N):
PY|            n = 4-x.bit_count()
PY|            expected = math.comb(n, j) if n >= j else 0
PY|            need(product_H[j][x][x] == expected,
PY|                 "ACTUAL_PRODUCT_HAMMING_LAYER")
PY|            need(all(not product_H[j][x][y] for y in range(N) if y != x),
PY|                 "ACTUAL_PRODUCT_LAYER_DIAGONAL")
PY|        references[j] = sorted((rq(product_H[j][x][x])
PY|                                for x in range(N)), reverse=True)
PY|        need(references[j] == literal[j], "PRODUCT_LAYER_REFERENCE")
PY|    columns = {}
PY|    for r in (16, 13):
PY|        column = []
PY|        for k, target in ((2, 5), (3, 6), (4, 7)):
PY|            need(F(target) > F(8*k, r), "CAUCHY_INCREASING_AT_TARGET")
PY|            column.append(F(target*target, k)+F((8-target)**2, r-k))
PY|        columns[r] = column
PY|    need(columns[16] == [F(92, 7), F(160, 13), F(37, 3)],
PY|         "RANK16_CAUCHEY_BOUNDARIES")
PY|    need(columns[13] == [F(293, 22), F(62, 5), F(445, 36)],
PY|         "RANK13_CAUCHEY_BOUNDARIES")
PY|    need(min(columns[16]) == F(160, 13), "RANK16_MINIMUM")
PY|    need(min(columns[13]) == F(445, 36), "RANK13_MINIMUM")
PY|    need(10*(1+F(3, 13)) == F(160, 13), "MIXED_THRESHOLD")
PY|    need(10*(1+F(17, 72)) == F(445, 36), "PURE_THRESHOLD")
PY|    need(1-F(17, 72) == F(55, 72), "PURE_ETA_THRESHOLD")
PY|    need(F(3, 13) < F(15, 64) <= F(17, 72), "PURE_ONLY_STATE_REGION")
PY|    need(F(17, 72) < F(1, 4), "PURE_REGION_H2_COMPATIBILITY")
PY|    need(F(3, 13) < F(1, 4), "MIXED_REGION_H2_COMPATIBILITY")
PY|    b0 = sorted((F(3, 4)*sum(1 if not (x >> (3-i)) & 1 else -1
PY|                             for i in range(4)) for x in range(N)),
PY|                reverse=True)
PY|    M = prefixes(b0)
PY|    L2 = prefixes(references[2])
PY|    for k in range(1, 17):
PY|        if k <= 4:
PY|            invariant = [3, 6, 9, 10][k-1]
PY|            bound = invariant+F(1, 2)*M[k-1]
PY|        elif k <= 10:
PY|            bound = k+8+F(1, 2)*M[k-1]
PY|        else:
PY|            bound = F(24)
PY|        need(bound <= L2[k-1], "H2_UNIFORM_HALF_DEFECT_TABLE")
PY|    need(mixed_accept(F(3, 13)), "MIXED_ENDPOINT_INCLUDED")
PY|    need(pure_accept(F(55, 72)), "PURE_ENDPOINT_INCLUDED")
PY|    print("EXACT_CAUCHEY_BOUNDARIES", columns)
PY|    print("EXACT_H2_TABLE_ALL16", "checked at d=1/2")
PY|    return references
PY|
PY|def make_cases():
PY|    Dv = vec({x: O for x in range(N) if x.bit_count() == 2})
PY|    yA = vec({3: II, 5: II, 6: II, 9: -II, 10: -II, 12: -II})
PY|    yB = vec({3: O+II, 5: -O, 10: -O, 12: O-II})
PY|    need(theta(Dv) == Dv and rq(dot(Dv, Dv)) == 6, "DICKE_VECTOR")
PY|    for y in (yA, yB):
PY|        need(theta(y) == y and dot(Dv, y) == 0 and dot(y, y) == 6,
PY|             "ACTUAL_THETA_FIXED_ORTHOGONAL_Y")
PY|    vectors = [
PY|        ("pure_q15_16", vec({0: SQ15, 15: SQ15, 3: II, 12: II}), F(49, 64)),
PY|        ("pure_q1_2_outside", vec({0: O, 15: O, 3: II, 12: II}), F(0)),
PY|        ("dicke", Dv, F(1)),
PY|        ("dicke_yA", [4*x+y.rotate(1) for x, y in zip(Dv, yA)], F(225, 289)),
PY|        ("dicke_yB", [4*x+y.rotate(1) for x, y in zip(Dv, yB)], F(225, 289)),
PY|        ("coherent_eta0_old", vec({0: 3, 1: 2, 2: 2, 4: 2, 8: 2}), F(0)),
PY|    ]
PY|    cases, by_name = [], {}
PY|    for name, vector, expected_eta in vectors:
PY|        rho, eta = pure(vector)
PY|        need(eta == expected_eta, "EXACT_SELECTED_PURE_ETA")
PY|        case = dict(name=name, rho=rho, pure=True, eta=eta, d2=1-eta)
PY|        cases.append(case)
PY|        by_name[name] = case
PY|    product, product_eta = pure(vec({0: O}))
PY|    need(product_eta == 0, "PRODUCT_BASE_DEFECT")
PY|    white = scale(I, F(1, 16))
PY|    B, D = by_name["dicke_yB"]["rho"], by_name["dicke"]["rho"]
PY|    mixed = [
PY|        ("mixed_product_6_13", add(scale(white, F(7, 13)),
PY|                                   scale(product, F(6, 13))),
PY|         product, F(1), F(6, 13)),
PY|        ("mixed_product_1_2_H2_boundary", add(scale(white, F(1, 2)),
PY|                                             scale(product, F(1, 2))),
PY|         product, F(1), F(1, 2)),
PY|        ("mixed_complex_B_white", add(scale(B, F(3, 4)), scale(white, F(1, 4))),
PY|         B, F(64, 289), F(3, 4)),
PY|        ("mixed_complex_B_D", add(scale(B, F(3, 4)), scale(D, F(1, 4))),
PY|         B, F(64, 289), F(3, 4)),
PY|        ("white_rank16", white, product, F(1), F(0)),
PY|    ]
PY|    for name, rho, base, base_d2, factor in mixed:
PY|        delta = scale(sub(rho, spin(rho)), F(1, 2))
PY|        base_delta = scale(sub(base, spin(base)), F(1, 2))
PY|        need(delta == scale(base_delta, factor), "EXACT_MIXED_DEFECT_SCALING")
PY|        case = dict(name=name, rho=rho, pure=False, eta=None,
PY|                    d2=factor*factor*base_d2)
PY|        cases.append(case)
PY|        by_name[name] = case
PY|    need(B[3][5] == E(F(11, 102), c=F(7, 102)),
PY|         "COMPLEX_PAIR_COHERENCE")
PY|    M = by_name["mixed_complex_B_white"]["rho"]
PY|    need(M[3][5] == E(F(11, 136), c=F(7, 136)),
PY|         "MIXED_COMPLEX_COHERENCE")
PY|    for site in range(4):
PY|        single = lifted_marginal(M, (site,))
PY|        need(all(not single[x][y] for x in range(N) for y in range(N) if x != y),
PY|             "MIXED_ONE_SITE_MARGINAL_DIAGONAL")
PY|    need(bool(M[3][5]), "MIXED_NONPRODUCT_DISCRIMINATOR")
PY|    return cases, by_name, product
PY|
PY|def audit_case(case, references, Qs, product):
PY|    global CHANNEL_CASES
PY|    tick()
PY|    name, rho, d2 = case["name"], case["rho"], case["d2"]
PY|    need(rho == adjoint(rho) and trace(rho) == 1, "DENSITY_HERMITIAN_TRACE")
PY|    sigma = scale(add(rho, spin(rho)), F(1, 2))
PY|    delta = sub(rho, sigma)
PY|    need(spin(sigma) == sigma, "ACTUAL_SIGMA_INVARIANT")
PY|    need(delta == scale(sub(rho, spin(rho)), F(1, 2)), "ACTUAL_DEFECT_HALF")
PY|    H = layers(rho)
PY|    G = layers(sigma)
PY|    R, S = pauli_layers(rho)
PY|    need(rho == scale(add(I, *R[1:]), F(1, 16)), "ALL_FOUR_PAULI_SECTORS")
PY|    need(sigma == scale(add(I, R[2], R[4]), F(1, 16)),
PY|         "SAME_STATE_EVEN_PART")
PY|    need(delta == scale(add(R[1], R[3]), F(1, 16)), "SAME_STATE_ODD_PART")
PY|    need(H[1] == add(scale(I, 2), scale(R[1], F(1, 2))), "H1_PAULI_IDENTITY")
PY|    need(H[2] == scale(add(scale(I, 6), scale(R[1], 3), R[2]), F(1, 4)),
PY|         "H2_PAULI_IDENTITY")
PY|    need(H[3] == scale(add(scale(I, 4), scale(R[1], 3),
PY|                           scale(R[2], 2), R[3]), F(1, 8)), "H3_PAULI_IDENTITY")
PY|    need(H[4] == rho, "H4_ACTUAL_DENSITY")
PY|    error_sum = add(*(conjugate_pauli(rho, P) for group in LOCAL for P in group))
PY|    need(H[3] == add(scale(rho, 2), scale(error_sum, F(1, 2))),
PY|         "H3_PHYSICAL_TWELVE_ERRORS")
PY|    need(G[1] == scale(I, 2) and G[2] == add(I, G[3]), "ACTUAL_INVARIANT_H2")
PY|    need(sub(H[2], G[2]) == scale(R[1], F(3, 4)), "ACTUAL_H2_PERTURBATION")
PY|    need(sub(H[3], G[3]) == scale(add(scale(R[1], 3), R[3]), F(1, 8)),
PY|         "ACTUAL_H3_PERTURBATION")
PY|    need([rq(trace(H[j])) for j in range(1, 5)] == [32, 24, 8, 1],
PY|         "ALL_LAYER_TRACES")
PY|    moment = rq(trprod(H[3], H[3]))
PY|    sigma_moment = rq(trprod(G[3], G[3]))
PY|    need(moment == 4+F(9*S[1]+4*S[2]+S[3], 4), "GENERAL_H3_MOMENT")
PY|    need(moment == sigma_moment+F(9*S[1]+S[3], 4), "EVEN_ODD_MOMENT_SPLIT")
PY|    need(sigma_moment <= 10, "INVARIANT_MOMENT_CAP")
PY|    need(S[1] <= 4*d2 and S[1]+S[3] <= 8*d2, "ACTUAL_DEFECT_PAULI_BOUNDS")
PY|    need(moment <= 10*(1+d2), "MIXED_DEFECT_MOMENT_BOUND")
PY|    need(rq(trprod(delta, delta)) <= d2/2, "TRACELESS_DEFECT_HS_BOUND")
PY|    if case["pure"]:
PY|        eta = case["eta"]
PY|        need(moment == 8+3*S[1]+2*eta, "PURE_MOMENT_2ETA")
PY|        need(S[1]+S[3] == 8*(1-eta), "PURE_ODD_PURITY")
PY|        need(2*S[2]+S[3] == 12+S[1], "PURE_COMPLEMENTARY_PURITY")
PY|    defect_values = eigenvalues(delta)
PY|    actual_d = sum(abs(x) for x in defect_values)
PY|    need(abs(actual_d*actual_d-float(d2)) <= TOL, "ACTUAL_TRACE_NORM_DEFECT")
PY|    required = mixed_accept(d2) or (
PY|        case["pure"] and pure_accept(case["eta"])) or name == "coherent_eta0_old"
PY|    h2_required = d2 <= F(1, 4) or name == "coherent_eta0_old"
PY|    h3_required = moment <= F(160, 13) or (
PY|        case["pure"] and moment <= F(445, 36)) or name == "coherent_eta0_old"
PY|    layer_values = {}
PY|    for j, flag in ((1, True), (2, h2_required), (3, h3_required), (4, True)):
PY|        values, _ = spectral_prefixes(H[j], references[j], flag,
PY|                                      "NUMERICAL_H%d_PREFIX" % j)
PY|        layer_values[j] = values
PY|        need(values[-1] >= -TOL, "NUMERICAL_LAYER_POSITIVITY")
PY|    need(layer_values[3][0] <= 4+TOL, "NUMERICAL_H3_OPERATOR_CAP")
PY|    if case["pure"]:
PY|        need(sum(x > 1e-8 for x in layer_values[3]) <= 13,
PY|             "NUMERICAL_PURE_H3_RANK")
PY|    invariant_values = eigenvalues(G[3])
PY|    need(invariant_values[0] <= 2+TOL and sum(invariant_values[:4]) <= 6+TOL,
PY|         "NUMERICAL_ACTUAL_SIGMA_SHARP_REFERENCE")
PY|    layer_prefixes = {j: prefixes(references[j]) for j in references}
PY|    worst_output = -float("inf")
PY|    for p in (F(0), F(1, 3), F(1, 2), F(2, 3), F(1), F(7, 6), F(4, 3)):
PY|        tick()
PY|        output = channel_pauli(rho, p)
PY|        need(output == channel_erasure(rho, H, p), "PAULI_VS_ERASURE_CHANNEL")
PY|        need(output == adjoint(output) and trace(output) == 1,
PY|             "ACTUAL_CHANNEL_HERMITIAN_TRACE")
PY|        reference = product_reference(p)
PY|        reference_output = channel_pauli(product, p)
PY|        need(all(not reference_output[x][y] for x in range(N)
PY|                 for y in range(N) if x != y), "PRODUCT_CHANNEL_DIAGONAL")
PY|        need(sorted((rq(reference_output[x][x]) for x in range(N)),
PY|                    reverse=True) == reference, "ACTUAL_PRODUCT_CHANNEL_SPECTRUM")
PY|        t, b = abs(1-p), (1-abs(1-p))/2
PY|        positive = channel_pauli(rho, 1-t)
PY|        need(positive == add(scale(rho, t**4), scale(H[3], t**3*b),
PY|                             scale(H[2], t*t*b*b), scale(H[1], t*b**3),
PY|                             scale(I, b**4)), "POSITIVE_RETENTION_EXPANSION")
PY|        ref_prefix = prefixes(reference)
PY|        for k, Q in enumerate(Qs, 1):
PY|            exact_reference = (t**4+t**3*b*layer_prefixes[3][k-1]
PY|                               +t*t*b*b*layer_prefixes[2][k-1]
PY|                               +t*b**3*layer_prefixes[1][k-1]+k*b**4)
PY|            need(exact_reference == ref_prefix[k-1], "EXACT_COORDERED_REFERENCE")
PY|            actual_terms = (trprod(Q, rho)*t**4+trprod(Q, H[3])*t**3*b
PY|                            +trprod(Q, H[2])*t*t*b*b
PY|                            +trprod(Q, H[1])*t*b**3+E(k*b**4))
PY|            need(trprod(Q, positive) == actual_terms, "ONE_COMMON_Q_EXPANSION")
PY|            if required:
PY|                for j in (1, 2, 3, 4):
PY|                    need(rq(trprod(Q, H[j])) <= layer_prefixes[j][k-1],
PY|                         "EXACT_SELECTED_COMMON_Q_LAYER")
PY|                need(rq(trprod(Q, positive)) <= ref_prefix[k-1],
PY|                     "EXACT_SELECTED_COMMON_Q_OUTPUT")
PY|            if p > 1:
PY|                need(output == spin(positive), "FULL_TRANSPOSE_OUTPUT_IDENTITY")
PY|                transported = spin(Q)
PY|                need(transported == adjoint(transported)
PY|                     and mm(transported, transported) == transported
PY|                     and trace(transported) == k, "FULL_TRANSPOSE_PROJECTOR")
PY|                need(trprod(Q, output) == trprod(transported, positive),
PY|                     "FULL_TRANSPOSE_COMMON_Q_EXPECTATION")
PY|        values, worst = spectral_prefixes(output, reference, required,
PY|                                          "NUMERICAL_OUTPUT_PREFIX", True)
PY|        need(values[-1] >= -TOL, "NUMERICAL_OUTPUT_POSITIVITY")
PY|        worst_output = max(worst_output, worst)
PY|        CHANNEL_CASES += 1
PY|    print("EXACT_CASE", name, "eta", case["eta"], "d_squared", d2,
PY|          "S1", S[1], "TrH3_squared", moment,
PY|          "new_or_old_scoped", required)
PY|    print("NUMERICAL_CASE", name, "trace_norm_defect", actual_d,
PY|          "maximum_sampled_output_prefix_excess", worst_output,
PY|          "tolerance", TOL,
PY|          "classification", "SCOPED" if required else "OUTSIDE_REGION_DIAGNOSTIC")
PY|    case.update(H=H, sigma=sigma, moment=moment, S1=S[1], numerical_d=actual_d)
PY|
PY|def mutation_checks(by_name, Qs, product):
PY|    q = by_name["pure_q15_16"]
PY|    B = by_name["dicke_yB"]
PY|    need(q["S1"] == 0 and q["moment"] == F(305, 32),
PY|         "Q15_EXACT_MOMENT_VALUE")
PY|    need(B["S1"] == F(256, 2601) and B["moment"] == F(8542, 867),
PY|         "COMPLEX_DICKE_EXACT_MOMENT_VALUE")
PY|    expect_rejection("DEFECT_HALF_FACTOR",
PY|        lambda: need(abs((2*q["numerical_d"])**2-float(q["d2"])) <= TOL,
PY|                     "DEFECT_HALF_FACTOR"))
PY|    expect_rejection("PURE_MOMENT_2ETA",
PY|        lambda: need(q["moment"] == 8+3*q["S1"], "PURE_MOMENT_2ETA"))
PY|    expect_rejection("SIGMA_IS_ACTUAL_AVERAGE",
PY|        lambda: need(scale(I, F(1, 16)) == B["sigma"],
PY|                     "SIGMA_IS_ACTUAL_AVERAGE"))
PY|    p = F(4, 3)
PY|    positive = channel_pauli(B["rho"], F(2, 3))
PY|    negative = channel_pauli(B["rho"], p)
PY|    Q = Qs[0]
PY|    correct = rq(trprod(Q, negative))
PY|    transported = rq(trprod(spin(Q), positive))
PY|    wrong = rq(trprod(conjugate_W(Q), positive))
PY|    need(correct == transported == F(77, 972), "COMPLEX_Q_CORRECT_VALUE")
PY|    need(wrong == F(1193, 16524) and correct-wrong == F(29, 4131),
PY|         "COMPLEX_Q_TRANSPOSE_DISCRIMINATOR")
PY|    expect_rejection("FULL_TRANSPOSE_COMPLEX_Q",
PY|        lambda: need(correct == wrong, "FULL_TRANSPOSE_COMPLEX_Q"))
PY|    p = F(1, 2)
PY|    actual_prefix = prefixes(product_reference(p))[1]
PY|    relaxed_prefix = actual_prefix+F(3, 32)
PY|    expect_rejection("REFERENCE_IS_ACTUAL_PRODUCT",
PY|        lambda: need(relaxed_prefix == actual_prefix,
PY|                     "REFERENCE_IS_ACTUAL_PRODUCT"))
PY|    expect_rejection("MIXED_ENDPOINT_INCLUDED",
PY|        lambda: need(F(3, 13) < F(3, 13), "MIXED_ENDPOINT_INCLUDED"))
PY|    expect_rejection("PURE_ENDPOINT_INCLUDED",
PY|        lambda: need(F(55, 72) > F(55, 72), "PURE_ENDPOINT_INCLUDED"))
PY|    expect_rejection("PURE_BAND_NOT_MIXED",
PY|        lambda: need(not (q["d2"] <= F(17, 72)), "PURE_BAND_NOT_MIXED"))
PY|    white_H3 = by_name["white_rank16"]["H"][3]
PY|    need(white_H3 == scale(I, F(1, 2)), "EXACT_MIXED_RANK16_CONTROL")
PY|    def rank_scope(is_pure, proposed_cap):
PY|        need(is_pure or proposed_cap == 16, "PURE_RANK_SCOPE")
PY|    rank_scope(True, 13)
PY|    rank_scope(False, 16)
PY|    expect_rejection("PURE_RANK_SCOPE", lambda: rank_scope(False, 13))
PY|    ghz_plus, ep = pure(vec({0: O, 15: O}))
PY|    ghz_minus, em = pure(vec({0: O, 15: -O}))
PY|    need(ep == em == 1, "GHZ_COMPONENTS_IN_PURE_REGION")
PY|    mixture = scale(add(ghz_plus, ghz_minus), F(1, 2))
PY|    separable = scale(add(outer(vec({0: O})), outer(vec({15: O}))), F(1, 2))
PY|    need(mixture == separable, "EXACT_SEPARABLE_MIXTURE_DECOMPOSITION")
PY|    expect_rejection("MIXTURE_GME_SCOPE",
PY|        lambda: need(mixture != separable, "MIXTURE_GME_SCOPE"))
PY|    print("EXACT_TRANSPOSE_EXPECTATIONS", correct, wrong, correct-wrong)
PY|    print("SCOPE_CONTROLS",
PY|          "endpoint, threshold, rank and GME controls are not channel counterexamples")
PY|
PY|def main():
PY|    global DEADLINE
PY|    parser = argparse.ArgumentParser(description=__doc__)
PY|    parser.add_argument("--seconds", type=float, default=55.0)
PY|    args = parser.parse_args()
PY|    if not math.isfinite(args.seconds) or not 1 <= args.seconds <= 55:
PY|        parser.error("--seconds must be finite and between 1 and 55")
PY|    start = time.perf_counter()
PY|    DEADLINE = start+max(0.1, args.seconds-0.75)
PY|    try:
PY|        print("ASSURANCE", "exact field Q(sqrt(15),i); spectra NUMERICAL")
PY|        print("LIMITS", "finite selected states and parameters; no universal numerical proof")
PY|        cases, by_name, product = make_cases()
PY|        references = arithmetic_checks(layers(product))
PY|        Qs = projectors()
PY|        for case in cases:
PY|            audit_case(case, references, Qs, product)
PY|        mutation_checks(by_name, Qs, product)
PY|        need(len(cases) == 11 and CHANNEL_CASES == 77
PY|             and PREFIX_COMPARISONS == 1232, "COMPLETE_DESIGNED_COVERAGE")
PY|        tick()
PY|        print("NUMERICAL_RESIDUALS",
PY|              "eigenpair_frobenius", MAX_RESIDUAL,
PY|              "orthogonality_entrywise", MAX_ORTHOGONALITY,
PY|              "offdiagonal_row", MAX_ROW_RESIDUAL)
PY|        print("COUNTS", "exact_or_numeric_checks", CHECKS, "spectra", SPECTRA,
PY|              "channel_cases", CHANNEL_CASES, "output_prefixes", PREFIX_COMPARISONS)
PY|        print("ELAPSED_SECONDS", time.perf_counter()-start)
PY|        print("RESULT", "FINITE_CHECK_COMPLETE",
PY|              "exact identities and selected expectations checked;",
PY|              "spectral conclusions NUMERICAL only; no unrestricted theorem")
PY|        return 0
PY|    except Incomplete as exc:
PY|        print("RESULT", "INCOMPLETE", str(exc),
PY|              "completed_channel_cases", CHANNEL_CASES,
PY|              "completed_output_prefixes", PREFIX_COMPARISONS)
PY|        return 2
PY|    except CheckFailure as exc:
PY|        print("RESULT", "FAIL", exc.reason)
PY|        return 1
PY|
PY|if __name__ == "__main__":
PY|    sys.exit(main())

## 6. Disposition limits

- **Observed execution:** none.
- **Prepared implementation:** complete source and argv above.
- **Written result:** exact selected-state arithmetic, independent threshold/table reconstruction and a discriminating complex-\(Q\) transpose control.
- **Finite numerical corroboration:** NOT PERFORMED.
- **Universal written theorem:** no defect identified at the frozen sufficient-region scope; still conditional on the imported invariant-sector interface.
- **Unrestricted four-qubit closure, novelty, independent-model-family, human and formal-kernel verification:** not claimed.

Overall correctness: **correct**.

Explanation: No defect was identified in the frozen scoped written argument. This is a complete source-only FINITE return, not an executed finite verification or a mathematical acceptance disposition.

Confidence: **0.90** for the scoped written assessment; no executed-code assurance is claimed.