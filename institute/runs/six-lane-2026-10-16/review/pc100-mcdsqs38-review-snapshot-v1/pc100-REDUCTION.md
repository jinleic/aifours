# Point-cyclic resolutions of 2-(100,4,1) designs: complete reduction to eight base blocks

Lane `information-science/evidence/six-lane-20261016/point-cyclic100` (worker InfoCyclic100). Written 2026-10-17
(host clock, PDT) BEFORE any search in this lane. Status: worker derivation, untrusted until parent verification and
review. No novelty or priority claim. The contract calls the 8-block form the "initial T2 ansatz" and warns that a
miss of it is not general nonexistence; Theorems A-C below claim more: the ansatz is equivalent to the full problem.
The parent should check that claim before it is used for anything other than search design.

## 0. Definitions

Source: Topalova-Zhelezova, Axioms 15 (2026) 762 (local copy `../point-cyclic88/sources/axioms-15-00762.pdf`,
SHA-256 d5170670a40e95195ac3e440121e447b998d3f775cc6bb52e1555e01b3b99608), Definitions 1-5, the isomorphism sentence after
Definition 3, and the type list on PDF p.5 ("T1-the short block orbit is a parallel class; T2-each block from the short
block orbit is in a different parallel class; T3-there are parallel classes with more than one block from the short
block orbit"). The binding of "automorphism of a resolution" is the one accepted for the 88 lane
(`../point-cyclic88/PROOF.md` Section 0): a permutation of the points that maps the block set onto itself and maps
every parallel class of R onto a parallel class of R. Any stronger reading only adds hypotheses to Theorems A and B;
Theorem C produces a resolution invariant under +1 in this sense (each class is mapped onto a class).

* A 2-(v,4,1) design (V, B): |V| = v, B a set of 4-subsets (blocks), every 2-subset of V in exactly one block.
* Parallel class: set of blocks partitioning V. Resolution R: partition of B into parallel classes.
* R is point-cyclic if some automorphism of R permutes V in a single v-cycle.

## 1. Setting

Let D = (V, B) be a 2-(100,4,1) design, R a resolution of D and sigma an automorphism of R that is a 100-cycle.
Counting: b = 100*99/12 = 825 blocks, r = 99/3 = 33 blocks through each point, 100/4 = 25 blocks per class,
825/25 = 33 classes. Fix x0 and label sigma^i(x0) by i in Z_100; then sigma(x) = x + 1. For X a subset of Z_100 and a
set P of blocks write X + d, P + d for translates. By hypothesis:

* (H1) B + d = B for all d; (H2) P + d is a class of R for every class P and every d;
* (H3) two distinct blocks share at most one point (lambda = 1); (H4) blocks of one class are pairwise disjoint.

For a block X, Stab(X) = {d : X + d = X}; for a class P, Stab(P) = {d : P + d = P}; both are subgroups of Z_100.
For h | 100 let H_h be the unique subgroup of order h, H_h = <100/h>. Used below:
H_2 = {0,50}, H = H_4 = {0,25,50,75}, H_5 = <20> = {0,20,40,60,80}, H_20 = <5>, K = H_25 = <4>.
Note 20 lies in H_5, H_20, H_25 and H_100 = Z_100, but not in H_4.

## 2. Short blocks

**Lemma 1 (translation).** If X is a block, x != y in X, and x + d, y + d in X, then d in Stab(X).
Proof: X + d is a block (H1) sharing the two points x + d, y + d with X, so X + d = X (H3).

**Lemma 2.** Every block X has Stab(X) = {0} or Stab(X) = H. The blocks with Stab(X) = H are exactly the 25 cosets
a + H, and all of them are blocks.
Proof: X is a union of Stab(X)-cosets, so |Stab(X)| divides 4: Stab(X) in {{0}, H_2, H}. If Stab(X) = H_2 then
X = {a, a+50, c, c+50} with c not in {a, a+50}; Lemma 1 with x = a, y = a+50, d = c - a gives c - a in H_2,
contradiction. If Stab(X) = H, X is one H-coset. Conversely, for a in Z_100 the pair {a, a+50} lies in a block X
(design property); Lemma 1 with x = a, y = a + 50, d = 50 gives 50 in Stab(X), so Stab(X) = H and X = a + H.

Blocks a + H are *short* (set S, 25 blocks, one translation orbit); all other blocks are *full*: trivial stabilizer,
orbits of size 100. So there are 800 full blocks in exactly 8 full orbits. Two points of a short block differ by an
element of H \ {0} = {25, 50, 75}. A full block never contains two points x, x' with x' - x in H \ {0}: the pair
{x, x'} lies in the short block x + H, and two distinct blocks cannot share two points (H3).

## 3. Classes and stabilizers

Let P be a class, Stab(P) = H_h, and m = m(P) the number of short blocks in P.

**Lemma 3.** (a) The orbit of P under translation consists of 100/h distinct classes; hence 100/h <= 33, so
h >= 4, i.e. h in {4, 5, 10, 20, 25, 50, 100}.
(b) h divides 25 - m.
(c) If m >= 1, then (100/h) * m = 25, and every short block lies in a class of the orbit of P.
Proof. (a) orbit-stabilizer. (b) H_h permutes the blocks of P (H2 with P + d = P); on a full block it acts freely
(Lemma 2), so the 25 - m full blocks of P split into H_h-orbits of size h. (c) The 100/h classes of the orbit are
distinct classes of the partition R, hence pairwise disjoint as block sets, and each has exactly m short blocks
(translation maps short blocks to short blocks bijectively). The set U of short blocks occurring in classes of the
orbit is nonempty and translation-invariant, and S is a single translation orbit, so U = S and |U| = (100/h) m = 25.

**Corollary 4.** If m(P) >= 1 then (h, m) is (4, 1), (20, 5) or (100, 25). Exactly one class orbit O_S contains
short blocks; every class outside O_S has m = 0.
Proof. By (c), m = h/4, so 4 | h; the divisors of 100 in the list of (a) that are divisible by 4 are 4, 20, 100,
giving m = 1, 5, 25; (b) holds in all three cases (4 | 24, 20 | 20, 100 | 0). If P' also has m(P') >= 1, a short
block X of P' lies in some class Q of the orbit of P (by (c)), and P' = Q because R is a partition of B.

Types (matching the source's list): T1 if O_S has (h, m) = (100, 25), i.e. S is a class; T2 if (4, 1), each short
block in a different class; T3 if (20, 5), classes with five short blocks.

**Lemma 5.** If m(P) = 0 then Stab(P) = H_5 or Stab(P) = K = H_25.
Proof. By (b), h | 25; by (a), h >= 4; so h in {5, 25}.

**Lemma 6.** If X in P, d in Stab(P) and x, x + d in X, then d in Stab(X). In particular a full block of P contains
no two points differing by an element of Stab(P) \ {0}.
Proof. X + d is a block of P + d = P containing x + d, as does X; blocks of P are disjoint (H4), so X + d = X.

## 4. Types T1 and T3 are impossible

**Theorem A.** R is of type T2.
Proof. Suppose R has type T1 or T3. Let P be any class containing a full block. If P is in O_S the type is T3
(in T1 the only class of O_S is S, which has no full block), so Stab(P) = H_20 = <5>, which contains 20. Otherwise
m(P) = 0 and Stab(P) is H_5 = <20> or H_25 = <4> (Lemma 5), both containing 20. So 20 in Stab(P) for every class P
that contains a full block. The pair {0, 20} lies in a block X. X is not short because 20 is not in {25, 50, 75}.
So X is full and lies in a class P with 20 in Stab(P). Lemma 6 with x = 0, d = 20 gives 20 in Stab(X) = {0}, a
contradiction.

## 5. Structure of type T2

**Theorem B.** Let R have type T2 and let P_0 be the class containing the short block H. Then:
1. Stab(P_0) = H and O_S = {P_0 + t : 0 <= t <= 24} consists of 25 distinct classes, each with exactly one short
   block.
2. P_0 = {H} u {X_i + h : 1 <= i <= 6, h in H} for six full blocks X_1, ..., X_6. Each X_i has four distinct
   residues mod 25, and the six residue sets X_i mod 25 are pairwise disjoint with union Z_25 \ {0}.  (S2)
3. The 8 classes outside O_S form two orbits {Q_j + t : 0 <= t <= 3} (j = 1, 2), where Q_j = {Y_j + k : k in K},
   K = <4>, and each Y_j is a full block containing exactly one point of each residue class mod 4.  (S3)
4. The 8 full block orbits are the orbits of X_1, ..., X_6, Y_1, Y_2, and the 96 ordered differences x' - x
   (x != x' in the same block, over these eight blocks) are exactly the elements of Z_100 \ H, each once.  (S1)

Proof. (1) Type T2 means (h, m) = (4, 1) for O_S, so Stab(P_0) = H_4 = H and the orbit has 100/4 = 25 classes;
P_0 + t = P_0 + t' iff t - t' in H, which fails for distinct t, t' in {0, ..., 24}.

(2) H acts freely on the 24 full blocks of P_0 (Lemma 2), giving six orbits {X_i + h : h in H}. By Section 2, X_i
has no two points differing by an element of H \ {0}, i.e. four distinct residues mod 25. For p in Z_100 with
p = x (mod 25) for some x in X_i we have p - x in H, so the point set of the four blocks X_i + h is exactly the set of
points whose residue lies in X_i mod 25. The blocks of P_0 partition Z_100, H is the set of points with residue 0, and
the point sets of the six groups X_i + H are unions of blocks of P_0; hence the six residue sets and {0} are pairwise
disjoint and cover Z_25.

(3) The 33 - 25 = 8 classes outside O_S have m = 0 (Corollary 4) and stabilizer H_5 or K (Lemma 5). A class with
stabilizer H_5 has an orbit of 100/5 = 20 classes, all with m = 0, i.e. all outside O_S: more than 8. So every class
Q outside O_S has Stab(Q) = K and an orbit of 4 classes; 8 = 4 + 4 gives exactly two orbits. K (order 25) acts freely
on the 25 full blocks of Q, so Q = {Y + k : k in K} for any Y in Q. If y != y' in Y with y = y' (mod 4), then
y' - y in K \ {0}, so Y and Y + (y' - y) are distinct blocks of Q (trivial stabilizer) sharing the point y',
contradicting (H4). So Y has four distinct residues mod 4, i.e. one point in each residue class mod 4. Take Y_j in a
class Q_j of the j-th orbit; the orbit {Q_j + t : 0 <= t <= 3} contains every translate Y_j + s (write s = k + t
with t = s mod 4 in {0,1,2,3}, k = s - t in K).

(4) The classes of O_S contain the 25 short blocks and the blocks X_i + h + t (h in H, 0 <= t <= 24), which are all
translates X_i + s (s = h + t uniquely); these 600 blocks are distinct because the 25 classes are pairwise disjoint
block sets of 24 full blocks each. The two other class orbits contain the 100 translates of Y_1 and of Y_2. Since
25 + 600 + 200 = 825 = b and R partitions B, B consists exactly of the translates of H, X_1..X_6, Y_1, Y_2, and the
eight full orbits are distinct. Fix d in Z_100 \ {0}. Every full block containing {0, d} is Z + s for a unique base
block Z among the eight and a unique s, and then z = -s and z' = d - s lie in Z with z' - z = d; conversely each
ordered pair (z, z') in a base block Z with z' - z = d gives the full block Z - z containing 0 and d, and distinct
triples (Z, z, z') give distinct blocks (Z - z determines the orbit, hence Z, and Z - z = Z - w forces z = w by
the trivial stabilizer). So the number N(d) of ordered pairs with difference d equals the number of full blocks
containing {0, d}. For d not in H this is 1 (the design property, as no short block contains {0, d}); for d in
H \ {0} it is 0 (Section 2). Hence (S1). The equal count 96 = 8 * 12 = |Z_100 \ H| is a consistency check.

## 6. Converse

**Theorem C.** Let X_1, ..., X_6, Y_1, Y_2 be 4-subsets of Z_100 satisfying (S1), (S2) and (S3) of Theorem B (with
H = {0,25,50,75}, K = <4>). Put P_0 = {H} u {X_i + h : i <= 6, h in H} and Q_j = {Y_j + k : k in K}. Then
B = {H + t} u {X_i + s} u {Y_j + s} (t, s in Z_100) is a 2-(100,4,1) design with 825 distinct blocks, and the 33 sets
P_0 + t (0 <= t <= 24), Q_j + t (j = 1, 2; 0 <= t <= 3) are parallel classes forming a resolution that x -> x + 1
maps onto itself class by class. So the resolution is point-cyclic.
Proof. By (S1) no base block X in {X_i, Y_j} has a nonzero stabilizer (a nonzero t with X + t = X would give the
difference t four times), so each has 100 distinct translates. For a pair {x, y}: if y - x in H \ {0} it lies in the
short block x + H and in no translate of a base block (their differences avoid H by (S1)); otherwise the ordered pairs
(z, z') with z' - z = y - x in base blocks correspond bijectively to translates containing {x, y} (as in the proof of
Theorem B(4)), and there is exactly one by (S1). Counting with multiplicity, the 25 + 800 listed blocks cover each of
the 4950 pairs exactly once; hence the listed blocks are pairwise distinct (a repeated block would cover its pairs
twice) and form a 2-(100,4,1) design. P_0 is a partition of Z_100 by the residue argument of Theorem B(2) and (S2)
(it has 1 + 24 = 25 blocks); Q_j is a partition by (S3) (for p in Z_100 the unique y in Y_j with y = p (mod 4)
gives p - y in K). Translates of partitions are partitions. The classes P_0 + t (0 <= t <= 24) contain each block
H + t and each X_i + s exactly once (s = h + t uniquely), the classes Q_j + t (0 <= t <= 3) contain each Y_j + s
exactly once; so the 33 classes partition B. Finally (P_0 + t) + 1 = P_0 + (t + 1) with P_0 + 25 = P_0 (25 in H
permutes H and each group {X_i + h}), and (Q_j + t) + 1 = Q_j + (t + 1) with Q_j + 4 = Q_j.

**Corollary D.** A point-cyclic resolution of a 2-(100,4,1) design exists if and only if eight 4-subsets of
Z_100 satisfying (S1)-(S3) exist. (Theorems A, B for "only if", Theorem C for "if".)

Consequences for this lane (not mathematical claims beyond Corollary D): a verified 8-block witness is a complete
existence proof once expanded and checked; a search miss proves nothing; a nonexistence claim would need a
certified exhaustive search of (S1)-(S3) under proved normalizations, or a proof.

## 7. Consistency checks against known cases (not used above)

The same chain with v = 4q, q = v/4:
* v = 52 (q = 13): the divisors h of 52 with 4 | h are 4 and 52, so m >= 1 forces (h, m) = (4, 1) or (52, 13):
  only T1 and T2 are possible. T1 is impossible because the m = 0 classes need h | 13 with 52/h <= 16, so h = 13,
  and <4> lies in every such stabilizer while 4 is not a short-block difference (short differences 13, 26, 39). T2:
  the remaining 17 - 13 = 4 classes form one orbit of length 4 with stabilizer <4>. This matches Lam-Miao-Mishima
  2001 (preprint, `sources/`), Theorem 2.3 (only type T2) and Section 3 (the class orbit without short blocks has
  length 4), and their Appendix A base blocks have exactly the form (S1)-(S3) with 3 + 1 blocks (checked by
  `code/control52.py`).
* v = 64 (q = 16): m >= 1 forces h = 4m with h | 16 - m; only (64, 16) survives, i.e. type T1, matching the source's
  Section 3 and Theorem 1. The v = 100 argument has no analogue there because every admissible m = 0 stabilizer at
  v = 64 contains <16> = H_4, whose differences are short-block differences (as in the 88 lane).
