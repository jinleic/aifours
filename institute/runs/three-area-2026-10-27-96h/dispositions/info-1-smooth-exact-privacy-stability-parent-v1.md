# Parent disposition - smooth exact-privacy approximants, nonattainment and TV exponent barrier (f3)

Observed native clock before writing: **2026-10-28T17:22:10-0700 PDT**. Same-harness written support conditional on one named prior import; not formal/kernel, human, configured-family or novelty acceptance. Frontier-first direction: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Complete reads by Main

| Input | SHA-256 | LF | Read |
|---|---|---|---|
| Candidate `frontier-20261028-smooth-exact-privacy-stability-v1.md` (InfoResearch96h-2) | `40651c034f1800091c1daeb17ea9490fcf9e745fe4c74494381869b5e3626eec` | 217 | raw 1-110 and 110-217 through ending |
| Review `frontier-review-f3-exact-privacy-stability-v1.md` (MathSun8-2) | `3eafa87f5d4e689fa251ae291d50ee72939f1afb9b02f3e17f19f2b79337c009` | 150 | raw 1-150 through ending |
| Assignment `review-waves/f3-exact-privacy-stability/assignment-v1.json` | `a0b94cc177d4e86094e9b4526b0224f66207d4fe2e70b319906df18bcbb93a92` | 20 | frozen before dispatch |
| Prior import: LAW642 parent disposition (previous round) | `c08f6353f121ef9e35da0e9d5e8ec9c87b0da838be0d1adf38b807010a1cd979` | 40 | pinned; statement used at its exact scope, proof not re-reviewed |

## Adopted statement (exact conditional scope)

Fix any finite epsilon > 0, b = exp(-epsilon), D the closed unit l1 diamond, F_epsilon the Borel laws with mu(A) <= b^{-1} mu(A+h) for every Borel A and every h in D, J the squared Euclidean second moment, V its infimum. IMPORT (LAW642, prior-round written support): V is finite and attained by exactly one law mu_* with density p_* = Z^{-1} b^{n(x)}, n(x) = min{k >= 0 : x in S + kD}, S compact convex with 0 in its interior. Let phi be any probability density supported in [-1,1]², symmetric, with kappa = E|U|² > 0 and alpha = P(U1+U2 > 1) > 0, and mu_t = Law(X + tU), X ~ mu_* independent of U ~ phi. Then for every t > 0:

- **A.** mu_t is in F_epsilon (all-event, full closed-shift privacy at the SAME epsilon); for the C-infinity flat bump the density q_t is C-infinity and strictly positive; the shift h = (1,0) and any bounded open rectangle E in the far quadrant {x1, x2 > B + t} give the exact equality mu_t(E) = b^{-1} mu_t(E+h), so the privacy parameter is exactly epsilon.
- **B.** J(mu_t) = V + kappa t². Hence the infimum of J over C-infinity strictly positive exact-epsilon laws (and over continuous-density privacy-at-most-epsilon laws) equals V and is not attained: mu_* has no continuous density version (far-quadrant staircase jump), and uniqueness of the optimal law excludes any continuous-density attainer.
- **C.** W2(mu_t, mu_*) <= sqrt(kappa) t; for all t, TV(mu_t, mu_*) <= t sqrt(kappa) [P(S) + 4 sqrt2 b/(1-b)]/(2Z) (named BV translation and planar Minkowski-perimeter imports); for 0 < t < 1/4, TV(mu_t, mu_*) >= [b^k (1-b) alpha/(2Z)] t with k any integer with c + k > 2B + 8. Consequently TV = Theta(sqrt(J - V)) along this family and no bound TV <= C (J - V)^a with a > 1/2 holds on any cost-gap neighbourhood within the smooth exact-epsilon class. For the triangular kernel kappa = 1/3 and alpha = 1/24 exactly.

## Parent verification

Main reconstructed by hand: the Tonelli argument for all-event privacy at the same shift; the far-quadrant distance formula dist_1(x,S) = x1 + x2 - c and n(x) = ceil(x1 + x2 - c) with closed dilates, giving q_t(x + h) = b q_t(x); the exact second-moment identity (E[U] = 0, E|X| finite); the nonattainment via the a.e.-version discontinuity across the diagonal x1 + x2 = c + k; the pointwise level representation p_* = ((1-b)/Z) sum b^k 1_{K_k} and the perimeter sum ((1-b)/Z) sum b^k (P(S) + 4 sqrt2 k) = [P(S) + 4 sqrt2 b/(1-b)]/Z; the strip lower bound (shell indices k or k+1 only, since u - t(U1+U2) in (-2t, 3t) and t < 1/4; q_t - p_* = Z^{-1} b^k (1-b) P(U1+U2 >= u/t) >= Z^{-1} b^k (1-b) alpha; strip area t; far-quadrant containment from c + k > 2B + 8); and the exponent ratio t^{1-2a} -> infinity. The reviewer's independent rational polygon integration of the synthetic S = D, b = 1/2 staircase (q = 25/18432, shifted 25/36864, ratio 1/2) is diagnostic only.

Reviewer verdict NO_SUBSTANTIVE_DEFECT, 0F/0M/0m at the conditional scope, with the explicit boundary NR-LAW642-PROOF/FULL-PRIOR-AUDITS.

## Not established

LAW642 itself (import); any TV upper modulus for arbitrary near-optimal laws; a uniform-in-epsilon statement; the registered source-equivalence ceiling (PMLR first-norm theorem is not promoted to squared-l1/squared-Euclidean statements); novelty (NR). The earlier S20 continuous-density note is superseded on the infimum question by this additive result, not edited.
