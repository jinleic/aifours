# Addendum 5: the universal critical hidden sum exceeds 269/50

Status: **WRITTEN-checked with exact stdlib Fraction/Bernstein arithmetic**, pending independent scientific review. This immutable successor improves `frontier-20261029-ph7-critical-all-hidden-sum-greater-five-v1-addendum-4.md` (SHA256 `a26a40aff63eafb07f10912566147052ba957d9787b2089e22398e94ff355395`) to

`p>269/50`.

The hypotheses remain those of the parent: a real seven-state Metzler generator with zero eigenvalue, the critical complex pair repeated twice, and two stable hidden eigenvalues whose monic quadratic is `y^2+p*y+q`. This is a necessary spectral condition, not an unrestricted PH7 verdict.

## 1. Sharpening the resource constants

The previous proof bounds centered `tau4` by the triangle term and optimizes the allocation of centered diagonal variance. Keep the same notation `D2=sum_i d_i^2`, `t=sqrt(D2/tau2)`, and oriented triangle-product sum `W`. The elementary bounds can be sharpened to

`|sum_i d_i^3| <= (5/sqrt(42))*D2^(3/2) < (31/40)*D2^(3/2)`,

`|3sum_{i<j}(d_i+d_j)A_ij A_ji| <= (3/sqrt(2))*sqrt(D2)*(tau2-D2) < (17/8)*sqrt(D2)*(tau2-D2)`.

Thus

`3W <= tau3 + tau2^(3/2)*[(17/8)t-(27/20)t^3]`.

The exact maximum on `0<=t<=1` of `t*[(17/8)t-(27/20)t^3]` is `1445/1728`. Because `4sqrt(3)/3 <37/16` and `(37/16)*(1445/1728)=53465/27648<39/20`, the same fourth-walk derivation gives

`tau4+(37/16)*sqrt(tau2)*max(tau3,0)+(39/20)*tau2^2 >=0`.      (RESOURCE-4C)

The rational comparisons follow by squaring positive numbers: `(5/sqrt(42))^2=25/42<(31/40)^2` and `(4sqrt(3)/3)^2=16/3<(37/16)^2`. For `tau2=0`, the centered Metzler matrix is entrywise nonnegative and `tau4>=0`.

## 2. Exact complex-hidden covers

A real hidden pair already obeys the stronger `p>3437/500`. For a nonreal hidden pair `-r +/- ih`, the prior trace-square argument gives `r>43/20`. Suppose `r<=269/100` and write

`r=43/20+(27/50)*s`, `h^2=t*(45r^2-72r-58)/63`, `0<=s,t<=1`.

For `tau3<=0`, the centered trace-three bound and(RESOURCE-4C) require `E3=(25/42)tau2^3-tau3^2>=0` and `J=tau4+(39/20)tau2^2>=0`. Exact stdlib checker `frontier-20261029-ph7-complex-hidden-third-fourth-269over100-check.py` (SHA256 `27028c95d8f9e97e6d80d3f6630db7b9f2e877f6550f8250a8e8b5dee364061c`) returned PASS for a complete selector tree with **33** strict `-E3` leaves and **23** strict `-J` leaves.

For `tau3>0`, exact stdlib checker `frontier-20261029-ph7-complex-hidden-positive-skew-269over100-check.py` (SHA256 `e62a85f224e07f64eaebe117dd78b1e561fb2d63b80e0dc1d93484fbf8ef7f58`) returned PASS for a complete tree with **18** `-tau3>=0` leaves and **16** leaves proving both `-J>0` and `J^2-(1369/256)tau2*tau3^2>0`. On the positive-skew subdomain the latter contradicts(RESOURCE-4C).

Each program imports only the pinned predecessor's mathematical definitions, stretches the original r coordinate by `54/35`, and constructs/checks its own complete binary tree using stdlib `Fraction`/integer arithmetic. This is reused implementation by the same owner, not disjoint scientific review or formal proof. Both skew domains exclude the endpoint, so `p=2r>269/50`.

No PH7 or PH8 realization/exclusion, minimum-state result, novelty, or parent adoption is asserted. The exact walk expansion, diagonal extremum, both selector unions, and real-hidden branch all remain audit targets.
