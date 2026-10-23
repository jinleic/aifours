# K62-DT-B-v1: Part B of the DG case analysis — the generic sub-case: degree bounds, no K4, at most one "free" family [CANDIDATE]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:32:29-0700.
- **Author:** Sun63Successor; single author, unreviewed, written only (HOLD in force; nothing run).
- **Labels.** B1-B3 use the 5/6 row bounds of `K62-CAP-v1.md` (C) (candidate, sha256
  19dccc3d8bce5908a14ff96462a05beeb38ba966374c8c4740e6a66a312b16d5) and are otherwise unconditional. **B4-B5 are
  CONDITIONAL ON DG** (`K62-DG-v1.md` a4bfc41e… + erratum e435430c…, under dual review) and use Lemma CI of
  `K62-DT-A-v1.md` (sha256 cd7266d4071a8c91ac753b1f9900d690b72cf667f74046a1f90b5b449afd1a70). Imports as in Part A, plus
  accepted K62-E3 Lemma 2 (at most two entries 1 in an O-row) and C2.

## 0. The generic sub-case G
**G:** no vertex of O carries a marker (the 3-marker is on i* or absent; the 5-marker is on d, on i*, or absent),
e_d >= 4, e* = 2. Then (alpha_(d i*), alpha*_(d i*)) = (1, 1) (K62-E3 Lemma 1), both families satisfy x_(d i*) = 1, every
O-vertex is unmarked, and at every v in O the alpha-row and the alpha*-row satisfy the 5/6 bound (K62-CAP (C)): every
feasible y has val(y) := sum over O-neighbours u of y_u x_vu + y_(i*) x_(v i*) + 3 y_d <= 5 (units of 1/6). In G the label
of an O-neighbour u at v has {2,3,5}-type x_vu exactly; the label of i* has 2-part 2^(1 + v2 x_(v i*)) and shares no odd
prime with an O-label; the label of d has 2-part >= 8 and shares no odd prime with an O-label or with the i*-label. So an
entry 1 is isolated, entries 2 and 4 have 2-adic valuations 1 and 2, and d has valuation >= 3.

## 1. Two row facts (G; any v in O; either orientation)
- **(R4)** A row whose four O-entries all lie in {1, 2} violates the 5/6 bound.
  Certificate: y = 1 on entries 1, 1/2 on entries 2, y_d = 1/2, all else 0. Feasible: entries 1 are isolated; an allowed
  set with >= 3 elements contains at most one element of 2-adic valuation 1 (otherwise all its pairwise gcds through
  those two elements are 2 and, with d, no pair reaches 3: Sun(3)), so positive-weight sets are singletons, pairs
  (sum <= 1) and nothing larger. Values: (2,2,2,2): 4 + 3/2; (2,2,2,1): 1 + 3 + 3/2; (2,2,1,1): 2 + 2 + 3/2; all 11/2 > 5.
  Rows with three or four entries 1 are excluded by K62-E3 Lemma 2.
- **(R3)** A row whose O-entries are three entries in {1, 2} and one entry 4, and whose i*-entry is odd, violates the
  5/6 bound. Certificate: y = 1 on entries 1, 1/2 on entries 2, on the 4 and on i*, y_d = 0. The i*-label then has
  2-adic valuation 1, so the elements of valuation 1 are the 2-entries and i*; an allowed set with >= 3 elements
  contains at most one of them, so positive-weight allowed sets have sum <= 1 ({two, 4, d} and {i*, 4, d} sum to 1).
  Values: (2,2,2,4): 3 + 2 + x/2; (2,2,1,4): 1 + 2 + 2 + x/2; (2,1,1,4): 2 + 1 + 2 + x/2; all >= 11/2 > 5 (x >= 1).

