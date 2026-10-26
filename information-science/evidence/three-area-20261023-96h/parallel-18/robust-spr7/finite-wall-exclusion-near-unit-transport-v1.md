# SPR7 — finite-wall exclusion for actual near-unit gain transport

Actual `/bin/date` observation immediately before this paper: **Sun Oct 25 12:19:33 PDT 2026**. InfoSPR7 / info-2. **NEW COMPLETE WRITTEN THEOREM CANDIDATE**, not yet independently reconstructed or parent accepted. All algebra below is written exact polynomial/rational algebra; no scientific interpreter/eval/program/CAS, arithmetic enumeration, optimization, sampling or replay was used. Metadata source/hash/clock operations only. V9/v10/v11 and scientific HOLD remain binding.

The v83-A original-r1 review was fully written and actually RETURNED before this new primary proof. `primary-return-from-v83-exposure-ack-v1.json` expressly discloses earlier informal sign-support/Cauchy ideas considered before that return; those ideas are not called post-return or preregistered. The new finite-wall proof was developed after that ACK and saved substantively in checkpoint-v21.

## 0. Exact new scope

For EVERY actual independent robustly Hurwitz monic septic box with at least one varying coefficient in EACH parity block, a sequence of admissible root transports with bounded last odd root and gain products tending to the unit threshold CANNOT approach any positive finite mutual-root collision or any opposite-ACTUAL-band endpoint. There is a uniform positive distance from all fifteen such finite walls throughout a sufficiently near-unit sublevel with the last odd root bounded.

This closes a particular genuine boundary-control obligation. It does NOT prove the existence of any product below one, compactness of all bad minimizers, automatic stationary cone membership, universal SPR7, or an unrestricted counterexample. Root0 and the last odd root escaping to infinity remain separate. A precise gain product approaching1, not merely a finite product greater than1, is essential.

This is one complete boundary theorem, independent of the still-candidate compactified-repair/facet-path v3 packet; it does not inherit any pending cone verdict.

## 1. Named inputs and the original profile boundary

Mathematical input R is `general-seven-band-root-transport-certificate-v1.md`, SHA256 `b064261dae70f2dc0dc53317a7d99d6e38fe5e5885f7f4db8cf16ac418eb3dfb`, especially its ACTUAL component intervals, root domain, worst-product identity and exact gains in §§1–3. Its v56 correction is `root-transport-v56-rationality-and-leading-sign-addendum-v1.md`, SHA256 `b1358582f7be557e1e912bd944692411a1b834f1063ba6401a04d7f9df881a50`: the t-component cubics have leading coefficient−1; the s-numerator is monic. No rationality of an optimizer or gain is inferred from rational roots. The parent supported R at its named Hermite–Biehler/root-continuity/classical boundaries, not formal/kernel/human/configured-family/novelty acceptance.

The original pinned even-Euler packet is `even-euler-comparator-candidate-v1.md`, SHA256 `ec744ccc6b269bb935aaa95e075cc559cda0ca6c44cc6bd580144306edc3c61a`, supported at its explicit sufficient-budget scope by RUN/`spr7-even-euler-parent-v1.md`. The entire-span reciprocal obstruction is `even-euler-entire-profile-obstruction-v1.md`, SHA256 `cf7d75fac33d83ffa93cf5af5d3f277753585375345fb38f4a18e6e511a2368f`, with the SPR section of RUN/`wave-v17-partial-parent-dispositions-v1.md` preserving its FIXED-M normalization and profile-only exclusion. These two packets supply the historical problem/claim boundary, not a universal dichotomy premise. No all-M obstruction or characterization by the even-profile condition is assumed. Their named sufficient results are not restated as an unrestricted theorem.

New classical tools here are elementary cubic Lagrange interpolation, compactness/subsequences, continuity of polynomial coefficients, and the fact that a differentiable nonnegative real function has derivative0 at an interior zero. All uses are given below. No scientific computation or finite certificate is an input.

## 2. Original box, exact root domain and exact gains

Let the ORIGINAL independent box be

`K={a(s)=s^7+a_1s^6+...+a_7 : l_i<=a_i<=u_i}`,

with every member strictly Hurwitz. Set

`E_a(t)=-a_1t^3+a_3t^2-a_5t+a_7`,

`O_a(t)=-t^3+a_2t^2-a_4t+a_6`.

Assume at least one of intervals1,3,5,7 has positive width AND at least one of intervals2,4,6 has positive width. This includes every all-seven-positive-width box. It does NOT silently replace the unrestricted target by this subdomain; boxes with one fixed parity block retain their separate existing scope.

