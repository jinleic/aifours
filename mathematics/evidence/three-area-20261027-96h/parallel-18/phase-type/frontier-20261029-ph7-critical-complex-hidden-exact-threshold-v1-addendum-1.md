# Addendum: the complex-hidden algebraic threshold is strict

Status: **WRITTEN-checked-in-kernel with exact rational polynomial arithmetic**, pending independent mathematical review. This is an immutable strengthening of `frontier-20261029-ph7-critical-complex-hidden-exact-threshold-v1.md` (SHA256 `16441b5fa43e2d02f71eaa0d73d9640f0a59b08d2e70e756f5c1da26cc68e0f2`).

Under the hypotheses of that source, the mean decay of the nonreal hidden pair satisfies

`r > alpha`,

where `alpha` is the unique root in `(49/20,5/2)` of `g(r)=90r^3-216r^2-131r+293`. Therefore `p=2r>2alpha`, and the same strict lower bound holds for either hidden-root type using the stronger all-real theorem.

## Proof

Suppose `r=alpha`. The boundary factorization in the cited source reads, for `t=V(r)-h^2` and `0<=t<=V(r)`,

`E = -972*g(r)^2/49 + 8748*(5r-4)*g(r)*t/7 - 19683*(5r-4)^2*t^2 + 127575*t^3`.

At `g(alpha)=0`, the last two terms are strictly negative whenever `t>0`, because `19683*(5alpha-4)^2>127575*V(alpha)`. If `t>0`, then `tau2>0`, the `tau3` bracket equals `(315alpha-252)*t>0`, and the symmetrized third-moment inequality requires `E>=0`; contradiction. Hence `t=0` and `tau2=tau3=0`.

Let `X=G+[(4+2alpha)/7]I`, so `tr X=0`. The exact identity

`tr(X^2)=sum_i X_ii^2 + 2*sum_{i<j} X_ij*X_ji`

and Metzler signs force every diagonal `X_ii=0` and every bidirectional product `X_ij*X_ji=0`. Thus **all entries of `X` are nonnegative**. In particular, `tr(X^4)>=0`, because it is a sum of nonnegative closed-walk products.

The formal eigenvalues of `X`, with `h^2=V(alpha)`, instead give a negative fourth trace. Exact polynomial division by `g` yields

`tr(X^4) = -4*(1488*alpha^2-3792*alpha+541)/945`.

The quadratic in parentheses is strictly positive on `[49/20,5/2]`: at `49/20` it is `4558/25>0`, and its derivative there is `17496/5>0` and increases. Thus `tr(X^4)<0`, contradiction. Equality is impossible, so `r>alpha`.

The displayed boundary factorization and fourth-trace polynomial remainder were checked in the owner's SymPy kernel with exact rational arithmetic. They are not formal proof-assistant verification or independent scientific review. The all-hidden caller still depends on the separately pinned real-hidden-root theorem. This is a necessary spectral bound only; it supplies no PH7/PH8 realization or exclusion, novelty clearance, or parent adoption.
