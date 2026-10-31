# F540 — WRITTEN review of the sixty-ray complement obstruction

**Candidate:** f535, “No globally distinct six-dimensional complement to the two-antipodal-pair four-sector support”  
**Verdict:** **SUPPORTED at the stated sixty-cell and ten-support \(4+6\) scope.**  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**

The proof correctly derives constant, actual rank-two missing-space projections from the thirty physical ONB conditions, then proves that the individual cell rays—not merely their four-dimensional block spans—respect the resulting \(2+2+2\) decomposition. The final row/column argument forces parallel rays at different cells. No unrestricted hundred-ray conclusion follows.

## 1. Frozen inputs and review procedure

The review used the frozen wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f540-rqls10-sixty-ray-missing-projection-rigidity-written-review/`

Bindings supplied by the parent and user:

- Manifest SHA-256: `a868b8d7c9ba36c4a18e2eb4e66197fcd1bf3f7100ad0e697705278db6d8387b`
- Freeze-receipt SHA-256: `0a09d2e8366f8ce6da31d996b145a5974a0a4e86c05a60ef08f2881711154ca1`
- Literal-packet SHA-256: `4b24f7ab1119653a5d2d10b91b97962764d7e2dbe33aa48355d55fb26e4eb61c`

These are **supplied bindings, not independently recomputed hashes**.

Before opening the mathematical packet, I read the complete manifest, freeze receipt, parent metadata supply, dispatch receipt, and every listed status-only control through its ending. An attempted administrative ACK through `agent://parent` failed because that route was unavailable. A direct pre-body ACK was then delivered in the conversation **before the first mathematical packet read**.

I subsequently read packet LF **1–461**, in consecutive exact raw windows of at most twenty LF, including both source endings, before deriving the review:

| Source | Coverage | Supplied source SHA-256 |
|---|---|---|
| **S1:** f535 `review-v1.md` | Complete logical source lines 1–430; receipt records 429 LF separators | `66d721d49592e97768a0c6b20707dae043db51176aa9466bd5fcf26c72b0c14e` |
| **S2:** binary-sector/cyclic-support parent disposition | Complete source lines 1–29 | `a4c7197d031810d9986249612b98749efc2edf705986808b718c609b9704152b` |

No source links were followed. No author optional checker, sibling review, prior reviewer body, or held mathematical payload was read. Quarantine controls were used only for their status and exclusion boundaries.

**Scientific execution: NOTRUN.** No scientific code, interpreter, CAS, solver, enumeration, finite replay, selected concrete probe, external-model call, build, test, lint, or formatter was used. The frozen parent clock is not represented as a reviewer-native clock.

This review checks the mathematical argument in S1. It does not independently certify S1’s historical statements about the author’s earlier reads or execution history.

## 2. Per-claim assessment

| Claim | Assessment | Source lines |
|---|---|---|
| CRT indexing represents exactly the sixty specified physical cells and all thirty six-vector contexts | **SUPPORTED** | S1:59–107 |
| Every four-cell CRT block consists of four mutually orthogonal physical rays; its missing operator is an actual rank-two orthogonal projection | **SUPPORTED** | S1:109–140 |
| Summing paired physical contexts produces the three stated projection equations, with the stated modulo-five reindexing | **SUPPORTED** | S1:142–182 |
| These equations force every \(E_{a,d}\) to be independent of \(a\), without assuming commutativity or vector covariance | **SUPPORTED** | S1:184–258 |
| The three-partition lemma is valid and applies to both row-plane and column-plane partitions | **SUPPORTED** | S1:261–312 |
| Every individual rank-one cell projection commutes with the fixed missing-space partition | **SUPPORTED** | S1:314–332 |
| Global pairwise nonparallelness is impossible on the sixty cells | **SUPPORTED** | S1:334–352 |
| An actual \(4+6\) completion with four-sector support \(\{0,1,5,6\}\) is excluded | **SUPPORTED** | S1:354–368 |
| The exclusion transports to the entire ten-support two-antipodal-pair affine orbit | **SUPPORTED** | S1:370–382 |
| Standalone forty-ray feasibility is contradicted | **Not claimed; no such conclusion follows** | S1:21–27, 418 |
| An unrestricted hundred-ray no-go is established | **Not claimed; not established** | S1:395–404, 428 |

