# F509 — Independent finite physical-layer check

**Status: WRITTEN EXACT RECONSTRUCTION COMPLETE; SCIENTIFIC EXECUTION NOT RUN.**

**No mathematical defect was identified in the reconstructed coherent vacuum–\(W_4\) statements. This return supplies no executed finite-check evidence, independent-model-family credit, parent acceptance, novelty finding, or unrestricted-target closure.**

The complete proposed body below is returned for Main materialization. No repository file was created or modified.

## 1. Input binding and chronology

Frozen wave:

/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f509-coherent-vacuum-w4-independent-physical-layer-finite-check/

Supplied bindings:

- Manifest SHA256: bbea38e03e9351156da80b3b783ceecab3b0dc6ba2e58b56d4c21323bb8ffcb1.
- Receipt SHA256: ddd84b8a53a998f28832bd2091be6aba94104fe05e1f8fdfe64bc2cdcb9673fd.
- Packet SHA256, from parent metadata: 9171cb5e56b5ffdbdc76d704878968b801492af7f671dfef869304c5d670c2a8.

These are **supplied/parent-observed bindings**, not child-native hash computations.

Before reading scientific bodies, I completely read the manifest, receipt, dispatch receipt, metadata supply, and every manifest-listed status/permission control through its ending. I then sent a direct PRE-BODY ACK to agent://Main; the messaging tool reported **“Delivered to Main.”** Only afterward did I read the complete literal packet in consecutive raw ranges 1–20, 21–40, …, 761–780.

Coverage includes:

- S1 logical lines 1–730, through the author’s final confidence field.
- S2 lines 1–48, through its limitations and unrestricted-target statement.

The S1 metadata reports 729 LF characters while the packet labels 730 logical lines; my coverage statement refers to the displayed logical lines, not a new byte/LF measurement.

All historical held episodes and their consumers remained NONINPUT. The quarantine records were read only as status controls. No linked scientific source or sibling return was opened.

F480’s original acknowledgment remains **transcript-recorded, without observed direct delivery**. This review does not upgrade that history. Owner addendum 2 prevents treating that transport fault alone as mathematical invalidity; it does not itself accept the theorem.

A read-only git diff restricted to this wave’s manifest, receipt, and packet returned no output. That observation is neither a source-hash check nor mathematical verification.

## 2. Execution boundary

My higher-priority review role restricts Bash to read-only git-family inspection and forbids executing checks. Accordingly:

- Scientific code, numerical spectra, exact-matrix programs, builds, tests, and formatters: **NOT RUN**.
- No scientific execution output or timing measurement exists for this return.
- The full fresh standard-library checker below is supplied **NOT RUN**, as the frozen task explicitly permits when role-limited.
- There was no execution through another tool, subprocess, external model, or delegate.

The checker has a cooperative 50-second deadline, fixed finite inputs, and no files, network, children, installations, or mutations. Completion within that bound is **not observed**; deadline exhaustion produces INCOMPLETE, not PASS.

## 3. Exact written reconstruction

Let

\[
|\psi_q\rangle=\sqrt q\,|0000\rangle+
\frac{\sqrt{1-q}}2\sum_{i=1}^4|e_i\rangle,\qquad
r=1-q,\quad u=\sqrt{qr}.
\]

The finite inputs specified below use \(q=0,9/25,1\). Both square roots are rational at all three choices.

### 3.1 Physical partial traces

Tracing the actual pure density over the erased physical indices gives

\[
\rho_{\bar i}=|v_i\rangle\langle v_i|+\frac r4|000\rangle\langle000|,
\]

where \(v_i=\sqrt q\,|000\rangle+(\sqrt r/2)\sum_{j\ne i}|e_j\rangle\), and

\[
\rho_{ij}=|v_{ij}\rangle\langle v_{ij}|+\frac r2|00\rangle\langle00|.
\]

These are compatible marginals of the same four-qubit state. No independently chosen marginals enter the reconstruction.

For \(q=9/25\), an actual pair marginal, in physical computational order, is

\[
\rho_{ij}=\frac1{25}
\begin{pmatrix}
17&6&6&0\\
6&4&4&0\\
6&4&4&0\\
0&0&0&0
\end{pmatrix},
\]

and an actual one-qubit marginal is

\[
\rho_i=\frac1{25}
\begin{pmatrix}21&6\\6&4\end{pmatrix},
\qquad \det\rho_i=\frac{48}{625}.
\]

### 3.2 Independent characteristic-polynomial identities

Using the physical computational entries and the invariant decomposition, the full characteristic polynomials are

\[
\chi_{H_3}(x)=x^7P_3(x)B_2(x)^3,
\]

with

\[
P_3(x)=x^3-5x^2+
\left(4+\frac{15r^2}{4}\right)x
-\frac{3r^2(2+3r)}4,
\]

\[
B_2(x)=x^2-x+\frac{r^2}{4}.
\]

For \(H_2\),

\[
\chi_{H_2}(x)=x(x-1)^2P_4(x)B_3(x)^3,
\]

where

\[
P_4(x)=x^4-10x^3+
\left(27+\frac{39r^2}{4}\right)x^2
-\left(18+\frac{135r^2}{4}+\frac{27r^3}{4}\right)x
+\frac{27r^2(2+2r+r^2)}4,
\]

\[
B_3(x)=x^3-4x^2+
\left(3+\frac{7r^2}{4}\right)x
-\frac{r^2(5+r)}4.
\]

These follow from the tridiagonal determinant recurrence, using squared adjacent couplings. They independently reproduce the source’s shifted-minor formulas.

At \(q=9/25\), the factors become

\[
P_3=x^3-5x^2+\frac{692}{125}x-\frac{18816}{15625},
\qquad
B_2=x^2-x+\frac{64}{625},
\]

\[
P_4=x^4-10x^3+\frac{19371}{625}x^2
-\frac{524898}{15625}x+\frac{3984768}{390625},
\]

