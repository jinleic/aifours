# v48-A — universal complex Gram criterion and complete copositivity of the weighted three-ME scalar family

Reviewer MathSemigroup-2; author PhysicsPPT44. Actual precreation clock: **Sun Oct 25 07:07:50 PDT 2026** (`/bin/date`).

## 1. Verdict and exact scope

**FULLY_RECONSTRUCTED_AT_NAMED_LINEAR_ALGEBRA_IMPORTS; 0 FATAL / 0 MAJOR / 0 MINOR findings.** The new written proof supports:

1. The exact criterion `H(S)<=lambda I_m` for EVERY complex4-by2 isometry S, with the stated normalized rays, correct adjoints/phase conjugation, rank<=2 quantifier and all zero weights.
2. The analytic ALL-PPT screen `Tr(Q_p rho)<=sum(p_r)/4`, not a selected or sampled target test.
3. Every two-block-positive scalar completion of at most THREE mutually orthogonal ME4 rays with arbitrary nonnegative weights is COMPLETELY COPOSITIVE. For nonzero Q_p the proof gives a strictly positive partial-transpose margin; the all-zero case is treated separately and needs only nonnegativity.
4. For literal I,Z,X, the specified plane gives the necessary lower bound `(2+sqrt2)/4`, every PPT overlap is at most3/4, and the explicit rational rank-two control gives5/6 with the correct normalization.

No load-bearing NEW identity in this scope remains NOT_RECONSTRUCTED. This is a genuinely mathematics-to-physics same-harness supplied-proof reconstruction, not blind/cross-vendor/configured dual-family/human/formal/kernel/executable/novelty acceptance. It closes only the stated scalar-completion mechanism, not arbitrary three-negative witnesses or unrestricted P44.

No scientific interpreter/eval/program, enumeration, symbolic computation, solver, replay, table execution, CLI or nested agent was used. All calculations below are WRITTEN derivations. Only source reads and metadata clocks/hashes were used. HOLD/v8 and the unchanged deadline/cutoff remain binding.

## 2. Frozen input, complete coverage and exposure

Parent v8 was read FIRST, all37LF. Then exact v48-A entry and packet receipt were read, including raw recovery of the truncated manifest scope LF40. The own-root ACK `peer-review-ppt-three-ME-scalar-ack-v1.json` was written BEFORE opening any current proof-body line.

Actual observed metadata pins:

- v48 manifest: `9d51b70b4be5cfdbe3952980904e5925907056303494eb70e0b0f244f199add3`.
- Mandatory literal packet `peer-review-wave-v48-ppt-three-ME-scalar-sources-v1.md`: `cd45b3f0301f0a9dc4af1b4c1de45e8661baaf8958222d419ee5a3c4874d7504`.
- Sole source S, `physics/evidence/three-area-20261023-96h/parallel-18/ppt-schmidt44/three-ME-scalar-consolidated-obstruction-v1.md`: `741f24d87c9aa713ccc5c8725da04e151d04e9bff2988fb2be52935027b6d764`.

The entire literal packet LF1–234 was read, including EVERY original source LF1–227. Actual windows1–145 plus displayed context through148, then149–234 cover all lines; no cut mathematical line remains. Original source LF numbers are used below. The complete37LF source/Gram freeze was also read. Its disclosed informal pre-freeze reasoning is not relabeled preregistration.

Prior exposure: I reconstructed the preceding two-Bell cyclic family in v43-B. Its phase convention is compared explicitly below, but no previous verdict is transferred to this new theorem. The present body was not read before ACK; only the parent/manifest proposed result was known.

