# SPR7 reciprocal W_II/W_III — finite cubic completion removes the remaining frequency quantifiers

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 05:08:25 PDT 2026**. Owner InfoSPR7/info-2. **NEW COMPLETE WRITTEN CONDITIONAL THEOREM/REPRESENTATION CANDIDATE.** No original counterexample or emptiness is claimed. This is a NEW source, not an edit or retrospective insertion into any frozen gate.

Only SYMBOLIC variables, exact fractions and integer-product identities are used, including privately. No numerical parameter trial, approximate gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. All FOUR owner exactness findings, v18's stricter symbolic-only breach and all parent histories remain permanent; withdrawn probes receive ZERO credit.

## 0. Exact import and new advance

The operative new import is the COMPLETE257LF packet `reciprocal-WII-WIII-pal-contact-height-wall-and-two-gap-v11.md`, SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8`. Its named v5/v9/v10+erratum interfaces remain as stated there: positive four-contact dual/admission, and converse first-critical/weak-quadratic reduction. None is promoted by this successor. The even/odd-profile failures remain qualified ancestry, not an unrestricted verdict.

In v11, after choosing target T, two pal-contact locations and heights, the only nonpalindromic global requirements were:

- R(v)>=0 on the TWO negative-A gaps;
- the appropriate actual corner amplitude is nonzero at EVERY zero of R.

**New theorem.** Once the two DISTINCT selected nonpalindromic contacts of W_II or W_III are included, BOTH requirements have an explicit FINITE algebraic test. The remaining quotient is a monic cubic with positive constant. Its half-line nonnegativity is decided by rational polynomial inequalities, and it has at most ONE additional positive zero, whose exact amplitude is checked. No frequency grid, numerical minimum, quantifier over a continuum, generic-rank assumption or no-extra-contact hypothesis remains.

This does not decide whether the resulting finite semialgebraic system has a point. It is an exact representation theorem, not an executed elimination/SAT certificate.

## 1. Data carried exactly from v11

Use d,e,f>0, D=de-f>0, the target T=z^3+d z^2+e z+f, and its phase cubic A with roots

`0<rho1<f/d<rho2<e<rho3`.

Choose a in(rho2,rho3), b in(0,rho1), l,m>0 and set

`phi1=(v-a)^2(v+l)`, `phi3=(v-b)^2(v+m)`.

Recover the ORIGINAL paired independent intervals by v11's exact center/width inverse. Retain its positive-width cone, the appropriate strict C1 height-wall side, and the exact amplitudes kappa_+(v),kappa_-(v). All original constants, degree7, reciprocal coefficient correlations and nonzero target components are retained.

The determinant is the EXPLICIT monic septic

`R(v)=(v+4)Phi(v)^2-vK(v)^2`

`    =(v+4)phi1(v)phi3(v)+4A(v)H(v)`,

where Phi=(phi1+phi3)/2 and H is the physical positive width quadratic. It is monic because Phi is monic cubic and K has degree<=2. Its constant is

`R0=R(0)=4Phi(0)^2>0`.

By v11, R is STRICTLY positive everywhere outside the two open gaps (rho1,rho2) and(rho3,infinity). The pal-corner amplitudes/strict stability and the target-component-zero margins are already handled there.

## 2. Exact two-contact factor test

Let r,s be the two DISTINCT positive selected contacts in the v-variable, not the old t-frequency labels. Put

`S=r+s`, `P=rs`,

`D4(v)=(v-r)^2(v-s)^2`

`     =v^4-2S v^3+(S^2+2P)v^2-2PSv+P^2`.

Write the explicit determinant coefficients as

`R(v)=v^7+R6 v^6+R5 v^5+R4 v^4+R3 v^3+R2 v^2+R1 v+R0`.

Define the monic cubic Q(v)=v^3+c2 v^2+c1 v+c0 by

`c2=R6+2S`,

`c1=R5+2S c2-(S^2+2P)`,

`c0=R4+2S c1-(S^2+2P)c2+2PS`.

Then R=D4 Q IFF the following FOUR explicit remainder equations hold:

`R3=-2S c0+(S^2+2P)c1-2PS c2+P^2`,

`R2=(S^2+2P)c0-2PS c1+P^2 c2`,

`R1=-2PS c0+P^2 c1`,

`R0=P^2 c0`. (REM)

**Proof.** Multiply the displayed quartic and cubic. The first three formulas match coefficients of v^6,v^5,v^4; the four equations match all remaining coefficients. No polynomial-division executable is invoked.

Because r,s>0 and R0>0, (REM) forces c0=R0/P^2>0. Since the contacts are distinct, (REM) is also equivalent to R(r)=R'(r)=R(s)=R'(s)=0. It imposes AT LEAST double zeros, not exactly double. A higher-order selected contact is retained.

Since D4>=0 and is strictly positive away from r,s, the equivalence

`R>=0 on [0,infinity) IFF Q>=0 on [0,infinity)` (QEQ)

follows by continuity even at the selected zeros. Using v11's automatic positivity off the gaps, this is equivalent to its ENTIRE two-gap inequality (GAPS).

## 3. Quantifier-free half-line test for the cubic

Let Q=v^3+c2v^2+c1v+c0 with c0>0. Put

`Delta=c2^2-3c1`, `E=2c2^3-9c2c1+27c0`.

Define the ACTIVE-minimum condition

`Delta>0 AND (c2<0 OR c1<0)`.

Then Q>=0 on [0,infinity) IFF:

- the ACTIVE condition is FALSE; OR
- the ACTIVE condition is TRUE and `E>=0 AND E^2>=4Delta^3`. (CUB)

These are finite rational POLYNOMIAL inequalities in the cubic coefficients; no square root evaluation is required for the positivity test.

**Proof.** Q'=3v^2+2c2v+c1. If Delta<=0 it is nonnegative everywhere, so Q is nondecreasing on the positive half-line and Q(0)>0. If Delta>0, its local minimum is at

`zeta=(-c2+sqrt(Delta))/3`.

It is positive EXACTLY when c2<0 or c1<0. If not positive, Q has no positive local minimum and again stays above its positive value at0. If positive, the only possible negative global minimum on the half-line is at zeta. With y=v+c2/3,

`Q=y^3-(Delta/3)y+E/27`,

so

`Q(zeta)=(E-2Delta^(3/2))/27`.

For Delta>0 this is nonnegative iff E>=0 and E^2>=4Delta^3. A possible positive local MAXIMUM cannot yield an additional lower value; the endpoints are Q(0)>0 and Q(v)→infinity. This proves (CUB), including repeated-critical-point boundaries.

## 4. EVERY positive zero and all admission amplitudes — only one possible extra check

Under (CUB), Q is strictly positive on (0,infinity) EXCEPT in the single boundary case

`ACTIVE true`, `E>0`, `E^2=4Delta^3`.

In that case zeta=(-c2+sqrt(Delta))/3>0 is its ONLY positive zero, with multiplicity TWO, and

`Q(v)=(v-zeta)^2(v+eta)`, `eta=c0/zeta^2>0`.

**Proof.** A monic cubic nonnegative on the positive axis cannot have an odd-multiplicity positive root. Since c0>0 there is no zero at0. It therefore has at most one positive root, necessarily double. The calculus proof identifies precisely when that minimum is0. The remaining linear factor has positive constant by c0>0, and the displayed eta follows.

Consequently ALL positive R zeros are the two selected r,s and, only in that exact boundary case, zeta. If zeta equals a selected contact, the selected root simply has higher multiplicity; it is not discarded or double-counted as a new orbit.

The original admission condition from v11 is therefore FINITE:

1. Check kappa_sigma(r)!=0 and kappa_sigma(s)!=0 for their actual gap corners.
2. In the ACTIVE equality case only, check the appropriate kappa_sigma(zeta)!=0.

The extra zeta AUTOMATICALLY lies in one of the two negative-A gaps, because v11 gives R>0 outside them and at their boundaries. Thus its actual corner is unambiguously C2 on (rho1,rho2) and C4 on (rho3,infinity). No zero at a target component, frequency0/1/infinity or an unseen fourth positive orbit is possible.

The selected amplitudes have the prescribed lead/lag signs, stronger than their nonvanishing. The extra one needs only nonvanishing, not an invented orientation. The expression for zeta is an exact algebraic number, not a numerical approximation; alternatively introduce it as an auxiliary variable with 3zeta^2+2c2zeta+c1=0, Q(zeta)=0 and zeta>0 on that branch.

## 5. Complete finite W_II and W_III systems

Start with all v11 data/width inequalities and its strict C1 height-wall side. Then replace BOTH its universal-frequency conditions by (REM), (CUB) and the FINITE amplitude checks above. Select contact locations as follows:

- **W_II:** rho1<r<s<rho2, with kappa_+(r)<0 (C2 lead at the LATER t-frequency t(r)) and kappa_+(s)>0 (C2 lag at the EARLIER t-frequency t(s)). C1 is on the lead side. C3 is automatically lag.
- **W_III:** rho1<r<rho2 and rho3<s, with kappa_+(r)<0 (C2 lead) and kappa_-(s)<0 (C4 lead). C1 is on the lag side, requiring rho2<a<e and0<l<f(e-a)/(da-f); C3 is automatically lag.

The notation r,s here is v-ordered and explicitly differs from v10's t labels. In W_II it corresponds to old s=t(r), old r=t(s); in W_III old r=t(r), old d0=t(s). The reciprocal relation is strictly decreasing, so the four original contacts have exactly the required frequency order.

**Necessity.** Every actual W_II/W_III point provides these selected positive double contacts, so D4 divides R and (REM) holds. Global corner positivity gives Q>=0 and hence (CUB). Its whole-box strict Hurwitz property supplies every finite amplitude check, including an extra cubic zero if present.

**Sufficiency.** (REM)+(CUB) give R>=0 at EVERY frequency by (QEQ), not just the selected contacts or a finite grid. The finite amplitude checks exhaust ALL positive zeros. Therefore v11's entire admission argument proves EVERY member of the reconstructed original independent box is strictly Hurwitz. The selected contacts have the required nonzero amplitudes and alternating orientations. At the named v5/v10 positive-kernel interface they give a positive annihilation against EVERY unrestricted target numerator. Thus a point of either finite system would be an actual reciprocal counterexample, not just a profile failure.

Converse reduction from an arbitrary negative reciprocal input still additionally uses v5/v9 and retains W_I as a third alternative. No W_I elimination, actual point, feasible instance, emptiness, original universal conclusion, evaluated certificate or new GO is claimed.

## 6. Exact residual and next representation

The W_II/W_III questions are now literal FINITE semialgebraic feasibility questions:

- target d,e,f and the phase-root ordering;
- pal contacts a,b and heights l,m;
- the three positive-width inequalities;
- the exact C1 height-wall side;
- two selected nonpal contact locations and FOUR polynomial remainder equations;
- the explicit cubic Boolean inequality (CUB);
- nonzero amplitudes at two selected contacts and at most ONE additional exactly specified point.

No uncontrolled continuum inequality or unchecked extra contact is left. Square roots in xi or zeta can be retained algebraically by positive-root equations, preserving their exact branch. Producing a point or an emptiness identity is STILL missing. An SOS/real-algebraic certificate, or a new written elimination of these explicit equations, is the next representation; no such computational generation/replay is authorized or performed under HOLD.

All named imports and original targets retain their assurance. This is WRITTEN, not formal/kernel, human, configured-family/cross-vendor, executable/triple-finite, novelty or parent acceptance. All frozen gates/sources and process histories are unchanged. Same original18 owners, science cutoff2026-10-27T11:05:38-07:00 and deadline12:35:38 remain; no park/turn-end is justified merely by a pending review.
