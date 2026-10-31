# An exact algebraic mean bound for complex hidden poles

Status: **WRITTEN-checked-in-kernel by exact rational symbolic identities**, pending independent mathematical review. This strengthens the complex-hidden case of `frontier-20261029-ph7-critical-all-hidden-sum-lower-bound-v1.md` (SHA256 `fb7a5540887785cd64d5e73f397bafb0ec71261ed3b5945c612b97d8da64840a`). It does not establish that the hidden poles are complex or decide PH7 existence.

## 1. Statement

Suppose a real seven-state Metzler generator has the critical double pair and stable nonreal hidden pair `-r +/- i*h` with `r,h>0`. Then

`r >= alpha`, hence `p=2r>=2alpha`,

where `alpha` is the unique real root in `[49/20,5/2]` of

`g(r)=90r^3-216r^2-131r+293`.

The root is strictly above `49/20`, so the result strictly strengthens `p>49/10`. Equality is not excluded by this necessary moment argument and is not asserted realizable.

## 2. Exact centered-moment factorization

Use the centered `tau2,tau3` formulas of the cited universal hidden-sum source. Their Metzler square inequality gives `r>43/20` and

`0<v:=h^2<=V(r):=(45r^2-72r-58)/63`.

The square bracket in `tau3` is decreasing in `v` for `r>43/20`, and at `v=V(r)` it equals `-2g(r)`. On `[43/20,alpha)`, `g<0`, so `tau3<0`. Hence the geometric-mean symmetrization/7-state symmetric trace inequality gives

`E(r,v):=(107163/4)*[(25/42)tau2^3-tau3^2] >= 0`.

Put `t=V(r)-v`, so `0<=t<=V(r)`. Exact expansion gives the useful *boundary factorization*

`E(r,V-t) = -972*g(r)^2/49 + [8748*(5r-4)*g(r)/7]*t - 19683*(5r-4)^2*t^2 + 127575*t^3`.

For `r in [43/20,alpha)` the first term is strictly negative and the linear coefficient is strictly negative. The quadratic-plus-cubic terms are nonpositive because `t<=V(r)` and

`19683*(5r-4)^2 - 127575*V(r) = 162*(2475r^2-3960r+2669) >0`.

The last quadratic has positive leading coefficient and negative discriminant. Thus `E<0`, contradicting the necessary inequality. This proves `r>=alpha`.

## 3. Root isolation and verification scope

Exact values are `g(43/20)=-2965/32`, `g(49/20)=-751/800`, and `g(5/2)=87/4`. For `r=43/20+s`, `s>=0`,

`g'(r)=(10800s^2+29160s+7531)/40 >0`.

Consequently `alpha` exists and is unique above `43/20`, with `49/20<alpha<5/2`. The factorization and displayed polynomial identities were checked using exact SymPy rational arithmetic in the owner's kernel and are explicitly printed for independent reconstruction; no sampled spectrum is used in the proof.

The disjoint real-hidden-root branch retains the stronger `p>=2r_*>3437/500`. Combining the two branches gives an all-hidden necessary bound `p>=2alpha` for stable hidden roots. This is not an actual PH witness, minimum-state theorem, independent scientific review, formal proof, novelty clearance, parent adoption, or complete 8/9 verdict.
