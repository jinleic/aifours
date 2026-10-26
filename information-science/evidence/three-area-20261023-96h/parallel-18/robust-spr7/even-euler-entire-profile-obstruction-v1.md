# Candidate v1 — an exact reciprocal box defeats the entire new even-Euler profile

Actual clock observed before creation: **2026-10-24T04:25:46-0700 PDT**. InfoSPR7, info-2. This follows the ONE choice frozen in `continuation-v3-new-profile-counterexample-freeze-v1.json`: an exact counterexample to the newly proposed profile over its entire scalar family, not a simultaneous all-box synthesis branch. **Complete WRITTEN CANDIDATE, pending actual separate reconstruction and parent disposition.** No mathematical program, arithmetic interpreter, CAS, numerical root search, enumeration, solver, compilation, CLI or nested agent was used.

## 0. Literal result and original-target gap

We construct a closed independent monic degree-seven interval box whose every member is strictly Hurwitz, yet for its **actual normalized midpoint even cubic F**, every numerator

`b_epsilon(s)=F(-s^2)+epsilon*s*[4F(t)-tF'(t)]_(t=-s^2)`

fails at one exact finite algebraic frequency, for **every real epsilon**. This includes all positive epsilon giving the previously proposed exact-degree-seven profile and all its positive scalar normalizations. In fact the proof excludes the whole real linear span of its two component polynomials, not merely one failed sufficient budget.

This does **not** refute the previously supported sufficient implication: this box cannot meet a correct hypothesis that would make that profile succeed. It also does **not** refute universal SPR7. An explicit unrestricted monic degree-seven common numerator for this same box is supplied in §6, using the exact supported positive application and a fully justified reciprocal transformation. The failure is genuinely profile-specific.

Together with the earlier same-box escape result, this shows neither fixed anchor profile is universal or dominates the other. It does not show that choosing between the two profiles covers every robustly stable box. The original unrestricted degree-seven problem remains open.

## 1. Frozen source interfaces and provenance

The following bytes were freshly bound at the branch freeze and remain unchanged:

- `even-euler-comparator-candidate-v1.md`: SHA256 **`ec744ccc6b269bb935aaa95e075cc559cda0ca6c44cc6bd580144306edc3c61a`**. Its §7 supplies an explicit common numerator B_* and weighted pairing margin for a full-seven-width box containing the old control family below.
- `consolidation-scope-companion-v1.md`: SHA256 **`d0f816590907602e33e0c8843d3be575eb902700e76ca58f45047e8442adecea`**. Its exact old box/sign control is restated independently below rather than accepted from a hash alone.
- Actual parent `spr7-even-euler-parent-v1.md`, read completely: SHA256 **`ebb381e5a7d78ee4d0c0541fa374052b5f8cbabb3ce0c22c0983a7a55a8ed06e`**. It records present complete parent reads and WRITTEN_SUPPORTED sufficient/application scope, not universality or formal/novelty certification.
- Operative `parent-evidence-erratum-v4.md`, read completely: SHA256 **`9226da81aba4a5255050dbd2cf99db5d1cdf9b7d2a4fcb96e1bb9136b6bc4b17`**. Its correction of earlier premature read claims is retained; later reads do not retroactively establish earlier coverage.

The freeze discloses preliminary reciprocal scoping before its creation. No pristine/blind preregistration or independence from the earlier countercontrol is claimed. Reciprocal root transport and the two anchor profiles have classical antecedents; novelty is UNCLEAR. The new profile-exclusion proof §§2–5 does not depend on the correctness of the positive certificate; that prior positive margin is used only for the additional common-numerator witness in §6.

## 2. Literal independent monic coefficient box

Put

`M=375000`, `C_0=100000000`,

and retain the old polynomial family

`a_c(s)=s^7+s^6+3050s^5+(4001/2)s^4+2150000s^3`

`          +751000s^2+c s+M`,

`2000000<=c<=198000000`.

Define the new family by the **fixed normalization**

`p_c(s)=s^7*a_c(1/s)/M`.                                     (1)

This is a polynomial, not a Laurent transfer function. Explicitly,

`p_c(s)=s^7+(c/M)s^6+(751/375)s^5+(86/15)s^4`

`          +(4001/750000)s^3+(61/7500)s^2+(1/M)s+1/M`.         (2)

Thus the exact independent coefficient intervals are

`a_1 in[16/3,528]`,

`a_2=751/375`, `a_3=86/15`, `a_4=4001/750000`,

`a_5=61/7500`, `a_6=a_7=1/375000`.

Only a_1 is uncertain; the other six intervals are degenerate. Such boxes are explicitly allowed by the original target and the positive profile theorem. Both closed endpoints are included. All coefficients are positive, and every denominator has exact degree seven and leading coefficient1.

The normalization is legitimate for the **whole** interval box because M, the old constant coefficient, is the same positive number for every c. It is not an independent interval hull of a correlated normalized image, nor division by the variable c. The new variable c/M runs bijectively through one interval while every other coefficient is fixed. No invalid monic-reciprocal-family assumption is hidden in(1).

