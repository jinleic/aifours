# v55-A — fixed four-Weyl projection: exhaustive range rank, exact PPT spectrum and scalar no-go

Reviewer MathSemigroup-2; author PhysicsPPT44. Actual precreation clock: **Sun Oct 25 08:25:42 PDT 2026** (`/bin/date`).

## 1. Verdict and exact scope

**FULLY_RECONSTRUCTED_AT_NAMED_LINEAR_ALGEBRA_IMPORTS; 0 FATAL / 0 MAJOR / 0 MINOR findings.** This fresh written reconstruction covers ALL the new load-bearing statements for the FIXED projection Q onto the normalized I,Z,X,ZX rays:

- the full-complex rank-two Gram iff and the correct adjoint/phase convention;
- every endpoint case in the cyclic-bidiagonal kernel proof, including both adjacency orientations, and consequently rank>=3 for every nonzero range matrix;
- compactness giving eta<1 and existential non-PSD two-block-positive scalar completions, without an evaluated eta or a displayed valid rational lambda;
- every entry of the eight partial-transpose2-by2 blocks, their exhaustive invariant-sector decomposition and exact multiplicities;
- the stated nonnegative-t PPT interval, endpoint t0, attained ALL-PPT overlap alphaP, and its exact multiplication identity;
- rational rho4 and each PPT Gram block, expectation -1/40, followed by the ACTUAL rank-two rejection with expectation -7/30;
- the strictly positive copositivity margin for EVERY two-block-positive scalar completion of THIS Q.

No load-bearing NEW step at that scope remains NOT_RECONSTRUCTED. This is same-harness mathematics-to-physics supplied-proof WRITTEN support, not blind/cross-vendor/configured-family/human/formal/kernel/executable/novelty acceptance. It does not classify arbitrary four-ME subspaces, four weights, four nonorthogonal terms, non-ME rays, anisotropic positive parts or unrestricted P44. In particular the failed W_trial is NOT an SN3 certificate; the present argument does not determine the actual Schmidt number of rho4 by a different method either.

No scientific interpreter/eval/program, symbolic calculation program, enumeration, replay, solver, table execution, CLI or nested agent. All calculations below are WRITTEN. Only source reads and metadata clocks/hashes. HOLD/v9 remains binding.

## 2. Pins, coverage, serial settlement and exposure

The earlier primary was safely frozen as `semigroup-embedding-consolidated-v2.md` with `park-v4.json` BEFORE starting this review; no unfinished primary write overlapped. Mandatory v9 was read before the proof; the exact v55-A entry, raw full scope LF36 and byte-equality receipt were read. Own-root `peer-review-ppt-four-Weyl-ack-v1.json` was written BEFORE opening the mathematical body.

Observed metadata pins match the frozen entry/receipt:

- Manifest: `57933f7f691423a04fed91fdc6ec171a8738e9bd5f4d6dd753bc5189c8c6cf9d`.
- ONLY literal part `peer-review-wave-v55-v55-A-part1-v1.md`: `3c74082243c9dc040650021e88176a4d005b84637fcc2f2d706533fd8fea06c3`.
- S2, `physics/evidence/three-area-20261023-96h/parallel-18/ppt-schmidt44/four-Weyl-rectangle-consolidated-obstruction-v1.md`,232LF: `eb1ed1c5aba2bb444a817b48a39ff3d7206c1aacc65421cca7073cffe64a5e02`.

ALL280 physical packet lines were read. Actual windows1–175 plus displayed context through178, then179–280 cover EVERY LF of S1/v9 and S2, including both endings. No reader-truncated proof line remains. Original S2 line numbers are used below. The complete25LF interface freeze was additionally read; its informal pre-freeze reasoning is disclosed and is not preregistration.

I previously reconstructed the at-most-three arbitrary-ME TERM result in v52-D. It does not cover this four-dimensional range or its exact spectrum, and its verdict is not transferred. Before ACK only the parent's proposed four-ray claims were known; the current proof body had not been read.

