# f572 — Written review of the other cyclic ten-mask orbit

**Role:** WRITTEN  
**Mathematical verdict:** SUPPORTED at the frozen scope  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR**  
**Scientific execution:** NOTRUN  
**Parent adoption:** Not asserted by this review  
**Unrestricted hundred-ray target:** UNRESOLVED

## 1. Scope and source bindings

I reconstructed the complete proposed obstruction for sixty pairwise nonparallel unit vectors in \(\mathbb C^6\) on
\[
H_T=\{(r,c)\in\mathbb Z_{10}^2:c-r\in T\},
\qquad T=\{2,5,6,7,8,9\},
\]
where every restricted row, column and cyclic symbol class \(r+c\) must be an ONB. I also checked its consequence for an actual common four-dimensional sector on \(S=\{0,1,3,4\}\), its affine transport to ten masks, and the precisely limited conditional union with the two adopted dispositions.

The frozen bindings supplied by Main are:

- Manifest: `a7cfa66c929e898a60ec905254779bed14fd52ae3a48a53cc2c7138ec36dc4c1`.
- Freeze receipt: `7cdb267f5134317117e150aeb8d3ade824e147caaf6ed75ca8e34960fb333dfe`.
- Literal packet: `136028d985e7641ca77eb6e5ccd943a8d0ce325bc27c04b0b92a20eb98c78d84`.

Scientific inputs, using the packet’s source identifiers:

1. **S1 — complete author candidate:**  
   `review-waves/f557-rqls10-other-cyclic-four-sector-orbit-actual-complex-closure-frontier/review-v1.md`  
   SHA-256 `48ef117bd36a93937d078086a82428c166da38df04998f0a18b7777568a8d953`; logical lines 1–747, with 746 LF separators.

2. **S2 — adopted other-complement disposition:**  
   `dispositions/physics-5-rqls10-sixty-ray-complement-and-ten-four-sector-orbit-exclusion-parent-v1.md`  
   SHA-256 `98777a066b61d4023ec20dd0f3f8c1b39a5e0eef4a168a0eaf0f911dc3c6a19d`; lines 1–37.

3. **S3 — adopted binary-sector/cyclic-support disposition:**  
   `dispositions/physics-5-rqls10-binary-sector-and-cyclic-rank4-family-exclusions-parent-v1.md`  
   SHA-256 `a4c7197d031810d9986249612b98749efc2edf705986808b718c609b9704152b`; lines 1–29.

These hashes and the clock observations in the administrative supply are **parent-supplied metadata**, not independently executed child hash or native-clock checks.

## 2. Read sequence and process boundary

Before reading mathematical packet content, I completely read:

- Manifest lines 1–132.
- Freeze receipt lines 1–60.
- All twelve listed permission/status controls, in manifest order and including their endings.
- The parent metadata supply and dispatch receipt.

I then delivered a separate administrative pre-body ACK directly through `agent://Main`. Only afterward did I read the entire literal packet, lines 1–815, in consecutive raw windows of at most twenty lines. This included the complete endings of S1, S2 and S3. No elision appeared in those reads. Derivation began only after the complete packet read.

All quarantine records were used for **status and exclusion only**. No excluded link, held scientific payload, held consumer, sibling review, author code or additional scientific source was opened.

This review uses formal reconstruction of the supplied general arguments, not new selected vector, operator, graph or parameter diagnostics. No scientific executable, interpreter, CAS, enumeration, solver, replay, build, test, lint, formatter, Git command or external-model CLI was run.

No project file was written. This complete body is returned for Main’s materialization; no filesystem-write refusal is claimed.

## 3. Per-claim disposition

