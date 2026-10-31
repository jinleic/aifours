# Strict gap between full two-dimensional privacy and exact marginal relaxation

**AUTHOR CANDIDATE — WRITTEN; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:54:56 PDT 2026`.

## 1. Scope and exact claims

Condition on the unreviewed source-independent 1D value/profile proof `frontier-20261028-exact-scalar-marginal-relaxation-v1.md`, SHA-256 `cde9bcc08bd4f87e635f1a2566fb2eaae6f1b289df5ebd4d36707229c8fc60ed`. Let `b=e^(-epsilon)` for ANY fixed epsilon>0 and kappa>=0. V_1,kappa is that candidate's exact all-law 1D infimum of `E[Y^2+kappa|Y|]`; V_2,kappa is the original all-law 2D infimum of `J+kappa L` under ALL events and the FULL closed l1-unit-diamond shifts.

The additional written conclusion is the STRICT inequality

    V_2,kappa > 2 V_1,kappa    for every epsilon>0, kappa>=0.           (1)

For pure L, with its separately derived 1D optimum from cde9, also

    inf_(full-D 2D) L > 2sqrt[b]/(1-b).                                  (2)

These are strict gaps in the original finite-epsilon optimization problem. No explicit positive gap size, source-equivalence or novelty is claimed. The proof establishes global existence from compactness, uniqueness of the 1D minimizing density, and a direct privacy contradiction at two simultaneous staircase jumps. It does NOT assume the 2D optimizer is a product, centered, radial or staircase.

## 2. The exact 1D optimizer is unique as a law

Let gamma in (0,1) be the cde9 root for the chosen cost. An arbitrary 1D optimum p can be symmetrized without changing privacy or the even cost. In cde9's exact lower proof, equality forces BOTH of the following for its symmetrized density p_s:

* The integer-tail inequalities are equalities for every k, so `p_s(n+x)=b^n p_s(x)` for a.e. x in (0,1) and all n>=0.
* The bounded-ratio fractional profile is exactly the high/low two-level profile, because `c(x)-c(gamma)` has strict sign off gamma and equality in its pointwise bathtub inequality forces both extreme density values.

Thus p_s is the symmetric staircase. To upgrade this to uniqueness of the ORIGINAL p, choose x in (0,gamma) and y in (gamma,1). Symmetric equality gives `p_s(y)=b p_s(x)` a.e.; privacy separately gives `p(y)>=b p(x)` and `p(-y)>=b p(-x)`. Their sums are equal, so both are equalities a.e. in (x,y). Hence on (0,1) the positive side has constants A,bA on the high/low intervals, and the negative side C,bC. Pick x>0 near 0 and y>gamma sufficiently near gamma that x+y<1. Cross-origin privacy gives `p(-y)=bC>=b p(x)=bA`, hence C>=A; the reverse signs give A>=C. Thus A=C.

For each n, the symmetrized staircase also saturates the integer-step lower ratio. Applying the same nonnegative-sum equality to p(n+x) and p(-n-x) forces each side to inherit exactly the b^n step. Thus p is the unique symmetric staircase almost everywhere. The same reasoning works for pure first norm, whose 1D fractional cost x is strictly increasing and whose gamma is `sqrt[m(m+1)]-m`.

## 3. Two marginal jumps violate a short diagonal shift

Suppose, for contradiction, a 2D full-D-private law has both coordinate marginals equal to that 1D staircase. Its bounded all-point private density f is strictly positive everywhere: any point of positive density propagates to any other by finitely many D shifts.

Choose `0<delta<min(gamma,1-gamma,1/2)` and `I=(gamma-delta,gamma)`. For a.e. x in I, the first marginal satisfies `p_1(x+delta)=b p_1(x)`. Pointwise privacy gives `f(x+delta,y)>=b f(x,y)`; integrating over y gives equality, so

    f(x+delta,y)=b f(x,y)  for a.e. (x,y) in I x R.                    (3)

The second marginal similarly implies

    f(x,y+delta)=b f(x,y)  for a.e. (x,y) in R x I.                    (4)

Null sets remain null under translation, so for a.e. (x,y) in I x I the two equalities chain to `f(x+delta,y+delta)=b^2 f(x,y)`. But the diagonal shift `(delta,delta)` is in D, and direct privacy requires `f(x+delta,y+delta)>=b f(x,y)`. Because 0<b<1 and f>0, this is impossible.

This contradiction uses the actual diagonal shifts of the FULL sensitivity diamond. It would not follow from checking only the two axis-unit shifts.

## 4. Existence makes the infimum gap strict

For J+kappa L, a minimizing sequence has bounded J and is tight; for pure L a minimizing sequence has bounded first moment and is tight. Product Laplace supplies a finite feasible trial. Weak subsequential limits preserve ALL D-shift privacy: for each h, pass the measure inequality through nonnegative bounded continuous test functions, then use measure order. The continuous nonnegative objective is lower semicontinuous, so the limit is feasible and attains the infimum.

If the 2D mixed infimum equaled twice the 1D optimum, its minimizer's two additive coordinate costs would each attain the 1D optimum. Section 2 then makes both marginals the unique staircase, contradicting §3. The same argument applies to pure L, proving (1)–(2). This establishes a positive but nonquantified gap for each fixed epsilon and kappa; no uniform-in-epsilon size is asserted.

## 5. Status and review

No numerical, formal, independent-model or human verification was performed. The exact 1D value and profile are explicitly imported from the pinned, unreviewed cde9 candidate; uniqueness, compactness and the diagonal-jump contradiction are written deductions. No named external research theorem, global source nonequivalence, novelty or parent acceptance is claimed. Disjoint review should examine the unsymmetrization equality, a.e. rectangle chain, closure under weak convergence, and strictness of the attained infimum.
