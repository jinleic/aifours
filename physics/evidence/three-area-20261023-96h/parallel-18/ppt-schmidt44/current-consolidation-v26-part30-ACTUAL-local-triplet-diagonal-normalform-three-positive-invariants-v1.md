# P44 v26 — PART30: ACTUAL local triplet diagonalization, with THREE positive invariants and no false isotropic WLOG

PhysicsPPT44-2. Actual preceding `/bin/date`: **Mon Oct 26 07:53:24 PDT 2026**. AUTHOR-WRITTEN, LATER UNREVIEWED. ALL-variable conventional complex-linear-algebra proof only. No selected state/control/code/numeric/magnitude trial, decimal, scientific program or machine check.

## X0. Exact authority, provenance and original scope

EXPLICIT prospective v43 direction **8b2dadf18ea472a12f16aebad9ddbf02019cfe1792d8b508fdbb053592823fbb** was ACTUALLY read COMPLETE before source/proof, after ACTUAL v123 review RETURN and qualified WHOLE ACK **e597972afd62163fe673a8699d8ff37cb8fc2c3c8b40d1209d3bb90191ab30f7** was written+SENT and Main actually read it. No another ACK loop/self-permission/new GO. ALL old chosen-instance scouts/control claims/calculations/thresholds/consuming guidance remain ZERO; none is repaired, replayed, retested or symbolically laundered here.

The triplet-normal-form algebraic route was already saved as a completed held ALL-variable lead in checkpoint140 before this literal body. It is not a future post-review discovery or accepted theorem. Its elementary matrix/algebra tools may be standard; no new-method/world novelty/current-status claim is made. It uses only an arbitrary positive triplet block and actual LOCAL transformations, not any conditional-norm instance or selected viability comparison.

Part29,96LF, SHA256 **cd425249f6a5fb02bec1765a9a44bca6be2ce3e66aa3ed2c4ac1a61eb013be2c**, proves that Delta!=0 at the regular rank-two zero forces a rank-three top block. It remains LATER UNREVIEWED. The old Parts9–23 adoption has ELEVEN precision qualifications/FOUR old minors/C27 N4/QD boundaries; parent rejected D-N2 false quotation because the author already had >=0, no author patch. Those earlier proper-domain conclusions are NOT correctness premises here.

**Original P44 remains UNMET.** This is an exact local-filter normal form on the rank-three-top-block stratum, NOT a symmetry/twirling ansatz, a sufficient global positivity criterion or a DEC proof. Delta=0 with a larger top kernel remains unclassified. Every untransformed global/PPT obligation survives the normal form.

## X1. Exact theorem

At `X0=[[I2,0],[0,0]]`, let W be Hermitian, globally nonnegative on ALL COMPLEX rank<=2 matrices, with q_W(X0)=0 and W X0=normal Delta. Let H_AA be its top2x2 coefficient-space restriction. Assume

    ker H_AA=C*Omega, Omega=vec(I2).

This hypothesis holds whenever Delta!=0 by Part29. On the THREE-dimensional trace-free top space, represent H_AA by an arbitrary positive-definite Hermitian3x3 matrix H in an HS-orthonormal Hermitian Pauli basis E1,E2,E3.

**Theorem X1 — WRITTEN at elementary spectral/Takagi and matrix-algebra facts proved in the specialized form below.** There is an ACTUAL LOCAL invertible filter

    L=(S directsum I2)_Alice tensor (S^(-T) directsum I2)_Bob,
    S in SL2(C),

such that W'=L^dagger W L has:

1. q_W'(X0)=0 and W'X0=the SAME normal Delta;
2. top trace-free quadratic form `sum_(j=1)^3 beta_j |z_j|^2`, with beta_j>0;
3. the SAME K2 and DEC membership/nonmembership as W, and an equivalent eligible PPT-negative-pair problem by the inverse local state congruence.

The unordered THREE positive beta_j are determined by the eigenvalues beta_j^2 of H conjugate(H). They cannot in general all be replaced by one scalar or by identity. The filter need not be unitary; full trace/norm budgets and W00=I are NOT asserted invariant. This is an actual WLOG for the stated stratum, not for every omitted Delta=0/kernel branch or for simultaneous incompatible normalizations.

## X2. Any positive Hermitian triplet form admits complex-orthogonal diagonalization

