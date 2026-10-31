# Explicit balanced-atom domains for small supports

**Status: WRITTEN with exact integer checks; conditional on the pinned conditioned graph-FD inequality, review pending.** The minimum-atom inequality in `frontier-20261028-balanced-atom-obstruction-v1.md` SHA-256 `94c10a8a86d3603d563b8c91a116496bb19ee6268554e794e60a7d1c36c730a1` gives `Delta<=0` for every original-neighbour R-minus FD law in each domain below:

| Maximum joint-support size | Every positive word probability at least |
|---:|---:|
| 6 | `1/13` |
| 7 | `1/11` |
| 8 | `1/10` |
| 9 | `1/9` |

The first three rows include nonuniform probability regions; the fourth forces the uniform nine-word law when the support has size nine. For instance, no six-word strict-gap law can have positive rational probabilities with a common denominator at most 13.

For each row `(m,d)`, `H(P)<=log2 m` and the pinned minimum-atom criterion gives `Delta<=0` whenever `(20/3)h_2(1/d)>log2 m`. That inequality is equivalent to the exact integer comparison

\[
d^{20d}>(d-1)^{20(d-1)}m^{3d}.
\]

`frontier-20261028-balanced-atom-threshold-check.py` SHA-256 `d9d2639374bfb2a9f099a1bdfaaa0ed068c7624184439fd59ed9124ce46f30dc`, receipt SHA-256 `0fe3911425fcf24a99bee001f489ee76d7757c30451f91aef9d4ccbd5302da53`, checks all four comparisons exactly and rejects the deliberately unsupported `(m,d)=(6,14)` sufficient test. No broader small-support impossibility, numerical guessing-number bound, novelty or independent scientific review is asserted.
