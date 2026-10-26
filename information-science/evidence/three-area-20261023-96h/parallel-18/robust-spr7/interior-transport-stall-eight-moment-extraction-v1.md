# Universal SPR7 route — an interior transported-root stall can produce an ACTUAL full eight-moment obstruction

Actual `/bin/date` observation before this paper: **Sun Oct 25 09:45:15 PDT 2026**. InfoSPR7 / info-2. **NEW WRITTEN CONDITIONAL THEOREM CANDIDATE**, pending complete separate reconstruction. No scientific interpreter/eval/program, symbolic computation, enumeration, sampling, optimization run or replay was used. Source/clock/hash metadata only. HOLD/v9/v10 remain binding. No literal obstructing box or stationary point is claimed found.

## 0. New direction and precise result

The preceding actual-box examples and four-column obstructions are NOT being repeated. This paper addresses the FULL unrestricted eight-coordinate cone at the SAME original independent coefficient box.

**Conditional extraction theorem.** Suppose an admissible finite six-root transport is a local minimum of `log(G_E G_O)` in the FULL open admissible six-root domain, its gain product is at least one, and all three selected EVEN roots lie in their own ACTUAL even uncertainty bands. Then an explicit positive linear combination of ACTUAL member/frequency vectors annihilates ALL EIGHT numerator coefficients. It can be converted to at most NINE ACTUAL Kharitonov-corner/frequency atoms. Consequently this would prove that this SAME box has NO unrestricted common degree-seven SPR numerator.

The key new step is not a projected-zero claim: the root-stationarity equations first kill all four even moments and leave a precisely identified odd residual. Original coefficient-block independence supplies realizable ZERO-EVEN correction atoms that cancel that residual with positive weights. When the even roots leave their actual bands, this completion is no longer automatic; the exact missing cone-realizability step is retained in §8.

No example satisfying the bad-stall hypotheses is supplied. The theorem therefore does NOT refute universal SPR7. It provides a certificate-producing same-box obstruction route, not an assertion that every bad fixed profile or every constrained root optimum is an unrestricted obstruction.

## 1. Inputs and original quantifiers

Let K be an arbitrary compact robustly Hurwitz ORIGINAL independent monic degree-seven coefficient box. Degenerate intervals are allowed, but the theorem's positive gains may themselves exclude some degenerate cases. Let I_Ej,I_Oj be its six actual root bands. Use the accepted real root-transport theorem at its exact scope, read with all author qualifications:

- `general-seven-band-root-transport-certificate-v1.md`, SHA256 `b064261dae70f2dc0dc53317a7d99d6e38fe5e5885f7f4db8cf16ac418eb3dfb`;
- `root-transport-v56-rationality-and-leading-sign-addendum-v1.md`, SHA256 `b1358582f7be557e1e912bd944692411a1b834f1063ba6401a04d7f9df881a50`;
- the parent root-transport disposition and its additive correction, retaining the historical0F/0M/2MINOR finding record.

The newer Vieta/sharp-class paper and its actual v66-C review are NOT needed as accepted premises here. Its scope is now immutably clarified by `vieta-sharp-v66-scope-addendum-v1.md`: SCERT contains CERT; SBC strictly contains BC; strict existential all-transports CERT enlargement is not established. That separate history does not upgrade this new extraction theorem.

For a finite admissible transport put

`e(t)=-product_(j=1)^3(t-p_j)`,

`o(t)=-product_(j=1)^3(t-q_j)`.

The odd component has degree three and leading coefficient -1. All roots are positive/simple and their transported hulls strictly alternate. A common monic numerator with these roots would be `k e(-s^2)+s o(-s^2)`, k>0. Define the original-box exact worst products

`A(t)=min_(a in K) e(t)E_a(t)`,

`B(t)=min_(a in K) t o(t)O_a(t)`.

The original even/odd coefficient blocks are independent; each minimum is attained by its actual pointwise extreme component corner. The four combinations of E_-/E_+ and O_-/O_+ are ACTUAL coefficient corners. Thus an actual minimizing member can be selected for either ratio below.

Let

`a=G_E=max_(even transported hulls) (-A)_+/B`,

`b=G_O=max_(odd transported hulls) (-B)_+/A`.

In this paper a,b are GAIN values, not denominator coefficients. Assume a>0,b>0 and ab>=1. An even active atom has a frequency t_e and an actual minimizing corner with values

