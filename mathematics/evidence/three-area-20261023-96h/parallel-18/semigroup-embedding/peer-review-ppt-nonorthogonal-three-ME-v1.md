# v52-D — arbitrary nonorthogonal/dependent at-most-three ME4 conic terms

Reviewer MathSemigroup-2; author PhysicsPPT44. Actual precreation clock: **Sun Oct 25 07:46:16 PDT 2026** (`/bin/date`).

## 1. Verdict and exact reconstructed scope

**FULLY_RECONSTRUCTED_AT_NAMED_LINEAR_ALGEBRA_IMPORTS; 0 FATAL / 0 MAJOR / 0 MINOR findings.** The206LF successor supplies a complete written proof, freshly reconstructed below, that every two-block-positive scalar completion of a conic combination of at most THREE arbitrary normalized ME4 ray projectors is completely copositive. Orthogonality, distinctness, independence and commutation are genuinely absent, not silently retained from the older theorem.

Reconstructed: full-complex Gram iff without inverses/independence; real lambda and the empty/all-zero boundary; actual conic weights rather than eigenvalues; original `U2 U1*` versus reduced `U1* U2` eigenplane; cyclic phase gaps including multiplicities/wraparound; exact principal eigenvalue normalization; full-Gram Rayleigh domination; strict partial-transpose margin; every zero/single/two/three positive-weight case. No load-bearing NEW step in that scope remains NOT_RECONSTRUCTED.

The theorem counts **ME conic TERMS**, not the negative spectral rank of W. It does NOT say at least four negative eigenvalues are necessary for a PPT detector. Non-ME rays, non-scalar completions and operators requiring at least four ME conic terms are not settled. Unrestricted P44 remains open.

This is a genuinely cross-domain mathematics-to-physics SAME-HARNESS supplied-proof reconstruction, not blind discovery, configured-family/cross-vendor/human/formal/kernel/executable/novelty acceptance. No scientific program/interpreter/eval, symbolic program, enumeration, replay, solver, CLI or nested agent was used. Only metadata clocks/hashes and source reads. Parent v9 and earlier errata/HOLD remain binding; no new GO.

## 2. Pins, complete literal coverage and supplied-lead exposure

Read v9 FIRST, complete35LF, then the exact v52-D manifest entry/receipt, including raw recovery of manifest scope LF331. The own-root exposure ACK was written BEFORE opening this proof body OR the parent's lead body. Its clock is actual returned `/bin/date` stdout `Sun Oct 25 07:43:11 PDT 2026`; the metadata call completed as bg_39 and was not rerun.

Actual observed hashes match the manifest/receipt:

- Manifest: `9756dab3ec4803da16e2bba4862bba8b2ff8c2126cfddc3c7c34baec41e8188e`.
- ONLY literal part, `peer-review-wave-v52-v52-D-part1-v1.md`: `d2e59cffee708a2467e13bcbe762ef2e07490a0e6bed42b6716bf20f1d4a3cfc`.
- S1/v9,35LF: `b7c92143cda18c88c7c56017859ab3c7f08fa92ef3d00fd85ba29f41ac258034`.
- S2, `physics/evidence/three-area-20261023-96h/parallel-18/ppt-schmidt44/three-ME-nonorthogonal-consolidated-obstruction-v2.md`,206LF: `06374bdddb31569066a881fbddcea71c1579013f27ac29356308fe4dbece6640`.
- S3, run-root `ppt-three-ME-nonorthogonal-written-lead-v1.md`,38LF: `fa727f533812e42495f54c5f0cbaad9ccb93310934ca6dc219e65e4363e945ae`.
- S4, run-root `ppt-three-ME-depol-faces-parent-v1.md`,46LF: `77681c87105f3a6199b9a76789bb632e8f7c8b732852383e5d77abbb0d8be7fc`.

ALL348 physical LF of the ONLY literal part were read, with actual windows1–170 plus displayed surrounding lines through173, then174–348. This covers EVERY source LF of S1,S2,S3,S4 including all endings; there is no missing part or reader-truncated proof line. Other assignments' manifest bodies are not claimed reviewed.

Exposure is explicit: the parent supplied the proposed closest-eigenphase, principal-Gram and strict-margin chain. Both author and this reviewer are inspecting that supplied chain, not claiming blind rediscovery. I previously reconstructed the orthogonal three-ray packet in v48-A and the two-Bell cyclic packet in v43-B. Their verdicts are NOT transferred: the new nonorthogonal argument is reconstructed afresh below. S4 correctly restricts its older PPT disposition to the ORTHOGONAL class and treats S3 as a separate candidate. Its unrelated depolarizing ENERGY/FACE claims were READ as supplied context but are NOT_RECONSTRUCTED here and are not premises of this PPT theorem.

