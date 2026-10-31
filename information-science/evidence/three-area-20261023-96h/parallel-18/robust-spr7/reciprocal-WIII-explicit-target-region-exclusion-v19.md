# SPR7 — an explicit polynomial target region contains NO W_III critical configuration

Actual returned `/bin/date` BEFORE creation: **Mon Oct 26 06:01:10 PDT 2026**. InfoSPR7/info-2. **NEW COMPLETE WRITTEN CONDITIONAL PARTIAL-EMPTINESS THEOREM CANDIDATE.** This excludes a nontrivial coefficient region of W_III, uniformly over ALL palindromic/nonpalindromic contacts, heights and actual positive input widths. It is not another tiny-r W_I result. W_I/W_II and universal SPR7 remain open.

All reasoning uses SYMBOLIC variables and exact polynomial/integer-product comparisons, even privately. No numerical instance, decimal gloss, calculator, scientific interpreter/eval/program/CAS, enumeration, solver, replay, CLI, nested agent or GO. All FOUR owner exactness/v18 process findings and every old history remain permanent/ZERO probe credit. No frozen source/gate is edited or retrospectively widened.

## 0. Exact inputs and theorem

Use the COMPLETE v11 actual pal-contact/width correspondence, `reciprocal-WII-WIII-pal-contact-height-wall-and-two-gap-v11.md`, SHA256 `6ce35ce58f8636a95aeddb3b3bbdcbda33a29facb18cdeb28d9b98f236c405b8`, and the COMPLETE221LF v16 necessary contact-location bound, `reciprocal-WIII-positive-width-lower-bounds-and-guarded-target-slices-v16.md`, SHA256 `850f35ab4b266e21ab5cf13a0c8885a1cd918f0899a432ae73ecae027ed369da`. The operative necessary inequality is reproduced below. Their original named v5/v9/v10+erratum and written assurance remain unchanged.

Let the strict target be

`T(z)=z^3+d z^2+e z+f`, `d,e,f>0`, `D:=de-f>0`.

**Theorem.** W_III has NO point with this target if

`E_*:=e(d+1)-d^2>0`,

`D(d+1)^3 e(e+1)<=d E_*^2`. (REG)

This is a rational POLYNOMIAL inequality region of strict cubic target coefficients. It imposes NO bound on the contact heights, frequencies or original width ratios. It does not exclude W_I/W_II at the same target and does not prove a reciprocal-class verdict.

## 1. The exact necessary W_III target/contact gap

The target phase cubic A(v) has roots

`0<rho1<f/d<rho2<e<rho3`.

W_III's C1 lag contact a satisfies rho2<a<e and height l<f(e-a)/(da-f). Let b in(0,rho1) be its C3 pal contact. Positive original widths imply w1<L. The direct v11 width inverse gives

`C0<l M(a)-m M(b)`,

`C0=(a-b)(2e-a-b)>0`, `M(v)=(D+d)v^2/f-2v+e>0`.

Hence l>C0/M(a). Compatibility with the lag upper wall forces

`D(e-a)a(a+1)>(da-f)(e-b)^2`.

This is v16's exact factored inequality, derived there by expanding the two sides. Since a(a+1)<=e(e+1), it implies

`e-a>epsilon_b:=D(e-b)^2/[d(e-b)^2+D e(e+1)]`.

The expression is increasing in(e-b)^2. Thus b<rho1 gives the target-only bound

`e-a>epsilon_T:=D(e-rho1)^2/[d(e-rho1)^2+D e(e+1)]`. (NEC)

But a>rho2 also gives e-a<e-rho2. Therefore W_III is empty whenever epsilon_T>=e-rho2. The proof below shows that(REG) is an explicit sufficient coefficient condition for exactly this contradiction.

## 2. Locate the target's inner phase roots using a fixed symbolic comparison point

Set

`v_*=d^2/(d+1)`, `h_*=e-v_*>0`,