No claimed mathematical implication was found REFUTED or INCONCLUSIVE.

## 3. Reconstruction of the physical-cell and context routing

### 3.1 Exactly sixty cells

Write
\[
r\leftrightarrow(a,u),\qquad c\leftrightarrow(b,v)
\]
under \(\mathbb Z_{10}\cong\mathbb Z_5\times\mathbb Z_2\). The stated inverse
\[
\operatorname{crt}(a,u)=a+5((u-a)\bmod2)
\]
has the required residues modulo five and modulo two.

The difference set
\[
\{2,3,4,7,8,9\}\subset\mathbb Z_{10}
\]
is exactly the inverse image of
\[
D=\{2,3,4\}\subset\mathbb Z_5.
\]
Consequently, the labels
\[
(a,d,u,v)\in\mathbb Z_5\times D\times\mathbb Z_2^2
\]
give precisely the sixty distinct cells
\[
(r,c)=\bigl(\operatorname{crt}(a,u),\operatorname{crt}(a+d,v)\bigr).
\]

This is a physical-cell parametrization, not an abstract incidence mask substituted for vectors.

### 3.2 All thirty contexts

For a fixed physical row \((a,u)\), the six cells are indexed by \(d\in D\) and \(v\in\mathbb Z_2\).

For a fixed physical column \((b,v)\), they are indexed by \(d\in D\) and \(u\in\mathbb Z_2\), with \(a=b-d\).

For a fixed cyclic symbol \((s,w)\), the equations are
\[
2a+d=s\pmod5,\qquad u+v=w\pmod2.
\]
Since \(2^{-1}=3\pmod5\), these give
\[
a=3(s-d),\qquad v=w-u,
\]
exactly as in S1:99–105.

Thus all ten rows, ten columns, and ten cyclic symbol classes are represented, each with six distinct cells.

### 3.3 Four-cell blocks are genuinely orthonormal

Fix \(a,d\). Any two different parity pairs \((u,v)\) either:

- agree in \(u\), so their cells share a row;
- agree in \(v\), so their cells share a column; or
- differ in both coordinates, so their sums \(u+v\) agree modulo two, while their symbol coordinate modulo five is the common value \(2a+d\).

The third case therefore shares a physical cyclic symbol class. Every pair in the block is orthogonal by an actual required ONB condition.

Accordingly,
\[
F_{a,d}=\sum_{u,v}p_{a,d}^{uv}
\]
is an orthogonal projection of rank four, and
\[
E_{a,d}=I_6-F_{a,d}
\]
is an orthogonal projection of rank two. No sufficiency claim is inferred from incidence counts.

## 4. Reconstruction of missing-projection rigidity

Summing the two row ONB equations with fixed \(a\) counts every member of each four-cell block once:
\[
\sum_{d\in D}F_{a,d}=2I_6.
\]
There are three values of \(d\), so
\[
\sum_{d\in D}E_{a,d}=I_6.
\]

The two columns with fixed modulo-five coordinate \(b\), and the two symbols with fixed modulo-five coordinate \(s\), similarly give
\[
\sum_{d\in D}E_{b-d,d}=I_6,\qquad
\sum_{d\in D}E_{3(s-d),d}=I_6.
\]

Set
\[
A_a=E_{a,2},\qquad B_a=E_{a,3},\qquad C_a=E_{a,4}.
\]
The author’s reindexing is correct:

- the row equation gives \(A_a+B_a+C_a=I_6\);
- choosing \(b=a+3\) gives
  \[
  A_{a+1}+B_a+C_{a-1}=I_6;
  \]
- choosing \(s=2a+3\) gives
  \[
  A_{a+3}+B_a+C_{a-3}=I_6.
  \]

Subtracting the first equation from the second yields
\[
C_a-A_{a+1}=C_{a-1}-A_a.
\]
Hence \(C_a=A_{a+1}+K\) for one operator \(K\) independent of \(a\). Subtracting the first equation from the third then gives
\[
A_{a+3}-A_a=A_{a+1}-A_{a-2}.
\]
Because \(a-2=a+3\) modulo five,
\[
2A_{a+3}=A_a+A_{a+1}.
\]