Named classical imports are finite-dimensional SVD/column-space completion, spectral theorem and unitary diagonalization, the Gram/operator-norm identity, elementary2-by2 Hermitian eigenvalues, the elementary cosine/sum-angle identities, local-unitary invariance of Schmidt rank/PPT, and the Choi characterization of complete copositivity by PSD partial transpose. No historical computation, current-status headline or full external-paper validity is imported. The corresponding Choi/source interfaces were bounded actual reads in my earlier v43-B, not newly formalized here.

## 3. Normalization, conic weights and real-lambda boundary — S2 LF15–47

With the source convention `vec(C)=sum_ij C_ij|ij>`, a unitary U has `||vec(U)||^2=Tr(U*U)=4`. Thus `Phi_U=vec(U)/2` has unit norm and

    <Phi_U,vec(C)>=(1/2)Tr(U* C).

For nonnegative p_r,

    Q=sum_r p_r P(Phi_r)>=0,
    Tr Q=sum_r p_r.

These identities require no orthogonality. In particular Q=0 iff every weight is zero, because its trace is a sum of nonnegative numbers. Repeated or dependent projectors cannot cancel.

The p_r are the coefficients in THIS conic representation. Without orthogonality they are not Q's eigenvalues, and neither rank(Q) nor the number of negative eigenvalues of lambda I-Q is asserted equal to the number of listed terms.

For any normalized product ket x, two-block positivity gives

    0<=<x,W x>=lambda-<x,Qx>,

with `<x,Qx>>=0`. Therefore lambda>=0 even though the family initially permits real lambda. In particular every negative-lambda branch fails without needing an inverse, a nonzero weight, or a product ket outside Q's range.

## 4. Full-complex Gram iff, including dependencies and zero rows — S2 LF49–90

For any rank<=2 complex coefficient matrix C choose a complex4-by2 isometry S containing its column space, and write C=SZ. Lower ranks are included by completing a plane. Conversely every SZ has rank<=2 and `||C||_F^2=||Z||_F^2`.

Writing z_j for column j of Z, define columns

    v_jr=sqrt(p_r)/2 S*U_r e_j,

and V_j with those m columns. Then

    h_r=sqrt(p_r)/2 Tr(U_r* C),
    h=sum_j V_j* z_j.

Crucially, even for nonorthogonal/dependent rays,

    <vec(C),Q vec(C)>=sum_r |h_r|^2.

This follows from the DEFINITION as a sum of positive projectors, not from treating the rays as an orthonormal basis of Q's range.

The linear map L:Z->h has

    (LL*)_(rs)=sum_j v_jr* v_js
       =sqrt(p_rp_s)/4 Tr(U_r* P U_s)=H_rs(P),
    P=SS*.

Thus H is PSD, may be singular, and depends only on P. Its diagonal is

    H_rr=(p_r/4)Tr(U_r*PU_r)=p_r/2,

using cyclicity and Tr(P)=2, not orthogonality of different rays. Its exact squared map norm is lambda_max(H). Hence H<=lambda I_m implies

    ||h||^2<=lambda||Z||_F^2,
    <vec(C),W vec(C)>=0.

For the converse, first use Section3 to get lambda>=0. If Hv=gv for a unit v and g>lambda, choose `z_j=V_jv`. Then

    ||Z||_F^2=v*Hv=g>0,
    h=Hv=gv,
    <vec(C),W vec(C)>=lambda g-g^2=g(lambda-g)<0.

The resulting C is nonzero and rank<=2. Therefore the exact criterion is

    lambda>=0 AND H(P)<=lambda I_m
       for EVERY complex rank-two orthogonal P.

For m=0 the Gram matrix is empty, so the explicit lambda>=0 must remain. With zero weights but m>0, the zero Gram rows/columns are harmless. No inverse of H, division by a weight, or independent-column assumption occurs.

As a normalization/dependence check, if all ray matrices coincide, H is one-half the rank-one matrix `q q*`, where q_r=sqrt(p_r). Its top eigenvalue is `(sum p_r)/2`, not the largest individual p_r/2. Thus the criterion correctly retains correlations rather than replacing conic weights by spectral coefficients.

For a diagonal phase unitary Z=diag(i^j), the overlap above contains `(-i)^j C_jj`, while V_j contains positive i^j before its adjoint. This is the same conjugation checked in the two-Bell precedent; no new Tr(Z C) substitution is made.

## 5. Original versus reduced relative unitary — S2 LF94–110

For p2>0, applying the physical Alice unitary U1* sends each coefficient matrix and each ray matrix to its left product by U1*. The first ray becomes I and the second becomes

    V=U1*U2.

