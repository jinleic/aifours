# A universal phase-jump packing obstruction for stable convex families

**Status: WRITTEN theorem with one WRITTEN-checked-in-kernel example; author candidate, not parent adoption.** This result applies to every convex family of real monic Hurwitz polynomials of fixed degree, including every eligible interval box. It rules out a broad class of attempted counterexample constructions that demand incompatible resonances from different members. It does not decide the unrestricted common-SPR question.

## Universal packing bound

Let \(K\) be a nonempty convex family of monic real degree-\(n\) polynomials, all strictly Hurwitz. For each \(p\in K\), let \(\theta_p(\omega)=\arg p(i\omega)\) be continuously unwrapped from \(\theta_p(0)=0\). Given ordered, nonoverlapping intervals
\[
0\le u_1<v_1\le u_2<v_2\le\cdots\le u_N<v_N<\infty
\]
and arbitrary actual members \(p_1,\ldots,p_N\in K\),
\[
\boxed{\quad
\sum_{j=1}^N\bigl[\theta_{p_j}(v_j)-\theta_{p_j}(u_j)\bigr]
<\left(\frac n2+N-1\right)\pi.\quad}
\]
In particular, two disjoint septic-frequency windows cannot each contain an actual member whose phase rises by more than \(9\pi/4\), because their sum would exceed \(9\pi/2\).

**Proof.** Every Hurwitz polynomial has \(\theta_p(0)=0\), \(\theta_p(\infty)=n\pi/2\), and strictly increasing phase: if its roots are \(r_j\) in the open left half-plane, then
\[
\theta_p'(\omega)=\sum_j\operatorname{Re}\frac1{i\omega-r_j}>0.
\]
For any two members \(p,q\), convexity and strict stability of their segment imply
\[
|\theta_p(\omega)-\theta_q(\omega)|<\pi\quad(\omega\ge0).
\]
Indeed, a phase difference equal to \(\pm\pi\) would make their imaginary-axis values opposite nonzero rays, so a convex combination would vanish. The continuous phase difference starts at zero and cannot leave that interval.

For each gap \(v_j\le u_{j+1}\), monotonicity and the phase-spread bound give
\[
\theta_{p_j}(v_j)-\theta_{p_{j+1}}(u_{j+1})<\pi.
\]
Telescoping the \(N\) increments and \(N-1\) gaps leaves
\(\theta_{p_N}(v_N)-\theta_{p_1}(u_1)<n\pi/2\), giving the bound. ∎

This is a necessary restriction on actual stable families, not a sufficient SPR synthesis condition. The bound is generally not asserted sharp. It explains why separately chosen extreme resonances cannot simply be placed into a candidate interval box without checking the segment and mixed-corner stability.

## Exact failed construction

Let
\[
p_1(s)=(s+1)\left((s+\tfrac1{100})^2+1\right)^3,\qquad
p_2(s)=4^7p_1(s/4).
\]
Both polynomials are individually Hurwitz. On \([9/10,11/10]\), \(p_1\)'s phase rises by more than \(3\pi-3/4\), and on \([18/5,22/5]\), \(p_2\)'s phase rises by the same amount. Their sum exceeds \(9\pi/2\), so no strictly stable convex family—and in particular no eligible independent interval box—can contain both.

The independent exact replay proves this incompatibility directly as well: the imaginary part of \(p_1(i\omega)\overline{p_2(i\omega)}\) has opposite strict signs at \(\omega=51/50\) and \(11/10\), while its real part is strictly negative on that entire interval, certified by eight negative Bernstein coefficients. At an intermediate frequency the two values are opposite nonzero rays, so an actual convex combination has an imaginary-axis zero. The coefficientwise interval hull's \((E_+,O_-)\) corner also has \(\Delta_2=-19653209/100000<0\). The direct segment finding is stronger than merely saying the independent hull is unstable.

Frozen polynomial factors, cross-polynomial coefficients and exact signs: `frontier-20261029-incompatible-resonance-segment-frozen-v1.json`, SHA-256 `8261c3ed39d6e4b9422629b0f6653d581f5eb167d0b315f7f7320b029a61590b`. Independent checker `frontier-20261029-incompatible-resonance-segment-independent-kernel-v1.py`, SHA-256 `7996eb11fcd59413298bdc929e34512b04547c61370c7a85d7f274ef3f303b87`; receipt `frontier-20261029-incompatible-resonance-segment-independent-result-v1.json`, SHA-256 `9ff769edd30be520004e7497ba5c2eb459a6ffa422bc376cb4bd889fd27823e6`. The receipt records the corrected initial hull-corner indexing; the segment cross checks had already passed and the corrected block was resumed.

The packing theorem is written mathematics; the example's finite identities use exact integers and `fractions.Fraction` on one Python Eval host. No formal proof, cross-vendor review, novelty clearance, arbitrary-box synthesis verdict, or all-numerator negative certificate is claimed.
