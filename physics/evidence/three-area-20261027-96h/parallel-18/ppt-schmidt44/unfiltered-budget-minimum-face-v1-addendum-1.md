# Unfiltered minimum-face addendum1 — an actual negative-margin bound from the two original minimum eigenvalues

Owner **PhysicsPPT44-2**, physics-3. Actual native `/bin/date` immediately BEFORE this NEW immutable write: **Tue Oct 27 17:03:57 PDT 2026**. **WRITTEN UNREVIEWED**, no identity machine-checked. Same narrow release `e7064ab24f10a1228c22b9d9c7c2e9a6868b4aee3d2818eaf2c422ec9ec300ff`; same actual pre-derivation ACK `b49ec7b0...` before ALL current mathematics.

This continues the actual original-operator result `unfiltered-budget-minimum-face-v1.md`, SHA `499cedbd21a8540b0f4d178919f45c4f604742602e45ec2fb9b64a4a951b69c3`,159LF. That result is AUTHOR-WRITTEN/UNREVIEWED, not a parent adoption. The elementary scalar-form steps used here are supplied explicitly below rather than inferred from a favorable review.

## 1. Exact quantified claim

Keep the ORIGINAL C^4 tensor C^4 and EVERY Hermitian complex-two-block-positive W in the release. Let A=Tr_B W, B=Tr_A W, with minimum eigenvalues alpha,beta and minimum spaces E_A,E_B. Their positivity and the zero-minimum boundary are established in the preceding original-vector proof. Put

    c=min(alpha,beta),
    m=min(dim E_A,dim E_B),
    kappa=max(m-2,0).

For EVERY positive density rho with ORIGINAL range in E_A tensor E_B,

    Tr(W rho) >= -kappa*c.                                (1.1)

No PPT assumption is needed for that lower bound. If rho is PPT, the exact adopted actual-pair upper inequality also gives

    -kappa*c <= Tr(W rho) <= c.                           (1.2)

If a negative eligible pair in this face exists, its margin therefore obeys

    0 < -Tr(W rho) <= kappa*c.                            (1.3)

No bound is asserted sharp or achievable. This is a quantitative necessary coupling for actual original pairs, not a constructed state/separator or a favorable sign in the residual case.

## 2. Uniform product pairings from the ACTUAL partial traces

For EVERY unit u in E_A and EVERY unit v in E_B,

    0 <= <u tensor v|W|u tensor v> <= c.                  (2.1)

The lower bound is the given product-vector positivity. To prove the upper bound alpha, complete the ARBITRARY quantified v to ANY full orthonormal family on the ORIGINAL Bob space. The defining partial trace identity sums the nonnegative product expectations to `<u|A|u>=alpha`; hence the particular summand at that same arbitrary v is at most alpha. The symmetric full-family trace identity gives beta. No concrete basis is selected or tested: the proof holds for every u,v and every completion and the partial trace is basis-independent.

Homogeneity gives for ALL u in E_A,v in E_B, including zero,

    0 <= q_W(u tensor v) <= c ||u||^2 ||v||^2.             (2.2)

This is a scalar identity/bound on the original W, not a new local operator, projector congruence, filter or replacement problem. No physical rho or W is normalized/regauged by this argument.

For any TWO original product vectors x,y, positivity of `q_W(lambda x+mu y)` for ALL complex lambda,mu gives the scalar-form Cauchy bound

    |<x|W|y>| <= sqrt(q_W(x)q_W(y)).                       (2.3)

It is precisely the full two-scalar quadratic-form fact already proved in the preceding packet, not an operator compression and not a chosen scalar or phase probe. The complex modulus is retained; no real-only positivity is used.

## 3. ALL original vectors in the face, including every Schmidt rank

Let psi be an ARBITRARY original vector in E_A tensor E_B. If it is zero, the claim is immediate. Otherwise its ordinary Schmidt decomposition can be written as an EXACT equality of ORIGINAL vectors

    psi=sum_(i=1..r) s_i u_i tensor v_i,
    s_i>0,   sum_i s_i^2=||psi||^2,

with the nonzero Schmidt vectors u_i in E_A, v_i in E_B and r<=m. This follows from ordinary finite-dimensional singular-value/spectral tensor algebra: the two local spans of a tensor in E_A tensor E_B lie in those intrinsic subspaces. No new operator or state on a smaller tensor space is introduced or tested. The decomposition does not act on W or rho.

Set x_i=s_i u_i tensor v_i and d_i=q_W(x_i). By(2.2),

    d_i>=0,    S:=sum_i d_i <= c ||psi||^2.