No trace-zero condition follows or is used. Diagonalize V as `V=S0 diag(eta_j)S0*`. The further coefficient transformation

    C -> S0* C S0

is the actual local unitary `S0* tensor S0^T`: with this vec convention `(A tensor B)vec(C)=vec(A C B^T)`. Both factors are unitary, I remains I, and V becomes diagonal. The third ray, when present, remains an arbitrary unitary; it is NOT simultaneously diagonalized. Scalar lambda I is invariant, and all complex coefficient planes are carried bijectively to complex planes.

In ORIGINAL coordinates, the Gram off-diagonal is

    Tr(U1* P_orig U2)=Tr(P_orig U2U1*).

Thus the original eigenplane belongs to `R_orig=U2U1*`, not generally to U1*U2 with the same projector. These matrices are unitarily similar:

    R_orig=U1 V U1*.

For `P_red=U1*P_orig U1`, the same trace becomes `Tr(P_red V)`. Conversely an eigenplane P_red of V gives the correct original plane `P_orig=U1 P_red U1*`. This explicitly verifies the projector orientation, not just equality of the two matrices' spectra.

For local unitaries A,B and W'=(A tensor B)W(A tensor B)*,

    W'^Gamma=(A tensor conjugate(B))W^Gamma
                 (A tensor conjugate(B))*.

Hence the partial-transpose lower scalar margin, when proved after reduction, transfers unchanged to the original operator. No nonunitary local filtering or uncontrolled rescaling is used.

## 6. Closest CYCLIC phase pair, with repeated/wraparound eigenvalues — S2 LF114–138

V is unitary, so it has an orthonormal eigenbasis, counting all four eigenvalues with multiplicity. Choose phases in `[0,2pi)` and order them nondecreasingly. The four nonnegative cyclic gaps are

    theta2-theta1, theta3-theta2, theta4-theta3,
    theta1+2pi-theta4.

Their sum is2pi, so at least one gap d is<=pi/2. The associated indices are DISTINCT: either an adjacent pair or the pair4,1. If eigenvalues repeat, the eigenvectors within the repeated eigenspace can still be chosen orthonormal; a repeated phase gives d=0 and still produces a rank-two projector.

Let P_red project onto the two corresponding eigenvectors. Then

    Tr(P_red V)=eta_i+eta_j,
    |Tr(P_red V)|^2=2+2cos(d)>=2.

For wraparound, the ordinary phase difference is2pi-d and has the same cosine, so the formula is unchanged. For a repeated phase it gives4, not a degenerate rank-one plane. Therefore

    |Tr(P_red V)|>=sqrt2.

This proof does not assume Tr(V)=0, orthogonality of Phi1/Phi2, distinct rays, eigenvalue separation or a real plane. It REPLACES the old trace-zero/six-pair-average mechanism. Arbitrary relative global phase just rotates the eigenvalues and does not invalidate the cyclic gap or modulus.

## 7. Exact principal eigenvalue and full-Gram domination — S2 LF142–163

Order positive conic weights so p1>=p2>=p3>=0. At the actual plane of Section6, the first-two-term principal block is

    G2=[[p1/2, sqrt(p1p2)t/4],
        [sqrt(p1p2)conj(t)/4,p2/2]],
    t=Tr(P_red V).

The larger2-by2 eigenvalue is obtained from

    (a+d)/2 + sqrt((a-d)^2/4+|b|^2),

with a=p1/2,d=p2/2,b=sqrt(p1p2)t/4. Substitution gives EXACTLY

    lambda_max(G2)
      =[p1+p2+sqrt((p1-p2)^2+p1p2|t|^2)]/4.

Thus the normalization has a common1/4 outside the square root expression, not an extra1/2 or a missing phase conjugate. Since |t|^2>=2,

    lambda_max(G2)>=[p1+p2+sqrt(p1^2+p2^2)]/4.

For the FULL possibly singular/nonorthogonal H, extend a unit two-component vector by a zero third component. Its full Rayleigh quotient equals its G2 quotient. Consequently `lambda_max(H)>=lambda_max(G2)` regardless of the third row/column correlations. No claim that H is block diagonal, or that the third correlations have a chosen sign, is needed.

The universal Gram criterion therefore forces

    lambda >= [p1+p2+sqrt(p1^2+p2^2)]/4.           (THRESH)

This is a necessary threshold, not the exact positivity threshold for every triple. It is derived from an actual complex rank-two eigenplane and the full feature Gram matrix, with no simultaneous diagonalization of the third unitary.

## 8. Copositivity certificate and every weight boundary — S2 LF167–192

