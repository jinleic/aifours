# Numbered scope companion v1 — the fixed midpoint derivative profile is not universal

Observed before creation: **2026-10-23T15:02:36-0700**. InfoSPR7, same info-2 target. Written candidate, **not parent/peer accepted**. Frozen on the parent's explicit instruction to fold this qualification into one companion while preserving the earlier pins. No program, solver, arithmetic interpreter, numerical root search or executable certificate check ran.

## 1. What is qualified

This companion belongs to the one lane consolidation:

- `consolidated-v2.md`, SHA256 `5d5f8d3708ff3368143289edc8866238603d8ea0c0db33b17eddb854f8fc3c18`;
- positive criterion appendix v1, `be9631c3dae51e4342fb192b932608c43ae6ba954e82cc7d0c2c9ad657fae172`;
- positive application appendix v2, `d99ec39949ed4198e1916aa09349796c7948fd4d2c2851fc4f7e38589d71ce06`.

The sufficient positive certificate remains a candidate theorem with its explicit scalar-budget hypothesis. Nothing below refutes that theorem or its explicit positive application. Instead, the proposed path from robust stability to that budget for the **fixed midpoint-odd comparator and derivative profile** is now definitively blocked by an exact stable interval-family control.

The previous wording that such an implication was merely "not proved" is superseded in this precise sense: the profile itself can fail for **every** value of its scalar parameter. Therefore no tightening of the same budget estimates can make that fixed profile universal. A universal continuation needs a different comparator/profile or another positivity mechanism.

This is a mathematical scope qualification, **not another problem, independent result tally, or counterexample to unrestricted SPR7**.

## 2. The literal degree-seven coefficient box

Take the fixed even component

`E(t)=-(t-1/2)(t-500)(t-1500)`

`    =-t^3+(4001/2)t^2-751000t+375000`,

and let the odd component vary as

`O_c(t)=-t^3+3050t^2-2150000t+c`,

`2000000<=c<=198000000`.

Equivalently the actual polynomial family is

`a_c(s)=s^7+s^6+3050s^5+(4001/2)s^4+2150000s^3`

`          +751000s^2+c s+375000`.                            (1)

Only its linear coefficient is uncertain. This is a genuine closed monic degree-seven interval box; the other six intervals are degenerate. Such boxes are explicitly allowed by the original frozen target and the positive certificate.

## 3. Every member is strictly Hurwitz

At the three even roots, coefficient-endpoint bounds give

`O_c(1/2)>=7406099/8>0`,

`O_c(500)<=-239500000<0`,

`O_c(1500)>=264500000>0`.

For clarity, the first is exactly

`-1/8+3050/4-2150000/2+2000000=7406099/8`.

The second uses the upper endpoint `c=198000000`; the third the lower endpoint `c=2000000`. The signs therefore hold throughout the **entire interval**, including both closed endpoints. Since the odd component is cubic with negative leading coefficient, it has one root in each of

`(1/2,500)`, `(500,1500)`, `(1500,infinity)`.

These three distinct roots exhaust its degree and are simple. Together with the fixed even roots `1/2,500,1500`, positive component constants and correct negative leading signs, this is exactly the strict degree-seven Hermite–Biehler ordering. Hence every denominator in(1) has all roots in the open left half-plane. No numerator cancellation or numerical stability test is involved.

## 4. The actual midpoint odd comparator and an exact isolated frequency

The midpoint odd component is

`Q(t)=-t^3+3050t^2-2150000t+100000000`

`    =-(t-50)(t-1000)(t-2000)`.

Its derivative profile polynomial is

`D(t)=(tQ(t))'=-4t^3+9150t^2-4300000t+100000000`.

The exact endpoint values are

`D(20)=17628000>0`, `D(30)=-20873000<0`.

Thus there is a root `tau in(20,30)`. This gives an exact algebraic-frequency specification, not a floating-point approximation: `tau` is the unique zero of the displayed cubic in the rational interval `(20,30)`. Indeed

`D'(t)=-12t^2+18300t-4300000<0` on `[20,30]`,

since `18300t<=549000<4300000` there. The root is therefore unique and simple on that interval. Set `omega=sqrt(tau)>0`.

The factored `Q` is strictly positive on `[20,30]`. It is also strictly decreasing there, because

`Q'(t)=-3t^2+6100t-2150000<0`.

Consequently

`0<Q(tau)<Q(20)=58212000<98000000`.                            (2)

The lower-endpoint denominator has odd component

`O_low=Q-98000000`,

so (2) proves `O_low(tau)<0`.

## 5. Every scalar parameter in the fixed profile fails

Consider the exact profile used in the positive appendix,

`b_epsilon(s)=sQ(-s^2)+epsilon D(-s^2)`.

Its frequency components are `E_b=epsilon D` and `O_b=Q`. At the exact frequency from §4, the pairing with the lower-endpoint member of(1) is

`P_{a_low,b_epsilon}(tau)`

` =epsilon D(tau)E(tau)+tau Q(tau)O_low(tau)`

` =tau Q(tau)O_low(tau)<0`.                                   (3)

Equation(3) holds for **every real epsilon**, not merely for one failed parameter choice. In particular no positive epsilon from any improved scalar estimate can yield a common numerator of this fixed form. Positive scalar normalization of a numerator does not change this negative sign.

This is an exact finite obstruction to the displayed **profile**, quantified over all of its scalar parameters, with a certified stable original interval family. It is not a numerical sample being promoted to a universal statement about all real degree-seven polynomials.

## 6. Consequence for the consolidated research route

- The positive certificate's conditional implication is untouched: when its explicit budget holds, its constructed numerator and strict pairing proof still stand subject to their pending reconstruction.
- This family has the positive comparator residues guaranteed by robust stability, yet the fixed midpoint derivative profile cannot work. Thus robust stability alone cannot make that same profile's sufficient budget universally applicable.
- The exact positive `rho=10^-6` application remains a valid separate candidate application of the sufficient criterion; it makes no universal assertion contradicted here.
- The universal missing ingredient is now **a different comparator/profile or another global cubic mechanism**, not merely a better constant in the same midpoint-derivative budget. A different admissible comparator has not been excluded, and neither have general cubic even/odd numerator components.
- The original problem permits unrestricted real exact-degree-seven numerators. Nothing here obstructs that quantifier. This family has fixed even part, a class already recorded as classically synthesizable in the actual book/source baseline. No new unrestricted common numerator for this control is constructed or claimed here; its existence is not a premise needed for the strict-Hurwitz and profile-failure statements.

## 7. Review and priority limits

This companion's integer/rational identities, full-interval Hermite–Biehler signs and isolated-root argument were derived in writing only. Actual separate reconstruction and parent verification have not occurred. Earlier reviews of the Routh or dual-lift packets do not authenticate this control automatically.

All original snapshots and hashes remain unchanged. This qualification must travel with the positive criterion in future consolidation so that it is never described as one unproved scalar inequality away from universal SPR7. No novelty, earliest-order, formal/kernel, human, external-model or solved-book claim is made. Generic limitations of fixed numerator profiles may have classical precedents; priority remains UNCLEAR.