Named classical imports: finite-dimensional SVD/rank-Schmidt equivalence, Hermitian spectral/Gram norm facts, positive-projector identities, elementary2-by2 eigenvalues/PSD Gram facts, compactness in finite-dimensional complex matrix space, rational density and the Choi/copositivity interface. The bounded Hou2015/0908.1846v2 interfaces were actually read during the earlier v43-B review; no whole-paper/new-SOTA audit is claimed here. The present calculations do not borrow a sufficient spectral test as a universal criterion.

## 3. Literal geometry and universal COMPLEX Gram iff — S2 LF19–69

Use `vec(C)=sum C_rs|r,s>`, indices modulo4, zeta=i, Z e_j=i^j e_j and X e_j=e_(j+1). A4-by4 unitary has Frobenius norm2, so Phi_U=vec(U)/2 is normalized.

The four U are mutually Hilbert–Schmidt orthogonal: traces of X,ZX,Z*X vanish by their nonzero shift; Tr Z=0; and `Tr(X*ZX)` equals Tr Z by cyclicity. Thus Q is an orthogonal projection of rank4 and trace4. A conic sum of at most three rank-one projectors has range in the span of at most three kets, so THIS Q cannot admit the earlier <=3-term representation, even allowing dependence/nonorthogonality. For0<=lambda<1, W_lambda has four negative eigenvalues. This is a literal fixed-family fact, not a universal lower bound on a detector's negative inertia.

For a rank<=2 coefficient matrix C choose ANY complex4-by2 isometry S spanning its columns and write C=SZ. Let z_j be columns of Z and V_j have columns `(1/2)S*U_a e_j`. Then

    h_a=(1/2)Tr(U_a* C),
    h=sum_j V_j* z_j,
    ||C||_F^2=||Z||_F^2,
    sum_j V_j*V_j=H(P),
    H_ab(P)=Tr(U_a* P U_b)/4, P=SS*.

The squared negative energy is ||h||^2. The linear map Z->h has squared norm lambda_max(H), so H<=lambda I4 implies nonnegative expectation for every Z. Conversely if Hv=gv with ||v||=1 and g>lambda>=0, choose z_j=V_jv. Then `||Z||^2=g`, h=gv and expectation is `g(lambda-g)<0` on a nonzero rank<=2 C. This proves the iff over EVERY complex two-plane, including lower-rank C by completion, not a real-grid surrogate.

The adjoint is essential: the Z overlap contains `sum (-i)^j C_jj/2`, not positive i^j; the corresponding Gram upper I/Z entry is `Tr(PZ)/4`, with its conjugate below. On P=diag(1,1,0,0), the principal I/Z block is

    [[1/2,(1+i)/4],[(1-i)/4,1/2]].

Its largest eigenvalue is `(2+sqrt2)/4=lambda0`. Embedding its Rayleigh vector by two zeros into the FULL four-feature matrix gives lambda>=lambda0. No assertion that the X/ZX correlations vanish or that this is the exact global threshold is needed.

## 4. Exhaustive cyclic-bidiagonal rank proof over C — S2 LF73–92

For C in the stated range write

    C=alpha I+beta Z+gamma X+delta ZX,
    A_r=alpha+beta i^r,
    B_r=gamma+delta i^r.

Because ZX has row phase i^r, the row-r kernel equation is exactly

    A_r v_r+B_r v_(r-1)=0.                         (REC)

No row/column transpose or XZ phase has been silently substituted. A nonzero affine polynomial in z has at most one zero among the four distinct fourth roots.

**A identically zero.** Then alpha=beta=0 and C=diag(B_r)X. Nonzero C means B is not identically zero, so at least three B_r are nonzero. X is invertible, hence rank(C)>=3. This includes constant/nonvanishing B and its one-root case.

**B identically zero.** The dual diagonal case gives rank(C)>=3. Both lists identically zero would imply C=0 and is excluded.

Henceforth neither list is identically zero and each has at most one zero.

