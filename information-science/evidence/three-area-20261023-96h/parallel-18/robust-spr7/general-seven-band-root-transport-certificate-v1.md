# General SPR7 root transport — complete six-band selection criterion and an explicit uniform band-conditioned class

Actual `/bin/date` observation before creation: **Sun Oct 25 08:05:58 PDT 2026**. InfoSPR7 / info-2. **NEW WRITTEN CANDIDATE**, requiring separate supplied-proof reconstruction. HOLD/v9 and all earlier errata are binding. No scientific interpreter/eval/program, symbolic computation, enumeration, sampling or replay was used. Metadata/source reads only. This is one consolidated general-box paper, not an R/T constant increment or a claim that the fixed root1000 is universal.

## 0. Delivered scope, and what is still missing

For an ARBITRARY robustly Hurwitz independent monic degree-seven coefficient box, this packet proves:

1. Every genuine common SPR numerator must transport its three even and three odd roots so that their hulls with the six ACTUAL uncertainty bands still strictly alternate. This is necessary for ALL unrestricted numerators, not an imposed four-column ansatz.
2. On that exact admissible root domain, a direct scalar positive-cone test is necessary and sufficient for the chosen roots. Existence of roots passing it is therefore a complete root-selection criterion for the original unrestricted problem, with zero, infinity, equal degree and all corners retained.
3. A finite ENDPOINT-PRODUCT inequality implies the test, with an explicit numerator. Its midpoint specialization defines a scale-invariant uniform structural class of original independent boxes, with arbitrary band locations and all seven widths allowed. It uses no frequency maximum, fixed example scale, hidden numerator search or machine certificate.

This does NOT prove that every robust box belongs to that class or admits successful root transport. The exact remaining obstruction is simultaneous cross-band gain control while roots move in the necessary admissible domain; a fixed-midpoint hybrid is already known insufficient. The active-root derivative identities in §7 identify the first unproved transport step rather than treating a projected zero as a full obstruction.

The accepted literal R/T box and its unrestricted numerator retain their scope. Parent `spr-unrestricted-box-kac-larger-blocks-parent-v1.md`, read completely, freshly observed SHA256 `6baba692f1e4e5fd76afa17cbe55ab3446f041989cd7a90e88e7fc2f3e558af3`, explicitly leaves general root selection open. That example is not a premise needed for the theorems below and is not extrapolated universally.

## 1. Original input and six ACTUAL root bands

Let

`K={a(s)=s^7+a_1s^6+...+a_7 : l_i<=a_i<=u_i}`,

with finite endpoints, degenerate intervals allowed, and every member strictly Hurwitz. All seven coefficient intervals remain the original independent ones. Write

`E_a(t)=-a_1t^3+a_3t^2-a_5t+a_7`,

`O_a(t)=-t^3+a_2t^2-a_4t+a_6`,

`P_(a,b)(t)=E_aE_b+tO_aO_b`.

All lower coefficients of a real monic Hurwitz polynomial are positive, hence `0<l_1<=u_1` and `l_7>0`. Let m_i,w_i be midpoint/half-width data and put

`E_0=E_mid`, `Q=O_mid`,

`R_E(t)=w_1t^3+w_3t^2+w_5t+w_7`,

`R_O(t)=w_2t^2+w_4t+w_6`.

At each t>=0 the ACTUAL component values independently fill `[E_0-R_E,E_0+R_E]` and `[Q-R_O,Q+R_O]`. No arbitrary rectangle is substituted for that actual linear image.

Recall the written root-band consequence, also re-derived here at its import boundary. Fixing Q and varying the independent even block, Hermite–Biehler gives three simple positive even roots; their ordered maps are continuous on a compact connected coefficient box. Their images are compact intervals I_Ej. The same holds for the odd block with midpoint E fixed. Every even choice combines with every odd choice in the original box, so their attained extrema strictly alternate:

`I_Ej=[a_j,b_j]`, `I_Oj=[c_j,d_j]`,

`0<a_1<=b_1<c_1<=d_1<a_2<=b_2<c_2<=d_2`

`             <a_3<=b_3<c_3<=d_3<infinity`.             (B)

Here a_j,b_j are ROOT-BAND endpoints, not the polynomial coefficients a_i. The full root ranges, not merely selected corner roots, are intended. Every actual denominator factors as

`E_a(t)=-a_1 product_j(t-r_j)`, `r_j in I_Ej`,

`O_a(t)=-product_j(t-s_j)`, `s_j in I_Oj`.

Correlations among the roots of each actual component are not discarded: bounds below hold for every actual root tuple and do not declare the larger free-root family an independent coefficient box.

Named classical imports are degree-seven Hermite–Biehler, continuous dependence of ordered simple roots, monic root continuity, compactness and elementary factor inequalities. No sextic theorem, numerical root isolation or global SPR theorem is assumed.

