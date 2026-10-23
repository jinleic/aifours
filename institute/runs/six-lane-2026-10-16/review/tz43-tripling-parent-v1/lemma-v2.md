# Zero-sum tripling lemma and SAT-free frames for FDGDD(3,4,5{18}) — v2

Parent desk Tz43TriplingAudit, 2026-10-18 PT. This note is a written proof with no novelty or priority claim. Its
scope is the §4(3) frame step that has already been closed. It does not open a new problem slot. The only external
import is Hall's theorem, in the form of König's edge-colouring theorem for regular bipartite graphs, stated and
proved in §1 Step 3. The proof uses no finite census, solver output or symmetry assumption.

**v2 versus v1.** `lemma-v1.md` is preserved unchanged. v2 applies the three MINOR proof findings of the
`tz43-tripling-claude-v1` review (see `dispositions-v1.md`):

* E^s is now explicitly an indexed family;
* the containment step is made explicit in (iii);
* |D| = 72 and |A0| = 540 are derived rather than asserted.

No mathematical statement changed. §4 also cites the v2 generator and runner.

## 0. Definitions

Quoted from Tan–Zhou arXiv:2503.11934v1. Pinned text `mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt`,
SHA-256 `df52a8f11a46974eef129fa115bb3305831f7c8edc3e2102e4fd22c64c3c8164`; LF line numbers.

* **D1 GDD(t,K,v)** (LF 48–59). A triple (X, G, B), where G is a partition of X into groups:
  "(1) B is a family of subsets of X (called blocks), each having cardinality in K;
  (2) each block of B intersects any given group in at most one point;
  (3) each t-subset of X from t distinct groups is contained in exactly one block."
* **D2 PPC and PC** (LF 69–70). "A partial parallel class (PPC) of Y is a collection of pairwise disjoint blocks
  contained in Y. A parallel class (PC) of Y is a PPC that partitions Y."
* **D3 Kirkman frame** (LF 237–239). KF(m^v) "is a GDD(2,3,mv) of type m^v (X,G,B) such that the block set B can
  be partitioned into subsets P_r, r ∈ R, each P_r being a PC of X \ G for some group G ∈ G."
* **D4 derived design** (LF 241–242). For a GDD(3,4,mv) (X,G,A) of type m^v and x ∈ X, let
  A_x = {A \ {x} : x ∈ A ∈ A}. The derived design is (X \ G, G \ {G}, A_x), where G is the group containing x.
* **D5 FDGDD(3,4,v{m})** (LF 246–247). "a GDD(3,4,mv) of type m^v whose derived design at every point is a
  KF(m^(v−1))".
* **H(5,6,4,3).** Used here only as a name for a GDD(3,4,30) of type 6^5.

**Hypergraph terms.**

* A *3-partite 3-graph* H = (V, E) with parts A, B, C has V = A ⊔ B ⊔ C, and E is a finite family of triples.
  Each triple e ∈ E meets each part in exactly one vertex, written e = (a_e, b_e, c_e).
* Edges are indexed, so repeated triples would be distinct members. No simplicity or linearity is assumed.
* H is *r-regular* if every vertex lies in exactly r members of E.
* A *perfect matching* is a subfamily M ⊆ E (a subset of the index set) such that every vertex lies in exactly one
  member of M. For H^s, a subfamily is a subset of the index set E × Z3² defined next.
* For s ∈ Z3, the **zero-sum blow-up** H^s has vertex set V × Z3 and the edge family
  E^s = ( L(e; x, y, s − x − y) )_{(e, x, y) ∈ E × Z3²}, a family indexed by E × Z3²,
  where L(e; x, y, z) = {(a_e, x), (b_e, y), (c_e, z)}. For a lift indexed by (e, x, y), write z = s − x − y.
* Each lift contains exactly one vertex over each of a_e, b_e and c_e. Each e has exactly 9 lifts: x and y are free
  and z = s − x − y. Hence |E^s| = 9|E| as an indexed family. If H has no repeated triples, distinct indices give
  distinct vertex sets: the projection of a lift is e, and the copy coordinates are read off. Then E^s is also a
  set of 9|E| triples.

## 1. Lemma 1 (zero-sum tripling)

