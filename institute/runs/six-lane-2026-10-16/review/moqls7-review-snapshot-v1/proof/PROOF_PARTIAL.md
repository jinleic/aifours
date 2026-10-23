# Problem 16 at n = 7: partial results (reductions), with proofs

Status: PARTIAL / CANDIDATE (lane write-up 2026-10-17 PDT). Problem 16 at n = 7 is NOT solved. Pending: parent
re-derivation, hostile review, priority audit. Definitions, rules #1–#3, Lemma 10, Theorem 9 as in
Ball–Simoens arXiv:2607.12933v2 (§2–3). Weights are always taken w.r.t. a stated reference row (standard form):
"standard form w.r.t. row i0" = move row i0 to the top (simultaneous row permutation) and apply to each square the
unitary sending its row-i0 entries to |1⟩,…,|7⟩ (in column order).

## 0. Results

- **Theorem A.** If, in standard form w.r.t. some row, every entry of every square of a set of 4 MOQLS(7) has weight
  ≤ 2, the set is classical. (Also gives Ball–Simoens Theorem 5 at n = 7 by a different route.)
- **Theorem B.** If three squares of a set of 4 MOQLS(7) are classical, so is the fourth.
- **Theorem C (reduction).** Let S be a non-classical set of 4 MOQLS(7). Applying Lemma 10 to every square that has
  only weight-≤2 entries (w.r.t. row 1) gives a non-classical set S′ in which at least two squares are non-classical,
  and for EVERY reference row and EVERY reference column at least two squares of S′ have an entry of weight 3.
  At such an entry the other three squares have weight-1 entries whose supports, with it, partition the 6 coordinates
  other than the column index.

Consequently a negative answer at n = 7 (M(7) = 4) needs ≥ 2 genuinely quantum squares with weight-3 entries in every
frame; the one-quantum-square and all-weight-≤2 regimes are closed.

Imported results (not re-proved here): Lemma 10 ([2, Lemma 13], proof in the source); Theorem 9 (Shrikhande 1961);
Bose: complete sets of MOLS(n) ↔ affine planes of order n; M. Hall Jr., Proc. AMS 4 (1953) 912–916: the projective
plane of order 7 is unique (Desarguesian); Egan–Wanless, Math. Comp. 85 (2016) 799–824 (arXiv:1406.3681v2, Table 7
"Number of reduced lists of k-maxMOLS(n)": for n = 7 maximal lists exist only for k = 1, 2, 6) — a computer
classification, hence every set of 3 MOLS(7) extends to a complete set. Finite facts (L), (C) below are re-checked by
two independent implementations (`code/impl1_incidence.py`, `code/impl2_chart.py`).

## 1. Elementary lemmas

**Prop 1 (orthogonality = disjoint non-orthogonality graphs).** For a QLS Ψ let N(Ψ) be the set of unordered pairs of
cells {c, c′} with ⟨ψ(c), ψ(c′)⟩ ≠ 0. QLS Ψ, Φ of order n are orthogonal iff N(Ψ) ∩ N(Φ) = ∅.
*Proof.* ⟨ψ(c)⊗φ(c), ψ(c′)⊗φ(c′)⟩ = ⟨ψ(c),ψ(c′)⟩⟨φ(c),φ(c′)⟩; n² orthonormal vectors in an n²-dimensional space
form a basis. ∎
(Side remark, re-derivation of the known Theorem 2: rows/columns are orthogonal, and every cell is non-orthogonal to
≥ 1 entry of each other row, so |N(Ψ)| ≥ n²(n−1)/2 with equality iff Ψ is classical; the pairs not in a common row or
column number n²(n−1)²/2; so t MOQLS(n) have t ≤ n−1, and t = n−1 forces every square classical.)

**Lemma 2 (two vectors sharing one coordinate).** If supp u ∩ supp v = {k}, then ⟨u, v⟩ = ū_k v_k ≠ 0.

