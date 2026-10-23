# Problem 16 at n = 8 — no set of five MOQLS(8) has exactly one or exactly two non-classical squares
# Written partial proof, revision r2 (supersedes r1 editorially; r1 unchanged)

Scope: ONLY m = 1 and m = 2 (classes K1, K2). Not a solution of Problem 16 at n = 8; K3–K5 are open here; the
proof-free generic Gram-encoding runs are not part of this proof. Model-authored (lane worker); parent verdict
CORRECTNESS-ACCEPTED (partial) with editorial fixes, which r2 applies (Codex and Claude reviews, minors 1–10).

Result (invariant form). No set of 5 MOQLS(8) has exactly one, or exactly two, non-classical squares. Consequently, in
every row (or column) standard form of a non-classical set of 5 MOQLS(8), at least three squares have a weight-3 entry.

## 0. Setting
Definitions: Ball–Simoens arXiv:2607.12933v2 §2.2–2.3. Indices 0..7; row 0 is the reference row; standard form w.r.t.
row 0: Ψ_s(0,j) = |j⟩ (one unitary per square, preserving orthogonality and classicality). supp, weight w.r.t. the
computational basis. "8 rays ⇔ classical ⇔ MOLS": one row already supplies 8 pairwise orthogonal rays, so a square
with exactly 8 rays has all entries in one ONB, which a per-square unitary sends to the computational basis (symbol
array Latin by the row/column ONB property); by Prop 1 two such classical squares are orthogonal iff their symbol arrays
are orthogonal Latin squares.

## 1. Tools
- Prop 1. Ψ ⊥ Φ ⇔ no pair of distinct cells c, c′ has ⟨Ψ(c),Ψ(c′)⟩ ≠ 0 and ⟨Φ(c),Φ(c′)⟩ ≠ 0 (the tensor-product inner
  product factorizes; 64 orthonormal vectors in C⁶⁴ form a basis). If Φ is classical, Ψ is an ONB on Φ's symbol lines.
- Lemma 2. If supp u ∩ supp v = {k} then ⟨u,v⟩ = ū_k v_k ≠ 0.
- Lemma 3 (any n). Let an ONB of Cⁿ consist of vectors of weight ≤ 2. A vector with support {a,b} has exactly one partner
  with support {a,b}, and no other basis vector meets {a,b}. Proof: in the bipartite support graph (vectors vs
  coordinates) every component spans the space of its coordinates, so it has as many vectors as coordinates. A
  component with ≥ 2 vectors contains no weight-1 vector (Lemma 2 against any vector meeting its coordinate) and no
  coordinate of degree 1 (a unit column with one nonzero entry would make that vector a basis vector, weight 1); with
  all vectors of weight 2 and all coordinates of degree ≥ 2, edge counting gives degree exactly 2: the component is a
  single cycle of length 2k. For k ≥ 3 consecutive vectors share exactly one coordinate, contradicting Lemma 2. So k = 2.
- Lemma 10 (source, printed proof raw.txt:345–356). While Ψ (no entry of weight ≥ 3) has an entry ψ of weight 2, say
  supp ψ = {a,b}, take the unitary U on span{|a⟩,|b⟩} (fixing the other basis vectors) with Uψ = |a⟩ up to phase, and
  apply U to every entry whose support is exactly {a,b}; the number of weight-2 entries strictly decreases, so the
  process ends with a classical Ψ′. Same-or-disjoint step: if ψ(c′) ⊥ ψ(c), supp ψ(c) = {a,b}, |supp ψ(c′)| ≤ 2, then
  Lemma 2 forbids |supp ψ(c′) ∩ {a,b}| = 1. Properties: (i) supp Ψ′(c) ⊆ supp Ψ(c); (ii) weight-1 entries (in
  particular row 0 of a standard form) are literally unchanged; (iii) the non-orthogonality graph only shrinks, so every
  square orthogonal to Ψ is orthogonal to Ψ′ — Ψ′ does not depend on the other squares, so the lemma can be applied to
  several squares of a set one after another (each application changes one square and leaves the "no weight ≥ 3"
  hypothesis of the unprocessed squares untouched); (iv) each row/column is either untouched or mapped entirely by U,
  so Ψ′ is a QLS.
