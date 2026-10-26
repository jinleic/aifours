# Addendum 1 to `PH7-band-closure-through-mid-cycles-v1.md`: the band closure is empty for every z ≥ 4/5

The actual `/bin/date` returned before this addendum was **Sun Oct 25 22:59:02 PDT 2026**. The base file (SHA256 `9a6dad309d82b68e448e7a50ae9d5f143e24ac7ee248885ad3a59d41fde3cdc5`) is NOT edited. Everything below is exact hand algebra; no machine was used.

## 1. General-z form of Delta

The base file states Delta only at z = 8/9. Keeping z symbolic in the same expansion (with Adiff and Bdiff exactly as written there, and the factor 3delta² + 3delta + 1 − 2z) gives

    Delta(delta; z) = 2delta⁷ + 7delta⁶ + (12z+9)delta⁵ + (2z+5)delta⁴
                      + (30z² − 26z + 1)delta³ + (21z² − 24z)delta²
                      + (12z³ − 3z² − 6z)delta + 3z²(2z − 1).

Check: at z = 8/9 every coefficient reduces to the base file's value (59/3, 61/9, 43/27, −128/27, 176/243, 448/243).

The intermediate products are:

- First = delta(3+9delta+8delta²)·Adiff = 8delta⁷ + 25delta⁶ + (32z+29)delta⁵ + (36z+15)delta⁴ + (32z² − 4z + 3)delta³ + (36z² − 18z)delta² + (12z² − 6z)delta.
- Second = Bdiff·(3delta² + 3delta + 1 − 2z) = 6delta⁷ + 18delta⁶ + (20z+20)delta⁵ + (34z+10)delta⁴ + (2z² + 22z + 2)delta³ + (15z² + 6z)delta² + (15z² − 12z³)delta + 3z² − 6z³.

Delta is First − Second.

## 2. Monotonicity in z

Differentiating coefficient by coefficient:

    dDelta/dz = 12delta⁵ + 2delta⁴ + (60z − 26)delta³ + (42z − 24)delta²
                + (36z² − 6z − 6)delta + 18z² − 6z.

For z ≥ 4/5 every coefficient is positive:

- 60z − 26 ≥ 22,
- 42z − 24 ≥ 48/5,
- 36z² − 6z − 6 ≥ 306/25,
- 18z² − 6z ≥ 168/25.

So for each delta > 0, Delta is increasing in z on [4/5, ∞).

## 3. Delta(·; 4/5) > 0 for all delta > 0 (exact)

At z = 4/5,

    125·Delta = 250delta⁷ + 875delta⁶ + 2325delta⁵ + 825delta⁴ − 75delta³ − 720delta² − 72delta + 144.

Split it as P(delta) − N(delta), with

    P = 144 + 825delta⁴ + 2325delta⁵ + 875delta⁶ + 250delta⁷,
    N = 75delta³ + 720delta² + 72delta.

Both P and N are increasing on (0, ∞). Hence on any interval [a, b], 125·Delta ≥ P(a) − N(b). Every value below is exact: the points are terminating decimals.

| interval [a, b] | P(a) | N(b) | margin |
|---|---|---|---|
| [0, 1/3] | 144 | 106.7777… (= 75/27 + 80 + 24) | > 0 |
| [1/3, 2/5] | 144 + 825/81 + 2325/243 + 875/729 + 250/2187 (> 165) | 148.8 | > 16 |
| [2/5, 9/20] | 192.9216 | 185.034375 | 7.8872 |
| [9/20, 1/2] | 228.9329138671875 | 225.375 | 3.5579… |
| [1/2, 11/20] | 283.84375 | 269.878125 | 13.96… |
| [11/20, 3/5] | 364.5329220703125 | 318.6 | 45.9… |
| [3/5, 7/10] | 479.5344 | 428.925 | 50.6… |
| [7/10, 17/20] | 856.3767 | 627.459375 | 228.9… |
| [17/20, 1] | > 144 + 430.655 + 1031.6148 > 1600 | 867 | > 700 |

For [1, ∞): there δ^k ≥ δ³ for k ≥ 3, so P ≥ 144 + 4275δ³ > 867δ³ ≥ N.

So Delta(delta; 4/5) > 0 for every delta > 0. By §2, Delta(delta; z) > 0 for every z ≥ 4/5 and every delta > 0.

## 4. Consequence

Fix z ≥ 4/5 and delta > 0. If 3delta² + 3delta + 1 − 2z ≤ 0, inequality (I) of the base file fails. Otherwise (I) and (II) together need Delta ≤ 0, which is false. At delta = 0 the base file already needs z ≤ 1/2.

**So for EVERY z ≥ 4/5 and every u ≥ 1, the band's holding pattern (u,u,u,w,1,1,1) with arbitrary through-mid cycles cannot realize the PH7 spectrum.**

The supported actual band reaches z_star > 7/9 (parent disposition, per IRC). The supremum of this whole mechanism, over u ≥ 1 and all through-mid cycles, therefore lies in (7/9, 4/5]. It does not reach 0.8, while the target is 8/9 ≈ 0.889. This assumes the u-deformation family's z_new uses u ≥ 1 and this holding pattern; that membership is NOT verified here, so z_new is not ordered by this addendum.

## 5. Scope

This is still a RESTRICTED family. Not covered: u < 1, other holding patterns, cycles avoiding the middle state, other topologies, and Case II. There is no unrestricted 8/9 decision; the minimum stays in {7,8}. HOLD, root, cutoff and deadline are unchanged.
