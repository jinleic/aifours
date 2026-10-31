# Actual septic-box dual obstruction: five positive frequencies force both endpoints

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 17:58:49 PDT 2026**. **WRITTEN all-variable candidate; not reviewed or adopted.** A preliminary finite symbolic sign-class check was performed in the owner's Eval kernel; the proof below does not rely on that enumeration, a sampled polynomial or any numerical root. It establishes a necessary obstruction condition, not a counterexample or universal positive sign.

## 1. Exact original-object result

Use the original independent closed monic septic-box definition `institute/runs/three-area-2026-10-27-96h/written-releases/info-2-septic-box-definitions-v1.md`, SHA256 `d86737954bee95836e2d2cffade9cba15a99f2bb486b660ada2562c25fc764ad`. Let K be ANY such box, including degenerate intervals, with EVERY member strictly Hurwitz. A compactified actual-member annihilator is a positive finite weighted combination of actual pairings, at x in `[0,1]`, that vanishes on EVERY real coefficient vector of degree at most7. Frequencies x=0 and x=1 mean zero and compactified infinity. After merging all equal x, write m for the number of distinct **positive finite** squared frequencies, and e0,einf in `{0,1}` for the presence of these endpoints.

**Theorem.** Every such actual-box annihilator has `m>=5`. If `m=5`, then **both** endpoint atoms are present: `e0=einf=1`. In particular no exactly-one-endpoint or endpoint-free obstruction can be supported at five positive frequencies, irrespective of how many actual denominators were originally assigned to a single frequency.

If the entire actual-corner `<=8`-atom alternative in `frontier-20261028-connected-eight-atom-algebraic-obstruction-v1.md`, SHA256 `d8c1deeab9439e9f0644e2fde45c40a0c188904fbb2a56a8afdc8e989b4d90ac`, is accepted, a counterexample with m=5 has an obstruction with both endpoints and either seven or eight actual-corner atoms. The present lower-bound theorem itself does not assume that unreviewed upper-support theorem. No zero certificate or actual negative box is claimed.

## 2. Common, strictly separated phase-root bands

Write `a(i sqrt(t))=E_a(t)+i sqrt(t) O_a(t)`, where

`E_a=a_0-a_2 t+a_4 t^2-a_6 t^3`, `O_a=a_1-a_3 t+a_5 t^2-t^3`.

For each actual a, factor it into seven complex linear factors with roots `-alpha+i beta`, alpha>0. The continuous phase theta of `a(iw)`, starting from theta(0)=0, has derivative `sum alpha/(alpha^2+(w-beta)^2)>0` and tends to `7pi/2` as w increases. Conjugate pairing gives initial phase zero. Hence E_a has three simple positive roots e1<e2<e3, O_a three simple positive roots o1<o2<o3, and

`0<e1<o1<e2<o2<e3<o3`.

The corresponding six roots are continuous functions on their compact coefficient boxes: opposite-sign isolating intervals for simple roots persist under small perturbations, and cubic degree prevents additional roots. The even and odd coefficient boxes are independent. Therefore EVERY even-part choice and EVERY odd-part choice can be combined into one actual a in K. Taking the actual maximizer of one root and actual minimizer of the next gives SIX globally ordered compact root bands, with every maximum of a band strictly less than every minimum of the next. This remains true if some bands are points.

For a positive frequency t and actual a, assign a phase class q in `{0,...,6}` according to `q*pi/2 <= theta_a(sqrt(t)) <= (q+1)*pi/2`. At a root either adjacent class may be selected. The sign classes, away from zeros, are

`q : 0   1   2   3   4   5   6`
`EO: ++  -+  --  +-  ++  -+  --`.

**Ordering fact.** For ANY two actual members sampled at t_i<t_j and ANY valid phase-class choices q_i,q_j, `q_i <= q_j+1`. Otherwise `q_i>=q_j+2`; t_i is at or beyond its q_i-th root, while t_j is at or before its `(q_j+1)`-st root. The strictly separated global bands put the former root strictly after the latter, contradicting t_i<t_j. If BOTH E/O signs reverse between two nonzero samples, their phase classes cannot be equal or adjacent; the ordering fact therefore forces `q_j>=q_i+2`. If only one sign reverses, it gives the weaker `q_j>=q_i-1`.