## 2. A necessary unrestricted root-transport lemma

### 2.1 The numerator itself is Hurwitz

Let b be ANY common real exact-degree-seven strict SPR numerator. Its leading coefficient h is positive: h<0 eventually gives a negative leading t^7 pairing at finite frequencies, and h=0 violates exact degree. Divide by h, so b is monic.

Fix a monic Hurwitz a^0 in K and consider `a_lambda=(1-lambda)a^0+lambda b`. Its pairing with a^0 is

`(1-lambda)|a^0(iw)|^2+lambda P_(a^0,b)(w^2)>0`.

An imaginary-axis zero of a_lambda would make that pairing zero. The path has fixed monic degree and bounded coefficients, so roots cannot escape through infinity. Root continuity from a^0 proves b itself strictly Hurwitz. This includes frequency zero; no cancellation or harmonic-boundary waiver is used.

Thus write

`E_b=k e_p`, `e_p(t)=-product_j(t-p_j)`,

`O_b=o_q`, `o_q(t)=-product_j(t-q_j)`,

where k>0, all six roots are positive and simple, and

`p_1<q_1<p_2<q_2<p_3<q_3`.                            (N-HB)

This represents every admissible monic numerator, not a chosen low-dimensional profile.

### 2.2 Opposite-parity bands cannot be crossed

At EVERY actual even-component zero t in I_Ej, the denominator has a nonzero odd component. Its pairing with b is `t O_a(t)o_q(t)>0`, so o_q has the same strict sign as O_a there. At EVERY actual odd-component zero t in I_Oj, `E_a(t)e_p(t)>0`, so e_p has the same strict sign as E_a there.

Consequently the numerator roots obey

`0<p_1<c_1`, `d_1<p_2<c_2`, `d_2<p_3<c_3`,

`b_1<q_1<a_2`, `b_2<q_2<a_3`, `b_3<q_3<infinity`,

as well as N-HB. Strictness matters at every attained band endpoint.

Define the six transported hulls

`J_Ej=conv(I_Ej union {p_j})`,

`J_Oj=conv(I_Oj union {q_j})`.

The original inequalities B, the cross-band inequalities just derived, and N-HB together imply

`0< J_E1 < J_O1 < J_E2 < J_O2 < J_E3 < J_O3`,           (T)

where `J<J'` means `max J<min J'`.

For example `max(b_j,p_j)<min(c_j,q_j)` follows from all four cross comparisons; the next even band is handled identically. Thus T is NECESSARY for every unrestricted common numerator. Equivalently, positive pairing forces the mixed even/odd component polynomials E_a+sO_b and E_b+sO_a to have the appropriate HB root ordering for every actual a. This cross-stability is stronger than merely choosing six positive numerator roots.

Conversely any finite positive roots whose hulls satisfy T automatically satisfy N-HB and the strict opposite-band signs. Such a selection will be called ADMISSIBLE. The domain is nonempty (root-band midpoints are admissible), but the quantitative pairing condition below need not follow from T alone.

## 3. Exact positive-cone test for a chosen admissible root transport

Fix admissible p,q and define ACTUAL worst component products

`A_p(t)=e_p(t)E_0(t)-|e_p(t)|R_E(t)`,

`B_q(t)=t[o_q(t)Q(t)-|o_q(t)|R_O(t)]`.

For k>0, independence of the original parity blocks gives the exact identity

`min_(a in K) P_(a,b)(t)=k A_p(t)+B_q(t)`.             (MIN)

A minimizing actual coefficient corner exists at each t; this corner may vary with t but b never does.

The transported hulls have a load-bearing sign property. Outside all J_Ej, every factor t−p_j has the same sign as t−r_j for every actual even root r_j, so A_p>0. Similarly B_q>0 for positive t outside all J_Oj. In particular

`B_q>0 on union J_Ej`, `A_p>0 on union J_Oj`.

All possible negative contributions occur on the separated transported bands. At zero, A_p(0)>0 and B_q(0)=0. At infinity, B_q has leading t^7 coefficient one, while A_p has degree six and positive leading coefficient.

Define the finite exact gains

`G_E(p,q)=max_(t in union J_Ej) (-A_p(t))_+/B_q(t)`,

`G_O(p,q)=max_(t in union J_Oj) (-B_q(t))_+/A_p(t)`.

The denominators are strictly positive on these compact sets. No frequency optimization or arithmetic program is being executed by this definition.

### Theorem R — complete root-selection criterion

For these chosen roots, one common strict numerator exists exactly when

`G_E(p,q) G_O(p,q)<1`.                                (R)

It is precisely `b=k e_p(-s^2)+s o_q(-s^2)` with

`k>G_O`, `k G_E<1`, k>0.