**Lemma 3 (weight ≤ 2 bases).** In an ONB of C^n all of whose vectors have weight ≤ 2 (w.r.t. a fixed ONB), every
vector of weight 2 with support {a,b} has exactly one partner in the basis with the same support {a,b}, and no other
basis vector meets {a,b}.
*Proof.* Consider the bipartite support graph (vectors vs coordinates). A connected component with k vectors spans the
coordinate space of its k′ coordinates, so k = k′ (unitary). If k ≥ 2, no vector of weight 1 lies in it (a weight-1
vector e_a and a vector meeting a would share exactly one coordinate, Lemma 2), so all its vectors have weight 2 and
every coordinate has degree ≥ 2 (a degree-1 coordinate gives a column of the unitary with one nonzero entry, forcing
that vector to have weight 1); counting edges, the component is a single cycle of length 2k. For k ≥ 3 consecutive
vectors share exactly one coordinate — impossible by Lemma 2. So k = 2. ∎

**Lemma 4 (weights).** In standard form w.r.t. a row i0, at a cell c outside row i0 the supports of the four squares
are pairwise disjoint subsets of [7] \ {col(c)} (rules #2, #3). Hence every weight is ≤ 3, and a weight-3 entry forces
the other three entries at c to have weight 1, the four supports partitioning [7] \ {col(c)}.

## 2. Theorem A

Let Ψ1,…,Ψ4 be in standard form w.r.t. row 1 with all weights ≤ 2.
1. Apply Lemma 10 successively to Ψ1,…,Ψ4. The result Ψ′1,…,Ψ′4 is a set of classical MOQLS with
   (i) supp Ψ′s(c) ⊆ supp Ψs(c), (ii) weight-1 entries (in particular the first rows) unchanged up to phase
   (the procedure only rotates entries whose pattern is exactly the chosen weight-2 pattern). Their symbol arrays
   L′1,…,L′4 (L′s(c) = k iff Ψ′s(c) ∝ |k⟩) are 4 MOLS(7) with first row 1,…,7.
2. Theorem 9 (n − 3 = 4, n ≠ 4) extends them to 6 MOLS(7); with rows and columns these form an affine plane of order 7
   (Bose), which is AG(2,7) (Hall). So L′1 is isotopic to the Latin square defined by three distinct parallel classes
   of AG(2,7).
3. **Fact (C)** (impl 1: all 336 ordered class triples; impl 2: closed forms y − mx): in such a square, for every pair
   of symbols {a,b} the graph G_ab on the 14 cells carrying a or b, with edges joining cells in a common row or column,
   is connected (one 14-cycle). This is invariant under isotopy.
4. Suppose Ψ1 has an entry of weight 2, with support {a,b}; let E = {c : supp Ψ1(c) = {a,b}}. By Lemma 3 each row and
   each column meets E in 0 or 2 cells. By (i), L′1(c) ∈ {a,b} for c ∈ E. If a row meets E in c, c′, then
   L′1(c) ≠ L′1(c′), so E ∩ row = the two cells of that row carrying a or b in L′1; likewise for columns. Hence E is a
   union of connected components of G_ab, so E = ∅ or E = V(G_ab). But (1,a) ∈ V(G_ab) by (ii) and (1,a) ∉ E (weight 1).
   So E = ∅ — contradiction. Hence Ψ1, and likewise every square, has only weight-1 entries: the set is classical. ∎

*Control (Theorem 5 at n = 7).* For 5 MOQLS(7), Lemma 4's count gives weights ≤ 2 automatically (5 disjoint
supports in 6 coordinates); Lemma 10 gives 5 MOLS(7); they extend (deficiency 1); steps 3–4 apply verbatim.

## 3. Theorem B

Let Ψ2, Ψ3, Ψ4 be classical; in standard form Ψr(c) ∝ |Lr(c)⟩ with L2, L3, L4 three MOLS(7).
1. By Prop 1, Ψ1 ⊥ Ψr iff the seven vectors of Ψ1 on each line {c : Lr(c) = x} are pairwise orthogonal. So Ψ1 is an
   ONB on every line of the 5-net 𝒩 = {rows, columns, L2-, L3-, L4-lines}.
2. By Egan–Wanless (no maximal 3-, 4- or 5-MOLS(7)) L2, L3, L4 extend to a complete set; with Bose and Hall the eight
   parallel classes form AG(2,7), 𝒩 is a set of 5 of them, and the other 3 form the "free" set F.