For the ACTUAL attained ordered root bands write

`I_Ej=[a_j,b_j]`, `I_Oj=[c_j,d_j]`,

`0<a1<=b1<c1<=d1<a2<=b2<c2<=d2<a3<=b3<c3<=d3`.

Root endpoints here are not coefficient names. R provides these strict cross-parity separations for actual component blocks, preserving all within-block correlations.

For chosen roots set

`e(t)=-product_j(t-p_j)`, `o(t)=-product_j(t-q_j)`.

The admissible domain is EXACTLY

`0<p1<c1`, `d1<p2<c2`, `d2<p3<c3`,

`b1<q1<a2`, `b2<q2<a3`, `b3<q3<infinity`,

`p1<q1<p2<q2<p3<q3`.                                  (D)

Its transported hulls are `J_Ej=hull(I_Ej,p_j)` and `J_Oj=hull(I_Oj,q_j)`; they strictly alternate. Define the ACTUAL independent minima

`A_p(t)=min_(E actual) e(t)E(t)`,

`B_q(t)=min_(O actual) t o(t)O(t)`.

They are the explicit midpoint/radius formulas in R. Independence gives, for `N_k(s)=k e(-s^2)+s o(-s^2)`,

`min_(a in K) P_(a,N_k)(t)=k A_p(t)+B_q(t)`,

where `P=E_aE_N+tO_aO_N`. All seven original coefficients and every actual corner are retained.

The sign control from R is

`B_q>0 on union J_Ej`, `A_p>0 on union J_Oj`;

outside those hulls neither product is negative for positive t. The gains are

`alpha=G_E=max_(union J_Ej) (-A_p)_+/B_q`,

`beta=G_O=max_(union J_Oj) (-B_q)_+/A_p`,

and `rho=alpha beta`. Each is an exact finite maximum for an admissible finite root configuration. A strict common numerator with those roots exists iff rho<1, with `k>beta` and `k alpha<1`. Below we deliberately use k=beta only to obtain a WEAK limiting inequality; equality at that k is not called SPR.

## 3. Both varying parity blocks force all six actual bands to have positive width

Fix all coefficients of an actual component except one varying coefficient and choose two distinct allowed values of that coefficient. The resulting cubics differ by a nonzero constant times one monomial `t^r`; r is0,1,2 or3 for E and0,1 or2 for O.

They cannot share ANY positive root: at such a root their difference would be nonzero. Each actual cubic has its three simple positive ordered roots by the named HB input. Therefore each of the three same-index roots takes at least two distinct values. Its attained band has positive width. Apply this independently to both parity blocks.

Hence throughout the present theorem

`a_j<b_j` and `c_j<d_j` for every j.                    (PW)

This is an actual coefficient-box argument, not the assertion that arbitrary ordered free roots are independent coefficients.

## 4. Uniform positive lower bounds on BOTH gains when q3 is bounded

Fix any finite bound M>0 and consider admissible roots with q3<=M. By interlacing, ALL six selected roots are then at most M.

Choose four distinct positive RATIONAL frequencies `tau_i` strictly inside I_E1. At each tau_i the ACTUAL even-component interval strictly straddles0. Indeed an actual first even root occurs below tau_i and another above it, while every actual second root is beyond this band. Thus there are actual even values of both strict signs. Put

`delta_E=min_i min{max_E E(tau_i), -min_E E(tau_i)}>0`.

For ANY cubic f with leading coefficient−1, degree-three Lagrange interpolation at these four fixed nodes gives

`-1=sum_i f(tau_i)/product_(j!=i)(tau_i-tau_j)`.

Consequently

`max_i |f(tau_i)| >= c_tau`,

`c_tau=[sum_i 1/|product_(j!=i)(tau_i-tau_j)|]^-1>0`.    (LAG)

For f=e, select such an i. By actual even variation,

`-A_p(tau_i)>=delta_E c_tau`.

This frequency is in J_E1, so B_q(tau_i)>0. Since all q roots are bounded by M and K is fixed compact, there is a fixed finite positive D_E with `B_q(tau_i)<=D_E` for every i and every root configuration under consideration. For example use the maximum of `tau_i(tau_i+M)^3 max_(O actual)|O(tau_i)|`. Therefore

`alpha>=g_E:=delta_E c_tau/D_E>0`.                    (LE)

