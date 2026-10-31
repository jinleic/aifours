# F567 FINITE — complete independent-check return

**Execution status: NOT RUN. Finite acceptance: NOT ESTABLISHED.**

The runtime assignment prohibits scientific execution and file edits. I honored that restriction: no Python, CAS, solver, test, build, external-model CLI, or scientific shell command was run. The frozen task expressly permits returning full source and argv marked NOT RUN when role-limited. This return supplies that fallback, together with exact written reconstructions and explicit scope limits.

No candidate FATAL, MAJOR, or MINOR defect was established. That is **not** an executed finite PASS or acceptance of the universal theorem.

## 1. Frozen inputs and actual chronology

Wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f567-four-qubit-invariant-normal-form-sharp-extremizer-independent-exact-check/`

Parent-attributed metadata, not my own hash or native-clock observations:

- Manifest SHA256: `3cb2fb0a64a1d1a2ccc87a164df536fdbc84cab291e1dd7490d2aa2cf6e0c15d`
- Receipt SHA256: `ade3cffd5923ea220fa89b7ecd9071e94ee383cb5d00dc3def9d6a54010adab1`
- Literal packet SHA256: `c5977f67d64cad70e6b00e3be6bffa9c21702c0450a2d72bfac90eba00fffd68`
- S1 SHA256: `e300afac40b19341a321be3e9acd84c1d9c81bd10e6f1d3638733087faf3ee51`
- Parent metadata clock: `2026-10-30T13:31:55-0700 PDT`

Actual read order:

1. Required memory summary and relevant review/finite-verification skills.
2. Complete manifest, freeze receipt, parent metadata supply, and all twelve declared status/permission controls.
3. Direct pre-body ACK delivered to `agent://Main`, explicitly disclosing the execution restriction and NOT RUN fallback.
4. Complete literal packet in ordered raw chunks, each containing at most twenty LF, through packet lines 681–700 and S1 logical line 698.
5. Direct read of S1’s terminal logical line 698.
6. Dispatch receipt, for attribution only.
7. Fresh finite-check design and exact written algebra below.

The twelve quarantine controls were used only for permissions/status. No held mathematical payload, sibling scientific return, author code, or additional public source was opened. No cognitive-isolation certificate is asserted.

## 2. What is reconstructed, and what is not

The supplied program constructs, independently from computational-basis definitions:

- Actual sixteen-component pure inputs and their rational density matrices.
- Every physical one-, two-, and three-qubit partial trace, with lifting back to the original physical positions.
- The physical Pauli-twirl expression for \(H_3\).
- All six magic-basis physical generator matrices.
- The coefficient conversion between diagonal magic-product coordinates and the \(e_j^+\) normal form.
- Actual \(X_i,Y_i,Z_i\) error vectors and their consuming physical blocks.
- Exact characteristic polynomials of \(H_3\) and channel outputs for four specified source-family inputs.
- The actual sharp common projector \(Q_*\).
- All 220 three-vector frame Grams and all seven principal minors of \(2I-G\) per Gram.
- Physical Pauli-sum channels at \(p=0,\frac12,1,\frac43\), including independently constructed physical product-reference outputs.
- All sixteen prefixes for every specified input/channel pair.
- A genuinely complex, physically local-unitary-rotated input/projector control that distinguishes full-transpose transport from omission of the transpose.
- Fourteen intended-reason negative controls.

**None of those programmatic checks has been executed.** The source does not establish SO(4) surjectivity, the real-SVD reduction, the mixed-state convex extension, or a universal theorem by finite sampling. Those remain written-proof interfaces for the independent WRITTEN duties and parent disposition.

## 3. Exact written reconstruction of the sharp physical certificate

### 3.1 Actual density and marginals

Let \(v\in\mathbb Z^{16}\), in binary computational order, have

\[
v_0=v_{15}=2,\qquad
v_3=v_{12}=v_5=v_{10}=1,
\]

and all other entries zero. Then

\[
\psi_*=\frac{v}{\sqrt{12}},
\qquad
\rho_*=\frac{vv^T}{12}.
\]

Thus positivity, trace one, and the complete physical sixteen-component input are explicit.

For a physical subset \(S\), the actual marginal is

\[
(\rho_*)_S[a,b]
=\frac1{12}\sum_{z\in\{0,1\}^{S^c}}
v_{(a,z)}v_{(b,z)}.
\]

Here \((a,z)\) inserts the bits into the original physical positions; no regrouped tensor ordering is substituted. The program implements precisely this definition and the corresponding physical lift.

The independent physical twirl to compare with those lifted marginals is

\[
H_3
=2\rho_*+\frac12\sum_{i=1}^4
\left(X_i\rho_*X_i+Y_i\rho_*Y_i+Z_i\rho_*Z_i\right).
\]

Its trace is \(2+12/2=8\). This checks the factor \(1/2\); replacing it by \(1\) would not preserve the actual marginal trace.

### 3.2 Sharp \(H_3\) characteristic polynomial and projector

Written substitution gives

\[
\operatorname{spec}H_3(\rho_*)
=
\left(2,\;(4/3)^{\times3},\;(1/3)^{\times6},\;0^{\times6}\right),
\]

so the exact characteristic polynomial is

\[
\chi_{H_3}(z)
=z^6(z-2)(z-4/3)^3(z-1/3)^6.
\]

Consequently,

\[
\operatorname{Tr}H_3=8,\qquad
\operatorname{rank}H_3=10,\qquad
K_4(H_3)=6.
\]

Using the source’s explicitly specified physical vectors,

\[
Q_*=
|\psi_*\rangle\langle\psi_*|
+|e_0^-\rangle\langle e_0^-|
+|u_X\rangle\langle u_X|
+|u_Y\rangle\langle u_Y|,
\]

where

\[
u_X=\frac12\sum_{i=1}^4f_i^+,\qquad
u_Y=\frac12(f_1^--f_2^--f_3^-+f_4^-),
\]

the four summands are orthogonal normalized vectors. Thus \(Q_*\) is Hermitian and idempotent, has rank four, and the **same actual matrix** gives

\[
\operatorname{Tr}(Q_*\rho_*)=1,\qquad
\operatorname{Tr}(Q_*H_3)=6.
\]

The program checks those statements by full matrix operations rather than by separate scalar maximizations.

### 3.3 Sharp output spectrum and selected physical parameters

Put

\[
\alpha=t^2ab,\qquad \beta=a^2b^2.
\]

The written sharp-state output spectrum is

\[
t^4+2\alpha+\beta,\quad
(\tfrac43\alpha+\beta)^{\times3},\quad
(\tfrac13\alpha+\beta)^{\times6},\quad
\beta^{\times6}.
\]

The following are **written exact values, not program output**:

| Physical \(p\) | \(t\) | Sharp output spectrum | Sharp \(K_4\) | Reference \(K_4\) | Gap |
|---|---:|---|---:|---:|---:|
| \(0\) | \(1\) | \(1,0^{\times15}\) | \(1\) | \(1\) | \(0\) |
| \(1/2\) | \(1/2\) | \((49,25^{\times3},13^{\times6},9^{\times6})/256\) | \(31/64\) | \(81/128\) | \(19/128\) |
| \(1\) | \(0\) | \((1/16)^{\times16}\) | \(1/4\) | \(1/4\) | \(0\) |
| \(4/3\) | \(1/3\) | \((27,20^{\times3},14^{\times6},12^{\times6})/243\) | \(29/81\) | \(40/81\) | \(11/81\) |

At \(p=1/2\), the sixteen sharp-state prefixes, multiplied by 256, are

\[
49,74,99,124,137,150,163,176,189,202,211,220,229,238,247,256.
\]

The corresponding reference prefixes are

\[
81,108,135,162,189,198,207,216,225,234,243,246,249,252,255,256.
\]

At \(p=4/3\), the sixteen sharp-state prefixes, multiplied by 243, are

\[
27,47,67,87,101,115,129,143,157,171,183,195,207,219,231,243.
\]

The corresponding reference prefixes are

\[
48,72,96,120,144,156,168,180,192,204,216,222,228,234,240,243.
\]

These are checks of the named sharp state, not evidence that arbitrary states satisfy the theorem.

### 3.4 A signed generic source-family input

For the additional specified input

\[
x=\frac{(1,-2,3,4)}{\sqrt{30}},
\]

written evaluation gives

\[
\chi_{H_3}(z)=
z^4(z-2)(z-5/3)
(z-16/15)^2(z-3/5)^2
(z-4/15)^3(z-1/15)^3.
\]

Its fourth prefix is \(29/5\), below six. The program compares this predicted spectrum with the characteristic polynomial of the actual lifted-marginal matrix. It does not infer the general family from this example.

## 4. Exhaustive three-frame written census

There are \(\binom{12}{3}=220\) triples.

The actual three bases imply four Gram characteristic-polynomial classes:

| Triple type | Count | Gram characteristic polynomial |
|---|---:|---|
| Three from one basis | 12 | \((z-1)^3\) |
| Two from one basis, one from another | 144 | \((z-1)((z-1)^2-\frac12)\) |
| One from each basis, positive off-diagonal product | 48 | \((z-2)(z-\frac12)^2\) |
| One from each basis, negative off-diagonal product | 16 | \(z(z-\frac32)^2\) |

For the last two counts: fix a coordinate vector \(e\). For the sixteen choices \(b,c\) in the other two bases,

\[
\sum_{b,c}(e\cdot b)(b\cdot c)(c\cdot e)=1.
\]

Each summand is \(+1/8\) or \(-1/8\). Therefore twelve are positive and four negative for each \(e\), giving 48 and 16.

Every diagonal principal minor of \(2I-G\) is one. Every two-by-two principal minor is one or \(3/4\). The three-by-three determinant is respectively \(1,\frac12,0,\frac12\) in the four classes. Hence all seven principal minors are nonnegative in every class.

This is a written exhaustive classification; it is not a claim that a loop over 220 cases was run. The source below independently enumerates the actual vectors, checks the 1,540 principal minors, and checks the census.

## 5. Meaningful complex negative-branch control

A real sharp input alone would make some transpose omissions nondiscriminating. The supplied control instead uses the physical local unitary

\[
U=\operatorname{diag}(1,i)\otimes I^{\otimes3},
\quad
\rho_U=U\rho_*U^\dagger,
\quad
Q_U=UQ_*U^\dagger.
\]

At \(t=1/3\), compare the physical channels \(p=2/3\) and \(p=4/3\).

The correct transported projector is

\[
Q'=WQ_U^TW,\qquad W=Y^{\otimes4}.
\]