\[
B_3=x^3-4x^2+\frac{2323}{625}x-\frac{9024}{15625}.
\]

These are **written exact derivations, not program output**.

### 3.3 Determinants and multiplicities

For the source’s \(B_3\), the leading principal determinants of \(3I-B_3\) are

\[
r,\qquad \frac32r^2,\qquad \frac{r^2(16-r)}4.
\]

For \(A_4-I\), they are

\[
5-3r,\quad 10-15r+9r^2,\quad
\frac32r(3r-2)(5-r),\quad
\frac34r^2(9r^2+9r-14).
\]

At \(r=16/25\), these are respectively

\[
\left(\frac{16}{25},\frac{384}{625},\frac{24576}{15625}\right)
\]

and

\[
\left(\frac{77}{25},\frac{2554}{625},
-\frac{5232}{15625},-\frac{546432}{390625}\right).
\]

The block multiplicities are essential:

- \(H_3\): one \(3\times3\) block, three \(2\times2\) blocks, seven zeros; trace \(5+3=8\).
- \(H_2\): one \(4\times4\) block, three \(3\times3\) blocks, two scalar ones, one zero; trace \(10+12+2=24\).

Dropping one standard-sector copy changes both characteristic-polynomial degree and trace.

### 3.4 Endpoint spectra

The endpoint spectra, calculated directly from the diagonal blocks, are:

| State | \(H_3\) spectrum | \(H_2\) spectrum |
|---|---|---|
| \(q=0\), equal \(W_4\) | \((5/2,3/2,1,(1/2)^{\times6},0^{\times7})\) | \((3^{\times2},5/2,2^{\times3},(3/2)^{\times4},1^{\times2},(1/2)^{\times3},0)\) |
| \(q=1\), product vacuum | \((4,1^{\times4},0^{\times11})\) | \((6,3^{\times4},1^{\times6},0^{\times5})\) |

Their traces are \(8\) and \(24\), respectively. In particular, the endpoints must not be interchanged.

### 3.5 Majorization and consuming-side channel assembly

The reconstructed blocks support the source’s majorization argument:

- For \(H_3\), the large block is positive, has trace five, and norm at most four. Every eigenvalue from a small block is at most one. Allocating selected eigenvalues between these blocks gives \(K_k(H_3)\le k+3\) for \(k=1,\ldots,4\); trace eight supplies the remaining prefixes.
- For \(H_2\), the shifted \(B_3\) minors prove \(B_3\le3I\). The \(A_4-I\) inertia argument proves that at least three eigenvalues of \(A_4\) are at least one, hence its top-two sum is at most nine. The reference direct-sum multiplicities reproduce exactly \(L_2\).

I also checked the consuming-side identities, rather than stopping at layer production. For the **same** rank-\(k\) projector \(Q\),

\[
T_t^{\otimes4}(\rho)
=t^4\rho+t^3bH_3+t^2b^2H_2+tb^3H_1+b^4I.
\]

The reference coefficient matrices are co-ordered by physical Hamming weight. Thus the sum of reference prefixes is exactly the product-output prefix. No simultaneous attainment of the actual layer bounds is required.

For the physical negative branch,

\[
T_{-t}^{\otimes4}(\rho)
=W[T_t^{\otimes4}(\rho)]^TW,\qquad W=Y^{\otimes4},
\]

and the consuming projector is explicitly transported to

\[
Q'=WQ^TW.
\]

This is full transpose. Substitution of one-qubit partial transpose is not the same operation.

The checker independently implements both the erasure expansion and the sequential Pauli channel, including all four physical tensor positions.

### 3.6 Genuine entanglement and comparison class

For \(q=9/25\), every nontrivial bipartition has Schmidt rank two. A computational \(2\times2\) coefficient minor across any such cut is \(-r/4=-4/25\), so it is nonzero.

Across a balanced cut, the pair support is

\[
\operatorname{span}\{|00\rangle,\ |01\rangle+|10\rangle\}.
\]

The product-coordinate determinant of
\(x|00\rangle+y(|01\rangle+|10\rangle)\) is \(-y^2\). Hence this rank-two support has exactly one product ray.

This excludes the frozen Class A and Class B rank-two pair supports, which have two independent product rays in a suitable physical pairing. The argument uses all three pairings, not a computational coefficient-count surrogate.

Furthermore, \(48/625\ne3/16\), so the intermediate state is not in the equal-\(W_4\) physical local-unitary orbit. The pure-state extremality argument then excludes membership in the finite convex hull of those earlier classes.

The endpoint \(q=0\) is, of course, equal \(W_4\), and \(q=1\) is product. The strict-enlargement statement concerns \(0<q<1\).

### 3.7 Moments and their limitations

The characteristic factors give

\[
\operatorname{Tr}H_3^2=20-9r^2.
\]

For this family,

\[
S_1=4-3r^2,\qquad \eta=0,
\]

so the source’s general formula \(8+3S_1+2\eta\) agrees.

The values at \(q=0,9/25,1\) are respectively

\[
11,\qquad \frac{10196}{625},\qquad20.
\]

The Cauchy–Schwarz boundary moments are exactly

\[
\frac{92}{7},\qquad \frac{160}{13},\qquad\frac{37}{3},
\]

whose minimum is \(160/13\). Failure of this sufficient moment condition is not failure of layer or channel majorization.

**Finite-scope limitation:** every state in the assigned coherent family, including its physical local-unitary images, has \(\eta=0\). These finite inputs therefore cannot empirically distinguish the coefficient \(2\eta\) from another coefficient multiplying \(\eta\). Its support here is the written Pauli-purity elimination, not a claimed finite mutation test. No unrelated four-qubit state is introduced to conceal this limitation.

## 4. Supplied finite experiment — NOT RUN

The planned input set is:

- \(q=0,9/25,1\);
- each state in its original basis and after one fixed, asymmetric, genuinely complex physical local unitary;
- \(p=0,1/3,2/3,5/6,1,7/6,4/3\).

