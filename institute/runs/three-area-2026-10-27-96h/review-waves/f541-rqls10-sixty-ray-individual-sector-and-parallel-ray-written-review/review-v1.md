# f541 — WRITTEN review of the f535 sixty-ray complement obstruction

**Verdict: SUPPORTED at the stated scope.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The proof rules out sixty pairwise nonparallel complex rays on the specified complementary support, without vector covariance. Its essential consuming-side step is valid: the actual rank-one cell projections—not merely their four-cell block spans—must respect a common orthogonal \(2+2+2\) decomposition. The resulting repeated ray occurs at distinct physical cells.

This supports excluding the ten-support two-antipodal-pair orbit **as actual orthogonal \(4+6\) sectors**. It does not contradict the standalone forty-ray construction or establish an unrestricted hundred-ray no-go.

## 1. Binding, coverage and process

Reviewed frozen wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f541-rqls10-sixty-ray-individual-sector-and-parallel-ray-written-review/`

Supplied bindings:

- Manifest: `209378226b8719787d69f6d28778d3db4a76a6018d15eefbe84ec548890213c0`
- Freeze receipt: `a679ca2f54292099b24f583233c2f9b5922fbd185c86e0d57c4d00e7299c0ea8`
- Literal packet: `5f93977bfc3d54aa1597f8ae21258659e2916ad381e16f93abc1dbe1e5a0d4ba`

These are **parent-supplied bindings**, not independently executed child-native hash measurements.

Before reading the mathematical packet, I read the complete manifest, freeze receipt, dispatch receipt, parent metadata supply and all twelve status-only controls, then delivered the direct administrative pre-body ACK. I subsequently read packet lines **1–793**, in consecutive raw windows of at most twenty lines, through the ending, before deriving. No elided packet segment remained. After that complete read, I reread the consuming operator identity at packet lines 314–333.

Scientific coverage was exactly:

| Input | Binding and coverage |
|---|---|
| **S1 — f535 author candidate** | SHA `66d721d49592e97768a0c6b20707dae043db51176aa9466bd5fcf26c72b0c14e`; complete logical lines **1–430**. The receipt reports 429 LF bytes; this is not treated as a claim that only 429 logical lines exist. |
| **S2 — f496 standalone forty-ray candidate** | SHA `b12cd548fbb850d1c13d2cb06cc0e2a47adf7a34b919bec68bff70d4ed0a6784`; authorized selected lines **1–332 only**. |
| **S3 — earlier scoped disposition** | SHA `a4c7197d031810d9986249612b98749efc2edf705986808b718c609b9704152b`; complete lines **1–29**. |

The f496 optional code was neither read nor executed. No scientific links were followed, no sibling review was read, and no new public source was consulted. Quarantined episodes and their consumers remained status-only NONINPUT.

**Scientific execution: NOTRUN.** No scientific code, CAS, interpreter, solver, enumeration, replay, external-model call, or new privately or publicly selected concrete diagnostic was used. The reconstruction below is general written reasoning on the frozen claim.

This is the complete return for parent materialization. No successful filesystem write, write refusal, native clock measurement, or native hash execution is claimed.

## 2. Per-claim dispositions

| Claim | Disposition | Source location |
|---|---|---|
| The CRT description accounts for the sixty physical cells and all thirty six-vector contexts. | **SUPPORTED** | S1 lines 61–113 |
| Each four-cell CRT block is orthonormal, giving actual rank-four \(F_{a,d}\) and rank-two \(E_{a,d}\). | **SUPPORTED** | S1 lines 115–140 |
| Row, column and symbol equations force \(E_{a,d}\) to be independent of \(a\). | **SUPPORTED** | S1 lines 142–238 |
| The three constant rank-two projections form a mutually orthogonal partition of \(\mathbb C^6\). | **SUPPORTED** | S1 lines 240–257 |
| The three-partition lemma applies to the actual row and column pair projections. | **SUPPORTED** | S1 lines 261–312 |
| The correctly indexed product of a row pair and a column pair equals the individual cell projection. | **SUPPORTED** | S1 lines 314–325 |
| Every physical ray lies wholly in one common two-dimensional sector. | **SUPPORTED** | S1 lines 323–332 |
| Every row and column contains exactly two rays in each sector, forcing parallel rays at distinct cells. | **SUPPORTED** | S1 lines 334–352 |
| Consequently, an actual \(4+6\) realization cannot use this four-sector support. | **SUPPORTED** | S1 lines 354–368 |
| The obstruction transports to the entire ten-support affine orbit without ray covariance. | **SUPPORTED** | S1 lines 370–382 |
| This does not invalidate standalone forty-ray feasibility or settle the unrestricted hundred-ray problem. | **SUPPORTED as a scope distinction** | S1 lines 395–418; S2 lines 15, 306–318 |

No mathematical claim in the reviewed f535 proof is REFUTED or left INCONCLUSIVE by this reconstruction. The author’s historical process assertions are not independently certified merely because they appear in the frozen body.

## 3. Reconstruction of the physical context equations

Write
\[
r\leftrightarrow(a,u),\qquad c\leftrightarrow(b,v),
\]
with \(a,b\in\mathbb Z_5\) and \(u,v\in\mathbb Z_2\). The prescribed complement is exactly
\[
b-a\in D=\{2,3,4\}\pmod5.
\]
Thus the variables \(q_{a,d}^{uv}\) represent exactly
\[
5\cdot3\cdot2\cdot2=60
\]
physical cells, with no missing parity choice.

For a fixed row \((a,u)\), the vectors are indexed by \(d\in D\) and \(v\in\mathbb Z_2\). For a fixed column \((b,v)\), they are indexed by \(d\in D\) and \(u\in\mathbb Z_2\), with first coordinate \(a=b-d\).

For a fixed symbol \((s,w)\), the cell equations are
\[
2a+d=s\pmod5,\qquad u+v=w\pmod2.
\]
Since \(2^{-1}=3\) in \(\mathbb Z_5\), these give
\[
a=3(s-d),\qquad v=w-u.
\]
This is precisely the author’s symbol formula. Each context has six vectors. The row, column and symbol parameters each range over ten contexts, so these are the complete thirty physical ONB equations.

For fixed \(a,d\), every pair among the four \(q_{a,d}^{uv}\) is orthogonal:

- Equal \(u\) gives a shared row.
- Equal \(v\) gives a shared column.
- If both parity coordinates differ, their sums \(u+v\) agree in \(\mathbb Z_2\), while their modulo-five symbol coordinate \(2a+d\) is already common.

Consequently,
\[
F_{a,d}=\sum_{u,v}p_{a,d}^{uv}
\]
is an actual rank-four orthogonal projection, and
\[
E_{a,d}=I_6-F_{a,d}
\]
is an actual rank-two orthogonal projection. No incidence mask is being substituted for a physical operator.

Adding the two row equations of a fixed modulo-five row coordinate counts every \(p_{a,d}^{uv}\) once, giving
\[
\sum_d F_{a,d}=2I_6,
\qquad
\sum_d E_{a,d}=I_6.
\]
The column equations give the stated analogous identity. Adding the two symbol-parity equations also counts all four parity pairs once for each relevant block, yielding
\[
\sum_d E_{3(s-d),d}=I_6.
\]

These establish all three displayed missing-space equations without assuming vector covariance.

## 4. Reconstruction of missing-space rigidity

Set
\[
A_a=E_{a,2},\qquad B_a=E_{a,3},\qquad C_a=E_{a,4}.
\]
The row equation and the author’s reindexed column and symbol equations are
\[
A_a+B_a+C_a=I_6,
\]
\[
A_{a+1}+B_a+C_{a-1}=I_6,
\]
\[
A_{a+3}+B_a+C_{a-3}=I_6.
\]

The column substitution \(b=a+3\) and symbol substitution \(s=2a+3\) produce these indices correctly.

Subtracting the first equation from the second gives
\[
C_a-A_{a+1}=C_{a-1}-A_a.
\]
Because this holds around all of \(\mathbb Z_5\), the common difference is a single operator \(K\), so
\[
C_a=A_{a+1}+K.
\]
Subtracting the first equation from the third and substituting this relation gives
\[
A_{a+3}-A_a=A_{a+1}-A_{a-2}.
\]
The equality \(a-2=a+3\) modulo five therefore yields
\[
2A_{a+3}=A_a+A_{a+1}.
\]

The projection-average lemma applies exactly here. If \(P,Q\) and \((P+Q)/2\) are orthogonal projections, idempotence gives
\[
PQ+QP=P+Q,
\]
hence
\[
(P-Q)^2=0.
\]
Since \(P-Q\) is Hermitian, it vanishes. Applying this to \(A_a,A_{a+1}\), whose average is the projection \(A_{a+3}\), proves
\[
A_a=A_{a+1}
\]
for every \(a\). Thus \(A_a\), then \(C_a\), then \(B_a\), are constant.

The resulting rank-two projections \(E_2,E_3,E_4\) sum to \(I_6\). They are mutually orthogonal: for \(x\in\operatorname{ran}E_i\),
\[
\|x\|^2
=\sum_j\langle x,E_jx\rangle
=\|x\|^2+\sum_{j\ne i}\|E_jx\|^2.
\]
All other terms vanish. Therefore
\[
\mathbb C^6=H_2\oplus H_3\oplus H_4,\qquad
H_j=\operatorname{ran}E_j,\quad \dim H_j=2.
\]

This establishes a common decomposition, but does not yet establish individual-ray membership. The next step is therefore genuinely necessary.

## 5. Reconstruction of the consuming-side operator argument

### 5.1 The three-partition lemma

For orthogonal projection partitions \((E_i)\) and \((R_i)\), each with exactly three members, assume \(R_iE_i=0\). Taking adjoints also gives \(E_iR_i=0\).

For any off-diagonal block \(E_jR_iE_k\), \(j\ne k\):

- If \(i=j\), it vanishes by \(E_iR_i=0\).
- If \(i=k\), it vanishes by \(R_iE_i=0\).
- Otherwise \(i,j,k\) exhaust the three indices, and
  \[
  E_jR_iE_k
  =E_j(I-R_j-R_k)E_k=0.
  \]

The last equality uses \(E_jE_k=0\), \(E_jR_j=0\), and \(R_kE_k=0\). Thus each \(R_i\) is block diagonal for the \(E\)-partition.

The argument relies on **three partition members**, not on an unjustified extension to an arbitrary number of members. It works over complex spaces.

### 5.2 Application to actual row and column planes

For each fixed row \((a,u)\),
\[
\mathsf R_{a,d,u}=p_{a,d}^{u0}+p_{a,d}^{u1}
\]
is a rank-two projection. Its three values of \(d\) form an orthogonal partition of \(I_6\), because the row is an ONB. Its range lies in
\[
F_{a,d}=I_6-E_d,
\]
so \(\mathsf R_{a,d,u}E_d=0\). The lemma therefore proves that every such row-plane projection commutes with every \(E_j\).

For each fixed column \((b,v)\),
\[
\mathsf C_{b,d,v}=p_{b-d,d}^{0v}+p_{b-d,d}^{1v}
\]
has the same properties, using the column ONB and the same constant \(E_d\). It too commutes with every \(E_j\).

### 5.3 Exact routing to the physical cell projection

The crucial column index is **\(b=a+d\)**. At this index,
\[
\mathsf C_{a+d,d,v}
=p_{a,d}^{0v}+p_{a,d}^{1v}.
\]
Both factors in
\[
\mathsf R_{a,d,u}\mathsf C_{a+d,d,v}
\]
are consequently sums of projections from the **same four-cell orthonormal block**. Expanding the product, all terms vanish except the shared cell projection:
\[
\mathsf R_{a,d,u}\mathsf C_{a+d,d,v}=p_{a,d}^{uv}.
\]

This is an exact operator identity, not an inference from an unspecified intersection of spans. It requires no global commutation assumption between unrelated row and column planes.

Both factors commute with every \(E_j\), so their product \(p_{a,d}^{uv}\) does as well. Since \(p_{a,d}^{uv}\) has rank one, its range is invariant under every \(E_j\). Each restricted \(E_j\) acts on that one-dimensional range as zero or identity, and their sum acts as identity. Exactly one acts as identity.

Thus **each of the sixty physical rays lies wholly in exactly one common two-dimensional sector**. The transition from missing-space rigidity to individual-ray membership is fully justified.

## 6. Reconstruction of the repeated-ray contradiction

Because every row is an ONB and every rank-one projection belongs to one sector,
\[
\operatorname{tr}E_j
=\operatorname{tr}\!\left(E_j\sum_{\text{row cells}}p\right)
=\sum_{\text{row cells}}\operatorname{tr}(E_jp)
\]
counts precisely the row’s rays in \(H_j\). Since \(\operatorname{rank}E_j=2\), this count is exactly two. The same calculation applies to every column.

For an arbitrary cell ray \(q\in H_j\), its row therefore contains one other \(H_j\)-ray \(x\), and its column contains one other \(H_j\)-ray \(y\). Both are orthogonal to \(q\). Within the complex two-dimensional space \(H_j\), the orthogonal complement of \(\mathbb Cq\) is one-dimensional, so
\[
\mathbb Cx=\mathbb Cy.
\]

The cells containing \(x\) and \(y\) are distinct. Otherwise their common cell would lie in both the selected row and selected column, whose unique intersection is the original cell of \(q\); neither companion is that cell.

This produces parallel rays at distinct physical cells, contradicting global pairwise nonparallelness. The contradiction is not merely an abstract sector-count obstruction.

## 7. Four-sector completion and affine transport

If the forty cells on \(S=\{0,1,5,6\}\) form an actual common four-dimensional sector in a full hundred-ray solution, every row’s four sector vectors are an ONB of that sector. Its other six vectors therefore lie in the common six-dimensional orthogonal complement.

The full column and symbol ONB conditions then give the corresponding six-vector ONBs there. The inherited sixty vectors remain pairwise nonparallel. This is exactly the complementary problem already excluded.

This necessity argument does **not** depend on accepting the f496 construction.

For a unit \(h\) modulo ten and any \(t\), the relabeling
\[
(r,c)\longmapsto(hr,hc+t)
\]
permutes rows and columns and sends symbol \(r+c\) to \(h(r+c)+t\). It sends differences to \(h(c-r)+t\), hence sends the support \(S\) to \(hS+t\). Its inverse therefore pulls any hypothetical transported complementary solution back to the excluded one.

Modulo five, a two-antipodal-pair support is a two-element subset. The units modulo ten project onto every nonzero multiplier modulo five, so these affine maps act transitively on those pairs. There are exactly ten such supports.

Accordingly, the obstruction covers that complete support orbit without any unitary or covariance condition on the vector assignment.

## 8. Imports and acceptance boundaries

The proof’s load-bearing mathematics is reconstructed from S1 itself. The elementary projection facts it needs are proved above.

- **S2** supplies the exact standalone-versus-completion distinction. Its forty-ray feasibility is not a premise of the complement obstruction. This review does not independently adopt the entire f496 construction or its unexecuted checker.
- **S3** supplies the original global nonparallelness and context definitions, and the cyclic support scope. Its earlier binary-rank, mask-classification and finite-execution claims are not needed to establish this new obstruction and were not replayed.
- Historical acceptance labels, author process reports and parent pre-freeze reading do not substitute for proof reconstruction or establish parent adoption.

The supported result remains restricted to:

1. The specified sixty-cell complex ONB problem;
2. Its forced common \(2+2+2\) decomposition;
3. The resulting impossibility under global nonparallelness; and
4. The corresponding ten-support orbit of actual orthogonal \(4+6\) realizations.

It does not settle the other residual four-support orbit, noncirculant supports, other resolutions, the rank-28 \(5+5\) branch, or irreducible ten-dimensional realizations. It supplies no hundred-ray witness, unrestricted hundred-ray no-go, finite execution result, independent-family assurance, human verification, formal/kernel verification, novelty determination, or global closure.

## 9. Final verdict

**Overall correctness:** correct.

**Explanation:** The complete written argument supports the stated sixty-ray obstruction. The projection rigidity, three-partition lemma, correctly routed row–column product identity, exact physical sector counts and distinct-cell parallel-ray contradiction all hold; no FATAL, MAJOR or MINOR defect was found. Parent adoption remains a separate disposition.

**Confidence:** 0.98.