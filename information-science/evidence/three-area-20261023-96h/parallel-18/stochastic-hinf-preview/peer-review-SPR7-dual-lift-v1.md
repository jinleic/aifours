# Priority in-harness review — conditional dual Routh lift and cubic-bound attack

Reviewer **InfoHinfPreview**, info-3. Observed before creation **2026-10-23T14:35:17-0700**, `/bin/date '+%Y-%m-%dT%H:%M:%S%z'`. This is the parent's bounded priority review, not the author's self-review or an independent-model CLI run. No author files were edited, no scientific program was executed and no new agent was launched.

## Exact packet and verdict

Both full files and the actual SPR selection/definition boundaries were read. Independently observed SHA256s match the assignment:

1. `information-science/evidence/three-area-20261023-96h/parallel-18/robust-spr7/dual-lift-candidate-v1.md`: **d9861944688b8b4bb958b6622ce84401735e59f91cec5212b16206478e8a66da**.
2. `information-science/evidence/three-area-20261023-96h/parallel-18/robust-spr7/cubic-bound-attack-v1.md`: **9e5e2ed587fc88d14de7985810552a1cf97ecc14c79bc6230eb95517e6f87d4f**.

**No FATAL, MAJOR or MINOR mathematical defect found at the explicitly conditional/scoped claims.** The fixed-`c` dual identity and degree/strictness restoration reconstruct correctly. The cubic control blocks an even-data-only finite terminal bracket, **not all possible global cubic comparison lemmas**. It is an attack record identifying a missing ingredient, not proof that the full degree-seven target or every cubic comparison is impossible.

## 1. Exact hypothesis boundary of the lift

The common coefficient `c=[s^6]a>0` is fixed across the compact robustly Hurwitz monic septic family (dual-lift lines7–13). For each actual member, the preceding separately reviewed Routh argument gives a monic stable sextic `q_a`, with

`E_q=E_a/c`, `O_q=(O_a-E_a/c)/c`.

The existence of one degree-six `beta=F(-s^2)+sG(-s^2)` with a genuine strict-SPR proof **for all actual correlated `q_a`** is a supplied premise, not established by the manuscript. It is not inferred from pointwise stability, an unstable coefficient hull, a segment theorem or an unauthenticated Lean announcement.

The fixed-`c` premise is load-bearing: the proposed common numerator contains `1/c`. Substituting a different `c(a)` into the numerator would violate the common-numerator quantifier. This exact limitation is explicitly retained at dual-lift lines75–80.

## 2. Independent reconstruction of the shear identity

For `b0=F(-s^2)+(s+s^2/c)G(-s^2)`, direct evaluation on `s=i w`, `t=w^2`, gives

`E_b0=F-tG/c`, `O_b0=G`.

Therefore

`P(a,b0)=(F-tG/c)E_a+tG O_a`

`        =F E_a+tG(O_a-E_a/c)`

`        =c[(E_a/c)F+t((O_a-E_a/c)/c)G]`

`        =c P(q_a,beta)`.

This checks all factors of `c` and the minus sign introduced by `s^2=-t` in dual-lift lines21–33. The identity is symbolic and preserves the actual correlations. No independent interval hull is introduced.

Since `deg F<=3` and `deg G<=2`, `F(-s^2)`, `sG(-s^2)` and `(s^2/c)G(-s^2)` have degrees at most6,5,6 respectively. Thus `deg b0<=6`, as needed for the subsequent degree-raising step.

## 3. Compactification margin and exact degree-seven restoration

Let `ell` be the leading coefficient of the supplied exact-degree-six `beta`. With monic sextic denominators, `Re(beta(iw)/q_a(iw))` tends to `ell`. Strict positivity at every finite frequency implies `ell>=0`; exact degree implies `ell!=0`, hence `ell>0`. This supplies the positive endpoint at infinity claimed at dual-lift lines39–47, not an unproved strict limit from a merely nonnegative limiting ratio.

The pairing `P(q_a,beta)` has degree6 in `t`, with leading coefficient `ell`: its even-even product contributes `ell t^6`, while its odd-odd term has degree at most5. Thus `P/(1+t)^6` extends continuously to `x=t/(1+t)=1` with the same **uniform positive value** `ell`. Compactness of the true coefficient image and the frequency compactification then gives the strictly positive `mu` of(3). This is an existence/margin argument conditional on `beta`, not an algorithm solving the omitted common-numerator problem. The manuscript correctly allows replacing `mu` by a separately certified lower bound.

The monomial `s^7` has even component0 and odd component `-t^3`, so