`A_e=e(t_e)E_e(t_e)<0`, `B_e=t_e o(t_e)O_e(t_e)>0`,

`-A_e/B_e=a`.

An odd active atom has

`A_o=e(t_o)E_o(t_o)>0`, `B_o=t_o o(t_o)O_o(t_o)<0`,

`-B_o/A_o=b`.

All such frequencies are positive and finite. Every component factor printed in a denominator is nonzero there. Repeated active frequencies/corners may be combined when appropriate.

The classical new imports are finite-dimensional strict separation/Caratheodory and the elementary compact active-gradient necessary condition proved in §3. There is no assumed invariant form, numerical optimizer or evaluated stationary configuration. All weights below are real; rationality is NOT inferred from rational input data.

## 2. The stationarity identities needed for extraction

The elementary extraction in §§4–5 only requires finite probability weights mu_E on even active atoms and mu_O on odd active atoms, each summing to one, satisfying for EVERY real polynomial z of degree at most three

`sum_E mu_e z(t_e)/e(t_e)=sum_O mu_o z(t_o)/e(t_o)`,    (SE)

`sum_E mu_e z(t_e)/o(t_e)=sum_O mu_o z(t_o)/o(t_o)`.    (SO)

These are two full FOUR-dimensional polynomial identities, not one scalar condition per profile. They need not hold at a generic bad root selection; stationarity is a genuine additional hypothesis.

The next section proves that a local minimum in the FULL admissible root domain supplies such finite measures, including ties among frequencies or corners. After that proof, extraction is purely algebraic and uses original-box realizability.

## 3. Why an unconstrained interior root minimum supplies SE/SO

### 3.1 Fixed compact guards and smooth active branches

Strict transported-hull separation permits six slightly larger, still strictly separated guard intervals containing every hull for all sufficiently small root perturbations. On each even guard, o and every actual odd component have the same nonzero sign; on each odd guard, e and every actual even component have the same nonzero sign. Thus the gains can locally be written as maxima over FIXED compact frequency guards and the four actual extreme-component corners:

`g_e=(-e E_corner)/(t o O_corner)` where this is positive,

`g_o=(-t o O_corner)/(e E_corner)` where this is positive.

Outside the corresponding moving negative-support hull, the positive part is zero. The guard formulation therefore has the same positive maximum. Since a,b>0, all active branches stay away from zero numerator/denominator factors; only a compact neighbourhood of those positive active branches matters locally. Their root derivatives are continuous. No derivative of a moving maximizing frequency is taken.

### 3.2 The compact active-gradient condition

Let theta=(p_1,p_2,p_3,q_1,q_2,q_3). The objective is the maximum, over an even and an odd active-branch pair, of `log g_e(theta)+log g_o(theta)`. At a local minimum in the FULL open admissible domain, zero belongs to the convex hull of the SIX-dimensional gradients of its active pairs.

Here is the necessary-condition proof. If zero were outside that compact convex hull, strict separation would give a direction with uniformly negative dot product against every active gradient. Compactness and continuity make the same inequality hold on all sufficiently near-active branches. Branches with a fixed strict gap below the maximum cannot overtake it under a sufficiently small perturbation. A small step in that direction would then decrease the whole maximum, contradicting local minimality. This argument treats tied maximizers, not only a smooth unique active pair.

Caratheodory in R^6 gives a finite probability combination of at most seven active PAIRS with zero average gradient. Its two marginals are finite probabilities mu_E,mu_O. No such weights are computed here; their existence is the written necessary condition.

### 3.3 Root derivatives give ALL cubic variations

For an active pair the derivative in an even root is

`1/(t_o-p_j)-1/(t_e-p_j)`,

and in an odd root is

`1/(t_e-q_j)-1/(t_o-q_j)`.

Equivalently, for a variation delta e it is `delta e(t_e)/e(t_e)-delta e(t_o)/e(t_o)`, and for delta o the reversed analogous expression. The three derivatives of e with respect to its distinct roots, `-e/(t-p_j)`, form a basis of quadratics: their evaluations at the three p_j are diagonal and nonzero. The same holds for o. Hence the zero average gradient proves SE/SO for all quadratics.