## 3. Every closed-endpoint member is strictly Hurwitz

For completeness write the old components as

`E_old(t)=-(t-1/2)(t-500)(t-1500)`,

`O_c(t)=-t^3+3050t^2-2150000t+c`.

Across the entire c-interval, exact endpoint bounds are

`O_c(1/2)>=7406099/8>0`,

`O_c(500)<=-239500000<0`,

`O_c(1500)>=264500000>0`.

The cubic O_c tends to negative infinity. It therefore has one simple positive root in each of `(1/2,500)`, `(500,1500)`, `(1500,infinity)`. They exhaust its degree and strictly interlace the fixed even roots, with positive component constants and the correct negative leading signs. The degree-seven Hermite–Biehler criterion proves every a_c Hurwitz, including both endpoints. These three sign intervals plus degree are a full root-order proof, not a numerical sample.

Every root lambda of a_c is nonzero because its constant M is positive. The roots of p_c are exactly 1/lambda, with the same algebraic multiplicities. For complex lambda,

`Re(1/lambda)=Re(lambda)/|lambda|^2<0`.

Consequently **every** p_c is strictly Hurwitz. This proof allows arbitrary nonreal roots and does not invoke cancellation in any numerator/denominator ratio.

## 4. The actual midpoint even cubic and an exactly isolated zero of its Euler polynomial

The new even component is

`E_(p_c)(t)=[1-3050t+2150000t^2-c t^3]/M`.

The midpoint of the variable c is C_0. The actual midpoint a_1 is `C_0/M=800/3`. Therefore its normalized midpoint even cubic is exactly

`F(t)=[1-3050t+2150000t^2-C_0t^3]/C_0`

`    =-t^3+(43/2000)t^2-(61/2000000)t+1/100000000`

`    =-(t-1/2000)(t-1/1000)(t-1/50)`.                        (3)

This is the comparator demanded by the NEW profile for THIS box, not a freely substituted anchor.

Its complementary Euler polynomial is

`H(t)=4F(t)-tF'(t)`

`    =-t^3+(43/1000)t^2-(183/2000000)t+1/25000000`.

For an integer-coefficient isolator put

`J(t)=C_0 H(t)=-100000000t^3+4300000t^2-9150t+4`.

Direct rational substitution gives

`J(1/30)=20873000/27000>0`,

`J(1/20)=-17628000/8000<0`.

Moreover

`J''(t)=-600000000t+8600000<=-11400000<0`

on `[1/30,1/20]`, and `J'(1/30)=-167450/3<0`. Thus J is strictly decreasing there and has a unique simple root

`sigma in(1/30,1/20)`.                                       (4)

Equations(3)–(4) specify an exact finite algebraic squared frequency; no numeric root approximation or executable isolation is used. Define `omega=sqrt(sigma)>0`.

All three roots of F are at most1/50, while sigma>1/30. Hence

`F(sigma)<0`.                                                (5)

## 5. A strict negative pairing for EVERY scalar parameter

Choose the actual lower-endpoint member p_- corresponding to c=2000000. Its even component is

`E_-(t)=[1-3050t+2150000t^2-2000000t^3]/M`.

For every `t in[1/30,1/20]`, bound the positive quadratic below at1/30 and both negative terms below at1/20:

`M E_-(t)>=1-3050/20+2150000/900-2000000/8000`

`          =35773/18>0`.                                     (6)

In particular E_-(sigma)>0. The denominator is already Hurwitz by §3, so its actual frequency value is nonzero (also immediate from this positive even part).

For an arbitrary real epsilon, the profile numerator has components

`E_b=F`, `O_b=epsilon H`.

At the SAME algebraic frequency(4), its pairing with the SAME denominator p_- is

`P_(p_-,b_epsilon)(sigma)`

` =F(sigma)E_-(sigma)+epsilon*sigma*H(sigma)O_(p_-)(sigma)`

` =F(sigma)E_-(sigma)<0`.                                    (7)

Thus `Re(b_epsilon(i omega)/p_-(i omega))<0` for **every real epsilon**. In particular every positive epsilon from any tightened sufficient budget fails. Division by a positive epsilon to make the profile monic cannot repair the sign.

### Entire projective profile, not a fixed normalization trick

The same argument excludes every real linear combination

`b_(u,v)(s)=u F(-s^2)+v*s H(-s^2)`.

If u>0, (7) is multiplied by u and is still negative at sigma, independently of v. If u<=0, the pairing at zero is `u F(0)p_-(0)<=0`, violating strict positivity. Thus no polynomial in this entire two-dimensional real component span can work. This does **not** enlarge the exclusion to arbitrary degree-seven polynomials, which have eight unconstrained real coefficients.

### Relation to the earlier countercontrol

The reciprocal connection can be checked symbolically, not inferred from a matching root count. If

`Q_old(t)=-(t-50)(t-1000)(t-2000)`,

then