If G_E>0 use `k=(G_O+1/G_E)/2`; if G_E=0 use `k=G_O+1`.

**Proof.** On the even transported bands, MIN is at least `(1-kG_E)B_q`; on the odd transported bands it is at least `(k-G_O)A_p`. Outside those bands both products are positive for t>0, and zero is covered directly. This proves the entire finite half-line. If a gain is positive its maximum is attained where its corresponding component is negative, so equality in either scalar restriction gives an actual corner pairing zero; the strict bounds are necessary. Leading coefficient one and compactification at infinity give a uniform positive weighted margin. Degenerate root-band widths and zero gains are covered by the printed alternatives.

Combining §2 with this theorem gives the GENERAL unrestricted equivalence:

> A common real exact-degree-seven strict SPR numerator for K exists IF AND ONLY IF there is an admissible six-root transport satisfying R.

This is a root-selection theorem with explicit geometric constraints and a scalar cone interval, not the old four-column separation alternative. It is not a proof that such roots always exist.

## 4. A finite ENDPOINT-PRODUCT certificate — no continuous frequency test

The exact gains can be conservatively bounded using only finitely many distances. For a compact interval J and point z define

`m(J,z)=min_(t in J)|t-z|`, `M(J,z)=max_(t in J)|t-z|`.

For an interval I use the corresponding minimum/maximum over t in J,r in I. Both are explicit endpoint expressions; m is the ordinary interval distance, zero only when intervals overlap. All m denominators below are positive by T.

Put

`Delta_Ej=max(|p_j-a_j|,|p_j-b_j|)`,

`Delta_Oj=max(|q_j-c_j|,|q_j-d_j|)`.

For J_Ej with left endpoint L_Ej define

`C_Ej = Delta_Ej^2 * product_(k!=j)[M(J_Ej,p_k) M(J_Ej,I_Ek)]`

`         / {4 L_Ej product_k[m(J_Ej,q_k) m(J_Ej,I_Ok)]}`.

For J_Oj with right endpoint R_Oj define

`C_Oj = R_Oj * Delta_Oj^2`

`         * product_(k!=j)[M(J_Oj,q_k) M(J_Oj,I_Ok)]`

`         / {4 product_k[m(J_Oj,p_k) m(J_Oj,I_Ek)]}`.

Then

`G_E<=u_1 max_j C_Ej`,

`G_O<=(1/l_1)max_j C_Oj`.                             (EP)

### Proof of the endpoint bound

On J_Ej, every other even factor pair has the same sign. A negative even product can therefore only come from `(t-p_j)(t-r_j)<0`. Its magnitude is at most `(p_j-r_j)^2/4<=Delta_Ej^2/4`. Multiply by a_1<=u_1 and the printed maximum bounds for all other factors. The odd product is positive, t>=L_Ej, and every odd factor distance has the printed positive lower bound. Division gives the first estimate. On J_Oj the same argument applies to the one potentially mismatched odd root factor, with t bounded by the right endpoint; the even product has leading factor at least l_1. This proves the second estimate.

Therefore the explicit finite inequality

`(u_1/l_1)(max_j C_Ej)(max_j C_Oj)<1`                  (CERT)

constructs a common numerator: substitute the upper gains from EP in Theorem R's k formula. This is a sufficient endpoint test, not a necessary condition for all root transports. Failure of CERT is not a negative verdict.

The intervals may be exact actual bands or any PROVED strictly alternating outer enclosures containing every actual root. Thus rational enclosing endpoints and rational selected roots give rational C-bounds, k, and numerator coefficients, with no numerical root approximations promoted to proof.

## 5. A uniform structural class with an explicit no-search numerator

A particularly transparent specialization chooses each p_j and q_j to be its actual band midpoint, so J_Ej=I_Ej and J_Oj=I_Oj. Let

`w_Ej=b_j-a_j`, `w_Oj=d_j-c_j`,

`D_Ejk=max_(r in I_Ej,s in I_Ek)|r-s|`,

`D_Ojk=max_(r in I_Oj,s in I_Ok)|r-s|`,

`g_jk=dist(I_Ej,I_Ok)>0`.

Define the completely explicit band-conditioning quantities

`B_E=max_j { w_Ej^2 product_(k!=j) D_Ejk^2`

`                      / [16 a_j product_k g_jk^2] }`,

`B_O=max_j { d_j w_Oj^2 product_(k!=j) D_Ojk^2`

`                      / [16 product_k g_kj^2] }`.

The ENDPOINT-ONLY class is

`(u_1/l_1) B_E B_O<1`.                                (BC)

**Uniform structural theorem.** EVERY original independent monic degree-seven box whose actual root bands (or proved outer bands) satisfy B and BC has a common monic degree-seven numerator with roots at these band midpoints and the explicit k from EP. All seven intervals may have positive width. No additional constraint on coefficient magnitudes, a named R/T family or a fixed numerator root is imposed.

