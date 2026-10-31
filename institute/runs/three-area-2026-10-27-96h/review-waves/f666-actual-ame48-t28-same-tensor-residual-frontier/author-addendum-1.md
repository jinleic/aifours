# Addendum 1: a self-contained excess-four proof and the q=1 line

**Status: author reconstruction, unreviewed; read after `author-candidate-v1.md`.** The observation of the native clock before creating this additive correction was `2026-10-30T15:52:24-0700 PDT`. No scientific executable or selected search was used. The original candidate remains unchanged.

The candidate used the S4 excess-four theorem as a named import. The argument below independently derives precisely the support theorem used there. Subject to independent review of this addendum and the candidate, the combined proof is therefore self-contained from the original same-tensor/unitarity assumptions; it does not require treating S4 as an unproved premise. This prospective reconstruction does not alter the earlier chronology or certify S4's historical source chain.

Also, the transition in candidate Section 3 from `q<=4` to `q in {3,4}` should display the one-line `q=1` exclusion: `sum_x d_i(x)=8`, but one residual symbol has at most six partners, so q=1 is impossible. The already-written argument excludes q=2. No other change to the candidate is intended.

## A. Component facts and low rows

Fix one residual 8-by-8 unitary with 20 nonzeros. Each row and column has degree at least 2: a singleton would have modulus 1 by its norm and would not be residual. If two rows, or two columns, have precisely one common nonzero position, their inner product has one nonzero term and cannot vanish. Every connected bipartite support component is square: an `r`-by-`c` component has both r orthonormal rows and c orthonormal columns, so `r<=c` and `c<=r`. For a component of order m, define its excess by `e=(number of nonzeros)-2m`; it is the sum of `degree-2` on either side and is nonnegative. The total excess is 4.

An excess-zero component is a full 2-by-2 block. To see this, all its rows and columns have degree 2. A row with support `{c,d}` forces every row meeting c to meet d as well. Both columns have degree 2, so their common neighborhood consists of precisely two rows; those rows have no other entries.

We next prove a bound for a connected component of order greater than 2. Call a degree-2 row low. If its two columns are c,d, row orthogonality forbids any other row from meeting exactly one, so c,d have identical row neighborhoods. A second low row cannot use the same pair: the two orthonormal low rows span the two-column space and force every other row to be zero in those columns, isolating a 2-by-2 component. Different low rows therefore use disjoint column pairs.

Each such twin column pair has degree at least 3. If its degree were 2, both columns would be supported on the low row and one other row. Their orthonormality would make that 2-by-2 submatrix unitary, saturating those two rows and isolating the pair. Hence each low row consumes at least 2 units of column excess, and disjointness gives at most `floor(e/2)` low rows. The number of non-low rows is at most e, so

`m <= e + floor(e/2)` for every connected component of order greater than 2.       (A.1)

In particular, an excess-1 component is impossible, since (A.1) would give m<=1. An excess-2 component has m<=3; it cannot have order 2 with positive excess, so it is a 3-by-3 matrix with eight nonzeros, namely the complete 3-by-3 support minus one entry. Its degrees are `(2,3,3)` on both sides.

## B. The excess-four component

An excess-four component has order at most 6 by (A.1). Its order cannot be 6. If it were, there would be exactly two low rows and four degree-3 rows. The low rows' two disjoint twin column pairs each have degree exactly 3, accounting for the entire column excess, so the two remaining columns have degree 2. Each twin pair meets its low row and two high rows. No high row can meet both twin pairs because its degree is only 3; hence the two pairs have disjoint high-row neighborhoods, partitioning the four high rows.

A high row has one additional entry in one of the two remaining columns. That column must also meet the *other* high neighbor of the same twin pair: otherwise it would overlap either twin column only in the chosen high row. Since the additional column has degree 2, it is now saturated. The two high-row pairs therefore use different additional columns, and the component splits into two disjoint 3-by-3 support components. This contradicts connectedness.

In the full residual unitary, if an excess-four component exists, all other components have excess zero and order 2. The remaining order `8-m` is even, so m is even. It cannot be 2 or 6; hence m=4. The only possible row degree multisets, with sum 12 and degrees in `{2,3,4}`, are

`(3,3,3,3)`, `(2,3,3,4)`, `(2,2,4,4)`.

The middle case is impossible. Its unique low row has twin columns c,d. If those columns have degree 3, one of the three non-low rows avoids both and can use at most the other two columns, contradiction. If they have degree 4, all four rows meet c,d, and the other two columns have degree 2 each. The two degree-3 rows each use one of those columns and the degree-4 row uses both. If the degree-3 rows choose the same column, the other has degree 1; if they choose different columns, those columns overlap in exactly the degree-4 row. Both are impossible.

In the `(2,2,4,4)` case, the two low rows have disjoint supports, while the two high rows are full. Consequently all four column degrees are 3. Applying the preceding exclusion to the transpose shows that in the `(3,3,3,3)` row case, the column degrees are either `(3,3,3,3)` or `(2,2,4,4)`. When both sides are 3-regular, the four missing positions form a perfect matching. In the mixed case the two degree-4 lines are full, and the two degree-2 lines on that side use disjoint pairs.

Finally, if there is no excess-four component, the only possible partition of total excess 4 has two excess-2 components: a positive excess-3 component would require an impossible excess-1 component to make up the total, and excess-1 is excluded. The residual orders are therefore `3+3+2`. Otherwise they are `4+2+2`. The resulting pair multiplicity systems are exactly D and Q as stated in the candidate; Q on one side has D on the complementary side, and its two degree-4 lines meet all four degree-3 lines in the same 4-by-4 component. This proves every use of the component theorem in the candidate.

## C. Result and review boundary

Together, the candidate and this addendum give a complete author-written contradiction for the original exact support-48/t=28 complex tensor, with all three flattenings of the same tensor. This is a **candidate proof**, not a parent disposition, a formal/kernel check, a novelty claim, or a statement about the minimum support. The independent review must check this component proof as well as all the case analysis and isolation arguments in the candidate; neither a previously adopted source nor an unobserved computational result substitutes for that review.