**At least one list has no zero.** If every A_r is nonzero, solve(REC) cyclically forward for v_r from v_(r-1). All four values depend on one initial value; the closing equation may kill it, never add freedom. A zero B merely forces a zero along this recurrence. If every B_r is nonzero, solve cyclically backward instead. Thus nullity<=1 in every such case. In particular if exactly one of the lists has one zero and the other has none, that zero equation propagates to all variables and yields the stronger nullity0, but the proof only needs the stated upper bound.

**Both unique zeros at the SAME index r.** Row r vanishes. The other three rows have both coefficients nonzero and form a single three-edge path through all four unknowns. Starting at one endpoint determines every component with no remaining closing constraint. There is exactly one free scalar, so nullity1.

**Unique A-zero r and B-zero s with r!=s.** Row r forces v_(r-1)=0; row s forces v_s=0. Remove these two cycle edges. All remaining links have nonzero coefficients. The path from s forward through r-1 is anchored to zero and hence identically zero. The complementary path from r through s-1 has one free scalar propagated by its nonzero links. This includes EVERY separation:

- s=r-1: both anchors are the same single vertex; the other three-vertex path has one free scalar;
- s=r+1: the unanchored path is the single vertex r; the three-vertex anchored path is zero;
- the opposite case: each path has two vertices, one zero and one with one free scalar.

Thus again nullity<=1. These cases exhaust both affine lists over the full complex field. Every nonzero C has rank>=3; no real-coefficient or generic-nonzero hypothesis was needed.

## 5. Compactness headroom is existential only — S2 LF94–100

The set K of unit-Frobenius matrices of rank<=2 is closed (all3-by3 minors vanish) and bounded in finite-dimensional complex matrix space, hence compact. The continuous quadratic form `<psi,Qpsi>` attains a maximum eta on K. Since Q is an orthogonal projection, it is<=1. Equality at a unit vector would give `(I-Q)psi=0`, placing that rank<=2 vector in Ran(Q), contrary to Section4. Hence eta<1.

By definition every lambda>=eta gives two-block positivity. Rational density supplies some rational lambda in(eta,1), for which W_lambda is non-PSD because its four range eigenvalues are lambda-1<0. This proves actual EXISTENCE of non-PSD two-block-positive completions, but gives neither an evaluated eta nor a displayed certified rational lambda. In particular it does not certify lambda=3/5. Complete copositivity later is consistent with this headroom: copositive witnesses can detect NPT states but not the PPT targets sought here.

## 6. Derivation of ALL eight partial-transpose blocks — S2 LF104–140

Let T=Q^Gamma, Gamma on Bob, and F_swap the swap. For U_pq=Z^p X^q,

    U_pq*=X^(-q)Z^(-p).

Apply the normalized-ME formula `(U tensor I)F_swap(U* tensor I)/4` to |r,s>. The first U* contributes `i^(-pr)|r-q>`, swap gives `|s,r-q>`, and the final U contributes `i^(p(s+q))|s+q,r-q>`. Summing p,q in{0,1} yields EXACTLY

    4T|r,s>=(1+i^(s-r))|s,r>
               +(1+i^(s-r+1))|s+1,r-1>.           (ACT)

In particular the +1 phase in the second term is present.

The total tau=r+s modulo4 is invariant. Set `v_r^(tau)=|r,tau-r>`. Then

    4T v_r=(1+i^(tau-2r))v_(tau-r)
              +(1+i^(tau-2r+1))v_(tau-r+1).

Here is the complete action on the SIXTEEN basis vectors, obtained by the four powers of i; v indices are in the indicated sector:

| tau | 4Tv0 | 4Tv1 | 4Tv2 | 4Tv3 |
|---|---|---|---|---|
|0|2v0+(1+i)v1|(1-i)v0|2v2+(1+i)v3|(1-i)v2|
|1|(1+i)v1|(1-i)v0+2v1|(1+i)v3|(1-i)v2+2v3|
|2|(1-i)v3|2v1+(1+i)v2|(1-i)v1|(1+i)v0+2v3|
|3|2v0+(1-i)v3|(1+i)v2|(1-i)v1+2v2|(1+i)v0|