For the odd gain choose four distinct rational frequencies `upsilon_i` strictly inside I_O3. The ACTUAL odd-component interval strictly straddles0 there, by the same root-range argument. Let its minimum two-sided magnitude be delta_O>0 and its Lagrange lower constant be c_upsilon>0.

At a sample where |o|>=c_upsilon,

`-B_q(upsilon_i)>=upsilon_i delta_O c_upsilon`.

The frequency lies in J_O3, and A_p>0 there. Bounded selected roots and compact actual E data give a fixed upper bound D_O>0 for A_p at these samples. Hence

`beta>=g_O:=(min_i upsilon_i)delta_O c_upsilon/D_O>0`.  (LO)

The two constants are uniform over ALL admissible transports with q3<=M, including p1 tending to0 and approaches to finite walls. No denominator lower bound at a moving wall was assumed. A small denominator can only increase the corresponding gain.

If K has rational coefficient endpoints, M can be taken rational. All chosen sampling nodes and Lagrange constants can be rational; component extrema at these fixed nodes are actual linear-box extrema, so the displayed bound constants can also be chosen rational. No nodes or constants were numerically evaluated, and no rationality of alpha or beta is asserted.

## 5. Any finite-root near-unit limit has nonnegative ACTUAL pairings

Let `(p_n,q_n)` be admissible, q3,n<=M, and

`limsup_n rho_n<=1`.

Eventually rho_n<=4. From LE/LO,

`g_O<=beta_n<=4/g_E`.

Set `k_n=beta_n` EXACTLY. It is bounded above and away from0. After passing to a subsequence the roots and k_n converge; denote their limiting cubics by e*,o* and scale by k*>0. The leading coefficients of e*,o* remain−1. Set

`N*(s)=k* e*(-s^2)+s o*(-s^2)`.

This is still monic exact degree7, though it is not asserted strict Hurwitz or SPR at this stage.

For every n and t in an even transported hull,

`k_n A_n(t)+B_n(t)>=B_n(t)(1-rho_n)`.

In an odd transported hull it is at least `(k_n-beta_n)A_n=0`. Outside all hulls it is nonnegative; t=0 is also nonnegative. Thus with `epsilon_n=(rho_n-1)_+ ->0`,

`min_(a in K) P_(a,N_n)(t)>=-epsilon_n |B_n(t)|`.      (WEAK)

For bounded q roots and compact actual coefficients, `|B_n(t)|<=(constant)(1+t)^7` uniformly in n,t. This follows directly from `|o_n(t)|<=(t+M)^3` and the fixed cubic coefficient bound on O. No optimization is hidden in this estimate.

Taking coefficient limits in WEAK gives

`P_(a,N*)(t)>=0 for EVERY a in K and EVERY t>=0`.     (NN)

The infinity coefficient remains1. NN is only weak positivity and is not a constructed strict numerator.

## 6. Positive finite selected-root collisions are impossible in this limit

Every same-parity limiting root is simple. In fact the closed inequalities give

`p1*<=c1<d1<=p2*<=c2<d2<=p3*`,

`q1*<=a2<b2<=q2*<=a3<b3<=q3*`,

using PW. Hence each cubic retains three distinct roots. Only p1* can be0.

Suppose e* and o* share a positive root t0. By NN, for EACH actual a the polynomial P_(a,N*) is nonnegative and vanishes at this interior point. Its derivative must vanish. Because both numerator components vanish there,

`k* e*'(t0) E_a(t0)+t0 o*'(t0) O_a(t0)=0`            (C)

for EVERY actual denominator.

Hold an actual odd component fixed and vary one nonconstant even coefficient. At positive t0 its monomial direction is nonzero, so E_a(t0) takes at least two distinct values. Subtracting C forces `k* e*'(t0)=0`. Since k*>0 this contradicts the already proved simple even root. Varying the odd block would independently force `t0 o*'(t0)=0` as well.

Thus none of the five adjacent mutual-root gaps in D can collapse at a positive finite limit. This proof uses actual coefficient independence, not merely ordered abstract bands or an assumed invariant measure.

## 7. Opposite-ACTUAL-band endpoint contacts are also impossible

Suppose an even selected root p_j* equals ANY finite endpoint of an actual odd band that bounds its cell in D. Such an endpoint t0>0 is attained by an actual odd component O^0, with O^0(t0)=0. Fix this actual O^0 and combine it independently with EVERY actual even component E.

Both terms of the pairing vanish at t0, because e*(t0)=0 and O^0(t0)=0. NN and the interior derivative condition give

