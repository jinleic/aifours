# f573 — Exact physical-routing and rank-regime interface reconstruction

**Role:** FINITE  
**Candidate:** f557, UNADOPTED  
**Disposition:** Written interfaces supported; executable verification **NOTRUN**; parent acceptance pending.

**Mathematical findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Documentary finding:** **1 MINOR**, corrected additively: my pre-body ACK incorrectly said eleven controls, and included insufficiently grounded exact LF totals for two administrative files. There are **twelve** controls. All twelve had actually been completely read before the ACK. The subsequent correction’s `111–120` transport-range typo was immediately corrected to the actual `101–120` request. These are reporting errors, not missing-control reads or mathematical findings.

No scientific program, checker, build, test, solver, external-model CLI, source-following operation, or sibling review was run/read. No project file was written. The complete unexecuted verifier source and exact proposed argv appear below.

## 1. Evidence and chronology

Frozen wave:

`institute/runs/three-area-2026-10-27-96h/review-waves/f573-rqls10-other-orbit-sixty-cell-projection-and-rank-regime-exact-check/`

Parent-supplied bindings:

- Manifest: `1b2742462e05358415e68cc5fb9d77c8b04741cbc83065ef194ac4241567588c`
- Freeze receipt: `8b55e27094a21884ebce94facc571caad1c046e1629568690d1c292646e74747`
- Literal packet: `cfe083f115ad90627159233c912349db7d577532444fee7d2c18cacc446b57c8`

These are **parent-observed metadata**, not independently executed child hash checks. The clock in the metadata supply is likewise not a child-native observation.

Before my direct pre-body ACK, I read:

- Manifest requested LF 1–116, in ordered raw windows of at most twenty LF.
- Freeze receipt through its closing brace, requested LF 1–60 in windows of at most twenty.
- All twelve control bodies and endings:
  - Prospective restoration: 1–15.
  - Owner addendum 2: 1–14.
  - L1 quarantine: 1–20, 21–23.
  - Privacy quarantine: 1–11.
  - CORE-GRAM quarantine: 1–9.
  - AME quarantine: 1–8.
  - PH consumer quarantine: 1–20, 21–40, 41–49.
  - f439 quarantine: 1–20, 21–23.
  - f444 quarantine: 1–16.
  - f448 quarantine: 1–20.
  - f508 quarantine: 1–20, 21–22.
  - f513 quarantine: 1–20, 21–22.
- Parent live-metadata supply through the closing brace returned by `101–120`.
- Dispatch receipt through the closing brace returned by `1–20`.

I then read the complete literal packet in consecutive raw windows `1–20, …, 761–778`, including the endings of **S1 logical lines 1–747** and **S2 lines 1–29**, before derivation. At the administrative interruption, the packet frontier was LF 400; I rechecked manifest control entries LF 7–80, sent the inventory corrections, then resumed at LF 401. No derivation or execution preceded the packet’s completion.

Held episodes and **all their consumers** remained NONINPUT. No clean-cognition or provenance-isolation certificate is asserted.

## 2. Actual sixty-cell universe and all physical contexts

Let

\[
T=\{2,5,6,7,8,9\},\qquad
H_T=\{(r,c):c-r\pmod {10}\in T\}.
\]

The complete original-coordinate cell inventory is:

| Original row \(r\) | Original columns \(c\) |
|---|---|
| 0 | 2, 5, 6, 7, 8, 9 |
| 1 | 0, 3, 6, 7, 8, 9 |
| 2 | 0, 1, 4, 7, 8, 9 |
| 3 | 0, 1, 2, 5, 8, 9 |
| 4 | 0, 1, 2, 3, 6, 9 |
| 5 | 0, 1, 2, 3, 4, 7 |
| 6 | 1, 2, 3, 4, 5, 8 |
| 7 | 2, 3, 4, 5, 6, 9 |
| 8 | 0, 3, 4, 5, 6, 7 |
| 9 | 1, 4, 5, 6, 7, 8 |

