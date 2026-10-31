# A compact all-syndrome information inequality

**Status: WRITTEN with exact checked coefficients; scientific review pending.** For any original R-minus FD law on finite group triangle factors, let `S` be the complete vector of all ten factor syndromes, with arbitrary distribution and arbitrarily many values. Let `G` be the four factor-preserving graph automorphisms in `frontier-20261028-common-syndrome-compact-dual-v1.json` SHA-256 `580416bde07e8009210f1e9cef3272c4a465f8693c35cfd67046e6bdbc6353a9`, and write an overline for their average. Then

\[
\boxed{\quad
3\Delta(X)\le
\overline{H(S\mid X_{N(2)})}+
\overline{H(S\mid X_{N(6)})}+
\overline{H(S\mid X_{T_1})}.\quad}\tag{41}
\]

Here `T_1={1,2,3}`. This holds for arbitrary support, factor correlations, and nonabelian finite group alphabets, and uses no two-syndrome theorem. It is a general *syndrome-dependent* restriction, not an improved numerical guessing-number upper bound: the three nonnegative defects need not vanish.

## Proof

The 60-CMI exact identity verified in `frontier-20261028-common-syndrome-compact-dual-check-result.json` SHA-256 `fe63e84172928106831f8e6062da5ad9f0d0226d40d5f466c1e863ce8790f029` represents `Delta` as negative CMI terms plus positive one-third weights for each of the three displayed syndrome-defect rows, three original FD rows, five conditional local-factor FD rows, and the term `-H(S|X_V)`. For the **full** syndrome vector `S`, the latter is zero, as are the original FDs. Every local-factor FD also vanishes because `S` supplies each triangle product and the other two components determine the target component. Multiplying by 3 and dropping the nonpositive CMI sum yields (41). No assumption is made that a triangle or neighbourhood determines the whole syndrome.

More generally, the identity implies the same right side for any functional auxiliary `S` for which the five listed local-factor FDs are valid. For a common binary selector each syndrome defect vanishes, giving the repaired two-syndrome common-selector bound. For general `S`, independent conditional-factor tensorization also gives `3Delta+2 sum_v I(X_v;S)<=3H(S)`. Neither inequality by itself excludes a strict gain; both keep the original target and all quantifiers explicit.
