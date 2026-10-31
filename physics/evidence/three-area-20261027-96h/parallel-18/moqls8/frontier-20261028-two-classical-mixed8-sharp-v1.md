# A sharp eight-mixed-cell bound for a quantum Latin square with two classical mates

**Status: WRITTEN author candidate plus owner-local exact finite witness checks; independently owned physical verification, source/priority audit and mathematical review are pending.**

Let Q be a nonclassical ordinary complex QLS(8) orthogonal to two classical QLS A,B. Choose any one of the four line classes—rows, columns, A symbols or B symbols—and any actual line in that class. Use Q's eight rays on that line as its coordinate ONB. Then **at least eight of Q's 64 cells are not first-row-basis rays** (equivalently, have support size at least two in that basis). The bound holds for arbitrary complex amplitudes and phases and does not require a fourth square, a catalogue or Hcat. It strengthens the earlier ≥6 observation in `frontier-20261028-max2-transversal-capacity-v1.md` SHA256 484d32d8b1ba02cc2b26925e08469d5232514920896051e519ba74645646cd8e.

The explicit three-member example in §4 has exactly eight such cells in a chosen first-row basis, so the bound is sharp for a QLS with two classical mates, subject to independent verification of the finite witness. It is **not** a four-family witness. No claim of a numerical M(8) update, novelty, priority, formal/human/model-family acceptance or A10/A11 closure is made in this packet.

## 1. Four actual net-line ONBs and local line lemmas

The rows, columns and A/B symbol classes form a four-net. Q is an ONB on every line: on an A- or B-symbol line its mate ray is equal, and actual product-ONB orthogonality makes the Q rays pairwise orthogonal. Any two distinct cells share at most one net line. After reindexing the chosen line as row 0, its Q rays are e_j; a *light* cell is a ray e_j up to phase and a *mixed* cell is any other ray.

A line containing a mixed vector contains at least two mixed cells. Indeed, a mixed vector has at least two occupied first-row coordinates, so each of those squared magnitudes is strictly below 1. No light vector on the same line can occupy such an axis, and the ONB resolution of identity requires another mixed vector with nonzero coefficient there.

If a line contains exactly k mixed cells, its 8−k light vectors occupy distinct coordinate axes; all k mixed vectors lie in the orthogonal complement of those axes, a k-dimensional coordinate space, and form an ONB of it. In particular:

- for k=2, both mixed vectors have **the same two-axis support**, since each is non-singleton;
- for k=3, at most one of the three mixed vectors has support size 2. Two distinct 2-subsets of three axes intersect in one axis and cannot be orthogonal; if the two supports coincide, the two orthogonal vectors span that two-space and force the third vector to be the remaining singleton. Thus at least two have support size 3.

These are statements about actual ONBs, not abstract graph colorings.

## 2. Excluding five and six mixed cells

Let H be the set of mixed cells. Pick x∈H. Each of the four distinct net lines through x contains another mixed cell, and those four other cells are distinct, so `|H|≥5`.

If `|H|=5`, write H as x and four cells y_c, where y_c is the unique other mixed cell on the line of class c through x. Every y_c needs another mixed cell on each of its other three class-lines; the only available cells are the other three y's, and each lies on a different one of those lines. Fix a class c. The point y_c is already paired with x on its c-line, while each of the other three y's requires exactly one c-line neighbor among themselves. That would be a matching with three degree-one vertices, impossible. Thus five is impossible.

Now suppose `|H|=6`. A line with k mixed cells has `|H|≥k+3`: from any cell on it, the other three class-lines each require a distinct mixed point outside the line. Hence k≤3.

- If all nonempty mixed lines have size 2, the mixed-cell graph has degree 4 on six vertices and is `K_6` minus a perfect matching. It is connected and contains a triangle. The line lemma forces equal two-axis supports along every edge, hence the three triangle rays are mutually orthogonal nonzero vectors in one two-dimensional space, impossible.
- If some line has exactly three mixed cells x,y,z, its other three mixed cells a,b,c must each be connected to each of x,y,z on the other three class-lines: each triple point needs one point on each of its three remaining lines, and there are only three outside. At each outside point those three connections use distinct classes, so its remaining parallel-class line needs another outside mixed cell. With only three outside points, they must all lie on one parallel line. Every crossing line then contains exactly two mixed cells, so the line lemma makes x,y,z all support-size 2. But a three-mixed ONB line has at most one such ray. Contradiction.

Thus six is impossible.

## 3. Excluding seven mixed cells