| Claim | Source lines | Disposition |
|---|---|---|
| The CRT formulas represent all sixty actual cells and all thirty physical ONB contexts | S1 66–180 | **SUPPORTED** |
| The actual block projections and thirty ONB equations imply balance (6) and annihilations (7) | S1 182–287 | **SUPPORTED** |
| The five missing-space projections commute and have one common pairwise intersection projection \(G\) | S1 291–374 | **SUPPORTED** |
| The rank alternatives are exhaustively \(g=1\) or \(g=2\) | S1 376–395 | **SUPPORTED** |
| The \(g=1\) regime contradicts the actual off-diagonal vectors and global nonparallelness | S1 399–503 | **SUPPORTED** |
| In the \(g=2\) regime, balance forces \(U_a=U\), \(V_a=V\), without ray covariance | S1 505–555 | **SUPPORTED** |
| Actual row and column group planes reduce \(G,U,V\), and their intersection routes each individual off-diagonal ray | S1 557–631 | **SUPPORTED** |
| Three common two-dimensional sectors contradict distinct physical row/column partners | S1 633–652 | **SUPPORTED** |
| The complement obstruction excludes actual \(4+6\) completion on the representative and its ten-mask affine orbit | S1 654–700 | **SUPPORTED** |
| Conditional on adoption of S1, the imported scopes yield exclusion of all 100 specified balanced cyclic/circulant four-sector completions | S2 3–7; S3 15–21; S1 671–700 | **SUPPORTED, conditional on adoption of S1 and the stated prior dispositions** |
| An unrestricted hundred-ray no-go, noncirculant exclusion, other-resolution exclusion, rank-28 \(5+5\) exclusion or irreducible exclusion follows | Outside the proved scope; expressly excluded in S1 714–724 | **INCONCLUSIVE / not established** |

No claim in the frozen candidate was refuted.

## 4. Actual-cell and context reconstruction

Translate the column coordinate by two:
\[
c'=c-2.
\]
This permutes columns and sends the cyclic symbol \(r+c\) to \(r+c-2\). The complementary differences become
\[
T'=\{0,3,4,5,6,7\}.
\]

In CRT coordinates,
\[
r\leftrightarrow(a,u),\qquad c'\leftrightarrow(b,v),
\]
with \(a,b\in\mathbb Z_5\) and \(u,v\in\mathbb Z_2\), the inverse supplied in S1 is
\[
\operatorname{crt}(a,u)=a+5((u-a)\bmod2).
\]
Thus the original physical cell is
\[
(r,c)=\bigl(\operatorname{crt}(a,u),\operatorname{crt}(b,v)+2\bigr).
\]

The support consists exactly of:

- All four bit pairs when \(a=b\).
- \(v=u\) when \(b-a=\pm1\).
- \(v=u+1\) when \(b-a=\pm2\).

The resulting diagonal vectors \(q_a^{uv}\) and off-diagonal vectors \(q_{ab}^u\) therefore label actual cells, not independently chosen context occurrences.

For a row \((a,u)\), the six vectors are
\[
q_a^{u0},\ q_a^{u1},\quad q_{ab}^{u}\ (b\ne a).
\]
For a column \((b,v)\), they are
\[
q_b^{0v},\ q_b^{1v},\quad
q_{ab}^{\,v-\tau(a,b)}\ (a\ne b).
\]
A shifted symbol has CRT label
\[
(s,w)=(a+b,u+v).
\]
Writing \(k=3s\), its parity-zero context comprises the diagonal pair \(q_k^{00},q_k^{11}\) and the two ordered blocks between \(k-2\) and \(k+2\). Its parity-one context comprises \(q_k^{01},q_k^{10}\) and the two ordered blocks between \(k-1\) and \(k+1\).

These are precisely the thirty contexts used downstream. In particular, the symbol equations are attached to the actual same vectors as the row and column equations; there is no independent symbol gauge.

## 5. Projection balance and missing-space rigidity

### 5.1 Actual projections

Within a diagonal block, two different vectors share a row, column or symbol according to which bits differ. Thus all four are mutually orthogonal, and
\[
F_a=\sum_{u,v}p_{q_a^{uv}}
\]
is a rank-four orthogonal projection.

The projections
\[
U_a=p_{q_a^{00}}+p_{q_a^{11}},\qquad
V_a=p_{q_a^{01}}+p_{q_a^{10}},\qquad
E_a=I-F_a
\]
are mutually orthogonal, each of rank two, and sum to \(I\).

For \(a\ne b\), the two vectors \(q_{ab}^0,q_{ab}^1\) share a symbol and are orthogonal. Hence
\[
P_{ab}=p_{q_{ab}^0}+p_{q_{ab}^1}
\]
is an actual rank-two projection.

### 5.2 Balance