The remaining cubic direction follows from the probability normalizations. Substituting z=e in SE gives1=1; quadratics together with the degree-three e span all cubics. Substituting z=o does the same for SO. Thus SE and SO hold for EVERY cubic, including the leading-coefficient directions. No eighth-coordinate/infinity condition has been discarded by fixing the root-polynomial leading coefficients during differentiation.

This proof would NOT apply to a root optimum constrained to a face unless the FULL six-root stationarity identities are independently established. In particular a one-sided boundary optimum of p_j in I_Ej is not automatically an unconstrained stationary point.

## 4. First positive weights: all EVEN moments vanish, ODD residual is explicit

Assume SE/SO. Give the original even active atoms raw weights

`nu_e=-mu_e/A_e>0`,

and the odd active atoms raw weights

`nu_o=mu_o/A_o>0`.

For ANY cubic z, their even-coordinate functional is

`sum_E nu_e E_e(t_e)z(t_e)+sum_O nu_o E_o(t_o)z(t_o)`

` =-sum_E mu_e z(t_e)/e(t_e)`

`      +sum_O mu_o z(t_o)/e(t_o)=0` by SE.

Thus ALL FOUR even moments vanish already.

For the odd functional, the active ratios imply

`-B_e/A_e=1/a`, `B_o/A_o=-b`.

Consequently its value on ANY cubic z is

`(1/a)sum_E mu_e z(t_e)/o(t_e)`

`      -b sum_O mu_o z(t_o)/o(t_o)`

` =(1/a-b)H(z)`,                                      (RES)

where the COMMON functional H is the two sides of SO. This is the full remaining odd residual, not a claim that projected stationarity already annihilates eight coordinates.

If ab=1, RES vanishes and the positive original active atoms are already a full eight-coordinate zero balance. If ab>1, its coefficient is NEGATIVE; §5 constructs an actual positive correction rather than cancelling it with an unjustified signed or abstract atom.

## 5. Original-box zero-EVEN correction cancels ALL FOUR odd moments

Now assume every p_j lies in its ACTUAL even root band I_Ej. Then each even transported hull equals that actual band. Every even active frequency t_e belongs to the actual zero-attainability set of the even component.

At that frequency E_-(t_e)<=0<=E_+(t_e), with `E_+-E_->0` because A_e<0 rules out a common zero extreme. Define

`theta_e=E_+(t_e)/(E_+(t_e)-E_-(t_e))`,

`E_e^0=theta_e E_-+(1-theta_e)E_+`.

This is an ACTUAL even coefficient choice with `E_e^0(t_e)=0` and 0<=theta_e<=1. Retain the actual odd component O_e of its even active corner. ORIGINAL parity-block independence gives a genuine denominator a_e^0 in the SAME box. No arbitrary mixed root tuple or merely feasible frequency rectangle is being called a denominator.

Admissibility makes `t_e O_e(t_e)o(t_e)>0` throughout these even bands. If `c=b-1/a>=0`, add the ACTUAL zero-even member/frequency atom with raw weight

`nu_e^0=c mu_e/[t_e O_e(t_e)o(t_e)]>=0`.                (CORR)

Omit it when c=0. It contributes zero to every even moment and contributes

`c sum_E mu_e z(t_e)/o(t_e)=c H(z)`

to the odd functional. This cancels RES EXACTLY. The total raw functional therefore annihilates

`E_a z_E(t)+t O_a z_O(t)`

for EVERY pair of independent cubics z_E,z_O. That is ALL EIGHT numerator coefficients, not only F,D_Q,H,Q or a single fixed even component.

Each a_e^0 is itself a convex combination of TWO actual Kharitonov corners, using the same O_e and E_-/E_+. Replacing this correction by those two positive corner atoms preserves the functional. Thus all atoms can be actual coefficient corners of the original seven-interval box; no shared/source geometry has been enlarged.

The case ab>1 is why the proper-even-band condition matters. If p_j lies outside I_Ej, some even active frequency may not admit any original E_a(t)=0. The formula CORR would then have no guaranteed actual member. The theorem does NOT silently apply there.

## 6. Compactification, at-most-NINE atoms and unrestricted exclusion

Use the full coefficient order

`(e_0,e_1,e_2,e_3; o_0,o_1,o_2,o_3)`

with the alternating t basis. The eight zero equations proved above are

`sum_i nu_i (-1)^j t_i^j E_(a_i)(t_i)=0`,

`sum_i nu_i (-1)^j t_i^(j+1) O_(a_i)(t_i)=0`, j=0,1,2,3.