`k* e*'(t0) E(t0)+t0 o*(t0) (O^0)'(t0)=0`            (E-WALL)

for every actual E. Varying the even block and subtracting again forces e*'(t0)=0, contradicting simplicity. No claim that root endpoints arise from unrelated free cubics is used: O^0 is an attained ACTUAL component.

The odd-root wall case is symmetric but its factor t0 must be retained. If q_j* is an attained actual even-band endpoint, fix E^0 with E^0(t0)=0 and vary all actual O. The derivative identity is

`k* e*(t0)(E^0)'(t0)+t0 o*'(t0) O(t0)=0`             (O-WALL).

Actual odd variation and t0>0 force o*'(t0)=0, again impossible.

These arguments exclude ALL ten opposite-band endpoint inequalities in D from becoming equalities. They also apply if p1* happens to be0 elsewhere in the same limit; the contact t0 considered here remains strictly positive.

## 8. Exact uniform threshold-compactness theorem

Define the FIFTEEN finite wall margins, excluding the separately unresolved root0 margin, by

`c1-p1, p2-d1, c2-p2, p3-d2, c3-p3`,

`q1-b1, a2-q1, q2-b2, a3-q2, q3-b3`,

`q1-p1, p2-q1, q2-p2, p3-q2, q3-p3`.

**Theorem F.** Under the actual-box/two-varying-parity-block hypotheses above, for EVERY finite M>0 there exist epsilon>0 and delta>0 such that EVERY admissible root transport satisfying

`q3<=M` and `G_E G_O<=1+epsilon`

has ALL fifteen displayed margins at least delta. The set may be empty; no existence of a near-unit point is asserted. There is no asserted uniform positive lower bound on p1.

**Proof.** If not, choose for each positive integer n an admissible transport with q3<=M, rho<=1+1/n, and a displayed wall margin less than1/n. The roots belong to a fixed bounded closed coordinate region. Pass to a convergent subsequence, and then one along which the same displayed margin tends to0. Sections4–5 produce NN with k*>0. Same-parity roots stay simple by PW. Sections6–7 exclude every such positive finite wall. This is a contradiction. The argument is compactness, not an interpreter enumeration or a numerical epsilon/delta search.

Equivalently: a unit-threshold sequence with bounded q3 can escape the original open root domain ONLY through p1->0; no positive finite gap collapse or opposite-band touch survives. If p1 is ALSO bounded away from0, every subsequential limit is strictly admissible, and the exact gain formulas are continuous there. Even then a limiting gain product equal to1 gives only a weak boundary numerator, not the required strict one.

## 9. Exact unresolved gap and next representation

Theorem F supplies actual global boundary control at the UNIT threshold. It does not control an infimum strictly greater than1, prove a bad minimum exists in the interior, show product<1 somewhere, or create an actual full-eight obstruction.

The two remaining threshold escape mechanisms are p1->0 and q3->infinity. At0 the derivative argument fails because0 is an endpoint of the frequency half-line; at infinity the monic coefficient compactness used above fails when q3 diverges. Neither is dismissed by adding a frequency0/infinity correction atom, and no degree-six or zero-constant limit is substituted for the original target.

The next representation is the EXACT reciprocal/projective pairing at the two endpoint limits, together with full active-ratio/stationarity and actual independent coefficient data. If a threshold sequence stays bounded away from both endpoints, F puts it in the strict root domain where the existing full stationary moment/cone machinery applies. That machinery still needs automatic actual membership, an actual full-eight negative instance, or a genuinely gain-controlled root escape; passing or failing a sufficient endpoint test alone is not a general verdict.

The original fixed-M reciprocal profile obstruction remains only a profile obstruction. The already positively solved actual R/T box remains positive. No universal selection between the even/odd profiles, all-M obstruction, even-profile characterization, new counterexample, or solution of universal SPR7 is claimed.

## 10. Assurance boundary

This new theorem and all its load-bearing gain bounds, weak-limit estimates and wall exclusions are WRITTEN candidates requiring fresh complete source-pinned reconstruction. Accepted R/classical input is explicitly named; no pending v3 result, historical unadmitted computation, Kac review, old witness count, or reviewer headline is a mathematical premise.

All pinned sources and process findings remain immutable. No scientific execution, new GO, external model/CLI, nested agent, author/shared write, Git/config/publication/deletion, formal/kernel/human/configured-family/executable or novelty acceptance occurred or is claimed. Original science cutoff2026-10-27T11:05:38-07:00 and final deadline12:35:38 remain unchanged. This packet is not round completion.