**Lemma 1.** Let H be a 3-regular 3-partite 3-graph with parts A, B, C, and let s ∈ Z3. Then E^s is partitioned into
9 perfect matchings of H^s. More precisely, the label classes C_P, P ∈ Z3², defined in Step 4 below, are pairwise
disjoint perfect matchings of H^s whose union is E^s.

**Step 1 (sizes).**

* Every edge has exactly one vertex in A, so Σ_{a∈A} deg(a) = |E|. By 3-regularity, 3|A| = |E|.
* The same argument for B and C gives |A| = |B| = |C| = |E|/3 =: n.
* Hence |V| = 3n = |E|.

**Step 2 (incidence graph).**

* Let I be the bipartite graph with left nodes V and right nodes E. It has one edge (v, e) for each incidence
  v ∈ e. I is simple: the three vertices of e lie in different parts, so they are distinct.
* Every left node v has degree deg_H(v) = 3.
* Every right node e has degree |e| = 3.
* So I is 3-regular on both sides.

**Step 3 (the only import: Hall's theorem).** Hall: a bipartite graph with sides L and R has a matching saturating L
iff |N(S)| ≥ |S| for every S ⊆ L.

* Let the bipartite graph be k-regular with k ≥ 1, and let S ⊆ L.
* The k|S| edges leaving S all end in N(S). The set N(S) receives at most k|N(S)| edges in total. Hence
  |N(S)| ≥ |S|, and a matching saturating L exists.
* Since k|L| = (number of edges) = k|R|, we have |L| = |R|, so this matching is perfect.
* Deleting it leaves a (k−1)-regular bipartite graph.
* Induction on k therefore splits the edge set of I into three perfect matchings M_0, M_1, M_2. This is König's
  edge-colouring theorem for I.

Define u(v, e) = i iff (v, e) ∈ M_i. Then:

* **(U1)** For each v ∈ V, the map e ↦ u(v, e) is a bijection from the three edges at v onto Z3. Each M_i is
  perfect, so it contains exactly one incidence at v.
* **(U2)** For each e ∈ E, the map v ↦ u(v, e) is a bijection from the three vertices of e onto Z3. Each M_i
  contains exactly one incidence at the right node e.
* **(U3)** Consequently u(a_e, e) + u(b_e, e) + u(c_e, e) = 0 + 1 + 2 ≡ 0 (mod 3) for every e.

**Step 4 (labels).**

* For L = L(e; x, y, z) ∈ E^s, put λ(L) = (x + u(a_e, e), y + u(b_e, e)) ∈ Z3².
* Let C_P = {L ∈ E^s : λ(L) = P}.
* λ is a function on the (indexed) family E^s. So every lift has exactly one label, the nine C_P are pairwise
  disjoint, and their union is E^s.

**Step 5 (each C_P is a perfect matching).** Fix P = (p1, p2). Every vertex of H^s lies in exactly one member of
C_P.

* **(i) Vertex (a, x), a ∈ A.** A lift contains (a, x) iff it is a lift of an edge e with a_e = a and has first copy
  coordinate x. It lies in C_P iff, in addition:
  * u(a, e) = p1 − x;
  * its second coordinate is y = p2 − u(b_e, e); and
  * z = s − x − y.

  By (U1) at a, exactly one edge e at a has u(a, e) = p1 − x. The coordinates y and z are then forced. The resulting
  triple satisfies x + y + z = s, so it lies in E^s, and its label is (p1, p2).
* **(ii) Vertex (b, y), b ∈ B.** This is symmetric.
  * By (U1) at b, exactly one e at b has u(b, e) = p2 − y.
  * Then x = p1 − u(a_e, e) and z = s − x − y are forced.
* **(iii) Vertex (c, z), c ∈ C (third part).**
  * A lift contains (c, z) iff it is a lift of an edge e with c_e = c and third copy coordinate z. This holds
    because the parts are disjoint and a lift has exactly one point over each of a_e, b_e and c_e.
  * Let e be an edge with c_e = c. A lift of e that contains (c, z) and has label P must have
    x = p1 − u(a_e, e) and y = p2 − u(b_e, e). So each such edge gives at most one candidate index (e, x, y). That
    candidate is a member of E^s with third coordinate z iff x + y + z = s, that is, iff
    p1 + p2 − (u(a_e, e) + u(b_e, e)) + z = s.
  * By (U3), u(a_e, e) + u(b_e, e) = −u(c, e). So the condition is equivalent to **u(c, e) = s − z − p1 − p2**.
  * By (U1) at c, exactly one of the three edges at c satisfies it. For that edge, the triple with the forced x and
    y lies in E^s and has label P (existence). No other edge contributes a member of C_P containing (c, z)
    (uniqueness): edges with c_e ≠ c are excluded by the first bullet, and the other edges at c by (U1).

  So C_P covers every vertex exactly once. ∎

**Where each hypothesis is used.**

* (U1) is used at A-vertices in (i), at B-vertices in (ii) and at C-vertices in (iii).
* The zero-sum identity (U3) is used **only** in (iii).
* What (iii) really needs is that, for each c ∈ C, the map e ↦ −(u(a_e, e) + u(b_e, e)) is a bijection on the edges
  at c. (U3) together with (U1) at c supplies this.
* Suppose u were a bijection at every vertex but failed (U2) on some edges. Then (i) and (ii) still hold, but (iii)
  can fail. Mutation (b) in §5 realises exactly this case.

**Counts.**

* |C_P| = |V × Z3|/3 = 3n.
* The total 9 · 3n = 27n = 9|E| = |E^s|.
* Neither linearity nor any condition on s is used. The colouring u depends only on H, so one u serves all three
  values of s.

## 2. Lemma 2 (missing-group families are (g/2)-regular)

**Lemma 2.** Let (Y, {G_1, …, G_4}, D) be a GDD(2,3,4g) of type g^4. Every triple of D meets exactly three groups,
so it misses exactly one group. Let F_i = {T ∈ D : T ∩ G_i = ∅}. Then:

* F_i is a 3-partite 3-graph whose parts are the three groups G_j, j ≠ i;
* every vertex of ∪_{j≠i} G_j has degree exactly g/2 in F_i; and
* in particular g is even.

**Proof.**

* By D1(2), a triple has its three points in three distinct groups. So it misses exactly one of the four groups.
  Every triple of F_i therefore meets each G_j, j ≠ i, in exactly one point.
* Fix y ∈ G_a, and for each i ≠ a let n_i = n_i(y) be the number of triples through y that miss G_i.
  * Every triple through y misses exactly one group.
  * That group is not G_a, because y ∈ G_a.
* Fix b ≠ a.
  * A triple through y contains a point of G_b iff it misses neither G_a nor G_b. That holds iff it misses one of the
    other two groups.
  * Such a triple contains exactly one point of G_b.
  * By D1(3), every pair {y, w} with w ∈ G_b lies in exactly one triple.
  * Counting the pairs {y, w}, w ∈ G_b, therefore gives g = Σ_{i ∉ {a, b}} n_i.
* Name the three groups other than G_a as G_b, G_c, G_d. Then n_c + n_d = g, n_b + n_d = g and n_b + n_c = g.
  Hence n_b = n_c = n_d = g/2.
* The degree of y in F_i (i ≠ a) is n_i(y) = g/2. ∎

**Case g = 6.** Each F_i is 3-regular and 3-partite, with parts of size 6 and 6 · 3 = 18 edges. Each point y lies
in n_b + n_c + n_d = 3g/2 = 9 triples, so |D| = 24 · 9/3 = 72 = 4 · 18. Pair uniqueness also makes D linear, but
nothing here uses linearity.

## 3. Theorem 3 (every zero-sum-tripled H(5,6,4,3) is an FDGDD(3,4,5{18}) with explicit frames)

**Setup.**

* Let (X0, {G0_1, …, G0_5}, A0) be a GDD(3,4,30) of type 6^5.
* Put X = X0 × Z3 and G_i = G0_i × Z3, so |G_i| = 18.
* Let A be the family of all {(p_0, β_0), …, (p_3, β_3)} with {p_0, …, p_3} ∈ A0 and β_0 + β_1 + β_2 + β_3 = 0 in Z3.

**(a) (X, {G_i}, A) is a GDD(3,4,90) of type 18^5.**

* A block projects onto a master block, so it has 4 points in 4 distinct groups.
* Take a 3-subset {(q_1, γ_1), (q_2, γ_2), (q_3, γ_3)} from three distinct groups.
  * {q_1, q_2, q_3} meets three distinct master groups. By D1(3) it lies in exactly one master block
    {q_1, q_2, q_3, q_4}.
  * A block of A containing the 3-subset projects onto a master block containing {q_1, q_2, q_3}, hence onto this
    one.
  * Its fourth point is then (q_4, γ_4) with γ_4 = −(γ_1 + γ_2 + γ_3), which is forced. That block lies in A.
  * So the 3-subset lies in exactly one block.
* Distinct master blocks have distinct projections, and each gives 27 distinct blocks.
  * By D1(3), each of the C(5,3) · 6³ = 2160 transverse triples of the master lies in exactly one master block.
  * Each block contains 4 such triples, so |A0| = 2160/4 = 540.
  * Hence |A| = 27 · 540 = 14580.
* This is inflation by the zero-sum TD(3,4,3), {β ∈ Z3⁴ : Σβ = 0}. Any three coordinates of that design determine the
  fourth.

**(b) Derived design.**

* Let x = (p, β) with p ∈ G0_a, and put s = −β.
* A block contains x iff it is {(p, β), (q_1, γ_1), (q_2, γ_2), (q_3, γ_3)} with {p, q_1, q_2, q_3} ∈ A0 and
  β + γ_1 + γ_2 + γ_3 = 0. Hence

  A_x = { {(q_1, γ_1), (q_2, γ_2), (q_3, γ_3)} : {q_1, q_2, q_3} ∈ D_p, γ_1 + γ_2 + γ_3 = s },

  where D_p = {B \ {p} : p ∈ B ∈ A0} is the master derived design.
* D_p is a GDD(2,3,24) of type 6^4 on X0 \ G0_a.
  * Its triples avoid G0_a and meet each group at most once.
  * For a cross pair {q, q′}, the transverse triple {p, q, q′} lies in exactly one master block, by D1(3).
* The same one-line argument applied to (a) shows that A_x is a GDD(2,3,72) of type 18^4 on X \ G_a.
* Distinct pairs (T, γ) give distinct triples, because T is the projection. So |A_x| = 72 · 9 = 648.

**(c) One missed group at a time.**

* For i ≠ a, let F_i(p) be the missing-group family of D_p. By Lemma 2 with g = 6 it is 3-regular and 3-partite.
  Its parts are G0_j for the three j ∉ {a, i}, taken in increasing index order as (A, B, C).
* A triple of A_x misses G_i iff its projection misses G0_i. So the triples of A_x that miss G_i are exactly the
  zero-sum lifts of F_i(p) with constant s.
* By Lemma 1 these 162 triples split into 9 classes. Each class is a perfect matching of
  ∪_{j∉{a,i}} G0_j × Z3 = (X \ G_a) \ G_i, that is, a PC of (X \ G_a) \ G_i in the sense of D2.

**(d) KF and FDGDD.**

* Every triple of A_x misses exactly one G_i with i ≠ a.
* Hence the 4 × 9 = 36 classes from (c) partition A_x. Each class is a PC of (X \ G_a) \ G_i for a group G_i of the
  derived design.
* With (b), this is exactly D3 for the derived design at x: a KF(18⁴).
* Since x was arbitrary, (X, {G_i}, A) satisfies D5: it is an FDGDD(3,4,5{18}). ∎

**What is and is not claimed.**

* The 36 classes at x partition the **derived triples** A_x into holey parallel classes. Nothing is said about
  resolving the 4-blocks A (an RH), and nothing about resolvable derived designs (an RDGDD).
* A KF class is a PC of (X \ G_x) \ G_i, not a PC of X \ G_x. So no RDGDD(3,4,5{18}) is claimed.
* The master is not required to be frame-derived, and the frames are not lifts of master frames.
  * The pinned master is in fact not frame-derived. This is a worker diagnosis and is not used here.
  * Lemma 1 builds new 9-class decompositions of the lifted size-18 families. One colouring u of F_i(p) serves all
    three copies (p, β); only the constant s = −β changes.
* Only g = 6 is covered, which gives group size 18 with r = g/2 = 3.
  * No statement is made for g = 4, g = 8 or general g.
  * No statement is made for other numbers of groups.
  * The odd-r conjecture and the even-r parity remarks in the scout note are not reviewed here.
* Existence of H(5,6,4,3) is classical, according to the scout's quotation of Zhang–Ge 2013. It is not re-proved or
  re-read here.
  * Theorem 3 is applied below only to the explicitly pinned master. That master was found by an earlier
    Kramer–Mesner SAT model and checked directly.
  * Theorem 3 makes the **frame** step SAT-free. The master's own provenance is unchanged.

## 4. Finite instance (implementation outline; results in `verdict-v1.md` and `receipt-v1.json`)

The generator is `code/build_tripled_fdgdd.py` (v1, which wrote the files). `code/build_tripled_fdgdd_v2.py` is
the v2 version: it regenerates the same bytes, re-parses the rendered certificate, and enforces the original
header/GROUPS/BLOCKS prefix. Both are stdlib only, import no lane, producer, SAT or checker code, and read only
`groups` and `blocks` from the pinned master JSON (SHA-256 `89133772…db2c`). They do the following.

1. It checks that the master is a GDD(3,4,30) of type 6^5. All 2160 transverse triples occur once; this is a
   direct count, not SAT.
2. It checks that each master derived design D_p is a 3-GDD of type 6^4.
3. It builds the 14,580 zero-sum blocks with labels 3p + β.
4. For each of the 30 × 4 = 120 pairs (p, i), it forms F_i(p) and checks that F_i(p) is 3-partite and 3-regular with
   18 edges.
5. It colours the incidence graph by three successive augmenting-path perfect matchings, then checks (U1) and (U2)
   at every vertex node and every edge node.
6. At every inflated point 3p + β it writes the 9 label classes of each family, with s = −β, as `FRAME i` classes.
7. It checks internally that each class covers the 54 points of (X \ G_a) \ G_i exactly once, and that the 36
   classes list exactly the 648 derived triples of the inflated blocks.
8. v2 only: it requires the rendered header/GROUPS/BLOCKS lines to equal the original certificate's byte for byte.
   It then re-parses the rendered POINT/FRAME records and compares them with the in-memory classes.
9. It writes (v1) or byte-compares against the existing files (v2 `--verify-existing`) only after every check
   passes.

## 5. Mutations (intended failures)

Each mutation changes only one POINT section of the positive certificate.

* **(a) Vertex-permutation break.**
  * At POINT 7 the generator swaps u(a_e, e) and u(b_e, e) on one edge of one family.
  * (U2) and (U3) still hold at e, but (U1) fails at a_e and at b_e.
  * Classes overlap.
* **(b) Zero-sum break with (U1) kept everywhere.**
  * At POINT 31 it adds 1 to u(a*, e) for the three edges at one A-vertex a*.
  * (U1) holds at every vertex, and (U3) fails on those three edges.
  * Only the third-part step (iii) can fail, in both existence and uniqueness. Coverage defects must therefore occur
    only at C-copies; A- and B-copies stay exactly covered.
* **(c) Wrong sum constant.** At POINT 56 the lifts use s′ = s + 1.
  * The classes are still parallel classes of the correct 54 points, by Lemma 1 for s′.
  * None of the listed triples is a derived triple of that point.
* **(d) Duplicated class.** At POINT 89 one FRAME 0 class is replaced by a copy of another FRAME 0 class.

## 6. Status

* **Correctness.** This parent proof has been executed on one instance; see `verdict-v1.md`. The static CLI reviews
  `tz43-tripling-codex-v1` (ACCEPT) and `tz43-tripling-claude-v1` (ACCEPT-WITH-FIXES, 10 MINOR) reviewed v1. Their
  findings are disposed in `dispositions-v1.md`. This v2 note was not re-reviewed.
* **Novelty.** NOT CLAIMED. Lemma 1 is an elementary corollary of König's theorem and may be folklore. No
  literature screen was run at this desk.
