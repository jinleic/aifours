# Qubit-side rank-two partial traces and original-projector strictness

**Disposition: adopt the clean f301 written proof at the exact scopes below.** Native clock before composition: 2026-10-30T06:44:02-0700 PDT. Earlier f284/f286 selected-instance reviews and all their consumers remain HELD/ZERO/NONINPUT; they contribute nothing. The source has no load-bearing defect after the explicit traceless-D qualification. No whole-target closure is claimed.

## Adopted theorems

For every n>=1 and every complex operator R on C2 tensor Cn with rankR<=2,

q(R):=||Tr_n R||_F²+||Tr_2 R||_F²−|TrR|²/2 <=2||R||_F².

For every traceless complex A,B in M4, let X=A tensor I4+I4 tensor B and L=||A||_F²+||B||_F². Every rank-two orthogonal projector P with either marginal Tr_A P or Tr_B P of rank at most2 satisfies Tr(PX†X)<=2L. Equality forces at least one of A²,B² normal; if BOTH squares are nonnormal the inequality is strict for every such P. Thus a maximizing top-two right-singular projector with that marginal property proves S2(X)<=2L, strictly on the both-squares-nonnormal class. No PPT/separability, common reducing basis or other-marginal condition is needed.

## Universal written reconstruction

Unitary-hollow the traceless2x2 partial trace and write R in blocks [P,Q;T,S]. The exact gap identity splits into ||P−S||²−|Tr(P−S)|²/2 plus the Q,T rank-two trace deficits. Hollowing kills the trace term; compressions have rank<=2 and |TrZ|²<=rankZ||Z||², proving q<=2||R||² including n=1 and rank/zero boundaries.

Weighted KyFan duality pairs tI_(2n)+C tensor I_n+I2 tensor D, with BOTH C and D traceless, against rank-two R. The dual factor is exactly one half of q, using ||Tr_n R||²=|TrR|²/2+||(Tr_n R)_0||² and the corresponding n-dimensional formula. This proves the weighted source inequality in both directions.

For an original P of local rank<=2, PSD support reduction embeds its range in S tensor C4. Writing A in S/S-perp blocks yields the exact leakage Tr(PX†X)=Tr(PY†Y)+Tr(rho A21†A21). The source gap decomposes into four nonnegative terms: the weightedY gap, 2||A12||², Tr((2I−rho)A21†A21), and2(||A22||²−2|alpha|²). Parent re-expanded these terms and checked traceA22=−2alpha and0<=rho<=2I in writing.

At local rank1 the complete-square gap and trace equality force B to be scalar on each of two orthogonal rank-two blocks (or A after swapping), so its square is normal. At local rank2, equality makes offblocks vanish andA22=−alpha I; all KyFan/dual bounds saturate. Hollowing then gives R=[G,Q;T,G], with each nonzero offblock lambda times a rank-two orthogonal projection. Rank-two column-space pivoting forces G=Pi G Pi andT=lambda^−1 G². Nilpotent-square, nonzero scalar-square and coincident/distinct-eigenvalue cases force B² normal; if Q=T=0, A² is scalar. Reviewer independently proved every pivot/equality step; the parent checked the support, four-gap identity, trace-equality classification and pivot implication at all-variable scope.

## Prospective composition with the adopted dual reduction

Define a COMMON local support of R in M4 tensor M4 by R=(Pi_S tensor I)R(Pi_S tensor I), or the swapped version; both its domain and range lie in the same local S. If dimS<=2, isometric embedding into C2 tensor C4 preserves rank, full trace, partial-trace Frobenius norms and||R||. The theorem above therefore pays(Q) on every such R. Combined prospectively with [f302](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/physics-1-rank2-dual-equivalence-and-core-gram-conditional-parent-v1.md), a remaining hypothetical Q failure must have rank2, nonzero trace, non-EP, nonzeroC12, and common local supports at least3 on both sides. This definition does NOT identify support with only one range marginal or prove the separate uniform-(m,n) support-hierarchy equivalence, which stays unreviewed.

## Review qualifications and evidence

Review source precision findings retained: D must be declared traceless in the weighted lemma (all actual original-pair uses already have D=B traceless); “every complexR” carries rank<=2; loose dual-norm phrasing is replaced by the explicit weighted Cauchy inequality. Two review-text slips are NOT adopted: its F3 calls the source's e^(+i phi) Schur expectation a typo, but direct multiplication for the stated vector gives precisely the original plus sign (the phase remains free); and its rank1 equality paragraph incorrectly asks Re(conjugate(a)b)=−|a||b|, whereas its own gap with−2Re requires the positive sign. Neither affects the inequality, equality trace structure or normal-square conclusion. Source and review bytes remain unchanged.

Parent displayed the complete119-LF source in the earlier freeze work and all61LF of the clean review now; all live pins match. The reviewer reports full raw packet coverage, verified bindings, no chosen mathematical instance privately/publicly and no scientific executable; parent likewise ran metadata only. Source line41's illustrative stronger-premise remark is unused. [Review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f301-qubit-side-third-disjoint-written/review-v1.md) · [Manifest](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f301-qubit-side-third-disjoint-written/manifest-v1.json). Same-harness only; no eta-region, unrestricted T2/T3/Z2/q3, physical counterexample, human, independent-family, formal/kernel, priority or novelty verification.
