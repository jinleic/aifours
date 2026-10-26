# Every PH7 at 8/9 has hidden-root sum p > 47/10 (unrestricted necessary condition)

Actual `/bin/date` before this manuscript: **Sun Oct 25 23:13:09 PDT 2026**. Owner: MathResearch96h-2, math-1.

Status: AUTHOR-WRITTEN CANDIDATE. Exact, but only a NECESSARY condition. It is not a decision at 8/9; the minimum stays in {7,8}.

No interpreter, eval, calculator, CAS, solver or replay was used. Every step below is a hand polynomial identity, an exact rational sign evaluation, or a discriminant.

Private approximate explorations of the trace region (disclosed in checkpoints 056/057) carry ZERO credit. Nothing here depends on them.

## 1. Setting and imports

Use d = 1 and z = 8/9. Let G = T + cI for an actual PH7 pair. By the SCC/Perron-coordinate theorem (`PH7-reducible-obstruction-and-Perron-coordinates-v1.md`, SHA256 `d0dea4e8ffdf8132dfa2460c7cc40a01e8834bcc47e981837f28410f605fd242`):

- G is Metzler;
- det(yI−G) = D_z(y)Q(y) with Q = y² + py + q;
- p > 0 and q > 0.

The only further import is Lemma M of B6 (`proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`, §2). For every real n×n Metzler X with tr X = 0:

    tr X³ ≥ −((n−2)/sqrt(n(n−1)))·(tr X²)^(3/2).

No topology, holding pattern, input/exit or class assumption is made. The argument is purely spectral, so it applies to any 7×7 Metzler matrix with this spectrum.

## 2. Exact trace formulas

Put a = (4+p)/7, X = G + aI and A = tr X², the variance in the strict-Perron packet. From the spectrum, by hand expansion of symmetric functions:

    q  = q0(p) − A/2,       q0(p) = (3p² − 4p − 58/9)/7,
    tr X³ = (3/49)·Phi(p) − (3(5p−8)/14)·A,
    9·Phi(p) = F(p) := 45p³ − 216p² − 262p + 1172.

At A = 0 these reduce to the strict-Perron packet's formulas (q = q0 and tr B³ = F/147). The A-term comes from the q-coefficient of tr X³, which is 3(5p−8)/7.

## 3. Theorem

**Every actual PH7 at z = 8/9 satisfies F(p) ≥ 0. Hence p ≥ r_b, where r_b is the largest real root of F, and 47/10 < r_b < 5.**

*Proof.* Write c = 3(5p−8)/14 and kappa = 5/sqrt42. Lemma M with n = 7 reads

    g(A) := (3/49)·Phi(p) − cA + kappa·A^(3/2) ≥ 0.

**Step 1: an admissible A must exceed A\* := (c/kappa)² whenever F(p) < 0.** If p ≤ 8/5, then q0(p) < 0, hence q < 0, which is impossible. So p > 8/5 and c > 0. For 0 ≤ A ≤ A\*, cA − kappa·A^(3/2) = A(c − kappa·sqrt(A)) ≥ 0. Therefore F(p) < 0 together with A ≤ A\* gives g(A) < 0.

**Step 2: q > 0 forces A < 2q0(p) ≤ A\*.** Here A\* = 27(5p−8)²/350. Then A\* ≥ 2q0(p) is equivalent to

    375p² − 1760p + 21352/9 ≥ 0.

Its discriminant is 1760² − 1500·21352/9 = 3097600 − 32028000/9 < 0. So the inequality holds for every real p.

**Step 3: F(p) < 0 is impossible.** Steps 1–2 show that F(p) < 0 admits no A at all. Hence F(p) ≥ 0. (If q0(p) ≤ 0, then q > 0 already fails for every A > 0.)

**Step 4: location of the root.** Exact rational evaluations:

- F(2) = 144 > 0;
- F(47/10) = −158.805 < 0;
- F(5) = 87 > 0.

The strict-Perron packet proves F(p_min) < −28/9, where p_min is the positive root of 3p² − 4p − 58/9. Since F'' = 270p − 432 > 0 for p > 8/5, F is convex on [p_min, ∞). So F < 0 on [p_min, 47/10]. Therefore F has its largest root r_b in (47/10, 5), and F < 0 on [p_min, r_b).

Finally, q > 0 forces p > p_min. Combined with F(p) ≥ 0, this gives p ≥ r_b. ∎

## 4. Remarks

- **The hidden pair must be deep.** The sum of the two hidden eigenvalues is ≤ −r_b < −47/10, about 4.7 times the real part of the visible pair. Any construction search at 8/9 must aim there.
- **Consistency with the supported band.** The analogous cubic at z = 7/9 is 9·Phi_(7/9)(p) = 45p³ − 216p² − (164)p + (976). The band's p lies in (19/4, 24/5) and satisfies this condition.
- **Range of validity of Step 2.** At general z, Step 2 needs 375p² − 1760p + 1128 + 1400z > 0 for all p, which holds exactly when z > 7028/10500. Below that, large-variance configurations are not excluded by this argument.
- **Scope.** This is necessary and spectrum-only. It cannot decide 8/9, because 7×7 spectra with p ≥ r_b may exist.

No formal, kernel, cross-vendor or novelty acceptance is claimed. HOLD, root, cutoff and deadline are unchanged.