Adding the two row ONB equations at \(a\), and separately the two column equations, gives
\[
\sum_{b\ne a}P_{ab}=I+E_a,\qquad
\sum_{b\ne a}P_{ba}=I+E_a.
\]
The two kinds of symbol equations are
\[
P_{k-2,k+2}+P_{k+2,k-2}=I-U_k,
\]
\[
P_{k-1,k+1}+P_{k+1,k-1}=I-V_k.
\]

Grouping each outgoing block with its reversal yields exactly
\[
U_{a-2}+U_{a+2}+V_{a-1}+V_{a+1}=2F_a.
\]
Taking the quadratic form on \(\operatorname{ran}E_a\), positivity of every summand gives
\[
E_aU_{a\pm2}=0,\qquad E_aV_{a\pm1}=0,
\]
and the reverse products vanish by adjunction. Consequently,
\[
E_{a\pm1}\le E_a+U_a,\qquad
E_{a\pm2}\le E_a+V_a.
\]

### 5.3 Rigidity without assumed commutation

The projection-contraction observation in S1 is valid: from
\[
PQ=PRQ,\qquad RQ=RPQ,
\]
for \(x\in\operatorname{ran}Q\), the vectors \(y=Px\) and \(z=Rx\) satisfy
\[
y=Pz,\qquad z=Ry.
\]
The two contraction inequalities are equalities, forcing \(y=z\), so
\[
(P-R)Q=0.
\]

Apply this with
\[
P=E_{a-1},\quad Q=E_a,\quad R=E_{a+1}.
\]
Relative to the partition at \(a+1\), the parts of \(P\) and \(Q\) outside \(R\) lie in orthogonal \(V\)- and \(U\)-spaces. This proves \(PQ=PRQ\); the partition at \(a-1\) proves the other identity. Therefore
\[
(E_{a-1}-E_{a+1})E_a=0.
\]

For \(T_a=E_aE_{a+1}\), this gives
\[
T_a=T_{a+1}^{\dagger}.
\]
The odd five-cycle forces every \(T_a\) to be the same self-adjoint operator. A self-adjoint product of two orthogonal projections is their commuting intersection projection.

Repeating the argument in the distance-two cyclic order gives the same conclusion for all distance-two products. Each of these common projections lies in every \(E_a\); comparison through the corresponding intersections shows they coincide. Thus
\[
E_aE_b=G\qquad(a\ne b)
\]
for one orthogonal projection \(G\).

This proves the needed commutation rather than assuming it.

### 5.4 Exhaustive ranks

Put \(g=\operatorname{rank}G\). The five projections \(E_a-G\) are mutually orthogonal, each has rank \(2-g\), and each is orthogonal to \(G\). Hence
\[
g+5(2-g)\le6.
\]
With \(0\le g\le2\), this leaves exactly
\[
g=1\quad\text{or}\quad g=2.
\]

## 6. The rank-one regime

When \(g=1\), let
\[
L_a=\operatorname{ran}(E_a-G).
\]
The rank equality gives
\[
\mathbb C^6=\operatorname{ran}G\oplus\bigoplus_{a\in\mathbb Z_5}L_a,
\]
where the \(L_a\) are mutually orthogonal lines. The annihilations and rank two of \(U_a,V_a\) then force
\[
\operatorname{ran}U_a=L_{a-1}\oplus L_{a+1},\qquad
\operatorname{ran}V_a=L_{a-2}\oplus L_{a+2}.
\]

The candidate’s coordinate/noncoordinate dichotomy is exhaustive over complex two-dimensional ONBs. If either vector has a zero coefficient, orthogonality forces the basis to be the two coordinate lines. Otherwise both vectors have nonzero coefficients on both lines.

Every coordinate basis uses two of the five fixed \(L\)-rays. Global pairwise nonparallelness prohibits reuse of any such ray. Thus at most two of the ten diagonal-block bases are coordinate, leaving at least three indices whose two bases are both noncoordinate.

