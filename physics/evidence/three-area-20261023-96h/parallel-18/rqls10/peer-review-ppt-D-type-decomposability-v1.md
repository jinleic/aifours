# v37-D — whole-class D-type decomposability: written reconstruction

**Reviewer:** PhysicsRQLS10-2 / physics-5. **Author:** PhysicsPPT44. Actual pre-write `/bin/date`: **Sun Oct 25 05:16:13 PDT 2026**.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR at the complete stated operator-theorem scope.** I reconstruct the whole coefficient-wise decomposition, including zero-coefficient boundaries. No load-bearing mathematical identity in that decomposition is left NOT_RECONSTRUCTED. This is same-harness written support for the D-type route only, not parent acceptance or an unrestricted P44 result.

No scientific interpreter/eval, arithmetic program, enumeration, certificate replay, solver, nested agent or external CLI was used. The source's historical or other accepted x1111 decompositions are not premises. HOLD v2 and parent evidence erratum v7 remain binding.

## 1. Exposure, pins, complete body and import boundaries

The pre-body ACK was written FIRST at `peer-review-ppt-D-type-decomposability-ack-v1.json`, with observed clock **Sun Oct 25 05:12:58 PDT 2026**, before opening the source body.

- Manifest: `peer-review-wave-eighteen-v37.json`, exact v37-D entry LF81–102, SHA256 `eb3d6f624c9e191702658bf2a8c969b2904e9aa347c91df173b131c0be1dba54`.
- Packet receipt: `peer-review-wave-eighteen-v37-packet-receipt-v1.json`, all LF1–43 read, SHA256 `a6f2954275c0599fca95790b3471fdf66f1faabaa846191e0a43d70c6d4b75c2`. It records literal equality for this packet.
- Literal packet: `peer-review-wave-v37-ppt-D-type-decomposability-sources-v1.md`, SHA256 `c680b77764a5d5ff0bbb7425c2767e3ed1db481d8de10026d090dc80a49d5599`; ALL packet LF1–297 read.
- **S**, the complete declared source: `physics/evidence/three-area-20261023-96h/parallel-18/ppt-schmidt44/diagonal-bell-consolidated-decomposability-v2.md`, ALL LF1–288, SHA256 `a3f31bcafd86554f7304775566d451264fc5cac1837dfd7236cbab1bca1b3523`. Fresh metadata hash matches the frozen source pin.
- Parent erratum v7 was read in full earlier this session; its operative LF5–11,37–39 were explicitly reread for this assignment. No computation exception or GO is inferred.

Long/load-bearing packet lines additionally reread verbatim with `:raw`: LF11,15,40,44,46,48,50,67,98,164,178,185,229,276,284,288,290,292,294,296. Source line citations below refer to S; packet line number is source LF+8.

Only elementary finite-dimensional operator/linear algebra, Schmidt rank of a vectorized matrix, weighted Cauchy–Schwarz, real quadratic minimization, the two-by-two PSD criterion and the definition of partial transpose are used in the proof. No old finite certificate or prior review verdict transfers into the theorem.

## 2. Literal operator and the prior reductions

### 2.1 Normalization and coefficient orientation — S:9–22,46–59

With unnormalized `Omega=sum_i |ii>`, its projector contributes −1 at every coherent entry `|ii><jj|`. For `vec(C)=sum_ij C_ij |ij>`, direct expansion gives

    <vec(C),W(a)vec(C)>=sum_ij a_ij|C_ij|²−|Tr C|².

There is no missing dimension-four normalization factor. The vector's Schmidt rank equals rank C, so testing every complex matrix of rank at most two is the correct two-block-positivity condition.

The coefficient convention in the D-type map is also consistent. For

    L_D(X)=diag_j(sum_i X_ii D_ij)−X,

the Choi expansion `sum_pq |p><q| tensor L_D(E_pq)` has product diagonals D_pj and coherent negative term `−|Omega><Omega|`. Thus D=a, not a transpose. This checks the local orientation claim without importing a map-classification theorem.

For strictly positive entries, the inverse-Gram reduction is correct: write C=UZ, with U an arbitrary complex two-plane isometry, and set `u_j=U*e_j`, `A_j=U*diag_i(a_ij)U`. Every A_j is positive definite. Weighted Cauchy–Schwarz gives

    |sum_j u_j*z_j|² <= [sum_j u_j*A_j^(-1)u_j]
                         [sum_j z_j*A_j z_j].

Conversely choosing `z_j=A_j^(-1)u_j` gives energy-minus-trace-square `H(1−H)`, negative for H>1. A rank-one image is included by extending it to a two-plane. This is universal over COMPLEX planes, not a finite or real-only test. The inverse criterion is not silently extended to singular A_j at zero coefficients; the decomposability proof below does not need it there.

**Boundary verdict:** 0F/0M/0m.

### 2.2 CLDUI form and the PPT Gram objective — S:61–74