Indeed midpoint selection gives Delta_Ej=w_Ej/2 and Delta_Oj=w_Oj/2. Every maximum distance to a selected midpoint is at most the maximum distance to its band, while each minimum distance is at least the interval gap. Substitution in CERT gives exactly BC.

This is a larger uniform STRUCTURAL class, rather than another fixed example: all six ordered band locations, widths and the finite leading-coefficient contrast are arbitrary subject to the stated endpoint inequality. It is invariant under common positive squared-frequency scaling: B_E scales inversely, B_O directly, and their product and u_1/l_1 do not change. It does not require small absolute coefficients or a neighbourhood of one prescribed R/T point. It is not asserted to contain every earlier sufficient class or the relocated-root example; admissible MOVING roots and CERT remain available when midpoint selection fails.

The proof retains the full original denominator box. No unproved independent choice of root tuples is declared to be its coefficient parameterization. The root estimates are uniform upper/lower bounds on all actual tuples, which is precisely what makes this structural class rigorous.

## 6. Every original acceptance quantifier is retained

For CERT or BC, the numerator is fixed once for the entire input box. MIN and the root estimates establish positivity for ALL a, equivalently every actual coefficient corner, and every finite t>=0. Zero has positive even product because all p_j>0 and l_7>0. The odd polynomial is monic with leading t^3 coefficient -1, so N has exact degree seven and its normalized pairing tends to one at infinity.

A positive uniform bound `mu(1+t)^7` follows by compactifying t and taking the positive minimum over the finitely many original corners. No numeric mu is invented. Denominator Hurwitzness is the original hypothesis or a separately proved HB root enclosure, never a cancellation assertion.

For NECESSITY in Theorem R, the common numerator's six roots and all transported hulls are finite and strictly separated. A limiting selection with q_3→infinity, a root→zero, or a transported gap collapsing is NOT itself a solution. An infimum of gain products below a threshold does not justify an unattained boundary selection without an actual admissible finite point. In particular no degree-six limiting numerator is silently substituted for the equal-degree target.

## 7. The first genuinely unproved root-transport step

The universal degree-seven question is now the following geometric one:

> For every ACTUAL robustly Hurwitz independent coefficient box, can six roots be placed so that the transported hulls T strictly alternate and the EXACT product R is less than one?

The endpoint class BC proves a uniform positive region, but no argument currently moves an arbitrary box into it. A midpoint failure, a failure of CERT, or even a failure of all roots in a restricted subcell is insufficient to refute unrestricted synthesis. The earlier actual box shows why roots must be permitted to leave their own uncertainty band while staying out of the opposite-parity bands.

There is a concrete cross-band tradeoff, not merely a generic dimensional projection gap. At fixed actual corner/sign and negative-product frequencies t_E,t_O, all factors are nonzero. For the corresponding individual gain product, written logarithmic derivatives are

`partial_(p_j) log(G_E G_O)=1/(t_O-p_j)-1/(t_E-p_j)`,

`partial_(q_j) log(G_E G_O)=1/(t_E-q_j)-1/(t_O-q_j)`.

These follow by differentiating the numerator root factors, keeping those frequencies and their active corner/sign fixed. They are NOT asserted to differentiate a nonsmooth maximum when several frequencies/corners tie. They show precisely why a relocation that improves one active even/odd pair can worsen another pair, or run into a transported-band endpoint.

**First missing lemma:** a global admissible root-transport or positive-cone argument controlling ALL active pairs at once, or an actual box on which every admissible transport is stalled with exact gain product at least one. Pairwise descent, one successful root move, a fixed1000 rule, or an abstract six-band pattern lacking original coefficient-box realizability does not establish either alternative.

If an actual all-transports obstruction were proved, Theorem R plus the already supported eight-coordinate alternative would imply a full positive eight-moment obstruction. No such box or obstruction is supplied here. Conversely a proof that the root domain always contains a successful point would solve universal SPR7; that proof remains absent.

## 8. Parkable disposition

Delivered: a necessary unrestricted cross-stability/root-transport lemma, a complete admissible-root positive-cone criterion, finite endpoint certificates, and a scale-invariant uniform band-conditioned class with explicit numerator selection. The exact general residual is the simultaneous root-transport step in §7. This is not an unrestricted solution, another R/T perturbation, a separation-only restatement or a new negative example.

Every statement is WRITTEN at the named classical imports, with no executed arithmetic. The new general criterion and structural class require complete separate supplied-proof reconstruction; prior support of the actual-box construction does not accept them automatically. All pinned sources, previous reviews and process errata are preserved. Novelty remains UNCLEAR; no formal/kernel/human/cross-vendor acceptance or scientific GO is claimed.