- W8. In row-0 standard form of 5 MOQLS(8), at a cell (i,j) with i ≠ 0 the five supports are pairwise disjoint (rule #3:
  ⟨k|Ψ_s(c)⟩⟨k|Ψ_u(c)⟩ = 0 because Ψ_s(c)⊗Ψ_u(c) ⊥ Ψ_s(0,k)⊗Ψ_u(0,k) = |k⟩⊗|k⟩) and avoid j (rule #2: column j contains
  (0,j) = |j⟩). So Σ_s w_s ≤ 7: weights ≤ 3, a weight-3 entry forces weight 1 in the other four squares, and
  "weight 3" ⇔ "weight ≥ 3".

## 2. Theorem A8 (for a set of 5 MOQLS(8)): if all weights are ≤ 2 in some row standard form, the set is classical.
Proof as in r1 §2 (Lemma 10 on the other four squares first; the six classes 𝒞 form a net; E ⊆ V; every line of 𝒞 meets
E in 0 or 2 cells = V ∩ M; H is 6-regular on 8 + 8 vertices, two a-cells share ≥ 2·6 − 8 = 4 neighbours, H connected;
(0,a) ∈ V ∖ E; E = ∅). For t squares the bound is 2(t + 1) − 8, so the argument needs t ≥ 4; here t = 5.

## 3. Lemma R (regridding) and transport
Lemma R as in r1 §3 (net 𝒩 of order 8 with k ∈ {5, 6} classes; q = 7 − k assignments Ψ_s, each an ONB on every line, with
pairwise tensor-product ONBs; any choice of row/column classes gives q QLS orthogonal to each other and to the k − 2
classical squares |L_D⟩ of the remaining classes; vector multisets, ray counts and line-frame supports unchanged).
Transport. If φ : 𝒩 → 𝒩′ is a net isomorphism, the assignments Ψ_s ∘ φ⁻¹ satisfy the hypotheses of Lemma R on 𝒩′ (lines
go to lines), have the same vector multisets (hence ray counts), and for every line ℓ the ℓ-frame supports of Ψ_s are
carried to the φ(ℓ)-frame supports of Ψ_s ∘ φ⁻¹.

## 4. K1 = ∅
Lemma K1-AG (restricted to nets containing the direction ∞; this suffices because the bridge representative
{∞, 0, s1, …, s4} contains it). Let 𝒩 consist of six direction classes of AG(2,8) including ∞, and Ψ an ONB on every
line of 𝒩. Then Ψ has 8 rays. Proof as in r1 §4 (frame r = 0 in the ∞ class; T = the 3 free directions, one of the 56
three-subsets of GF(8); t0 = t1+t2+t3 ∉ T; supports along t0-lines lie in b + rV with W = V ∪ {0} a 2-dimensional
F2-subspace; |rV ∩ r′V| = 1 for r ≠ r′; Lemma 2 ⇒ disjoint ⇒ singletons). Exact checks: evidence/k1_analytic/checks_v2.json.
Bridge. Egan–Wanless Table 6 (layout.txt:763) gives ONE paratopism class for (n, k) = (8, 4). E–W define paratopism for
lists (layout.txt:145–146) as the action of row/column/within-column symbol permutations and the S_{k+2} permutation of
the orthogonal-array columns, which absorbs the ordering (so sets and lists have the same classes); reducedness affects
only the Equality column (layout.txt:737–738); the parallel classes of a net are recovered from incidence (two lines
are parallel iff equal or disjoint). Hence the Paratopism entry is the number of isomorphism classes of (k+2)-nets:
every 4-MOLS(8) 6-net is isomorphic to the AG representative c + s·r (four distinct nonzero s). For a K1 set (one
non-classical Ψ, four classical squares) transport Ψ along this isomorphism (§3); Lemma K1-AG makes it classical —
contradiction. (Independent confirmation, not needed: FIXED K1 certificates, evidence/k1_cert_v1.)

