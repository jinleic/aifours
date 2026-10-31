# No 12-cell 4×5 mixed board in a four-family

**WRITTEN author candidate; disjoint review pending.** For any member Q of an ordinary complex four-MOQLS(8), exactly 12 mixed cells relative to a chosen actual Q row cannot occupy four rows and five columns; the incidence transpose is also excluded. Other members are arbitrary complex QLS. This is a complete 4×5 stratum exclusion, not an all-m12 or global four-family conclusion.

Named WRITTEN inputs: the exclusive-axis cycle bound `frontier-20261028-exclusive-axis-cycle-bound-v1.md` SHA256 0464e54938c55b35f45c81074f5736f93edfed4827ce3309d3afa6301939407b and the three-rectangle bridge in `frontier-20261028-mixed12-six-line-obstruction-v1.md` SHA256 bd20c7c8b4c91a754b6ec5c50c01ac8304acad8f971371b3f9ec4fa89b8a826e; both need disjoint review. The 3-space observation proved below is repeated explicitly so no selected calculation or source classification is imported.

## Line and 3-space observations

In a degree-k mixed line, its mixed Q rays form an ONB of a complementary k-axis subspace. A degree-2 line has two rays on a common support-2 set; a degree-3 line has at most one support-2 ray. Distinct orthogonal support-2 sets in the same line are disjoint. In a degree-4 line with at least two support-2 rays, if every ray has support at most 3 then all four rays have support 2, in two disjoint pairs each repeated twice. In a degree-4 line with at least three support-2 rays the fourth has support 2 without needing a separate support-size assumption.

If u_1,u_2 are orthogonal rays on a common support-2 set U and x_1,x_2 are orthogonal full-support-3 rays on T=U∪{z}, they cannot also satisfy x_i⊥u_i for i=1,2. In the ONB u_1,u_2,e_z their inner product has the sole contribution of two nonzero e_z coefficients.

## A reusable all-support-2 12-cell lemma

Suppose there are exactly 12 mixed cells, every mixed Q ray has support 2, every mixed-line degree is 2 or 4, and at least one line has degree 4. Pair the two cells on each line having the same support; along degree-4 lines the two pairs have disjoint supports. Row/column partners partition the 12 cells into simple alternating support-constant cycles. The degree-4 line belongs to two distinct cycles, so the only cycle-length partitions are `(4,8)`, `(6,6)`, and `(4,4,4)`.

With two cycles, their supports are disjoint because they both meet the chosen degree-4 line; each has an exclusive axis. The imported cycle bound applied to a C4 or C6 excludes a four-family. With three C4s, the two rectangles meeting that line have disjoint supports U,V and share the line; their opposite-line sets are disjoint, since otherwise their common row/column cell would lie in both rectangles. Let W be the third support. If W misses U or V, that rectangle has an exclusive axis. Otherwise W meets each of U,V once, and the imported three-rectangle bridge gives at most two mates. Thus the lemma rules out a four-family in either case. Transposing all lines is harmless.

## Column profile (4,2,2,2,2)

Each degree-3 row meets the degree-4 column at most once and would meet at least two degree-2 columns, contradicting the degree-3 fact. The only row profile without degree 3 is `(4,4,2,2)`. Every degree-4 row meets three degree-2 columns, so all its four rays have support 2; the degree-2 rows already have support 2. Apply the all-support-2 lemma.

## Column profile (3,3,2,2,2)

Every ray has support at most 3. The row profiles are `(5,3,2,2)`, `(4,4,2,2)`, `(4,3,3,2)`, and `(3,3,3,3)`.

* `(3,3,3,3)`: six incidences lie in degree-2 columns. Some degree-3 row would meet at least two, impossible.

* `(4,4,2,2)`: a degree-3 column can meet at most one degree-2 row, hence meets both degree-4 rows and one degree-2 row. Each degree-4 row meets both high columns and two low columns; its two support-2 low rays force all its rays to have support 2. Each high column then contains at least two support-2 rays, impossible.

* `(4,3,3,2)`: each degree-3 row meets at most one low column and hence meets both high columns. Each high column has only one further incidence. If the degree-4 row meets both, its two low-column rays force all its rays to have support 2; its two high-column support-2 rays are orthogonal and, as the two high columns have the same 3-axis subspace T determined by either degree-3 row, must have the same support U. The two degree-3-row high rays are full-support T, orthogonal, and each is orthogonal to its corresponding U ray, contradicting the 3-space observation.

  If instead the degree-4 row meets only one high column, the degree-2 row meets the other. Each high column has its unique support-2 ray on the degree-4 or degree-2 row, so both degree-3 rows' high rays have full support 3 and the two high-column subspaces coincide at T. The degree-4 row meets all three low columns and has three support-2 low rays, so its high ray also has support 2 and its four support sets are U,U,V,V disjoint. Each of its low-column partner rays lies in a degree-3 row or the degree-2 row; all those partner supports lie in T, as does the high ray. Thus T contains U∪V, four axes, contradiction. The degree-4 row cannot miss both high columns because there are only three low columns.

* `(5,3,2,2)`: the degree-5 row meets every column. The degree-3 row meets both high columns and exactly one low column. Each high column can meet at most one degree-2 row and hence meets the degree-5 row, the degree-3 row, and exactly one low row. The two degree-3-row high rays have full support on a common 3-set T, and so both high-column mixed subspaces are T; their degree-5-row rays have full support T too. The degree-3 row's low ray has support U⊂T; its low-column partner in the degree-5 row has the same support. In that row this support-U ray and the two high rays are orthogonal and span T. The other two rays must lie in the 2-axis complement of T within the row's 5-axis subspace, and hence share a support V disjoint from T.

  If each degree-2 row meets one high and one low column, its two rays share support V by their low-column partner, but its high ray must lie in T, contradiction. Otherwise one degree-2 row meets both high columns and its two rays share a support W⊂T; the other meets both low columns. The degree-3 row's two full-T high rays are orthogonal and each is orthogonal to the corresponding W ray in its column, contradicting the 3-space observation.

All row/column profiles are excluded. This does not settle the remaining 4×4 12-cell board, the original four-family question, numerical M(8), original A10/A11 or novelty. Full independent mathematical review must check the mixed-column neighbor counts, both degree-5-row alternatives, the cycle/bridge imports and the arbitrary-complex nonzero-coordinate claims. No parent, formal, human, configured-family or executable verdict is asserted.
