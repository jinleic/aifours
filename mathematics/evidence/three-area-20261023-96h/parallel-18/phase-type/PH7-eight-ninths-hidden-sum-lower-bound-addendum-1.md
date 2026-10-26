# Addendum 1 to `PH7-eight-ninths-hidden-sum-lower-bound-v1.md`: sharpened to p > 49/10

The base file is not edited; its SHA256 is `8d71075c806165851ed89c90184f8cc2b683519d6b432e80ca81411fd5fbbc81`. Author: MathResearch96h-2. This addendum uses one exact evaluation and no machine.

## The sharper bound

At the terminating decimal p = 49/10:

    F(49/10) = 45(117.649) − 216(24.01) − 262(4.9) + 1172
             = 5294.205 − 5186.16 − 1283.8 + 1172
             = −3.755 < 0.

## Why this pins the root

Step 4 of the base file shows that F is convex on [p_min, ∞). Here p_min is the positive root of 3p² − 4p − 58/9, and F(p_min) < 0.

A convex function is at most the larger of its two endpoint values on any interval. Both F(p_min) and F(49/10) are negative, so F < 0 on [p_min, 49/10].

The base file also gives F(5) = 87 > 0. Hence:

    49/10 < r_b < 5.

## Consequence

Every actual PH7 at 8/9 has hidden-root sum p > 49/10. Equivalently, the sum of the two hidden eigenvalues is below −4.9. All other statements of the base file are unchanged, and the status remains a necessary condition only.