At any O-root, E has signs `(-,+,-)` on the three globally ordered O-root bands; at any E-root, O has signs `(+,-,+)` on its three ordered bands. Thus along increasing actual O-roots (respectively E-roots), the other part can change sign at most twice. Since actual a is Hurwitz, E and O never vanish simultaneously at a positive t.

## 3. Exact moments and frequency merging

For an atom at t>=0 define `P_(a,b)(t)=Re[b(i sqrt(t))a(-i sqrt(t))]` and its compactified value `P_(a,b)(t)/(1+t)^7`. At infinity the pairing is b_7. Multiple actual members at the SAME positive t can be replaced by their positive-weight coefficient average because the pairing is affine in a. The average belongs to the SAME K and is Hurwitz; the total positive weight is retained. Merge endpoint atoms analogously at the level of their scalar contributions. No independent artificial E/O data are introduced.

For merged distinct t_1<...<t_m, let `E_j,O_j` be the even/odd evaluations of that actual averaged member, and let `mu_j>0` be its total weight divided by `(1+t_j)^7`. If zero occurs put `eta0=sum_(zero atoms) lambda a_0 >0`, otherwise eta0=0. If infinity occurs put `etaI=sum_(infinity atoms) lambda>0`, otherwise etaI=0. Testing exact annihilation against the eight numerator monomials gives, for k=0,1,2,3,

`sum_j mu_j t_j^k E_j = -eta0 * 1_(k=0)`,
`sum_j mu_j t_j^(k+1) O_j = etaI * 1_(k=3)`.

The infinity sign is as shown because the degree-seven odd monomial has sign `-t^3` in O_b but contributes `+b_7` at infinity. All weights and t_j are positive.

For `H(t)=product_j(t-t_j)`, elementary interpolation gives

`sum_j t_j^k/H'(t_j)=0` for `0<=k<=m-2`,
`sum_j t_j^(m-1)/H'(t_j)=1`,
`sum_j 1/(t_j H'(t_j))=-1/H(0)`.

The first two follow by comparing leading coefficients in Lagrange interpolation; the last follows by evaluating the partial-fraction identity for 1/H at t=0. The moment matrices have full row rank when the distinct-node Vandermonde dimensions permit it. These identities are exact and all-variable.

## 4. Fewer than five positive frequencies

For m<=3, real polynomial interpolation alone rules out an annihilator. Match the actual averaged denominators at all m conjugate frequency pairs, and at zero if present, with a real polynomial c of degree `<2m+e0`. Such interpolation is bijective because a real polynomial of lower degree with all prescribed conjugate-compatible values zero has too many distinct roots. If infinity is absent, c has degree<=7. If infinity is present, add `s^(7-2m-e0) R(s)`, where `R=s^e0 product_j(s^2+t_j)`, so the finite values stay matched and the leading coefficient is1. Every atom then has strictly positive pairing with the test polynomial, contradiction. The empty finite-node case with infinity uses b=s^7.

For m=4, H(0)>0 and the signs of `1/H'(t_j)` are `(-,+,-,+)`. The four-row Vandermonde is invertible.

- With no endpoints the moments force both E_j=0 and O_j=0 at every node, impossible for an actual Hurwitz member.
- With zero only, every O_j=0 and `mu_j E_j=eta0 H(0)/(t_j H'(t_j))`. The E signs alternate four times through three ordered O-root bands, which allow at most two sign changes; impossible.
- With infinity only, every E_j=0 and `mu_j t_j O_j=etaI/H'(t_j)`. The O signs have the same four-term alternation through three E-root bands; impossible.
- With both endpoints, E_j and O_j have the same signs `(-,+,-,+)`, so the sign pairs are `--,++,--,++`. Each of the three transitions reverses both signs and advances the phase class by at least2. The first `--` has q>=2, forcing q_4>=8, but q<=6. Contradiction.

Thus every actual annihilator has m>=5.

## 5. Five positive frequencies and no endpoint

Now H is quintic, `H(0)<0`, and the signs of `1/H'(t_j)` are `(+,-,+,-,+)`. The four-by-five moment matrix has one-dimensional nullspace spanned by `1/H'(t_j)`. With no endpoint, for constants alpha,beta,

