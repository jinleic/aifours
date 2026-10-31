# Parity contexts and a 2-adic obstruction for 1-resolvable QLS

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 22:38:47 PDT 2026**. This gives a new SAME-vector consequence for a class of non-Fourier 1-RQLSs, not an unrestricted no-go. The original maximal 1-RQLS10 remains open.

## 1. Odd incidence kernel ⇒ parity contextuality

Let L be the Latin square whose labels index a fixed 1-resolution of a QLS(n). Select row, column and transversal labels via bits `a_r,b_c,h_l` satisfying

`a_r + b_c + h_(L(r,c)) = 0 mod2` for every cell.                 (1)

If the total number of selected blocks `sum a + sum b + sum h` is odd, then the selected ONBs form a parity Kochen–Specker configuration: each cell lies in either0 or2 selected ONBs, so after identifying coincident rays each actual ray appears an even number of times. A noncontextual 0/1 assignment with exactly one 1 per ONB would have an odd total when counted by blocks and an even total when counted by rays. This is an implication from an actual QLS; parity contextuality itself is not a contradiction to quantum mechanics.

The EXACT finite test is the odd-weight kernel of the `n² × 3n` incidence matrix over F2; it depends only on L, not on a selected classical mate or on a floating Gram matrix.

## 2. Complete characterization of this parity mechanism

For n even, every solution of (1) is either a constant solution with even weight, or a nonconstant balanced quotient

`h(L(r,c)) = a_r + b_c` over F2, with exactly n/2 ones in EACH of a,b,h.

To prove this, if h is constant then the equation forces a,b constant. If h is nonconstant, neither a nor b can be constant: for example, constant a would make h constant on every label appearing in each column, but each column is a permutation of all labels. Both values of a therefore occur. Let k be the number of1 symbols in h. A row with a_r=0 has k ones in b, and a row with a_r=1 has n−k; hence k=n/2 and b has n/2 ones. Using columns analogously gives n/2 ones in a.

Thus an odd incidence-kernel vector exists EXACTLY when `n≡2 mod4` and L admits this nontrivial balanced two-color quotient. For n odd, a nonconstant quotient is impossible by the same count; constants still have even total weight. A cyclic label square at n=2m, m odd, has the quotient `a_r=r mod2`, `b_c=c mod2`, `h_l=l mod2`.

## 3. Order10: 15 ONBs and an actual 2-local no-go

For n=10 and such an L, exactly15 of the30 ONBs are selected;25 cells occur0 times and75 cells occur2 times. In a maximal-cardinality QLS10 those75 cells are 75 distinct rays, each in exactly2 of the15 contexts. The context-incidence graph is the complete tripartite graph K_(5,5,5): contexts are the five selected rows, columns and transversal labels, and their pairwise intersections are the 75 rays. With repeated rays the parity proof remains valid after identifying rays, but the graph need not be a simple faithful ray-incidence graph.

Summing the 15 ONB projector identities gives an exact SAME-array identity

`2 * sum_(75 selected cells) P_(r,c) = 15 I_10`.                 (2)

Therefore no such QLS can have all selected rank-one projector entries rational with ODD denominators in any one common basis: the left diagonal entries are even in Z_(2), whereas15 is odd. More generally, if all those projector entries lie in the valuation ring of a prime over2 of a number field F in some common basis, the left side is divisible by2 and the right side is a unit, also impossible. This is a genuine no-go only under the named 2-integrality and quotient premises; it does NOT impose either premise on arbitrary QLSs or on all Fourier products.

## 4. Exact reference checks and scope

`frontier-20261028-resolution-parity-code-v1.py` SHA **56b6b388c25210c4e5212208dcfb13cca25abaabb684c70b92c72f07c20abbc1**, result SHA **ff33ef2b1a5d66d5db79c7043b504739db212c54af684d8110b78a602ce8af71**, independently computes an F2 nullspace and enumerates all1024 symbol bit patterns. For the cyclic order10 label square the kernel dimension is3 and an odd vector selects15 contexts/75 double-occurring cells. For the Weisner Fig.1 and Parker reference label squares, the dimension is2 with ONLY constant solutions and no odd vector. The Parker13-ray exact witness has denominator3, so its projector entries have denominators dividing9; its quotient-free label square avoids (2). This does NOT classify the other order10 resolutions.

The preceding 2-sparse obstruction and all-even Fourier family results are separate. An even cyclic-Fourier counterexample in dimension10 would induce a parity KS configuration, but contextuality is allowed and no contradiction is asserted. The 2-local algebra, label-kernel characterization, incidence extraction and exact references require independent review.