This action proves, rather than assumes, the following blocks. Diagonal pairs and upper-right entries in the next table are unscaled; divide each whole block by4 and use the conjugate lower-left.

| tau | ordered pair | diagonals | upper-right |
|---|---|---|---|
|0|(0,1)|(2,0)|1-i|
|0|(2,3)|(2,0)|1-i|
|1|(0,1)|(0,2)|1-i|
|1|(2,3)|(0,2)|1-i|
|2|(0,3)|(0,2)|1+i|
|2|(1,2)|(2,0)|1-i|
|3|(0,3)|(2,0)|1+i|
|3|(1,2)|(0,2)|1-i|

Every computational ket occurs exactly once because each tau sector is a disjoint four-ket set, and each listed sector is partitioned into two pairs. Formula(ACT) forbids cross-sector entries, and the sixteen displayed images forbid every unlisted same-sector entry. Thus this is an exhaustive16-by16 matrix-element reconstruction, not verification of a copied spectrum alone.

Each unscaled block has trace2 and determinant `2*0-|1+i|^2=-2`, so its characteristic polynomial is x^2-2x-2 and eigenvalues are1+sqrt3,1-sqrt3. Consequently

    alphaP=(1+sqrt3)/4, multiplicity8,
    betaP=(1-sqrt3)/4, multiplicity8.

All signs/conjugations agree with Hermiticity in the action table. The trace is4, consistent with Tr(Q), but that consistency is not used instead of the full entry calculation.

## 7. rho_t: exact PPT interval and attained all-PPT overlap — S2 LF185–210

For the STATED t>=0 family,

    rho_t=(I+tQ)/(16+4t),

positivity and normalization follow from Q^2=Q, TrQ=4: numerator eigenvalues are1+t on Ran(Q) and1 on its complement. Partial-transpose numerator eigenvalues are1+t alphaP and1+t betaP. Since alphaP>0 and betaP<0, PPT is equivalent to

    0<=t<=t0=-1/betaP
               =4/(sqrt3-1)=2(1+sqrt3).

No claim about a negative-t extension is needed. At t0 the lower eigenvalue is exactly zero; at t>t0 it is negative.

For any PPT density rho, rho^Gamma is PSD of trace1, hence

    Tr(Qrho)=Tr(T rho^Gamma)<=alphaP.

The displayed family attains this ALL-PPT bound. Its overlap is

    Tr(Qrho_t)=(4+4t)/(16+4t)=(1+t)/(4+t).

At t0 its numerator/denominator become3+2sqrt3 and6+2sqrt3. The exact identity is

    [(1+sqrt3)/4]*(6+2sqrt3)
       =(6+8sqrt3+6)/4=3+2sqrt3.

Thus the overlap equals alphaP, proving the exact maximum over ALL PPT densities, not only the family rho_t. The saturating rho_t0 is algebraic, not claimed Gaussian-rational.

Accordingly W_lambda is nonnegative on every PPT state iff lambda>=alphaP. For lambda<alphaP, rho_t0 is a genuine negative PPT direction. For rational lambda<alphaP, continuity near t0 and density of rationals provide a rational t<t0 sufficiently close to keep the expectation negative, hence a Gaussian-rational PPT target. This is an existence argument without sampling; Section8 supplies one actual rational example.

## 8. Actual rho4 and its per-block Gram certificate; rejected trial — S2 LF144–181

Since Q has Gaussian-rational entries with denominator4, `rho4=(I+4Q)/32` has Gaussian-rational entries with denominator dividing32. It has eigenvalues5/32 on the four-dimensional range and1/32 on its twelve-dimensional complement, so is positive definite with trace1. Each ME projector reduces to I4/4; therefore Q reduces to I4 and rho4 reduces to `(4I4+4I4)/32=I4/4` on either party. Both local supports are all4 dimensions.

Each partial-transpose block of I+4T is one of

    [[3,u],[conj(u),1]]
       =P((u,1))+P((1,0)),
    [[1,u],[conj(u),3]]
       =P((1,conj(u)))+P((0,1)),

