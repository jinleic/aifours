# f570 — WRITTEN review of the other cyclic four-sector orbit

**Reviewer:** ReviewF570OtherRigidity  
**Role:** WRITTEN  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR**  
**Scientific execution:** **NOTRUN**

This is the complete review body for Main’s materialization. No project file was written, and no filesystem-write refusal is claimed. The review supports the candidate’s stated ten-mask-orbit obstruction at its exact physical scope; it does not itself adopt the candidate or establish an unrestricted hundred-ray no-go.

## 1. Binding, coverage and process record

The assigned wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f570-rqls10-other-orbit-five-cycle-missing-projection-rigidity-review/`

Bindings:

- Manifest SHA-256: `bc0c365532539eb813ea4e9dd3f7cf53f53809dee8fedc39e196c0f5e32a7210`.
- Freeze-receipt SHA-256: `c7f3e7f42c2f315fd1cab77aa22ee3cfb5f8fe292203a4fdb5803e9d7b6391a7`.
- Literal-packet SHA-256, according to the supplied receipt and metadata: `24dcf2a73d5d63675ca8883ecacb97b20dddd00ddbeacd13f1a35c00baad25d0`.

These are user-provided and parent-supplied bindings, not independently executed child hash measurements. The parent’s supplied clock observation is not represented as a child-native review timestamp.

Before opening the mathematical packet, I read:

1. The complete manifest.
2. The complete freeze receipt.
3. The complete parent metadata supply and dispatch receipt.
4. All twelve listed status-only controls, including their endings.

I then sent a direct administrative pre-body ACK to Main; delivery was confirmed by the tool. Only afterward did I read the complete literal packet, consecutively in raw windows of at most twenty lines, through its ending at packet line 778. Both scientific source endings were included. No mathematical derivation preceded completion of that packet read.

The scientific inputs were:

- **S1:** f557 candidate, complete logical lines 1–747, SHA-256  
  `48ef117bd36a93937d078086a82428c166da38df04998f0a18b7777568a8d953`.
- **S2:** original binary-sector/cyclic-support disposition, complete lines 1–29, SHA-256  
  `a4c7197d031810d9986249612b98749efc2edf705986808b718c609b9704152b`.

S1’s 747 logical lines and the supplied 746 LF count are distinguished; I read the final logical line rather than treating the LF count as the complete logical-line count.

All references below use **source logical line numbers**, not packet line numbers.

The held episodes and their consumers were status-only exclusions. I did not follow their links or use their mathematical payloads. I did not read sibling reviews, author code, excluded checkers or new scientific sources. No private selected vector, operator, graph or parameter probe was introduced. No scientific interpreter, CAS, enumeration, solver, build, test, lint, formatter, external-model CLI or finite replay was run.

## 2. Per-claim dispositions

| Claim | S1 lines | Disposition |
|---|---:|---|
| Exact sixty-cell support and all thirty physical context formulas | 66–180 | **SUPPORTED** |
| Actual rank-two projection partitions and off-diagonal block projections | 182–225 | **SUPPORTED** |
| ONB equations imply balance, annihilation and range inclusions | 227–287 | **SUPPORTED** |
| Projection contraction and both odd-cycle arguments imply \(E_aE_b=G\) | 291–374 | **SUPPORTED** |
| The only possible common-intersection ranks are one and two | 376–395 | **SUPPORTED** |
| Rank-one regime contradicts the actual off-diagonal rays | 399–503 | **SUPPORTED** |
| Rank-two regime forces individual rays into common two-sectors and then repetition | 505–650 | **SUPPORTED** |
| Complement obstruction excludes an actual \(4+6\) completion on the representative support | 654–669 | **SUPPORTED** |
| Context-preserving transport excludes the complete ten-mask affine orbit | 671–700 | **SUPPORTED** |

No scoped mathematical claim above is left unreviewed. The reconstruction follows.

## 3. Physical coordinates and consuming contexts

### 3.1 Support membership

The column translation \(c'=c-2\) sends the stated complement
\[
T=\{2,5,6,7,8,9\}
\]
to
\[
T'=\{0,3,4,5,6,7\}.
\]
It permutes columns and translates every cyclic symbol label by the same amount.

Under CRT coordinates
\[
r\leftrightarrow(a,u),\qquad c'\leftrightarrow(b,v),
\]
the difference has coordinates \((b-a,v-u)\). Consequently:

- Difference residue zero admits both parities, giving all four cells when \(a=b\).
- Difference residue \(\pm1\) admits exactly even parity, so \(v=u\).
- Difference residue \(\pm2\) admits exactly odd parity, so \(v=u+1\).

These are precisely the shifted differences in \(T'\). Thus the five four-cell diagonal blocks and twenty two-cell ordered off-diagonal blocks account for the actual sixty cells, not an abstract incidence substitute. This supports S1 lines 66–136.

### 3.2 All thirty contexts

The row and column formulas in S1 lines 140–153 follow directly from fixing \((a,u)\) or \((b,v)\).

For symbols, the actual shifted cyclic symbol has CRT coordinates
\[
(a+b,u+v).
\]
Writing \(a+b=2k\):

- Symbol parity zero selects off-diagonal differences \(\pm1\). Their endpoints are \(k-2,k+2\), in both orders. Its diagonal vectors are \(q_k^{00},q_k^{11}\).
- Symbol parity one selects differences \(\pm2\). Their endpoints are \(k-1,k+1\), in both orders. Its diagonal vectors are \(q_k^{01},q_k^{10}\).

Therefore the two displayed symbol formulas in S1 lines 162–175 are correct. Each includes two diagonal vectors and four off-diagonal vectors. Together with the row and column formulas, they cover all ten rows, ten columns and ten cyclic symbols.

This verifies the physical routing needed by the subsequent operator equations.

## 4. Actual projections, balance and positivity

The four vectors in a diagonal block are mutually orthogonal: a pair shares a row, shares a column, or differs in both bits and therefore shares a symbol. Hence the operators \(U_a,V_a,E_a\) are actual mutually orthogonal rank-two projections with
\[
U_a+V_a+E_a=I.
\]

Likewise, \(q_{ab}^{0}\) and \(q_{ab}^{1}\) share a physical symbol, so their sum of rank-one projections is an actual rank-two orthogonal projection \(P_{ab}\). These conclusions support S1 lines 182–225.

Adding the two physical row equations and the two physical column equations gives
\[
\sum_{b\ne a}P_{ab}=I+E_a,\qquad
\sum_{b\ne a}P_{ba}=I+E_a.
\]
The physical symbol equations give
\[
P_{k-2,k+2}+P_{k+2,k-2}=I-U_k,
\]
\[
P_{k-1,k+1}+P_{k+1,k-1}=I-V_k.
\]

For an edge from \(a\) to \(a\pm1\), the midpoint is \(a\mp2\), and the reversed pair uses the \(U\)-equation. For an edge to \(a\pm2\), the midpoint is \(a\pm1\), and the reversed pair uses the \(V\)-equation. Summing the four reversed pairs therefore yields
\[
U_{a-2}+U_{a+2}+V_{a-1}+V_{a+1}
=2(U_a+V_a).
\]

The positivity argument is valid without assuming any inter-index commutativity. For \(x\in\operatorname{ran}E_a\), the right-hand quadratic form is zero, while each left-hand term is the squared norm of a projection of \(x\). Thus each term annihilates \(x\). Taking adjoints gives
\[
E_aU_{a\pm2}=0,\qquad E_aV_{a\pm1}=0.
\]
Applying these identities at the neighboring indices gives
\[
E_{a\pm1}\le E_a+U_a,\qquad
E_{a\pm2}\le E_a+V_a.
\]

This reconstructs S1 lines 227–287 without a commutative substitution.

## 5. Missing-space rigidity

### 5.1 Projection contraction observation

For the author’s projections \(P,Q,R\), suppose
\[
PQ=PRQ,\qquad RQ=RPQ.
\]
For \(x\in\operatorname{ran}Q\), let \(y=Px\) and \(z=Rx\). Then
\[
y=Pz,\qquad z=Ry,
\]
so
\[
\|y\|\le\|z\|\le\|y\|.
\]
Equality for the orthogonal projection \(P\) implies \(z\in\operatorname{ran}P\), hence \(y=z\). Therefore
\[
(P-R)Q=0.
\]
The observation in S1 lines 301–320 is correct, including the zero-norm case.

### 5.2 Adjacent cycle: both required identities hold

Take the author’s
\[
P=E_{a-1},\qquad Q=E_a,\qquad R=E_{a+1}.
\]

At index \(a+1\), the range inclusions give
\[
P\le R+V_{a+1},\qquad Q\le R+U_{a+1}.
\]
Consequently \((I-R)Q=U_{a+1}Q\), while \(PU_{a+1}=0\). Hence
\[
P(I-R)Q=0,
\]
which is precisely \(PQ=PRQ\).

At index \(a-1\), the corresponding inclusions are
\[
R\le P+V_{a-1},\qquad Q\le P+U_{a-1}.
\]
They give \(R(I-P)Q=0\), hence \(RQ=RPQ\).

The contraction observation therefore gives
\[
(E_{a-1}-E_{a+1})E_a=0.
\]

For \(T_a=E_aE_{a+1}\), this implies
\[
T_a=T_{a+1}^{\dagger}.
\]
Going around the five-cycle applies the adjoint an odd number of times and returns to the same index. Thus each \(T_a\) is self-adjoint, and all are equal. A self-adjoint product of two orthogonal projections is their commuting intersection projection. Their common value \(T\) is therefore a projection below every \(E_a\).

This supports S1 lines 323–355.

### 5.3 Distance-two cycle: the interchanged partitions are correct

For the distance-two version, use
\[
P=E_{a-2},\qquad Q=E_a,\qquad R=E_{a+2}.
\]

At \(R\), the index of \(P\) differs by \(-4=1\) modulo five, whereas the index of \(Q\) differs by \(-2\). Therefore
\[
P\le R+U_{a+2},\qquad Q\le R+V_{a+2}.
\]
At \(P\), the index of \(R\) differs by \(4=-1\), whereas that of \(Q\) differs by \(2\). Therefore
\[
R\le P+U_{a-2},\qquad Q\le P+V_{a-2}.
\]
These are exactly the two orthogonal-complement placements needed for the same contraction argument.

The resulting product relation runs around the author’s odd cycle \(0,2,4,1,3\). Thus all \(E_aE_{a+2}\) equal a common self-adjoint intersection projection \(W\), below every \(E_a\).

Since \(T\) lies in every \(E_a\), it lies in the intersection represented by \(W\). Conversely, \(W\) lies in the adjacent intersection represented by \(T\). Hence \(T=W=G\). Every distinct index pair has distance one or two, proving
\[
E_aE_b=G\qquad(a\ne b).
\]

The argument in S1 lines 359–374 is supported. Neither cycle assumes the commutativity it is establishing.

### 5.4 Exhaustive rank split

Because \(G\le E_a\), each \(E_a-G\) is a projection. For distinct indices,
\[
(E_a-G)(E_b-G)=0.
\]
They are also orthogonal to \(G\).

With \(g=\operatorname{rank}G\), the occupied dimension is therefore
\[
g+5(2-g)=10-4g\le6.
\]
Together with \(0\le g\le2\), this leaves exactly \(g=1\) or \(g=2\). S1 lines 376–395 are supported.

## 6. Rank-one regime: individual physical rays give the contradiction

When \(g=1\), the author’s five lines
\[
L_a=\operatorname{ran}(E_a-G)
\]
and \(\operatorname{ran}G\) form an orthogonal decomposition of all \(\mathbb C^6\).

The annihilation identities and the rank-two dimensions force
\[
\operatorname{ran}U_a=L_{a-1}\oplus L_{a+1},\qquad
\operatorname{ran}V_a=L_{a-2}\oplus L_{a+2}.
\]

For an ONB of either displayed two-plane, a zero coordinate forces the entire basis to be the two coordinate rays. Otherwise both basis vectors have nonzero components on both coordinate lines. This statement is valid over \(\mathbb C\).

Each coordinate basis uses two of the five rays \(L_a\). Global pairwise nonparallelness prevents reuse of any such ray, so at most two of the ten diagonal-block bases can be coordinate. Thus at least three block indices are good in the author’s sense. The existence of two distinct good indices follows without further assumptions.

Take the author’s arbitrary distinct good indices \(a,b\), with midpoint \(k=3(a+b)\). The physical symbol equation gives
\[
\operatorname{ran}(P_{ab}+P_{ba})
=\operatorname{ran}G\oplus L_a\oplus L_b\oplus L_k.
\]
The two cases in S1 lines 470–471 have the correct omitted planes.

Relative to endpoint \(a\), the indices \(b\) and \(k\) lie in different distance classes. Hence within this four-space, a vector \(q_{ab}^{u}\) has only one potentially occupied line in each of \(U_a,V_a\). Its two physical diagonal-block row partners are one vector from each plane, and goodness makes their coefficients on those permitted lines nonzero. Orthogonality to those partners therefore eliminates both components, giving
\[
q_{ab}^{u}\in\operatorname{ran}E_a.
\]

The actual column partners are \(q_b^{0v},q_b^{1v}\), with \(v=u+\tau(a,b)\). They likewise give one vector in each of \(U_b,V_b\); goodness at \(b\) eliminates the corresponding components and yields
\[
q_{ab}^{u}\in\operatorname{ran}E_b.
\]
Thus
\[
q_{ab}^{u}\in\operatorname{ran}G.
\]

This holds for both values of \(u\), but the two vectors belong to one physical symbol ONB and are orthogonal unit vectors. They cannot both lie in a one-dimensional space.

The contradiction in S1 lines 399–503 is supported. It uses actual individual-ray orthogonality, not merely a block-span condition.

## 7. Rank-two regime: sector reduction reaches individual rays

### 7.1 Constant symbol planes

When \(g=2\), all \(E_a=G\). With \(F=I-G\), one has \(V_a=F-U_a\), and balance becomes
\[
U_{a-2}+U_{a+2}-U_{a-1}-U_{a+1}=0.
\]

The finite Fourier argument is an exact linear argument on operator-valued sequences. Its multiplier is
\[
z^2+z^{-2}-z-z^{-1}
=(x-2)(x+1),\qquad x=z+z^{-1}.
\]
For a nontrivial fifth root \(z\), neither factor vanishes: \(x=2\) forces \(z=1\), while \(x=-1\) forces a third-root relation incompatible with a nontrivial fifth root. Therefore every nonconstant coefficient vanishes.

It follows that \(U_a=U\) and \(V_a=V\), with
\[
G+U+V=I
\]
an orthogonal partition into rank-two projections. This does not impose covariance on the vectors.

The symbol equations then give the stated physical bounds
\[
P_{ab}\le G+V\quad(b-a=\pm1),\qquad
P_{ab}\le G+U\quad(b-a=\pm2).
\]

### 7.2 Three-partition lemma and its actual applications

The proof in S1 lines 571–589 is correct. For distinct \(j,k\), the off-diagonal block \(A_jQ_iA_k\) vanishes directly if \(i=j\) or \(i=k\). Otherwise the three indices exhaust the partition, and
\[
A_jQ_iA_k=A_j(I-Q_j-Q_k)A_k=0.
\]
Thus each \(Q_i\) is block diagonal in the \(A\)-partition and commutes with every \(A_j\).

For each physical row, the groups \(R,X,Y\) are mutually orthogonal two-planes spanning the row ONB. Their exclusions are exactly
\[
RG=0,\qquad XU=0,\qquad YV=0.
\]
The lemma therefore applies to the actual row groups. The corresponding column grouping has the same exclusions and gives the same conclusion.

Hence all the row and column group planes used by the author reduce \(G,U,V\).

### 7.3 The individual-ray consumer is valid

For any off-diagonal cell ray \(q\), its row group plane and column group plane are two-dimensional and contain \(q\).

If these planes were equal, their respective other basis rays would lie in the same one-dimensional complement of \(\mathbb Cq\) inside that plane. Those rays occupy distinct cells because the physical row and column intersect only at the cell of \(q\). They would therefore violate global pairwise nonparallelness.

The planes are consequently distinct, and their intersection is exactly \(\mathbb Cq\). Each of \(G,U,V\) preserves both planes, so each preserves that line. Its restriction to the line is zero or identity; their sum is identity. Exactly one acts as identity. Thus \(q\) lies wholly in one of the three common two-dimensional sectors.

The diagonal-block rays already have this property. Therefore **every one of the sixty actual rays** lies in one of the three sectors.

This checks the integration step in S1 lines 613–631. It does not require the row and column group projections to commute with one another.

### 7.4 Repeated-ray contradiction

Every physical row and column ONB must contain exactly two rays from each two-dimensional sector: the rays in that sector must span it, and the other sector rays are orthogonal to it.

For a cell ray \(q\) in sector \(K\), let \(x\) be its other row partner in \(K\), and \(y\) its other column partner in \(K\). Both lie in
\[
K\cap(\mathbb Cq)^\perp,
\]
which is one-dimensional. Their cells are distinct, so their parallelness contradicts the global hypothesis.

S1 lines 633–650 therefore exclude the rank-two regime. Both branches of the exhaustive rank split have been checked.

## 8. Exact target relation and orbit transport

For an actual four-dimensional sector on the stated support \(S\), each full context contains four orthonormal sector vectors. They span that sector, forcing its six other context vectors into the common six-dimensional orthogonal complement.

Across the array those vectors are precisely the sixty complementary cells. Their restricted contexts are ONBs, and they inherit global pairwise nonparallelness. The proved complement obstruction therefore excludes the actual \(4+6\) completion. No standalone realization of the forty-cell subsystem is assumed.

For
\[
(r,c)\longmapsto(hr,hc+t),
\]
with \(h\) a unit modulo ten, rows and columns are permuted, cyclic symbols transform by \(s\mapsto hs+t\), and differences transform by \(d\mapsto hd+t\). Thus this is a context-preserving cell relabeling, not a vector-covariance assumption.

The author’s displayed identities for \(3S,7S,9S\) make every unit image a translation of \(S\). A nontrivial translational stabilizer would have order two, five or ten. Orders five and ten are incompatible with a four-element set, and order two would require antipodal-pair structure absent from \(S\). Hence its ten translations are distinct and constitute the full affine orbit.

S1 lines 654–700 support exclusion of the complete assigned ten-mask orbit.

## 9. Findings and acceptance boundary

**FATAL:** None.  
**MAJOR:** None.  
**MINOR:** None.

The supported conclusion is:

> On the sixty cells complementary to \(S=\{0,1,3,4\}\), no sixty pairwise nonparallel unit vectors in \(\mathbb C^6\) can make every restricted row, column and cyclic \(r+c\) symbol class an ONB. Consequently, no actual orthogonal \(4+6\) completion of the original hundred-ray problem can use any four-sector support in this ten-mask affine orbit.

This conclusion requires the actual physical ONB and global nonparallelness hypotheses. The missing-space rigidity follows from the actual projection equations; the two final contradictions explicitly consume individual physical rays.

This return does **not**:

- Adopt the candidate on Main’s behalf.
- Re-review or adopt the separate other ten-mask-orbit candidate.
- Certify a union of prior exclusions with this result covering all one hundred specified masks.
- Establish an unrestricted hundred-ray no-go.
- Resolve noncirculant supports, other resolutions, remaining branches or irreducible arrays.
- Supply a finite execution result, source-equivalence determination, novelty judgment, independent-family review, human verification or kernel/formal proof.
- Independently verify the author’s historical process declarations beyond the frozen text supplied here.

S2 was used for the exact original physical hypotheses and the recorded prior scope, not as a substitute for the reconstruction above or as a new certification of its linked finite checker.

**Overall correctness:** correct.

**Explanation:** The complete written reconstruction supports the candidate’s physical context mapping, noncommutative missing-space rigidity, exhaustive rank split, both individual-ray contradictions and ten-mask-orbit transport. No mathematical blocker was found within that scope; adoption, union bookkeeping and the unrestricted original target remain outside this verdict.

**Confidence:** 0.98.