`P(a,s^7)=-t^4 O_a=t^7-a2 t^6+a4 t^5-a6 t^4`.

All septic Hurwitz coefficients are positive. Dropping its positive terms and using `t^6,t^4<=(1+t)^6` gives the stated lower bound `-(U2+U6)(1+t)^6`. For

`epsilon=c*mu/[2(1+U2+U6)]`,

one has

`c*mu-epsilon(U2+U6)>c*mu/2>0`.

Consequently the pairing remains strictly positive at **every** `t>=0`, including zero. The added `epsilon s^7` cannot cancel against any degree-at-most-six term, so the result has exact degree7 and leading coefficient `epsilon>0`. At infinity its ratio to each monic septic tends to this positive `epsilon`. These checks establish the lift exactly under its fixed-`c` and supplied-`beta` assumptions; they do not establish either missing prerequisite.

## 4. Independent reconstruction of the cubic control

For each fixed `R>20`, the cubic-bound manuscript uses the fixed even polynomial

`E=-(t-1)(t-3)(t-5)=-t^3+9t^2-23t+15`

and an actual independent box

`O=-t^3+A t^2-Bt+C`,

`A in[R+6,R+7]`, `B in[6R+8,6R+14]`, `C in[8R,8R+8]`.

Direct coefficient-endpoint bounds give:

* `O(1)>=-1+(R+6)-(6R+14)+8R=3R-9>0`;
* `O(3)<=-27+9(R+7)-3(6R+8)+(8R+8)=20-R<0`;
* `O(5)>=-125+25(R+6)-5(6R+14)+8R=3R-45>0`.

The cubic tends to negative infinity, so it has one root in each of `(1,3),(3,5),(5,infinity)`. They exhaust its degree and are distinct, hence simple. The exact order with even roots1,3,5 is the correct degree-seven Hermite–Biehler order. This proves stability of **every** independent coefficient choice, not only the named member or finitely many tests.

Expanding the named member gives

`O_R=-(t-2)(t-4)(t-R)`

`   =-t^3+(R+6)t^2-(6R+8)t+8R`.

It is an endpoint member of the same box and has terminal odd root exactly `R`. Because the even polynomial does not change as `R` grows, no finite upper bound on that terminal root can depend **only** on its even-root data. Each fixed-`R` coefficient family is compact and has its own coefficient/root bounds; the argument does not deny those ordinary bounds.

The conclusion supported by cubic-bound lines39–54 is therefore precise: a literal even-data-only reuse of the sextic bounded-gap bracket fails. It **does not** exclude bounds using the actual odd coefficients, an `R`-dependent terminal scale, other global cubic inequalities or an improved construction. The author explicitly names those possibilities and leaves the global cubic comparison obligation unresolved.

## 5. Actual primary comparison and import trust

I opened the actual primary [sextic paper, arXiv2609.26541v2](https://arxiv.org/html/2609.26541v2), §3 Lemma3.1 and **Lemma3.2 with its full proof**, equations(3.5)–(3.9). It constructs two quadratics `U=(t-A)(t-c)` and `V=(t-B)(t-b)` from bounded even-root gaps, scales them to satisfy global `hU<O_-<=O_+<kV`, and proves the inequalities by the completed-square identity for nested **quadratic** root intervals. The final scale comparison also uses positive coefficient endpoints and the ordering of the two discriminants. Thus the cubic-bound manuscript correctly identifies a missing geometric ingredient, rather than overlooking that the sextic lemma already controls an unbounded third odd root. No cubic theorem or generic arbitrary-order claim appears in that imported statement.

The earlier Routh reduction/Hermite–Biehler bridge was reconstructed in my completed `peer-review-SPR7-Routh-obstruction-v1.md`; it remains a standard named classical import at the stated degree-specific orientation. The dual-lift result uses no sextic existence theorem except its explicitly hypothetical supplied numerator. I did not authenticate or execute the announced sextic Lean development, and no numerical examples or root tests were run.

## Result and remaining obligation

The packet supports a **conditional correlation-preserving numerator-lift lemma** and a correctly scoped negative control against one even-only bounded-gap extrapolation. It does not prove universal SPR7, does not supply a common numerator for arbitrary true sextic Routh images, does not handle varying common `c` by the same formula, and does not establish a global cubic comparison lemma. Those are genuine mathematical gaps, not omitted environment work. Priority/novelty remains UNCLEAR; neither the standard compactness/degree-raising mechanism nor the fixed-even-part control should be counted as a new open-problem resolution.