Using(2.3) for EVERY pair of these original product terms gives

    q_W(psi)
      >= sum_i d_i - 2 sum_(i<j) sqrt(d_i d_j)
       = 2S-(sum_i sqrt(d_i))^2
      >= -(r-2)S.                                        (3.1)

The last inequality is ordinary finite-sum Cauchy. This is the ENTIRE symbolic sum over all terms; no Schmidt coefficient, phase, rank or numerical vector is substituted for a sanity check.

For r<=2 the given SR2 hypothesis directly gives q_W(psi)>=0. For r>2, (3.1) and S<=c||psi||^2 yield

    q_W(psi)>=-(r-2)c||psi||^2
             >=-kappa*c||psi||^2.                         (3.2)

These cases exhaust every possible r, without choosing a rank to test. All zero d_i, degenerate Schmidt coefficients and complex phases are harmless; no division by them occurs.

## 4. The actual mixed-state caller, without transforming rho

Spectral decomposition of the ORIGINAL positive rho expresses it as a positive sum of unit original eigenvectors in its range. Every such vector is in the prescribed face. Sum(3.2) with those actual positive spectral weights; they sum to Tr rho=1. This proves(1.1) for the SAME rho and W. No projector is formed or applied, and no quotient/rank-model alias replaces an actual eigenvector.

For PPT rho, the original adopted inequality is `Tr(W rho)<=min(b_A,b_B)`. On the actual face, the re-derived intrinsic eigenvalue condition gives b_A=beta and b_B=alpha. This pays the upper bound c in(1.2) at its exact original-object caller. Strict negativity gives(1.3), not existence.

In the source's original notation Z=tau I-I tensor B-A tensor I+W, equation(1.1) also yields the actual slack estimate

    Tr(Z rho)>=tau-alpha-beta-kappa*c.                   (4.1)

This is weaker than the favorable-sign threshold `tau-alpha-beta` when kappa*c>0. Hence the remaining positive-minima, large-eigenspace sign is NOT silently disposed of by the quantitative bound.

## 5. Degenerate boundaries and exact scientific delta

If either minimum is zero, c=0 and(1.2) gives exact zero for PPT rho, consistent with the stronger original-kernel conclusion in v1. That earlier kernel argument actually applies to every positive face state, not merely PPT. If m<=2, kappa=0 and(1.1) gives nonnegativity, again consistent with the actual tensor-rank proof. No state outside the face is included in these conclusions.

If c>0 and m>2, the lower bound permits a negative interval. Neither equality nor a negative actual pair is asserted; proving favorable sign still needs the stronger PPT-specific residual coupling identified in v1. No source theorem, dimension change, selected spectral multiplicity, nonunitary congruence or marginal normalization has been used to force it.

The new delta is a **uniform actual negative-margin bound** in terms of the SAME W's two minimum partial-trace eigenvalues and intrinsic minimum-space dimensions. It is not an additional positive-reconstruction map iteration or coordinate encoding. It supplies a constraint on any possible eligible negative pair in this entire face, not a proper witness ansatz treated as WLOG.

This continuation does not prove P44 or global nonnegativity, and is not a novelty/historical-absence claim. Its exact first unpaid implication remains: the given original PPT condition must be used to raise(4.1) to `Tr(Z rho)>=tau-alpha-beta`, or an exact eligible pair violating that threshold must be supplied. No such extra premise/result is available in this packet. No transformed lower-dimensional theorem or old held proof is invoked as a substitute.

## 6. Controls

All mathematics is on original W/rho/vectors with elementary scalar Hermitian forms, trace identities, Schmidt/spectral decomposition and finite-sum Cauchy, each actual use written above. No projector compression/congruence/filter/regauging/marginal normalization, old scaling/JL/L1/zero-ensemble/normal-chart guide, external source or reviewer body. No selected operator/state/basis/parameter case was evaluated EVEN PRIVATELY. All vectors, scalar coefficients and ranks in the proof are the FULL quantified ones needed to prove the stated theorem.

No scientific interpreter/calculator/Eval arithmetic/CAS/program/enumeration/solver/replay/build/test/typechecker, modelCLI/nested agent/paidAPI, Git/delete/contact/publication/infrastructure mutation. Metadata clocks/hashes/counts only. w30/JL and all legacy STOP/HOLD/ZERO/findings/N4 UNKNOWN historical exit unestablished/old21 NR/auxiliary214 STOP persist; L1/consumers remain HELD/ZERO/NONINPUT. No formal/kernel/executable/human/configured-family/novelty/P44 acceptance; successor end2026-10-31T21:23:27.000Z unchanged.