All initial atoms have 0<t_i<infinity. Define their compactified weights by

`lambda_i=nu_i(1+t_i)^7 / sum_k nu_k(1+t_k)^7`.

They are nonnegative, have total one, and give EXACTLY a zero convex combination of the full eight-coordinate W_8 vectors. Every finite factor is positive. After corner expansion the set is finite, so ambient Caratheodory reduces it to at most nine ACTUAL corner/frequency atoms selected from that set. No numerical reduction or actual atom list is claimed to have been evaluated.

Any real numerator of degree at most seven with positive pairing against every actual member at all finite frequencies would have a positive dot product with every atom, contradicting that positive zero balance. In particular no unrestricted real EXACT-degree-seven common SPR numerator exists. Denominators are already assumed strictly Hurwitz. No cancellation or degree-drop inference is involved.

Zero and infinity remain part of the original acceptance criterion; this conditional NEGATIVE certificate happens to use only positive finite frequencies. It does not need to omit any original constraint to be valid. All eight polynomial coordinates, including the leading odd coordinate, were annihilated explicitly.

## 7. Conditional theorem and no-spurious-stall consequence

Combining §§2–6 proves:

> For EVERY actual robustly Hurwitz independent monic septic box, any finite full-domain local minimum with G_EG_O>=1 and all selected even roots in their actual even bands produces a positive full eight-coordinate obstruction on the SAME box.

The elementary extraction only needs SE/SO, so an exactly supplied stationary active-pair balance satisfying those identities is enough even without separately proving a local minimum. A generic bad root choice is NOT enough.

Contrapositively, a box already known to possess an unrestricted common numerator cannot have such a bad unconstrained interior local minimum in this proper-even sector. The compact active-gradient argument then supplies a common decreasing direction against all tied active pairs whenever its product is at least one. This is a landscape/certificate statement, not an assumption that the desired numerator exists for every box.

The previous accepted R/T box is only a correctness/scope control for that contrapositive; no new constant or sample on it is being proposed.

## 8. Entire exact residual and next genuinely missing bridge

Still NOT established:

1. An actual box and finite root configuration satisfying the bad-stall hypotheses. No unrestricted counterexample follows without such an actual realization.
2. Existence/attainment of a suitable local minimum for every original box. Roots can approach0, transported gaps can collapse, q_3 can escape to infinity, or the even roots can leave their actual bands. None is an admissible degree-seven solution by a limiting waiver.
3. That restricting even roots to their actual bands loses no possible successful numerator. No root-clamping/compression theorem is assumed.
4. The full eight-coordinate correction when the even active frequencies lie outside actual even zero-attainability bands.

For the last case RES gives an exact new interface. It would suffice to represent H as a positive combination of the odd-coordinate functionals of ACTUAL zero-even members. Under p_j in I_Ej this representation is explicitly CORR at the active frequencies. Outside it, positive representation in that actual zero-even cone is a genuinely unproved moment-realizability problem; an arbitrary signed functional or projected balance is not a substitute. This is a sufficient completion route, not asserted necessary for all possible obstructions.

The original universal problem therefore remains: either find a successful admissible transport for every realizable box, or realize an actual full obstruction. This theorem gives a SAME-BOX route from an interior local stall to the latter, with every coordinate and correction realized, rather than another fixed-hybrid failure.

The dossier's existing H/J theory already gives critical eight-finite/seven-plus-infinity alternatives after a suitable contraction and a closed numerator. That is not repeated as a discovery. Here no contraction, pre-existing closed numerator, contact pairing or coprime critical numerator is assumed; stationarity plus actual zero-even correction is the new conditional interface.

## 9. Assurance

Every new step is WRITTEN. The compact active-gradient argument, conversion from root variations to all cubic variations, sign of RES and actual CORR weights require fresh hostile reconstruction before parent support. No actual stationary weights or unrestricted-negative box have been produced. Rational input data do not by themselves make these active frequencies/weights rational; no finite executed certificate is claimed.

The preceding Vieta/sharp-class source and both author wording addenda remain unchanged, with their actual finding histories. V9/v10 are mandatory evidence overlays; no earlier computation gains verification credit. No formal/kernel/human/cross-vendor/novelty acceptance or new scientific GO is conferred. The original universal SPR7 quantifiers, cutoff and deadline remain unchanged.
