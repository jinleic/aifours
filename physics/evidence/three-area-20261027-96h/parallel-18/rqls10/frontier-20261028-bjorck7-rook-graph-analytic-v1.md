# An elementary all-order rook-graph proof for the Björck7 factor

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 23:52:26 PDT 2026**. This removes the finite-clique-enumeration premise from `frontier-20261028-bjorck7-coprime-tensor-no-transversal-v1.md` SHA **61bfa877334178ba64ec822be6c83ddfd301edd621d5f0204a66aa8238764687**, while retaining its restricted-family scope.

## Theorem

Let `a=(-3+sqrt(-7))/4`, and K7 be the circulant matrix with first column `(1,1,1,a,1,a,a)`. For EVERY ordering of K7's source rows, two distinct cells of its cyclic-Fourier-product QLS are orthogonal **if and only if** they share a physical row or share a physical column. Its orthogonality graph is exactly the 7×7 rook graph.

Consequently its only orthogonal seven-cell bases are the seven rows and seven columns. For every positive m coprime to7 and every local source order, the CRT-aligned Fourier-product QLS based on `K7 tensor F_m` has NO orthogonal transversal. This includes infinitely many even orders n=14k with 7 not dividing k. No arbitrary mixed-coordinate source permutations are claimed.

## Proof of the rook graph

The support on which the circulant sequence equals a is `B={3,5,6}` in Z7. Its six ordered nonzero differences are exactly `{1,2,3,4,5,6}`. Therefore any two distinct translates of B intersect once. Comparing any two K columns gives a coordinatewise ratio taking the values `a` twice, `conjugate(a)` twice, and `1` three times, irrespective of source-row order. Since `|a|=1` and `a+conjugate(a)=-3/2`, the ordinary column inner product is `3+2(a+conjugate(a))=0`; K is Hadamard.

Consider cells in different physical rows and different columns. Let zeta be a primitive seventh root, let S_A be the sum of the two zeta-powers at positions with column ratio a, and S_B the sum at positions with ratio conjugate(a). The row difference is nonzero mod7, so the sum of all seven powers is zero. The unnormalized Gram is

`(a-1) S_A + (conjugate(a)-1) S_B = (a-1)(S_A-conjugate(a) S_B)`.

Neither two-term sum can be zero because seventh roots have odd order. If the Gram vanished, `S_A/S_B=conjugate(a)` and hence `|S_A|=|S_B|`. For two unordered distinct seventh-root pairs, equality of their sum magnitudes implies equality up to sign of their index differences: `|zeta^i+zeta^j|²=2+2cos(2pi(i-j)/7)`, and the three possible absolute differences 1,2,3 have distinct cosine values. Thus the two pairs are translates, and `S_A/S_B` is a seventh root of unity. But a is not any root of unity: `a+conjugate(a)=-3/2` is a noninteger rational, whereas a root of unity plus its inverse is an algebraic integer. Contradiction.

Cells in the same physical row are orthogonal by K-column orthogonality; cells in the same column are orthogonal by the Fourier sum. This proves the exact rook graph. Every 7-clique in a rook graph is a full row or full column.

## Tensor implication

For coprime7 and m, CRT factors the Fourier matrix into F7 tensor F_m. A hypothetical `7m` transversal partitions by the m classical F_m-factor rays into m groups of seven; each group is a local row or column. Let R_i be the number of row-i groups, C_j the number of column-j groups, with totals R,C. Global row usage gives `7R_i+C=m=R+C`, so 7 divides R; global column usage similarly implies 7 divides C. Hence 7 divides m, contradicting coprimality. The same argument applies to tensoring this local QLS with ANY classical Latin QLS of order m with 7 not dividing m.

The nonroot cross-ratio `1/a` also proves the tensor matrix is outside every Butson monomial class. The cyclotomic F7-factor field contains Q(sqrt(-7)), so this is not a consequence of the earlier irreducible-Phi7 field theorem. The earlier two independently coded all-order clique computations remain corroboration but are no longer needed for the written proof.

This is not an even-order transversal construction, arbitrary-K no-go, or resolution of unrestricted QLS10. The difference-set, equal-two-root-sum and CRT callers require independent review.