For this invariant projector, \(Q'=Q_U\). Omitting the transpose instead gives \(WQ_UW=Q_U^T\), which is distinguishable.

The written exact expectations are

\[
\operatorname{Tr}(Q_U\,T_{-1/3}^{\otimes4}(\rho_U))
=\frac{29}{81}=\frac{87}{243},
\]

whereas the omitted-transpose transported expectation is

\[
\operatorname{Tr}\!\left[(WQ_UW)T_{1/3}^{\otimes4}(\rho_U)\right]
=\frac{70}{243}.
\]

The difference is \(17/243\), not zero. In the unrotated coordinates the latter calculation has

\[
q_{\rm bad}=\frac23,\qquad h_{3,\rm bad}=\frac{10}{3},
\]

giving

\[
\frac13t^4+\frac83\alpha=\frac{17}{243}
\]

as the lost expectation. Thus this is a meaningful transpose control, not a real-matrix check that would pass both implementations.

## 6. Mutation coverage and limits

Every execution result in this table is **NOT RUN**.

| Mutation | Intended rejection |
|---|---|
| Reverse a magic-generator orientation | `MAGIC_ORIENTATION` |
| Treat a particular improper O(4) reflection as a fixed-site product unitary | `FIXED_SITE_PRODUCT` |
| Admit an arbitrary entangling two-qubit unitary into the real SO(4) interface | `CNOT_NOT_REAL_INTERFACE` |
| Omit the \(i\) in the exact \(Y_i\psi\) vector comparison | `Y_VECTOR_PHASE` |
| Reverse one relative \(Y\)-matrix sign | `Y_RELATIVE_SIGN` |
| Substitute \(M_Z^TM_Z\) for \(M_ZM_Z^T\) | `TRANSPOSED_Z_FACTOR` |
| Omit one physical lifted marginal | `MISSING_MARGINAL` |
| Change one sign-vector prediction for \(c\) | `C_SIGN` |
| Replace cross-frame \(1/2\) inner products by \(1\) | `GRAM_BOUND` |
| Use an actual rank-five sum as the rank-four projector | `RANK4_PROJECTOR` |
| Supply different projectors for the density and layer expectations | `COMMON_PROJECTOR` |
| Replace \(\alpha=t^2ab\) by \(t^2b^2\) | `OUTPUT_ALPHA` |
| Reverse the reference-gap sign | `GAP_SIGN` |
| Omit the full transpose in negative-branch projector transport | `FULL_TRANSPOSE` |

Important qualifications:

- A **common overall \(i\)** on a \(Y\)-error vector disappears from its outer product. The vector-phase mutation checks the stated vector convention; it must not be misreported as a density-matrix defect when only a global phase was omitted. The separate relative-sign mutation is physically consequential.
- \(M_X\) and \(M_Y\) are symmetric, so merely transposing either is nondiscriminating. The consuming-factor control uses nonsymmetric \(M_Z\), where the two products differ.
- An improper real O(4) magic-basis reflection need not be entangling: the specific reflection used below is swap-like and non-product on fixed physical sites. The program checks that actual fixed-site obstruction. It does not falsely “prove all SO(4) is physical” from finite tests.
- The CNOT control separately demonstrates why an arbitrary entangling two-qubit unitary is not an admissible substitute for the source’s product-local interface.

## 7. Complete source — NOT RUN

Intended filename: `f567_finite.py`

Intended argv: `python3 -B f567_finite.py`

**This file was not created, compiled, imported, or executed. Its syntax, completion time, and machine results are unverified.**

To reconstruct the source, remove exactly the leading `PY|` from each following source line, preserving the remaining indentation and adding LF line endings. There are no omitted source sections.

The program performs no data-file I/O, network access, child-process creation, installation, or deletion. It retains its result in `RESULT`; it does not write a receipt or print a purported PASS. It has a cooperative 50-second limit. Expiration raises `TIME_LIMIT_INCOMPLETE` and produces no successful result.

PY|from fractions import Fraction as F
PY|from itertools import combinations, product
PY|from time import monotonic
PY|
PY|DEADLINE = None
PY|
PY|class AuditError(Exception):
PY|    def __init__(self, reason):
PY|        self.reason = reason
PY|        super().__init__(reason)
PY|
PY|def need(condition, reason):
PY|    if not condition:
PY|        raise AuditError(reason)
PY|
PY|def pulse():
PY|    if DEADLINE is not None and monotonic() > DEADLINE:
PY|        raise AuditError("TIME_LIMIT_INCOMPLETE")
PY|
PY|def expect_bad(reason, callback):
PY|    try:
PY|        callback()
PY|    except AuditError as exc:
PY|        need(exc.reason == reason, "WRONG_REJECTION_REASON:" + exc.reason)
PY|        return reason
PY|    raise AuditError("EXPECTED_REJECTION_NOT_OBSERVED:" + reason)
PY|
PY|def zero(n, m=None):
PY|    if m is None:
PY|        m = n
PY|    return [[F(0) for _ in range(m)] for _ in range(n)]
PY|
PY|def eye(n):
PY|    a = zero(n)
PY|    for j in range(n):
PY|        a[j][j] = F(1)
PY|    return a
PY|
PY|def mt(a):
PY|    return [list(row) for row in zip(*a)]
PY|
PY|def madd(*args):
PY|    n, m = len(args[0]), len(args[0][0])
PY|    return [[sum((a[i][j] for a in args), F(0))
PY|             for j in range(m)] for i in range(n)]
PY|
PY|def mscale(a, s):
PY|    return [[s * x for x in row] for row in a]
PY|
PY|def msub(a, b):
PY|    return madd(a, mscale(b, -1))
PY|
PY|def mm(a, b):
PY|    n, h, m = len(a), len(b), len(b[0])
PY|    need(len(a[0]) == h, "MATRIX_DIMENSION")
PY|    out = zero(n, m)
PY|    for i in range(n):
PY|        for k in range(h):
PY|            x = a[i][k]
PY|            if not x:
PY|                continue
PY|            for j in range(m):
PY|                if b[k][j]:
PY|                    out[i][j] += x * b[k][j]
PY|    return out
PY|
PY|def tr(a):
PY|    return sum((a[j][j] for j in range(len(a))), F(0))
PY|
PY|def trprod(a, b):
PY|    return sum((a[i][j] * b[j][i]
PY|                for i in range(len(a)) for j in range(len(a))), F(0))
PY|
PY|def rank(a):
PY|    b = [[F(x) for x in row] for row in a]
PY|    rows, cols = len(b), len(b[0])
PY|    r = 0
PY|    for c in range(cols):
PY|        pulse()
PY|        pivot = next((i for i in range(r, rows) if b[i][c]), None)
PY|        if pivot is None:
PY|            continue
PY|        b[r], b[pivot] = b[pivot], b[r]
PY|        q = b[r][c]
PY|        b[r] = [x / q for x in b[r]]
PY|        for i in range(rows):
PY|            if i != r and b[i][c]:
PY|                q = b[i][c]
PY|                b[i] = [x - q * y for x, y in zip(b[i], b[r])]
PY|        r += 1
PY|        if r == rows:
PY|            break
PY|    return r
PY|
PY|def charpoly(a):
PY|    n = len(a)
PY|    b = eye(n)
PY|    coeff = [F(1)]
PY|    for k in range(1, n + 1):
PY|        pulse()
PY|        c = mm(a, b)
PY|        ck = -tr(c) / k
PY|        coeff.append(ck)
PY|        for j in range(n):
PY|            c[j][j] += ck
PY|        b = c
PY|    return tuple(coeff)
PY|
PY|def rootpoly(roots):
PY|    p = [F(1)]
PY|    for e in roots:
PY|        out = [F(0)] * (len(p) + 1)
PY|        for j, c in enumerate(p):
PY|            out[j] += c
PY|            out[j + 1] -= c * e
PY|        p = out
PY|    return tuple(p)
PY|
PY|def prefixes(values):
PY|    out, s = [], F(0)
PY|    for x in values:
PY|        s += x
PY|        out.append(s)
PY|    return tuple(out)
PY|
PY|def gmul(a, b):
PY|    return (a[0] * b[0] - a[1] * b[1],
PY|            a[0] * b[1] + a[1] * b[0])
PY|
PY|def gconj(a):
PY|    return (a[0], -a[1])
PY|
PY|def gscale(a, s):
PY|    return (s * a[0], s * a[1])
PY|
PY|def inner(v, w):
PY|    out = (F(0), F(0))
PY|    for a, b in zip(v, w):
PY|        c = gmul(gconj(a), b)
PY|        out = (out[0] + c[0], out[1] + c[1])
PY|    return out
PY|
PY|def realvec(values):
PY|    return [(x, 0) for x in values]
PY|
PY|def linear(basis, coeff):
PY|    n = len(basis[0])
PY|    return [(sum(coeff[j] * basis[j][k][0] for j in range(len(coeff))),
PY|             sum(coeff[j] * basis[j][k][1] for j in range(len(coeff))))
PY|            for k in range(n)]
PY|
PY|def tensor(v, w):
PY|    return [gmul(a, b) for a in v for b in w]
PY|
PY|UNITS = ((1, 0), (0, 1), (-1, 0), (0, -1))
PY|
PY|def pauli_map(word):
PY|    n = len(word)
PY|    dest, phase = [], []
PY|    for k in range(1 << n):
PY|        j, e = k, 0
PY|        for q, letter in enumerate(word):
PY|            mask = 1 << (n - 1 - q)
PY|            bit = 1 if k & mask else 0
PY|            if letter == "X":
PY|                j ^= mask
PY|            elif letter == "Y":
PY|                j ^= mask
PY|                e += 1 + 2 * bit
PY|            elif letter == "Z":
PY|                e += 2 * bit
PY|            else:
PY|                need(letter == "I", "PAULI_LETTER")
PY|        dest.append(j)
PY|        phase.append(e % 4)
PY|    return dest, phase
PY|
PY|def act(v, word):
PY|    dest, phase = pauli_map(word)
PY|    out = [(0, 0)] * len(v)
PY|    for k, z in enumerate(v):
PY|        out[dest[k]] = gmul(UNITS[phase[k]], z)
PY|    return out
PY|
PY|def outer(v, denominator):
PY|    n = len(v)
PY|    r, im = zero(n), zero(n)
PY|    for i in range(n):
PY|        for j in range(n):
PY|            z = gmul(v[i], gconj(v[j]))
PY|            r[i][j] = F(z[0]) / denominator
PY|            im[i][j] = F(z[1]) / denominator
PY|    return r, im
PY|
PY|def padd(a, b):
PY|    return madd(a[0], b[0]), madd(a[1], b[1])
PY|
PY|def pscale(a, s):
PY|    return mscale(a[0], s), mscale(a[1], s)
PY|
PY|def ptranspose(a):
PY|    return mt(a[0]), mt(a[1])
PY|
PY|def pmm(a, b):
PY|    return (msub(mm(a[0], b[0]), mm(a[1], b[1])),
PY|            madd(mm(a[0], b[1]), mm(a[1], b[0])))
PY|
PY|def ptrprod(a, b):
PY|    return (trprod(a[0], b[0]) - trprod(a[1], b[1]),
PY|            trprod(a[0], b[1]) + trprod(a[1], b[0]))
PY|
PY|def conj_map(a, dest, phase):
PY|    n = len(a[0])
PY|    r, im = zero(n), zero(n)
PY|    for k in range(n):
PY|        for l in range(n):
PY|            if not a[0][k][l] and not a[1][k][l]:
PY|                continue
PY|            z = gmul(UNITS[(phase[k] - phase[l]) % 4],
PY|                     (a[0][k][l], a[1][k][l]))
PY|            r[dest[k]][dest[l]] = z[0]
PY|            im[dest[k]][dest[l]] = z[1]
PY|    return r, im
PY|
PY|def pcj(a, word):
PY|    dest, phase = pauli_map(word)
PY|    return conj_map(a, dest, phase)
PY|
PY|def u_phase(a, qubit):
PY|    n = len(a[0])
PY|    phase = [(k >> (3 - qubit)) & 1 for k in range(n)]
PY|    return conj_map(a, list(range(n)), phase)
PY|
PY|def channel(a, p):
PY|    out = zero(16), zero(16)
PY|    for letters in product("IXYZ", repeat=4):
PY|        pulse()
PY|        weight = F(1)
PY|        for letter in letters:
PY|            weight *= 1 - 3 * p / 4 if letter == "I" else p / 4
PY|        if weight:
PY|            out = padd(out, pscale(pcj(a, "".join(letters)), weight))
PY|    return out
PY|
PY|def bits(k):
PY|    return tuple((k >> (3 - q)) & 1 for q in range(4))
PY|
PY|def extract(k, positions):
PY|    out = 0
PY|    for q in positions:
PY|        out = 2 * out + ((k >> (3 - q)) & 1)
PY|    return out
PY|
PY|def partial(a, positions):
PY|    other = tuple(q for q in range(4) if q not in positions)
PY|    out = zero(1 << len(positions))
PY|    for i in range(16):
PY|        for j in range(16):
PY|            if extract(i, other) == extract(j, other):
PY|                out[extract(i, positions)][extract(j, positions)] += a[i][j]
PY|    return out
PY|
PY|def lift(a, positions):
PY|    other = tuple(q for q in range(4) if q not in positions)
PY|    out = zero(16)
PY|    for i in range(16):
PY|        for j in range(16):
PY|            if extract(i, other) == extract(j, other):
PY|                out[i][j] = a[extract(i, positions)][extract(j, positions)]
PY|    return out
PY|
PY|def physical_layers(rho):
PY|    layers, marginals, lifted = {}, {}, {}
PY|    for j in (1, 2, 3):
PY|        h = zero(16)
PY|        for s in combinations(range(4), j):
PY|            pulse()
PY|            marginal = partial(rho, s)
PY|            need(mt(marginal) == marginal, "MARGINAL_HERMITIAN")
PY|            need(tr(marginal) == 1, "MARGINAL_TRACE")
PY|            term = lift(marginal, s)
PY|            marginals[s] = marginal
PY|            lifted[s] = term
PY|            h = madd(h, term)
PY|        layers[j] = h
PY|    return layers, marginals, lifted
PY|
PY|def paired(a, b, sign):
PY|    v = [0] * 16
PY|    v[a], v[b] = 1, sign
PY|    return realvec(v)
PY|
PY|EPLUS = [paired(a, 15 - a, 1) for a in (0, 3, 5, 6)]
PY|EMINUS = [paired(a, 15 - a, -1) for a in (0, 3, 5, 6)]
PY|FPLUS = [paired(1 << (3 - q), 15 ^ (1 << (3 - q)), 1)
PY|         for q in range(4)]
PY|FMINUS = [paired(1 << (3 - q), 15 ^ (1 << (3 - q)), -1)
PY|          for q in range(4)]
PY|
PY|MAGIC = [
PY|    [(0, 1), (0, 0), (0, 0), (0, 1)],
PY|    realvec((1, 0, 0, -1)),
PY|    realvec((0, 1, 1, 0)),
PY|    [(0, 0), (0, 1), (0, -1), (0, 0)],
PY|]
PY|
PY|def sgen(j, k):
PY|    out = zero(4)
PY|    out[k][j], out[j][k] = F(1), F(-1)
PY|    return out
PY|
PY|def magic_matrix(word):
PY|    out = zero(4)
PY|    for j in range(4):
PY|        v = [gmul((0, -1), z) for z in act(MAGIC[j], word)]
PY|        for i in range(4):
PY|            z = gscale(inner(MAGIC[i], v), F(1, 2))
PY|            need(z[1] == 0, "MAGIC_GENERATOR_REAL")
PY|            out[i][j] = z[0]
PY|    return out
PY|
PY|def xmatrix(r):
PY|    a, b, c, d = r
PY|    return [[a, b, c, d], [b, a, d, c],
PY|            [c, d, a, b], [d, c, b, a]]
PY|
PY|HAD = [[1, 1, 1, 1], [1, 1, -1, -1],
PY|       [1, -1, 1, -1], [1, -1, -1, 1]]
PY|ODD = [[1, -1, -1, -1], [1, -1, 1, 1],
PY|       [1, 1, -1, 1], [1, 1, 1, -1]]
PY|
PY|def frames():
PY|    out = []
PY|    for j in range(4):
PY|        out.append(tuple(F(int(i == j)) for i in range(4)))
PY|    out += [tuple(F(x, 2) for x in row) for row in HAD]
PY|    out += [tuple(F(x, 2) for x in row) for row in ODD]
PY|    return out
PY|
PY|def dot(a, b):
PY|    return sum((x * y for x, y in zip(a, b)), F(0))
PY|
PY|def cvalues(r, frame=None):
PY|    if frame is None:
PY|        frame = frames()
PY|    norm = sum(x * x for x in r)
PY|    return [4 * dot(v, r) ** 2 / norm for v in frame]
PY|
PY|def error_coefficients(v, axis, basis):
PY|    out = [[None] * 4 for _ in range(4)]
PY|    for q in range(4):
PY|        word = "".join(axis if i == q else "I" for i in range(4))
PY|        w = act(v, word)
PY|        for j in range(4):
PY|            out[j][q] = gscale(inner(basis[j], w), F(1, 2))
PY|    return out
PY|
PY|def projected_real_block(a, basis):
PY|    need(all(z[1] == 0 for v in basis for z in v), "REAL_BLOCK_BASIS")
PY|    return [[sum((F(basis[i][k][0]) * a[k][l] *
PY|                  F(basis[j][l][0])
PY|                  for k in range(16) for l in range(16)), F(0)) / 2
PY|             for j in range(4)] for i in range(4)]
PY|
PY|def twirl_from_vectors(v, denominator, rho):
PY|    out = mscale(rho, 2)
PY|    for q in range(4):
PY|        for axis in "XYZ":
PY|            word = "".join(axis if i == q else "I" for i in range(4))
PY|            r, im = outer(act(v, word), denominator)
PY|            need(im == zero(16), "ERROR_OUTER_REAL")
PY|            out = madd(out, mscale(r, F(1, 2)))
PY|    return out
PY|
PY|def det3(a):
PY|    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
PY|            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
PY|            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))
PY|
PY|def principal_psd3(a):
PY|    minors = [a[i][i] for i in range(3)]
PY|    minors += [a[i][i] * a[j][j] - a[i][j] * a[j][i]
PY|               for i, j in combinations(range(3), 2)]
PY|    minors.append(det3(a))
PY|    return all(x >= 0 for x in minors)
PY|
PY|def projector(q, expected_rank, reason):
PY|    need(mt(q) == q, reason)
PY|    need(mm(q, q) == q, reason)
PY|    need(tr(q) == expected_rank, reason)
PY|    need(rank(q) == expected_rank, reason)
PY|
PY|def complex_projector(q, expected_rank):
PY|    need(mt(q[0]) == q[0], "COMPLEX_PROJECTOR_HERMITIAN")
PY|    need(mt(q[1]) == mscale(q[1], -1),
PY|         "COMPLEX_PROJECTOR_HERMITIAN")
PY|    need(pmm(q, q) == q, "COMPLEX_PROJECTOR_IDEMPOTENT")
PY|    need((tr(q[0]), tr(q[1])) == (F(expected_rank), F(0)),
PY|         "COMPLEX_PROJECTOR_RANK")
PY|
PY|def common_certificate(qrho, qlayer, rho, h):
PY|    need(qrho == qlayer, "COMMON_PROJECTOR")
PY|    projector(qrho, 4, "COMMON_PROJECTOR")
PY|    need(trprod(qrho, rho) == 1, "COMMON_PROJECTOR")
PY|    need(trprod(qlayer, h) == 6, "COMMON_PROJECTOR")
PY|
PY|def polyadd(a, b):
PY|    n = max(len(a), len(b))
PY|    return tuple((a[i] if i < len(a) else F(0)) +
PY|                 (b[i] if i < len(b) else F(0)) for i in range(n))
PY|
PY|def polyscale(a, s):
PY|    return tuple(s * x for x in a)
PY|
PY|def polymul(a, b):
PY|    out = [F(0)] * (len(a) + len(b) - 1)
PY|    for i, x in enumerate(a):
PY|        for j, y in enumerate(b):
PY|            out[i + j] += x * y
PY|    return tuple(out)
PY|
PY|def polypow(a, n):
PY|    out = (F(1),)
PY|    for _ in range(n):
PY|        out = polymul(out, a)
PY|    return out
PY|
PY|def finite_audit():
PY|    global DEADLINE
PY|    started = monotonic()
PY|    DEADLINE = started + 50.0
PY|    controls = []
PY|    i16 = eye(16)
PY|    z16 = zero(16)
PY|
PY|    expected_generators = [
PY|        madd(sgen(0, 2), sgen(1, 3)),
PY|        msub(sgen(0, 2), sgen(1, 3)),
PY|        msub(sgen(0, 1), sgen(2, 3)),
PY|        madd(sgen(0, 1), sgen(2, 3)),
PY|        madd(mscale(sgen(0, 3), -1), sgen(1, 2)),
PY|        madd(sgen(0, 3), sgen(1, 2)),
PY|    ]
PY|    words = ("XI", "IX", "ZI", "IZ", "YI", "IY")
PY|    generators = [magic_matrix(word) for word in words]
PY|    need(generators == expected_generators, "MAGIC_GENERATOR_TABLE")
PY|    controls.append(expect_bad("MAGIC_ORIENTATION", lambda:
PY|        need(generators[0] == mscale(expected_generators[0], -1),
PY|             "MAGIC_ORIENTATION")))
PY|
PY|    for d in ((1, 0, 0, 0), (1, -2, 3, 4)):
PY|        pulse()
PY|        lhs = linear([tensor(m, m) for m in MAGIC], d)
PY|        a, b, c, e = d
PY|        numerators = (-a + b, -a - b, c - e, c + e)
PY|        rhs = linear(EPLUS, numerators)
PY|        need(lhs == rhs, "NORMAL_FORM_CONVERSION")
PY|        need(sum(x * x for x in numerators) ==
PY|             2 * sum(x * x for x in d), "NORMAL_FORM_NORM")
PY|
PY|    reflected_projector = outer(MAGIC[0], 1)
PY|    need(reflected_projector[1] == zero(4), "REFLECTION_REAL")
PY|    reflection = msub(eye(4), reflected_projector[0])
PY|    need(charpoly(reflection) ==
PY|         rootpoly((F(-1), F(1), F(1), F(1))), "REFLECTION_SPECTRUM")
PY|    def real_pauli_matrix(word):
PY|        dest, phase = pauli_map(word)
PY|        out = zero(4)
PY|        for k in range(4):
PY|            need(UNITS[phase[k]][1] == 0, "REAL_PAULI")
PY|            out[dest[k]][k] = F(UNITS[phase[k]][0])
PY|        return out
PY|    xleft = real_pauli_matrix("XI")
PY|    zright = real_pauli_matrix("IZ")
PY|    reflected_x = mm(mm(reflection, xleft), mt(reflection))
PY|    commutator = msub(mm(reflected_x, zright),
PY|                     mm(zright, reflected_x))
PY|    controls.append(expect_bad("FIXED_SITE_PRODUCT", lambda:
PY|        need(commutator == zero(4), "FIXED_SITE_PRODUCT")))
PY|
PY|    def cnot(v):
PY|        out = [(0, 0)] * 4
PY|        for k in range(4):
PY|            out[k ^ (1 if k & 2 else 0)] = v[k]
PY|        return out
PY|    bell = cnot(realvec((1, 0, 1, 0)))
PY|    need(bell[0][0] * bell[3][0] -
PY|         bell[1][0] * bell[2][0] != 0, "CNOT_ENTANGLES")
PY|    cnot_magic = [[gscale(inner(MAGIC[i], cnot(MAGIC[j])), F(1, 2))
PY|                   for j in range(4)] for i in range(4)]
PY|    controls.append(expect_bad("CNOT_NOT_REAL_INTERFACE", lambda:
PY|        need(all(z[1] == 0 for row in cnot_magic for z in row),
PY|             "CNOT_NOT_REAL_INTERFACE")))
PY|
PY|    frame = frames()
PY|    for b in range(3):
PY|        for i in range(4):
PY|            for j in range(4):
PY|                need(dot(frame[4 * b + i], frame[4 * b + j]) ==
PY|                     int(i == j), "FRAME_ORTHONORMAL")
PY|    for i, j in combinations(range(12), 2):
PY|        target = F(0) if i // 4 == j // 4 else F(1, 2)
PY|        need(abs(dot(frame[i], frame[j])) == target, "FRAME_CROSS")
PY|    histogram = {}
PY|    gram_count = 0
PY|    for triple in combinations(range(12), 3):
PY|        pulse()
PY|        g = [[dot(frame[i], frame[j]) for j in triple] for i in triple]
PY|        need(principal_psd3(msub(mscale(eye(3), 2), g)), "GRAM_BOUND")
PY|        polynomial = charpoly(g)
PY|        histogram[polynomial] = histogram.get(polynomial, 0) + 1
PY|        gram_count += 1
PY|    expected_histogram = {
PY|        (F(1), F(-3), F(3), F(-1)): 12,
PY|        (F(1), F(-3), F(5, 2), F(-1, 2)): 144,
PY|        (F(1), F(-3), F(9, 4), F(-1, 2)): 48,
PY|        (F(1), F(-3), F(9, 4), F(0)): 16,
PY|    }
PY|    need(gram_count == 220, "GRAM_COUNT")
PY|    need(histogram == expected_histogram, "GRAM_CENSUS")
PY|    triple = (0, 4, 9)
PY|    g = [[dot(frame[i], frame[j]) for j in triple] for i in triple]
PY|    doubled_cross = [[g[i][j] if i == j else 2 * g[i][j]
PY|                      for j in range(3)] for i in range(3)]
PY|    controls.append(expect_bad("GRAM_BOUND", lambda:
PY|        need(principal_psd3(msub(mscale(eye(3), 2), doubled_cross)),
PY|             "GRAM_BOUND")))
PY|
PY|    product_vector = realvec((1,) + (0,) * 15)
PY|    product_density = outer(product_vector, 1)
PY|    reference_layers, _, _ = physical_layers(product_density[0])
PY|    reference_layer_spectra = {}
PY|    for j in (1, 2, 3):
PY|        a = reference_layers[j]
PY|        need(all(a[k][l] == 0 for k in range(16)
PY|                 for l in range(16) if k != l), "REFERENCE_LAYER_DIAGONAL")
PY|        reference_layer_spectra[j] = sorted(
PY|            (a[k][k] for k in range(16)), reverse=True)
PY|    expected_layer_spectra = {
PY|        3: [F(4)] + [F(1)] * 4 + [F(0)] * 11,
PY|        2: [F(6)] + [F(3)] * 4 + [F(1)] * 6 + [F(0)] * 5,
PY|        1: [F(4)] + [F(3)] * 4 + [F(2)] * 6 + [F(1)] * 4 + [F(0)],
PY|    }
PY|    need(reference_layer_spectra == expected_layer_spectra,
PY|         "REFERENCE_LAYER_SPECTRA")
PY|    rprefix = {j: prefixes(reference_layer_spectra[j]) for j in (1, 2, 3)}
PY|    coefficient_table = []
PY|    for k in range(1, 17):
PY|        m = F(6) if k == 4 else F(min(2 * k, 8))
PY|        coefficient_table.append((rprefix[3][k - 1] - m,
PY|                                  rprefix[2][k - 1] - k - m,
PY|                                  rprefix[1][k - 1] - 2 * k))
PY|    expected_table = [
PY|        (2, 3, 2), (1, 3, 3), (0, 3, 4), (1, 5, 5),
PY|        (0, 5, 6), (0, 5, 6), (0, 5, 6), (0, 5, 6),
PY|        (0, 5, 6), (0, 5, 6), (0, 5, 6), (0, 4, 5),
PY|        (0, 3, 4), (0, 2, 3), (0, 1, 2), (0, 0, 0),
PY|    ]
PY|    need(coefficient_table == expected_table, "PREFIX_COEFFICIENT_TABLE")
PY|
PY|    apoly, bpoly = (F(1, 2), F(1, 2)), (F(1, 2), F(-1, 2))
PY|    reference_fourth_poly = polyadd(
PY|        polypow(apoly, 4),
PY|        polyscale(polymul(polypow(apoly, 3), bpoly), 3))
PY|    f4poly = (F(1, 4), F(0), F(1), F(0), F(-1, 4))
PY|    gap_poly = polyadd(reference_fourth_poly, polyscale(f4poly, -1))
PY|    gap_factor_poly = (F(0), F(5, 8), F(-5, 8), F(-1, 8), F(1, 8))
PY|    need(gap_poly == gap_factor_poly, "GAP_POLYNOMIAL_IDENTITY")
PY|    controls.append(expect_bad("GAP_SIGN", lambda:
PY|        need(gap_poly == polyscale(gap_factor_poly, -1), "GAP_SIGN")))
PY|
PY|    parameters = (F(0), F(1, 2), F(1), F(4, 3))
PY|    reference_outputs, reference_prefixes = {}, {}
PY|    for p in parameters:
PY|        actual = channel(product_density, p)
PY|        need(actual[1] == z16, "REFERENCE_OUTPUT_REAL")
PY|        need(all(actual[0][i][j] == 0 for i in range(16)
PY|                 for j in range(16) if i != j), "REFERENCE_OUTPUT_DIAGONAL")
PY|        spectrum = sorted((actual[0][j][j] for j in range(16)),
PY|                          reverse=True)
PY|        t = abs(1 - p)
PY|        a, b = (1 + t) / 2, (1 - t) / 2
PY|        expected = sorted((a ** (4 - sum(bits(k))) * b ** sum(bits(k))
PY|                           for k in range(16)), reverse=True)
PY|        need(spectrum == expected, "PHYSICAL_REFERENCE_SPECTRUM")
PY|        reference_outputs[p] = spectrum
PY|        reference_prefixes[p] = prefixes(spectrum)
PY|
PY|    inputs = (
PY|        ("sharp", (2, 1, 1, 0)),
PY|        ("ghz", (1, 0, 0, 0)),
PY|        ("equal", (1, 1, 1, 1)),
PY|        ("signed_generic", (1, -2, 3, 4)),
PY|    )
PY|    case_results, retained = {}, {}
PY|    for name, r in inputs:
PY|        pulse()
PY|        norm = sum(x * x for x in r)
PY|        denominator = 2 * norm
PY|        v = linear(EPLUS, r)
PY|        rho_parts = outer(v, denominator)
PY|        rho, im = rho_parts
PY|        need(im == z16 and mt(rho) == rho, "INPUT_HERMITIAN")
PY|        need(tr(rho) == 1 and rank(rho) == 1, "INPUT_PURE_DENSITY")
PY|        need(pcj(ptranspose(rho_parts), "YYYY") == rho_parts,
PY|             "INPUT_SPIN_FLIP")
PY|        layers, marginals, lifted = physical_layers(rho)
PY|        h = layers[3]
PY|        need(len(marginals) == 14, "ALL_PROPER_MARGINALS")
PY|        need(layers[1] == mscale(i16, 2), "H1_IDENTITY")
PY|        need(layers[2] == madd(i16, h), "H2_IDENTITY")
PY|        need(tr(h) == 8, "H3_TRACE")
PY|        twirl = twirl_from_vectors(v, denominator, rho)
PY|        need(twirl == h, "PHYSICAL_TWIRL")
PY|
PY|        mx = xmatrix(r)
PY|        my = xmatrix((r[0], -r[1], -r[2], -r[3]))
PY|        mz = [[r[i] * HAD[i][j] for j in range(4)] for i in range(4)]
PY|        actual_x = error_coefficients(v, "X", FPLUS)
PY|        actual_y = error_coefficients(v, "Y", FMINUS)
PY|        actual_z = error_coefficients(v, "Z", EMINUS)
PY|        need(actual_x == [[(F(x), F(0)) for x in row] for row in mx],
PY|             "X_PHYSICAL_ERROR_COLUMNS")
PY|        need(actual_y == [[(F(0), F(x)) for x in row] for row in my],
PY|             "Y_PHYSICAL_ERROR_COLUMNS")
PY|        need(actual_z == [[(F(x), F(0)) for x in row] for row in mz],
PY|             "Z_PHYSICAL_ERROR_COLUMNS")
PY|        for matrix, basis in ((mx, FPLUS), (my, FMINUS), (mz, EMINUS)):
PY|            predicted = mscale(mm(matrix, mt(matrix)), F(1, 2 * norm))
PY|            need(projected_real_block(h, basis) == predicted,
PY|                 "PHYSICAL_ERROR_BLOCK")
PY|        even_block = [[F(2 * r[i] * r[j], norm) for j in range(4)]
PY|                      for i in range(4)]
PY|        need(projected_real_block(h, EPLUS) == even_block,
PY|             "EVEN_PLUS_BLOCK")
PY|
PY|        c = cvalues(r)
PY|        hspectrum = sorted([F(2)] + [x / 2 for x in c] +
PY|                           [F(0)] * 3, reverse=True)
PY|        hpoly = charpoly(h)
PY|        need(hpoly == rootpoly(hspectrum), "ACTUAL_H3_CHARPOLY")
PY|        need(sum(hspectrum) == 8, "H3_SPECTRAL_TRACE")
PY|        need(prefixes(hspectrum)[3] <= 6, "FINITE_H3_FOURTH")
PY|        outputs = {}
PY|        channel_results = {}
PY|        for p in parameters:
PY|            pulse()
PY|            actual = channel(rho_parts, p)
PY|            need(actual[1] == z16, "OUTPUT_REAL")
PY|            t = abs(1 - p)
PY|            a, b = (1 + t) / 2, (1 - t) / 2
PY|            alpha, beta = t * t * a * b, a * a * b * b
PY|            reduced = madd(mscale(rho, t ** 4), mscale(h, alpha),
PY|                           mscale(i16, beta))
PY|            need(actual[0] == reduced, "ACTUAL_CHANNEL_REDUCTION")
PY|            expected_eigenvalues = sorted(
PY|                [t ** 4 + 2 * alpha + beta] +
PY|                [alpha * x / 2 + beta for x in c] + [beta] * 3,
PY|                reverse=True)
PY|            need(charpoly(actual[0]) == rootpoly(expected_eigenvalues),
PY|                 "ACTUAL_OUTPUT_CHARPOLY")
PY|            oprefix = prefixes(expected_eigenvalues)
PY|            gaps = tuple(x - y for x, y in
PY|                         zip(reference_prefixes[p], oprefix))
PY|            need(all(x >= 0 for x in gaps), "ALL16_PREFIXES")
PY|            need(gaps[-1] == 0, "OUTPUT_TRACE_ONE")
PY|            if 0 < t < 1:
PY|                need(all(x > 0 for x in gaps[:-1]),
PY|                     "FINITE_PROPER_PREFIX_STRICTNESS")
PY|            if name == "sharp":
PY|                f4 = (1 + 4 * t * t - t ** 4) / 4
PY|                gap = t * (1 - t) * (5 - t * t) / 8
PY|                need(oprefix[3] == f4, "SHARP_F4")
PY|                need(gaps[3] == gap, "SHARP_REFERENCE_GAP")
PY|            outputs[p] = actual
PY|            channel_results[p] = {
PY|                "spectrum": tuple(expected_eigenvalues),
PY|                "prefixes": oprefix,
PY|                "reference_prefixes": reference_prefixes[p],
PY|                "gaps": gaps,
PY|            }
PY|        case_results[name] = {
PY|            "r": r, "normalizer_squared": norm,
PY|            "H3_spectrum": tuple(hspectrum),
PY|            "H3_charpoly": hpoly, "H3_rank": rank(h),
PY|            "channels": channel_results,
PY|        }
PY|        retained[name] = (v, rho_parts, layers, lifted, twirl,
PY|                          mx, my, mz, actual_y, outputs)
PY|
PY|    (v, rho_parts, layers, lifted, twirl,
PY|     mx, my, mz, actual_y, outputs) = retained["sharp"]
PY|    rho, h = rho_parts[0], layers[3]
PY|    need(rank(h) == 10, "SHARP_H3_RANK")
PY|    uz = EMINUS[0]
PY|    ux = linear(FPLUS, (1, 1, 1, 1))
PY|    uy = linear(FMINUS, (1, -1, -1, 1))
PY|    q = madd(rho, outer(uz, 2)[0], outer(ux, 8)[0], outer(uy, 8)[0])
PY|    projector(q, 4, "SHARP_PROJECTOR")
PY|    common_certificate(q, q, rho, h)
PY|    need(charpoly(q) == rootpoly([F(1)] * 4 + [F(0)] * 12),
PY|         "SHARP_PROJECTOR_CHARPOLY")
PY|
PY|    controls.append(expect_bad("Y_VECTOR_PHASE", lambda:
PY|        need(actual_y == [[(F(x), F(0)) for x in row] for row in my],
PY|             "Y_VECTOR_PHASE")))
PY|    bad_my = [row[:] for row in my]
PY|    bad_my[0][1] = -bad_my[0][1]
PY|    controls.append(expect_bad("Y_RELATIVE_SIGN", lambda:
PY|        need(actual_y == [[(F(0), F(x)) for x in row] for row in bad_my],
PY|             "Y_RELATIVE_SIGN")))
PY|    wrong_z_block = mscale(mm(mt(mz), mz), F(1, 12))
PY|    controls.append(expect_bad("TRANSPOSED_Z_FACTOR", lambda:
PY|        need(projected_real_block(h, EMINUS) == wrong_z_block,
PY|             "TRANSPOSED_Z_FACTOR")))
PY|    missing = msub(h, lifted[(1, 2, 3)])
PY|    controls.append(expect_bad("MISSING_MARGINAL", lambda:
PY|        need(missing == twirl, "MISSING_MARGINAL")))
PY|    bad_frame = list(frame)
PY|    bad_frame[5] = bad_frame[4]
PY|    bad_c = cvalues((2, 1, 1, 0), bad_frame)
PY|    controls.append(expect_bad("C_SIGN", lambda:
PY|        need(charpoly(h) == rootpoly(
PY|            [F(2)] + [x / 2 for x in bad_c] + [F(0)] * 3), "C_SIGN")))
PY|
PY|    extra = outer(EPLUS[3], 2)[0]
PY|    q_rank5 = madd(q, extra)
PY|    controls.append(expect_bad("RANK4_PROJECTOR", lambda:
PY|        projector(q_rank5, 4, "RANK4_PROJECTOR")))
PY|    q_other = madd(q, mscale(rho, -1), extra)
PY|    projector(q_other, 4, "OTHER_PROJECTOR")
PY|    other_traces = (trprod(q_other, rho), trprod(q_other, h))
PY|    need(other_traces == (F(0), F(4)), "OTHER_PROJECTOR_TRACES")
PY|    controls.append(expect_bad("COMMON_PROJECTOR", lambda:
PY|        common_certificate(q, q_other, rho, h)))
PY|
PY|    t, a, b = F(1, 2), F(3, 4), F(1, 4)
PY|    bad_output = madd(mscale(rho, t ** 4),
PY|                      mscale(h, t * t * b * b),
PY|                      mscale(i16, a * a * b * b))
PY|    controls.append(expect_bad("OUTPUT_ALPHA", lambda:
PY|        need(outputs[F(1, 2)][0] == bad_output, "OUTPUT_ALPHA")))
PY|
PY|    rotated_rho = u_phase(rho_parts, 0)
PY|    rotated_q = u_phase((q, z16), 0)
PY|    complex_projector(rotated_q, 4)
PY|    need(pcj(ptranspose(rotated_rho), "YYYY") == rotated_rho,
PY|         "ROTATED_INPUT_SPIN_FLIP")
PY|    need(any(x for row in rotated_rho[1] for x in row),
PY|         "COMPLEX_CONTROL_DISCRIMINATING_INPUT")
PY|    positive = channel(rotated_rho, F(2, 3))
PY|    negative = channel(rotated_rho, F(4, 3))
PY|    need(negative == pcj(ptranspose(positive), "YYYY"),
PY|         "NEGATIVE_BRANCH_FULL_TRANSPOSE")
PY|    transported_q = pcj(ptranspose(rotated_q), "YYYY")
PY|    complex_projector(transported_q, 4)
PY|    need(ptrprod(rotated_q, negative) ==
PY|         ptrprod(transported_q, positive), "PROJECTOR_TRANSPORT")
PY|    correct_expectation = ptrprod(rotated_q, negative)
PY|    omitted_transpose_q = pcj(rotated_q, "YYYY")
PY|    wrong_expectation = ptrprod(omitted_transpose_q, positive)
PY|    need(correct_expectation == (F(29, 81), F(0)),
PY|         "COMPLEX_CONTROL_CORRECT_VALUE")
PY|    need(wrong_expectation == (F(70, 243), F(0)),
PY|         "COMPLEX_CONTROL_WRONG_VALUE")
PY|    controls.append(expect_bad("FULL_TRANSPOSE", lambda:
PY|        need(correct_expectation == wrong_expectation, "FULL_TRANSPOSE")))
PY|
PY|    need(len(controls) == 14, "CONTROL_COUNT")
PY|    pulse()
PY|    return {
PY|        "status": "PASS_FINITE_ONLY",
PY|        "elapsed_seconds": monotonic() - started,
PY|        "input_cases": case_results,
PY|        "proper_marginals_per_source_input": 14,
PY|        "magic_generator_count": 6,
PY|        "normal_form_conversion_cases": 2,
PY|        "gram_count": gram_count,
PY|        "gram_principal_minors_checked": 7 * gram_count,
PY|        "gram_charpoly_histogram": histogram,
PY|        "prefix_coefficient_table": tuple(coefficient_table),
PY|        "sharp_common_projector_traces": (trprod(q, rho), trprod(q, h)),
PY|        "sharp_projector_rank": rank(q),
PY|        "sharp_H3_rank": rank(h),
PY|        "different_projector_traces": other_traces,
PY|        "complex_transport_correct": correct_expectation,
PY|        "complex_transport_omitted_transpose": wrong_expectation,
PY|        "intended_reason_rejections": tuple(controls),
PY|        "universal_SO4_surjectivity_proved_by_execution": False,
PY|        "mixed_invariant_theorem_proved_by_samples": False,
PY|        "unrestricted_four_qubit_claim": False,
PY|    }
PY|
PY|if __name__ == "__main__":
PY|    RESULT = finite_audit()