Named classical imports: finite-dimensional SVD/column-space completion, spectral theorem and operator-norm/Gram identities,2-by2 Hermitian eigenvalues, unitary diagonalization, invariance of Schmidt rank and PPT under local unitaries, and the standard Choi characterization of complete copositivity by a PSD partial transpose. The Choi/Schmidt interfaces in [Hou et al.2015 Propositions2.2–2.3](https://faculty.sites.iastate.edu/ytpoon/files/inline-files/pmaps_LAA_2015.pdf) and the strict sufficient spectral condition in [0908.1846v2 SectionII/Theorem1](https://arxiv.org/html/0908.1846v2) were actually read at their bounded interfaces in my preceding v43-B. Neither entire paper nor a current-SOTA/novelty audit is claimed. The new core inequalities are derived here, not imported from either paper.

## 3. Normalization, noncommuting literal span and inertia — S9–25

For a4-by4 unitary U, `||vec(U)||^2=Tr(U*U)=4`, so Phi_U=vec(U)/2 is normalized. The given I,Z,X are Hilbert–Schmidt orthogonal:

- Tr Z=1+i-1-i=0;
- X has zero diagonal, so Tr X=0;
- Z*X has zero diagonal as well, so Tr(Z*X)=0.

Acting on e_j gives `ZX e_j=i^(j+1)e_(j+1)=i XZ e_j`, including the cyclic boundary. Thus ZX=iXZ; the three-dimensional unitary span contains noncommuting generators and is not the old commuting two-Bell plane.

The three normalized rays are orthonormal, so unweighted Q is a rank3 orthogonal projection. Therefore lambda I16-Q has eigenvalue lambda-1 three times and lambda thirteen times. For0<=lambda<1 its negative inertia is exactly three, even though some other eigenvalues vanish at lambda=0. This distinguishes it from the literal one/two-negative predecessors; it does not by itself show two-block positivity or indecomposability.

## 4. Fresh full-complex simultaneous Gram derivation — S39–84

Use coefficient matrices C with `vec(C)=sum C_ij |ij>`. For ANY rank<=2 C, choose a complex4-by2 isometry S spanning its columns and write C=SZ. Rank-one and zero matrices are included by completing the plane. Conversely every SZ has rank<=2, and isometry gives `||C||_F^2=||Z||_F^2`.

Let z_j be column j of Z. For normalized weighted rays the negative overlaps are exactly

    h_r=sqrt(p_r)/2 Tr(U_r* C)
       =sum_j [sqrt(p_r)/2 e_j* U_r* S] z_j.

Define `v_jr=sqrt(p_r)/2 S*U_r e_j` and V_j with those columns. Then `h=sum_j V_j* z_j`. Thus the linear map L:Z->h has

    (L L*)_(rs)=sum_j v_jr* v_js
       =sqrt(p_r p_s)/4 sum_j e_j* U_r* S S* U_s e_j
       =sqrt(p_r p_s)/4 Tr(U_r* P U_s)=H_rs(S).

This is Hermitian PSD and depends only on the complex plane P=SS*, not its orthonormal basis. Its exact squared operator norm is lambda_max(H). Consequently

    ||h||^2<=lambda_max(H)||Z||_F^2,
    <vec(C),W vec(C)>=lambda||Z||_F^2-||h||^2.

If H<=lambda I_m for every S, all rank<=2 expectations are nonnegative. Conversely, if H has a unit eigenvector v with g>lambda, choose `z_j=V_j v`. Then

    ||Z||_F^2=v*Hv=g,
    h=Hv=gv,
    <vec(C),W vec(C)>=lambda g-g^2=g(lambda-g)<0.

Since lambda>=0, g>lambda implies g>0, so the constructed C is nonzero and still rank<=2. This proves the exact converse, not only a sufficient bound. All zero weights simply zero the corresponding columns/rows; no division by p_r or lambda is used. For m=0/all weights zero the matrix inequality is vacuous and W=lambda I is PSD/copositive.

### Phase-conjugation comparison with the two-Bell precedent

For U_r=Z=diag(i^j), the overlap is

    Tr(Z* C)/2=sum_j (-i)^j C_jj/2,

NOT `sum i^j C_jj/2`. Correspondingly the column v_jr contains positive i^j, and taking V_j* conjugates it in h. The upper-right Gram entry against U_0=I is nevertheless `Tr(PZ)/4`, with its conjugate in the lower-left. This is exactly the consistent convention of the previous two-functional derivation, now rederived from vec coefficients rather than accepted from its verdict. With scalar positive energy lambda I, the former inverse-Gram normalization reduces to H<=lambda I; the direct proof avoids an invalid division at lambda=0.

The criterion quantifies over EVERY complex S. No real-plane restriction, phase gauge making all variables real, finite test set or sampled Schmidt basis occurs.

## 5. Analytic ALL-PPT screen and the actual copositivity certificate — S88–119

Let F_swap exchange the two4-dimensional tensor factors. Directly,

    P(Phi_I)^Gamma
      =(1/4)sum_ij |ij><ji|=F_swap/4.

Because Phi_U=(U tensor I)Phi_I and Gamma is on Bob,

    P(Phi_U)^Gamma
      =(U tensor I)F_swap(U* tensor I)/4.

F_swap is a Hermitian involution and `I-F_swap` is twice the antisymmetric projection, hence F_swap<=I. Unitary conjugation therefore gives `P(Phi_U)^Gamma<=I16/4`. Multiplying by nonnegative p_r and summing yields the OPERATOR inequality

    Q_p^Gamma<=(sum_r p_r)I16/4.

For every PPT density rho, rho^Gamma is PSD of trace1. The trace pairing of partial transpose gives

    Tr(Q_p rho)=Tr(Q_p^Gamma rho^Gamma)<=sum_r p_r/4.

This is a bound on the ENTIRE PPT cone, not a candidate search. A negative expectation against W would require `lambda<sum p_r/4`.

More strongly the same operator inequality gives

    W^Gamma=lambda I-Q_p^Gamma
       >=[lambda-sum p_r/4]I16.                   (CP-CERT)

Thus any strictly positive lower margin for lambda-sum p_r/4 proves complete copositivity directly, not merely a trace test or cone-duality assertion. Sections6–7 derive that margin from actual rank-two controls.

## 6. Literal I,Z,X controls and exact constants — S123–154

Take P=diag(1,1,0,0). All three diagonal Gram entries equal Tr(P)/4=1/2 by unitarity and cyclicity of trace. The I/Z entry is

    H_01=Tr(PZ)/4=(1+i)/4,
    H_10=(1-i)/4.

The entries coupling X to I or Z vanish: the relevant products are a diagonal matrix times X, which has zero diagonal. Therefore

    H=[[1/2,(1+i)/4,0],[(1-i)/4,1/2,0],[0,0,1/2]].

The2-by2 eigenvalues are1/2 +/- |1+i|/4=1/2 +/- sqrt2/4, and the third is1/2. The universal condition necessarily gives

    lambda>=(2+sqrt2)/4.

This is a NECESSARY bound from one actual plane, not a claim that this is the exact global two-block-positivity threshold. Meanwhile the all-PPT screen gives `Tr(Qrho)<=3/4` for every PPT rho; no attainment/optimality of that upper bound is assumed.

The source's rational control C0=diag(1,1+i,0,0) has rank2 and norm squared3. Its unnormalized I and Z overlaps are respectively

    (2+i)/2,       [1-i(1+i)]/2=(2-i)/2,

and its X overlap is zero. After normalization by sqrt3, the first two squared overlaps are each5/12. Hence the total Q expectation is5/6 and the W expectation is lambda-5/6. This independently verifies the literal control as a weaker necessary bound `lambda>=5/6>3/4`, with no missing normalization factor.

Combining the stronger plane bound with(CP-CERT),

    W^Gamma>=[(sqrt2-1)/4]I16>0.

Thus no PPT-negative target exists for any two-block-positive lambda in the literal family. The overlap<=3/4 assertion is an analytic upper bound, not an evaluated PPT maximizer or an exhibited state.

## 7. Entire arbitrary-weight, at-most-three orthogonal-ME family — S158–209

Relabel weights `p1>=p2>=p3>=0`, appending zero weights when needed.

### 7.1 All weight boundaries

If p1=0, every weight is zero and W=lambda I has PSD partial transpose for all lambda>=0. No positive margin is asserted at lambda=0.

If p1>0 but p2=0, only one ray is present. Truncate that ray's ME Schmidt decomposition to two terms and normalize. Each Schmidt coefficient is1/2; the normalized rank-two control has squared overlap1/2. Thus two-block positivity forces `lambda>=p1/2`. Equation(CP-CERT) gives

    W^Gamma>=p1 I16/4>0.

This treats a single nonzero weight without requiring a nonexistent second unitary/eigenvalue pair. It also shows lambda=0 cannot be two-block-positive when Q_p is nonzero.

### 7.2 Actual local-unitary reduction for p2>0

First send U1 to I by multiplying coefficient matrices on the left by U1*. The relative V=U1*U2 is unitary and has trace0 by orthogonality. Diagonalize it as `T*VT=diag(eta_1,...,eta_4)`. The further coefficient transformation `C->T*C T` is realized by local unitaries `T* tensor T^T`; it preserves I, rank, Frobenius norm and scalar completion. Thus the two largest-weight rays may genuinely be treated as I and diag(eta), not as an assumed common Schmidt basis. The transformed third ray remains ME and contributes a nonnegative squared overlap.

The eigenvalues have unit modulus and sum0. Expanding the squared sum gives

    0=|sum eta_i|^2
      =4+2 sum_(i<j)Re(eta_i conj(eta_j)).

Hence the six pairwise real parts sum to -2. At least one is at least their average -1/3. This is an exact sum/average proof, not sampling or a root catalogue.

### 7.3 The terminal rank-two eigenvalue bound

Use only diagonal C_ii=x, C_jj=y for that pair, with `|x|^2+|y|^2=1`. Such C is an actual rank<=2 coefficient matrix. The first two weighted overlaps contribute

    (1/4)[p1|x+y|^2
          +p2|conj(eta_i)x+conj(eta_j)y|^2].

Its Hermitian2-by2 Rayleigh matrix has diagonal `(p1+p2)/4` and upper-right

    [p1+p2 eta_i conj(eta_j)]/4,

with conjugate lower-left. Its largest eigenvalue is exactly

    [p1+p2+|p1+p2 eta_i conj(eta_j)|]/4.

An eigenvector supplies x,y attaining that value. The remaining weighted projector term is nonnegative, so the FULL Q_p expectation is at least this attained first-two value. Two-block positivity consequently forces

    lambda >= [p1+p2+R]/4,
    R=sqrt(p1^2+p2^2-(2/3)p1 p2).

The modulus bound follows by expanding its square and using the selected pair's real part>=-1/3. No sufficient witness spectral condition enters.

Because p1>=p2>0,

    R^2-p2^2=p1[p1-(2/3)p2]
       >=p1*p2/3>0.

Thus `R>p2>=p3`, including p3=0 and every equality among the positive weights. Subtracting the all-PPT operator bound in(CP-CERT) gives

    W^Gamma>=[(R-p3)/4]I16>0.

This is the claimed complete-copositivity certificate for EVERY nonzero admissible weight vector with p2>0. It also covers exactly two nonzero weights. Together with7.1 it covers ALL nonnegative-weight boundaries without a continuity argument, inverse at zero, or lost case.

For three unit weights, `R=2/sqrt3`, so the uniform necessary bound is `1/2+1/(2sqrt3)>3/4`. The literal bound `(2+sqrt2)/4` is stronger for I,Z,X; it is not claimed uniformly for all orthogonal triples.

The at-most-three hypothesis is used precisely when the remaining weight is only p3<=p2. For four or more rays the proof does NOT establish `R>sum of the remaining weights`. Orthogonality supplies trace0 of the relative unitary; maximal entanglement supplies unitaries and the1/4 swap bound; scalar completion supplies the common norm comparison. None of these hypotheses may be dropped by this proof.

## 8. Primary-source applicability and non-promotions

S31–35 correctly limits Hou et al. to a general multiple-negative Choi/Schmidt framework. It does not import an indecomposable2-positive M4 example. The exact H criterion and terminal eigenvalue bound have been reconstructed directly above.

For the literal unweighted0<=lambda<1 trial, the three negative eigenrays are normalized ME4 rays. Each has squared2-Schmidt norm1/2, so the total is3/2, not strictly below1. The actually read0908.1846v2 Theorem1 requires that STRICT condition; it cannot certify this trial. For weighted trials the actual negative spectrum would have to be considered before using any such spectral theorem. This review uses no borrowed sufficient certificate; the swap proof supplies the needed partial-transpose bound directly.

No positive candidate state is substituted after the all-PPT incompatibility. No numerical target screening, program-backed isometry census, evaluated Schmidt optimizer or finite certificate is asserted. Prior D-type/two-Bell/x1111/N4 artifacts are not premises, and their individual v8-qualified histories remain unchanged.

## 9. Findings and remaining gaps

**Findings: none at the reconstructed written scope (0F/0M/0m).** No load-bearing new Gram, phase, all-PPT, terminal-eigenvalue or zero-weight step remains NOT_RECONSTRUCTED. The finite-dimensional linear-algebra and Choi/copositivity interfaces remain named classical imports, not proof-assistant certification; full primary-article validity and novelty are not newly audited.

Supported: the entire stated scalar-completion class with at most three mutually orthogonal ME4 projectors and arbitrary nonnegative weights has no two-block-positive PPT detector; every such two-block-positive completion is completely copositive, with the stated strict margin for nonzero Q_p.

NOT supported: arbitrary nonorthogonal rays; four or more rays; nonmaximally entangled rays; non-scalar/anisotropic positive completions; arbitrary rank-three negative parts or arbitrary2-positive M4 maps; a rational PPT/SN3 state; unrestricted P44; formal/kernel/human/cross-vendor/novelty or publication acceptance. The source's mechanism closure is not a full-target theorem or a scientific GO.