## 2. Structure lemmas (G)
For a family x let H_x be the graph on O of the pairs with x = 4 (so x' <= 2 on them, INV (b)).
- **B1 (degree <= 3).** Every v in O has H_x-degree <= 3. *Proof.* Degree 4 makes all four O-entries of the x'-row of v
  lie in {1, 2}: (R4). QED
- **B2 (degree-3 rule).** If v has H_x-degree 3 and e is its fourth O-neighbour, then x'_ve = 4 (so x_ve <= 2) and
  x'_(v i*) is even. *Proof.* Three x'-entries of v lie in {1, 2}; if x'_ve <= 2 as well, (R4); so x'_ve = 4, and then
  (R3) forbids an odd x'_(v i*). QED
- **B3 (no K4, no bowtie).** H_x contains no K4 and no two triangles sharing exactly one vertex. *Proof.* A K4 on
  {a,b,c,d} gives each of its vertices degree 3 (B1), so by B2 x' = 4 on all four pairs from the fifth vertex e to the
  K4, and e has H_(x')-degree 4, contradicting B1 for x'. A bowtie's common vertex has degree 4 (B1). QED

## 3. Conditional consequences (CONDITIONAL ON DG)
Call an x-4-pair **non-tight** if (x, x') = (4, 1).
- **B4 (free families have a diamond).** If no x-4-pair is non-tight, then Theorem DG for x forces H_x to contain a
  diamond (K4 minus one edge).
  *Proof.* By CI' (Part A, applicable at every vertex in G), every cherry a-v-b of H_x (a, b in O) has tau_x(vab) != 4 x_ab:
  so no cherry has x_ab = 1 (tau = 4 is forced there), every (2,4,4) triple has tau = 4 (depth 3), and every 4-triangle has
  tau in {4, 8, 12}. Hence the triples of depth >= 4 are exactly the 4-triangles with tau = 8 (depth 4), and no triple has
  depth 5. If all 4-subsets have depth <= 4, DG (a) gives 2a >= 3 (Part A (3c)), so H_x has two triangles, which share an
  edge by B3 (two triangles in a 5-set share a vertex): a diamond. Otherwise some 4-subset Q has depth >= 5; by DG-4 every
  e in Q has depth(Q minus e) + v2(m_e) >= 5 with depth <= 4, i.e. either Q minus e is a 4-triangle (tau = 8) and m_e >= 2, or
  m_e = 4. If Q contains no 4-triangle, every e has m_e = 4 and Q is a K4 (B3: impossible). If Q contains exactly one
  4-triangle R = Q minus e, each r in R has Q minus r not a 4-triangle, so m_r = 4, i.e. r is joined by 4 to e and to the other
  two vertices of R: Q is a K4 (impossible). So Q contains two 4-triangles: a diamond. QED
- **B5 (at most one free family).** If H_x contains a diamond on {a, b, c, d} (missing the pair ab), then H_(x') lies in
  {ab, ea, eb, ec, ed} (e the fifth O-vertex), which contains a single triangle, so H_(x') contains no diamond. Hence at
  least one family y has a non-tight y-4-pair, i.e. u(y) >= 1, and by accepted K62-E3 C2 for y':
  **n_4(y') >= 2 n_1(y') + 2 >= 2 u(y) + 2 >= 4.** Moreover, if H_x contains the diamond, B2 at c and d (H_x-degree 3)
  gives x'_ce = x'_de = 4 and x'_(c i*), x'_(d i*) even.

## 4. Exact remaining gap after Parts A-B (CONDITIONAL ON DG)
Inside G: patterns in which (i) one family x has a diamond in H_x with x'_ce = x'_de = 4 as in B5, the other family y
satisfies DG through deep triples or 4-subsets whose forced apexes (CI') use non-tight y-4-pairs, and C2 holds in both
families; or (ii) neither family has a diamond and both satisfy DG through non-tight pairs. Not yet treated: these
residual patterns; the sub-cases with a marker in O (including (alpha_(d i*), alpha*_(d i*)) = (1,3), where DG applies to
one family only and CI' needs x_(d i*) = 1); and e_d-dependent weight details (a depth-5 triple counts 1/16 when e_d = 4).
Nothing in this file excludes the residue. Full K6.2* (e_d >= 4) and full Sun(7) remain OPEN.
