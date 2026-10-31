# F533 — WRITTEN review: forty-ray realization, affine orbit, and six-dimensional complement

**Disposition:** SUPPORTED at the stated forty-ray and conditional-complement scopes.  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Scientific execution in this review:** **NOTRUN.**

This is the complete review body for parent materialization as this wave’s `review-v1.md`. No working-tree file was written.

## 1. Frozen inputs, coverage, and method

Wave root:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f533-rqls10-forty-ray-distinctness-affine-orbit-and-complement-review/`

Frozen identifiers:

- Manifest SHA-256: `7e57a3ec1c900d628f06b7f2ac879e36b38d19a1ac864b3144b25ee906e3cefe`.
- Freeze-receipt SHA-256: `098adbeaffb29aa3ba290297469597fe36f5947bc615f77f0436a5e31d7b655e`.
- Literal-packet SHA-256: `8a001dba7c28d067319f951e9a51b2ded2da18f44eb321007018eda6fc68f461`.

Mathematical inputs were exactly:

**S1 — fresh author body**

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f496-rqls10-rank28-5plus5-or-remaining-cyclic-4sector-frontier/review-v1.md`

- Whole-file SHA-256: `b12cd548fbb850d1c13d2cb06cc0e2a47adf7a34b919bec68bff70d4ed0a6784`.
- Authorized coverage: **LF1–332 only**, out of the parent-reported 584 LF.
- The optional checker and all later source lines were excluded and not read.

