# Written peer review: persistent kernel and open reference region

Before-creation clock observed: **2026-10-23T14:00:23-07:00**. Reviewer: `InfoResearch96h`, completing the explicit legacy review exception before all new primary writes move to the retained info-1 slot. No author files were changed; no scientific program, symbolic engine, point evaluation, model CLI or nested agent was used. This is ordinary in-harness written reconstruction, not blind/cross-vendor/human/formal acceptance.

## Exact snapshot and verdict

Read **all 219 lines**, including the complete untruncated line 211, of `physics/evidence/three-area-20261023-96h/proof-persistent-kernel-and-open-reference-region-v1.md`, SHA-256:

`eed1b651dd9d8f051a090e2332af39be58c8a5bb231f40c7017cc411a0417397`.

Read the complete 294-line original ME4 proof, `proof-GS4-maximally-entangled-reference-v1.md`, SHA-256:

`684ec10f7b7ab25bf0331fdbe9f660ffbfc195c37581addd36d14cf1228debb5`.

Read the explicit separation construction and its qualifications in checkpoint 001, Section 6, SHA-256:

`f9f4cf45de4031459862fb86ad98556fa6dca5607271ecb9d450be53380179e5`.

**Verdict: no substantive mathematical defect found at the declared boundaries. Findings: 0 FATAL / 0 MAJOR / 0 MINOR.** Both PK and the explicit OR sufficient tube reconstruct; the extension to the existing reference-ray/equality interface and the strict nonuniform coverage example are supported as stated. Existing source/novelty/import levels and parent errata remain operative. Unrestricted W4 and the sharp angular boundary are not proved by this review.

## 1. Complex persistent-kernel identity — lines 59–85

For eta=sum eta_i|i>, the identity sum eta_i L_i=A_eta is correct with **unconjugated eta_i**. The bra in L_i already carries the conjugation. Applying the co-Choi sum with input reversal gives

    S_eta(eta tensor z)
      =sum_j |j> tensor [sum_i eta_i L_i] A_eta^(-1)L_j†z
      =sum_j |j> tensor L_j†z.

For C_B, the same contraction is sum_j |j> tensor Lambda_B(|eta><j|)z, which equals the displayed expression by adjoint preservation. Thus PK holds for every nonzero complex eta, without a real-Schmidt-coordinate assumption.

The compression of R_B has least eigenvalue at least ||eta||^2/4: each local R has eigenvalues 1/2 and 3/2. Hence A_eta is invertible even when eta has zero Schmidt coefficients. The ordinary Choi matrix of M_eta is the block Gram matrix of L_i A_eta^(-1/2); it is PSD. Its partial transpose S_eta is Hermitian, not necessarily PSD. C_B is Hermitian as well. For normalized eta, PK therefore implies both D_eta P_eta=0 and P_eta D_eta=0. The projection in the moving-complement argument is the actual orthogonal P_eta.

## 2. Uniform-reference gaps from the original orthogonal blocks — lines 87–117

The normalization eta0=Omega4/2 changes neither M nor S, so the original ME4 blocks apply unchanged.

### Minus sign

- K-perpendicular sectors in the original table have least positive eigenvalue 1/6.
- On the identity sector, subtracting the actual action matrices gives [[0,-1/4],[0,1]], whose eigenvalues are 0,1. The action is self-adjoint in its physical Gram metric; its eigenvalues are intrinsic and not the entries/eigenvalues of an uncorrected quadratic-form matrix.
- On a traceless sector, f_minus has eigenvalue 1. Its other block is

      [[1/6,-sqrt(3)/6,0],
       [-sqrt(3)/6,11/6,2/3],
       [0,2/3,1/3]].

  The original SOS makes this rank-two PSD. Its trace is 7/3. Its three principal 2x2 minors are 2/9,1/18,1/6, summing to 4/9, the product of the two nonzero eigenvalues. Therefore the smaller is at least (4/9)/(7/3)=4/21>1/6.

The identity block has one zero and each of the fifteen traceless blocks one zero. PK supplies a 16-dimensional subspace ran P_eta0 of the kernel, so these dimension counts identify the whole kernel. Consequently D_eta0>=1/6(I-P_eta0) and D_eta0+P_eta0>=I/6.

### Plus sign

- K-perpendicular sectors have least plus eigenvalue 1/3.
- The identity action matrix is [[5/2,-7/4],[-2,3/2]], with trace 4 and determinant 1/4. Positivity follows from the original Gram-corrected form, and its smaller eigenvalue is at least determinant/trace=1/16.
- The traceless f_minus eigenvalue is 1/2. The remaining block is

      [[1/3,sqrt(3)/6,0],
       [sqrt(3)/6,8/3,-2/3],
       [0,-2/3,7/6]].

  Its trace is 25/6 and its determinant is 19/24, by direct expansion. For positive eigenvalues, lambda2 lambda3<=(trace/2)^2, so the least is at least 4(19/24)/(25/6)^2=114/625>1/16.

Thus H_eta0>=I/16 on the entire physical 256-dimensional space. No uncomputed sector or numerical eigenvalue estimate enters either uniform gap.

## 3. Lipschitz constants and the block-norm factor — lines 119–155

For normalized eta,eta0 at distance epsilon, compression/mixed compression of the fixed R_B gives exactly

    ||R_B||=9/4,
    ||A_eta-A_eta0||<=2(9/4)epsilon=9epsilon/2,
    ||A_eta^(-1)||,||A_eta0^(-1)||<=4,
    ||L_i||<=9/4, ||Delta L_i||<=9epsilon/4.

The inverse identity yields ||Delta A^(-1)||<=4(9epsilon/2)4=72epsilon. Splitting a matrix-unit M block into its left-L, inverse and right-L differences gives

    (9/4)^2(4+72+4)epsilon=405epsilon.