## 5. K2 = ∅
Reduction. Let S be a non-classical set of 5 MOQLS(8) in row-0 standard form, and S′ := Lemma 10 applied to every square
of S without a weight-3 entry. The non-classical squares of S′ are exactly the m untouched squares with a weight-3
entry; m ≥ 1 by A8 applied to S; m ≠ 1 by §4.
All-frames claim (m = 2, quantum squares Q1, Q2, 5-net 𝒩): both have a weight-3 entry in the frame of every line ℓ of 𝒩
— proof as in r1 §5 (regrid with ℓ as row 0; standard form; no weight 3 in Q1 ⇒ Lemma 10 ⇒ K1 set; none in both ⇒ A8).
Lemma P (necessary support conditions of the transported K2 set on a representative's grid, row-0 standard form):
- (P0) row 0 is fixed: supp Q_s(0,j) = {j}.
- (P1) for cells (i,j) with i ≠ 0 only: supp Q_s(i,j) ≠ ∅; j ∉ supp (rule #2); L_D(i,j) ∉ supp for each classical D
  ((P2) on the classical line through (0, L_D(i,j)), whose row-0 vector is |L_D(i,j)⟩); supp Q1(i,j) ∩ supp Q2(i,j) = ∅
  (rule #3).
- (P2) on every row, column and classical line (including its row-0 cell) the supports satisfy the following NECESSARY
  conditions for the support pattern of a unitary (not full unitary realizability): every coordinate is covered (unit
  columns); no two cells share exactly one coordinate (Lemma 2 for orthogonal rows); no two coordinates co-occur in
  exactly one cell (Lemma 2 for orthogonal columns).
- (P3) no pair of distinct cells shares exactly one coordinate in both Q1 and Q2 (Prop 1 with Lemma 2).
- (P4) each of Q1, Q2 has a weight-3 entry in the row-0 frame (the all-frames claim; by W8 equivalent to weight ≥ 3).
These are the clause families of FIXED FK2(R_k) (enc8_a2.py / enc8_b2.py, --mode fixed --slopes "" --squares R_k
--quantum 12 --p4 12, no symmetry breaking; row-0 cells constant). All 39 instances are UNSAT with drat-trim-verified
proofs (lane and parent replay), hence K2 = ∅.
Invariant restatement: K1 = K2 = ∅ means that no set of 5 MOQLS(8) has exactly one or two non-classical squares. In any
row (column, by transposition) standard form of a non-classical set, the reduction yields m ≥ 3, i.e. at least three
squares with a weight-3 entry.

## 6. Catalogue: trust narrowed to the integer 39
Coverage follows from three facts: (a) the 39 representatives are valid 3-MOLS(8) (checked locally and by the parent);
(b) their 39 nauty certificates are pairwise distinct (lane pynauty; parent labelg), so the 39 nets are pairwise
non-isomorphic; (c) E–W Table 6 (layout.txt:762) states that there are exactly 39 paratopism (= net-isomorphism, §4)
classes for (8, 3). Hence the 39 nets exhaust all classes; archive authenticity of the Wayback copies is no longer
needed (provenance retained in r1 §6). Table 5's "38 maximal" serves only as a consistency check (matched by the local
maximality SAT checks).

## 7. Certificates, controls, deviations
Unchanged from r1 §7 (78 verified proofs; per-row artifacts in evidence/MANIFEST_K2_ARTIFACTS_v2_1105.sha256; parent
replay: 78/78 CNFs regenerated byte-equal and 78/78 VERIFIED with the parent's checker; fail-closed controls; M2
production --squares control; deviations in evidence/LOG.md; 78 leftover FIFO nodes recorded).

## 8. Trust boundary
Imported: the definitions of the source; E–W Table 6 entries for (8, 3) = 39 and (8, 4) = 1 together with E–W's
paratopism definition. Re-checked: Lemma 10 from its printed proof. Machine facts: the 78 drat-trim verifications
(solver correctness not trusted). Written (model-authored, reviewed): Prop 1, Lemmas 2, 3, W8, A8, Lemma R + transport,
Lemma K1-AG (with exact field checks), reduction, all-frames claim, Lemma P.