Use \(c'=c-2\), not \(c+2\). Then

\[
c'-r\in\{0,3,4,5,6,7\}.
\]

For \(a,b\in\mathbb Z_5\), \(u,v\in\mathbb Z_2\), put

\[
\operatorname{crt}(a,u)=a+5((u-a)\bmod2).
\]

The actual original coordinates are

\[
r=\operatorname{crt}(a,u),\qquad
c=\operatorname{crt}(b,v)+2\pmod {10}.
\]

The exact cell rule is:

- \(a=b\): all four bit pairs.
- \(b-a=\pm1\): \(v=u\).
- \(b-a=\pm2\): \(v=u+1\).

Write diagonal labels \(D_a^{uv}\) and off-diagonal labels \(O_{ab}^{u}\), where \(v=u+\tau(a,b)\), with \(\tau=0\) for difference \(\pm1\), and \(\tau=1\) for difference \(\pm2\).

This gives twenty diagonal and forty off-diagonal cells, not an abstract replacement incidence structure.

### Thirty contexts

For every \(a,u\), the physical row is

\[
\{D_a^{u0},D_a^{u1}\}\cup\{O_{ab}^{u}:b\ne a\}.
\]

For every \(b,v\), the physical column is

\[
\{D_b^{0v},D_b^{1v}\}
\cup
\{O_{ab}^{\,v-\tau(a,b)}:a\ne b\}.
\]

For an **original** symbol \(\ell=r+c\), set

\[
s=(\ell-2)\bmod5,\qquad
w=(\ell-2)\bmod2,\qquad
k=3s\bmod5.
\]

The inverse multiplier is **3**, since \(2k=s\pmod5\).

The six-cell symbol contexts are:

\[
w=0:
\quad
\{D_k^{00},D_k^{11}\}
\cup
\{O_{k-2,k+2}^{u},O_{k+2,k-2}^{u}:u=0,1\};
\]

\[
w=1:
\quad
\{D_k^{01},D_k^{10}\}
\cup
\{O_{k-1,k+1}^{u},O_{k+1,k-1}^{u}:u=0,1\}.
\]

These formulas cover ten rows, ten columns and ten actual \(r+c\) symbol classes. Each contains six cells.

An independent original-coordinate count is also available: for a fixed \(\ell\), each \(d\in T\) of the same parity as \(\ell\) gives two solutions of \(2r=\ell-d\pmod {10}\). There are three such \(d\), hence six cells.

## 3. Operator interfaces derived from those cell sets

Assume the physical contexts are ONBs in \(\mathbb C^6\). Write \(p_x=xx^\dagger\).

The four diagonal rays at index \(a\) are mutually orthogonal: each pair shares a row, column, or symbol. Therefore

\[
F_a=\sum_{u,v}p_{D_a^{uv}},\qquad E_a=I-F_a
\]

have ranks four and two. Define

\[
U_a=p_{D_a^{00}}+p_{D_a^{11}},\qquad
V_a=p_{D_a^{01}}+p_{D_a^{10}}.
\]

Then \(U_a,V_a,E_a\) form an orthogonal rank-two projection partition.

The two rays of every \(O_{ab}\) block share a physical symbol, so

\[
P_{ab}=p_{O_{ab}^{0}}+p_{O_{ab}^{1}}
\]

is a rank-two projection.

Adding the two actual rows at index \(a\), and separately the two columns, gives

\[
\sum_{b\ne a}P_{ab}=I+E_a,\qquad
\sum_{b\ne a}P_{ba}=I+E_a.
\]

The actual symbol sets give

\[
P_{k-2,k+2}+P_{k+2,k-2}=I-U_k,
\]

\[
P_{k-1,k+1}+P_{k+1,k-1}=I-V_k.
\]

For every edge \(\{a,b\}\), its midpoint is \(k=3(a+b)\). Differences \(\pm1\) omit \(U_k\), and differences \(\pm2\) omit \(V_k\). Thus all five balance equations are

\[
U_{a-2}+U_{a+2}+V_{a-1}+V_{a+1}=2U_a+2V_a.
\]

Their positive-neighbor coefficient rows are:

| \(a\) | \(U\)-indices with coefficient \(+1\) | \(V\)-indices with coefficient \(+1\) |
|---|---|---|
| 0 | 2, 3 | 1, 4 |
| 1 | 3, 4 | 0, 2 |
| 2 | 0, 4 | 1, 3 |
| 3 | 0, 1 | 2, 4 |
| 4 | 1, 2 | 0, 3 |

Each row also has coefficient \(-2\) on \(U_a,V_a\).

Positivity, applied on \(\operatorname{ran}E_a\), gives

\[
E_aU_{a\pm2}=0,\qquad E_aV_{a\pm1}=0.
\]

Consequently,

\[
E_{a\pm1}\le E_a+U_a,\qquad
E_{a\pm2}\le E_a+V_a.
\]

No graph-intersection rank has been substituted for a projection rank.

## 4. Both five-cycles and the operator proof boundary

For projections satisfying

\[
PQ=PRQ,\qquad RQ=RPQ,
\]

take \(x\in\operatorname{ran}Q\), \(y=Px\), \(z=Rx\). Then \(y=Pz\), \(z=Ry\). Projection contraction yields

\[
\|y\|\le\|z\|\le\|y\|,
\]

so equality forces \(Pz=z\), hence \(y=z\) and \((P-R)Q=0\).

For \(P=E_{a-1},Q=E_a,R=E_{a+1}\), the containment interfaces put \(P,Q\) in \(R+V_{a+1}\), \(R+U_{a+1}\), respectively. Since \(U_{a+1}V_{a+1}=0\),

\[
PQ=P(R+V_{a+1})(R+U_{a+1})Q=PRQ.
\]

The partition at \(P\) similarly gives \(RQ=RPQ\).

This establishes

\[
(E_{a-1}-E_{a+1})E_a=0.
\]

For \(T_a=E_aE_{a+1}\), it follows that \(T_a=T_{a+1}^\dagger\). Traversing

\[
0,1,2,3,4
\]

has odd length, so all these products are one self-adjoint projection.

The same argument, with \(U,V\) exchanged, works for

\[
0,2,4,1,3.
\]

It gives one common self-adjoint distance-two product. Both common projections lie in every \(E_a\), so they contain one another and coincide. Therefore

\[
E_aE_b=G\quad(a\ne b).
\]

The five residual projections \(E_a-G\) are pairwise orthogonal. Their dimension count is

\[
g+5(2-g)\le6,\qquad 0\le g\le2,
\]

so exactly \(g=1\) or \(g=2\) remains.

**Boundary:** the finite source below checks index dispatches and formal algebraic certificates. The contraction/positivity argument above is the general Hilbert-space argument; it is not replaced by testing finitely many numerical matrices.

### Necessary even-cycle control

In \(\mathbb R^4\), let

\[
P=\operatorname{diag}(1,1,0,0),
\quad
Q=p_{e_0}+p_{(3e_1+4e_2)/5}.
\]

Both have rank two. In the four-cycle \(P,Q,P,Q\), adjacent products alternate \(PQ,QP,PQ,QP\), satisfying \(T_j=T_{j+1}^{\mathsf T}\). Nevertheless \(PQ\ne QP\), since its \((1,2)\) entry is \(12/25\) and its \((2,1)\) entry is zero.

Also,

\[
\operatorname{rank}(PQ)=2,\qquad
\dim(\operatorname{ran}P\cap\operatorname{ran}Q)=1.
\]

Thus neither Hermiticity on an even cycle nor intersection rank from the rank of an unproved noncommuting product is valid.

This is a **local countermodel to omitted hypotheses**, not a physical sixty-ray witness.

## 5. Rank-one regime: all coordinate-choice patterns and both consumers

When \(g=1\),

\[
\mathbb C^6=G\oplus L_0\oplus\cdots\oplus L_4,
\]

where each summand is a line, and

\[
E_a=G\oplus L_a,\quad
U_a=L_{a-1}\oplus L_{a+1},\quad
V_a=L_{a-2}\oplus L_{a+2}.
\]

The ten \(U_a,V_a\) line-pairs are exactly the ten edges of \(K_5\).

A coordinate two-vector ONB uses both of its line rays. Global nonparallelness therefore requires coordinate choices to be a matching on these five line vertices.

The complete necessary coordinate-choice inventory is:

- Zero coordinate bases: \(1\) pattern.
- One coordinate basis: \(10\) patterns.
- Two disjoint coordinate bases: \(15\) patterns.
- Three coordinate bases: impossible.

Thus there are **26** legal necessary index patterns. The “15” is the number of **two-coordinate-basis** patterns, not the total.

Their good-index histogram is:

| Number of good indices | Number of patterns |
|---|---|
| 5 | 1 |
| 4 | 15 |
| 3 | 10 |

Of the fifteen two-basis patterns, five use both bases at the same index, while ten affect two different indices. In particular, every pattern has at least three good indices.

These are necessary combinatorial patterns, **not constructed physical configurations**.

### Both endpoint orthogonality implications

For distinct good \(a,b\), let \(k=3(a+b)\). The symbol equation puts each \(O_{ab}^{u}\) in

\[
G\oplus L_a\oplus L_b\oplus L_k.
\]

At endpoint \(a\), \(b\) and \(k\) belong to different \(U_a,V_a\) line-pairs:

- \(b-a=\pm1\) implies \(k-a=\mp2\).
- \(b-a=\pm2\) implies \(k-a=\pm1\).

A noncoordinate ONB of a two-dimensional coordinate plane has both coefficients nonzero in both basis vectors. If an off-diagonal ray has only one possible coordinate in that plane, orthogonality to the relevant diagonal ray is an equation

\[
\overline{\alpha}\,x=0,\qquad \alpha\ne0,
\]

not a cancellation between two unknown coordinates. Hence \(x=0\).

The row’s two diagonal rays therefore kill the \(L_b,L_k\) coordinates, yielding

\[
O_{ab}^{u}\in G\oplus L_a=E_a.
\]

The actual column uses diagonal rays \(D_b^{0v},D_b^{1v}\), where \(v=u+\tau(a,b)\). One belongs to \(U_b\), the other to \(V_b\). Since \(b\) is good, the same nonzero-coefficient argument kills \(L_a,L_k\), yielding

\[
O_{ab}^{u}\in G\oplus L_b=E_b.
\]

Thus both \(u=0,1\) rays lie in the one-dimensional \(G\), contradicting their physical-symbol orthogonality.

The source below exhausts all 26 patterns, all ordered good endpoint pairs, and both values of \(u\): **520 endpoint/bit dispatches** are the written-derived expected count.

## 6. Rank-two regime: exact rational linear certificate

When \(g=2\), all \(E_a=G\), and \(U_a+V_a=F=I-G\). The balance becomes

\[
U_{a-2}+U_{a+2}-U_{a-1}-U_{a+1}=0.
\]

The exact rational coefficient matrix is

\[
L=
\begin{pmatrix}
0&-1&1&1&-1\\
-1&0&-1&1&1\\
1&-1&0&-1&1\\
1&1&-1&0&-1\\
-1&1&1&-1&0
\end{pmatrix}.
\]

It satisfies

\[
L\mathbf1=0,\qquad L^2=5I-J.
\]

Therefore its kernel is exactly the constant line and its rank is four.

On the sum-zero basis \(e_0-e_4,\ldots,e_3-e_4\), its matrix is

\[
\begin{pmatrix}
1&0&2&2\\
-2&-1&-2&0\\
0&-2&-1&-2\\
2&2&0&1
\end{pmatrix},
\]

with determinant \(25\). The principal four-by-four cofactor of \(L\) is \(5\); its first-row expansion is \(1+1-(-3)=5\).

Thus \(U_a=U,V_a=V\), with \(G,U,V\) a common orthogonal rank-two partition. This is a linear operator-valued argument, not a covariance assumption.

## 7. Rank-two individual-ray consumer and its necessary control

For projection partitions \(A_1+A_2+A_3=I\), \(Q_1+Q_2+Q_3=I\) with \(Q_iA_i=0\), every off-diagonal sandwich \(A_jQ_iA_k\), \(j\ne k\), vanishes:

- If \(i=j\) or \(i=k\), use the matching annihilation.
- Otherwise substitute \(Q_i=I-Q_j-Q_k\).

Hence every \(Q_i\) reduces every \(A_j\).

For each physical row, group its rays into:

- Its two diagonal rays \(R\), annihilating \(G\).
- Its two difference-\(\pm1\) rays \(X\), annihilating \(U\).
- Its two difference-\(\pm2\) rays \(Y\), annihilating \(V\).

These are orthogonal rank-two group projections summing to \(I\). The lemma makes them reduce \(G,U,V\). The same applies to each physical column.

For an individual off-diagonal ray \(q\), its row and column group planes contain \(q\) and reduce the common sectors. **Nonparallelness is indispensable here.** If the planes were equal, the row and column partner rays would be parallel in their common one-dimensional complement to \(q\). They occupy distinct actual cells, since a physical row and column meet only at \(q\).

The planes are therefore distinct two-planes with intersection exactly \(\mathbb Cq\). Their common reducing operators preserve that intersection, so precisely one of \(G,U,V\) acts as identity on \(q\). The individual ray—not merely its containing block—is in one common sector.

Every physical row and column consequently has two rays in each common two-sector. The sector partner of any \(q\) in its row and in its column must again be parallel at distinct cells. This excludes the rank-two regime.

### Exact local control for omitting nonparallelness

In \(\mathbb R^6\), take

\[
G=\langle e_0,e_1\rangle,\quad
U=\langle e_2,e_3\rangle,\quad
V=\langle e_4,e_5\rangle,
\]

and group planes

\[
R=\langle e_2,e_5\rangle,\quad
X=\langle e_0,e_4\rangle,\quad
Y=\langle e_1,e_3\rangle.
\]

They form a projection partition with \(RG=XU=YV=0\), and reduce \(G,U,V\). Let

\[
q=(3e_0+4e_4)/5,\qquad x=(4e_0-3e_4)/5.
\]

They are an ONB of \(X\). Use this same plane and basis for two locally labelled row/column group planes. Then:

- Both containing rank-two planes reduce all three sectors.
- \(q\) is **not** in any single sector.
- Its rank-one projector does **not** commute with \(G\).
- The partner \(x\) is repeated.

This disproves the false inference “the block reduces the sectors, therefore every ray does.” It also shows why equal group planes cannot be excluded without nonparallelness.

It is **only a local countermodel to weakened consumer hypotheses**. It does not satisfy, or claim to satisfy, sixty physical ONBs.

## 8. Forty affine maps and the scoped union

For each \(h\in\{1,3,7,9\}\), \(t\in\mathbb Z_{10}\),

\[
(r,c)\mapsto(hr,hc+t)
\]

permutes actual rows and columns and sends symbols and differences by

\[
r+c\mapsto h(r+c)+t,\qquad
c-r\mapsto h(c-r)+t.
\]

No vector covariance is imposed.

For \(S=\{0,1,3,4\}\),

\[
3S=S+9,\quad7S=S+7,\quad9S=S+6.
\]

Its ten orbit masks are its ten distinct translates:

\[
\begin{gathered}
0134,\ 1245,\ 2356,\ 3467,\ 4578,\\
5689,\ 0679,\ 0178,\ 1289,\ 0239.
\end{gathered}
\]

Here each string denotes a four-element subset, not a number. All forty group elements act; each image occurs four times.

The frozen S2 disposition supplies the prior partition:

- Sixty balanced masks containing a nondegenerate three-term AP.
- Twenty masks in the affine orbit of \(\{0,1,3,8\}\).
- Ten masks in the orbit of \(\{0,1,5,6\}\).
- Ten masks in the present orbit.

The other ten-mask orbit consists exactly of unions of two antipodal pairs. It is disjoint from the present orbit. Its proof is **not** an input to this assignment.

The set bookkeeping is

\[
60+20+10+10=100.
\]

This does **not** adopt either unadopted ten-mask theorem. Even a future accepted union would exclude only the specified cyclic, circulant, actual orthogonal four-sector completions—not noncirculant supports, other resolutions, rank-28 \(5+5\) branches, irreducible arrays, or the unrestricted hundred-ray problem.

## 9. Control and execution receipt

**Observed scientific execution:** NOTRUN.

Every executable control below is therefore **NOTTESTED_BY_EXECUTION** in this return. The intended rejection reasons are explicit in the complete source:

| Mutation / weakened inference | Intended reason |
|---|---|
| Reverse the column shift | `SUPPORT_MISMATCH` |
| Reverse off-diagonal parity classes | `SUPPORT_MISMATCH` |
| Use 2 instead of 3 for the physical symbol inverse | `SYMBOL_ROUTE` |
| Omit the symbol ONB family | `CONTEXT_FAMILY` |
| Infer Hermiticity from the even four-cycle | `HERMITIAN_PRODUCT` |
| Identify product rank with intersection dimension before commutation | `PRODUCT_IS_NOT_INTERSECTION` |
| Reuse a coordinate line in two coordinate bases | `COORDINATE_RAY_REUSE` |
| Route through equal planes without nonparallel partners | `GLOBAL_NONPARALLEL_REQUIRED` |
| Route an individual mixed ray merely from its reducing block | `INDIVIDUAL_RAY_MIXED` |
| Substitute the other ten-mask pattern for this orbit | `WRONG_ORBIT` |

The explicit rational countermodels and algebra above explain why the controls target their intended hypotheses. They are not substituted for an observed program run.

## 10. Complete unexecuted finite verifier source

**Proposed filename:** `f573-finite-verifier-v1.py`  
**Exact proposed argv:** `python3 -B f573-finite-verifier-v1.py`  
**Status:** **NOTRUN.**

Only standard-library imports are used. There is no filesystem data I/O, network, child process, installation, deletion, or background work. Output is stdout only. The cooperative deadline is 55 seconds, checked throughout the bounded calculations.

To preserve the full source without a fenced code block, every source line below has the literal prefix `PY|`. Remove exactly that three-character prefix from every such line; no other transformation or omitted source is required.

PY|from collections import Counter
PY|from fractions import Fraction as F
PY|from itertools import combinations, product
PY|from time import monotonic
PY|
PY|START = monotonic()
PY|LIMIT = 55.0
PY|REJECTIONS = []
PY|S = frozenset((0, 1, 3, 4))
PY|T = frozenset((2, 5, 6, 7, 8, 9))
PY|
PY|class CheckError(Exception):
PY|    pass
PY|
PY|def tick():
PY|    if monotonic() - START > LIMIT:
PY|        raise CheckError("TIME_BOUND")
PY|
PY|def need(condition, reason):
PY|    tick()
PY|    if not condition:
PY|        raise CheckError(reason)
PY|
PY|def reject(name, reason, operation):
PY|    try:
PY|        operation()
PY|    except CheckError as error:
PY|        need(str(error) == reason, "UNINTENDED_REJECTION:" + name)
PY|        REJECTIONS.append((name, reason))
PY|    else:
PY|        raise CheckError("MUTATION_ACCEPTED:" + name)
PY|
PY|def crt(a, u):
PY|    a %= 5
PY|    u %= 2
PY|    return a + 5 * ((u - a) % 2)
PY|
PY|def tau(a, b):
PY|    need(a != b, "DIAGONAL_TAU")
PY|    return int((b - a) % 5 in (2, 3))
PY|
PY|def D(a, u, v):
PY|    return ("D", a % 5, u % 2, v % 2)
PY|
PY|def O(a, b, u):
PY|    return ("O", a % 5, b % 5, u % 2)
PY|
PY|LABELS = tuple(
PY|    [D(a, u, v) for a, u, v in product(range(5), range(2), range(2))]
PY|    + [O(a, b, u) for a, b, u in product(range(5), range(5), range(2))
PY|       if a != b]
PY|)
PY|UNIVERSE = frozenset(
PY|    (r, c) for r, c in product(range(10), repeat=2)
PY|    if (c - r) % 10 in T
PY|)
PY|
PY|def cell(label, shift=2, flip=False):
PY|    if label[0] == "D":
PY|        _, a, u, v = label
PY|        b = a
PY|    else:
PY|        _, a, b, u = label
PY|        v = (u + tau(a, b) + int(flip)) % 2
PY|    return (crt(a, u), (crt(b, v) + shift) % 10)
PY|
PY|def mapping(shift=2, flip=False):
PY|    return {label: cell(label, shift, flip) for label in LABELS}
PY|
PY|def actual_contexts(mp):
PY|    contexts = {(family, i): set() for family in ("R", "C", "L")
PY|                for i in range(10)}
PY|    for label, (r, c) in mp.items():
PY|        contexts["R", r].add(label)
PY|        contexts["C", c].add(label)
PY|        contexts["L", (r + c) % 10].add(label)
PY|    return {key: frozenset(value) for key, value in contexts.items()}
PY|
PY|def specified_contexts(inverse=3):
PY|    contexts = {}
PY|    for a, u in product(range(5), range(2)):
PY|        contexts["R", crt(a, u)] = frozenset(
PY|            [D(a, u, v) for v in range(2)]
PY|            + [O(a, b, u) for b in range(5) if b != a]
PY|        )
PY|    for b, v in product(range(5), range(2)):
PY|        contexts["C", (crt(b, v) + 2) % 10] = frozenset(
PY|            [D(b, u, v) for u in range(2)]
PY|            + [O(a, b, v - tau(a, b)) for a in range(5) if a != b]
PY|        )
PY|    for ell in range(10):
PY|        s, w = (ell - 2) % 5, (ell - 2) % 2
PY|        k = inverse * s % 5
PY|        step = 2 if w == 0 else 1
PY|        a, b = (k - step) % 5, (k + step) % 5
PY|        contexts["L", ell] = frozenset(
PY|            [D(k, 0, w), D(k, 1, w - 1)]
PY|            + [O(a, b, u) for u in range(2)]
PY|            + [O(b, a, u) for u in range(2)]
PY|        )
PY|    return contexts
PY|
PY|def validate(mp, contexts):
PY|    need(len(mp) == 60 and len(set(mp.values())) == 60, "CELL_BIJECTION")
PY|    need(frozenset(mp.values()) == UNIVERSE, "SUPPORT_MISMATCH")
PY|    keys = {(family, i) for family in ("R", "C", "L") for i in range(10)}
PY|    need(set(contexts) == keys, "CONTEXT_FAMILY")
PY|    actual = actual_contexts(mp)
PY|    for key in sorted(keys):
PY|        need(len(contexts[key]) == 6, "CONTEXT_SIZE")
PY|        reason = "SYMBOL_ROUTE" if key[0] == "L" else "ROW_COLUMN_ROUTE"
PY|        need(contexts[key] == actual[key], reason)
PY|    for family in ("R", "C", "L"):
PY|        counts = Counter(label for i in range(10)
PY|                         for label in contexts[family, i])
PY|        need(counts == Counter(LABELS), "CONTEXT_COVERAGE")
PY|
PY|def shared_context(x, y, mp):
PY|    r, c = mp[x]
PY|    s, d = mp[y]
PY|    return r == s or c == d or (r + c) % 10 == (s + d) % 10
PY|
PY|def projection_incidence(mp, contexts):
PY|    balance = []
PY|    for a in range(5):
PY|        diagonal = [D(a, u, v) for u, v in product(range(2), repeat=2)]
PY|        for x, y in combinations(diagonal, 2):
PY|            need(shared_context(x, y, mp), "DIAGONAL_ORTHOGONALITY_ROUTE")
PY|        rows = Counter(x for u in range(2)
PY|                       for x in contexts["R", crt(a, u)])
PY|        expected_rows = Counter(
PY|            diagonal + [O(a, b, u) for b in range(5) if b != a
PY|                        for u in range(2)]
PY|        )
PY|        need(rows == expected_rows, "ROW_SUM_PROJECTORS")
PY|        columns = Counter(x for v in range(2)
PY|                          for x in contexts["C", (crt(a, v) + 2) % 10])
PY|        expected_columns = Counter(
PY|            diagonal + [O(b, a, u) for b in range(5) if b != a
PY|                        for u in range(2)]
PY|        )
PY|        need(columns == expected_columns, "COLUMN_SUM_PROJECTORS")
PY|        coefficients = [0] * 10
PY|        for b in range(5):
PY|            if a == b:
PY|                continue
PY|            k = 3 * (a + b) % 5
PY|            offset = 0 if (b - a) % 5 in (1, 4) else 5
PY|            coefficients[offset + k] += 1
PY|            x, y = O(a, b, 0), O(a, b, 1)
PY|            need((sum(mp[x]) - sum(mp[y])) % 10 == 0,
PY|                 "TWO_CELL_SYMBOL")
PY|        coefficients[a] -= 2
PY|        coefficients[5 + a] -= 2
PY|        expected = [
PY|            -2 if j == a else int((j - a) % 5 in (2, 3))
PY|            for j in range(5)
PY|        ] + [
PY|            -2 if j == a else int((j - a) % 5 in (1, 4))
PY|            for j in range(5)
PY|        ]
PY|        need(coefficients == expected, "BALANCE_COEFFICIENT_ROW")
PY|        balance.append(tuple(coefficients))
PY|    for k, w in product(range(5), range(2)):
PY|        step = 2 if w == 0 else 1
PY|        a, b = (k - step) % 5, (k + step) % 5
PY|        labels = [D(k, 0, w), D(k, 1, w - 1)]
PY|        labels += [O(a, b, u) for u in range(2)]
PY|        labels += [O(b, a, u) for u in range(2)]
PY|        ell = (crt(2 * k, w) + 2) % 10
PY|        need(len(set(labels)) == 6, "SYMBOL_PARTITION_DISJOINT")
PY|        need(frozenset(labels) == contexts["L", ell],
PY|             "SYMBOL_PROJECTOR_PARTITION")
PY|    return balance
PY|
PY|def mat(rows):
PY|    return [[F(x) for x in row] for row in rows]
PY|
PY|def diag(n, indices):
PY|    indices = set(indices)
PY|    return mat([[int(i == j and i in indices) for j in range(n)]
PY|                for i in range(n)])
PY|
PY|def transpose(a):
PY|    return [list(row) for row in zip(*a)]
PY|
PY|def mm(a, b):
PY|    tick()
PY|    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
PY|             for j in range(len(b[0]))] for i in range(len(a))]
PY|
PY|def plus(a, b, scale=1):
PY|    return [[a[i][j] + scale * b[i][j] for j in range(len(a[0]))]
PY|            for i in range(len(a))]
PY|
PY|def rank(a):
PY|    a = mat(a)
PY|    row = 0
PY|    for col in range(len(a[0])):
PY|        tick()
PY|        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
PY|        if pivot is None:
PY|            continue
PY|        a[row], a[pivot] = a[pivot], a[row]
PY|        divisor = a[row][col]
PY|        a[row] = [x / divisor for x in a[row]]
PY|        for i in range(len(a)):
PY|            if i != row and a[i][col]:
PY|                factor = a[i][col]
PY|                a[i] = [x - factor * y for x, y in zip(a[i], a[row])]
PY|        row += 1
PY|        if row == len(a):
PY|            break
PY|    return row
PY|
PY|def determinant(a):
PY|    a = mat(a)
PY|    result = F(1)
PY|    for j in range(len(a)):
PY|        tick()
PY|        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
PY|        if pivot is None:
PY|            return F(0)
PY|        if pivot != j:
PY|            a[j], a[pivot] = a[pivot], a[j]
PY|            result = -result
PY|        value = a[j][j]
PY|        result *= value
PY|        for i in range(j + 1, len(a)):
PY|            factor = a[i][j] / value
PY|            a[i] = [x - factor * y for x, y in zip(a[i], a[j])]
PY|    return result
PY|
PY|def outer(v):
PY|    return [[x * y for y in v] for x in v]
PY|
PY|def vector(n, entries):
PY|    return [F(entries.get(i, 0)) for i in range(n)]
PY|
PY|def is_projection(a):
PY|    return a == transpose(a) and mm(a, a) == a
PY|
PY|def intersection_dimension(a, b):
PY|    joined = [x + y for x, y in zip(a, b)]
PY|    return rank(a) + rank(b) - rank(joined)
PY|
PY|def circular_linear_certificate():
PY|    L = mat([[0 if i == j else
PY|              (1 if (j - i) % 5 in (2, 3) else -1)
PY|              for j in range(5)] for i in range(5)])
PY|    need(all(sum(row) == 0 for row in L), "CONSTANT_KERNEL")
PY|    target = mat([[5 * int(i == j) - 1 for j in range(5)]
PY|                  for i in range(5)])
PY|    need(mm(L, L) == target, "L_SQUARED_CERTIFICATE")
PY|    need(rank(L) == 4, "CIRCULANT_RANK")
PY|    minor = [row[:4] for row in L[:4]]
PY|    need(determinant(minor) == 5, "CIRCULANT_COFACTOR")
PY|    restricted = [[L[i][j] - L[i][4] for j in range(4)] for i in range(4)]
PY|    need(determinant(restricted) == 25, "NONCONSTANT_DETERMINANT")
PY|    augmented = [[L[i][j] + F(1, 5) for j in range(5)]
PY|                 for i in range(5)]
PY|    need(determinant(augmented) == 25, "CONSTANT_COMPLEMENT_DETERMINANT")
PY|    return L, restricted
PY|
PY|def linear_combination(terms):
PY|    result = Counter()
PY|    for scale, polynomial in terms:
PY|        for key, value in polynomial.items():
PY|            result[key] += scale * value
PY|    return {key: value for key, value in result.items() if value}
PY|
PY|def formal_cycles():
PY|    def outside(neighbor, center):
PY|        difference = (neighbor - center) % 5
PY|        need(difference != 0, "CONTAINMENT_DIAGONAL")
PY|        return "U" if difference in (1, 4) else "V"
PY|    covered = set()
PY|    orders = []
PY|    for step in (1, 2):
PY|        order = tuple(step * j % 5 for j in range(5))
PY|        need(len(set(order)) == 5 and len(order) % 2 == 1, "ODD_CYCLE")
PY|        orders.append(order)
PY|        for a in range(5):
PY|            p, q, r = (a - step) % 5, a, (a + step) % 5
PY|            at_r = (outside(p, r), outside(q, r))
PY|            at_p = (outside(r, p), outside(q, p))
PY|            need(set(at_r) == {"U", "V"}, "P_R_Q_CONTAINMENT")
PY|            need(set(at_p) == {"U", "V"}, "R_P_Q_CONTAINMENT")
PY|            need(({"E", at_r[0]} & {"E", at_r[1]}) == {"E"},
PY|                 "PARTITION_PRODUCT_REDUCTION")
PY|            covered.add(frozenset((a, (a + step) % 5)))
PY|    need(orders == [(0, 1, 2, 3, 4), (0, 2, 4, 1, 3)], "BOTH_CYCLES")
PY|    need(covered == {frozenset(pair) for pair in combinations(range(5), 2)},
PY|         "ALL_DISTINCT_PRODUCTS")
PY|    norm_square = {"yy": 1, "zz": 1, "yz": -1, "zy": -1}
PY|    relations = [
PY|        {"yz": 1, "yy": -1}, {"zy": 1, "yy": -1},
PY|        {"yz": 1, "zz": -1}, {"zy": 1, "zz": -1}
PY|    ]
PY|    need(linear_combination([(-1, relation) for relation in relations])
PY|         == linear_combination([(2, norm_square)]),
PY|         "CONTRACTION_NORM_CERTIFICATE")
PY|    need([g for g in range(3) if g + 5 * (2 - g) <= 6] == [1, 2],
PY|         "RANK_REGIME_EXHAUSTION")
PY|
PY|def reduce_word(word):
PY|    word = list(word)
PY|    while True:
PY|        changed = False
PY|        for j in range(len(word) - 1):
PY|            left, right = word[j], word[j + 1]
PY|            if left[0] == right[0]:
PY|                if left[1] != right[1]:
PY|                    return None
PY|                del word[j + 1]
PY|                changed = True
PY|                break
PY|            if left[1] == right[1]:
PY|                return None
PY|        if not changed:
PY|            return tuple(word)
PY|
PY|def reduce_polynomial(terms):
PY|    result = Counter()
PY|    for coefficient, word in terms:
PY|        reduced = reduce_word(word)
PY|        if reduced is not None:
PY|            result[reduced] += coefficient
PY|    return {word: coefficient for word, coefficient in result.items()
PY|            if coefficient}
PY|
PY|def three_partition_certificate():
PY|    count = 0
PY|    for i, j, k in product(range(3), repeat=3):
PY|        if j == k:
PY|            continue
PY|        A_j, A_k = ("A", j), ("A", k)
PY|        if i in (j, k):
PY|            terms = [(1, (A_j, ("Q", i), A_k))]
PY|        else:
PY|            terms = [
PY|                (1, (A_j, A_k)),
PY|                (-1, (A_j, ("Q", j), A_k)),
PY|                (-1, (A_j, ("Q", k), A_k))
PY|            ]
PY|        need(reduce_polynomial(terms) == {}, "THREE_PARTITION_SANDWICH")
PY|        count += 1
PY|    need(count == 18, "THREE_PARTITION_COVERAGE")
PY|
PY|def g1_patterns():
PY|    planes = {}
PY|    for a in range(5):
PY|        planes["U", a] = frozenset(((a - 1) % 5, (a + 1) % 5))
PY|        planes["V", a] = frozenset(((a - 2) % 5, (a + 2) % 5))
PY|    need(set(planes.values())
PY|         == {frozenset(pair) for pair in combinations(range(5), 2)},
PY|         "G1_TEN_LINE_PAIRS")
PY|    def coordinate_choice(choice):
PY|        used = [line for key in choice for line in planes[key]]
PY|        need(len(set(used)) == len(used), "COORDINATE_RAY_REUSE")
PY|    reject("coordinate pair reuse", "COORDINATE_RAY_REUSE",
PY|           lambda: coordinate_choice((("U", 0), ("U", 2))))
PY|    histogram = Counter()
PY|    patterns = []
PY|    dispatches = 0
PY|    keys = tuple(sorted(planes))
PY|    for size in range(3):
PY|        for choice in combinations(keys, size):
PY|            tick()
PY|            used = [line for key in choice for line in planes[key]]
PY|            if len(set(used)) != len(used):
PY|                continue
PY|            coordinate_choice(choice)
PY|            good = {a for a in range(5)
PY|                    if ("U", a) not in choice and ("V", a) not in choice}
PY|            need(len(good) >= 3, "GOOD_INDEX_COUNT")
PY|            patterns.append(choice)
PY|            histogram[len(good)] += 1
PY|            for a, b in product(sorted(good), repeat=2):
PY|                if a == b:
PY|                    continue
PY|                k = 3 * (a + b) % 5
PY|                need(k not in (a, b), "MIDPOINT_ENDPOINT")
PY|                support = {a, b, k}
PY|                killed = {}
PY|                for endpoint in (a, b):
PY|                    hits = [planes[group, endpoint] & support
PY|                            for group in ("U", "V")]
PY|                    need(all(len(hit) == 1 for hit in hits),
PY|                         "NONZERO_COEFFICIENT_SINGLETON")
PY|                    killed[endpoint] = set().union(*hits)
PY|                need(support - killed[a] == {a}, "GOOD_ROW_TO_E_A")
PY|                need(support - killed[b] == {b}, "GOOD_COLUMN_TO_E_B")
PY|                need((support - killed[a]) & (support - killed[b]) == set(),
PY|                     "GOOD_ENDPOINTS_TO_G")
PY|                for u in range(2):
PY|                    v = (u + tau(a, b)) % 2
PY|                    need({"U" if u == bit else "V" for bit in range(2)}
PY|                         == {"U", "V"}, "ROW_DIAGONAL_PLANE_DISPATCH")
PY|                    need({"U" if bit == v else "V" for bit in range(2)}
PY|                         == {"U", "V"}, "COLUMN_DIAGONAL_PLANE_DISPATCH")
PY|                    dispatches += 1
PY|    need(len(patterns) == 26, "COORDINATE_PATTERN_TOTAL")
PY|    need(histogram == Counter({5: 1, 4: 15, 3: 10}), "GOOD_PATTERN_HISTOGRAM")
PY|    need(sum(len(choice) == 2 for choice in patterns) == 15,
PY|         "TWO_COORDINATE_PATTERN_TOTAL")
PY|    need(dispatches == 520, "GOOD_DISPATCH_TOTAL")
PY|    return histogram, dispatches
PY|
PY|def local_route(row_plane, column_plane, q, row_mate, column_mate, sectors):
PY|    pq, pr, pc = outer(q), outer(row_mate), outer(column_mate)
PY|    for plane, mate in ((row_plane, pr), (column_plane, pc)):
PY|        need(is_projection(plane) and rank(plane) == 2, "LOCAL_GROUP_PLANE")
PY|        need(is_projection(pq) and is_projection(mate), "LOCAL_UNIT_RAYS")
PY|        need(plus(pq, mate) == plane, "LOCAL_GROUP_ONB")
PY|        need(all(mm(plane, a) == mm(a, plane) for a in sectors),
PY|             "LOCAL_REDUCING_PLANE")
PY|    need(pr != pc, "GLOBAL_NONPARALLEL_REQUIRED")
PY|    need(row_plane != column_plane, "DISTINCT_PLANES_REQUIRED")
PY|    need(intersection_dimension(row_plane, column_plane) == 1,
PY|         "LOCAL_INTERSECTION_LINE")
PY|    need(sum(mm(a, pq) == pq for a in sectors) == 1,
PY|         "INDIVIDUAL_RAY_MIXED")
PY|
PY|def local_matrix_controls():
PY|    P = diag(4, (0, 1))
PY|    rotation = vector(4, {1: F(3, 5), 2: F(4, 5)})
PY|    Q = plus(diag(4, (0,)), outer(rotation))
PY|    need(is_projection(P) and is_projection(Q), "ROTATION_PROJECTIONS")
PY|    need(rank(P) == rank(Q) == 2, "ROTATION_RANK_TWO")
PY|    PQ, QP = mm(P, Q), mm(Q, P)
PY|    products = [PQ, QP, PQ, QP]
PY|    need(all(products[j] == transpose(products[(j + 1) % 4])
PY|             for j in range(4)), "EVEN_CYCLE_ADJOINT_RELATIONS")
PY|    reject("even four cycle", "HERMITIAN_PRODUCT",
PY|           lambda: need(PQ == transpose(PQ), "HERMITIAN_PRODUCT"))
PY|    need(rank(PQ) == 2 and intersection_dimension(P, Q) == 1,
PY|         "ROTATION_INTERSECTION_COUNTS")
PY|    reject("product rank versus intersection", "PRODUCT_IS_NOT_INTERSECTION",
PY|           lambda: need(rank(PQ) == intersection_dimension(P, Q),
PY|                        "PRODUCT_IS_NOT_INTERSECTION"))
PY|    G, U, V = diag(6, (0, 1)), diag(6, (2, 3)), diag(6, (4, 5))
PY|    R, X, Y = diag(6, (2, 5)), diag(6, (0, 4)), diag(6, (1, 3))
PY|    zero = diag(6, ())
PY|    need(plus(plus(R, X), Y) == diag(6, range(6)), "LOCAL_PARTITION_SUM")
PY|    need(mm(R, X) == mm(R, Y) == mm(X, Y) == zero,
PY|         "LOCAL_PARTITION_ORTHOGONAL")
PY|    need(mm(R, G) == mm(X, U) == mm(Y, V) == zero,
PY|         "LOCAL_MATCHING_ANNIHILATIONS")
PY|    need(all(mm(group, sector) == mm(sector, group)
PY|             for group in (R, X, Y) for sector in (G, U, V)),
PY|         "LOCAL_THREE_PARTITION_COMMUTATION")
PY|    q = vector(6, {0: F(3, 5), 4: F(4, 5)})
PY|    mate = vector(6, {0: F(4, 5), 4: F(-3, 5)})
PY|    need(plus(outer(q), outer(mate)) == X, "MIXED_LOCAL_ONB")
PY|    need(mm(G, outer(q)) != mm(outer(q), G), "MIXED_RAY_NONCOMMUTATION")
PY|    reject("equal planes with repeated partner", "GLOBAL_NONPARALLEL_REQUIRED",
PY|           lambda: local_route(X, X, q, mate, mate, (G, U, V)))
PY|    reject("reducing block to individual ray", "INDIVIDUAL_RAY_MIXED",
PY|           lambda: need(sum(mm(a, outer(q)) == outer(q) for a in (G, U, V))
PY|                        == 1, "INDIVIDUAL_RAY_MIXED"))
PY|    e0, e4, e5 = (vector(6, {j: 1}) for j in (0, 4, 5))
PY|    local_route(diag(6, (0, 4)), diag(6, (0, 5)),
PY|                e0, e4, e5, (G, U, V))
PY|
PY|def orbit(mask):
PY|    return {frozenset((h * x + t) % 10 for x in mask)
PY|            for h in (1, 3, 7, 9) for t in range(10)}
PY|
PY|def mask_and_affine_checks():
PY|    balanced = {frozenset(mask) for mask in combinations(range(10), 4)
PY|                if sum(x % 2 == 0 for x in mask) == 2}
PY|    triples = {
PY|        frozenset((a, (a + d) % 10, (a + 2 * d) % 10))
PY|        for a in range(10) for d in range(1, 10)
PY|        if len({a, (a + d) % 10, (a + 2 * d) % 10}) == 3
PY|    }
PY|    ap = {mask for mask in balanced if any(triple <= mask for triple in triples)}
PY|    extra = orbit(frozenset((0, 1, 3, 8)))
PY|    other = orbit(frozenset((0, 1, 5, 6)))
PY|    new = orbit(S)
PY|    parts = (ap, extra, other, new)
PY|    need(tuple(map(len, parts)) == (60, 20, 10, 10), "MASK_PARTITION_COUNTS")
PY|    need(all(not (left & right) for left, right in combinations(parts, 2)),
PY|         "MASK_PARTITION_DISJOINT")
PY|    need(set().union(*parts) == balanced and len(balanced) == 100,
PY|         "FULL_BALANCED_MASK_UNION")
PY|    antipodal = {frozenset((a, a + 5, b, b + 5))
PY|                 for a, b in combinations(range(5), 2)}
PY|    need(other == antipodal, "OTHER_ORBIT_ANTIPODAL")
PY|    need(new == {frozenset((x + t) % 10 for x in S) for t in range(10)},
PY|         "NEW_ORBIT_TRANSLATIONS")
PY|    reject("other ten-mask pattern", "WRONG_ORBIT",
PY|           lambda: need(frozenset((0, 1, 5, 6)) in new, "WRONG_ORBIT"))
PY|    image_counts = Counter()
PY|    map_count = 0
PY|    for h, t in product((1, 3, 7, 9), range(10)):
PY|        tick()
PY|        image = frozenset((h * x + t) % 10 for x in S)
PY|        image_counts[image] += 1
PY|        cells = set()
PY|        for r, c in product(range(10), repeat=2):
PY|            nr, nc = h * r % 10, (h * c + t) % 10
PY|            cells.add((nr, nc))
PY|            need((nr + nc) % 10 == (h * (r + c) + t) % 10,
PY|                 "AFFINE_SYMBOL_CONSUMER")
PY|            need((nc - nr) % 10 == (h * (c - r) + t) % 10,
PY|                 "AFFINE_DIFFERENCE_CONSUMER")
PY|        need(len(cells) == 100, "AFFINE_CELL_BIJECTION")
PY|        transformed = {(h * r % 10, (h * c + t) % 10) for r, c in UNIVERSE}
PY|        expected = {(r, c) for r, c in product(range(10), repeat=2)
PY|                    if (c - r) % 10 not in image}
PY|        need(transformed == expected, "AFFINE_COMPLEMENT_CONSUMER")
PY|        map_count += 1
PY|    need(map_count == 40 and len(image_counts) == 10
PY|         and set(image_counts.values()) == {4}, "AFFINE_ORBIT_MULTIPLICITIES")
PY|    return tuple(map(len, parts)), len(balanced), map_count
PY|
PY|def main():
PY|    mp = mapping()
PY|    contexts = specified_contexts()
PY|    validate(mp, contexts)
PY|    reject("reversed column shift", "SUPPORT_MISMATCH",
PY|           lambda: validate(mapping(shift=-2), contexts))
PY|    reject("reversed parity classes", "SUPPORT_MISMATCH",
PY|           lambda: validate(mapping(flip=True), contexts))
PY|    reject("wrong physical symbol inverse", "SYMBOL_ROUTE",
PY|           lambda: validate(mp, specified_contexts(inverse=2)))
PY|    missing_symbols = {key: value for key, value in contexts.items()
PY|                       if key[0] != "L"}
PY|    reject("missing symbol ONB family", "CONTEXT_FAMILY",
PY|           lambda: validate(mp, missing_symbols))
PY|    balance = projection_incidence(mp, contexts)
PY|    L, restricted = circular_linear_certificate()
PY|    formal_cycles()
PY|    three_partition_certificate()
PY|    histogram, dispatches = g1_patterns()
PY|    local_matrix_controls()
PY|    counts, total, affine_maps = mask_and_affine_checks()
PY|    need(len(REJECTIONS) == 10, "CONTROL_COVERAGE")
PY|    tick()
PY|    print("RESULT: PASS_FINITE_INTERFACES_ONLY")
PY|    print("PHYSICAL_CELLS", len(mp))
PY|    print("CONTEXTS", len(contexts), "SIZE", 6)
PY|    print("BALANCE_ROWS", balance)
PY|    print("CIRCULANT", L)
PY|    print("SUM_ZERO_RESTRICTION", restricted)
PY|    print("GOOD_PATTERN_HISTOGRAM", sorted(histogram.items()))
PY|    print("GOOD_ENDPOINT_BIT_DISPATCHES", dispatches)
PY|    print("MASK_PARTITION", counts, "UNION", total, "AFFINE_MAPS", affine_maps)
PY|    for name, reason in REJECTIONS:
PY|        print("CONTROL_REJECTED", name, reason)
PY|    print("LIMITS: no physical vector witness, no operator-proof automation,")
PY|    print("no theorem adoption, no unrestricted hundred-ray conclusion.")
PY|    print("ELAPSED_SECONDS", monotonic() - START)
PY|
PY|if __name__ == "__main__":
PY|    main()

## 11. Exact unpaid steps and final disposition

1. **Executable evidence is unpaid.** The complete source above has not been run, so there is no observed exit code, stdout, timing, or executed mutation receipt. The expected numerical assertions are not represented as observed output.
2. **General written operator gates remain separate.** This return reconstructs the contraction, both cycle dispatches, rank split, and both individual-ray consumers; it does not replace the independently assigned written gates.
3. **Parent disposition remains unpaid.** This return does not adopt f557, adopt the other ten-mask candidate, or promote the documentary union to a scientific conclusion.
4. **The unrestricted original target remains unresolved.**

**Overall correctness:** correct within the inspected frozen candidate’s stated scope; no candidate defect found.  
**Explanation:** The physical \(r+c\) routing, five balance rows, both odd-cycle interfaces, rank-one coefficient consumers, and rank-two individual-ray consumer are consistent under the explicitly stated ONB and global nonparallelness hypotheses. The finite verifier and all executable controls are supplied in full but remain NOTRUN; no acceptance or global-target conclusion follows from this return alone.  
**Confidence:** 0.90.