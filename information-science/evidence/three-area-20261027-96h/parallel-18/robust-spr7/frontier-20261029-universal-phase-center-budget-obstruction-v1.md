# A universal phase-only separator and a barrier to phase-budget no-go proofs

**Status: WRITTEN; author candidate, not parent adoption.** Every compact convex family of real monic Hurwitz polynomials has a continuous, strictly increasing **phase-only** selector satisfying all common-SPR phase inequalities with a uniform gap. Consequently a no-go argument using only phase monotonicity, total phase budget, and the pointwise phase corridors cannot resolve the original interval-box problem. The remaining issue is whether such a selector can be realized by the phase of one real Hurwitz polynomial of the required degree; no such realization is claimed.

## Universal selector

Let \(K\) be a nonempty compact convex family of real monic Hurwitz polynomials of degree \(n\). For each \(p\in K\), let \(\theta_p(\omega)=\arg p(i\omega)\) be the continuous unwrapped phase with \(\theta_p(0)=0\). Define
\[
U(\omega)=\max_{p\in K}\theta_p(\omega),\qquad
L(\omega)=\min_{p\in K}\theta_p(\omega),\qquad
\theta_*(\omega)=\frac{U(\omega)+L(\omega)}2.
\]
Then \(\theta_*\) is continuous and strictly increasing on \([0,\infty)\), with \(\theta_*(0)=0\), \(\theta_*(\infty)=n\pi/2\), and
\[
|\theta_*(\omega)-\theta_p(\omega)|<\pi/2
\quad\text{for every }p\in K,\ \omega\ge0.
\]
In fact there is one \(\eta>0\), independent of \(p\) and \(\omega\), such that the absolute difference is at most \(\pi/2-\eta\).

**Proof.** As in `frontier-20261029-stable-family-phase-packing-obstruction-v1.md`, stable convex segments imply \(|\theta_p(\omega)-\theta_q(\omega)|<\pi\) for every \(p,q\in K\), so \(U-L<\pi\). The phases are continuous jointly in coefficients and frequency, with the prescribed unwrapped branch; monicity and bounded coefficients give uniform convergence to \(n\pi/2\) at infinity. Compactness of \(K\) and the compactified frequency interval makes the maximum phase spread strictly less than \(\pi\), giving the uniform gap.

Every \(\theta_p\) is strictly increasing, since \(\theta'_p(\omega)=\sum_{r:p(r)=0}\operatorname{Re}(i\omega-r)^{-1}>0\). On any fixed finite \([a,b]\), joint continuity and compactness give a common positive lower bound on this derivative. Both the maximum and minimum phase envelopes therefore increase strictly; their average does too. Their endpoints and continuity follow from the same compactness. ∎

The selector \(\theta_*\) need not be analytic or rational and is **not** asserted to be the boundary phase of a degree-\(n\) Hurwitz polynomial. The theorem gives a universal pointwise/monotonicity relaxation, not a common polynomial numerator.

## An absolute phase-budget no-go criterion is vacuous here

For arbitrary actual members \(p_i,q_i\in K\) and ordered nonoverlapping windows \([u_i,v_i]\),
\[
\begin{aligned}
\sum_i[\theta_{p_i}(v_i)-\theta_{q_i}(u_i)]
&\le\sum_i[U(v_i)-L(u_i)]\\
&=\sum_i[U(v_i)-U(u_i)]+\sum_i[U(u_i)-L(u_i)]\\
&<\frac{n\pi}{2}+N\pi.
\end{aligned}
\]
The first sum is at most the total monotone rise \(n\pi/2\); every phase spread in the second is strictly below \(\pi\). A proposed obstruction of the form
\(\sum_i[\theta_{p_i}(v_i)-\theta_{q_i}(u_i)]>n\pi/2+N\pi\)
therefore **cannot occur** in any compact stable convex family. In particular it cannot produce an eligible septic interval-box counterexample. More refined restrictions—such as the rootwise localization budgets in `frontier-20261029-multiwindow-phase-root-count-criterion-v1.md`—are not ruled out by this argument, because their bound may be smaller than the total phase budget.

This is a written theorem importing elementary Hurwitz factorization, convex-segment stability, compactness and phase continuity. It is not formal or cross-vendor verification, novelty clearance, a universal polynomial synthesis proof, or an unrestricted negative certificate.
