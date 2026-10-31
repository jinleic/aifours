# A common classical orthogonal subsquare is at most half the order

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:10:43 PDT 2026**. This bounds a single block in the constructive OLS-to-QLS extension; it is not a general QLS10 impossibility.

If a Latin square of order N contains a proper Latin subsquare of order k, then `N>=2k`: each of the k subsquare symbols already occurs in each of the k subsquare rows inside the k subsquare columns, so in any outside row those k symbols must all occur in the N-k outside columns. Thus k<=N/2. This applies separately to each classical square of a common subsquare in an orthogonal pair.

Consequently, within the block construction `frontier-20261029-ols-disjoint-block-quantum-extension-v1.md` SHA **3d9eb442e897bea98fb80e1f886955abb925df95820507c8ee0b6ee9e27e1a30**, every proper common block of an OLS10 has size at most5. Since its disjoint symbol sets satisfy `sum_i k_i<=10` and each local block contributes at most `k_i²` new rays, the ray count of such a construction is at most

`10 + sum_i k_i² <= 10 + 5 sum_i k_i <= 60`.

The bound is generous: it ignores overlap with the outside color rays, the nonexistence of a maximal 1RQLS2, and possible incompatibility of common blocks. It proves this proper-block mechanism alone cannot achieve the required 100 rays; it does not rule out a different method or a full-size local QLS10, for which the reduction is tautological.