`mu_j E_j=alpha/H'(t_j)`, `mu_j t_j O_j=beta/H'(t_j)`.

If alpha and beta are both nonzero, both signs reverse at each of four consecutive transitions; the phase-class ordering forces `q_5>=q_1+8`, impossible since 0<=q<=6. If alpha=0 but beta!=0, all E_j are roots and the O signs alternate four times, contradicting the three ordered E-root bands. If beta=0 but alpha!=0 the analogous O-root argument applies. If both are zero, an actual denominator has E=O=0. Therefore m=5 with no endpoints is impossible.

## 6. Five positive frequencies and exactly one endpoint

The same Vandermonde identities give all solutions of the four moment equations, not just selected candidates. At a possible zero of a numerator factor below, assign either adjacent phase class consistently with the factor's monotone threshold; the global ordering fact in §2 remains valid for both boundary choices.

### Zero present, infinity absent

Put `A=-eta0 H(0)>0`. There are real alpha,beta such that

`mu_j E_j=(alpha-A/t_j)/H'(t_j)`,
`mu_j t_j O_j=beta/H'(t_j)`.

The factor `alpha-A/t` is strictly increasing on t>0 and has at most one sign change from negative to positive.

If beta=0, every O_j=0. The E_j signs are the alternating `(+,-,+,-,+)` signs multiplied by a sequence with at most one sign change. Since E_j cannot vanish along with O_j, there are at least three sign changes, but E on globally ordered O-root bands changes sign at most twice. Contradiction.

Suppose beta!=0. If `alpha-A/t` has no sign switch between the five nodes, every transition reverses both signs and q_5>=q_1+8, impossible. If it switches once, three transitions reverse both signs and the one transition reverses only O. The phase ordering gives `q_5>=q_1+3*2-1>=5`. At the last node the monotone factor is positive and `1/H'(t_5)>0`, so E_5>0, while O_5 has the sign of beta. The final phase class must therefore be one of `0,3,4`, all <5. Contradiction. At a factor-zero node choose the boundary-side sign corresponding to either adjacent class; one of the same zero-or-one-switch arguments applies and E=O=0 is excluded.

### Infinity present, zero absent

There are real alpha,beta such that

`mu_j E_j=alpha/H'(t_j)`,
`mu_j t_j O_j=(beta+etaI t_j)/H'(t_j)`.

The second numerator is strictly increasing in t.

If alpha=0, every E_j=0 and O_j has at least three sign changes (the alternating derivative signs with at most one switch), contrary to the three ordered E-root bands. If alpha!=0 and the second numerator has no switch, all four transitions reverse both signs, impossible. If it switches once, `q_5>=q_1+5`. At the first node the second numerator is negative and `1/H'(t_1)>0`: if alpha>0 the first sign pair is `+-`, so q_1=3; if alpha<0 it is `--`, so q_1>=2. At the last node O_5>0; the final class is at most4 in the first case (`++`) and at most5 in the second (`-+`). Both contradict `q_5>=q_1+5`. A node exactly at the switch is covered by choosing its valid adjacent phase class as above.

Thus neither exactly-one-endpoint case can occur. Together with §5, every m=5 annihilator must contain BOTH endpoints. This is a strict strengthening of merely requiring five positive frequencies; it does not exclude the both-endpoint case.

## 7. Verification boundary and exact residual

This is a universal written proof over every actual independent robustly-Hurwitz septic box. It uses elementary polynomial root/phase continuity, compactness, interpolation, and ordinary real linear algebra, with all specialized uses supplied. In the owner's Eval kernel, a preliminary exact finite phase-class enumeration considered both one-endpoint sign patterns and all monotone threshold placements; no actual a, frequency, endpoint magnitude or counterexample was selected. The final phase-advance proof does not depend on that enumeration. No floating-point calculation, native scientific process, solver or external model was used.

The result requires a complete independent source/whole-proof review, especially common-band extrema, moment signs, factor-zero boundary cases and the phase-advance lemma. It is not formal/kernel/human/configured-family or novelty acceptance. Historical findings/STOP/HOLD/ZERO are neither erased nor proof inputs. The original shared-numerator sign remains OPEN: m=5 with BOTH endpoints and m>=6 remain possible in this theorem, and no actual zero-annihilator or universal common numerator is supplied.

**END.**