where u=1+i or1-i. These identities follow because |u|^2=2; the off-diagonal in the second identity is u, not conj(u). The two kets in each block are independent, so every block is positive definite. The eight block supports exhaust the physical16-space by Section6; their sum is a full exact Gaussian-integer Gram certificate of PPT after division by32. It is not a Schmidt decomposition of rho4 and does not prove its Schmidt number at most two.

Using Q^2=Q,

    Tr(Qrho4)=(4+4*4)/32=5/8,
    Tr(W_(3/5)rho4)=3/5-5/8=-1/40.

This is an actual negative candidate pair, not a hypothetical target. However C0=diag(1,1+i,0,0)/sqrt3 has unit Frobenius norm and rank exactly2. Its I and Z overlaps are

    (2+i)/(2sqrt3), (2-i)/(2sqrt3),

with squared moduli5/12 each. Both shifted unitaries X and ZX have zero diagonal, so their adjoint traces against diagonal C0 vanish. Therefore

    <vec(C0),Q vec(C0)>=5/6,
    <vec(C0),W_(3/5)vec(C0)>=3/5-5/6=-7/30.

Thus W_trial is NOT two-block-positive, regardless of the valid PPT negative expectation. No SN3 claim follows, and ordinary block positivity is not asserted either. Failure of this candidate does not classify rho4 against other possible witnesses.

## 9. Entire fixed scalar-completion no-go and why older bounds do not suffice — S2 LF212–230

Every two-block-positive W_lambda satisfies the actual plane bound lambda>=lambda0. The EXACT spectrum in Section6 gives T<=alphaP I. Thus

    W_lambda^Gamma=lambda I-T
       >=(lambda0-alphaP)I
       =[(1+sqrt2-sqrt3)/4]I>0.

Both 1+sqrt2 and sqrt3 are positive, and `(1+sqrt2)^2=3+2sqrt2>3`, so the final sign is strictly positive without numerical evaluation. This proves complete copositivity for EVERY universally rank-two-nonnegative lambda in this one fixed family, including the existential non-PSD region from Section5. It rules out PPT detection across the whole family, not merely the failed3/5 value.

The old generic swap bound for four unit-weight rays is only T<=I, while lambda0<1 since sqrt2<2. Those two old bounds alone do not yield the positive margin. The supported at-most-three-term theorem cannot apply because rank(Q)=4. The new exact spectrum is decisive for the no-go. The range-rank/compactness proof independently establishes that the family has genuine non-PSD two-block-positive headroom; it is not a surrogate spectral or sampling proof of the margin.

## 10. Findings and exact nonclaims

**0F/0M/0m at the reconstructed scope.** No newly load-bearing endpoint, rank, Gram, spectrum, PPT-boundary, rational-target or scalar-completion step remains NOT_RECONSTRUCTED. The standard compactness/linear-algebra/Choi interfaces remain named classical imports, not formal certification. Historical computational files, old finite certificates and the complete external-paper proofs are NOT_RECONSTRUCTED here and are not premises.

For the literal four negative ME eigenrays at0<=lambda<1, each squared2-Schmidt norm is1/2, giving total2, not<1. Thus the cited STRICT sufficient spectral theorem is inapplicable; it provides no positivity or indecomposability certificate. The new Gram iff, exact partial-transpose blocks and explicit rank-two test were instead derived directly.

This return supports only the FIXED unweighted Q={I,Z,X,ZX} and its one-parameter scalar completion. It does not support arbitrary four-ME subspaces, arbitrary four weights, four nonorthogonal ME terms, non-ME rays, anisotropic/non-scalar positive completions of this same range, arbitrary2-positive M4 maps, an SN3 classification of rho4, or unrestricted P44. No evaluated eta, explicit certified non-PSD two-positive rational lambda, optimizer algorithm, scientific GO, configured-family/human/formal/kernel/novelty/publication acceptance is supplied. Parent full-body integration remains separate.