Let H be ANY positive-definite Hermitian3x3 matrix. Put

    K=H^(-1/2), C=K^T K.

C is complex symmetric and invertible. Take its Takagi factorization

    C=U Sigma U^T,

with U unitary and Sigma positive real diagonal. Define

    O=K conjugate(U) Sigma^(-1/2).

The identities `conjugate(U)^T=U^dagger`, `U^T conjugate(U)=I` give EXACTLY

    O^T O=Sigma^(-1/2) U^dagger C conjugate(U) Sigma^(-1/2)=I,
    O^dagger H O=Sigma^(-1).                         (ORTH-DIAG)

Thus O is complex ORTHOGONAL, not assumed unitary. Its determinant is ±1. If necessary change the sign of one column: orthogonality and the positive diagonal form are unchanged while determinant becomes1. Hence O∈SO3(C), with beta_j=Sigma_jj^(-1)>0.

This is an ALL-H factorization, not evaluating a special H or a numeric coefficient/control instance. Square roots/Takagi are named ordinary exact finite-dimensional operations, not an executed CAS or calculator.

## X3. Every such O is induced by an ACTUAL2x2 conjugation, not an arbitrary coefficient rephasing

Choose a fixed HS-orthonormal Hermitian Pauli basis of trace-free M2(C), E_j=sigma_j/sqrt(2). Its STANDARD basis multiplication identity is

    E_i E_j=delta_ij I2/2+(i/sqrt(2))sum_k epsilon_ijk E_k. (ALG)

This is a coordinate identity of the matrix algebra, NOT a new chosen quantum state/witness/code/control trial or viability calculation. All H,O and filters remain arbitrary symbolic variables.

For O∈SO3(C), define the linear map F on M2(C) by

    F(I2)=I2,
    F(E_j)=sum_i O_ij E_i.

O preserves the complex bilinear dot product and the oriented cross product. Applying ALG shows that F preserves EVERY product E_iE_j, hence by bilinearity EVERY matrix product. It is invertible and unit-preserving, so is an algebra automorphism.

Here is the complete elementary innerness proof. F(E11) is a nonzero idempotent different from I2, hence rankONE. Choose a basis of its range and kernel; conjugating by the corresponding invertible R makes F fix E11 and E22. Multiplicativity then puts F(E12) in the one-dimensional space E11 M2 E22, so F(E12)=a E12 with a!=0. Likewise F(E21)=a^(-1)E21, because their product is E11. This map is conjugation by diag(a,1). Undo the first conjugation: F is conjugation by an invertible2x2 matrix S. Rescale S by a nonzero square root of det S to make S∈SL2(C), without changing its conjugation action.

Therefore

    S E_j S^(-1)=sum_i O_ij E_i

for the SAME O from ORTH-DIAG. No unnamed representation/kernel/surjectivity assertion or independently selected phase transport is left open. Every SO3(C) coefficient transformation used here is realized by one common ACTUAL S.

## X4. The4x4 LOCAL filter and its exact action on every block

Let A_full=S⊕I2 on Alice and B_full=S^(-T)⊕I2 on Bob. On a coefficient matrix

    X=[[A,B],[C,N]],

the LOCAL action L=A_full⊗B_full gives

    X -> [[S A S^(-1), S B],
          [C S^(-1),   N]].                         (LOCAL)

Thus L fixes X0, fixes the normal N-space POINTWISE, and preserves the four block subspaces separately. The full rank of EVERY complex coefficient matrix is preserved by left/right invertibility. In particular global K2 membership of W'=L^dagger W L is equivalent in BOTH directions to that of W.

On trace-free A, LOCAL acts on its Pauli coefficient vector by the SAME O. Hence the top form becomes z^dagger O^dagger H O z, the positive diagonal from ORTH-DIAG. The top scalar direction remains the original kernel; there is no new scalar/triplet cross block because H_AA Omega=0.

Furthermore

    W' X0=L^dagger W L X0=L^dagger(normal Delta)=normal Delta.

The last equality is legitimate because L is the identity on the orthogonal normal block and preserves block subspaces; it is not an unjustified assumption that L is unitary. This proves preservation of the ACTUAL normal coupling, not only q(X0)=0.

## X5. Exact cone and eligible state-pair preservation