Suppose `|H|=7`. A line with k mixed cells again has `k≤4`. If a line had four, each of its four points would need one mixed point on each of the other three class-lines. Only three mixed points lie outside, so every outside point would have to connect to all four points of the first line. Those four connections require four distinct nonparallel classes—two points already sharing the first line cannot share another—yet only three other classes exist. So no line has four mixed points.

If all nonempty mixed lines had size 2, each of the four classes would partition the seven mixed points into pairs, impossible by parity. Hence some line L contains exactly three mixed cells x,y,z. The other four mixed cells, on lines parallel to L, cannot be singletons or lie four on one line, so they form two parallel mixed pairs.

By the three-mixed-line lemma, at least one of x,y,z has support size 3; call it x. Each of the other three class-lines through x contains another mixed cell. If any contained exactly two mixed cells, the two-line lemma would force x to have support size 2. Hence each contains at least three. It cannot contain a second L-point, nor two points from the same outside parallel pair, because any two cells share at most one net line. Therefore each of the three lines through x contains one point from **each** outside pair. Distinct lines through x require three distinct points from each pair, but each pair has only two. Contradiction.

No count below eight remains, proving the bound.

## 4. Explicit sharp three-family witness

In the following table `+ = (e_0+e_1)/sqrt(2)` and `− = (e_0−e_1)/sqrt(2)`; integers denote first-row coordinate rays. The two displayed classical matrices use ordinary basis symbols 0–7. All three matrices share the same row/column grid.

```text
Q                  A          B
0 1 2 3 4 5 6 7    01234567   01234567
1 0 3 2 6 7 4 5    32107654   45670123
3 2 + − 7 6 5 4    54761032   10325476
2 3 − + 5 4 7 6    67452301   54761032
4 5 6 7 − + 2 3    10325476   76543210
6 7 4 5 + − 3 2    23016745   32107654
7 6 5 4 3 2 1 0    45670123   67452301
5 4 7 6 2 3 0 1    76543210   23016745
```

The eight mixed cells are zero-based linear indices `[18,19,26,27,36,37,44,45]`. Q's first row is e_0,...,e_7 and a mixed ray is not collinear with any of them, so Q is nonclassical. The construction rotates one two-symbol eight-cell trade of a source classical triple; the direct witness check does **not** rely on the trade mechanism or any catalogue completeness assumption.

The exact witness `frontier-20261028-three-family-mixed8-witness-v1.json` is SHA256 **a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413**; it encodes each real Q vector by an integer numerator and denominator squared 1 or 2. Producer `frontier-20261028-three-family-mixed8-witness-v1.py` SHA256 92a004171e6096e8298ed648c24452e3cea5e223134b3f9c183089531b36849e; receipt SHA256 bbd3e495ef0a4c6301f6bc2b1a944c62f77e005bf6920d517bb3e18c9bef0b9b.

The independent exact `Q(sqrt(2))` checker `frontier-20261028-three-family-mixed8-witness-check-v1.py` SHA256 7eb892b0a2e70398cd8917698143a117501b0a0440c2094ccf20983b4ad76662 (receipt SHA256 2b5d1064a29fe8664bf9446dff4b952107bc1d6f2178f556dad3f853eba55ec7) checks **1,536 row Gram entries, 1,536 column Gram entries and all 12,288 pair-product Gram entries**, all zero errors, with distinct quantum/classical duplicate mutations rejected. A third separately coded standard-library verifier explicitly constructs the 64-dimensional tensor-product vectors rather than multiplying pairwise Gram entries: `frontier-20261028-three-family-explicit-tensor-check-v1.py` SHA256 92379d1b6ed098b995e93bdfbf7216a34f33af404cd69f7a10976c3cb5e2bf5f, receipt SHA256 **db4d37227bbd7c7417d6a96f04462405f5632d795772c4e168cc7295a965bcb6**. It also checks an independently constructed GF(4) three-MOLS positive instance and rejects quantum duplicate, duplicate-mate, missing-cell, wrong-norm, out-of-range and wrong-hash mutations for their named reasons.

The same explicit-tensor checker and six intended-reason controls also passed under `python3 -O -B`; receipt `frontier-20261028-three-family-explicit-tensor-check-optimized-receipt-v1.json` SHA256 fad8819d126e7eb773562549502001a62eeb8e3674fa3e3b73625eee36d96f7a. This is a second interpreter mode of the same checker, not a fourth independent implementation.

These are owner-local independent implementations, not a separately owned witness verdict. The parent is performing independent literal physical verification and source-definition/priority audit. A disjoint reviewer should also reconstruct the m≤7 argument, check all four net-line uses and independently verify the exact witness. No numerical or novelty upgrade is claimed until those gates complete.