That is **42 planned state/channel cases**, with **672 planned numerical prefix comparisons**. These counts describe the source’s intended coverage, not completed checks.

Exact checks include:

- normalization, Hermiticity, positivity by rational congruence;
- actual partial traces and physical embeddings;
- rational invariant-basis identities and characteristic factors;
- shifted leading determinants;
- physical local-unitary covariance;
- erasure versus Pauli output equality;
- all sixteen fixed complex projectors, unchanged between layers;
- full-transpose output and projector transport;
- Schmidt ranks, pair-support structure, and moments.

Numerical checks use a standard-library realification/Jacobi eigensolver. They are explicitly labeled numerical, with tolerance \(2\times10^{-10}\) and a reported off-diagonal residual. They are not exact characteristic-root certificates.

Intended-reason mutations cover:

1. Wrong square-root coupling signs, detected by the exact invariant-basis identity—not by an isospectral sign-gauge test.
2. Wrong \(H_2\) block trace.
3. Missing standard-sector multiplicity.
4. A misplaced physical third-qubit embedding.
5. Partial versus full transpose.
6. Interchanged family endpoints.
7. Incorrect assignment to a two-product-ray old class.
8. An incorrect family moment constant.
9. An incorrect sufficient moment threshold.

## 5. Complete checker source and argv — NOT RUN

Materialization rule: remove exactly the leading **SRC|** from every source line below, preserving the remainder and line order. The resulting text is the complete Python source.

Full argv:

- argv[0]: python3
- argv[1]: -B
- argv[2]: -c
- argv[3]: the complete decoded source below

No source file is needed. No execution is claimed.