The diagonal-unitary action `D tensor conjugate(D)` fixes Omega and each product projector, so its average preserves W expectation and PPT. Its invariant pattern is exactly a coherent block r on span{|ii>} plus product diagonals s_ij for i different from j. Positivity is r>=0 and s>=0. Partial transpose replaces each coherent cross pair by a two-by-two block on {|ij>,|ji>}, so PPT is exactly

    s_ij s_ji >= |r_ij|²,

with the already nonnegative diagonals. For positive pair coefficients, minimizing `a_ij s_ij+a_ji s_ji` under that product constraint gives `2sqrt(a_ij a_ji)|r_ij|`, attained at the stated square-root ratio. The remaining Bell contribution is −2Re r_ij and the coherent diagonal coefficient is d_i=a_ii−1, giving S:(3).

This reduction is independently consistent, but neither it nor any successful numerical objective is needed for the whole-class proof.

**Boundary verdict:** 0F/0M/0m.

## 3. The rank-two matching test, including all zero-cost cases — S:78–120

Fix exactly the matching {01,23}. For any nonnegative z, choose a coefficient matrix with those two independent two-by-two diagonal blocks and diagonal entries z_i. On a matched pair impose `C_ij C_ji=z_i z_j`. Each block's determinant is zero, so its rank is at most one; the full coefficient matrix has rank at most two.

For positive pair coefficients, the elementary inequality

    a_ij x²+a_ji y² >= 2sqrt(a_ij a_ji)xy

is sharp at the positive ratio `x/y=sqrt(a_ji/a_ij)`, with xy=z_i z_j. Therefore its minimized energy is exactly `2c_ij z_i z_j`, where c_ij=sqrt(a_ij a_ji).

Zero cases are legitimate limits of the SAME rank-two tests:

- If z_i z_j=0, both off-diagonals may be zero and the block still has rank at most one.
- If z_i z_j>0 and precisely one coefficient is zero, send the entry with positive cost to zero and let its zero-cost partner grow so that their product remains fixed. Every finite approximating matrix still has the required rank. The cost tends to zero and the diagonal/trace part stays fixed. If that limiting expectation were negative, sufficiently late finite tests would already be negative. Thus two-block positivity forces its nonnegativity; no compactness of normalized test vectors is needed.
- If both costs are zero, choose any finite product realization and the cost is zero exactly.

Combining the two independently chosen blocks and subtracting `(sum_i z_i)²` proves copositivity of the exact symmetric matrix K with diagonal d_i, matched off-diagonals c_01−1,c_23−1, and four unmatched off-diagonals −1. It has the stated form

    K=[B -J; -J C].

This is ONLY copositivity at this stage. No invalid replacement by PSD has occurred.

**Boundary verdict:** 0F/0M/0m.

## 4. Two attained scalar minima and their complete formula — S:128–156

The two simplices are compact and the quadratics continuous, so mu and nu are attained. Copositivity with one block zero gives mu,nu>=0. For minimizing simplex vectors, independent nonnegative scaling gives

    mu t²+nu s²−2ts>=0 for all t,s>=0.

If mu=0, fix s=1 and let t grow; the expression becomes negative. The same argument excludes nu=0. Substituting s=1,t=1/mu yields nu>=1/mu, so mu nu>=1. Endpoint simplex choices imply d0,d1>=mu and d2,d3>=nu. In particular, a forbidden zero/small diagonal coefficient is ruled out by the original hypothesis itself, not ignored.

For completeness, the closed minimum formula S:(9) is correct at every branch boundary. Let p<=q and write the simplex point as (t,1−t). If b>=p,

    f(t)−p=(q−p)(1−t)²+2(b−p)t(1−t)>=0,

so min f=p. This includes the constant case p=q=b. If b<min(p,q), the coefficient p+q−2b is positive and the stationary point `(q−b)/(p+q−2b)` lies strictly between0 and1. Substitution gives `(pq−b²)/(p+q−2b)`. No zero denominator is invoked by the second branch.

**Boundary verdict:** 0F/0M/0m.

## 5. PSD caps with coefficient control, including vanishing square roots — S:160–204

Since `x^T Bx >= mu(sum x)²` for every x>=0 by scaling, `B−mu J` is copositive, and likewise for C−nu J.

For a real symmetric two-by-two matrix with nonnegative diagonal A,D, copositivity is exactly `b>=−sqrt(AD)`. Sufficiency is the displayed square identity. For necessity when A,D>0, choose the positive ratio cancelling that square. If A=0 and b<0, fixing v=1 and making u large gives negativity; the D=0 case is symmetric, and if both vanish take u=v=1. This spells out all zero-diagonal cases in the source's limiting argument.

It follows that `b0>=mu−g0` and `b1>=nu−g1`. Capping at the upper endpoints,

    h0=min(b0,mu+g0), h1=min(b1,nu+g1),

keeps h0 in [mu−g0,mu+g0], and analogously for h1. Thus the residual capped blocks have nonnegative diagonals and determinants

    (d0−mu)(d1−mu)−(h0−mu)² >=0,