This uses the normalized compression norms on every current and base factor. No small-epsilon inverse Neumann approximation is needed.

The co-Choi reversal preserves the maximum **block** norm; it need not preserve the whole operator norm, and the manuscript does not make that false claim. For a 16x16 matrix of output-operator blocks bounded by b, each output row norm is <=b sum_j||x_j||. Cauchy–Schwarz followed by summation over sixteen rows gives total norm <=16b. Hence ||Delta S||<=6480epsilon.

For unit rank-one projectors, expanding |eta><eta|-|eta0><eta0| gives norm <=2epsilon. Tensoring with I_B does not change it. Thus the moving B_eta=D_eta+P_eta has difference norm <=6482epsilon, while H_eta has <=6480epsilon. Both constants are exact hand arithmetic.

## 4. Radius, moving kernel and gaps — lines 157–175

32*6482=207424. Therefore epsilon<1/207424 makes both relevant perturbation errors <1/32. The plus gap is at least 1/16-1/32=1/32. The B gap is at least 1/6-1/32=13/96.

PK and Hermiticity eliminate both off-diagonal blocks of D_eta relative to ran P_eta and its orthogonal complement. B_eta acts as identity on ran P_eta and as D_eta on its complement. Its positive lower bound thus proves D_eta>=13/96(I-P_eta), with kernel **exactly** ran P_eta. The argument does not freeze P_eta0 or treat an unconstrained zero eigenspace as stable under perturbation.

The strict epsilon inequality in fact supplies a little more than the non-strict constants displayed, so the stated weak lower bounds are valid.

## 5. Local unitaries and the W versus bar-W convention — lines 177–189

Let W=U2 tensor U3. Direct covariance gives

    L_i(W eta)=sum_k (W†)_(k i) W L_k(eta) W†,
    A_(W eta)=W A_eta W†,
    M_(W eta)=Ad_W composed M_eta composed Ad_(W†).

Ordinary Choi covariance has bar(W) on its input leg. Taking the **input partial transpose** to obtain the co-Choi matrix reverses that factor to W, yielding

    S_(W eta)=(W tensor W)S_eta(W† tensor W†).

This is the correct displayed convention, not bar(W) tensor W. The same unitary leaves C_B invariant and carries P_eta to P_(W eta). Global phases leave all three operators unchanged.

In a Schmidt basis, the normalized reference distance squared to eta0 is exactly sum_i(sigma_i-1/2)^2. The argument needs only this sufficient representative distance, not a theorem about globally minimizing distance over the local-unitary orbit.

## 6. Explicit nonuniform reference — lines 191–201

For e=1/1000000, v=(1,1,1,1+e) and v0=(1,1,1,1),

    ||v/||v||-v0/2||
      <=| ||v||-2 |/2+||v-v0||/2<=e

by the reverse triangle inequality. Since 1000000>207424, the distance is inside the tube. The four positive Schmidt coefficients are not equal, and normalization cannot remove that inequality. The point is not a local-unitary image of the uniform reference.

## 7. Strict coverage and reference-ray consequence — lines 203–213, complete line 211

The previously established switched-complement bridge uses precisely -C_B<=S_eta<=C_B. The strict/equality interface further uses the plus gap and exact reference minus kernel. Those hypotheses are provided here; their use does not require a partial-trace rank assumption or reinterpret an arbitrary co-Choi negative direction as a rank-two Werner witness. The reference-ray/equality conclusions remain at the earlier bridge's exact dependency level, not a new unrestricted W4 theorem.

I independently checked the modified separation planes. For the range plane, u=|0> tensor eta_e and x=(|100>+|211>+|322>)/sqrt(3). With a nonzero x coefficient and zero u coefficient the Schmidt rank on every cut is three. When both are nonzero, the 1:23 rows comprise the three independent |00>,|11>,|22> components and a row with a nonzero |33> component, so the rank is four. Thus its only 1:23-biseparable ray is u, whose two-site Schmidt coefficients are unequal. For cuts 2:13 and 3:12, any nonzero u coefficient gives four nonzero orthogonal complementary components distinguished by the other diagonal-site label, so the rank is four. The co-range plane is the same argument with the cyclic first-site shift and its GHZ-type y. Consequently no alternative equal-Schmidt biseparable reference appears on another cut or by rotating singular vectors.

The old local support and product-code exclusions persist for exact reasons, not just a continuity assertion. Both planes have full one-site supports. Tr_1 C remains (|11><00|+|22><11|)/3. Tr_2 C and Tr_3 C contain the nonzero sum of |0,j><1,j| terms weighted by the positive sigma_j^2, plus three distinct cyclic first-site matrix units with disjoint supports; hence none of the one-site partial traces vanishes. The planes differ and the partial isometry is nonnormal. Finally, in a locally orthogonal product-code space a 1:23-Schmidt-rank-one vector uses a single code ray and is fully product. The entangled biseparable ray u, and similarly v, cannot lie in that class.

Thus this is a genuine sufficient nonuniform-reference family relative to the explicitly compared equal-Schmidt sector. It is not a worldwide novelty certificate, a sharp tube radius, a generic-two-plane result or an unrestricted Werner witness.

## Review boundary

The review reconstructs the displayed algebra, every stated error constant, gaps, conjugation convention and the explicit strict-coverage argument at the pinned snapshots. It does not authenticate all external paper proofs, formalize the matrices, perform a new finite assay, or certify novelty/clinical/physical significance. Earlier parent arithmetic cells remain scientific spot checks without separate admission records as disclosed in the parent verification erratum; no computation or proof-assistant label is added by this written review.
