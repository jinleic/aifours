# Bounded exact septic dual search and a continuum barrier on one symmetric box ray

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 18:29:27 PDT 2026**. **EXACT rational, same-owner kernel-checked candidate**, not parent-reviewed, formal-verified or novelty-cleared. This is a bounded actual-box search and an analytic continuum disposition of one explicit restricted ray. It is not a proof of universal septic synthesis or an unrestricted counterexample.

## 1. Actual box ray and new continuum result

Use the explicit base endpoints and unrestricted monic common numerator from the COMPLETE `frontier-20261028-actual-box-internal-numerator-obstruction-v1.md`, SHA256 `736008cc61a9f11bf8a29c6353c14ba44f42632d56580d158b61d69177729902`. Base endpoints in ascending coefficient order are

`l=(4435,10747,23670,40980,10632,13071,1089)/1000`,
`u=(4586,11496,24364,43182,11217,14315,1147)/1000`.

For a real factor r>=0 let `K(r)` be the closed monic coefficient box with midpoint `(l+u)/2` and half-width `r*(u-l)/2`, independently in all seven coefficients. Thus K(r) is nested as r increases, and r=0 is a permitted degenerate box.

Use the SAME explicit monic numerator

`b*=s^7+(3413/100)s^6+(3851/100)s^5+(23757/100)s^4`
`   +(16691/100)s^3+(7183/100)s^2+(883/25)s+1/1000`.

**Exact restricted-ray conclusion, conditional on the named four-corner stability proof below:**

- For EVERY real `0<=r<=4011/4000`, the actual box K(r) is Hurwitz and b* is a common exact-degree-seven SPR numerator. In fact the literal real-part ratio has the uniform lower bound
  `140823585288084633125/143052369744488955343439659008 > 0`.
- For EVERY real `r>=1003/1000`, K(r) is NOT eligible: it contains one explicitly given non-Hurwitz actual polynomial.
- Only the restricted ray interval `4011/4000 < r < 1003/1000`, of exact width `1/4000`, remains undisposed by this result. Other directions, arbitrary original boxes and even this ray interval are not decided.

The first result is a constructive obstruction to a negative certificate on an entire continuum of eligible boxes, not just the eight search frequencies. The second is an exact ineligibility barrier, not an SPR failure.

## 2. Exact whole-half-line constructive side

At r=`4011/4000`, the four actual parity corners all passed rational Routh first-column checks AND a separately structured integer Bareiss computation of all seven leading Hurwitz determinants at each corner. The four-corner-to-full-box step is the complete written edge/first-contact result `frontier-20261028-twenty-eight-determinant-negative-certificate-v1.md`, SHA256 `0beadbe1a359572c53ba46f25e36853f64ff710c0e8cc5fa32c64079dc1f412f`; it remains author-unreviewed. It is also the standard named Kharitonov stability boundary, not a new claimed theorem.

For each corner a_i form the polynomial `P_i(t)=Re[b*(i sqrt(t)) a_i(-i sqrt(t))]`. The exact reviewer code independently compared its direct signed monomial expansion with the separate `E_a E_b + t O_a O_b` convolution. It then transformed `Q_i(x)=(1-x)^7 P_i(x/(1-x))` to degree-seven Bernstein form on `[0,1]` and used exact Fraction de Casteljau subdivision. The four leaf counts are `7,10,10,10`; EVERY Bernstein coefficient on EVERY leaf is strictly positive. The least coefficient over the entire partition is exactly

`delta=225317736460935413/18471795346636800000000 >0`.

Hence every corner and every t>=0 satisfies `P_i(t)/(1+t)^7 >= delta`. For fixed t the actual even/odd denominator values fill the rectangle of the four actual corners, and the SAME b* pairing is affine on that rectangle. The inequality therefore holds for EVERY a in the whole K(4011/4000), including t=0 and the compactified infinity endpoint. The endpoint coefficient upper sum is `S=890518513/8000000`; `|a(iw)|/(1+w^2)^(7/2)<=S` for all w. Thus the ratio is at least `delta/S^2`, exactly the displayed positive rational. Every K(r) for r<=4011/4000 is a subset and inherits both stability and this same b* bound.

## 3. Exact continuum ineligibility side