The projection-average lemma is valid without a commutativity assumption. If \(P,Q\), and \((P+Q)/2\) are orthogonal projections, idempotence of the average gives
\[
PQ+QP=P+Q,
\]
and therefore
\[
(P-Q)^2=0.
\]
For every vector \(z\),
\[
\|(P-Q)z\|^2=\langle z,(P-Q)^2z\rangle=0,
\]
since \(P-Q\) is self-adjoint. Thus \(P=Q\).

Applying the lemma gives \(A_a=A_{a+1}\) for every \(a\). Then \(C_a=A_{a+1}+K\) and \(B_a=I_6-A_a-C_a\) are constant as well.

We therefore obtain fixed rank-two projections \(E_2,E_3,E_4\) satisfying
\[
E_2+E_3+E_4=I_6.
\]
They are mutually orthogonal: if \(x\in\operatorname{ran}E_i\), the identity implies
\[
\|x\|^2=\|x\|^2+\sum_{j\ne i}\|E_jx\|^2.
\]
Thus every other \(E_j\) annihilates \(x\). Their ranges form
\[
\mathbb C^6=H_2\oplus H_3\oplus H_4,\qquad \dim H_j=2.
\]

All operators here remain the actual operators derived from the hypothetical vectors.

## 5. Consuming-side check: from block projections to individual rays

This is a necessary integration step; constancy of the block complements alone would not prove the theorem.

### 5.1 The three-partition lemma

Suppose
\[
\sum_i E_i=I,\qquad \sum_i R_i=I,\qquad R_iE_i=0,
\]
where each family is an orthogonal projection partition with three members.

For \(j\ne k\), consider \(E_jR_iE_k\). If \(i=j\) or \(i=k\), it vanishes using \(E_iR_i=0\) or \(R_iE_i=0\), respectively. Otherwise \(i,j,k\) are the three different indices, so
\[
E_jR_iE_k=E_j(I-R_j-R_k)E_k=0.
\]
Each term vanishes by orthogonality of the \(E\)-partition or by the corresponding annihilation relation.

Thus \(R_i\) is block diagonal for the \(E\)-partition and commutes with every \(E_j\). The proof is valid over complex spaces and does not use an unstated dimension restriction.

### 5.2 Both required consumers satisfy the lemma

For each row, the three projections
\[
\mathsf R_{a,d,u}=p_{a,d}^{u0}+p_{a,d}^{u1}
\]
form an orthogonal partition of \(I_6\). Each is contained in \(F_{a,d}=I_6-E_d\), so
\[
\mathsf R_{a,d,u}E_d=0.
\]
The lemma therefore applies.

For each column, the projections
\[
\mathsf C_{b,d,v}=p_{b-d,d}^{0v}+p_{b-d,d}^{1v}
\]
also form an orthogonal partition. Constancy of \(E_{a,d}\) ensures that their corresponding missing projection is the same \(E_d\), independent of \(b-d\). The lemma applies to these column projections as well.

### 5.3 The product recovers the physical rank-one projection

For the cell \((a,d,u,v)\), the row-plane and column-plane projections in S1:314–323 are sums of projections from the **same orthonormal four-cell block**:
\[
\mathsf R_{a,d,u}=p_{a,d}^{u0}+p_{a,d}^{u1},\qquad
\mathsf C_{a+d,d,v}=p_{a,d}^{0v}+p_{a,d}^{1v}.
\]
Their product is exactly
\[
\mathsf R_{a,d,u}\mathsf C_{a+d,d,v}=p_{a,d}^{uv};
\]
all other products vanish by the already-established block orthogonality.

Both factors commute with every \(E_j\), so their product does too. This does not assume that arbitrary row and column projections commute.

A rank-one projection commuting with every \(E_j\) has a one-dimensional range preserved by each \(E_j\). On that line each \(E_j\) acts as zero or identity, and their sum acts as identity. Exactly one therefore acts as identity.

Hence every physical cell ray lies wholly in exactly one of \(H_2,H_3,H_4\). The consuming-side implication is complete.

## 6. Reconstruction of the forced parallel pair

Each row is a six-vector ONB, and its vectors lie in the three mutually orthogonal two-dimensional spaces. Each row consequently has exactly two rays in each space. The same holds for each column.