and its other-block analogue. This proves `Bhat>=mu J`, `Chat>=nu J` by the exact PSD criterion, even when a factor or g_e is zero.

The discarded amounts obey

    n=max(0,b−minimum−g),
    0<=n<=max(b,0)<=c,

because the minimum is strictly positive, g>=0, and b=c−1 with c>=0. In particular c=0 forces n=0. This controlled bound is genuinely established; the proof does NOT rely on an arbitrary PSD-plus-entrywise-nonnegative split of a copositive matrix.

**Boundary verdict:** 0F/0M/0m.

## 6. Coherent PSD block and both positive pair blocks — S:208–246

The identity

    P0=diag(Bhat−mu J,Chat−nu J)
        +[mu -1;-1 nu] tensor J

is exact entrywise. The first term is PSD by Section5. The scalar matrix has positive diagonal and determinant mu nu−1>=0; J is PSD. Their tensor product is PSD, including equality of the determinant. Hence P0>=0 and its coherent embedding P_coh>=0.

For EACH of the two matched edges, the physical pair block is

    T_e=[a_ij, −(c_e−n_e); −(c_e−n_e), a_ji]

on {|ij>,|ji>}. Its diagonals are nonnegative and

    det(T_e)=c_e²−(c_e−n_e)²=n_e(2c_e−n_e)>=0

from0<=n_e<=c_e. Thus BOTH T_01 and T_23 are PSD. This includes a zero coefficient, c_e=0, n_e=0, n_e=c_e, and any zero determinant: no division by c_e or individual coefficients is used at this stage. D_unmatched is PSD directly from nonnegative product-diagonal coefficients.

**Boundary verdict:** 0F/0M/0m.

## 7. Full physical operator identity and arbitrary PPT inputs — S:254–276

Take partial transpose on the second tensor factor. A product diagonal remains unchanged, while `|ij><ji|` becomes `|ii><jj|`. Check every possible support class:

1. Coherent diagonal ii: P_coh contributes d_i=a_ii−1, exactly the coefficient in W.
2. Unmatched coherent cross ii/jj: P_coh contributes −1; no other summand contributes there.
3. Matched coherent cross: P_coh contributes `h_e=c_e−1−n_e`, while T_e^Gamma contributes `−(c_e−n_e)`. Their sum is exactly −1.
4. Off-diagonal product diagonal ij: the coefficient a_ij is supplied by the corresponding matched T_e or by D_unmatched.
5. No other operator entry occurs in either side.

Therefore the ENTIRE identity is

    W=P_coh+D_unmatched+(T_01+T_23)^Gamma=P+Q^Gamma,
    P>=0, Q>=0.

This is not a check of a selected state or principal subblock. For any PPT rho, without a state ansatz,

    Tr(W rho)=Tr(P rho)+Tr(Q rho^Gamma)>=0.

The full D-type witness class therefore cannot detect a PPT state while satisfying the stated universal complex two-block-positivity condition.

**Boundary verdict:** 0F/0M/0m. No load-bearing whole-operator identity is missing.

## 8. Prior work, explicit unreconstructed non-premises and non-claims

The manuscript correctly retains inverse-Gram/D-type attribution to Hou–Li–Poon–Qi–Sze (2015), Proposition4.1 and its stated restricted subclass results, rather than claiming the universal complex inverse-compression framework as new. It retains the CLDUI framework attribution to Britz–Laurent, arXiv:2512.06551v2, rather than claiming the sparse invariant-state pattern as new. The local Choi orientation and invariant block conditions are reconstructed above.

**NOT_RECONSTRUCTED in this review:** the external papers' complete texts, the author's bounded literature-search chronology or exact priority conclusion; Yang–Leung–Tang's broader theorem; every earlier Grassmannian/PPT-dual manuscript; the old21-table; the separately accepted37-term x1111 decomposition; N4's scientific/child-exit history. None is a premise for the coefficient-wise proof above. Their non-reconstruction does not hide a load-bearing identity in the new theorem. Novelty remains UNCLEAR.

The dimension-four/rank-two restriction is essential to THIS proof: two disjoint rank-one two-by-two blocks give total rank at most two and independent pair minima. A two-plus-three partition cannot automatically achieve all pair minima in its larger rank-one block. This review does not extend the result to arbitrary dimension, negative part, or every two-positive M4 map.

**Route disposition if parent integrates the review:** retire the whole specified nonnegative-diagonal-minus-one-Bell-projector D-type witness route against arbitrary PPT inputs, not merely a symmetric or rational subfamily. This is a route closure, NOT unrestricted P44/SN<=2, NOT another PPT/SN3 state, and NOT an accepted new x1111 certificate. N4 remains UNKNOWN/incomplete without retry or recovered child-exit status.

All source/author files remain unchanged. Same-harness supplied-proof written reconstruction only: no formal/kernel, human, cross-vendor, executed finite-certificate or novelty acceptance, and no scientific GO.
