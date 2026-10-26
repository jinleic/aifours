# Assigned MOQLS global-defect reconstruction v1

Reviewer PhysicsRQLS10, physics-5. Actual before-creation clock: **2026-10-23T14:21:51-07:00**. This is the ONE bounded rotation assigned by `peer-review-wave-eighteen-v1.json`; I resume my own complex RQLS10 obligation after returning it.

## Snapshot and verdict

Complete source read: `/Users/jinleic/repos/aifours/physics/evidence/three-area-20261023-96h/parallel-18/moqls8/proof-global-gram-defect-v1.md`, **SHA256 `3b54a3e46ceb9ffa9edccab28664e13e322f5b47707fdffb77a51beba9a608d8`**, observed directly with `shasum -a 256`, exactly matching the assignment. The complete selection-v1.md and review-request-v1.json were also read.

**0 FATAL / 0 MAJOR / 1 MINOR (wording). No substantive mathematical defect found at the stated partial scope.** This is an in-harness written reconstruction with supplied author proof, not blind, cross-vendor, human or formal/kernel review. No executable scientific calculation was used.

What is supported: the full phase-bearing Gram equivalence, exact classicality saturation, orthogonal covariance-range/rank budget, residual/defect identity and the conditional B3 minimum-span dichotomy. What is NOT supported or claimed: D=0, either B3 branch's exclusion, any new GB closure, a nonclassical witness, novelty, or full five-MOQLS(8) classicality.

## Independent mathematical reconstruction

### 1. Full Gram equivalence and phases — source LF15–39

For a square, the n actual row ONBs give `VV*=nI`; hence `G=V*V` obeys `G²=nG`. Conversely Hermitian G with diagonal one and `G²=nG` has eigenvalues 0 or n, trace n² and therefore rank n and positive semidefiniteness. Its rank-n factor gives n orthogonal unit vectors on each real array row/column. The product-state Gram entry is `G_s(x,y)G_u(x,y)`, **without conjugating the second factor**. Thus E4 yields the complete tensor ONB, not merely an overlap-support relaxation.

The free-position count is consistent: for each cell there are `(8-1)²=49` cells outside its row/column; `64*49/2=1568` complex unordered entries per square, and five squares give 7840 complex coordinates. This does not supply feasibility or a runtime claim.

### 2. Classicality and saturation — LF43–67

Positive-semidefinite diagonal-one G gives h in [0,1]. Every term h(1-h) is nonnegative. If their sum vanishes, each cell's squared overlaps with the first-row ONB are 0/1 and sum to one, so its ray is one first-row basis ray. Separate output unitaries are allowed for each square; no incompatible family-level normalization is introduced. Conversely a classical family has only 0/1 h. The real reciprocal `zD=1` is therefore exactly the nonclassical question, with no unjustified margin bound. It is only an encoding/interface, not a constructed solution or an infeasibility proof.

### 3. Covariance normalization and rank budget — LF71–124

I obtain `H_sR=H_sC=J`, `H_s1=n1`, and `rc=cr=p=J/n²`. The n-eigenline of H is exactly the constant direction being removed by `T=H/n-p`. All remaining eigenvalues are nonnegative and at most n by the nonnegative row-sum argument. Hence `0≤T≤E`, with `E=I-r-c+p`, trace n-1 and rank `a_s-1`.

For two different squares, E4 makes all off-diagonal products of h vanish and each diagonal product equals one. Thus `tr(H_s H_u)=n²`; expanding `tr(T_sT_u)` gives zero. Positive-semidefinite trace orthogonality gives the stronger operator identity `T_sT_u=0`, not merely entrywise orthogonality. Their ranks consequently add inside dim W=(n-1)². The resulting n=8,t=5 excess budget is 14. The equivalence `a_s=n iff classical` follows from the first-row projectors spanning the full n-dimensional diagonal algebra, not from counting vector rays alone.

### 4. Residual and fractional spectra — LF128–162

On each mutually orthogonal T-range, K has eigenvalues 1-lambda; on the unused part of W it has eigenvalue one. This reconstructs `0≤K≤E` without assuming T is a projection. Its diagonal is `49/64-5*(7/64)=14/64=7/32`; the row/column off-diagonal and remaining entries agree with LF139–146.

Expansion gives `K-K²=Σ(T_s-T_s²)`. With `tr T_s²=tr H_s²/64-1` and `Σ h_s=512`, I obtain `tr K²=14-D/64`. If D>0, then `(tr K)²≤rank(K) tr K²` forces rank(K)>14. This is **not** a contradiction in dimension 49. Integer trace 14 does not imply idempotence; the author preserves that boundary. The projection/classicality equivalences follow from nonnegative eigenvalue deficits and Theorem C.

### 5. Two-basis span and B3 branches — LF166–217

The intersection of the two diagonal Hermitian algebras consists of real diagonal labels satisfying `(d_k-lambda_i)U_ki=0`, so labels are precisely constant on connected components of the bipartite support graph. Its dimension is c(U), proving span dimension `2n-c(U)` with arbitrary amplitudes/phases.

For the literal table LF189, the four graph components have sizes 1,3,2,2; the A-component is connected because rows1 and7 have all three nonzero coordinates. Thus the axis-projector span has dimension12. If the full projector span is still12, every full-cell rank-one projector lies in the same block-diagonal operator space. A vector nonzero in two blocks would have a nonzero cross-block outer product, so every cell is block-pure. Completeness of each ONB forces exactly the block dimensions as cell counts. Any mixed-block cell gives an additional independent projector direction and the remaining budget decreases from10 to9.

The eight e0 cells are one per row/column. The other square's vectors there are pairwise orthogonal because the square1 factor has nonzero unit-modulus overlaps. This gives the stated shared transversal, **not** an extra full classical square or completion. Neither rank12 realizability nor rank13 impossibility is proved.

## Finding

**MINOR M1 — LF179, scalar entry versus supported basis vector.** “If the transition has an entry supported on w basis coordinates” is imprecise: an entry of the transition matrix U is a scalar. The argument requires a **column of U / basis vector v_i** with w nonzero coordinates. Replace that phrase accordingly. The stated lower bound `a_s≥n+w-1` is correct under that intended meaning; no theorem or numerical bound changes.

## Actual source/dependency checks and limits

- Read actual Ball–Simoens [2607.12933v2](https://arxiv.org/html/2607.12933v2) §§2.2–2.3: product-state orthogonality and family isotopy match the proof exactly. Theorem5 concerns n-2 squares; it does not close five at n=8.
- Read actual Musto–Vicary [1804.04042v3](https://arxiv.org/html/1804.04042v3) Definition4 and the product-state versus entangled-officer distinction. The convention matches E4.
- The exact B3 column table is also present in the old `physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-d-general-extension/D-EXTENSION-CONCENTRATION-CANDIDATE-v1.md` LF16–19, located directly. In the present proof it is an explicit antecedent, not an imported exhaustive normal-form theorem. I do not re-certify U/T16, the historical CNFs, classifications, runtime or stream retention.
- Earlier scalar M(n) bounds do not by themselves state the full rank budget. That observation is not priority clearance: the candidate correctly marks projector methods as prior art and makes no novelty/SOTA claim.
- Both B3 branches remain covered and open. The exact phase Gram constraints cannot be replaced by H or an arbitrary PSD covariance family. No inference D=0 is licensed by this review.

No author file was edited. No scientific script, numerical/exact replay, solver, test suite or external model CLI was executed. This review supplies only the written-check level described above; Main retains source/acceptance integration.
