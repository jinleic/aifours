# Addendum 3: the universal critical hidden sum exceeds 16/3

Status: **WRITTEN-checked with exact stdlib Fraction/Bernstein arithmetic**, awaiting independent scientific review. This immutable successor strengthens `frontier-20261029-ph7-critical-all-hidden-sum-greater-five-v1-addendum-2.md` (SHA256 `636618365f15562f402b1381df3210b8b48e6fd0ef137497d4729be5231d1b2c`) to the topology-independent bound

`p>16/3`.

The original hypotheses and scope are unchanged: the generator is real seven-state Metzler, its spectrum contains zero and the critical complex pair twice, and its other two eigenvalues are stable with hidden quadratic `y^2+p*y+q`.

## 1. A sharper centered closed-walk inequality

Let `X` be any centered real 7-by-7 Metzler matrix (`tr X=0`), write `X=D+A` with diagonal `d_i` and nonnegative off-diagonal `A`, and let `tau_j=tr X^j`. Put `D2=sum_i d_i^2` and `B=sum_{i<j} A_ij*A_ji`, so `tau2=D2+2B`. Let `W` be the sum of the two directed triangle-orientation products over all unordered triples, each orientation counted once. The trace-three/four formulas in the parent source give

`3W=tau3-sum_i d_i^3-3sum_{i<j}(d_i+d_j)A_ij A_ji`,

`tau4 >= -4*sqrt(3*tau2)*W`.

Because the seven diagonal entries have sum zero,

`|sum_i d_i^3| <= (5/sqrt(42))*D2^(3/2) < (4/5)*D2^(3/2)`.

The extremum is the ordinary fixed-variance, zero-sum 7-vector extremum (six equal values and one opposite sixfold value). Also

`|3sum_{i<j}(d_i+d_j)A_ij A_ji| <= (3/sqrt(2))*sqrt(D2)*(tau2-D2) < (17/8)*sqrt(D2)*(tau2-D2)`.

Set `t=sqrt(D2/tau2)` when `tau2>0`. The sum of the two error bounds, divided by `tau2^(3/2)`, is at most

`(4/5)t^3+(17/8)t*(1-t^2) = (17/8)t-(53/40)t^3 <=21/20`, for `0<=t<=1`.

The square of its exact maximum is `24565/22896 < (21/20)^2`. Therefore

`3W <= tau3+(21/20)*tau2^(3/2)`,

and using `4sqrt(3)/3<7/3` yields the strictly stronger **universal necessary inequality**

`tau4+(7/3)*sqrt(tau2)*max(tau3,0)+(49/20)*tau2^2 >=0`.      (RESOURCE-4)

When `tau2=0`, `X` is entrywise nonnegative and the same weak inequality holds. All nonnegative closed-walk, AM-GM and diagonal-extremum claims need independent checking; no selected matrix or numerical generator is used.

## 2. Exact complex-hidden selector covers

If the stable hidden pair is real, the existing all-real theorem supplies the stronger `p>3437/500`. For hidden `-r +/- ih`, the original trace-square proof gives `r>43/20`. Suppose `r<=8/3`; parameterize the entire domain by

`r=43/20+(31/60)*s`, `h^2=t*(45r^2-72r-58)/63`, `0<=s,t<=1`.

For `tau3<=0`, the geometric-mean centered trace-three inequality and(RESOURCE-4) require both `E3=(25/42)*tau2^3-tau3^2>=0` and `J=tau4+(49/20)*tau2^2>=0`. The exact stdlib checker `frontier-20261029-ph7-complex-hidden-third-fourth-8over3-check.py` (SHA256 `2087dd1aec87124e9405fe6bd45a804789a6ad9f99be38238dc4b8d91e36156a`) returned PASS on a complete selector tree of **30** strict `-E3` leaves and **21** strict `-J` leaves.

For `tau3>0`, (RESOURCE-4) requires `J+(7/3)*sqrt(tau2)*tau3>=0`. The exact stdlib checker `frontier-20261029-ph7-complex-hidden-positive-skew-8over3-check.py` (SHA256 `e493713d6a67871cbeb1fe5b420f90a4c4f8746c6ffa80075593ea690f3924fd`) returned PASS on a complete tree of **19** `-tau3>=0` leaves and **12** leaves proving both `-J>0` and `J^2-(49/9)tau2*tau3^2>0`. On the strictly positive-skew domain the latter gives a contradiction.

Each exact program loads only definitions from its pinned predecessor and stretches the r-coordinate by `31/21`; each constructs/checks its own complete binary tree. This is reused stdlib `Fraction`/integer implementation by the same owner, not a disjoint scientific audit or formal proof. Both skew cases exclude the endpoint `r=8/3`, so `p=2r>16/3`. No PH7/PH8 realization or exclusion, minimum-state decision, novelty, or parent adoption is claimed.
