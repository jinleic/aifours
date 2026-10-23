# Point-cyclic resolutions of 2-(v,4,1) designs with v = 4n: orbit structure and an exact base-block reduction

Lane `information-science/evidence/six-lane-20261016/point-cyclic-table200` (worker InfoCyclic100). Written
2026-10-17 (host clock, PDT) BEFORE any block search in this lane. This is a worker derivation and is untrusted until
the parent's review. It generalizes the v = 100 reduction (`../point-cyclic100/REDUCTION.md`, reviewed by the parent:
ACCEPT-WITH-FIXES, no mathematical error; revision `review/pc100-mcdsqs38-parent-inputs-r2/pc100-REDUCTION.md`) to every
v = 4 (mod 12), and it applies the presentation fixes of that review: the conditions are stated on their own, translates
are indexed, partitions are counted, and types are labelled by m. No novelty or priority claim is made. In particular,
the type trichotomy and the T1/T2 necessary conditions are classical (Genma-Mishima-Jimbo 1997, Mishima-Jimbo 1997 as
restated in Mishima-Jimbo 2000, Lam-Miao-Mishima 2001; see `README.md` Section 1.3 for exact quotes). The point of this
note is a self-contained, uniform statement that is exact in both directions, so that each order can be settled either
by a certificate or by an argument over a proved-complete list of cases.

## 0. Definitions

These are the same as in the reviewed v = 88 and v = 100 notes: Topalova-Zhelezova, Axioms 15 (2026) 762, Definitions
1-5 and the isomorphism sentence after Definition 3, local copy `../point-cyclic88/sources/axioms-15-00762.pdf`, SHA-256
d5170670a40e95195ac3e440121e447b998d3f775cc6bb52e1555e01b3b99608.

* A 2-(v,4,1) design (V, B) has |V| = v and a set B of 4-subsets (blocks) such that every 2-subset of V lies in exactly
  one block.
* A parallel class is a set of blocks that partitions V. A resolution R is a partition of B into parallel classes.
* An automorphism of R is a permutation of V that maps B onto B and maps every class of R onto a class of R. R is
  point-cyclic if some automorphism of R is a single v-cycle.

Theorem A' assumes only the class-permuting notion. A stronger notion would only add hypotheses to A', and the
construction of Theorem C' satisfies it as stated (+1 maps each class onto a class; it does not fix every class).

## 1. Setting

Let v = 4n with v = 4 (mod 12), so n = 1 (mod 3). Then:

* b = v(v-1)/12 = n(4n-1)/3 blocks;
* r = (v-1)/3 = (4n-1)/3 blocks through each point;
* n blocks in every class, and r classes in all.

Let D, R and a v-cycle sigma be as in the definition. Label the points by Z_v so that sigma(x) = x + 1. Then:

* (H1) B + d = B for every d;
* (H2) for every class P and every d, P + d is a class;
* (H3) two distinct blocks share at most one point;
* (H4) the blocks of one class are pairwise disjoint.

For a block X let Stab(X) = {d : X + d = X}, and for a class P let Stab(P) = {d : P + d = P}. For h | v, H_h = <v/h> is
the unique subgroup of order h. Put H = H_4 = <n> = {0, n, 2n, 3n}.

For a modulus mu | v, the residue of x in Z_v mod mu is well defined. Two points x, y have the same residue mod mu iff
y - x lies in <mu>, the subgroup of the multiples of mu, which has order v/mu.

## 2. Short and full blocks

**Lemma 1 (translation).** Let X be a block, x != y in X, and suppose x + d and y + d are also in X. Then d lies in
Stab(X).
Proof: X + d is a block (H1) that shares two points with X, so X + d = X (H3).

**Lemma 2.** Every block X has Stab(X) = {0} or Stab(X) = H. The blocks with Stab(X) = H are exactly the n cosets a + H,
and all of them are blocks.
Proof: X is a union of Stab(X)-cosets, so |Stab(X)| divides 4.
- Stab(X) = H_2 = {0, 2n} is impossible. Then X = {a, a+2n, c, c+2n} with c not in {a, a+2n}, and Lemma 1 with
  d = c - a forces c - a in H_2.
- If Stab(X) = H, then X is a single coset of H.
- Conversely, take any a. The pair {a, a+2n} lies in a block X, and Lemma 1 with d = 2n gives 2n in Stab(X). By the
  above, Stab(X) = H and X = a + H.

The n blocks a + H are *short* and S denotes their set; S is a single translation orbit. Every other block is *full*:
it has trivial stabilizer, and so a translation orbit of size v. A full block never contains two points that differ by
an element of H \ {0}, because that pair already lies in a short block (H3).