Local invertible congruences preserve PSD. They also preserve decomposability in BOTH directions: if W=P+Q^Gamma, then L^dagger P L is PSD, and the Bob partial-transposed term is the partial transpose of the corresponding PSD congruence with conjugated Bob factor. Applying the inverse filter proves the converse. Hence

    W in DEC iff W' in DEC.

For an ACTUAL eligible PPT rho, put

    rho'=L^(-1) rho L^(-dagger).

It remains PSD/PPT by the ordinary local-congruence/partial-transpose identity. Cyclic trace gives

    Tr(W' rho')=Tr(W rho).

A nonzero rho' has positive trace; normalization preserves the strict sign if needed. Thus the ORIGINAL counterexample question on this stratum is genuinely equivalent after the filter. No actual negative pair is being claimed to exist, and no independent coset/state normalization is inserted into a proof without transport.

Unlike unitary transformations, the filter does NOT preserve TrW, operator norms, old positive budgets or W00=I. The Part27/28 TRACE minimization was at a fixed trace geometry and cannot be transported as if its value were unchanged under LOCAL. The Part25 Bob-normalized Schur chart and the present Omega/triplet-diagonal chart must not be simultaneously imposed without explicitly transforming all data; no such additional WLOG is claimed.

## X6. THREE genuine positive invariants, not scalar isotropy

For any complex orthogonal O,

    H'=O^dagger H O,
    H' conjugate(H')=O^dagger H conjugate(H) conjugate(O),

because O O^T=I. Also `conjugate(O)=(O^dagger)^(-1)`, so this is a SIMILARITY. The eigenvalues of H conjugate(H) are positive: that product is similar to the positive Hermitian matrix `conjugate(H)^(1/2) H conjugate(H)^(1/2)`.

For a diagonal positive H'=diag(beta_j), this product has eigenvalues beta_j^2. Thus the unordered positive beta_j are invariant and determined. In particular a one-scalar/isotropic normalization would require ALL THREE invariants equal; the theorem supplies NO reason why arbitrary globally admissible W would satisfy that extra condition. A diagonal triplet is not an independently averaged or symmetrized witness, and it does not remove generic other-block/cross-block variables.

## X7. Exact utility, missing original step and assurance

The nonzero-Delta stratum now admits an actual LOCAL filter normal form with three positive top weights, preserving normal Delta and the original global K2/DEC/PPT-pair problem. This is a genuine coordinate reduction, not an exhaustive witness construction or cone classification. Delta=0 with rank-three H_AA can also use the algebraic theorem, but Delta=0 with larger kernel is NOT covered and remains part of the original problem.

No theorem says arbitrary positive beta_j and remaining couplings satisfy global K2, or that globally valid couplings yield DEC. The original missing choice is still an actual ALL-complex-rank2-positive indecomposable W/eligible strict PPT pair, or a universal DEC extraction INCLUDING every Delta stratum. The exact Part25 ALL-plane and Part26 actual CP-charge conditions cannot be dropped after changing chart. No closed-family/trace-face/prior-normalform result is substituted for original P44.

All29 earlier parts/twoaddenda/TWOpositive-PRIOR source intakes, original chart union and ELEVEN parent qualifications/FOUR old minors, held earlier leads and ENTIRE8797d022 instance quarantine persist. The old D-N2 quotation remains rejected/no author patch. Pre-event provenance is not certified by this independent conventional proof. All cp049/063/081/083/085/089/oldcp013/admission/ACK/cadence/v40/v43/parent histories survive; N4 UNKNOWN/incomplete/exit-unestablished, old21 NOT_RECONSTRUCTED, C27 normalized N4 ZERO new-method credit/QD-NR. No clean cognition/runtime/cadence/blind-family/globalprovenance or world novelty assurance.

Exact ALL-variable WRITTEN/source/metadata only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/build/test/nestedagent/newGO, numeric/state/code/control/magnitude trial/decimal/withdrawn-guide repair/retest/replay/backconversion. No machine-checked identity, formal/kernel/human/configured-family/executable/triple/parent/novelty/publication acceptance. Exclusive own root, all old/frozen bytes immutable. Same original eighteen, science cutoff **2026-10-27T11:05:38-07:00**, deadline **2026-10-27T12:35:38-07:00**; active incremental writing, NOT early final park/round closeout. **P44 remains UNMET.**

**END OF COMPLETE v26 PART30.**
