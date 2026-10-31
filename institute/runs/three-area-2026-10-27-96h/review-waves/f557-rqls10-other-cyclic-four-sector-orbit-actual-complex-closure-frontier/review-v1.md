# f557 — A six-dimensional complement obstruction for the cyclic support \(\{0,1,3,4\}\)

**GENERAL AUTHOR PROOF CANDIDATE — UNREVIEWED.**

Complete proposed body for `author-candidate-v1.md`, returned for Main’s materialization. No project file was written, and no filesystem-write refusal is claimed.

## 1. Result and exact target relation

I obtain the following whole-complement obstruction.

> **Theorem.** On the sixty cells
> \[
> H_T=\{(r,c)\in\mathbb Z_{10}^{\,2}:c-r\in T\},
> \qquad T=\{2,5,6,7,8,9\},
> \]
> there do not exist sixty pairwise nonparallel unit vectors in \(\mathbb C^6\) such that every restricted row, column and cyclic symbol class \(r+c\) is an orthonormal basis.

Consequently, an actual orthogonal \(4+6\) realization of the original hundred-ray problem cannot have its four-dimensional sector on
\[
H_S,\qquad S=\{0,1,3,4\}.
\]

The argument transports to the entire ten-mask affine orbit of \(S\), without imposing covariance on the vectors.

The main new compatibility statement is an operator rigidity theorem for five rank-two missing-space projections. The thirty physical ONB equations force those projections to commute and to have a common pairwise intersection. There are exactly two possible rank regimes. Both contradict global ray distinctness, by different consuming-side arguments.

This is an **AUTHOR written proof candidate**, not an adopted theorem, executed verification, unrestricted hundred-ray no-go, or final completion claim.

## 2. Frozen inputs, chronology and execution boundary

The assigned wave is:

`institute/runs/three-area-2026-10-27-96h/review-waves/f557-rqls10-other-cyclic-four-sector-orbit-actual-complex-closure-frontier/`

Parent-supplied bindings:

- Manifest SHA-256: `5dec529d1a399691e4252ba885e15c53b00e3b6ef98bf16782fb17e2a3bea601`.
- Freeze-receipt SHA-256: `999fdbac239a17b4e3bd2778c12841e5f3e3c4d952e4b352278bd4bf5e394e52`.
- Literal-packet SHA-256: `a31819501def1bdc54fe7951ee5ecdb4b0df1c9b0c8a894c6a3e62cf3dc8a0ea`.

These are attributed to the parent’s live metadata supply, not to independently executed child hash checks. The supplied `2026-10-30T13:14:09-0700 PDT` clock observation likewise belongs to the parent; it is not my native start time.

Before derivation, I completed:

1. The manifest, freeze receipt, dispatch receipt and parent metadata supply.
2. All twelve permission/status controls, including their endings.
3. A direct pre-body ACK to Main.
4. The complete literal packet, LF 1–793, in consecutive raw windows of at most twenty LF, including every source ending.

The scientific coverage was exactly:

- **S1:** adopted binary-sector/cyclic-support disposition, LF 1–29.
- **S2:** unadopted f535 candidate, complete logical body LF 1–430.
- **S3:** unadopted f496 candidate, explicitly selected LF 1–332; its later checker was excluded.

Administrative inventory and required-skill reads preceded the complete control reads. After the complete packet read and initial derivation, I reread the exact physical target and frozen deliverable boundary.

S2 and S3 were exposure to author candidates, not accepted premises. In particular, I do **not** transfer f535’s antipodal-block conclusion to this different orbit. The physical context mapping and every mathematical lemma needed here are supplied below. The three-partition lemma appearing in S2 is reproved explicitly.

No held scientific payload, held consumer, sibling return, excluded checker or linked scientific source was opened.

**Scientific execution: NOTRUN.** No executable calculation, solver, checker, public-source search, external-model call or scientific shell command was performed. No code or machine output is offered as evidence. The result is a written argument.

