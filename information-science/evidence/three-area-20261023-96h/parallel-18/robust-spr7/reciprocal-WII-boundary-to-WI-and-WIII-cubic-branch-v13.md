# SPR7 reciprocal refinement — GLOBAL C2 multiplicity bound, W_II boundary reduces to W_I, and the W_III cubic discriminant branch

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 05:17:06 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN CONDITIONAL THEOREM CANDIDATE**, not a point, emptiness proof or universal verdict. Frozen sources and pending reviews are unchanged. No scientific interpreter/eval/calculator/program/CAS, numerical trial/decimal gloss, enumeration, solver, replay, CLI, nested agent or GO; symbolic variables only even privately. All FOUR owner exactness/v18 findings and all other histories remain permanent/ZERO probe credit.

## 0. Exact inputs and advance

Read with the ENTIRE new packets:

- v11 `reciprocal-WII-WIII-pal-contact-height-wall-and-two-gap-v11.md`,257LF, SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8`;
- v12 `reciprocal-WII-WIII-finite-cubic-completion-v12.md`,169LF, SHA256 `14e5154b5b3647714e583e9b33a30775f713c1de6a5249b0c9359c892234a397`.

Their v5/v9/v10+erratum interfaces remain named and unpromoted here. The compact functional formula used in Section1 is reproduced directly from v5 (SHA256 `7a358b729dfff820eb18d8af9bd474e83592979f4a045ea212a09237bda7f70a`). This extends that source's selected-support width argument to the ENTIRE nonpalindromic zero set, with multiplicities; it is not claimed novel or independent of that ancestry.

**New consequences:**

1. EVERY physically positive-width weak reciprocal configuration has at most TWO C2 half-frequency double-root slots, including unselected contacts and repeated higher-multiplicity slots.
2. If a W_II point's residual cubic has a positive zero, that zero MUST be in the outer C4 gap. The SAME point then belongs to W_I. Thus the only part of W_II contributing beyond W_I has a strictly positive residual cubic and NO extra contact/admission check.
3. In W_III the residual cubic's quadratic coefficient is automatically greater than l+m+4>0. Its entire positivity test reduces to `c1>=0 OR Disc(Q)<=0`; only the branch c1<0 and Disc(Q)=0 has an extra positive contact.

These are exact reductions, not a global decision of any word set.

## 1. A GLOBAL multiplicity bound, not just a selected-word count

Use the strictly Hurwitz palindromic target T=z^3+d z^2+e z+f, d,e,f>0,de>f, physical widths w_i>0, and actual compact coordinate xi=(1-t)/(1+t). The nonpalindromic functional from v5 is

`Qxi(xi)=Fhat(xi)+Khat(xi)`,

`Fhat=delta^3 Phi(v)`, `Khat=xi delta^3 K(v)`,

`delta=1-xi^2`, `v=4xi^2/delta`.

Fhat is even, Qxi has degree<=7, Qxi(1)=Qxi(-1)=64, and the quadratic coefficient of K is

`k2=(d+1)w1+w2>0`.

The leading contribution to Khat is `16 k2 xi^5(1-xi^2)`; all lower K terms have at least a delta^2 factor. Hence

`Qxi'(1)+Qxi'(-1)=-64 k2<0`. (END)

This is a polynomial derivative identity, not a numerical endpoint evaluation. Fhat's evenness cancels its two derivative values.

Assume Qxi>=0 on [-1,1], as required by whole-box weak positivity. Every root in(0,1) has even multiplicity. Define the C2 slot count to be the SUM of half those multiplicities. If it were at least3, degree<=7 forces exactly three slots, and

`Qxi=product_(j=1)^3(xi-r_j)^2 (Lxi*xi+Mxi)`,

with 0<r_j<1 and repetitions allowed. Endpoints give

`Mxi+Lxi=64/product(1-r_j)^2`,

`Mxi-Lxi=64/product(1+r_j)^2`.

Every factor (1-r_j)^2 is strictly below (1+r_j)^2, so Lxi>0 and Mxi>Lxi. Logarithmic differentiation at the nonzero endpoints yields

`Qxi'(1)+Qxi'(-1)`

`=64[4 sum_j r_j/(1-r_j^2)+Lxi/(Mxi+Lxi)+Lxi/(Mxi-Lxi)]>0`.

This contradicts (END). Therefore the GLOBAL C2 slot count is at most TWO. A quadruple C2 contact already consumes two slots and cannot coexist with any distinct C2 double contact; the argument explicitly allows repeated factors and does not assume generic simple contacts or positive dual weights on every zero.

## 2. W_II residual-cubic boundary is ALREADY W_I

Use v11/v12 notation: a is the C1 palindromic contact in(rho2,rho3), b is the C3 contact in(0,rho1). W_II selects two DISTINCT inner-gap v-contacts r<s, both in(rho1,rho2), with C2 lead at r (later t) and lag at s (earlier t). Its determinant factors

`R(v)=(v-r)^2(v-s)^2 Q(v)`,

Q monic cubic with positive constant and Q>=0 on [0,infinity).

From v12, Q can have at most ONE positive zero, necessarily double, at the exact ACTIVE equality branch. Suppose it has such a zero zeta.

**It cannot be in the inner gap, including zeta=r or zeta=s.** In that gap, one nonpal factor is zero and the other is strictly positive because Phi>0. Thus the order of a zero of R equals the order of the actual minimizing C2 functional. The v↔positive-xi change of variables has nonzero derivative, and all compactification factors are positive there. Consequently an inner zeta supplies a THIRD positive-xi slot in Qxi, even when coincident with a selected contact. This contradicts Section1.

By v11, R is strictly positive outside the two gaps, including at their boundaries. Thus zeta MUST be in the outer gap(rho3,infinity), giving an actual C4 contact at t(zeta)<x1. Complete admission retains its nonzero amplitude. For Hurwitz denominators/target, the v10 unwrapped-phase rule forces this first-cell C4 contact to LEAD.

Now select, in increasing t-frequency order:

- this C4 lead;
- the existing C2 lag at t(s);
- the existing C2 lead at t(r);
- the existing C3 lag at t(b).

This is EXACTLY word I. All four original corner inequalities, actual interval widths, whole-box strict Hurwitz admission, component-zero margins and nonzero amplitudes were already true for the SAME point. W_I does NOT prohibit unselected C1 contacts. Therefore the point belongs to W_I as well.

**Conclusion:**

`W_II subset W_I union W_(II,strict)`,

where W_(II,strict) is the v11/v12 W_II system with Q(v)>0 on [0,infinity). The reverse containment needed for replacing the union is trivial, so

`W_I union W_II union W_III = W_I union W_(II,strict) union W_III`.

No W_I emptiness is inferred. This is a reduction of the part of W_II that can contribute independently, not an assertion that all W_II points disappear.

For W_(II,strict), v12's ACTIVE branch uses STRICT `E>0` and `E^2>4Delta^3`; outside the ACTIVE branch positivity is already strict. There are no extra positive Q roots, so only the TWO selected nonpal amplitudes need checking. The positive cubic boundary is not silently thrown away: it is covered by the SAME-data W_I branch above.

## 3. W_III's residual cubic has an automatically positive quadratic coefficient

In v12, the coefficient of v^6 in R is independent of K, because vK^2 has degree<=5. Since

`Phi=v^3+[(l+m)/2-a-b]v^2+...`,

we have

`R6=l+m-2(a+b)+4`.

For selected nonpal v-contacts r,s the quotient coefficient is c2=R6+2(r+s), so

`c2=l+m+4+2[(r+s)-(a+b)]`. (C2)

In W_III, rho1<r<rho2 and s>rho3, while b<rho1 and a<rho3. Thus r>b and s>a. Therefore

`c2>l+m+4>0`.

This is a strict all-parameter consequence of the actual word geometry, with no numerical contact range or asymptotic assumption.

## 4. One explicit discriminant branch decides the W_III cubic

Let Q=v^3+c2v^2+c1v+c0, with c2>0 and c0>0. Define its exact discriminant

`Disc(Q)=c2^2 c1^2-4c1^3-4c2^3c0+18c2c1c0-27c0^2`.

The relation to v12's Delta,E is

`27 Disc(Q)=4(c2^2-3c1)^3-(2c2^3-9c2c1+27c0)^2`.

Then

`Q>=0 on[0,infinity) IFF c1>=0 OR Disc(Q)<=0`. (DIII)

**Proof.** If c1>=0 all four coefficients are nonnegative with positive constant and leading coefficient; Q is strictly positive on the positive half-line. If c1<0, Delta=c2^2-3c1>c2^2 and the positive local minimum is ACTIVE. Also E=2c2^3-9c2c1+27c0>0 automatically. Thus v12's exact criterion E^2>=4Delta^3 is precisely Disc(Q)<=0. This proves both directions.

The ONLY extra positive root/admission check occurs when

`c1<0 AND Disc(Q)=0`.

It is the exact double root zeta=(-c2+sqrt(c2^2-3c1))/3. If c1>=0, even a zero discriminant gives no positive zero. If c1<0 and Disc(Q)<0, Q is strictly positive. If c1<0 and Disc(Q)>0, the full global corner inequality FAILS, not merely a sampled test.

This exhausts the W_III positivity branches after the two selected R factors. No claim that its width/height/remainder equations force one of these branches is made.

## 5. Current exact residual

The reciprocal problem still has three genuine alternatives, now expressed as W_I, W_(II,strict) and W_III. The latter two have finite coefficient/remainder/width/orientation/admission systems from v11/v12, with the branch simplifications above. All selected and possible extra contact multiplicities remain accounted for; an unweighted contact is not discarded.

What is missing is a POINT of one complete physical system or a uniform contradiction covering all its parameters. The discriminant signs and remainder equalities have NOT been decided by a scientific program or in written generality. The original universal degree-seven problem remains OPEN, and the full general nonreciprocal problem is not reduced to these reciprocal sets.

No old gate is widened, no source altered, no profile failure promoted to unrestricted failure, and no formal/kernel/human/configured-family/cross-vendor/executable/triple-finite/novelty or parent acceptance is claimed. Original science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and same eighteen owners remain; active written work continues.
