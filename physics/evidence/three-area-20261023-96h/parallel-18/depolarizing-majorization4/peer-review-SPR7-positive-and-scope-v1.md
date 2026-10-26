# Supplied-proof reconstruction — SPR7 positive criterion, application and scope control

Observed review clock: **2026-10-23T15:11:40-0700**. Reviewer PhysicsDepol4, under `peer-review-wave-eighteen-v2.json`. Ordinary in-harness written reconstruction with the supplied sources; not blind, different-model-family, human, formal or novelty verification. No scientific executable, arithmetic interpreter, solver, enumeration, tests, CLI delegation or nested agent was used. Only the named new review file in the reviewer's own root is written.

## 1. Exact pins, actual read coverage and verdict

All three SHA-256 values were observed with `shasum -a 256` and matched the frozen assignment:

| Label | Author source in robust-spr7/ | Observed SHA-256 | Complete read |
|---|---|---|---|
| A | `consolidated-v2-positive-addendum-v1.md` | `be9631c3dae51e4342fb192b932608c43ae6ba954e82cc7d0c2c9ad657fae172` | all 237 lines |
| B | `consolidated-v2-positive-addendum-v2.md` | `d99ec39949ed4198e1916aa09349796c7948fd4d2c2851fc4f7e38589d71ce06` | all 143 lines |
| C | `consolidation-scope-companion-v1.md` | `d0f816590907602e33e0c8843d3be575eb902700e76ca58f45047e8442adecea` | all 127 lines |

Also read the actual `selection-v1.md` in full. Consumed interfaces of `consolidated-v2.md` were read at lines 1–145 and 330–382; its observed SHA is `5d5f8d3708ff3368143289edc8866238603d8ea0c0db33b17eddb854f8fc3c18`. This includes the exact target, pairing convention, classical interlacing statement and the complete two-frequency plant-box exclusion used by B §5. The old shared residue-margin lemma, Routh and dual-lift branches are **not mathematical premises of A's new proof** and were not independently accepted by this review.

**Verdict: 0 FATAL / 0 MAJOR / 1 MINOR precision finding.** The mathematical sufficient criterion, the full-seven-width application for every real L>=1000, and the fixed-midpoint-profile failure for every scalar parameter reconstruct at their literal scopes. The minor concerns calling the parameterized numerator rational when L is allowed to be irrational; it does not affect the real-coefficient synthesis theorem.

## 2. Finding requiring a wording qualification

**MINOR — B lines 9,113,137: rational-coefficient wording with real L.** B fixes **every real** L>=1000 at line 11, while the numerator coefficients in lines 33–37 contain nonzero rational multiples of 1/L. At an irrational L these coefficients are not rational numbers. Therefore the phrases describing an actual rational numerator/rational full-width construction cannot literally mean rational coefficients for the entire stated continuum.

**Consequence:** no defect in the required real polynomial, positivity margins or all-real-L theorem, but a downstream reader must not treat its coefficients as a rational certificate for arbitrary real L.

**Exact repair:** retain the all-real-L quantifier and say an explicit real numerator whose coefficients are rational functions of L, with rational coefficients whenever L is rational. The uniform margin `rho/(24*13^6)` really is rational and independent of L, so that statement needs no change. Do not silently narrow the theorem to rational L.

## 3. Literal scope and classical import boundary

The target is one **real exact-degree-seven** numerator, fixed across the full independent denominator box and all finite real frequencies, with each stipulated denominator Hurwitz before cancellation. The convention is `p(s)=E_p(-s^2)+sO_p(-s^2)` and

`P_(p,b)(t)=E_p(t)E_b(t)+tO_p(t)O_b(t)`,

so the ratio's real part is `P/|p(iw)|^2` at t=w^2. A proves the polynomial pairing before using denominator stability; there is no circular division by a denominator that has not yet been shown nonzero.

The actual classical import is Hermite–Biehler with the explicitly read degree-seven sign convention: positive component constants, negative cubic leading signs, and `e1<o1<e2<o2<e3<o3`. I checked its orientation against the displayed polynomial decomposition and retained it as a named classical theorem; this review does not claim a new proof of the general Hermite–Biehler theorem. Elementary root continuity, partial fractions, degree-two interpolation and Cauchy–Schwarz are the other imports, all used explicitly below.

