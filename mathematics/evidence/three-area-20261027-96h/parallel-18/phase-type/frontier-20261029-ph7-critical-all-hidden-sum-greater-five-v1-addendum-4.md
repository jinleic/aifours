# Addendum 4: the universal critical hidden sum exceeds 134/25

Status: **WRITTEN-checked with exact stdlib Fraction/Bernstein arithmetic**, pending disjoint scientific review. This immutable successor strengthens `frontier-20261029-ph7-critical-all-hidden-sum-greater-five-v1-addendum-3.md` (SHA256 `7976a0af141e18f781fcf42c400db667337094766b17b70d311d85eae9f0eece`) to

`p>134/25`.

The hypotheses are unchanged: a real seven-state Metzler generator with the critical repeated pair, a zero eigenvalue, and stable hidden quadratic `y^2+p*y+q`. This is a necessary spectral condition, not a PH7 decision.

## 1. A stronger diagonal-resource fourth-trace inequality

Use the centered notation of the preceding addendum. With `D2=sum_i d_i^2`, the directed-triangle contribution to `tau4` is bounded more accurately by the **diagonal** variance rather than the full trace:

`tau4 >= -4*sqrt(3*D2)*W`.

The same cubic-resource proof yields

`3W <= tau3 + tau2^(3/2)*f(t)`,

`t=sqrt(D2/tau2) in [0,1]`, `f(t)=(17/8)t-(53/40)t^3`.

Thus, for `tau2>0`,

`tau4 >= -(4sqrt(3)/3)*sqrt(tau2)*[t*tau3+t*f(t)*tau2^(3/2)]`.

The exact maximum of `t*f(t)` on `[0,1]` is `1445/1696`: writing `u=t^2`, it is the concave quadratic `(17/8)u-(53/40)u^2`. Since `4sqrt(3)/3<7/3` and `(7/3)*(1445/1696)=10115/5088<2`, we obtain the universal necessary inequality

`tau4+(7/3)*sqrt(tau2)*max(tau3,0)+2*tau2^2 >=0`.          (RESOURCE-4B)

This sign-safe inequality remains valid whether `tau3` is positive or negative: replace `t*tau3` by at most `max(tau3,0)`. If `tau2=0`, the centered matrix is entrywise nonnegative and `tau4>=0`. The exact closed-walk derivation and cubic error bound are imported from the preceding manuscript; no selected generator is involved.

## 2. Complete exact complex-hidden covers

For hidden `-r +/- ih`, the prior trace-square argument gives `r>43/20`. Assume `r<=67/25`, and parameterize the whole allowed rectangle by

`r=43/20+(53/100)*s`, `h^2=t*(45r^2-72r-58)/63`, `0<=s,t<=1`.

When `tau3<=0`, the usual centered trace-three inequality and(RESOURCE-4B) require `E3=(25/42)tau2^3-tau3^2>=0`, `J=tau4+2tau2^2>=0`. Exact checker `frontier-20261029-ph7-complex-hidden-third-fourth-67over25-check.py` (SHA256 `9ae5814d2aaab61627515314186e4888d750a066d1138ad463a33d152f97aabf`) returned PASS for a complete tree with **21** strict `-E3` leaves and **20** strict `-J` leaves.

When `tau3>0`, exact checker `frontier-20261029-ph7-complex-hidden-positive-skew-67over25-check.py` (SHA256 `8900f38eebc2f7bb8aa1d56655259015670f6e441bfb64cfde5f9c776917855e`) returned PASS for a complete selector tree with **18** leaves where `-tau3>=0` and **15** where both `-J>0` and `J^2-(49/9)tau2*tau3^2>0`. The latter alternative contradicts(RESOURCE-4B) on the positive-skew domain.

Each stdlib `Fraction`/integer checker imports only the pinned predecessor's mathematical definitions, stretches the r coordinate by `53/35`, and constructs/checks its own full binary tree. This is reused code by the same owner, not independent scientific review or formal verification. The stable real-hidden branch retains its stronger `p>3437/500`. Excluding the endpoint gives `p=2r>134/25` for the complex branch and hence for all stable hidden roots.

No full PH7/PH8 existence or exclusion result, minimum-state decision, novelty, or parent adoption is claimed.
