# No 2-(88,4,1) design has a point-cyclic resolution

Revision r2 (2026-10-17; write-up only). r1, SHA-256 227c200c6c0adb2874d4e1e482e88ad4de5edbe43c4ce12f8e1625f70de36bfa,
is the version reviewed by the parent's cross-vendor hostile review (Claude Opus 5.5 max: VERDICT ACCEPT, no fatal or
major findings; `institute/runs/six-lane-2026-10-16/review/point-cyclic88-hostile-review.note.md`). r1 is preserved
byte-for-byte as `archive/PROOF.r1-reviewed-227c200c.md`. r2 applies only the review's minor items: m1 verbatim
definitions and their binding (Section 0); m2 pinned quotes (Appendix A) and a pinned receipt for the computational
statements of Section 6; m3 the complete substitution list for the Corollary; m4 a definition of "type T1" (before
Corollary 4). The Theorem statement, every lemma statement and every proof step are unchanged. Changelog and hashes:
lane `README.md`, Section 4.

Status: written proof by worker InfoCdf. No novelty or priority claim is made here (parent audit). Finite checks of
every arithmetic step: `code/check88.py` (receipt `evidence/check88-receipt.json`); semantic positive control on the
published v = 64 example: `code/control64.py` (receipt `controls/control64-receipt.json`).

## 0. Statement and definitions

Source: S. Topalova, S. Zhelezova, "Point-Cyclic Resolutions of 2-(64,4,1) Designs", Axioms 15 (2026) 762,
DOI 10.3390/axioms15100762 (`sources/axioms-15-00762.pdf`, SHA-256
d5170670a40e95195ac3e440121e447b998d3f775cc6bb52e1555e01b3b99608). Verbatim quotes from the PDF text layer: emphasis
markers removed, line-break whitespace normalized, and sub/superscripts or fractions that the text layer splits are
written inline in square brackets; "p." is the PDF page. Further quotes (labels Q-...) are in Appendix A.

* Q-D1 (p. 3): "Definition 1. Let V = [{x_i}, i = 1, ..., v] be a finite set of v points, and B = [{B_j}, j = 1, ...,
  b] a finite collection of k-element subsets of V, called blocks. The incidence structure D = (V, B) is a 2-(v,k,λ)
  design if any 2-element subset of V is contained in exactly λ blocks of B."
* Q-D2 (p. 3): "Definition 2. A parallel class is a partition of the point set by blocks. A resolution of a 2-(v,k,1)
  design is a partition of the collection of blocks into parallel classes. A design is resolvable if it has at least
  one resolution."
* Q-D3 (p. 4): "Definition 3. An automorphism of the design D = (V, B) is a permutation of the points of V preserving
  B."
* Q-ISO (p. 4, the sentence following Definition 3): "Two resolutions are isomorphic if there is an automorphism of
  the underlying design that maps each parallel class of the first resolution to a parallel class of the second
  one."
* Q-D4 (p. 4): "Definition 4. A 2-(v,k,λ) design is cyclic if it is invariant under a cyclic automorphism group of
  order v."
* Q-D5 (p. 4): "Definition 5. A resolution is point-cyclic if it has an automorphism permuting the points in one
  cycle. A 2-(v,k,λ) design is cyclically resolvable if it has at least one point-cyclic resolution."

Binding of "automorphism" in Def. 5 (review item m1). The source has no separately numbered definition of an
automorphism of a resolution (its Definition 4 defines cyclic designs). In Q-D5 the automorphism is one that the
resolution has, and the only maps between resolutions defined in the source are those of Q-ISO. This proof therefore
reads an automorphism of the resolution R as an automorphism of the underlying design (Q-D3) that maps each parallel
class of R to a parallel class of R, i.e. an isomorphism of R onto itself in the sense of Q-ISO. The source's own
usage presupposes the same notion: its Theorem 1 (Q-THM1, Appendix A) describes orbits of parallel classes under the
cyclic group G, and Q-CONV separates point-cyclic resolutions from the class-transitive notion of other papers.
Robustness: the image of a parallel class under a design automorphism is again a set of blocks partitioning V, so
"maps to a class" and "maps onto a class" coincide; and any stronger reading of "automorphism of R" (for example one
fixing every class) only adds hypotheses, so the nonexistence Theorem remains true under it. Not covered: cyclic
automorphisms of D that do not map the classes of R to classes of R, and the class-transitive notion.

Working definitions used below (restatements of Q-D1, Q-D2, Q-D3, Q-ISO and Q-D5 with lambda = 1):