At r=`1003/1000`, the second parity corner in the kernel's `(E_-,O_+ )` ordering has ascending coefficients

`(8869547/2000000, 22994247/2000000, 24365041/1000000,`
` 40976697/1000000, 4252449/400000, 7158433/500000,`
` 1147087/1000000, 1)`.

Multiply the coefficient vector by the positive common denominator 2000000 and form its Hurwitz matrix. Its first seven leading minor signs are `+,+,+,+,+,-,-`; the sixth scaled determinant is exactly

`-20692796611395698634569012857725906552`.

Positive scaling preserves the sign of each Hurwitz determinant. The strict Routh–Hurwitz criterion therefore says this actual corner is **not** Hurwitz. For every r>=1003/1000, nesting places that same polynomial inside K(r), so the entire enlarged box is not robustly Hurwitz. No claim is made that its failure mode is a particular real or imaginary root.

## 4. Bounded discrete strict-cone search, and what it does not say

`frontier-20261028-bounded-exact-dual-search-kernel-v1.py`, SHA256 `bc10ea9be94ff63d729eccae52ad60e33079883a4b4ad33af898cea98535896a`, executed in Python Eval with Fraction/integer arithmetic and no optimizer import. It searched exactly six width factors `1,101/100,21/20,11/10,5/4,3/2`, four actual parity corners, and the eight rational frequencies

`1/2, 2/3, 1, 3/2, 2, 5/2, 3, 4`.

An exact simplex minimized the maximum of the eight coefficient sums over nonnegative normalized atom weights. It independently reconstructed and checked its primal and dual feasibility/equality with exact rational arithmetic. The synthetic minus/plus coordinate-basis controls had exact optima `-1/8` and `1/8`. All four-corner Routh statuses were compared with the separate integer Hurwitz determinant method; the pairing coefficient result was separately replayed by E/O convolution.

At r=1, the finite-grid optimum was

`40615253344833520237101/25233887965724661088 >0`,

so no strictly negative coefficient vector exists on THESE 32 selected corner/frequency atoms. The exact nonnegative dual coefficient vector and 14 simplex pivots are in `frontier-20261028-bounded-exact-dual-search-result-v1.json`, SHA256 `23d30e3b479bbd93036cc75ca0d55194a2a6348896ea42454154223072dad77b`. This dual vector has zero coefficients and is only a finite-grid separation witness; it is **not** asserted to be an original all-frequency common numerator. The other five tested factors have actual non-Hurwitz corners. No strict negative certificate was found.

The search does not rule out other rational frequencies, non-symmetric box variations, other actual coefficient boxes, or a negative certificate anywhere outside the proven constructive ray interval.

## 5. Reproducibility and remaining original gap

Exact kernel/receipt pins:

- Bounded simplex/stability/pairing source: SHA `bc10ea9be94ff63d729eccae52ad60e33079883a4b4ad33af898cea98535896a`.
- Initial five-factor ray Bernstein source `frontier-20261028-symmetric-ray-bernstein-kernel-v1.py`, SHA `67325a51c0a339158e347ab227ef2c9c384cbfb718cddebae959f3a94ab819c4`; full exact leaves receipt `frontier-20261028-symmetric-ray-bernstein-result-v1.json`, SHA `c981207d22fa00fc3618ca3e962eab3c8dd40c70b8c69ced43c5f13903c4f0eb`.
- Four new refinement factors source `frontier-20261028-symmetric-ray-refinement-kernel-v1.py`, SHA `0c3de65e9dbcfce988152a595c0dd07619e914ce819e4ebfaa345e46cb2f1b1a`; full exact polynomials/leaves receipt `frontier-20261028-symmetric-ray-refinement-result-v1.json`, SHA `d94784ff2b67847cc0deeef071e75a74bf5347011758c4d34b746fab0cf9b347`.

All scientific arithmetic for these results used integers and `fractions.Fraction` within the owner's Eval kernel. No floating-point optimization, native scientific subprocess, nested agent, external-model CLI, publication, Git or deletion was used in these checks. The distinct methods were written in the same harness; no independent human/configured-family/formal verification or literature novelty claim follows. The original actual-box shared-numerator/dual-sign problem remains OPEN.

**END.**