**S2 — original hypotheses and earlier scoped sector theorem**

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-5-rqls10-binary-sector-and-cyclic-rank4-family-exclusions-parent-v1.md`

- Whole-file SHA-256: `a4c7197d031810d9986249612b98749efc2edf705986808b718c609b9704152b`.
- Authorized coverage: **complete LF1–29**.

Before mathematical packet reading, I completed the manifest, freeze receipt, and all twelve listed status-only controls, including their endings, and sent the direct administrative pre-body ACK. Subsequently I read the complete **363-LF packet**, in consecutive exact raw windows of at most twenty LF, through S1 LF332 and S2 LF29, before deriving the review below. No raw packet elision remained.

Live hashes, byte/LF counts, and the supplied clock `2026-10-30T12:45:20-0700 PDT` are **parent observations**, not reviewer-native execution, reviewer start time, or an independently measured clock. I performed no hash/date command.

This review uses written identities quantified over their displayed variables and the author’s explicitly specified matrices and angles. It uses no additional selected concrete parameter, orientation probe, numerical example, scientific executable, CAS, enumeration, solver, author checker, sibling review, or linked-source follow. All quarantined episodes and consumers remain status-only NONINPUT.

The parent’s separately reported author-checker execution is not a premise of this review and is not represented as independent finite verification.

## 2. Claim-by-claim assessment

| Claim | Source scope | Assessment |
|---|---|---|
| CRT support and all thirty restricted-context memberships | S1 LF43–71 | **SUPPORTED** |
| Explicit unit vectors and operator identities | S1 LF75–220 | **SUPPORTED** |
| Ten block assignments give every restricted row, column, and symbol an ONB | S1 LF144–274 | **SUPPORTED** |
| All forty cell rays are pairwise nonparallel over complex scalars | S1 LF278–294 | **SUPPORTED** |
| Cell relabeling realizes the complete ten-mask antipodal-pair orbit | S1 LF298–304 | **SUPPORTED** |
| Full orthogonal \(4+6\) realization on a fixed such support is equivalent to its sixty-ray complementary problem | S1 LF306–316; S2 LF7 | **SUPPORTED** |
| Two-dimensional ray sectors are impossible; a putative cyclic six-dimensional complement cannot split into smaller orthogonal ray sectors | S1 LF318; S2 LF7,11–13 | **SUPPORTED**, with the precise sector meaning established below |
| Existence or impossibility of the required sixty-ray complement | S1 LF15,308–318 | **INCONCLUSIVE / NOT PROVED** |
| An actual full hundred-ray witness or unrestricted full-target no-go | S1 LF15,325–328 | **NOT SUPPLIED / NOT ESTABLISHED** |

No reviewed mathematical claim is REFUTED.

## 3. Physical vectors and exact cell assignment

The original physical requirement is one hundred pairwise nonparallel cell rays in \(\mathbb C^{10}\), with each of ten rows, ten columns, and ten Latin-resolution classes an ONB. Here the resolution is specifically

\[
L(r,c)=r+c\pmod {10}.
\]

The new construction supplies only the forty cells

\[
H_S=\{(r,c):c-r\in S\},\qquad S=\{0,1,5,6\}.
\]

Write CRT coordinates

\[
r\leftrightarrow(a,u),\qquad c\leftrightarrow(b,v),
\]

where \(a,b\in\mathbb Z_5\) and \(u,v\in\mathbb Z_2\). The inverse used by the author is

\[
\operatorname{crt}(a,u)=a+5((u-a)\bmod2).
\]

Reduction modulo five sends the two antipodal pairs in \(S\) to \(0\) and \(1\). Conversely, each of those residues has exactly its two displayed lifts modulo ten. Therefore

\[
(r,c)\in H_S\quad\Longleftrightarrow\quad b-a\in\{0,1\}\pmod5.
\]

Consequently the ten disjoint blocks are

\[
A_a=\{((a,u),(a,v)):u,v\in\mathbb Z_2\},
\]

\[
B_a=\{((a,u),(a+1,v)):u,v\in\mathbb Z_2\}.
\]

Each has four cells, giving exactly forty selected cells.

The author’s explicit two-component matrices are

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]

\[
N(\theta)=\cos\theta\,Z+\sin\theta\,X.
\]

The prescribed angles are

\[
\theta_1=0,\quad \theta_2=\frac{\pi}{4},\quad
\theta_3=\frac{\pi}{8},\quad \theta_4=\frac{3\pi}{8},
\qquad N_i=N(\theta_i).
\]

The five prescribed unitaries are

\[
U_0=I,\quad U_1=-Z,\quad
U_2=-e^{-iY\pi/4},\quad
U_3=N(-\pi/8),\quad U_4=-iY.
\]

The unit eigenvectors are

\[
w_0^\epsilon=\frac{1}{\sqrt2}(1,\epsilon i)^T,
\]

and, for \(1\leq i\leq4\),

\[
w_i^+=
\begin{pmatrix}\cos(\theta_i/2)\\ \sin(\theta_i/2)\end{pmatrix},
\qquad
w_i^-=
\begin{pmatrix}-\sin(\theta_i/2)\\ \cos(\theta_i/2)\end{pmatrix}.
\]

They satisfy

\[
Yw_0^\epsilon=\epsilon w_0^\epsilon,\qquad
N_iw_i^\epsilon=\epsilon w_i^\epsilon,
\]

and, for every fixed \(i\), the two choices of \(\epsilon\) are orthonormal.

The actual four-component vectors are

\[
Q_i^{\mathsf U}(\epsilon,\eta)
=\frac1{\sqrt2}
\begin{pmatrix}
w_i^\epsilon\\
\eta U_i^\dagger w_i^\epsilon
\end{pmatrix},
\]

\[
Q_i^{\mathsf V}(\epsilon,\eta)
=\frac1{\sqrt2}
\begin{pmatrix}
w_i^\epsilon\\
-i(-1)^i\eta U_i^\dagger w_i^\epsilon
\end{pmatrix},
\qquad \epsilon,\eta\in\{+1,-1\}.
\]

Their block lookup is:

| Block | Index | Branch |
|---|---:|---|
| \(A_0\) | 0 | \(\mathsf U\) |
| \(A_1\) | 3 | \(\mathsf V\) |
| \(A_2\) | 1 | \(\mathsf V\) |
| \(A_3\) | 4 | \(\mathsf U\) |
| \(A_4\) | 2 | \(\mathsf U\) |
| \(B_0\) | 4 | \(\mathsf V\) |
| \(B_1\) | 2 | \(\mathsf V\) |
| \(B_2\) | 0 | \(\mathsf V\) |
| \(B_3\) | 3 | \(\mathsf U\) |
| \(B_4\) | 1 | \(\mathsf U\) |

For its listed index and branch, the cell assignment is

\[
q_{A_a;u,v}
=Q_i^{\mathrm{branch}}\bigl((-1)^{u+v},(-1)^v\bigr),
\]

\[
q_{B_a;u,v}
=Q_i^{\mathrm{branch}}\bigl(-(-1)^{u+v},-(-1)^u\bigr).
\]

In each block, the map from \((u,v)\) to \((\epsilon,\eta)\) is bijective: in an \(A\)-block, \(\eta\) determines \(v\), and then \(\epsilon\) determines \(u\); in a \(B\)-block, \(\eta\) determines \(u\), and then \(\epsilon\) determines \(v\). Thus every listed block uses all four displayed vectors exactly once.

These formulas specify actual unit vectors, not merely an incidence selector or unspecified rays. Unitarity of \(U_i\) gives

\[
\left\|Q_i^{\mathrm{branch}}(\epsilon,\eta)\right\|^2
=\frac12\bigl(\|w_i^\epsilon\|^2+
\|U_i^\dagger w_i^\epsilon\|^2\bigr)=1.
\]

Both two-component blocks are nonzero.

## 4. Reconstruction of the operator certificate

The elementary Pauli multiplication gives the general identities

\[
N(\alpha)N(\beta)=e^{-iY(\alpha-\beta)},
\qquad
N(\alpha)e^{-iY\beta}=N(\alpha-\beta).
\]

Applied to the author’s displayed angles, these establish

\[
U_i=(-1)^iN_iU_{i-1}\qquad(1\leq i\leq4)
\]

with precisely the explicit \(U_i\) listed above. In particular,

\[
N_4N_3=N_2N_1=e^{-iY\pi/4},
\qquad U_4=-iY.
\]

For a two-dimensional unitary \(U\), define

\[
T(U)=\begin{pmatrix}0&U\\U^\dagger&0\end{pmatrix},
\qquad J(U)=T(iU).
\]

Then

\[
t_i=T(U_i),\qquad b_i=(-1)^iJ(U_i),
\]

\[
g_0=\operatorname{diag}(Y,Y),
\]

and, for \(1\leq i\leq4\),

\[
g_i=
\operatorname{diag}\bigl(N_i,U_{i-1}^\dagger N_iU_{i-1}\bigr).
\]

All these operators are Hermitian involutions. Each has two positive and two negative eigenvalues: this follows from the off-diagonal unitary form for \(t_i,b_i\), and from the two traceless Pauli-type blocks for \(g_i\).

For \(i\geq1\), block multiplication gives

\[
g_iT(U_{i-1})=T(N_iU_{i-1})
=T(U_{i-1})g_i.
\]

The corresponding identity with \(J\) also holds. Hence

\[
t_i=(-1)^ig_it_{i-1},
\qquad
b_i=-(-1)^ig_ib_{i-1},
\]

with the factors commuting, as claimed.

The two closing identities follow directly from \(U_0=I\) and \(U_4=-iY\):

\[
b_4=T(Y)=g_0t_0,
\]

\[
b_0t_4=
\begin{pmatrix}0&iI\\-iI&0\end{pmatrix}
\begin{pmatrix}0&-iY\\iY&0\end{pmatrix}
=-g_0.
\]

The reversed product in the latter identity is the same, so the relevant closing observables commute.

For \(i\geq1\),

\[
U_i^\dagger N_iU_i
=U_{i-1}^\dagger N_iU_{i-1}.
\]

This proves that \(Q_i^{\mathsf U}\) and \(Q_i^{\mathsf V}\) have \(g_i\)-eigenvalue \(\epsilon\). The case \(i=0\) follows from \(U_0=I\) and the \(Y\)-eigenvectors. Direct substitution gives

\[
t_iQ_i^{\mathsf U}(\epsilon,\eta)
=\eta Q_i^{\mathsf U}(\epsilon,\eta),
\]

\[
b_iQ_i^{\mathsf V}(\epsilon,\eta)
=\eta Q_i^{\mathsf V}(\epsilon,\eta).
\]

For either branch, different \(\epsilon\) give orthogonal vectors because both corresponding component inner products vanish. For fixed \(\epsilon\), opposite \(\eta\) give cancelling upper- and lower-block inner products. Each four-vector branch is therefore an ONB.

This establishes the required joint eigenbases explicitly; no unsupported inference from the word “independent” in S1 LF253 is needed.

## 5. Complete routing from blocks to physical contexts

Define the shared observables exactly as in S1:

| \(a\) | \(R_a\) | \(C_a\) | \(D_a\) |
|---:|---|---|---|
| 0 | \(b_4\) | \(t_0\) | \(g_0\) |
| 1 | \(b_2\) | \(b_3\) | \(g_3\) |
| 2 | \(b_0\) | \(b_1\) | \(g_1\) |
| 3 | \(t_3\) | \(t_4\) | \(g_4\) |
| 4 | \(t_1\) | \(t_2\) | \(g_2\) |

The recurrences and closing identities give the following complete ten-block check:

| Block | Ordered physical observables |
|---|---|
| \(A_0\) | \((g_0t_0,t_0,g_0)\) |
| \(A_1\) | \((g_3b_3,b_3,g_3)\) |
| \(A_2\) | \((g_1b_1,b_1,g_1)\) |
| \(A_3\) | \((g_4t_4,t_4,g_4)\) |
| \(A_4\) | \((g_2t_2,t_2,g_2)\) |
| \(B_0\) | \((b_4,-g_4b_4,g_4)\) |
| \(B_1\) | \((b_2,-g_2b_2,g_2)\) |
| \(B_2\) | \((b_0,-g_0b_0,g_0)\) |
| \(B_3\) | \((t_3,-g_3t_3,g_3)\) |
| \(B_4\) | \((t_1,-g_1t_1,g_1)\) |

For \(A_a\), these are \((R_a,C_a,D_a)\). For \(B_a\), they are \((R_a,C_{a+1},D_{a-2})\), with indices modulo five.

Thus every \(A\)-block has the form

\[
(R,C,D)=(gk,k,g),
\]

and every \(B\)-block has the form

\[
(R,C,D)=(k,-gk,g).
\]

All factors in each triple commute. Their products are respectively \(I\) and \(-I\).

Let \(x=(-1)^u\) and \(y=(-1)^v\). These are formal sign variables, not additional selected instances. The \(A\)-assignment has \((\epsilon,\eta)=(xy,y)\), so its physical eigenvalues are

\[
(R,C,D)=(x,y,xy).
\]

The \(B\)-assignment has \((\epsilon,\eta)=(-xy,-x)\), so its physical eigenvalues are

\[
(R,C,D)=(-x,-y,-xy).
\]

This verifies every entry of the author’s physical eigenvalue table, including the signs used when two different blocks meet a context.

### Rows

For every \((a,u)\), the four selected cells are the two \(A_a\)-cells and two \(B_a\)-cells with that \(u\).

The \(A_a\) pair is orthonormal and lies in the \(R_a=(-1)^u\) eigenspace. The \(B_a\) pair is orthonormal and lies in the opposite eigenspace. Both eigenspaces have dimension two. The four vectors therefore form an ONB.

This covers all five choices of \(a\) and both choices of \(u\): **all ten rows**.

### Columns

For every \((b,v)\), the selected cells are the two \(A_b\)-cells and two \(B_{b-1}\)-cells with that \(v\).

They occupy respectively

\[
C_b=(-1)^v,\qquad C_b=-(-1)^v.
\]

The same dimension and orthonormality argument proves **all ten columns**.

### Cyclic symbol classes

For a symbol \((s,w)\), an \(A_j\)-cell has

\[
2j=s\pmod5,\qquad u+v=w\pmod2.
\]

Since \(2^{-1}=3\pmod5\), its block index is \(a=3s\).

A \(B_j\)-cell has

\[
2j+1=s\pmod5,
\]

so \(j=3(s-1)=a+2\pmod5\). Thus the selected symbol cells are exactly two from \(A_a\) and two from \(B_{a+2}\), with \(u+v=w\).

Their symbol eigenvalues are

\[
D_a=(-1)^w,\qquad
D_{(a+2)-2}=D_a=-(-1)^w,
\]

respectively. These are complementary two-dimensional eigenspaces. Therefore **all ten symbol classes** are ONBs.

No context type or CRT-to-physical routing step is omitted.

## 6. All forty rays are globally distinct

The block table uses each \(i\in\{0,1,2,3,4\}\) once in branch \(\mathsf U\) and once in branch \(\mathsf V\). It therefore supplies eight candidate rays for each \(i\).

Every first two-component block is exactly \(w_i^\epsilon/\sqrt2\). Its underlying two-dimensional observable is one of

\[
Y,\quad Z,\quad N(\pi/4),\quad N(\pi/8),\quad N(3\pi/8).
\]

These are pairwise unequal even after multiplication by \(-1\). The four real-plane axes have distinct angles in a range shorter than \(\pi\); the \(Y\) axis is outside their real span in the Pauli basis.

For completeness, two traceless Hermitian two-dimensional involutions sharing an eigenray must equal one another up to sign: the orthogonal complement of that ray is also invariant for both, and their two diagonal eigenvalues are \(+1,-1\). Thus the listed unequal-up-to-sign axes have disjoint eigenray sets.

Consequently different indices \(i\) cannot produce parallel first blocks, and therefore cannot produce parallel four-component vectors.

For a fixed \(i\), opposite \(\epsilon\) give orthogonal first-block rays. For fixed \(i,\epsilon\), the four vectors have the common first block \(w_i^\epsilon/\sqrt2\), while the lower block is

\[
\frac{\alpha}{\sqrt2}U_i^\dagger w_i^\epsilon,
\qquad \alpha\in\{1,-1,i,-i\}.
\]

If two such four-component vectors were related by an arbitrary nonzero complex scalar, equality of their identical, nonzero first blocks would force that scalar to be \(1\). Equality of their nonzero lower blocks would then force their \(\alpha\) values to agree. The four displayed values are distinct.

There are therefore exactly

\[
5\cdot2\cdot4=40
\]

pairwise nonparallel unit-vector rays. This proves global complex-ray distinctness, not merely within-context orthogonality.

## 7. The complete ten-mask affine orbit

For a unit \(h\in\mathbb Z_{10}^{\times}\) and \(t\in\mathbb Z_{10}\), let

\[
F_{h,t}(r,c)=(hr,hc+t).
\]

This is a bijection of cells. It maps:

- row \(r\) to row \(hr\);
- column \(c\) to column \(hc+t\);
- symbol class \(r+c=\ell\) to symbol class \(r'+c'=h\ell+t\).

It also gives

\[
c'-r'=h(c-r)+t,
\]

so it maps \(H_S\) exactly to \(H_{hS+t}\).

Define the transported vector at \(F_{h,t}(r,c)\) to be the original vector at \((r,c)\). The context bijections preserve every ONB, and the cell bijection preserves global distinctness. No physical unitary covariance or equivariance of the vector assignment is asserted or needed.

Every \(hS+t\) is a union of two antipodal pairs because \(5h=5\pmod {10}\). The five antipodal pairs are the fibres of reduction modulo five, so there are exactly

\[
\binom52=10
\]

such masks.

Conversely, let the two chosen fibres have distinct residues \(x,y\in\mathbb Z_5\). Reduction of the four units modulo ten supplies every nonzero residue modulo five. Choose \(h\) with residue \(y-x\) and \(t\) with residue \(x\). Then \(hS+t\) has exactly the two chosen fibres. This establishes the whole ten-mask orbit without relying on prior finite enumeration.

## 8. Exact remaining sixty-ray obligation

For the displayed support, the complementary cells are exactly

\[
b-a\in\{2,3,4\}\pmod5.
\]

There are sixty such cells. Each full row, column, or cyclic symbol class has ten cells, exactly four already assigned to the constructed subsystem, and therefore exactly six in the complement.

The unresolved requirement is an actual assignment

\[
p_{r,c}\in\mathbb C^6
\]

on those sixty cells such that:

1. every vector is a unit vector;
2. all sixty rays are pairwise nonparallel, including cells not sharing a context;
3. every one of the ten restricted rows is an ONB of \(\mathbb C^6\);
4. every one of the ten restricted columns is an ONB;
5. every one of the ten restricted cyclic symbol classes is an ONB.

No such assignment is supplied or established in the frozen author body.

### Necessity

If a full hundred-ray realization has an actual orthogonal \(4+6\) sector decomposition with this four-sector cell support, restriction to the six-dimensional sector supplies precisely the sixty vectors above. Unit norm, context orthonormality, and global nonparallelness are inherited.

### Sufficiency

Suppose such sixty vectors exist. Embed the constructed forty vectors as

\[
(q_{r,c},0)\in\mathbb C^4\oplus\mathbb C^6
\]

and the complementary sixty as

\[
(0,p_{r,c}).
\]

Each full context contains a four-element ONB of the first summand and a six-element ONB of the second, hence a ten-element ONB of \(\mathbb C^{10}\).

Within each summand, rays are pairwise nonparallel by the respective hypotheses. Across summands, nonzero vectors are orthogonal and therefore cannot be parallel. The combined assignment has one hundred globally distinct rays.

Thus, for each fixed support in the stated orbit,

\[
\begin{aligned}
&\text{a full orthogonal \(4+6\) realization on that support exists}\\
&\quad\Longleftrightarrow\\
&\text{its complementary sixty-ray, thirty-ONB problem has a solution.}
\end{aligned}
\]

This equivalence concerns the specified cyclic \(4+6\) branch. It does **not** assert that every possible solution of the unrestricted original problem must have this decomposition or support.

The first unpaid step remains the actual existence or impossibility of those sixty complex vectors.

## 9. Two-dimensional exclusion and conditional complement irreducibility

Here “sector” means an **actual orthogonal ray sector** as in S2 LF7: the cell vectors lie in the mutually orthogonal summands, not arbitrary subspaces intersecting vectors with components in several summands.

### No two-dimensional ray sector

Assume such a sector has dimension two. Every full context contains exactly two sector vectors.

Choose any sector cell. Its row contains one other sector cell, and its column contains one other sector cell. Those two other cells are distinct because the row and column intersect only at the chosen cell.

Both corresponding vectors lie in the two-dimensional sector and are orthogonal to the chosen vector. They therefore lie on the same one-dimensional orthogonal-complement ray. This violates global pairwise nonparallelness.

This argument applies over \(\mathbb C\) and does not depend on cyclicity.

### Cyclic parity

For the cyclic resolution, the parity maps satisfy

\[
(r\bmod2)+(c\bmod2)+((r+c)\bmod2)=0\pmod2
\]

at every cell.

For an actual sector of dimension \(d\), its selector contains exactly \(d\) cells in every row, column, and symbol class. Sum the displayed parity identity over its selected cells. Each of the three families has five odd labels, so the resulting parity is

\[
0=5d+5d+5d=15d\pmod2.
\]

Hence \(d\) is even. This reconstructs exactly the cyclic even-sector consequence needed from S2 LF11–13; the broader Latin-rank classification is not needed for this conclusion.

### Consequence for a putative six-dimensional complement

If that complement split into two or more nonzero orthogonal ray sectors, each sector would have positive even dimension. Dimension two is impossible, so every sector would have dimension at least four. Two such sectors already require dimension at least eight, exceeding six.

Therefore any successful six-dimensional complement is irreducible **with respect to further orthogonal ray-sector decomposition**.

This is a necessary structural condition only. It neither supplies the sixty vectors nor excludes their existence.

## 10. Findings, imports, and final scope

### Findings

**None: 0 FATAL / 0 MAJOR / 0 MINOR.**

The explicit vector formulas, all ten block routings, all thirty contexts, arbitrary-complex-scalar ray distinctness, affine transport, and both directions of the complement equivalence have written reconstructions above. No mathematical repair is required at this scope.

### Exact imports and exclusions

- S2 LF7 supplies the original physical hypotheses and actual-sector meaning.
- The needed cyclic even-sector consequence of S2 LF11–13 was reconstructed explicitly.
- S2’s earlier finite-check reports, linked code, logs, other orbit exclusions, and broader rank statements were not used as substitute proofs of the new vector assignment.
- S2 LF19 and LF29 record an earlier frontier. The new construction advances the forty-vector subsystem of one orbit; it does not establish the six-dimensional complement or a complete hundred-ray realization.
- S1’s historical chronology and execution descriptions are author reports, not independently certified process facts from this review.

### What this return establishes

**SUPPORTED:** an explicit forty-ray unit-vector realization of the stated cyclic four-dimensional subsystem, with every required restricted context an ONB and all forty rays globally distinct; transport to all ten masks in its antipodal-pair orbit; and the exact conditional reduction of that \(4+6\) branch to the complementary sixty-ray problem.

**Not established:** any sixty-ray complement, hundred-ray witness, unrestricted no-go, rank-28 \(5+5\) resolution, other residual four-support orbit, or general-resolution conclusion.

This is a same-harness WRITTEN review. It provides no independent finite execution, independent-family, human, formal/kernel, or novelty assurance.

**Overall correctness:** correct within the explicitly reviewed scope.

**Explanation:** The provided forty-vector construction satisfies unit normalization, all thirty restricted ONB conditions, and global pairwise nonparallelness, and its affine transport and conditional complement equivalence are valid. The outstanding sixty-ray problem remains unproved, so no full hundred-ray result follows.

**Confidence:** 0.98.