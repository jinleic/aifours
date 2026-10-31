# SPR7 reciprocal W_II/W_III — complete positive-factor template and an exact contact-amplitude equation

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 05:22:28 PDT 2026**. Owner InfoSPR7/info-2. **NEW COMPLETE WRITTEN CONDITIONAL REPRESENTATION THEOREM CANDIDATE.** This is not an actual tuple, evaluated witness, feasibility/emptiness claim, universal SPR7 result or scientific GO.

All work uses SYMBOLIC variables and exact polynomial/integer-product identities only, even privately. No numerical parameter scout, decimal gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI or nested agent. All FOUR owner written-exactness findings, v18's symbolic-only breach and every parent history remain permanent with ZERO probe credit. No frozen source/review/gate is modified or its acceptance inherited.

## 0. Named inputs and scope

Use the complete current reciprocal packets:

- v11 `reciprocal-WII-WIII-pal-contact-height-wall-and-two-gap-v11.md`,257LF, SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8`;
- v12 `reciprocal-WII-WIII-finite-cubic-completion-v12.md`,169LF, SHA256 `14e5154b5b3647714e583e9b33a30775f713c1de6a5249b0c9359c892234a397`;
- v13 `reciprocal-WII-boundary-to-WI-and-WIII-cubic-branch-v13.md`,145LF, SHA256 `e6103a2e56026a394c721fa5c0342b334fda04023c30adf9954bd2e083b9cced`.

The current theorem supplies a SIMPLER exact positive-factor representation of v12's cubic condition, with its proof given below independently of the discriminant test. V13 is needed only when replacing W_II's boundary by W_I. Their v5/v9/v10+erratum assumptions and ordinary written assurance remain unchanged.

**Advance:** after the two selected nonpal contacts, the entire frequency-positivity condition can be built into one septic factorization with THREE residual positive parameters. The ONLY extra positive contact is visible as a single parameter face. The constant-coefficient equation has an exact positive square root giving a simple height-amplitude balance. No hidden continuum or numerical positivity test remains.

## 1. A complete positive-factor form for every monic nonnegative cubic

**Lemma.** A real monic cubic Q with Q(0)>0 is nonnegative on[0,infinity) IFF there exist

`alpha>0`, `h>0`, `lambda>=0`

such that

`Q(v)=(v+alpha)[(v-h)^2+lambda v]`. (PF)

Equivalently its coefficients satisfy

`c2=alpha+lambda-2h`,

`c1=h^2+alpha(lambda-2h)`,

`c0=alpha h^2`.

Q is STRICTLY positive on[0,infinity) IFF such a representation has lambda>0. If lambda=0, its ONLY positive zero is h, with multiplicity TWO.

**Necessity, complete proof.** Since Q(0)>0 and Q(v)→minus infinity as v→minus infinity, Q has at least one negative real root -alpha, alpha>0. Factor it over the reals as

`Q(v)=(v+alpha)(v^2+beta v+gamma)`.

Its constant gives gamma=Q(0)/alpha>0. Because v+alpha>0 on the positive half-line, the quadratic is nonnegative there. Put h=sqrt(gamma)>0. Evaluating that quadratic at the POSITIVE symbolic point v=h gives

`h^2+beta h+gamma=h(beta+2h)>=0`.

Thus lambda:=beta+2h>=0, and the quadratic is exactly(v-h)^2+lambda v. This proves (PF). No root was approximated or parameter instance tried: alpha is an existential real root supplied by the ordinary intermediate value theorem.

**Sufficiency.** For v>=0 both factors in(PF) are nonnegative and v+alpha>0. If lambda>0, the bracket is strictly positive: at0 it is h^2>0, and for v>0 the term lambda v>0. If lambda=0 it vanishes exactly at h and is otherwise positive. Conversely strict Q forbids lambda=0 in ANY representation, proving the strict equivalence.

This lemma exhausts ALL cubic coefficient/discriminant branches. Complex conjugate roots and three negative real roots are included; no real-rootedness or sign of c1/c2 is assumed.

## 2. Complete septic template for W_II/W_III

Retain v11's strict target T, pal contacts a,b, positive heights l,m, original center/width inverse and exact C1 height wall. Define its monic septic determinant

`R=(v+4)Phi^2-vK^2=(v+4)phi1phi3+4A H`,

with `phi1=(v-a)^2(v+l)`, `phi3=(v-b)^2(v+m)` and physical positive widths. Choose the two DISTINCT positive nonpal v-contacts r,s in their required gaps.

Then the ENTIRE nonpal frequency positivity, with the selected double contacts, is equivalent to the polynomial IDENTITY

`R(v)=(v-r)^2(v-s)^2(v+alpha)[(v-h)^2+lambda v]`,

`alpha>0`, `h>0`, `lambda>=0`. (SEPTIC)

**Proof.** Whole positivity makes every selected interior zero at least double, so the quartic divides R. Its quotient is a real monic cubic Q. R(0)=4Phi(0)^2>0 gives Q(0)>0. By continuity after dividing away the nonnegative square factors, Q>=0 on the half-line. Apply Section1. Conversely(SEPTIC) is visibly nonnegative for EVERY v>=0, not just at the selected roots, and supplies their double factors. This is exactly v12's factorization/positivity equivalence, now with positivity built in rather than decided by a Boolean discriminant test.

(SEPTIC) is a FINITE coefficient-matching system. It can be written as the three explicit c2,c1,c0 equations in Section1 plus v12's FOUR remainder equations, with no polynomial-division program. All original input widths/correlations and admission/orientation conditions are still those of v11; an arbitrary positive septic is not automatically an original box.

## 3. ALL extra contacts lie on one visible face

If lambda>0, the complete determinant's only positive zeros are the selected r,s, each with its displayed multiplicity. If lambda=0, there is exactly ONE additional candidate h, double, unless it coincides with a selected root and increases its multiplicity. This is the entire zero set, not a generic claim.

- Check actual nonzero amplitudes at r,s.
- On lambda=0 ONLY, also check the actual minimizing-corner amplitude at h; coincident checks are identical, not discarded.
- V11's positivity off the two phase gaps forces h, if present, into one of them. Target-component-zero and reciprocal endpoint margins remain automatic.

Thus the original EVERY-zero admission condition is exhaustive and finite in this template. All selected lead/lag signs remain required; no sign condition is imposed on an extra contact except its actual nonzero amplitude.

**Independent W_II contribution.** V13's GLOBAL C2 slot bound shows a W_II extra h cannot be in the inner gap, including coincidence with a selected C2 root. It must be outer C4, and the SAME point then belongs to W_I. Therefore, in the union problem, W_II can be replaced by the branch **lambda>0**, with lambda=0 already covered by W_I. This is not a W_I emptiness proof or a discarded boundary.

**W_III.** Its geometry gives

`alpha+lambda-2h=c2=l+m+4+2(r+s-a-b)>l+m+4>0`.

Hence the positive-factor data necessarily satisfy

`alpha+lambda>2h+l+m+4`.

On its extra-contact face lambda=0 this requires alpha>2h+l+m+4. This is exact, but not asserted inconsistent.

## 4. A positive amplitude balance from the constant coefficient

Since phi1(0)=a^2l and phi3(0)=b^2m,

`R(0)=4Phi(0)^2=(a^2l+b^2m)^2`.

Comparing with(SEPTIC) gives

`alpha h^2 r^2 s^2=(a^2l+b^2m)^2`.

Introduce z>0 with alpha=z^2. ALL factors are positive, so this is EXACTLY equivalent to the UNSQUARED equation

`z h r s=a^2l+b^2m`. (BAL)

No spurious sign branch is allowed. Replacing alpha by z^2 loses no positive alpha and adds no numerical approximation.

The width inverse also gives `2fL=a^2l-b^2m`, where L=w1+w2+w3>0. Together:

`a^2l=(zhrs+2fL)/2`,

`b^2m=(zhrs-2fL)/2`.

Positive l,m are therefore equivalent, at L>0, to the single strict amplitude surplus

`zhrs>2fL`,

with the two displayed positive-height formulas. This can eliminate BOTH pal heights if one instead uses L as a width-scale variable and retains the remaining original width equations. No center/width coordinate is silently independent: all v11 equations must still hold.

The v^6 coefficient gives the second low-cost exact match

`z^2+lambda-2h=l+m+4+2(r+s-a-b)`. (TOP)

Thus the two end-coefficient conditions already impose(BAL)/(TOP), rather than an unchecked spectral-factor choice. The other coefficient equations remain genuine and are NOT solved by those two identities alone.

## 5. Full finite alternatives and exact remaining gap

For either word, retain the WHOLE v11 reconstruction:

- d,e,f>0,de>f and actual phase roots;
- a in(rho2,rho3), b in(0,rho1);
- physical positive-width cone/center map and strict C1 height-wall side;
- selected nonpal gap positions and alternating exact amplitudes;
- (SEPTIC), or its explicit coefficient equations with z,h>0,lambda>=0;
- nonzero amplitudes at the selected roots and, ONLY on lambda=0, at h.

This is equivalent to the full W_II/W_III systems, not merely necessary conditions. A complete point would admit an actual original independent reciprocal box by v11 and provide an unrestricted numerator obstruction through the named v5/v10 positive-kernel theorem. No point has been delivered. For the full union, v13 permits lambda>0 for the independent W_II branch; W_I remains a separate live alternative. Converse reduction from an arbitrary negative reciprocal input still names v5 first-critical and v9 weak-quadratic transfer.

**Next exact representation:** solve or exclude the positive-factor coefficient system, especially the simultaneous(BAL), (TOP), height wall and positive-width cone. The former continuum positivity has been replaced by explicit squares and positive factors. Producing a numerical/rational tuple or a computed elimination certificate would be scientific execution requiring a separate named GO; none is requested or performed here. Written symbolic elimination remains permitted.

Original universal SPR7, the general nonreciprocal case, and feasibility/emptiness of the reciprocal alternatives remain OPEN. No formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/novelty or parent acceptance, source cutover, nineteenth owner, deadline reset or round closeout. Original science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and actual-clock substantive cadence remain binding; work remains active.