I also opened the actual Wang–Yu [math/0202242v1](https://arxiv.org/html/math/0202242v1), introduction/SPR definitions, and Xu et al. [2609.26541v2](https://arxiv.org/html/2609.26541v2), formulation and initial interlacing/paired-polynomial interfaces. Their equal-degree conventions and fixed-parity baseline are consistent with the selection. **The announced sextic existence theorem and its Lean development are not imported by this positive packet**, and I did not authenticate its full proof, Lean build or axiom trust. No unread common-numerator existence criterion is used in accepting A/B/C at their stated scopes.

## 4. General positive criterion A reconstructed

### Comparator and all-member residue hypotheses (A 11–49)

The midpoint Q uses only the odd coefficient intervals a2,a4,a6. Since the full family has independent coefficients, Q can be combined with every admissible E_a. If robust stability is initially given, Hermite–Biehler indeed yields simple positive Q roots and signs `E_a(rj)=(-,+,-)`, equal to the signs of Q'(rj), so all residues are positive. The endpoint expressions E_-,E_+ are the true coefficientwise minimum/maximum at each positive node; dividing by either sign of Q' is correctly handled by taking min/max of the two quotients.

Conversely, under A's explicit residue hypotheses, E_a has signs `+,-,+,-` at 0,r1,r2,r3. A cubic has exactly one simple root in each successive interval; these exhaust its degree. Together with the stated leading/constant signs, the nominal polynomial with odd part Q is Hurwitz. This proof does not assume the uncertain a1 is fixed.

### Exact rational identities and uniform loss (A 51–158)

Polynomial division and pole residues give

`E_a/Q=a1+sum_j A_j/(t-rj)`,

`D/Q=4+sum_j rj/(t-rj)`.

Multiplication yields double-pole coefficient rj A_j and simple-pole coefficient

`B_j=A_j[4+sum_(l!=j) rl/(rj-rl)]`

`       +rj[a1+sum_(l!=j) A_l/(rj-rl)]`,

exactly A 120–122. Taking absolute values and a1<=u1 gives the displayed b_j bounds. For `R_a=O_a-Q`, the quotient tR_a/Q has limiting constant `-[t^2]R_a` and simple residue `rj R_a(rj)/Q'(rj)`, establishing A 126–132 for all coefficient deviations.

The constructed numerator has even part epsilon D and odd part Q; expansion gives its leading coefficient one and exact degree seven. Thus its pairing is exactly `tQO_a+epsilon D E_a`. After division by Q^2, the coefficient of each inverse-square pole is epsilon rj A_j, and the inverse-pole coefficient is K_j+epsilon B_j. Completing the square with **half the inverse-square term retained** gives

`P >=(t-Lambda)Q^2+(epsilon/2)sum_j alpha_j Q_j^2`.

The loss is bounded by

`w2+sum_j (k_j+epsilon b_j)^2/(2epsilon alpha_j)`

` =A/epsilon+B+C epsilon`.

All quantities are uniform in the denominator. In particular the uncertain second septic coefficient a1 enters only through a positive quotient constant and the uniform bound u1, so no fixed-a1 hypothesis creeps in.

For A>0, epsilon=sqrt(A/C) achieves the displayed budget B+2sqrt(AC). For A=0, every k_j is zero and positivity of rj makes every odd half-width zero; hence B=0 and epsilon=t0/(2C) gives Lambda=t0/2. C is strictly positive because every b_j includes rj u1>0. The broader square-completion inequality itself is valid for any epsilon>0 with Lambda<t0; B's explicit epsilon is therefore a legitimate use of the proved inequality, not a hidden optimizing assumption.

### Poles, origin, infinity and denominator stability (A 160–214)

The Lagrange identity `sum Q_j/Q'(rj)=1` is an actual degree-at-most-two polynomial identity: it agrees at all three distinct nodes. Consequently `sum Q_j^2>=1/J`, and alpha_min>0 yields the uniform positive constant epsilon alpha_min/(2J) for all t>=t0. Multiplication by Q^2 gives polynomial expressions, so continuity covers all three apparent poles; no root-frequency gap remains.

At 0<=t<=t0<=1, the chosen endpoint bounds imply respectively

`E_a>=l7/2`, `O_a>=l6/2`, `D>=q0/2`, `Q>=q0/2`.

The extra positive constants in the denominators defining t0 make these estimates conservative, not reversed. Thus tQO_a>=0 and epsilon D E_a>=epsilon q0 l7/4, including t=0.

For t>=T=max(2,2r3), `t-Lambda>=t/2` and each `t-rj>=t/2`; hence the pairing is at least t^7/128. Combining the constant bound through T and that tail gives exactly the explicit positive weighted margin in A (8).

Finally, hold the even component fixed and interpolate the odd component from Q to its actual value. The full independent box contains this entire path. The positive polynomial pairing forbids every imaginary-axis crossing, including zero. Monicity, fixed degree and bounded path coefficients prevent roots escaping to infinity. Starting from the nominal Hurwitz polynomial therefore proves actual denominator Hurwitz stability. The numerator does not achieve analyticity by cancellation.

## 5. Full-seven-width application B reconstructed

The literal rho=10^-6 box includes seven independent positive widths, with its constant interval the Minkowski sum of `L(177/10+u)`, 0<=u<=1, and [-rho,rho]. Its even reference expands as

`E0=-t^3+(99/10)t^2-(133/5)t+177/10`.

At Q roots (2,4,6), Q'=(-8,4,-8), and its unperturbed residue intervals have the stated lower bounds `(29/80)L,(57/40)L,(1/16)L` and maximum `(67/40)L`. The largest perturbation factor `(1+r+r^2+r^3)/|Q'|` is `259/8<33`. Thus A_j^->=L/32 and A_j^+<=2L hold uniformly for every real L>=1000.

The regular factors H_j are exactly 1/2,2,13/2. Hence the three pieces in b_j are bounded by14L,12L,12L, giving b_j<=40L. Also alpha_j>=L/16, k_j<=65rho and w2=rho. With epsilon=13rho/(8L),

`epsilon*40L=65rho`, `2epsilon alpha_j>=13rho/64`.

Each completed-square loss is therefore at most `(130rho)^2/(13rho/64)=83200rho`; the total Lambda is at most249601rho. The cross-product comparison with t0 is exact:

`249601*31=7737631<8000000`.

The t0 minimum is genuinely 8/31: the even quotient is at least17/60, the odd quotient at least47/94=1/2, and the Q quotient is48/186=8/31. For the even quotient, `2(1+u5+u1)<=60L` follows from L>=1 and the stated coefficient bounds; no constant1 was silently dropped.

Substituting epsilon into A's numerator expansion reproduces every coefficient in B (1). The weighted lower margin also reconstructs:

`J=3/32`, `epsilon alpha_min/(2J)>=13rho/24`,

`epsilon q0 l7/4>=663rho/2`.

Through T=12 the lower constant is at least13rho/24, which becomes `rho/(24*13^6)` after dividing by13^7. The tail is larger than the same value because `13rho/24<1/128<=12^7/128`. Thus all frequencies, zero and Q's roots are covered with one numerator, throughout the full box.

The consumed plant-box exclusion in consolidation 330–382 also carries to rho=10^-6: it uses only L>=1000 and rho<1/100. At t=101/100 and11/10, the exact alpha values are97311/10^6 and114/125. The common error bound is less than1/100; it forces theta<19/90<1/4 and theta>31/40>3/4. Consequently no numerator inside the plant box works, while B's outside numerator does. This is the same restricted ansatz obstruction, not universal nonsynthesizability or a new independent count.

## 6. Exact scope control C reconstructed

The fixed E factor expands to `-t^3+(4001/2)t^2-751000t+375000`. The odd endpoint estimates are exact throughout c in[2000000,198000000]:

- at t=1/2, the lower bound is7406099/8>0;
- at500, the upper bound is-239500000<0;
- at1500, the lower bound is264500000>0.

These signs force one simple odd root in each of (1/2,500),(500,1500),(1500,infinity), giving the required degree-seven strict Hermite–Biehler ordering for **every** member, including both closed endpoints. The six degenerate coefficient intervals are allowed by the literal original target.

Its midpoint comparator is exactly `Q=-(t-50)(t-1000)(t-2000)`. The derivative profile D has the two stated signs `D(20)=17628000` and `D(30)=-20873000`; D'<0 throughout[20,30], so tau is an exact uniquely isolated positive algebraic root. Q is positive and decreasing on that interval, with Q(20)=58212000<98000000. Hence `O_low(tau)=Q(tau)-98000000<0`.

At that one exact finite frequency, every profile member has

`P_(a_low,b_epsilon)(tau)=tau Q(tau)O_low(tau)<0`,

because D(tau)=0. This holds for **every real epsilon**, not only an unlucky positive choice; positive rescaling cannot change it. Thus robust stability cannot force the fixed-midpoint derivative profile to work universally, even with arbitrarily sharpened budget constants.

This does **not** refute A's sufficient implication: C's family cannot meet a budget that would make that same profile succeed. It does not refute B's explicit different box, rule out another comparator/profile, prove nonsynthesis for unrestricted real degree-seven numerators, or rely on the classically known fixed-even synthesis theorem as a correctness premise.

## 7. Scope and exposure conclusion

The packet supplies an actual positive conditional synthesis theorem with whole-frequency margins and a concrete nonempty full-width application, together with an exact stable-family demonstration that the chosen profile cannot be universal. These statements coexist consistently. The universal SPR7 missing step requires another comparator/profile or positivity mechanism; it is not merely a tighter scalar estimate for the same fixed midpoint profile.

Exposure: the parent supplied all three author proofs and review focus. I reconstructed their load-bearing algebra, inequalities, interval coverage and endpoint/root arguments in writing. No prior review was silently transferred between snapshots. Hermite–Biehler remains an explicit standard import; no unauthenticated sextic/common-numerator or Lean claim is consumed. The sole MINOR wording repair above preserves the all-real-L theorem. Parent acceptance, formal/human verification and literature novelty remain separate.

The bounded review is complete; the reviewer returns to the one owned low-noise four-qubit majorization residual, not an additional weaker-region packet.