There are b - n = 4n(n-1)/3 = v(n-1)/3 full blocks, so f = (n-1)/3 full translation orbits.

## 3. Classes

For a class P let h = |Stab(P)|, so Stab(P) = H_h. Let m = m(P) be the number of short blocks in P, and let s = v/h be
the length of the translation orbit of P.

**Lemma 3.**
(a) h >= 4.
(b) h divides n - m.
(c) If m >= 1, then s m = n, and every short block lies in a class of the orbit of P.

Proof.
- (a) The orbit of P consists of s = v/h distinct classes, so v/h <= r = (v-1)/3, i.e. h >= 3v/(v-1) > 3.
- (b) H_h permutes the blocks of P and acts freely on its n - m full blocks (Lemma 2), in orbits of size h.
- (c) The s classes of the orbit are pairwise disjoint block sets, and each contains m short blocks. The set of short
  blocks occurring in the orbit is nonempty and translation-invariant. S is a single orbit, so that set is all of S,
  and s m = n.

**Lemma 4 (no difference from the class stabilizer).** Let X be in P and d in Stab(P). If x and x + d both lie in X,
then d is in Stab(X). In particular, a full block in P has four distinct residues modulo s.
Proof: X + d is a block of P + d = P that contains x + d, and so does X. Blocks of P are disjoint (H4), so X + d = X.
For the second sentence, Stab(P) = H_h = <s>.

**Lemma 5 (the orbit O_S).** Exactly one class orbit, O_S, contains short blocks. Let t be its length and let P_0 be the
class of O_S that contains the short block H. Then:
1. t | n and t = 1 (mod 4), and every class of O_S has m = n/t short blocks.
2. Stab(P_0) = <t>. The short blocks of P_0 are the n/t cosets of H contained in <t>.
3. P_0 = {a + H : a in <t>} u {X_i + c : 1 <= i <= (t-1)/4, c in <t>}, where X_1, ..., X_{(t-1)/4} are full blocks.
   Their residue sets modulo t are pairwise disjoint 4-sets whose union is Z_t \ {0}.
4. O_S = {P_0 + j : 0 <= j < t} consists of t distinct classes, and it contains each translate of each X_i exactly
   once.

Types: T1 if t = 1 (then m = n and P_0 = S); T2 if t = n (then m = 1); T3 if 1 < t < n (then 1 < m < n). These are the
source's types under any reading, since they are defined by m (review finding 4 on the v = 100 note).

Proof.
- Uniqueness of O_S: if P' has m(P') >= 1, one of its short blocks lies in a class Q of the orbit of P (Lemma 3c), and
  P' = Q because R partitions B.
- Item 1: from Lemma 3c, s m = n with s = t, so m = n/t, and h = v/t = 4m. Then 4 | h means t | n. Lemma 3b gives
  4m | n - m, i.e. 4m | m(t - 1), i.e. 4 | t - 1.
- Item 2: Stab(P_0) = H_h = <v/h> = <t>. H is contained in H_h because 4 | h. So H_h permutes the short blocks of P_0,
  with the stabilizer of a short block equal to H. The orbit of the short block H therefore has h/4 = m elements:
  these are all m short blocks of P_0, namely the cosets of H inside <t>.
- Item 3: H_h acts freely on the n - m full blocks of P_0, giving (n - m)/h = (t - 1)/4 orbits; let X_i represent
  them. X_i has four distinct residues mod t (Lemma 4). Its orbit X_i + <t> is exactly the set of points whose residue
  mod t lies in X_i mod t. The short blocks cover exactly the residue 0 mod t. P_0 is a partition, so the residue sets
  mod t of the X_i are pairwise disjoint with union Z_t \ {0}.
- Item 4: P_0 + j = P_0 iff j is in <t>, so the t classes P_0 + j (0 <= j < t) are distinct. The translate X_i + d lies
  in P_0 + j iff d - j is in <t>, i.e. for the unique j = d mod t. Distinct (i, c) give distinct blocks of P_0, since
  these blocks either cover different residues or differ by a nonzero element of the freely acting <t>.

**Lemma 6 (orbits without short blocks).** Let P be a class with m(P) = 0, and let s be its orbit length. Then:
1. s = 4k for a positive divisor k of n with 4k <= n.
2. P = {Y_l + c : 1 <= l <= k, c in <s>} for full blocks Y_1, ..., Y_k whose residue sets mod s are pairwise disjoint
   4-sets with union Z_s.
3. The orbit {P + j : 0 <= j < s} consists of s distinct classes, and it contains each translate of each Y_l exactly
   once.