Take a cell ray \(q\in H_j\). Its row contains one other \(H_j\)-ray \(x\), and its column contains one other \(H_j\)-ray \(y\). Both are orthogonal to \(q\). Since \(H_j\) is two-dimensional,
\[
H_j\cap(\mathbb Cq)^\perp
\]
is one-dimensional, so \(\mathbb Cx=\mathbb Cy\).

The cells containing \(x\) and \(y\) are different: the chosen row and column intersect only at the cell of \(q\), and neither other ray occupies that cell.

This contradicts global pairwise nonparallelness. It establishes the sixty-cell no-go, not merely a necessary compatibility condition.

## 7. Four-sector completion and affine-orbit scope

Suppose the full hundred-ray problem had an actual common four-dimensional sector on
\[
\{(r,c):c-r\in S\},\qquad S=\{0,1,5,6\}.
\]
Each row contains four selected rays. They are orthonormal in the common four-dimensional space, hence form its ONB. The remaining six row rays lie in its common six-dimensional orthogonal complement.

Each column and cyclic symbol class likewise has four selected cells and six complementary cells. For symbol classes this also follows directly from the CRT description: \(S\) is the inverse image of \(\{0,1\}\) modulo five, while the complementary differences are the three values in \(D\). Each such difference contributes two cells to a fixed symbol context.

The full ONB conditions therefore make the complementary sixty rays a solution of precisely the problem already excluded. Pairwise nonparallelness is inherited from the full array.

For a unit \(h\in\mathbb Z_{10}^{\times}\) and \(t\in\mathbb Z_{10}\),
\[
(r,c)\longmapsto(hr,hc+t)
\]
is a cell bijection preserving the three context families up to relabeling:
\[
r+c\longmapsto h(r+c)+t,\qquad
c-r\longmapsto h(c-r)+t.
\]
A hypothetical realization on support \(hS+t\) thus pulls back to one on \(S\). No vector covariance or associated unitary representation is assumed.

Finally, \(S\) is the inverse image of a two-element subset of \(\mathbb Z_5\). The units modulo ten reduce to all nonzero residues modulo five, and affine maps over \(\mathbb Z_5\) transport \(\{0,1\}\) to any two-element subset. There are exactly \(\binom52=10\) such supports. The stated ten-support exclusion follows.

## 8. Imports and boundaries

The new obstruction is reconstructed directly from S1’s specified physical hypotheses. It does **not** require:

- accepting or executing the f496 forty-ray construction;
- importing the binary-rank theorem from S2;
- rerunning or relying on S2’s historical finite checker;
- assuming vector covariance;
- treating a balanced incidence selector as a physical realization.

S2:7 supplies original-target terminology, and S2:19 identifies the previously residual support orbit. S2’s broader historical proof and execution claims are not independently re-certified by this review.

The supported conclusions are exactly:

1. No sixty globally pairwise nonparallel unit vectors in \(\mathbb C^6\) satisfy the stated thirty restricted ONB conditions.
2. Any hypothetical solution of those ONB conditions, without the global nonparallelness requirement, has the proved common \(2+2+2\) ray decomposition.
3. No actual orthogonal \(4+6\) completion uses \(S=\{0,1,5,6\}\), or another support in its ten-support affine orbit.

This review does **not** establish impossibility of the standalone forty-ray subsystem, the other residual orbit represented by \(\{0,1,3,4\}\), noncirculant supports, other Latin resolutions, the rank-28 \(5+5\) branch, or an irreducible ten-dimensional realization. It provides no unrestricted hundred-ray no-go.

## 9. Findings, evidence classification, and delivery

**FATAL: 0. MAJOR: 0. MINOR: 0.** No corrective erratum is requested for the scoped argument.

This is a **same-harness written reconstruction**. It is not finite-execution, independent-family, human, formal/kernel, novelty, or worldwide-priority assurance. Parent adoption is not conferred by this return.

The complete review body is returned for parent materialization. No `review-v1.md` filesystem write was performed, and no filesystem-write refusal is claimed.

**Overall correctness:** correct.  
**Explanation:** The sixty-cell proof covers the actual context routing, establishes missing-projection rigidity without covariance, and successfully carries that rigidity through row/column consumers to individual rays and a forced parallel pair. Its ten-support \(4+6\) consequence is valid at the expressly limited scope.  
**Confidence:** 0.98.