For distinct such good indices \(a,b\), let \(k=3(a+b)\). The applicable symbol equation places every \(q_{ab}^u\) in
\[
\operatorname{ran}G\oplus L_a\oplus L_b\oplus L_k.
\]
Relative to \(a\), the indices \(b\) and \(k\) belong to different \(U_a/V_a\) classes. Orthogonality to the actual two diagonal vectors in its row, each noncoordinate in its respective plane, therefore kills the \(L_b\) and \(L_k\) components. Thus
\[
q_{ab}^u\in\operatorname{ran}E_a.
\]
The actual column argument at the good index \(b\) kills the corresponding components and gives
\[
q_{ab}^u\in\operatorname{ran}E_b.
\]
Consequently both orthogonal unit vectors \(q_{ab}^0,q_{ab}^1\) lie in the one-dimensional intersection \(\operatorname{ran}G\), a contradiction.

This consuming argument uses the individual physical vectors and their actual row/column orthogonality. It does not treat a block-support condition as sufficient.

## 7. The rank-two regime and individual-ray consumer

### 7.1 Constant sector projections

When \(g=2\), rank equality forces
\[
E_a=G,\qquad U_a+V_a=F:=I-G.
\]
Substituting \(V_a=F-U_a\) into balance gives
\[
U_{a-2}+U_{a+2}-U_{a-1}-U_{a+1}=0.
\]

For a fifth-root Fourier mode, the multiplier is
\[
z^2+z^{-2}-z-z^{-1}
=(x-2)(x+1),\qquad x=z+z^{-1}.
\]
For nontrivial \(z^5=1\), neither factor vanishes: \(x=2\) forces \(z=1\), while \(x=-1\) gives \(z^2+z+1=0\), incompatible with a nontrivial fifth root. Applied entrywise to the operator-valued identity, this eliminates every nonconstant Fourier coefficient. Therefore
\[
U_a=U,\qquad V_a=V,
\]
and \(G,U,V\) are fixed mutually orthogonal rank-two projections summing to \(I\).

This is a linear operator identity; no covariance of vectors is introduced.

The symbol equations now imply
\[
P_{ab}\le
\begin{cases}
G+V,&b-a=\pm1,\\
G+U,&b-a=\pm2.
\end{cases}
\]

### 7.2 Actual group planes reduce the sectors

The three-partition lemma is correct. For orthogonal projection partitions
\[
\sum_iA_i=\sum_iQ_i=I,\qquad Q_iA_i=0,
\]
every block \(A_jQ_iA_k\) with \(j\ne k\) vanishes. If \(i=j\) or \(i=k\), annihilation gives the result. If all three indices differ, substituting \(Q_i=I-Q_j-Q_k\) gives it. Hence every \(Q_i\) commutes with every \(A_j\).

For an actual row, let \(R,X,Y\) project onto its diagonal pair, its difference-\(\pm1\) pair and its difference-\(\pm2\) pair. The row ONB ensures that these are orthogonal rank-two projections summing to \(I\). Their supports give
\[
RG=0,\qquad XU=0,\qquad YV=0.
\]
The lemma therefore shows that each row group plane reduces \(G,U,V\).

For an actual column, the same three groups consist of its diagonal pair and its two corresponding difference pairs. Column orthogonality and the same block supports give exactly the same conclusion. Thus the necessary consuming-side statement holds for **both** physical context families.

### 7.3 Intersection routes the individual ray

For an off-diagonal cell vector \(q\), let \(M\) and \(N\) be its row and column group planes. Both have dimension two, both contain \(q\), and both are preserved by \(G,U,V\).

If \(M=N\), the other vector in the row pair and the other vector in the column pair both lie on the one-dimensional orthogonal complement of \(q\) inside that plane. They must be parallel. Their cells are distinct because the physical row and column intersect only at the original cell of \(q\). Global nonparallelness excludes this possibility.

Therefore \(M\ne N\), and
\[
M\cap N=\mathbb Cq.
\]
Each sector projection preserves both planes, so it preserves their intersection. Its restriction to that line is an idempotent scalar, hence zero or identity. Since the three projections sum to identity, exactly one restricts to identity. Thus every off-diagonal ray lies wholly in exactly one of
\[
\operatorname{ran}G,\qquad \operatorname{ran}U,\qquad \operatorname{ran}V.
\]

This step requires **no commutation between the row and column group projections**. It uses invariance of their intersection. It also does not infer individual-ray routing merely from reduction of a larger block span.

The diagonal rays already lie in \(U\) or \(V\), so all sixty individual rays have now been routed.

### 7.4 Distinct partners give the contradiction