`F(t)=-t^3 Q_old(1/t)/C_0`,

`H(t)=-t^3[(u Q_old(u))']_(u=1/t)/C_0`.

The old derivative zero in(20,30) therefore corresponds to sigma in(1/30,1/20). Nevertheless §§4–5 prove the new zero and signs directly, so the new obstruction is not just an old verdict transported without checking the normalized midpoint definition.

## 6. An actual unrestricted common numerator exists for this same box

The preceding obstruction is intentionally profile-specific. To make the original-target gap explicit, set `k=10^7` and use the actually supported earlier positive application at its pinned source in §1. It supplies

`B_*(s)=s^7+k s^6+4001s^5+(4001/2)k s^4`

`           +2253000s^3+751000k s^2+1500000s+M k`,

and the exact full-frequency margin

`P_(a_c,B_*)(t)>=[k/(3001^7)](1+t)^7`                         (8)

for every old a_c in the entire interval: that family is contained in the source's explicit full-seven-width rho=1/1000 box. The parent disposition supports precisely this export at the stated in-harness written/classical boundary; no new execution or formal authentication is implied here.

Define the one polynomial

`N(s)=s^7 B_*(1/s)/(M k)`.

It is monic of exact degree seven because the old constant coefficient is Mk>0. Its complete coefficient formula is

`N(s)=s^7+(4/k)s^6+(751000/M)s^5+(2253000/(M k))s^4`

`       +(4001/(2M))s^3+(4001/(M k))s^2+(1/M)s+1/(M k)`.       (9)

Every coefficient is a literal rational number and N is independent of c. There is no placeholder synthesis step.

For s!=0,

`N(s)/p_c(s)=(1/k) B_*(1/s)/a_c(1/s)`.

At `s=i omega`, omega!=0, the right side evaluates the old strictly positive real ratio at the legal real frequency `-1/omega`, multiplied by the positive number1/k. At zero,

`N(0)/p_c(0)=[1/(M k)]/[1/M]=1/k>0`.

This proves strict positivity at **every** finite real frequency, not just away from zero. All new denominators are genuinely stable by §3, before any rational cancellation.

A direct pairing identity also transfers the whole-frequency certificate: for t>0,

`P_(p_c,N)(t)=[t^7/(M^2 k)]P_(a_c,B_*)(1/t)`.

Apply(8) and cancel the reciprocal powers to obtain

`P_(p_c,N)(t)>=[1/(M^2*3001^7)](1+t)^7>0`.                   (10)

Both sides are polynomials/continuous at0, so the same bound holds there. Thus(9) is an actual common numerator with a full weighted margin, not merely an appeal to the fixed-odd-part theorem.

As a consistency check, the fixed odd component of the new denominators is

`Q_new=-t^3+(751000/M)t^2-(4001/(2M))t+1/M`,

and(9) is exactly

`N(s)=sQ_new(-s^2)+(1/k)*(tQ_new(t))'|_(t=-s^2)`.

So the old odd-anchor profile succeeds on this box while the new even-anchor profile fails. On the earlier supported full-width box the reverse happened. Neither profile universally dominates the other. Their union has **not** been proved to cover every robustly stable box.

## 7. Exact interpretation and next mathematical boundary

**Closed by this candidate, subject to reconstruction:** a literal independent monic degree-seven interval family, strict all-member Hurwitz proof, its actual normalized midpoint even comparator, and an exact finite-frequency negative pairing for every scalar in the entire new profile; indeed for its whole real two-component span. The independently supported positive export plus the fully checked reciprocal identities give an explicit unrestricted common numerator for the same family.

**Not closed:** a counterexample to unrestricted SPR7, all-box synthesis, a general rule selecting between the two profiles, an exact optimal numerator family, necessity of either sufficient budget, or worldwide novelty. The fixed-even/fixed-odd special cases and reciprocal/Euler machinery remain classical baselines. The constructive witness(9) is used as a correctness/scope control, not another independent discovery to count.

Any universal continuation must now address **unrestricted comparator/profile selection or a different global mechanism**, not make either of these fixed midpoint profiles universal by improving constants. We do not claim their two-profile selection problem is equivalent to the original unrestricted synthesis problem; other degree-seven numerators remain fully admissible.

## 8. Verification boundary

No source has been edited. This new proof needs its own complete pinned supplied-proof reconstruction and parent disposition. Earlier reviews of the positive mechanism or the old profile do not automatically accept this reciprocal box, normalization, isolator, whole-span exclusion or zero-frequency witness transfer.

The profile obstruction §§2–5 is self-contained at the named degree-seven Hermite–Biehler and elementary reciprocal-root/continuity interfaces. Section6 separately consumes the exact previously supported positive margin(8); if that import is not authenticated at its literal pin, retain the profile obstruction but mark the optional unrestricted witness transfer conditional. No scientific program, kernel/Lean replay, outside-model/human review, publication, native retry or new GO occurred. The original96-hour deadline and all standing parent errata/HOLDs remain unchanged.