Proof.
- Item 1: by Lemma 3b, h | n, and by 3a, h >= 4. Put k = n/h. Then s = v/h = 4k and 4k <= n.
- Item 2: <s> = Stab(P) acts freely on P, giving n/h = k orbits; let Y_l represent them. Y_l has four distinct residues
  mod s (Lemma 4), and Y_l + <s> is exactly the set of points with residue mod s in Y_l mod s. P is a partition of Z_v,
  so these residue sets partition Z_s.
- Item 3: as in Lemma 5.4.

## 4. The structure theorem

Fix t, K and base blocks as follows:
- t >= 1 with t | n and t = 1 (mod 4);
- K, a finite multiset of positive divisors k of n;
- base blocks: 4-subsets X_1, ..., X_{(t-1)/4} of Z_v (none if t = 1) and, for every entry k_j of K, 4-subsets
  Y_{j,1}, ..., Y_{j,k_j} of Z_v.

Consider the conditions:
* **(R1)** The residue sets mod t of X_1, ..., X_{(t-1)/4} are pairwise disjoint 4-sets with union Z_t \ {0}.
* **(R2)** For every j, the residue sets mod 4k_j of Y_{j,1}, ..., Y_{j,k_j} are pairwise disjoint 4-sets with union
  Z_{4k_j}.
* **(D)** The ordered differences z' - z (z != z' in one base block), over all base blocks, are exactly the elements of
  Z_v \ H, each once.

For these data define
* P_0 = {a + H : a in <t>} u {X_i + c : i, c in <t>};
* Q_j = {Y_{j,l} + c : l <= k_j, c in <4k_j>};
* the block family B(t, K, X, Y) = {a + H : a in Z_v} u {X_i + d} u {Y_{j,l} + d} (d in Z_v);
* the class family R(t, K, X, Y) = {P_0 + i : 0 <= i < t} u {Q_j + i : 0 <= i < 4k_j}.

**Theorem A' (necessity).** Every point-cyclic resolution R of a 2-(v,4,1) design, with the points labelled so that
sigma = +1, has the form B = B(t, K, X, Y) and R = R(t, K, X, Y), for some t, K and base blocks satisfying (R1), (R2),
(D), and in addition:
- **(E)** t + 4 * sum(K) = r, equivalently (t-1)/4 + sum(K) = (n-1)/3;
- 4k <= n for every k in K.

Proof.
- Lemma 5 gives t, P_0 and the X_i with (R1).
- Every other class orbit has m = 0. Lemma 6 gives its k, the blocks Y_{j,l} and (R2), and the orbit is
  {Q_j + i : 0 <= i < 4k_j}.
- Counting classes gives (E).
- Each class orbit contains each translate of its own base blocks exactly once (Lemmas 5.4, 6.3), and distinct orbits
  are disjoint block sets. So the full blocks are exactly the indexed translates (Z, d), with Z a base block and
  d in Z_v, without repetition.