For ANY unitary U and normalized Phi_U, Bob partial transpose gives

    P(Phi_U)^Gamma=(U tensor I)F_swap(U* tensor I)/4.

The Hermitian swap has eigenvalues +/-1, so it is<=I. Multiplying by nonnegative weights and summing gives, WITHOUT orthogonality,

    Q^Gamma<=(p1+p2+p3)I16/4,
    W^Gamma>=[lambda-(p1+p2+p3)/4]I16.             (SWAP)

Missing weights are zero, not newly introduced positive terms.

**At least two positive weights.** From(THRESH) and(SWAP),

    W^Gamma>=delta I16,
    delta=[sqrt(p1^2+p2^2)-p3]/4.

Here p1>=p2>0 and p3<=p2. Since p1>0,

    p1^2+p2^2>p2^2,
    sqrt(p1^2+p2^2)>p2>=p3,

so delta>0. This includes p3=0, equal positive weights, repeated ray projectors, and all linear dependencies. A singular full H cannot undo the principal-Rayleigh lower bound. For three unit weights, delta=(sqrt2-1)/4 and the threshold is(2+sqrt2)/4 uniformly over arbitrary triples; this need not be sharp when rays coincide.

**Exactly one positive weight.** If p1>0 and p2=0, all other weights vanish. A normalized ME4 ray has four Schmidt coefficients1/2. Keep any two terms and normalize: the resulting Schmidt-rank-two unit vector has squared overlap1/2. Two-block positivity gives lambda>=p1/2. Equation(SWAP) gives

    W^Gamma>=p1 I16/4>0.

No second relative unitary or artificial nonzero weight is needed.

**All weights zero, including m=0.** Then Q=0, W=lambda I. Two-block positivity is exactly lambda>=0, and W^Gamma>=0. Strict positivity is correctly NOT asserted when lambda=0. This handles the sole case where the explicit lambda-real boundary is not forced by a nonzero feature Gram diagonal.

These cases exhaust zero, one, two and three contributing positive weights. No limiting argument, inverse at zero or normalization by a possibly vanishing weight occurs.

Finally, for EVERY PPT density rho,

    Tr(Wrho)=Tr(W^Gamma rho^Gamma)>=0,

and the value is at least delta (or p1/4 in the single-term case) for nonzero Q, because rho^Gamma is PSD of trace1. This is analytic screening of the ENTIRE PPT cone and an explicit positive partial-transpose certificate, not a sampled-state experiment or a selected rational target. The standard Choi interface identifies it as complete copositivity.

## 9. TERMS, not eigenvalues: exact logical boundary — S2 LF196–206

The operative theorem applies whenever Q ADMITS a conic representation by at most three normalized ME4 projector terms. It does not require that the displayed terms form its eigenbasis, and it does not count its negative spectral eigenvalues after subtracting from lambda I.

If an operator is written with four terms but also admits a three-term ME conic representation, it is STILL covered. Conversely four dependent ME terms can live in a smaller linear subspace; the present theorem alone does not reduce that conic representation to its spectral rank. Therefore neither `rank(Q)<=3` nor `negative inertia(W)<=3` is a substitute for the actual representation hypothesis. In particular **no rule requiring at least four negative eigenvalues is proved**.

A possible escape must lack every at-most-three-term ME conic representation under scalar completion, or abandon maximal entanglement or the scalar positive part. Four-or-more-term mechanisms, non-ME rays, anisotropic/non-scalar completions and unrestricted2-positive M4/P44 remain open. No one of those mechanisms is claimed viable. Nonorthogonality ALONE is genuinely closed by this successor; that broadening is not retroactively attributed to the older orthogonal source/review.

## 10. Findings and non-promotions

**0F/0M/0m at the reconstructed scope.** The supplied parent chain is valid at its explicit assumptions; no newly load-bearing statement remains NOT_RECONSTRUCTED. Standard finite-dimensional linear algebra/Choi interfaces are named imports, not formal proof. The unrelated depolarizing claims in S4, historical x1111/21-table/N4 execution facts and complete external-source proofs are NOT_RECONSTRUCTED here and supply no theorem premise.

S1/v9's unadmitted arithmetic, coverage and import corrections remain binding; no later written success retroactively admits them. S3 is an exposed proof lead, not acceptance or independent discovery. S4's earlier written disposition retains its exact orthogonal boundary and supplies no automatic verdict for S2.

This return supports ONLY the new arbitrary-nonorthogonal/dependent at-most-three-ME-TERM scalar-completion theorem and its stated margins. Parent full-body integration and stronger global union/acceptance gates remain separate. No rational PPT/SN3 witness, arbitrary-negative-rank theorem, full P44 solution, configured-family/human/formal/kernel/novelty/publication acceptance or new scientific GO follows.
