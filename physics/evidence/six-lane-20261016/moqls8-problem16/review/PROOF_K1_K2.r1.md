# Problem 16 at n = 8 — exclusion of the classes K1 and K2: written partial proof, revision r1

Scope: ONLY the cases m = 1 (K1) and m = 2 (K2) of the reduction below. This is NOT a solution of Problem 16 at
n = 8, and the proof-free generic Gram-encoding runs (GA-K2, GA-K5) are not part of it. Model-authored (lane worker),
not peer reviewed. Supersedes, without editing them, the K1 status in review/PROOF_N8_PARTIAL.md ("Certificate run
(DRAT) pending") and the "exploratory" status of review/K1_ANALYTIC_N8.md (whose "84" is corrected to 56 in
review/K1_ANALYTIC_N8_ERRATUM.md).

## 0. Setting
Definitions as in Ball–Simoens arXiv:2607.12933v2 §2.2–2.3 (sources/2607.12933v2.raw.txt): a QLS(8) is an 8×8 array
of unit vectors of C⁸ whose rows and columns are orthonormal bases (ONBs); QLS Ψ, Φ are orthogonal if the 64 vectors
Ψ(c)⊗Φ(c) form an ONB of C⁸⊗C⁸; a set is classical if every square has exactly 8 rays (up to phase), equivalently is
equivalent to a set of MOLS. Indices 0..7; row 0 is the reference row; standard form w.r.t. row 0: Ψ_s(0,j) = |j⟩
(one unitary per square; preserves orthogonality and classicality). supp Ψ(c) = {k : ⟨k|Ψ(c)⟩ ≠ 0}, weight = |supp|.
In standard form a square is classical iff all weights are 1.

## 1. Tools
- Prop 1. Ψ ⊥ Φ ⇔ there is no pair of distinct cells c, c′ with ⟨Ψ(c),Ψ(c′)⟩ ≠ 0 and ⟨Φ(c),Φ(c′)⟩ ≠ 0.
  (⟨Ψ(c)⊗Φ(c), Ψ(c′)⊗Φ(c′)⟩ = ⟨Ψ(c),Ψ(c′)⟩⟨Φ(c),Φ(c′)⟩.) In particular if Φ is classical, Ψ is an ONB on every
  symbol line of Φ.
- Lemma 2. If supp u ∩ supp v = {k} then ⟨u,v⟩ = ū_k v_k ≠ 0.
- Lemma 3. In an ONB of C⁸ all of whose vectors have weight ≤ 2, a vector with support {a,b} has exactly one partner
  with support {a,b}, and no other vector meets {a,b} (component argument; proof in the n = 7 lane,
  moqls7-problem16/review/PROOF_PARTIAL.md §1, independent of n).
- Lemma 10 (source, raw.txt:342–356). Statement: a QLS Ψ without entries of weight ≥ 3 admits a classical Ψ′ such that
  every QLS orthogonal to Ψ is orthogonal to Ψ′. Construction (from the printed proof): repeatedly pick a support
  {a,b} and apply one unitary U on span{|a⟩,|b⟩} (fixing the other basis vectors) to every entry whose support is
  exactly {a,b}. Same-or-disjoint step: if supp Ψ(c) = {a,b} and Ψ(c′) ⊥ Ψ(c) with weight ≤ 2, Lemma 2 forbids
  |supp Ψ(c′) ∩ {a,b}| = 1, so supp Ψ(c′) is {a,b} or disjoint from it. Properties used: (i) supp Ψ′(c) ⊆ supp Ψ(c)
  for every c; (ii) weight-1 entries (in particular row 0 of a standard form) are literally unchanged; (iii) the
  non-orthogonality graph only shrinks, so orthogonality to every other square of a set is preserved, in any order of
  application; (iv) Ψ′ is again a QLS.