- (D): fix delta in Z_v \ {0}. The map (Z, d) -> (Z, -d, delta - d) is a bijection from the indexed translates
  containing {0, delta} onto the triples (Z, z, z') with z, z' in Z and z' - z = delta.
  - If delta is not in H, no short block contains {0, delta}, and exactly one block does (the design property). So
    exactly one such triple exists.
  - If delta is in H \ {0}, the short block H already contains {0, delta}, so no full block does, and no such triple
    exists.

**Theorem C' (sufficiency).** Let t, K and the base blocks satisfy (R1), (R2) and (D); the inequality 4k <= n is not
needed. Then B(t, K, X, Y) consists of b distinct blocks and is a 2-(v,4,1) design. R(t, K, X, Y) is a resolution of it
into r classes, and x -> x + 1 maps B onto B and each class onto a class (P_0 + i -> P_0 + i + 1 with P_0 + t = P_0, and
Q_j + i -> Q_j + i + 1 with Q_j + 4k_j = Q_j). So the resolution is point-cyclic.

Proof.
- Design.
  - Index the full translates by (Z, d), with Z a base block and d in Z_v. By (D) and the cardinalities,
    (t-1)/4 + sum(K) = (n-1)/3.
  - Take a pair {x, y} with delta = y - x.
    - If delta is in H \ {0}, the pair lies in the short block x + H, and in no indexed translate, because (D)
      excludes differences in H.
    - Otherwise, (Z, d) -> (Z, x - d, y - d) is a bijection from {(Z, d) : x, y in Z + d} onto the ordered pairs
      (z, z') in Z with z' - z = delta. By (D) there is exactly one.
  - So each of the v(v-1)/2 pairs is covered exactly once by the n + v(n-1)/3 = b indexed blocks. A repeated block
    would cover its pairs twice, so the blocks are pairwise distinct and form a 2-(v,4,1) design.
- P_0 is a partition.
  - Covering: a point p with p = 0 (mod t) lies in the short block p + H, whose coset lies in <t>. If p is not 0 mod t,
    then by (R1) there is a unique i and a unique x in X_i with x = p (mod t), and p lies in X_i + (p - x) with
    p - x in <t>.
  - The indexed members of P_0 are n/t short blocks and ((t-1)/4)(v/t) = (t-1)n/t translates, n blocks in all. They
    hold 4n = v points with multiplicity and cover all v points, so they are pairwise disjoint.
  - The same argument with (R2) shows Q_j is a partition, and translates of partitions are partitions.
- The classes partition the blocks.
  - The short block a + H lies in P_0 + i exactly when a = i (mod t).
  - X_i + d lies in P_0 + (d mod t).
  - Y_{j,l} + d lies in Q_j + (d mod 4k_j).
  - Indexed blocks are pairwise distinct, so each block lies in exactly one listed class. The listed classes are pairwise
    distinct: they are different nonempty sets of distinct blocks.
- The shift. P_0 + t = P_0 and Q_j + 4k_j = Q_j, because t is in <t> and 4k_j is in <4k_j>. The class count is
  b/n = r, which recovers (E).

**Corollary D' (equivalence).** A 2-(v,4,1) design with a point-cyclic resolution exists iff there are t, K and base
blocks satisfying (R1), (R2), (D), (E), with t | n, t = 1 (mod 4), and every k in K a divisor of n with 4k <= n.
For a fixed v this is a finite list of types (t, K), and every point-cyclic resolution realizes exactly one of them,
namely its orbit structure. A nonexistence claim for v therefore needs a complete argument for EVERY admissible type.

**Corollary E (lcm obstruction).** Let L = {4k : k in K}, together with t if t > 1. If a point-cyclic resolution has
type (t, K), then n divides lcm(L).

Proof. Let g = lcm(L). Every class that contains a full block has stabilizer <s> for some s in L. If n does not divide
g, then g is not in H, so d = g is a nonzero element of Z_v (g = v would make n | g). It lies in the stabilizer of every
class that contains a full block. The pair {0, d} lies in a full block X, because d is not in H. X lies in a class P
with d in Stab(P), and Lemma 4 forces d in Stab(X) = {0}, a contradiction. Equivalently, in terms of (D): every base
block of an orbit of length s has no difference that is a multiple of s, so d is covered by no base block.

**Consistency checks (not used in the proofs).** `code/type_table.py` (receipt `evidence/type-table-200.txt`) lists, for
v = 4 (mod 12) up to 200, every (t, K) allowed by Lemmas 5-6, (E) and Corollary E. The checks:
- v = 28, 76, 124, 172 have no admissible type. This agrees with the Genma-Mishima-Jimbo prime condition.
- v = 88 and 184 have none. This agrees with the 8p theorem of `../point-cyclic88/PROOF.md`.
- v = 52 admits only T2 with K = {1}, class orbit lengths 13 and 4, as in Lam-Miao-Mishima 2001.
- v = 64 admits only T1 with K = {4, 1}, class orbit lengths 1, 16 and 4, which is Topalova-Zhelezova's Theorem 1.
- v = 100 admits only T2 with K = {1, 1}, the accepted v = 100 reduction.
- v = 16 and 40 have admissible types but no point-cyclic resolution. 16 has no cyclic 2-(16,4,1) design at all, and
  for 40 the source states that 52 is the smallest order. So the type list is necessary, not sufficient, and these two
  orders are negative controls.

## 5. The orders 100 < v <= 200 (summary; details and quotes in `README.md`)

Corollary E leaves no admissible type for 124, 172 and 184. The remaining orders:

| v | n | admissible types (t, K) |
|---|---|---|
| 112 | 28 | T1: K = {7, 2} or {7, 1, 1} |
| 136 | 34 | T3 with t = 17: K = {2,2,2,1}, {2,2,1,1,1}, {2,1,1,1,1,1} or {1 x 7} |
| 148 | 37 | T2: K = {1,1,1} (the v = 100 seed format with 9 X blocks and 3 Y blocks) |
| 160 | 40 | 12 T1 types and 27 T3 types with t = 5 (see `evidence/type-table-200.txt`) |
| 196 | 49 | T2: K = {1,1,1,1} (12 X blocks and 4 Y blocks) |

For 196 the X blocks satisfy (R1) with t = 49, so they have distinct residues modulo 49, and the 4 Y blocks are
transversals mod 4. This is exactly the T2 seed format of the v = 100 lane with q = 49.
