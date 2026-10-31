# Three-state conditional information bounds from one-hot exclusion

**Status: WRITTEN; scientific review pending.** For any finite random variables `S,X`, where `S` has at most three labelled values and `S_j=1{S=j}`,

\[
\frac53H(S\mid X)\le\sum_jH(S_j\mid X)\le2H(S\mid X).
\tag{47}
\]

The left inequality is the exact KL argument in `frontier-20261028-three-state-exclusion-entropy-v1.md` SHA-256 `9c5ee203ba255776702e93e90b958663e98a43ebfb3b522b97898381116785e7`; the right inequality is its addendum SHA-256 `a2f68e7268f05244ffb224b457df94083e3125c4fcf545d6b149f1bcb9c853ce`. Subtracting conditional from unconditional indicator entropies yields the useful bounded **difference**

\[
\frac53H(S)-2H(S\mid X)
\le\sum_j I(S_j;X)
\le2H(S)-\frac53H(S\mid X).\tag{48}
\]

These are distribution-free and require no original graph FD, group representation, two-syndrome theorem, or continuity beyond standard finite entropy conventions. They apply separately to any neighbourhood tuple or triangle tuple appearing in the compact all-syndrome inequality. They do not establish a global no-gap bound: lower bounds may be negative and simultaneous attainability is not asserted. For strictly positive `Delta`, combining (48) with the conditional two-syndrome gates requires independent scientific acceptance of the repaired two-syndrome theorem; the bound (47) itself does not.
