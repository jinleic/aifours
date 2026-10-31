# T2 for every separately 2+2-reducing traceless pair

**Disposition: same-harness WRITTEN adoption of the full arbitrary-block-trace theorem in f285.** Native clock before composition: 2026-10-30T03:25:44-0700 PDT. Review: **0F/0M/3m**, no load-bearing proof repair; historical class labels and a uniform-margin reading are not adopted.

For every complex traceless A,B in M4, each separately unitarily similar to a direct sum of two arbitrary2x2 blocks, put X=A tensor I4+I4 tensor B and L=||A||_F²+||B||_F². Then **sigma1(X)²+sigma2(X)²<=2L**. The reducing bases need not coincide; individual blocks need not be traceless or normal. This is not the unrestricted traceless-pair theorem.

## Written reconstruction

The key lemma, for arbitrary complex t and traceless C,D in M2, is

||tI4+C tensor I2+I2 tensor D||_op² <=4|t|²+||C||_F²+2||D||_F²,

and also the leg-swapped bound. For arbitrary unit u,v with coefficient matrices U,V, put s=Tr(U*V), M=VU*, N=V^T conjugate(U). Both traces equal s and N=(U*V)^T. Weighted Frobenius Cauchy charges the scalar/C/D coordinates by4/1/2; its dual factor is x+y/2−|s|²/2, where x=||VU*||² and y=||U*V||². Schmidt-reduce U=diag(a,b), a,b>=0, a²+b²=1, and leave every entry of V free subject to unit norm. Direct expansion gives x+y=1+|s|²−|bp+aw|² and x<=1. The dual factor is therefore (1+x−|bp+aw|²)/2<=1. Taking the full unit-vector supremum proves the lemma; no arbitrary-T4x2 claim is used.

Write A=(alpha I+C1) direct-sum (−alpha I+C2), B=(beta I+D1) direct-sum (−beta I+D2), with all C,D traceless. Then L=4(|alpha|²+|beta|²)+sum||C||²+sum||D||² and X has four orthogonal sectors X_rs=(epsilon_r alpha+epsilon_s beta)I4+C_r tensor I2+I2 tensor D_s.

- **Same sector:** the top two selected squares are at most its total Frobenius norm squared, 4|epsilon_r alpha+epsilon_s beta|²+2||C_r||²+2||D_s||²<=2L.
- **Opposite row and column:** operator triangle gives each sector norm <=a_r+b_s; (a+b)²<=2a²+2b² and operator norm<=Frobenius norm exhaust both blocks of both factors.
- **Same row:** apply the weighted lemma twice, keeping coefficient1 on the repeated C_r. The complex parallelogram identity sums the scalar charges to8(|alpha|²+|beta|²); the D blocks are each charged2, yielding<=2L. Same column uses the swapped lemma.

These exhaust every placement of two singular values, including ties, zeros and multiplicities. Simultaneous equality in separate sector bounds is never assumed. Parent reconstructed the weighted identity, global trace accounting, shared-row charge and sector exhaustion in writing.

## Strictness and structural example

The theorem is pointwise strict if all four traceless C1,C2,D1,D2 are nonzero and all four original2x2 blocks have rank2: shared-row/column/same-sector bounds have positive unused-block slack; opposite-sector bounds have positive second-singular-value slack. No uniform positive numerical margin over this open class is proved. The source's same-sector slack is an exact identity for its Frobenius bound; calling it “at least” is harmless.

The symbolic family A=(alpha I+cE12) direct-sum (−alpha I), B=(beta I+dE12) direct-sum (−beta I), alpha c beta d!=0, is included. Both are invertible with nontrivial Jordan blocks and both squares are nonnormal. An invertible weighted partial permutation is a weighted permutation; each cycle has characteristic polynomial z^k−w with w!=0 and is diagonalizable, so this family is not similar to such a matrix. These intrinsic structural facts are adopted. They do not establish exclusion from the optimized f274 eta-certificate region; later owner overlap diagnostics are unreviewed, separate inputs and not incorporated here.

## Evidence and ceiling

Parent displayed the complete132-line source and complete returned review, and verified the live source binding. Reviewer independently rehashed the packet/source, sent its pre-body ACK and displayed the full packet in seven<=20-line raw windows, then supplied the full written derivation. No scientific executable was run by parent or reviewer. Optional illustrative remarks in the review are not premises of the all-variable proof above. [Review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f285-werner-arbitrary-2plus2/review-v1.md) · [Frozen manifest](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f285-werner-arbitrary-2plus2/manifest-v1.json) · [Literal freeze](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f285-werner-arbitrary-2plus2/freeze-receipt-v1.json).

No global equality classification, claim for every both-squares-nonnormal pair, eta>2L witness, f274-region enlargement, unrestricted T2/T3/Z2/q3 result, human/independent-family/formal/kernel or novelty verification. The false f198 lemma and every historical quarantine remain unchanged.