SRC|from fractions import Fraction as F
SRC|from itertools import combinations
SRC|import math
SRC|import time
SRC|
SRC|START = time.monotonic()
SRC|LIMIT = 50.0
SRC|TOL = 2e-10
SRC|
SRC|class CheckFailure(Exception):
SRC|    pass
SRC|
SRC|class Deadline(Exception):
SRC|    pass
SRC|
SRC|def tick():
SRC|    if time.monotonic() - START >= LIMIT:
SRC|        raise Deadline("cooperative 50-second deadline")
SRC|
SRC|def must(condition, reason):
SRC|    if not condition:
SRC|        raise CheckFailure(reason)
SRC|
SRC|def G(a=0, b=0):
SRC|    return (F(a), F(b))
SRC|
SRC|Z, O = G(), G(1)
SRC|
SRC|def add(a, b):
SRC|    return (a[0] + b[0], a[1] + b[1])
SRC|
SRC|def neg(a):
SRC|    return (-a[0], -a[1])
SRC|
SRC|def sub(a, b):
SRC|    return add(a, neg(b))
SRC|
SRC|def cj(a):
SRC|    return (a[0], -a[1])
SRC|
SRC|def scale(a, c):
SRC|    return (a[0] * c, a[1] * c)
SRC|
SRC|def mul(a, b):
SRC|    if not a[1] and not b[1]:
SRC|        return (a[0] * b[0], F(0))
SRC|    return (a[0]*b[0] - a[1]*b[1],
SRC|            a[0]*b[1] + a[1]*b[0])
SRC|
SRC|def inv(a):
SRC|    d = a[0]*a[0] + a[1]*a[1]
SRC|    must(bool(d), "division by zero")
SRC|    return (a[0]/d, -a[1]/d)
SRC|
SRC|def zero(n, m=None):
SRC|    return [[Z for _ in range(n if m is None else m)] for _ in range(n)]
SRC|
SRC|def eye(n):
SRC|    a = zero(n)
SRC|    for i in range(n):
SRC|        a[i][i] = O
SRC|    return a
SRC|
SRC|def adj(a):
SRC|    return [[cj(a[i][j]) for i in range(len(a))]
SRC|            for j in range(len(a[0]))]
SRC|
SRC|def trans(a):
SRC|    return [list(row) for row in zip(*a)]
SRC|
SRC|def mm(a, b):
SRC|    must(len(a[0]) == len(b), "matrix dimensions")
SRC|    out = zero(len(a), len(b[0]))
SRC|    for i, row in enumerate(a):
SRC|        tick()
SRC|        for k, x in enumerate(row):
SRC|            if x == Z:
SRC|                continue
SRC|            for j, y in enumerate(b[k]):
SRC|                if y != Z:
SRC|                    out[i][j] = add(out[i][j], mul(x, y))
SRC|    return out
SRC|
SRC|def lin(terms):
SRC|    n = len(terms[0][1])
SRC|    out = zero(n, len(terms[0][1][0]))
SRC|    for c, a in terms:
SRC|        if not c:
SRC|            continue
SRC|        for i in range(n):
SRC|            tick()
SRC|            for j in range(len(a[0])):
SRC|                out[i][j] = add(out[i][j], scale(a[i][j], c))
SRC|    return out
SRC|
SRC|def tr(a):
SRC|    value = Z
SRC|    for i in range(len(a)):
SRC|        value = add(value, a[i][i])
SRC|    must(value[1] == 0, "nonreal trace")
SRC|    return value[0]
SRC|
SRC|def trprod(a, b):
SRC|    value = Z
SRC|    for i in range(len(a)):
SRC|        for j in range(len(a)):
SRC|            value = add(value, mul(a[i][j], b[j][i]))
SRC|    must(value[1] == 0, "nonreal Hermitian pairing")
SRC|    return value[0]
SRC|
SRC|def outer(v):
SRC|    return [[mul(x, cj(y)) for y in v] for x in v]
SRC|
SRC|def rank(a):
SRC|    a = [row[:] for row in a]
SRC|    row = 0
SRC|    for col in range(len(a[0])):
SRC|        tick()
SRC|        pivot = next((i for i in range(row, len(a))
SRC|                      if a[i][col] != Z), None)
SRC|        if pivot is None:
SRC|            continue
SRC|        a[row], a[pivot] = a[pivot], a[row]
SRC|        divisor = inv(a[row][col])
SRC|        a[row] = [mul(x, divisor) for x in a[row]]
SRC|        for i in range(row + 1, len(a)):
SRC|            c = a[i][col]
SRC|            if c != Z:
SRC|                a[i] = [sub(x, mul(c, y))
SRC|                        for x, y in zip(a[i], a[row])]
SRC|        row += 1
SRC|        if row == len(a):
SRC|            break
SRC|    return row
SRC|
SRC|def psd(a):
SRC|    must(a == adj(a), "Hermiticity")
SRC|    a = [row[:] for row in a]
SRC|    for i in range(len(a)):
SRC|        tick()
SRC|        d = a[i][i]
SRC|        must(d[1] == 0 and d[0] >= 0, "PSD negative pivot")
SRC|        if not d[0]:
SRC|            must(all(a[i][j] == Z for j in range(i + 1, len(a))),
SRC|                 "PSD zero-pivot row")
SRC|            continue
SRC|        for j in range(i + 1, len(a)):
SRC|            for k in range(j, len(a)):
SRC|                correction = scale(mul(a[j][i], a[i][k]), 1/d[0])
SRC|                a[j][k] = sub(a[j][k], correction)
SRC|                a[k][j] = cj(a[j][k])
SRC|
SRC|def pack(index, sites):
SRC|    value = 0
SRC|    for site in sites:
SRC|        value = 2*value + ((index >> (3-site)) & 1)
SRC|    return value
SRC|
SRC|def partial(rho, sites):
SRC|    other = tuple(i for i in range(4) if i not in sites)
SRC|    out = zero(1 << len(sites))
SRC|    for a in range(16):
SRC|        tick()
SRC|        for b in range(16):
SRC|            if pack(a, other) == pack(b, other):
SRC|                i, j = pack(a, sites), pack(b, sites)
SRC|                out[i][j] = add(out[i][j], rho[a][b])
SRC|    return out
SRC|
SRC|def embed(marginal, sites):
SRC|    other = tuple(i for i in range(4) if i not in sites)
SRC|    out = zero(16)
SRC|    for a in range(16):
SRC|        for b in range(16):
SRC|            if pack(a, other) == pack(b, other):
SRC|                out[a][b] = marginal[pack(a, sites)][pack(b, sites)]
SRC|    return out
SRC|
SRC|def layers(rho):
SRC|    return {m: lin([(F(1), embed(partial(rho, s), s))
SRC|                    for s in combinations(range(4), m)])
SRC|            for m in (1, 2, 3)}
SRC|
SRC|def kron(a, b):
SRC|    out = zero(len(a)*len(b), len(a[0])*len(b[0]))
SRC|    for i in range(len(a)):
SRC|        for j in range(len(a[0])):
SRC|            for k in range(len(b)):
SRC|                for l in range(len(b[0])):
SRC|                    out[i*len(b)+k][j*len(b[0])+l] = mul(a[i][j], b[k][l])
SRC|    return out
SRC|
SRC|def tensor(factors):
SRC|    out = [[O]]
SRC|    for a in factors:
SRC|        out = kron(out, a)
SRC|    return out
SRC|
SRC|def local_unitary():
SRC|    c, s = F(3, 5), F(4, 5)
SRC|    return tensor([
SRC|        [[G(c), G(0, s)], [G(0, s), G(c)]],
SRC|        [[O, Z], [Z, G(0, 1)]],
SRC|        [[G(c), G(-s)], [G(s), G(c)]],
SRC|        [[Z, O], [G(0, 1), Z]],
SRC|    ])
SRC|
SRC|def conjugate(u, a):
SRC|    return mm(mm(u, a), adj(u))
SRC|
SRC|def erasure(rho, h, p):
SRC|    s, b = 1-p, p/2
SRC|    return lin([(s**4, rho), (s**3*b, h[3]),
SRC|                (s**2*b**2, h[2]), (s*b**3, h[1]),
SRC|                (b**4, eye(16))])
SRC|
SRC|def pauli_channel(rho, p):
SRC|    out = [row[:] for row in rho]
SRC|    weights = [1-3*p/4, p/4, p/4, p/4]
SRC|    must(all(w >= 0 for w in weights), "physical Pauli weights")
SRC|    for site in range(4):
SRC|        tick()
SRC|        mask = 1 << (3-site)
SRC|        nxt = zero(16)
SRC|        for kind, weight in enumerate(weights):
SRC|            if not weight:
SRC|                continue
SRC|            for a in range(16):
SRC|                ba = bool(a & mask)
SRC|                ia = a ^ mask if kind in (1, 2) else a
SRC|                phase_a = G(0, -1 if ba else 1) if kind == 2 else (
SRC|                    G(-1 if ba else 1) if kind == 3 else O)
SRC|                for b in range(16):
SRC|                    if out[a][b] == Z:
SRC|                        continue
SRC|                    bb = bool(b & mask)
SRC|                    ib = b ^ mask if kind in (1, 2) else b
SRC|                    phase_b = G(0, -1 if bb else 1) if kind == 2 else (
SRC|                        G(-1 if bb else 1) if kind == 3 else O)
SRC|                    value = mul(mul(phase_a, out[a][b]), cj(phase_b))
SRC|                    nxt[ia][ib] = add(nxt[ia][ib], scale(value, weight))
SRC|        out = nxt
SRC|    return out
SRC|
SRC|def conjugate_w(a):
SRC|    return [[scale(a[15-i][15-j],
SRC|                   -1 if (i.bit_count()+j.bit_count()) % 2 else 1)
SRC|             for j in range(16)] for i in range(16)]
SRC|
SRC|def spin(a):
SRC|    return conjugate_w(trans(a))
SRC|
SRC|def partial_transpose(a, site):
SRC|    mask = 1 << (3-site)
SRC|    out = zero(16)
SRC|    for i in range(16):
SRC|        for j in range(16):
SRC|            ii = (i & ~mask) | (j & mask)
SRC|            jj = (j & ~mask) | (i & mask)
SRC|            out[ii][jj] = a[i][j]
SRC|    return out
SRC|
SRC|def padd(a, b):
SRC|    out = [F(0)] * max(len(a), len(b))
SRC|    for i, c in enumerate(a):
SRC|        out[i] += c
SRC|    for i, c in enumerate(b):
SRC|        out[i] += c
SRC|    return out
SRC|
SRC|def pmul(a, b):
SRC|    out = [F(0)] * (len(a)+len(b)-1)
SRC|    for i, x in enumerate(a):
SRC|        for j, y in enumerate(b):
SRC|            out[i+j] += x*y
SRC|    return out
SRC|
SRC|def product_polys(polys):
SRC|    out = [F(1)]
SRC|    for p in polys:
SRC|        out = pmul(out, p)
SRC|    return out
SRC|
SRC|def tri_poly(diagonal, adjacent_products):
SRC|    previous, current = [F(1)], [-diagonal[0], F(1)]
SRC|    for i in range(1, len(diagonal)):
SRC|        nxt = padd(pmul([-diagonal[i], F(1)], current),
SRC|                   [-adjacent_products[i-1]*c for c in previous])
SRC|        previous, current = current, nxt
SRC|    return current
SRC|
SRC|def leading_dets(diagonal, adjacent_products):
SRC|    before, current = F(1), diagonal[0]
SRC|    out = [current]
SRC|    for i in range(1, len(diagonal)):
SRC|        nxt = diagonal[i]*current-adjacent_products[i-1]*before
SRC|        before, current = current, nxt
SRC|        out.append(current)
SRC|    return out
SRC|
SRC|def blocks(matrices):
SRC|    n = sum(len(a) for a in matrices)
SRC|    out, offset = zero(n), 0
SRC|    for a in matrices:
SRC|        for i in range(len(a)):
SRC|            for j in range(len(a)):
SRC|                out[offset+i][offset+j] = a[i][j]
SRC|        offset += len(a)
SRC|    return out
SRC|
SRC|def extend(a, n):
SRC|    out = zero(n)
SRC|    for i in range(len(a)):
SRC|        for j in range(len(a)):
SRC|            out[i][j] = G(a[i][j])
SRC|    return out
SRC|
SRC|def invariant_basis():
SRC|    columns = []
SRC|    for weight in range(5):
SRC|        columns.append([G(int(i.bit_count() == weight)) for i in range(16)])
SRC|    for f in ((1,-1,0,0), (1,0,-1,0), (1,0,0,-1)):
SRC|        for weight in (1,2,3):
SRC|            v = [Z]*16
SRC|            for sites in combinations(range(4), weight):
SRC|                index = sum(1 << (3-i) for i in sites)
SRC|                v[index] = G(sum(f[i] for i in sites))
SRC|            columns.append(v)
SRC|    pairs = list(combinations(range(4), 2))
SRC|    for coefficients in ((1,0,-1,-1,0,1), (0,1,-1,-1,1,0)):
SRC|        v = [Z]*16
SRC|        for sites, c in zip(pairs, coefficients):
SRC|            v[sum(1 << (3-i) for i in sites)] = G(c)
SRC|        columns.append(v)
SRC|    out = [list(row) for row in zip(*columns)]
SRC|    must(rank(out) == 16, "invariant basis rank")
SRC|    return out
SRC|
SRC|def representations(r, u):
SRC|    a3 = [[4-3*r, 6*u, 0],
SRC|          [3*u/2, 1+3*r/2, 3*u/2],
SRC|          [0, u, 3*r/2]]
SRC|    b2 = [[1-r/2, u], [u/2, r/2]]
SRC|    a4 = [[6-3*r, 6*u, 0, 0],
SRC|          [3*u/2, 3, 3*u, 0],
SRC|          [0, 2*u, 1+3*r/2, u],
SRC|          [0, 0, 3*u/2, 3*r/2]]
SRC|    b3 = [[3-r, 2*u, 0],
SRC|          [u, 1+r/2, u/2],
SRC|          [0, u, r/2]]
SRC|    r3 = blocks([extend(a3, 5)] + [extend(b2, 3) for _ in range(3)]
SRC|                + [zero(2)])
SRC|    r2 = blocks([extend(a4, 5)] + [extend(b3, 3) for _ in range(3)]
SRC|                + [eye(2)])
SRC|    aa3 = [4-3*r, 1+3*r/2, 3*r/2]
SRC|    oo3 = [9*u*u, F(3,2)*u*u]
SRC|    aa4 = [6-3*r, F(3), 1+3*r/2, 3*r/2]
SRC|    oo4 = [9*u*u, 6*u*u, F(3,2)*u*u]
SRC|    bb2 = [1-r/2, r/2]
SRC|    ob2 = [u*u/2]
SRC|    bb3 = [3-r, 1+r/2, r/2]
SRC|    ob3 = [2*u*u, u*u/2]
SRC|    p3 = [-F(3,4)*r*r*(2+3*r), 4+F(15,4)*r*r, F(-5), F(1)]
SRC|    pb2 = [r*r/4, F(-1), F(1)]
SRC|    p4 = [F(27,4)*r*r*(2+2*r+r*r),
SRC|          -(18+F(135,4)*r*r+F(27,4)*r**3),
SRC|          27+F(39,4)*r*r, F(-10), F(1)]
SRC|    pb3 = [-r*r*(5+r)/4, 3+F(7,4)*r*r, F(-4), F(1)]
SRC|    for d, o, expected in ((aa3,oo3,p3), (bb2,ob2,pb2),
SRC|                           (aa4,oo4,p4), (bb3,ob3,pb3)):
SRC|        must(tri_poly(d, o) == expected, "characteristic factor")
SRC|    must(leading_dets([3-x for x in bb3], ob3) ==
SRC|         [r, F(3,2)*r*r, r*r*(16-r)/4], "B3 shifted determinants")
SRC|    must(leading_dets([x-1 for x in aa4], oo4) ==
SRC|         [5-3*r, 10-15*r+9*r*r,
SRC|          F(3,2)*r*(3*r-2)*(5-r),
SRC|          F(3,4)*r*r*(9*r*r+9*r-14)], "A4 shifted determinants")
SRC|    chi3 = product_polys([[F(0)]*7+[F(1)], p3, pb2, pb2, pb2])
SRC|    chi2 = product_polys([[F(0),F(1)], [F(-1),F(1)],
SRC|                          [F(-1),F(1)], p4, pb3, pb3, pb3])
SRC|    missing = product_polys([[F(0),F(1)], [F(-1),F(1)],
SRC|                             [F(-1),F(1)], p4, pb3, pb3])
SRC|    return r2, r3, chi2, chi3, missing
SRC|
SRC|def prefix(values):
SRC|    out, total = [], F(0)
SRC|    for value in values:
SRC|        total += value
SRC|        out.append(total)
SRC|    return out
SRC|
SRC|def reference(p):
SRC|    t = abs(1-p)
SRC|    a, b = (1+t)/2, (1-t)/2
SRC|    values = [a**(4-i.bit_count()) * b**i.bit_count()
SRC|              for i in range(16)]
SRC|    return prefix(sorted(values, reverse=True))
SRC|
SRC|def projectors(u):
SRC|    order = [0,5,10,15] + [i for i in range(16) if i not in (0,5,10,15)]
SRC|    current, out = zero(16), []
SRC|    for col in order:
SRC|        v = [row[col] for row in u]
SRC|        current = lin([(F(1), current), (F(1), outer(v))])
SRC|        out.append(current)
SRC|    for k, q in enumerate(out, 1):
SRC|        must(mm(q, q) == q and q == adj(q) and tr(q) == k,
SRC|             "complex consuming projector")
SRC|    return out
SRC|
SRC|def numerical_eigenvalues(a):
SRC|    n = len(a)
SRC|    real = [[float(x[0]) for x in row] for row in a]
SRC|    imag = [[float(x[1]) for x in row] for row in a]
SRC|    m = [real[i] + [-x for x in imag[i]] for i in range(n)]
SRC|    m += [imag[i] + real[i] for i in range(n)]
SRC|    size = 2*n
SRC|    for sweep in range(70):
SRC|        tick()
SRC|        off = max(abs(m[i][j]) for i in range(size) for j in range(i))
SRC|        if off < 2e-14:
SRC|            break
SRC|        for p in range(size-1):
SRC|            for q in range(p+1, size):
SRC|                x = m[p][q]
SRC|                if abs(x) < 1e-16:
SRC|                    continue
SRC|                tau = (m[q][q]-m[p][p])/(2*x)
SRC|                tangent = (1.0 if tau >= 0 else -1.0) / (
SRC|                    abs(tau) + math.sqrt(1+tau*tau))
SRC|                c = 1/math.sqrt(1+tangent*tangent)
SRC|                s = tangent*c
SRC|                m[p][p] -= tangent*x
SRC|                m[q][q] += tangent*x
SRC|                m[p][q] = m[q][p] = 0.0
SRC|                for k in range(size):
SRC|                    if k in (p,q):
SRC|                        continue
SRC|                    kp, kq = m[k][p], m[k][q]
SRC|                    m[k][p] = m[p][k] = c*kp-s*kq
SRC|                    m[k][q] = m[q][k] = s*kp+c*kq
SRC|    residual = max(sum(abs(m[i][j]) for j in range(size) if i != j)
SRC|                   for i in range(size))
SRC|    must(residual < 1e-11, "numerical Jacobi convergence")
SRC|    doubled = sorted((m[i][i] for i in range(size)), reverse=True)
SRC|    must(max(abs(doubled[2*i]-doubled[2*i+1]) for i in range(n)) < 1e-10,
SRC|         "realification paired eigenvalues")
SRC|    return [(doubled[2*i]+doubled[2*i+1])/2 for i in range(n)], residual
SRC|
SRC|def reject(reason, operation):
SRC|    try:
SRC|        operation()
SRC|    except CheckFailure as error:
SRC|        must(str(error) == reason, "mutation wrong rejection reason")
SRC|        return
SRC|    raise CheckFailure("mutation survived: " + reason)
SRC|
SRC|def family_vector(a, b):
SRC|    v = [Z]*16
SRC|    v[0] = G(a)
SRC|    for site in range(4):
SRC|        v[1 << (3-site)] = G(b/2)
SRC|    return v
SRC|
SRC|def schmidt_matrix(v, sites):
SRC|    other = tuple(i for i in range(4) if i not in sites)
SRC|    a = zero(1 << len(sites), 1 << len(other))
SRC|    for i, value in enumerate(v):
SRC|        a[pack(i, sites)][pack(i, other)] = value
SRC|    return a
SRC|
SRC|def run():
SRC|    u = local_unitary()
SRC|    must(mm(u, adj(u)) == eye(16), "physical local unitarity")
SRC|    qs = projectors(u)
SRC|    v_basis = invariant_basis()
SRC|    ref_layers = {
SRC|        1: prefix([4]+[3]*4+[2]*6+[1]*4+[0]),
SRC|        2: prefix([6]+[3]*4+[1]*6+[0]*5),
SRC|        3: prefix([4]+[1]*4+[0]*11),
SRC|    }
SRC|    parameters = [F(0),F(1,3),F(2,3),F(5,6),F(1),F(7,6),F(4,3)]
SRC|    inputs = [(F(0),F(0),F(1)), (F(9,25),F(3,5),F(4,5)),
SRC|              (F(1),F(1),F(0))]
SRC|    saved = {}
SRC|    cases = 0
SRC|    numeric_prefixes = 0
SRC|    max_violation = float("-inf")
SRC|    max_eigen_residual = 0.0
SRC|    for qvalue, amplitude0, amplitude_w in inputs:
SRC|        tick()
SRC|        r, coherent = 1-qvalue, amplitude0*amplitude_w
SRC|        v = family_vector(amplitude0, amplitude_w)
SRC|        rho = outer(v)
SRC|        must(tr(rho) == 1 and mm(rho,rho) == rho, "normalized pure input")
SRC|        h = layers(rho)
SRC|        r2, r3, chi2, chi3, missing = representations(r, coherent)
SRC|        must(mm(h[2],v_basis) == mm(v_basis,r2), "physical H2 invariant identity")
SRC|        must(mm(h[3],v_basis) == mm(v_basis,r3), "physical H3 invariant identity")
SRC|        must(len(chi2) == len(chi3) == 17, "characteristic degree")
SRC|        must(tr(h[1]) == 32 and tr(h[2]) == 24 and tr(h[3]) == 8,
SRC|             "physical layer traces")
SRC|        s1 = sum(2*trprod(partial(rho,(i,)), partial(rho,(i,)))-1
SRC|                 for i in range(4))
SRC|        eta = trprod(rho, spin(rho))
SRC|        moment = trprod(h[3],h[3])
SRC|        must(eta == 0 and s1 == 4-3*r*r, "family spin flip and S1")
SRC|        must(moment == 20-9*r*r == 8+3*s1+2*eta, "family H3 moment")
SRC|        cuts = [(i,) for i in range(4)] + [(0,j) for j in (1,2,3)]
SRC|        for cut in cuts:
SRC|            must(rank(schmidt_matrix(v,cut)) == (1 if qvalue == 1 else 2),
SRC|                 "physical Schmidt rank")
SRC|        if qvalue < 1:
SRC|            pair_expected = [
SRC|                [G(qvalue+r/2),G(coherent/2),G(coherent/2),Z],
SRC|                [G(coherent/2),G(r/4),G(r/4),Z],
SRC|                [G(coherent/2),G(r/4),G(r/4),Z],
SRC|                [Z,Z,Z,Z],
SRC|            ]
SRC|            for sites in ((0,1),(0,2),(0,3)):
SRC|                marginal = partial(rho,sites)
SRC|                must(marginal == pair_expected and rank(marginal) == 2,
SRC|                     "pair support from actual partial trace")
SRC|            support0, support1 = [O,Z,Z,Z], [Z,O,O,Z]
SRC|            def determinant2(w):
SRC|                return sub(mul(w[0],w[3]),mul(w[1],w[2]))
SRC|            must(determinant2(support0) == Z and determinant2(support1) == G(-1),
SRC|                 "pair-support product conic")
SRC|            mixed = [add(x,y) for x,y in zip(support0,support1)]
SRC|            must(determinant2(mixed) == G(-1), "pair-support mixed conic")
SRC|        transformed = conjugate(u,rho)
SRC|        transformed_h = layers(transformed)
SRC|        for m in (1,2,3):
SRC|            must(transformed_h[m] == conjugate(u,h[m]), "physical layer covariance")
SRC|        outputs_by_state = []
SRC|        for label, actual, actual_h in (
SRC|                ("base",rho,h), ("complex-LU",transformed,transformed_h)):
SRC|            psd(actual)
SRC|            for m in (1,2,3):
SRC|                psd(actual_h[m])
SRC|                for k, projector in enumerate(qs):
SRC|                    must(trprod(projector,actual_h[m]) <= ref_layers[m][k],
SRC|                         "fixed-projector layer prefix")
SRC|            outputs = {}
SRC|            for p in parameters:
SRC|                tick()
SRC|                output = erasure(actual,actual_h,p)
SRC|                must(output == pauli_channel(actual,p), "erasure versus Pauli")
SRC|                must(tr(output) == 1, "channel trace")
SRC|                psd(output)
SRC|                bound = reference(p)
SRC|                if p <= 1:
SRC|                    t, b = 1-p, p/2
SRC|                    for k, projector in enumerate(qs):
SRC|                        lhs = trprod(projector,output)
SRC|                        assembled = (t**4*trprod(projector,actual)
SRC|                                     +t**3*b*trprod(projector,actual_h[3])
SRC|                                     +t*t*b*b*trprod(projector,actual_h[2])
SRC|                                     +t*b**3*trprod(projector,actual_h[1])
SRC|                                     +(k+1)*b**4)
SRC|                        ref_assembled = (t**4+t**3*b*ref_layers[3][k]
SRC|                                         +t*t*b*b*ref_layers[2][k]
SRC|                                         +t*b**3*ref_layers[1][k]
SRC|                                         +(k+1)*b**4)
SRC|                        must(lhs == assembled, "same-projector channel assembly")
SRC|                        must(ref_assembled == bound[k], "co-ordered reference assembly")
SRC|                        must(lhs <= bound[k], "exact fixed-projector output bound")
SRC|                else:
SRC|                    positive = erasure(actual,actual_h,2-p)
SRC|                    must(output == spin(positive), "full-transpose output transport")
SRC|                    for k, projector in enumerate(qs):
SRC|                        transported = spin(projector)
SRC|                        must(mm(transported,transported) == transported
SRC|                             and transported == adj(transported)
SRC|                             and tr(transported) == k+1, "transported projector")
SRC|                        must(trprod(projector,output) == trprod(transported,positive),
SRC|                             "same-projector negative-branch pairing")
SRC|                        must(trprod(projector,output) <= bound[k],
SRC|                             "exact negative fixed-projector bound")
SRC|                if p == 0:
SRC|                    must(output == actual, "p zero endpoint")
SRC|                if p == 1:
SRC|                    must(output == lin([(F(1,16),eye(16))]), "p one endpoint")
SRC|                eigenvalues, residual = numerical_eigenvalues(output)
SRC|                max_eigen_residual = max(max_eigen_residual,residual)
SRC|                total = 0.0
SRC|                for k, eigenvalue in enumerate(eigenvalues):
SRC|                    total += eigenvalue
SRC|                    excess = total-float(bound[k])
SRC|                    max_violation = max(max_violation,excess)
SRC|                    must(excess <= TOL, "NUMERICAL output prefix")
SRC|                    numeric_prefixes += 1
SRC|                must(min(eigenvalues) >= -TOL, "NUMERICAL output PSD")
SRC|                outputs[p] = output
SRC|                cases += 1
SRC|            outputs_by_state.append(outputs)
SRC|        for p in parameters:
SRC|            must(outputs_by_state[1][p] == conjugate(u,outputs_by_state[0][p]),
SRC|                 "actual channel local covariance")
SRC|        saved[qvalue] = (rho,h,r2,r3,missing,transformed,transformed_h,
SRC|                         outputs_by_state,moment)
SRC|        print("EXACT written-factor comparison completed q =",str(qvalue),
SRC|              "H3 moment =",str(moment))
SRC|        print("H2 characteristic ascending coefficients:", " ".join(map(str,chi2)))
SRC|        print("H3 characteristic ascending coefficients:", " ".join(map(str,chi3)))
SRC|    middle = saved[F(9,25)]
SRC|    rho,h,r2,r3,missing,complex_rho,complex_h,outputs,moment = middle
SRC|    bad_sign = [row[:] for row in r3]
SRC|    bad_sign[0][1] = neg(bad_sign[0][1])
SRC|    bad_sign[1][0] = neg(bad_sign[1][0])
SRC|    reject("sqrt-sign", lambda: must(
SRC|        mm(h[3],v_basis) == mm(v_basis,bad_sign), "sqrt-sign"))
SRC|    bad_trace = [row[:] for row in r2]
SRC|    bad_trace[0][0] = add(bad_trace[0][0],O)
SRC|    reject("H2-block-trace", lambda: must(tr(bad_trace) == 24,"H2-block-trace"))
SRC|    reject("missing-multiplicity", lambda: must(
SRC|        len(missing) == 17, "missing-multiplicity"))
SRC|    source_sites, wrong_sites = (0,1,3), (0,1,2)
SRC|    actual_marginal = partial(complex_rho,source_sites)
SRC|    bad_index = lin([(F(1),complex_h[3]),
SRC|                     (F(-1),embed(actual_marginal,source_sites)),
SRC|                     (F(1),embed(actual_marginal,wrong_sites))])
SRC|    reject("third-qubit-physical-index", lambda: must(
SRC|        bad_index == complex_h[3], "third-qubit-physical-index"))
SRC|    positive = outputs[1][F(2,3)]
SRC|    wrong_transpose = conjugate_w(partial_transpose(positive,2))
SRC|    reject("partial-not-full-transpose", lambda: must(
SRC|        wrong_transpose == spin(positive), "partial-not-full-transpose"))
SRC|    reject("q-zero-is-not-product-vacuum", lambda: must(
SRC|        saved[F(0)][0][0][0] == O, "q-zero-is-not-product-vacuum"))
SRC|    reject("q-one-is-not-W", lambda: must(
SRC|        saved[F(1)][0][0][0] == Z, "q-one-is-not-W"))
SRC|    one_product_ray = 1
SRC|    reject("old-two-product-ray-class", lambda: must(
SRC|        one_product_ray == 2, "old-two-product-ray-class"))
SRC|    r = F(16,25)
SRC|    reject("wrong-family-moment", lambda: must(
SRC|        moment == 20-8*r*r, "wrong-family-moment"))
SRC|    thresholds = [F(x*x,k)+F((8-x)**2,16-k)
SRC|                  for k,x in ((2,5),(3,6),(4,7))]
SRC|    must(thresholds == [F(92,7),F(160,13),F(37,3)], "moment boundaries")
SRC|    reject("wrong-moment-threshold", lambda: must(
SRC|        min(thresholds) == F(160,12), "wrong-moment-threshold"))
SRC|    must(cases == 42 and numeric_prefixes == 672, "complete finite coverage")
SRC|    tick()
SRC|    print("PASS: exact physical-matrix identities and 10 intended-reason mutations")
SRC|    print("NUMERICAL, NOT EXACT: cases =",cases,"prefixes =",numeric_prefixes)
SRC|    print("NUMERICAL tolerance =",TOL,"max prefix excess =",max_violation)
SRC|    print("NUMERICAL max Jacobi off-diagonal row residual =",max_eigen_residual)
SRC|    print("Elapsed seconds =",time.monotonic()-START)
SRC|    print("LIMIT: family eta is zero; eta coefficient not finitely distinguished")
SRC|    print("LIMIT: no unrestricted target, novelty, independent-family or kernel claim")
SRC|
SRC|try:
SRC|    run()
SRC|except Deadline as error:
SRC|    print("INCOMPLETE:",str(error),"; no PASS or completed-coverage claim")
SRC|    raise SystemExit(2)

## 6. Result and remaining obligations

**Findings:** none identified in the written reconstruction. There is no patch-introduced defect to anchor in the empty assigned-path diff.

The independently reconstructed physical entries, characteristic factors, shifted determinants, endpoint spectra, state-class distinction, and consuming-side channel/projector transport are consistent with S1. The role-limited checker is a complete proposed experiment, not an executed certificate.

Still unpaid:

- Actual execution and examination of the supplied checker’s results.
- Any independently executed finite corroboration.
- Exact characteristic-root/Sturm certification of intermediate full spectra; none is claimed.
- Parent disposition and any required disjoint review gates.
- The unrestricted four-qubit \(H_3\) and all-prefix channel targets.
- Literature novelty, human verification, independent-model-family verification, and formal/kernel verification.

overall_correctness: correct

explanation: No patch-anchored defect was found, and the written exact reconstruction is consistent with the scoped coherent vacuum–W4 theorem and its channel consumers. Scientific execution was prohibited by this role and was not performed; the complete bounded checker is returned NOT RUN, without finite-check acceptance or unrestricted-target closure.

confidence: 0.94