3. **Fact (L)** (impl 1: explicit incidence; impl 2: Möbius charts + harmonic conjugates, identical class lists for all
   56 three-sets F): for every 3-set F of classes there are exactly two classes c ∉ F that are *linear*: for distinct
   parallel lines L0, L1 of class c and distinct q, q′ ∈ L1, the sets A(q) = {p ∈ L0 : the line pq has a class in F}
   have size 3 and |A(q) ∩ A(q′)| ≤ 1. (In the chart where c is at infinity, F is a 3-subset of F7 with distinct
   differences; the three non-linear classes are the harmonic conjugates of each point of F w.r.t. the other two.)
4. Fix a linear class c ∈ 𝒩 and a line L0 of class c; B = {Ψ1(p) : p ∈ L0} is an ONB. For q on another line L1 of
   class c, the four lines through q of the classes 𝒩 \ {c} meet L0 in four distinct points p with Ψ1(q) ⊥ Ψ1(p); the
   remaining three points of L0 are A(q) (the 8 lines through q: one parallel to L0, four of 𝒩, three of F). So the
   B-expansion of Ψ1(q) is supported in A(q). For q ≠ q′ on L1, Ψ1(q) ⊥ Ψ1(q′) and their supports meet in ≤ 1 point,
   hence (Lemma 2) in none. Seven non-empty pairwise disjoint subsets of the 7-set L0 are singletons, so Ψ1(q) ∝ Ψ1(p)
   for some p ∈ L0. The lines of class c cover all points, so Ψ1 has exactly the 7 rays of B: Ψ1 is classical. ∎

*Control (the mechanism does not over-claim).* For 4 or 5 free classes no class is linear (both implementations; a
k-subset of F7 with k ≥ 4 cannot have distinct differences). Correspondingly the Corollary-7 pair of order 7 (Example 15,
H = {1,2,4}; f0 = f − 2x, classical slope 4) is an exact non-classical orthonormal assignment on a 3-net: checked exactly
with seventh-root-of-unity sums (impl 2): QLS, orthogonal, 49 distinct rays. Mutations: affine f → 7 rays; a determined
direction → orthogonality fails.

## 4. Theorem C

Let S = {Ψ1,…,Ψ4} be non-classical, standard form w.r.t. row 1. Apply Lemma 10 to every square without weight-3
entries; call the result S′ (still 4 MOQLS(7), non-classical: squares with weight-3 entries are unchanged and are
non-classical, since a classical square in standard form has only weight-1 entries; if no square had weight 3, Theorem
A would make S classical). Let i0 be any row. In standard form w.r.t. i0:
- if all entries of S′ had weight ≤ 2, Theorem A would make S′ classical;
- if exactly one square Ψ had weight-3 entries, apply Lemma 10 (frame i0) to the other three: they become classical
  and stay orthogonal to Ψ, so Ψ is classical by Theorem B — but a classical square has only weight-1 entries in every
  standard form. Contradiction.
So ≥ 2 squares of S′ have weight-3 entries w.r.t. row i0; they are non-classical. Transposing every square preserves
all notions, so the same holds for every reference column. The last sentence of Theorem C is Lemma 4. ∎

## 5. What remains open (precisely)

Sets of 4 MOQLS(7) with ≥ 2 non-classical squares, each pair of frames (any row/column) exhibiting weight-3 entries in
≥ 2 squares. For two quantum squares plus two classical ones, the classical part is a pair of MOLS(7), which need not
extend (Egan–Wanless: 5 species of maximal 2-MOLS(7)), and no class of a 4-net is linear; Theorem B's mechanism does
not apply. No witness and no exclusion is claimed for this regime.

## 6. Evidence

`evidence/impl1.json`, `evidence/impl2.json` (facts (L), (C), controls, mutations), `evidence/SHA256SUMS.txt`,
`evidence/LOG.md`. Sources: `sources/quantum-latin-2607.12933v2.pdf` (SHA-256 2d60d45f…), `sources/1406.3681v2.pdf`
(Egan–Wanless, SHA-256 f01b494f…). Novelty/priority: not established (no literature search beyond the two sources).