- W8. In row-0 standard form of 5 MOQLS(8), at a cell (i,j), i ≠ 0, the five supports are pairwise disjoint (rule #3:
  ⟨k|Ψ_s(c)⟩⟨k|Ψ_u(c)⟩ = 0 from Ψ_s(c)⊗Ψ_u(c) ⊥ |k⟩⊗|k⟩) and avoid j (rule #2), so Σ_s w_s ≤ 7: every weight is ≤ 3,
  and a weight-3 entry forces weight 1 in the other four squares.

## 2. Theorem A8 (all weights ≤ 2 in some row standard form ⇒ classical)
Fix s. Apply Lemma 10 to the four squares Ψ_r (r ≠ s) one after another: they become classical Ψ′_r with symbol
arrays L′_r (Latin, first row identity), pairwise orthogonal and orthogonal to Ψ_s; hence (Prop 1) Ψ_s is an ONB on
every line of the six classes 𝒞 = {rows, columns, L′_r-lines}. 𝒞 is a net: lines of different classes meet in exactly
one cell (rows/columns trivially; rows or columns with L′_r-lines since L′_r is Latin; L′_r- with L′_r′-lines since
L′_r ⊥ L′_r′). Apply Lemma 10 to Ψ_s: Ψ′_s classical, symbol array L′_s orthogonal to every L′_r, supports shrink.
If Ψ_s had an entry with support {a,b}, let E = {c : supp Ψ_s(c) = {a,b}} ⊆ V = {c : L′_s(c) ∈ {a,b}} (16 cells).
Every line M ∈ 𝒞 meets V in one a-cell and one b-cell, and (Lemma 3, Ψ_s|M an ONB of weights ≤ 2) meets E in 0 or 2
cells, hence in 0 cells or in exactly V ∩ M. So E is a union of components of the bipartite graph H on V joining the
a-cell and b-cell of each line of 𝒞. H is 6-regular on 8 + 8 vertices (the six lines through a cell meet only there);
two a-cells share ≥ 6 + 6 − 8 = 4 neighbours, so H is connected and E ∈ {∅, V}. The row-0 cell (0,a) ∈ V has weight
1, so E = ∅: contradiction. Thus every square has only weight-1 entries: the set is classical. ∎

## 3. Lemma R (regridding), general form
Let 𝒩 be a net of order 8 with k classes (k = 5 or 6) on a 64-point set P, and Ψ_1, …, Ψ_q : P → unit vectors of C⁸
(q = 7 − k ∈ {1, 2}) such that each Ψ_s is an ONB on every line of 𝒩, and for s ≠ u the 64 vectors
Ψ_s(p)⊗Ψ_u(p) form an ONB. Choose two classes R, C as rows and columns, number their lines, and number the lines of
every other class D. With A_s[i][j] = Ψ_s(R_i ∩ C_j) and L_D[i][j] = number of the D-line through R_i ∩ C_j:
(i) each A_s is a QLS(8); (ii) each L_D is a Latin square, distinct L_D are orthogonal (two lines of different classes
meet exactly once), so the k − 2 classical squares |L_D⟩ are mutually orthogonal; (iii) A_s ⊥ |L_D⟩ (Prop 1:
A_s is an ONB on the D-lines); (iv) A_s ⊥ A_u for s ≠ u (the set of 64 tensor products is the same set of vectors,
re-indexed); (v) the multiset of vectors of A_s equals that of Ψ_s, so its number of rays (classical or not) is
unchanged, and for any line ℓ of 𝒩 the ℓ-frame supports {p ∈ ℓ : ⟨Ψ_s(p),Ψ_s(q)⟩ ≠ 0} do not depend on the gridding.
Conversely a set of 5 MOQLS(8) with q non-classical and 5 − q classical squares yields such data with 𝒩 = {rows,
columns, classical symbol classes} (k = 7 − q). Re-gridding is a re-indexing of points, not a claimed set isotopy.

## 4. K1 = ∅ (one quantum square, four classical)
Lemma K1-AG. If 𝒩 consists of six direction classes of AG(2,8) and Ψ is an ONB on every line of 𝒩, then Ψ has 8 rays.
Proof. Grid with a net class as rows (direction ∞) and frame r = 0 (vectors e_c after one unitary). The other net
directions are c + t·r = b, t ∈ A ⊂ GF(8), |A| = 5 (GF(8) = GF(2)[x]/(x³+x+1)); T = GF(8) ∖ A = {t1,t2,t3} — one of the
56 three-subsets of GF(8) (the free directions are finite because ∞ is a net direction). t0 = t1+t2+t3 ∉ T (else two
t's coincide), so the t0-class is in the net. For r ≠ 0, (r,c) lies on the t-line through (0, c + t r) for each
t ∈ A, so supp Ψ(r,c) ⊆ c + rT. On the t0-line c + t0 r = b the seven points q_r = (r, b + t0 r), r ≠ 0, have
supp ⊆ b + rV with V = T + t0 = {t2+t3, t1+t3, t1+t2}: three distinct nonzero elements with sum 0, so W = V ∪ {0}
is a 2-dimensional F2-subspace. For r ≠ r′, rW ≠ r′W (a = r′/r ≠ 1 cannot stabilize the 3-set V inside the cyclic
group GF(8)* of order 7) and two distinct 2-dimensional subspaces of F2³ meet in a 1-dimensional one, so
|rV ∩ r′V| = 1. The Ψ(q_r) are pairwise orthogonal with supports avoiding b and pairwise meeting in ≤ 1 coordinate,
hence (Lemma 2) disjoint; seven nonempty disjoint subsets of 7 coordinates are singletons. Every point off the frame
lies on a t0-line, so all weights are 1: Ψ is classical. ∎ (Exact checks for all 56 T, both implementations, with
explicit counters: code/k1_analytic_checks_v2.py → evidence/k1_analytic/checks_v2.json.)
Bridge (import): Egan–Wanless, Table 6 (arXiv:1406.3681v2, layout.txt:763): for n = 8, k = 4 there is ONE paratopism
class (Equality 4800, Isotopism 3, Trisotopism 2) — paratopy = isomorphism of the 6-net (Section 2, layout.txt:121–150);
the linear set c + s·r (four distinct nonzero s ∈ GF(8)) is a 4-MOLS(8), so every 4-MOLS(8) 6-net is isomorphic to six
AG(2,8) direction classes. Given a K1 set (one non-classical Ψ, four classical squares) apply Lemma R (q = 1, k = 6)
along the isomorphism; Lemma K1-AG makes Ψ classical — contradiction. Independent confirmation (not needed for the
logic): the FIXED K1 instance (AG 6-net) is UNSAT for encoders A8 and B8 with DRAT proofs "s VERIFIED"
(evidence/k1_cert_v1).

## 5. K2 = ∅ (two quantum squares, three classical)
Reduction. Let S be a non-classical set of 5 MOQLS(8) in row-0 standard form; S′ := Lemma 10 (row-0 basis) applied to
every square without a weight-3 entry. S′ is a set of 5 MOQLS(8) in row-0 standard form (not necessarily isotopic to
S) whose non-classical squares are exactly the m untouched squares with a weight-3 entry (W8: weights ≤ 3);
m ≥ 1 by A8; m ≠ 1 by §4 (with Lemma R). Class K2: m = 2, non-classical Q1, Q2, classical squares forming 3 MOLS(8).
All-frames claim. In a K2 set, Q1 and Q2 both have a weight-3 entry in the frame of EVERY line ℓ of the 5-net
𝒩 = {rows, columns, three symbol classes}. Proof: regrid (Lemma R, q = 2, k = 5) with ℓ's class as rows and ℓ as row 0
(any other class as columns) and pass to standard form. If neither Q1 nor Q2 had a weight-3 entry there, all weights
of this set of 5 MOQLS(8) would be ≤ 2 (W8) and A8 would make Q1, Q2 classical — but their ray counts are those of S′.
If, say, Q1 had none, Lemma 10 (this frame) would replace Q1 by a classical square, leaving Q2 unchanged and
non-classical with four classical squares: a K1 set, impossible by §4. ∎
Finite exclusion. 𝒩 is isomorphic to the 5-net of one E–W representative R_k (k = 1..39, §6). Transport Q1, Q2 along
the isomorphism and regrid on R_k's own rows/columns (Lemma R); by the all-frames claim both have a weight-3 entry in
the frame of R_k's row 0. After standard form w.r.t. row 0, the supports satisfy (Lemma P; proofs as in the n = 7
lane, moqls7-problem16/review/PROOF_CANDIDATE_r2.md §3, with 8 for 7): (P1) nonempty, avoid the column coordinate and
the three classical symbols, disjoint between Q1 and Q2; (P2) on every row, column and classical line the 8×8 support
pattern is that of a unitary (coverage; no two cells sharing exactly one coordinate; no two coordinates co-occurring
in exactly one cell); (P3) no pair of cells shares exactly one coordinate in both squares; (P4) each of Q1, Q2 has a
weight-3 entry. These are exactly the clause families of the FIXED instance FK2(R_k) built by enc8_a2.py and
enc8_b2.py with --mode fixed --slopes "" --squares R_k --quantum 12 --p4 12 (no symmetry breaking). All 39 FK2(R_k) are
UNSAT (§7), so K2 = ∅. ∎

## 6. Catalogue (imported completeness; local validity)
Source: Egan–Wanless species representatives (their data page, ref. [36] of arXiv:1406.3681v2; HTTP 503 on
2026-10-17), retrieved from the Wayback Machine: maxMOLS8.3.txt (capture 20191225120510) and nmaxMOLS8.3.txt
(20191225172426), SHA-1/base32 equal to the CDX digests (AEUWGV6W…54XZ, SBV375NG…YESS; identical digests in several
captures); local SHA-256 aa415da4…8071 and f8156dc1…e4b5. Limits: authenticity rests on the archive; COMPLETENESS (every
3-MOLS(8) is paratopic to one of these 39; E–W Table 6, layout.txt:762: 39 paratopism classes for n = 8, k = 3, of
which Table 5 lists 38 maximal) is an imported computer classification.
Local validity (evidence/k2_fixed/ew_nets.json): 39 triples, each Latin and mutually orthogonal (symbols relabelled
so that row 0 is 0..7); a fourth orthogonal square exists exactly for the non-maximal one (exact SAT). Pairwise
non-isomorphism is WITNESSED BY NAUTY canonical certificates of the point–line incidence graphs (pynauty 2.8.8.1 in the
lane venv env/venv8; evidence/k2_fixed/nauty.json: 39 distinct certificates; relabelled copies reproduce their
certificates). The earlier invariants (ew_nets_inv2/inv3) left four collisions and a VF2++ attempt timed out; they are
not used as witnesses.

## 7. Certificates, controls, deviations
- 78 FIXED instances (39 nets × encoders A8r2 (CaDiCaL 3.0.1) / B8r2 (kissat 4.0.4)): all UNSAT; every binary DRAT
  proof stored zstd-compressed and checked by streaming into drat-trim (source d834b649…, lane binary 111b0405…) with
  "s VERIFIED" (evidence/k2_fixed/all_v1/RECEIPT.json fd80a2f8…; per-row receipts and all artifacts hashed in
  evidence/MANIFEST_K2_ARTIFACTS_*.sha256). solve_secs = 5.0 is the watchdog sampling interval, not solver time.
- Controls: 10/10 fail-closed fixed-pattern controls for each base encoder (evidence/controls/controls8_{a,b}.json);
  production --squares path relaxed control on nmax00 (evidence/k2_fixed/relaxed_ctrl_v1/RECEIPT.json): without (P4)
  SAT for both encoders with models satisfying every clause, and SAT with the explicit classical configuration
  (two completing MOLS) fixed by 896 unit clauses; exact checkers for the classical AG(2,8) set and a non-classical
  Theorem-6 pair over Z2×Z4 (evidence/controls/exact8_{a,b}.json).
- Deviations (evidence/LOG.md): K3 batch launched before reporting its projection (stopped by SIGTERM); the §3 pilot
  ran proof-free and the certified batch covered all 39 nets (37 never piloted); VF2 job killed by the harness at
  its time cap while a solver was paused; processes stopped only by SIGTERM/SIGSTOP otherwise; one read-only git clone
  of public tooling (march_cu).

## 8. Trust boundary for K1/K2
Imported: Lemma 10 (source, used via its printed proof); E–W Table 6 rows n = 8, k = 3 and k = 4 and the
completeness/authenticity of the 39-representative catalogue; definitions of the source. Machine facts: the 78 drat-trim
verifications (and the CNF regeneration from the frozen encoders). Written (model-authored): Prop 1, Lemmas 2, 3, W8,
A8, Lemma R, Lemma K1-AG, the reduction and all-frames claim, Lemma P.
