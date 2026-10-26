# Addendum 1 to `PH7-eight-ninths-occupation-derivative-and-case-II-lemmas-v1.md`

This addendum was written right after the base file and before any pin of it. The base file is NOT edited. Owner: MathResearch96h-2.

## The gap

The proof of Proposition 4 in the base file covers only p > 2. Its phrase "on the relevant branch" leaves 0 < p <= 2 unstated, and that range has to be handled before the claim "max_p min(zq, zPhi) = z0*" holds for every p > 0.

## Completion

Take 0 < p <= 2.

- In Phi_z(p), the z-term 98z(2 − p) is >= 0, so the cubic trace gives no upper bound on z here.
- The only remaining constraint is q0 > 0, which means z < zq(p) = (3p² − 4p + 6)/14.
- On (0, 2], zq is convex with its minimum at p = 2/3. So its supremum on that interval is max(zq(0), zq(2)) = max(3/7, 5/7) = 5/7.
- The DISK is not needed: for 1 < p < 3 its left side (p−1)(p−3) is negative.

So zero-variance feasibility with 0 < p <= 2 forces z < 5/7.

The base file already shows z0* > 195/224, and 5/7 = 160/224 < 195/224. Proposition 4 therefore holds for every p > 0: the zero-variance system has a solution only if z < z0*, with 195/224 < z0* < 8/9.

## What does not change

No other statement of the base file changes. These are exact written comparisons only; there is no machine check. The status remains necessary conditions only, with the minimum at 8/9 still in {7,8}.