Each row and each column ONB contains exactly two rays from each fixed two-dimensional sector. For a cell ray \(q\) in a sector \(K\), its other same-sector row ray and its other same-sector column ray lie in
\[
K\cap(\mathbb Cq)^\perp,
\]
which is one-dimensional. They are therefore parallel.

They occur at distinct physical cells, again because the row and column intersect only at \(q\). This contradicts global pairwise nonparallelness and excludes \(g=2\).

Both exhaustive rank regimes are consequently impossible.

## 8. Actual \(4+6\) completion and affine orbit

The passage from the sixty-cell theorem to the original array is valid only for an **actual common four-dimensional sector**, as the candidate states.

Each full context has four sector rays and six complementary cells. The four orthonormal sector rays span that common four-dimensional space. Its remaining six context rays therefore lie in its common six-dimensional orthogonal complement and form an ONB there. Across the array, these are precisely the sixty cells of \(H_T\), and their rays inherit global nonparallelness. This is the excluded problem.

For a unit \(h\bmod10\), the cell map
\[
(r,c)\longmapsto(hr,hc+t)
\]
permutes rows and columns, sends symbols to \(h(r+c)+t\), and sends differences to \(h(c-r)+t\). Hence it transports the obstruction to \(hS+t\) without imposing a unitary representation on the rays.

The supplied identities
\[
3S=S+9,\qquad7S=S+7,\qquad9S=S+6
\]
show that the affine orbit consists of translations. Those translations are distinct: a stabilizing shift of order five or ten cannot preserve a four-element set, and an order-two stabilizer would make \(S\) a union of antipodal pairs, which it is not. The orbit therefore has exactly ten masks.

## 9. Exact prior imports and conditional union

The proof of the new sixty-cell obstruction above is self-contained within S1. It does **not** import the separate f535 theorem or a prior reviewer’s reasoning.

For the union statement only, the exact adopted imports are:

- **S3 lines 15–21:** among the 100 balanced four-element difference masks for the cyclic resolution, 60 arithmetic-progression masks and a separate 20-mask orbit are excluded already at the four-dimensional physical stage. The two residual affine orbits have representatives \(\{0,1,3,4\}\) and \(\{0,1,5,6\}\), each of size ten.
- **S2 lines 3–7 and 27:** the \(\{0,1,5,6\}\) orbit is excluded as an actual \(4+6\) completion by its own sixty-dimensional-complement argument, giving the prior 90-support scope.

S3 explicitly identifies the two residual orbits separately from its excluded 80. The present S1 addresses the other named residual orbit. Thus, **if Main adopts S1 at the proved scope**, those dispositions support exclusion of all 100 balanced **cyclic-resolution, circulant four-sector supports as actual full \(4+6\) realizations**.

This is bookkeeping from the stated adopted scopes, not a fresh finite enumeration, re-execution or verification of their linked artifacts. S2’s execution descriptions remain attributed to that disposition; no such execution was performed here. Its disclosed f540 ACK transport qualification is not erased by this review.

The conditional union is not retrospective adoption of S1 and is not an unrestricted hundred-ray no-go.

## 10. Findings, exclusions and final verdict

**FATAL:** None.  
**MAJOR:** None.  
**MINOR:** None.

The especially load-bearing individual-ray interface is complete: actual row and column group planes reduce the sector projections; equal planes violate global nonparallelness; distinct planes intersect in precisely the cell ray; invariance of that intersection forces the ray into one sector. No unproved mutual commutation of the two group planes is used.

This review supplies no:

- Sixty- or hundred-ray construction.
- Executed finite corroboration.
- Claim about standalone forty-ray realizability.
- Exclusion of noncirculant supports or other Latin resolutions.
- Resolution of rank-28 \(5+5\) or irreducible ten-dimensional branches.
- Printed-source equivalence, novelty, worldwide-priority, independent-family, human or formal/kernel assurance.
- Rehabilitation of any held episode or consumer.

**Overall correctness:** correct.

**Explanation:** The complete written argument supports the stated sixty-cell complement obstruction and its transport to the assigned ten-mask orbit. Conditional on parent adoption and the two explicitly imported dispositions, it also supports the limited 100-mask cyclic/circulant \(4+6\) exclusion, without resolving the unrestricted hundred-ray problem.

**Confidence:** 0.97.