## 8. Results, findings, and disposition

### Actually observed

- Complete declared control and candidate access, with pre-body ACK.
- No scientific execution.
- No repository or scratch-file edits.
- Exact written reconstructions in §§3–5.
- Complete source and intended invocation supplied above.

### Not observed

- Syntax success.
- Exit status.
- Runtime or resource consumption.
- Program-generated characteristic polynomials, Gram census, prefix tables, mutation rejections, or PASS.
- A checker-source SHA256.
- An execution receipt.

These must remain **NOT RUN / NOT COMPUTED**, not be filled from the written expected values.

### Findings

- **FATAL: 0 established.**
- **MAJOR: 0 established.**
- **MINOR: 0 established.**
- **Finite execution gate: NOT ESTABLISHED because execution was prohibited in this runtime.** This is an evidentiary limitation, not a mathematical defect attributed to S1.

### Scope status

- Sharp physical state, rational density, common-projector certificate, selected exact spectra, gap arithmetic, and discriminating complex transpose control: **written reconstructed; no machine verification claimed**.
- All-220 Gram classification: **written exact census; supplied exhaustive enumeration NOT RUN**.
- Physical generator and consuming-block interfaces: **fully mapped into the supplied independent checker; execution NOT RUN**.
- All-SO(4) realization, general normal-form reduction, mixed-state convex extension, and universal all-prefix invariant-sector theorem: **not promoted by this FINITE return**.
- Arbitrary non-spin-flip-invariant four-qubit inputs: **NOT PROVED**.
- Source equivalence, novelty, independent-family/human/kernel verification, and final program completion: **not claimed**.

**Overall correctness: correct in the review sense that no candidate defect was established by the permitted inspection.**

**Explanation:** The inspected physical interfaces and exact written certificates are consistent with S1, including a nontrivial complex negative-branch control. The independent executable finite gate remains NOT RUN and cannot supply acceptance until an authorized execution and receipt exist.

**Confidence: 0.88** for the inspection verdict; no confidence is asserted in an unperformed execution.