`K_*=d(d+2)/(d+1)`.

Because f=de-D, put W=e-v and X=f-dv=dW-D. Then the phase cubic identity is

`A(v)=[d^2-(d+1)v]W^2+D[(v-2d)W+D]`.

At the SYMBOLIC comparison v=v_*, the first bracket vanishes, while v_*-2d=-K_*. Hence

`A(v_*)=D[D-K_*h_*]`.

Condition(REG) is exactly

`0<D<= [d/(d+1)] h_*^2/[e(e+1)]`. (SMALL-D)

Since h_*<e, its upper bound is STRICTLY smaller than K_*h_*. Thus A(v_*)<0. Also v_*<e<rho3. By the known sign pattern of A, it follows that

`rho1<v_*<rho2`.

In particular e-rho1>h_* and rho2>v_*. This is a uniform symbolic root isolator, not a numerical target sample.

## 3. An exact upper bound for e-rho2

At v=rho2, put q=e-rho2>0 and X_+=d rho2-f>0. The root equation A(rho2)=0 gives

`X_+^2+rho2 X_+ q-rho2 q^2=0`.

Define k(v)>0 by

`k(v)^2+v k(v)-v=0`.

Its positive root satisfies0<k(v)<1 and is strictly increasing: implicit differentiation gives(2k+v)k'=1-k>0. At v=v_*, direct substitution gives

`k(v_*)=d/(d+1)`.

The root equation above says X_+/q=k(rho2). Also D=dq+X_+=(d+k(rho2))q. Since rho2>v_*,

`e-rho2=q=D/[d+k(rho2)]<D/K_*`. (QUP)

Every denominator is positive; no squared sign branch or approximate root value was used.

## 4. A contradictory lower bound from(REG)

Because e-rho1>h_* and x↦Dx/[dx+D e(e+1)] is strictly increasing on x>0,

`epsilon_T>D h_*^2/[d h_*^2+D e(e+1)]`.

By(SMALL-D), D e(e+1)<=d h_*^2/(d+1). Therefore

`d h_*^2+D e(e+1)<= [d+d/(d+1)]h_*^2=K_*h_*^2`.

Consequently

`epsilon_T>D/K_*>e-rho2`,

where the last strict inequality is(QUP). This contradicts(NEC) and a>rho2, which require epsilon_T<e-a<e-rho2. Hence W_III has NO such point. ∎

## 5. The excluded region is a genuine symbolic family, not an empty condition

For ANY d,e>0 with e(d+1)>d^2, the quantity

`C_*=d[e(d+1)-d^2]^2/[(d+1)^3 e(e+1)]`

is positive. Choose SYMBOLIC D with0<D<min(de,C_*) and put f=de-D>0. Then the target is strictly Hurwitz and satisfies(REG), strictly if D<C_*. This exhibits a whole parameter family without substituting or evaluating any numerical target.

It is a region adjacent to the cubic Hurwitz determinant boundary D=0 on the side e>d^2/(d+1). No claim is made for the opposite side, for larger D, for W_I/W_II, or for arbitrary input boxes. This is an exact W_III target-domain exclusion derived from actual width/height constraints, not a scientific solver result or an original universal numerator theorem.

## 6. Exact residual and assurance

For the reciprocal union, any W_III point must now lie OUTSIDE(REG), in addition to the finite positive-factor/amplitude system and guarded-source boundaries already stated. Deciding that remaining domain, W_I and W_II_strict, or delivering an actual complete physical point remains OPEN. The original general-box SPR7 problem is unchanged.

This is WRITTEN mathematics requiring a fresh full-source/application gate at its named imports, not formal/kernel, human, configured-family/cross-vendor, executable/triple-finite, novelty or parent acceptance. No scientific execution/new GO, source cutover, nineteenth owner, deadline reset or round closeout. Same original science cutoff2026-10-27T11:05:38-07:00/deadline12:35:38 and substantive actual-clock cadence; work remains active.