* A 2-(v,k,1) design is a pair D = (V, B), |V| = v, B a collection of k-subsets ("blocks") of V such that every
  2-subset of V lies in exactly one block.
* A parallel class is a set of blocks partitioning V. A resolution R of D is a partition of B into parallel classes.
* An automorphism of D is a permutation of V mapping B onto B. An automorphism of the resolution R is an
  automorphism of D that maps every parallel class of R onto a parallel class of R (this is the notion used in the
  source's definition of isomorphic resolutions).
* R is point-cyclic if it has an automorphism that permutes V in one cycle (Def. 5).

**Theorem.** Let D = (V, B) be any 2-(88,4,1) design and R any resolution of D. There is no permutation of V that is a
single 88-cycle, maps B onto B, and maps every parallel class of R onto a parallel class of R. Equivalently, no
2-(88,4,1) design is cyclically resolvable in the sense of the source.

Basic counts (from the definition): b = 88*87/(4*3) = 638 blocks; every point lies in r = 87/3 = 29 blocks; every
parallel class has 88/4 = 22 blocks; R has 638/22 = 29 classes.

## 1. Setting

Suppose, for a contradiction, that D, R and an 88-cycle sigma as in the Theorem exist. Fix a point x0 and label the
point sigma^i(x0) by i in Z_88 (integers mod 88). Then sigma(x) = x + 1, and sigma^d(x) = x + d. For a subset X of
Z_88 write X + d = {x + d : x in X}; for a set P of blocks write P + d = {X + d : X in P}. By hypothesis:

(H1) B + d = B for every d (sigma^d maps blocks to blocks);
(H2) for every class P in R and every d, P + d is a class of R;
(H3) two distinct blocks share at most one point (lambda = 1: two shared points would be a pair in two blocks);
(H4) the blocks of one class are pairwise disjoint.

The group G = Z_88 acts on Z_88, on B and on R by translation. For a block X, Stab(X) = {d : X + d = X}; for a class
P, Stab(P) = {d : P + d = P}. Both are subgroups of Z_88. For every divisor h of 88, Z_88 has exactly one subgroup of
order h, namely H_h = {0, 88/h, 2*88/h, ...} (the multiples of 88/h). In particular
H_2 = {0,44}, H_4 = {0,22,44,66}, H_11 = {0,8,16,...,80}, H_22 = {0,4,8,...,84}.

## 2. Short blocks

**Lemma 1 (translation lemma).** Let X be a block, x != y points of X, and d in Z_88 with x + d and y + d in X. Then
d in Stab(X).

Proof. X + d is a block by (H1) and contains x + d and y + d, which are two distinct points of X. By (H3), X + d = X.

**Lemma 2 (block stabilizers).** Every block X has Stab(X) = {0} or Stab(X) = H_4. The blocks with Stab(X) = H_4 are
exactly the 22 cosets a + H_4 = {a, a+22, a+44, a+66} (a = 0, ..., 21); all of them are blocks.

Proof. Let K = Stab(X). X is a union of K-orbits on Z_88, and the K-orbits are the cosets of K, each of size |K|.
Hence |K| divides |X| = 4, so K is {0}, H_2 or H_4 (the subgroups of order 1, 2, 4).
If K = H_2, then X = {a, a+44, c, c+44} with c not in {a, a+44}. Apply Lemma 1 to x = a, y = a + 44, d = c - a:
x + d = c and y + d = c + 44 lie in X, so c - a in K = H_2 = {0, 44}, i.e. c in {a, a+44}: contradiction.
If K = H_4, X is a union of H_4-cosets of size 4, so X is one coset.
Conversely let a in Z_88. The pair {a, a+44} lies in some block X (Def. 1). Apply Lemma 1 to x = a, y = a + 44,
d = 44: x + d = a + 44 and y + d = a + 88 = a lie in X, so 44 in Stab(X); hence Stab(X) != {0}, so Stab(X) = H_4 and
X is the coset of H_4 containing a, namely a + H_4. So every coset of H_4 is a block.

Call the 22 blocks a + H_4 *short* and write S for the set of them; every other block has trivial stabilizer and is
called *full*. S is a single G-orbit (a + H_4 = H_4 + a) and S + d = S for all d. The differences y - x of points
x != y of a short block all lie in H_4 \ {0} = {22, 44, 66}.

(Finite control: `check88.py` E1 enumerates all C(88,4) = 2,331,890 four-subsets; stabilizer orders occur as
{1: 2,330,944; 2: 924; 4: 22}; the subsets compatible with (H1)+(H3) that have a nontrivial stabilizer, and those that
contain a pair {x, x+44}, are in both cases exactly the 22 cosets of H_4.)

## 3. Parallel classes and their stabilizers

Let P be a class, Stab(P) = H_h (h | 88), and m = m(P) = number of short blocks in P (0 <= m <= 22).

**Lemma 3.** (a) The G-orbit of P consists of 88/h distinct classes, so 88/h <= 29; hence h >= 4, i.e.
h in {4, 8, 11, 22, 44, 88}.
(b) h divides 22 - m.
(c) (88/h) * m <= 22.

Proof. (a) Orbit-stabilizer; R has 29 classes. 29*h >= 88 fails for h = 1, 2 (29, 58 < 88) and holds for h = 4 (116).
(b) By (H2), P + d = P for d in H_h, so H_h permutes the blocks of P. For a full block X in P the map d -> X + d is
injective on H_h (Stab(X) = {0}), so the H_h-orbit of X has exactly h blocks, all in P. These orbits partition the
22 - m full blocks of P; hence h | 22 - m.
(c) Translation maps short blocks to short blocks and full blocks to full blocks, so every class P + d has m short
blocks. The 88/h classes of the orbit are distinct classes of a partition of B, hence pairwise disjoint, and they
contain (88/h)*m distinct short blocks; there are only 22 short blocks.

**Definition (type T1; review item m4).** As in the source (Q-T1, Appendix A: "T1—the short block orbit is a parallel
class"), say that R has type T1 if the set S of short blocks is a class of R. Only this property is used below; the
source's types T2 and T3 are not used.

**Corollary 4 (no mixed class; R has type T1).** m(P) is 0 or 22 for every class P. Consequently exactly one class, P0,
equals S, and every other class consists of full blocks only.

Proof. Suppose 1 <= m <= 21. By (c), m <= 22h/88 = h/4, so h >= 4m. Check every h of (a):
* h = 4: m <= 1, so m = 1; (b) requires 4 | 21. False.
* h = 8: m <= 2; (b) requires 8 | 21 or 8 | 20. False.
* h = 11: m <= 2; (b) requires 11 | 21 or 11 | 20. False.
* h = 22: m <= 5; (b) requires 22 | 22 - m with 17 <= 22 - m <= 21. False.
* h = 44: m <= 11; (b) requires 44 | 22 - m with 11 <= 22 - m <= 21. False.
* h = 88: m <= 22; (b) requires 88 | 22 - m with 1 <= 22 - m <= 21. False.
So m in {0, 22}. Every short block lies in some class, and a class with m = 22 consists of 22 short blocks, i.e. it
is S. Classes are disjoint, so exactly one class equals S; every other class has m = 0.
(Finite control: `check88.py` E2 lists all (h, m) with h | 88, 0 <= m <= 22 satisfying (a)-(c): exactly
(11, 0), (22, 0), (88, 22).)
(Remark: (c) can be sharpened to equality when m >= 1, because the union of P' intersected with S over the orbit
of P is a nonempty translation-invariant subset of the single orbit S; then h = 4m, and h | 22 - m fails for
m = 1, 2, 11 as well. The inequality suffices.)

**Lemma 5 (stabilizers of the other classes).** If P != P0, then Stab(P) = H_11 or H_22. In both cases 8 in Stab(P).

Proof. P0 = S satisfies P0 + d = P0 for all d, so P + d != P0 for all d: the orbit of P lies among the 28 classes
other than P0, hence 88/h <= 28. 28*h >= 88 fails for h = 1, 2 (28, 56 < 88), so h >= 4. By Corollary 4, m(P) = 0,
so Lemma 3(b) gives h | 22. The divisors of 22 that are >= 4 are 11 and 22. 8 is a multiple of 88/11 = 8 and of
88/22 = 4, so 8 lies in H_11 and in H_22.

## 4. The forbidden difference

**Lemma 6.** Let P be a class, X in P, and d in Stab(P). If x and x + d both lie in X, then d in Stab(X). In
particular a full block of a class P never contains two points x, x + d with d in Stab(P) \ {0}.

Proof. X + d is a block of P + d = P and contains x + d; X also contains x + d. Blocks of P are disjoint (H4), so
X + d = X.

## 5. Proof of the Theorem

The pair {0, 8} lies in a block X (Def. 1). X is not short: 8 - 0 = 8 is not in {22, 44, 66}. So X is full; X lies
in some class P (R partitions B), and P != P0 because P0 = S consists of short blocks. By Lemma 5, 8 in Stab(P). By
Lemma 6 with x = 0, d = 8, the full block X cannot contain both 0 and 8. Contradiction. Hence no such D, R, sigma
exist. QED.

(The same argument shows that every pair {x, x + d} with d in H_11 \ {0} = {8, 16, ..., 80}, i.e. 440 pairs, would
be covered by no block.)

## 6. Scope, checks against known positives, and a general form

Only the Corollary below is a mathematical claim; the other items of this section are consistency checks that
neither the Theorem nor the Corollary uses. Statements attributed to the source are backed by the verbatim quotes of
Appendix A. The papers the source cites for them ([5] Genma-Mishima-Jimbo 1997, [6] Lam-Miao 1999, [26]
Lam-Miao-Mishima 2001) were not read here; only the source's statements about them are used, and only as checks.

* Nothing beyond Defs. 1-5 is used: in particular not the T2/T3 lemmas of Mishima-Jimbo, not the cyclicity of the
  underlying design as an extra hypothesis (it follows from sigma), and no classification data.
* General form (same proof, v = 4n = 4 (mod 12), H_4 = <n>, n blocks per class, r = (v-1)/3 classes): Lemmas 1-2 and
  6 hold verbatim; Lemma 3 gives (a) v/h <= r, (b) h | n - m, (c) (v/h) m <= n. If no (h, m) with 1 <= m <= n-1
  satisfies (a)-(c) then the resolution has type T1, the other classes have stabilizer orders h | n with
  v/h <= r - 1, and if the gcd g of all such h does not divide 4, any d in H_g \ H_4 gives an uncovered pair.
  `code/general_table.py` (SHA-256 727446a0b72c3269889f3b8d4962d767bf4062da1b46a7bc81d7083ca5ba75a9, unchanged since
  r1) evaluates this with exact integers for every v = 4 (mod 12) with 16 <= v <= 10000 (833 values). Receipt with
  command, host time, script and output hashes, exact range and the verbatim output lines used here:
  `evidence/general-table-receipt-v1.md`. Results (computational, for this range only):
  - Excluded: exactly the v = 4p with p prime, p = 7 (mod 12), and the v = 8p with p prime, p = 11 (mod 12)
    (receipt line "excluded set equals A u B ...: True"). v = 88 = 8*11 is the smallest member of the second
    family. Nothing is claimed beyond 10000.
  - The first family is what the necessary condition stated by the source (Q-GMJ, attributed to [5]: if a
    2-(v,k,1) design possesses point-cyclic resolutions and v/k is prime, then v/k = 1 (mod k(k-1))) excludes among
    the v = 4p = 4 (mod 12): such p satisfy p = 1 or 7 (mod 12), and the condition removes p = 7 (mod 12) (receipt
    line "GMJ controls ...": the reproduced list equals the control list).
  - Not excluded: v = 52 (the mixed pair (h, m) = (4, 1) satisfies (a)-(c)), v = 64 (type T1 is forced, but every
    admissible non-short stabilizer contains H_4 = <16>, whose nonzero elements are exactly the short-block
    differences, so no pair is forced to be uncovered), and every v = 4q with q a prime = 13 (mod 24). For these
    the source states existence: v = 52 (Q-52a, Q-52b: six 2-(52,4,1) designs with one point-cyclic resolution
    each, whose classes form two orbits of lengths 4 and 13, attributed to [26]); v = 64 (Q-64: 258 point-cyclic
    resolutions, the source's own computer-aided result); v = 4q (Q-LM, attributed to [6]: q a product of primes of
    the form 12s + 1 with s odd; only prime q is used here). The receipt line "PROBLEMS: none" records that no such
    value is excluded.
* Corollary (same proof). For every prime p = 11 (mod 12), no 2-(8p,4,1) design has a point-cyclic resolution.
  Substitutions in Sections 1-5 (review item m3): 88 -> 8p; 22 -> 2p (blocks per class, number of short blocks, and
  the stabilizer order 22); 44 -> 4p (H_2 = {0, 4p}; the diameter pairs {a, a + 4p} of Lemma 2); 66 -> 6p, so
  H_4 = {0, 2p, 4p, 6p} and the short-block differences are {2p, 4p, 6p}; 29 -> r = (8p-1)/3; 28 -> r - 1 (Lemma 5);
  11 -> p (H_11 -> H_p = <8>, H_22 -> H_2p = <4>); 21 -> 2p - 1 (range of m in Corollary 4). The forbidden
  difference stays 8: 8 lies in H_p and in H_2p, and 8 is not in H_4 because 0 < 8 < 2p. Lemma 3(a): r*h >= 8p iff
  h >= 24p/(8p-1), and 3 < 24p/(8p-1) < 4, so h in {4, 8, p, 2p, 4p, 8p}. Corollary 4 for 1 <= m <= 2p-1 (with
  m <= h/4 from (c)): h = 4 gives m = 1 and 4 | 2p-1 (odd: false); h = 8 gives m <= 2 and 8 | 2p-1 (false) or
  8 | 2(p-1) (false since p = 3 mod 4); h = p needs p | 2p-m, i.e. p | m, impossible for 1 <= m <= p/4; h = 2p needs
  2p | m, impossible for m <= p/2; h = 4p, 8p need 4p | 2p-m resp. 8p | 2p-m with 1 <= 2p-m <= 2p-1: false.
  Lemma 5: (r-1)*h >= 8p iff h >= 6p/(2p-1), which lies in (3, 4) for p >= 3, so h | 2p and h >= 4 give
  h in {p, 2p}; both subgroups contain 8. Section 5 then applies to the pair {0, 8}. (Written for completeness; the
  target of this lane is v = 88.)
* Semantic positive control (`code/control64.py`, PASS): the published point-cyclic resolution of a 2-(64,4,1)
  design (source PDF pp. 6-7) was transcribed, developed and verified: 336 blocks, every pair once; 21 classes,
  each a partition of Z_64, pairwise disjoint, covering all blocks, mapped to classes by x -> x + 1; class orbit
  lengths 1, 4, 16. On it the lemmas above hold (short blocks = the 16 cosets of <16>; type T1; non-short class
  stabilizer orders 4 and 16; Lemma 6), and the intersection of the non-short stabilizers is <16> = H_4, which is why
  the v = 88 contradiction has no analogue at v = 64. Three corrupted copies are rejected and a reordering accepted.
  The transcription (constants BASE_1, P1_1, P2_1, P3_1 in `code/control64.py`) was made by hand from PDF pp. 6-7
  and is not machine-compared with the PDF text layer.

## Appendix A. Further verbatim source quotes (conventions as in Section 0)

* Q-CONV (p. 2): "A design with at least one point-cyclic resolution is called cyclically resolvable [5–7]. In some
  papers, the term cyclically resolvable has been used for designs with resolutions that are invariant under an
  automorphism group that maps the parallel classes to one another [8–10]. This is a property that we do not
  consider. In the present paper, when we talk about cyclically resolvable designs, we mean designs with point-cyclic
  resolutions."
* Q-GMJ (p. 2): "An important necessary condition says that if a 2-(v,k,1) design possesses point-cyclic resolutions
  and v/k is a prime number, then [v/k] ≡ 1 (mod k(k − 1)) [5]."
* Q-LM (p. 2): "The main existence result for cyclically resolvable Steiner 2-designs with block size 4 is derived in
  [6]. It states that there exist cyclically resolvable 2-(v,4,1) designs for v = 4q, where q is a product of primes
  of the form 12s + 1, and s is odd. This result, however, does not concern v = 64."
* Q-52a (p. 2): "The smallest cyclically resolvable 2-(v,3,1) design has 21 points, and the smallest cyclically
  resolvable 2-(v,4,1) design has 52 points."
* Q-NC (p. 4): "Only cyclic designs can be cyclically resolvable. There are, however, many cyclic designs that are
  not cyclically resolvable."
* Q-T1 (p. 5): "T1—the short block orbit is a parallel class;"
* Q-THM1 (p. 6): "Theorem 1. The parallel classes of a point-cyclic resolution of a cyclic 2-(64,4,1) design are in
  three orbits under G with orbit lengths 1, 4, and 16."
* Q-EX (pp. 6-7): the base blocks and the parallel classes P1, P2, P3 of the example (transcribed into
  `code/control64.py`; not reproduced here).
* Q-64 (p. 1, Abstract): "We establish that there are 258 point-cyclic resolutions of 2-(64, 4, 1) designs."
* Q-52b (p. 10): "The second algorithm uses the fact that the parallel classes of a point-cyclic resolution of a
  design with these parameters are in two orbits of lengths 4 and 13 [26], while the first algorithm considers the
  general case. We obtain that there are six 2-(52, 4, 1) designs, each of which possesses one point-cyclic
  resolution, namely the same result as in [26]."
* Q-OPEN (p. 11): "That is why v = 88 is the smallest v for which the existence of cyclically resolvable 2-(v, 4, 1)
  designs has not yet been determined. The number of the cyclic 2-(88, 4, 1) designs is 149,494,720, and what we know
  in advance is that their possible point-cyclic resolutions are of type T1."
