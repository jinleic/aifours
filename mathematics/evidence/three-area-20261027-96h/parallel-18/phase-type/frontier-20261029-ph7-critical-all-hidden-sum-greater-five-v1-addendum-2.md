# Addendum 2: the universal critical hidden sum exceeds 103/20

Status: **WRITTEN-checked with exact stdlib Fraction/Bernstein arithmetic**, awaiting disjoint scientific review. This immutable successor improves `frontier-20261029-ph7-critical-all-hidden-sum-greater-five-v1-addendum-1.md` (SHA256 `73b970af67b2a2fe2d4c84c922a0c575a13ec189eb4f2a7ffc4bcdc35cb34b9b`) to

`p>103/20`.

The hypotheses are unchanged: a real seven-state Metzler generator with the critical repeated pair, a zero eigenvalue, and two stable hidden eigenvalues whose monic real quadratic is `y^2+p*y+q`.

## Sharper fourth-trace inequality

The proof of the original `p>5` source `frontier-20261029-ph7-critical-all-hidden-sum-greater-five-v1.md` (SHA256 `2f01ff058c4977e5f49c77082b4353934e880b3efd0e6276857fdac848f32760`) can retain its exact constants. For a centered real Metzler matrix with `tau2=tr X^2>=0`, `tau3=tr X^3`, and `tau4=tr X^4`, the closed-walk expansion gives

`3W <= tau3+(1+3/sqrt(2))*tau2^(3/2)`,

`tau4 >= -4*sqrt(3*tau2)*W`.

Therefore

`tau4+(7/3)*sqrt(tau2)*max(tau3,0)+(29/4)*tau2^2 >=0`.    (SHARP4)

Indeed `4sqrt(3)/3<7/3` because `sqrt(3)<7/4`, and

`(4sqrt(3)/3)*(1+3/sqrt(2)) = 4sqrt(3)/3+2sqrt(6) < 7/3+49/10 =217/30 <29/4`,

using `sqrt(6)<49/20`. The `tau2=0` case gives `X` entrywise nonnegative and `tau4>=0`. This is a strict improvement on the previous safe coefficients 3 and 10, but still a necessary inequality, not a sharp constant claim.

## Exact selector covers

For the complex hidden pair `-r +/- ih`, suppose `r<=103/40`. The prior trace-square argument gives `r>43/20`, and the admissible rectangle is

`r=43/20+(17/40)*s`, `h^2=t*(45r^2-72r-58)/63`, `0<=s,t<=1`.

If `tau3<=0`, the geometric-mean trace-three bound requires `E3=(25/42)tau2^3-tau3^2>=0`, and(SHARP4) requires `J=tau4+(29/4)tau2^2>=0`. Exact checker `frontier-20261029-ph7-complex-hidden-third-fourth-103over40-check.py` (SHA256 `a97546108c6b222802942c691df7f5de3d390761ecc294eb85bbbe9b466ac00f`) returned PASS for a complete selector tree with **26** strict `-E3` leaves and **16** strict `-J` leaves.

If `tau3>0`, (SHARP4) requires `J+(7/3)sqrt(tau2)*tau3>=0`. Exact checker `frontier-20261029-ph7-complex-hidden-positive-skew-103over40-check.py` (SHA256 `b8f4db0f1f50ac7dddb21023ad8a7c963e037dc0247e0f8159413587666e64c6`) returned PASS for a complete tree with **15** leaves where `-tau3>=0`, and **12** leaves where `-J>0` and `J^2-(49/9)tau2*tau3^2>0`. On the positive-skew domain this contradicts(SHARP4).

Each checker loads only mathematical definitions from its pinned predecessor and stretches the prior r-coordinate by `17/14`; it constructs/checks its own full binary tree with stdlib `Fraction`/integer arithmetic. The two implementations reuse prior polynomial code and are not independent scientific audits. Both cases exclude the endpoint `r=103/40`, so `p=2r>103/20`. The stable real-hidden-root branch is already stronger (`p>3437/500`) by the named exact all-real theorem.

The result is an all-topology necessary spectral condition only. It does not establish PH7 existence or exclusion, the minimum state count, a PH8 result, novelty, formal proof, or parent adoption.
