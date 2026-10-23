# Addendum 1 to restricted-results-v1.md: R7 (qubit x MUB product ansatz)

Written about 14:50 PDT, 2026-10-18. Lane-internal derivation, **unreviewed**, restricted ansatz only. It is not a
statement about arbitrary vectors.

## R7. Product vectors sigma (x) e with e taken from pairwise non-orthogonal bases of C^5

### Ansatz

- Identify C^10 with C^2 (x) C^5 by any fixed unitary.
- Each cell p gets q_p = sigma_p (x) e_p, where sigma_p is any unit vector in C^2.
- e_p lies in M = M_1 u ... u M_r, a union of orthonormal bases of C^5. These bases are *pairwise non-orthogonal*:
  no vector of M_i is orthogonal to any vector of M_j for i != j. Example: any family of MUBs, such as the six
  Weyl-Heisenberg MUBs of C^5.
- The square is a 1-RQLS(10) with lines = rows, columns and classes of some Latin square B.
- Rays: q_p is parallel to q_p' iff sigma_p is parallel to sigma_p' and e_p is parallel to e_p'. This is the
  standard product-ray fact [IMPORT: Zhang-Cao Lemma 4.5, from their reference].

### Lemma 7.1: structure of a product ONB line

Group the qubit rays of a line into antipodal classes (axes). Then exactly one of the following holds:

- **(H)** One axis {tau, tau^perp} only. The 5 tau-cells have C^5 parts forming one basis M_i, and the 5 tau^perp-cells
  have C^5 parts forming one basis M_j.
- **(P)** At least 2 axes. All C^5 parts lie in a single basis M_i, and each occurring e occurs exactly twice, with
  antipodal qubit parts.

*Proof.*
1. Choose one ray from each axis. The vectors whose qubit parts are among the chosen rays have pairwise
   non-orthogonal qubit parts. So their C^5 parts are pairwise orthogonal, hence distinct, and there are at most 5.
2. With m axes, each vector lies in 2^{m-1} of the 2^m choices. Summing over choices gives
   10 * 2^{m-1} <= 5 * 2^m, which is an equality. So every choice gives exactly 5 vectors, and they form an ONB of
   C^5 inside M.
3. Any two orthogonal vectors of M lie in the same basis, so that ONB is a whole basis M_i.
4. Comparing two choices that differ on one axis gives m^+ = m^- for that axis.
5. If m >= 2, the remaining part of a choice is nonempty, so two such choices share their basis. Hence the C^5 parts
   at + and at - coincide on each axis. QED

### Lemma 7.2: partners

If two distinct cells on a common line have the same C^5 ray, their qubit parts are orthogonal, because
<e,e> != 0.

### Claim R7

No such configuration has 100 pairwise non-parallel rays.

*Proof.* Call a line *paired* if every C^5 ray in it occurs twice; this is (P), or (H) with i = j. Call it *bi*
otherwise; a bi-line is (H) with i != j and has a single qubit axis. Assume all rays are distinct.

1. **One paired line per cell.** Suppose cell p lies on two paired lines L1 != L2. Then e_p recurs at p1 in L1 and at
   p2 in L2, with p1 != p2. Both have qubit part sigma_p^perp by Lemma 7.2. So q_p1 is parallel to q_p2, a
   contradiction.
2. **Paired lines share a direction.** Lines of different directions always meet: row and column, row and class,
   column and class. So all paired lines lie in a single direction, if any exist.
3. **One global axis.** Hence two directions D and D' consist only of bi-lines. Each line of D meets each line of D'
   in exactly one cell, so all their axes coincide. Every cell lies on a line of D, so every qubit part is tau or
   tau^perp.
4. **Half-lines collapse.** By (H), every line splits into 5 tau-cells and 5 tau^perp-cells. The C^5 parts of each
   half form one basis of M. All three half-lines through p contain e_p, so they use the same basis. By connectivity,
   all half-lines of a connected tau-component use one basis M_i.
5. **A repeat is forced.** Take p in such a component C with e_p = e. Pick f in M_i with f != e. The f-cells r (in
   the row of p) and c (in the column of p) are distinct and lie in C. The column of r contains a tau-cell with ray e
   other than p. So two cells of C carry the same ray (tau, e), contradicting distinctness. QED

### Remarks

- **The classes are essential.** With rows and columns only, there is a QLS(10) with 100 distinct product rays: rows of
  type (P), columns of type (H) with 5 different qubit axes. This matches the known existence of maximal-cardinality
  QLS(10), so R7 says nothing about plain QLS.
- **Not covered:**
  - general e_p in C^5, where (P)-lines have arbitrary orthogonal decompositions into subspaces V_a with two different
    ONBs per V_a;
  - non-product vectors.