These statements describe the recorded read/work sequence; they are not a cognitive-isolation certificate.

## 3. Exact coordinates for all sixty cells

Translate the column coordinate by two:
\[
c'=c-2\pmod {10}.
\]
This permutes columns and replaces the symbol label \(r+c\) by \(r+c'=r+c-2\), also a permutation of the ten symbol classes.

The complementary support becomes
\[
c'-r\in T'=\{0,3,4,5,6,7\}.
\]

Use CRT coordinates
\[
r\longleftrightarrow(a,u),\qquad
c'\longleftrightarrow(b,v),
\]
where \(a,b\in\mathbb Z_5\) and \(u,v\in\mathbb Z_2\). The inverse is
\[
\operatorname{crt}(a,u)=a+5((u-a)\bmod2).
\]

Thus the original cell corresponding to \(((a,u),(b,v))\) is
\[
r=\operatorname{crt}(a,u),\qquad
c=\operatorname{crt}(b,v)+2\pmod {10}.
\]

Membership in the sixty-cell support has the following complete description:

- If \(b=a\), all four choices of \((u,v)\) occur.
- If \(b-a=\pm1\pmod5\), precisely \(v=u\) occurs.
- If \(b-a=\pm2\pmod5\), precisely \(v=u+1\) occurs.

Indeed, for a fixed residue modulo five and parity, the shifted difference is uniquely determined modulo ten:

- Residue zero gives shifted differences \(0,5\).
- Residues \(\pm1\) with even parity give \(4,6\).
- Residues \(\pm2\) with odd parity give \(3,7\).

These are exactly \(T'\).

Define
\[
\tau(a,b)=
\begin{cases}
0,&b-a=\pm1,\\
1,&b-a=\pm2.
\end{cases}
\]

For the five diagonal CRT blocks, write the four hypothetical vectors as
\[
q_a^{uv}\qquad(u,v\in\mathbb Z_2).
\]

For each ordered pair \(a\ne b\), write the two hypothetical vectors as
\[
q_{ab}^{u},
\]
at CRT coordinates
\[
((a,u),(b,u+\tau(a,b))).
\]

This accounts for
\[
5\cdot4+5\cdot4\cdot2=60
\]
actual cells.

### All thirty physical contexts

The ten rows are, for every \(a,u\),
\[
\{q_a^{u0},q_a^{u1}\}
\ \cup\
\{q_{ab}^{u}:b\ne a\}.
\tag{R}_{a,u}
\]

The ten columns are, for every \(b,v\),
\[
\{q_b^{0v},q_b^{1v}\}
\ \cup\
\{q_{ab}^{\,v-\tau(a,b)}:a\ne b\}.
\tag{C}_{b,v}
\]

A shifted symbol has CRT coordinates
\[
(s,w)=(a+b,u+v).
\]
Put \(k=3s\pmod5\), so \(2k=s\).

For \(w=0\), its six vectors are
\[
\{q_k^{00},q_k^{11}\}
\ \cup\
\{q_{k-2,k+2}^{u},q_{k+2,k-2}^{u}:u\in\mathbb Z_2\}.
\tag{L}_{k,0}
\]

For \(w=1\), they are
\[
\{q_k^{01},q_k^{10}\}
\ \cup\
\{q_{k-1,k+1}^{u},q_{k+1,k-1}^{u}:u\in\mathbb Z_2\}.
\tag{L}_{k,1}
\]

Every displayed context has six vectors. These formulas quantify over all ten rows, ten columns and ten symbol classes.

From now on, assume for contradiction that all these contexts are ONBs of \(\mathbb C^6\) and that all sixty cell rays are pairwise nonparallel.

## 4. Actual block projections

For a vector \(x\), write \(p_x=xx^\dagger\).

### Four-cell blocks

The four vectors \(q_a^{uv}\) are mutually orthogonal:

- Equal \(u\): common row.
- Equal \(v\): common column.
- Both bits different: common symbol, because \(u+v\) is unchanged modulo two.

Therefore
\[
F_a=\sum_{u,v}p_{q_a^{uv}}
\]
is a rank-four orthogonal projection.

Define
\[
U_a=p_{q_a^{00}}+p_{q_a^{11}},
\qquad
V_a=p_{q_a^{01}}+p_{q_a^{10}},
\]
and
\[
E_a=I-F_a.
\]

Then \(U_a,V_a,E_a\) are mutually orthogonal rank-two projections satisfying
\[
U_a+V_a+E_a=I.
\tag{1}
\]

### Two-cell blocks

For \(a\ne b\), the two vectors \(q_{ab}^{0},q_{ab}^{1}\) have the same symbol. Thus
\[
P_{ab}=p_{q_{ab}^{0}}+p_{q_{ab}^{1}}
\]
is a rank-two orthogonal projection.

All these operators arise from actual hypothetical vectors. They are not integer incidence selectors.

## 5. The thirty ONB equations force a five-cycle balance

Adding the two row equations with first coordinate \(a\) gives
\[
F_a+\sum_{b\ne a}P_{ab}=2I,
\]
hence
\[
\sum_{b\ne a}P_{ab}=I+E_a.
\tag{2}
\]

Adding the two column equations with first coordinate \(a\) gives
\[
\sum_{b\ne a}P_{ba}=I+E_a.
\tag{3}
\]

The symbol equations give
\[
P_{k-2,k+2}+P_{k+2,k-2}=I-U_k,
\tag{4}
\]
and
\[
P_{k-1,k+1}+P_{k+1,k-1}=I-V_k.
\tag{5}
\]

For a fixed \(a\), add (2) and (3). Group each ordered block with its reversal. Edges from \(a\) to \(a\pm1\) have midpoint \(a\mp2\) and use (4); edges to \(a\pm2\) have midpoint \(a\pm1\) and use (5). Consequently,
\[
2I+2E_a
=
4I-U_{a-2}-U_{a+2}-V_{a-1}-V_{a+1}.
\]

Using (1), this becomes
\[
\boxed{
U_{a-2}+U_{a+2}+V_{a-1}+V_{a+1}
=
2(U_a+V_a)=2F_a.
}
\tag{6}
\]

If \(x\in\operatorname{ran}E_a\), the quadratic form of the right side vanishes. Every summand on the left is positive. Therefore
\[
E_aU_{a\pm2}=0,
\qquad
E_aV_{a\pm1}=0.
\tag{7}
\]

Taking adjoints gives the reverse products as well. In particular,
\[
E_{a\pm1}\le E_a+U_a,
\qquad
E_{a\pm2}\le E_a+V_a.
\tag{8}
\]

The next lemma extracts the rigidity of these actual missing spaces.

## 6. Five-cycle missing-space rigidity

> **Lemma.** Let \((E_a,U_a,V_a)\), \(a\in\mathbb Z_5\), be orthogonal projection partitions satisfying (7). Then there is an orthogonal projection \(G\) such that
> \[
> E_aE_b=G
> \qquad\text{for all }a\ne b.
> \tag{9}
> \]
> In particular, all \(E_a\) commute.

### A projection contraction observation

Suppose orthogonal projections \(P,Q,R\) satisfy
\[
PQ=PRQ,\qquad RQ=RPQ.
\tag{10}
\]

For \(x\in\operatorname{ran}Q\), put \(y=Px\), \(z=Rx\). Then
\[
y=Pz,\qquad z=Ry.
\]
Projection contraction gives
\[
\|y\|\le\|z\|\le\|y\|.
\]
Equality in \(\|Pz\|\le\|z\|\) implies \(Pz=z\). Hence \(y=z\), proving
\[
(P-R)Q=0.
\tag{11}
\]

### Consecutive products

Take
\[
P=E_{a-1},\qquad Q=E_a,\qquad R=E_{a+1}.
\]

Relative to the partition at \(R\), (8) places \(P\) in \(R+V_{a+1}\) and \(Q\) in \(R+U_{a+1}\). Their components outside \(R\) are orthogonal. Thus
\[
PQ=PRQ.
\]
The partition at \(P\) similarly gives \(RQ=RPQ\).

By (11),
\[
(E_{a-1}-E_{a+1})E_a=0.
\tag{12}
\]

Let
\[
T_a=E_aE_{a+1}.
\]
Equation (12), with middle index \(a+1\), gives
\[
T_a=T_{a+1}^{\dagger}.
\tag{13}
\]

Following this relation around the odd five-cycle shows that every \(T_a\) is the same self-adjoint operator \(T\). A self-adjoint product of two orthogonal projections is their commuting intersection projection. Therefore \(T\) is a projection and
\[
T\le E_a\qquad\text{for every }a.
\tag{14}
\]

### Distance-two products

Repeat the same argument in cyclic order
\[
0,2,4,1,3.
\]
The roles of \(U\) and \(V\) in (8) are interchanged. It follows that all products \(E_aE_{a+2}\) are one common self-adjoint projection \(W\), also satisfying \(W\le E_a\) for every \(a\).

Because \(T\) lies in every \(E_a\),
\[
T\le E_0E_2=W.
\]
Because \(W\) lies in every \(E_a\),
\[
W\le E_0E_1=T.
\]
Hence \(T=W\). Call their common value \(G\). Every distinct pair of indices has distance one or two, proving (9). ∎

### The only possible ranks

Here every \(E_a\) has rank two. Write
\[
g=\operatorname{rank}G.
\]

The projections \(E_a-G\) are pairwise orthogonal, each of rank \(2-g\), and are orthogonal to \(G\). Thus
\[
g+5(2-g)\le6,
\]
or
\[
10-4g\le6.
\]
Since \(0\le g\le2\),
\[
\boxed{g=1\quad\text{or}\quad g=2.}
\tag{15}
\]

We exclude both regimes below.

## 7. The rank-one common-intersection regime is impossible

Assume \(\operatorname{rank}G=1\).

Set
\[
L_a=\operatorname{ran}(E_a-G).
\]
These are five mutually orthogonal one-dimensional spaces, orthogonal to \(\operatorname{ran}G\). The rank count is exact:
\[
\mathbb C^6
=
\operatorname{ran}G
\oplus L_0\oplus L_1\oplus L_2\oplus L_3\oplus L_4,
\tag{16}
\]
and
\[
\operatorname{ran}E_a=\operatorname{ran}G\oplus L_a.
\tag{17}
\]

By (7), \(U_a\) annihilates \(E_a,E_{a-2},E_{a+2}\). Its rank is two, so
\[
\operatorname{ran}U_a=L_{a-1}\oplus L_{a+1}.
\tag{18}
\]
Likewise,
\[
\operatorname{ran}V_a=L_{a-2}\oplus L_{a+2}.
\tag{19}
\]

### At least three diagonal blocks have no coordinate basis

For each \(a\), the pair
\[
\{q_a^{00},q_a^{11}\}
\]
is an ONB of the two-plane (18), while
\[
\{q_a^{01},q_a^{10}\}
\]
is an ONB of (19).

Call such a two-vector basis **coordinate** if its rays are precisely the two displayed \(L\)-lines. Otherwise, both vectors have nonzero components on both lines: a two-dimensional orthonormal basis with any zero coordinate is necessarily the coordinate basis.

Every coordinate basis uses two of the five fixed rays \(L_0,\ldots,L_4\). Global pairwise nonparallelness prevents any of those rays from being used twice, even in different diagonal blocks. Hence there can be at most two coordinate bases among all ten pairs.

Call \(a\) **good** when neither of its two bases is coordinate. At most two indices are not good; therefore at least three indices are good.

### An off-diagonal block between good indices collapses to \(G\)

Choose distinct good indices \(a,b\), and put
\[
k=3(a+b)\pmod5.
\]
Thus \(k\) is their midpoint modulo five and differs from both endpoints.

Equations (4)–(5), together with (18)–(19), show that
\[
P_{ab}+P_{ba}
\]
is the projection onto
\[
\operatorname{ran}G\oplus L_a\oplus L_b\oplus L_k.
\tag{20}
\]

Indeed:

- For \(b-a=\pm1\), the endpoints are \(k\pm2\); the omitted symbol plane is \(U_k=L_{k-1}\oplus L_{k+1}\).
- For \(b-a=\pm2\), the endpoints are \(k\pm1\); the omitted plane is \(V_k=L_{k-2}\oplus L_{k+2}\).

Thus every \(q_{ab}^{u}\) belongs to the four-space (20).

Relative to \(a\), the two indices \(b,k\) occupy different classes in (18)–(19):

- If \(b-a=\pm1\), then \(k-a=\mp2\).
- If \(b-a=\pm2\), then \(k-a=\pm1\).

The row through \(q_{ab}^{u}\) contains \(q_a^{u0}\) and \(q_a^{u1}\), one in \(U_a\) and one in \(V_a\). Because \(a\) is good, each has nonzero coefficients on both lines of its respective two-plane.

Within (20), the component of \(q_{ab}^{u}\) in each of \(U_a,V_a\) can occupy only one of those two lines: respectively \(L_b\) or \(L_k\). Orthogonality to the two diagonal-block row vectors therefore forces both components to vanish. Consequently,
\[
q_{ab}^{u}\in\operatorname{ran}G\oplus L_a
=\operatorname{ran}E_a.
\tag{21}
\]

Apply the same reasoning to its column. Since \(b\) is good,
\[
q_{ab}^{u}\in\operatorname{ran}G\oplus L_b
=\operatorname{ran}E_b.
\tag{22}
\]

Combining (21)–(22),
\[
q_{ab}^{u}\in\operatorname{ran}G.
\]

This holds for both \(u=0,1\). But \(q_{ab}^{0},q_{ab}^{1}\) are orthogonal unit vectors, whereas \(\operatorname{ran}G\) is one-dimensional. Contradiction.

Therefore the regime \(g=1\) cannot support the required sixty distinct rays.

## 8. The rank-two common-intersection regime is impossible

Assume \(\operatorname{rank}G=2\).

Because \(G\le E_a\) and both have rank two,
\[
E_a=G\qquad\text{for every }a.
\tag{23}
\]

Put \(F=I-G\). Then
\[
U_a+V_a=F.
\tag{24}
\]

Substitute \(V_a=F-U_a\) into (6):
\[
U_{a-2}+U_{a+2}-U_{a-1}-U_{a+1}=0.
\tag{25}
\]

### The symbol two-planes are constant

For a Fourier mode \(a\mapsto z^a\), \(z^5=1\), the multiplier in (25) is
\[
z^2+z^{-2}-z-z^{-1}.
\]
Writing \(x=z+z^{-1}\), it equals
\[
x^2-x-2=(x-2)(x+1).
\]

For a nontrivial fifth root \(z\):

- \(x=2\) would imply \(z=1\).
- \(x=-1\) would imply \(z^2+z+1=0\), impossible for a nontrivial fifth root.

Every nonconstant operator-valued Fourier coefficient therefore vanishes. Hence
\[
U_a=U,\qquad V_a=V
\tag{26}
\]
for fixed rank-two projections, with
\[
G+U+V=I
\tag{27}
\]
an orthogonal partition.

This finite Fourier argument solves a linear identity for arbitrary operators. It does not assume covariance of the physical vectors.

Every diagonal-block ray already lies in either \(\operatorname{ran}U\) or \(\operatorname{ran}V\).

For off-diagonal blocks, the symbol equations imply
\[
P_{ab}\le
\begin{cases}
G+V,&b-a=\pm1,\\
G+U,&b-a=\pm2.
\end{cases}
\tag{28}
\]

It remains essential to route the **individual off-diagonal rays**, not just their block spans, into this partition.

### Three-partition commutation lemma

Suppose
\[
A_1+A_2+A_3=I,\qquad Q_1+Q_2+Q_3=I
\]
are orthogonal projection partitions and \(Q_iA_i=0\) for each \(i\). Then every \(Q_i\) commutes with every \(A_j\).

To prove this, consider \(A_jQ_iA_k\), \(j\ne k\).

- If \(i=j\), it vanishes because \(A_iQ_i=0\).
- If \(i=k\), it vanishes because \(Q_iA_i=0\).
- Otherwise the three indices are different, and
  \[
  A_jQ_iA_k
  =A_j(I-Q_j-Q_k)A_k=0.
  \]

Thus every \(Q_i\) is block diagonal in the \(A\)-partition. ∎

### Row and column group planes reduce \(G,U,V\)

Fix a row \((a,u)\). Group its six rays into three orthogonal two-planes:

1. \(R\): its two diagonal-block rays.
2. \(X\): its two rays with \(b-a=\pm1\).
3. \(Y\): its two rays with \(b-a=\pm2\).

Their projections form an orthogonal partition:
\[
R+X+Y=I.
\]

The diagonal block lies in \(U+V\), so \(RG=0\). Equation (28) gives \(XU=0\) and \(YV=0\). Apply the three-partition lemma with
\[
(A_1,A_2,A_3)=(G,U,V),\qquad
(Q_1,Q_2,Q_3)=(R,X,Y).
\]
Every row group plane reduces \(G,U,V\).

The identical grouping of each column gives the same conclusion for every column group plane.

### Every individual off-diagonal ray lies in one common two-sector

Take an off-diagonal cell ray \(q\). Its row group plane and its column group plane are both two-dimensional, reduce \(G,U,V\), and contain \(q\).

If the two planes were equal, their two ONBs would share \(q\). Their respective other rays would then lie in the same one-dimensional orthogonal complement of \(\mathbb Cq\). Those rays occur at distinct cells: the row and column intersect only at the cell of \(q\). This would violate global pairwise nonparallelness.

Therefore the planes are distinct. Their intersection is exactly \(\mathbb Cq\).

Because each of \(G,U,V\) preserves both planes, it preserves their intersection. Each consequently acts on \(\mathbb Cq\) as zero or identity. Since their sum is identity, exactly one acts as identity. Thus \(q\) lies entirely in one of
\[
\operatorname{ran}G,\quad
\operatorname{ran}U,\quad
\operatorname{ran}V.
\tag{29}
\]

This argument does **not** assume the row and column group projections commute with each other.

Together with the diagonal-block rays, every one of the sixty rays is now routed into one of three fixed mutually orthogonal two-dimensional spaces.

### A common two-dimensional sector forces a repeated ray

Every row ONB contains exactly two rays from each space in (29); the same holds for every column ONB.

Choose any cell ray \(q\) and its two-dimensional sector \(K\).

- Its row has one other \(K\)-ray, \(x\).
- Its column has one other \(K\)-ray, \(y\).

Both are orthogonal to \(q\). But
\[
K\cap(\mathbb Cq)^\perp
\]
is one-dimensional, so \(x,y\) are parallel.

Their cells are distinct because the chosen row and column intersect only at the original cell of \(q\). This again contradicts global pairwise nonparallelness.

Therefore the regime \(g=2\) is impossible.

Both possibilities in (15) have now been excluded, proving the theorem.

## 9. Consequence for the actual hundred-ray problem

Suppose a full hundred-ray array had an actual four-dimensional sector on
\[
H_S,\qquad S=\{0,1,3,4\}.
\]

Each full context contains four sector rays. Those four orthonormal vectors span the four-dimensional sector. Its other six context rays must therefore lie in the common six-dimensional orthogonal complement.

Across all cells, these are exactly the sixty complementary cells \(H_T\). The full row, column and symbol ONBs make each restricted complementary context an ONB of that six-dimensional space. Global nonparallelness of all hundred rays includes nonparallelness of these sixty.

This is precisely the problem excluded above. Hence:

> **No actual orthogonal \(4+6\) realization of the original hundred-ray problem can use the support \(S=\{0,1,3,4\}\) for its four-dimensional sector.**

No assertion about standalone realizability of its forty-ray subsystem is needed.

## 10. Transport to the entire ten-mask orbit

For a unit \(h\in\{1,3,7,9\}\) and \(t\in\mathbb Z_{10}\), the relabeling
\[
(r,c)\longmapsto(hr,hc+t)
\tag{30}
\]
permutes rows and columns, sends symbols by
\[
r+c\longmapsto h(r+c)+t,
\]
and sends differences by
\[
c-r\longmapsto h(c-r)+t.
\]

Thus a hypothetical complementary realization for \(hS+t\) pulls back to one for \(S\), preserving every ONB requirement and every nonparallelness condition. Equation (30) is a cell relabeling; no unitary covariance of the vectors is assumed.

For this representative,
\[
3S=S+9,\qquad 7S=S+7,\qquad 9S=S+6.
\]
Its affine orbit is therefore exactly its set of translations
\[
\{S+t:t\in\mathbb Z_{10}\}.
\]

These ten translations are distinct. A nonzero translational stabilizer would have order two, five or ten. Orders five and ten cannot preserve a four-element subset; order two would require \(S\) to be a union of antipodal pairs, which it is not.

Accordingly, the theorem excludes the entire assigned ten-mask orbit as actual orthogonal \(4+6\) sectors.

## 11. What has and has not been established

### Supplied by this AUTHOR candidate

- A whole sixty-cell complement obstruction for the exact representative.
- Explicit routing of all ten rows, ten columns and ten symbol contexts.
- A uniform complex-operator rigidity lemma forcing commuting missing-space projections.
- An exhaustive rank split into common-intersection dimensions one and two.
- A contradiction in the rank-one regime using actual individual-vector coefficients and the global distinctness requirement.
- A contradiction in the rank-two regime with an explicit individual-ray consuming-side argument.
- Transport to the whole ten-mask orbit without vector covariance.

### Not supplied or claimed

- No sixty-vector or hundred-vector construction.
- No executed scientific calculation or finite checker.
- No independent or disjoint review of this candidate.
- No parent adoption.
- No adoption or verification of the separate f535 theorem for the other ten-mask orbit.
- No retrospective union acceptance covering all one hundred balanced masks.
- No result for noncirculant supports, other Latin resolutions, rank-28 \(5+5\) branches, or irreducible ten-dimensional arrays.
- No unrestricted resolution of the original hundred-ray target.
- No source-equivalence, novelty, independent-family, human, formal/kernel or final-completion assurance.

The first unpaid acceptance consumer is a disjoint reconstruction of
\[
\text{all thirty actual ONB equations}
\Longrightarrow
\text{balance (6)}
\Longrightarrow
E_aE_b=G
\Longrightarrow
\text{the exhaustive }g=1,2\text{ contradictions}.
\]

Within that reconstruction, the especially load-bearing individual-ray consumers are:

1. The rank-one regime’s implication from noncoordinate diagonal-block bases to
   \[
   q_{ab}^{u}\in E_a\cap E_b=\operatorname{ran}G.
   \]
2. The rank-two regime’s intersection argument routing each off-diagonal rank-one ray into a common two-dimensional sector.

Those implications are supplied explicitly above, rather than left as block-span sufficiency assumptions. Their independent checking and parent disposition remain pending.

**Evidence classification:** exact written AUTHOR proof candidate; scientific execution **NOTRUN**; acceptance **PENDING**; unrestricted original target **UNRESOLVED**.