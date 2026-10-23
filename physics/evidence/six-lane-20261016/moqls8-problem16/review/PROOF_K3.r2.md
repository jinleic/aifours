# Problem 16 at n = 8 — no set of five MOQLS(8) has exactly three non-classical squares (K3 = ∅)
# Written partial proof, revision r2 (r1 unchanged; applies the Claude review minors 1–7; Codex review: ACCEPT)

Scope: ONLY m = 3. Builds on review/PROOF_K1_K2.r2.md (K1 = K2 = ∅, parent-accepted, partial) and reuses its §0–§3
(conventions; Prop 1; Lemmas 2, 3, 10; W8; A8; Lemma R + transport). Not a solution of Problem 16 at n = 8 (K4, K5
open); the proof-free generic GA runs are not part of it. Model-authored; reviewed by model reviewers; parent full
replay of all 2165 certificates PASS (review/moqls8-k3-parent-replay-summary-v1.json).

Theorem (invariant). No set T of 5 MOQLS(8) has exactly three non-classical squares.
Corollary. In every row standard form of a non-classical set of 5 MOQLS(8), let m be the number of squares with a
weight-3 entry: m ≥ 1 by W8 + A8 (no weight-3 entry ⇒ all weights ≤ 2 ⇒ classical), and after the reduction of
PROOF_K1_K2.r2 §5 the reduced set has exactly m non-classical squares, so m ∉ {1, 2, 3} by K1, K2, K3 = ∅. Hence at
least four squares have a weight-3 entry; the same holds for column standard forms by transposition.

## 1. Lemma R for k = 4 and q = 3
The proof of Lemma R (PROOF_K1_K2.r2 §3) uses neither k nor q: for a 4-net 𝒩 of order 8 (rows, columns, two classical
symbol classes) carrying Ψ_1, Ψ_2, Ψ_3, each an ONB on every line, with pairwise tensor-product ONBs, any choice of
row/column classes yields three mutually orthogonal QLS(8) orthogonal to the two classical squares of the remaining
classes (orthogonal Latin squares), with unchanged vector multisets, ray counts and line-frame supports; transport along
a net isomorphism φ (Ψ_s ∘ φ⁻¹) preserves the same data.

## 2. The all-frames claim
Let T have exactly three non-classical squares Q1, Q2, Q3 (each with ≥ 9 rays) and two classical squares; 𝒩 is its
4-net. (The argument uses only these two facts; it applies to T itself and to any K3 set produced by the reduction.)
Claim: each Q has a weight-3 entry in the frame of every line ℓ of 𝒩. Proof: regrid (§1) with ℓ's class as rows and ℓ
as row 0 — the column class is arbitrary, since ℓ-frame weights do not depend on it — and pass to standard form (per-
square unitaries). Replace every Q without a weight-3 entry in this frame by its Lemma-10 classical replacement (W8:
such a Q has all weights ≤ 2; Lemma 10(iii) allows replacing one or two Q's in sequence). The result is a genuine set
of 5 MOQLS(8) whose non-classical squares are exactly the m_ℓ Q's with a weight-3 entry here (untouched Q's keep ≥ 9
rays; Lemma-10 outputs and the classical squares are classical). If m_ℓ = 0, no Q has a weight-3 entry in this frame,
so the regridded set itself (before any replacement) has all weights ≤ 2 (W8; classical squares have weight 1) and A8
makes it classical — contradicting the ≥ 9 rays of the Q's. If m_ℓ ∈ {1, 2}, the replaced set is a set of 5 MOQLS(8)
with exactly one or two non-classical squares, impossible by the invariant K1 = K2 = ∅. Hence m_ℓ = 3. ∎

## 3. Finite exclusion
Catalogue coverage: E–W Table 6 (layout.txt:761: n = 8, k = 2, Paratopism 2165; paratopism = isomorphism of the
4-nets, PROOF_K1_K2.r2 §4, an argument independent of k). The 2165 representatives are valid (every pair Latin and
orthogonal) and pairwise non-isomorphic: their certificates — of the point–line incidence graph (64 point vertices, 32
line vertices, adjacency = incidence) with ONLY the two vertex classes {points} and {lines} distinguished, so that
isomorphic nets have equal certificates — are pairwise distinct (lane: pynauty, evidence/k3_fixed/ew_nets2.json;
parent: labelg on the same uncoloured incidence construction, points of degree 4, lines of degree 8). By counting they
meet every class. Optional cross-check (independent of E–W's labels): deleting each of the five classes from each of
the 39 representatives of 3-MOLS(8) gives 195 4-nets in exactly 38 classes, equal (by certificate) to the 38 classes of
nmaxMOLS8.2.txt (evidence/k3_fixed/crosscheck_nmax.json; code/k3_crosscheck_nmax.py).
Transport and Lemma P. The 4-net of T is isomorphic to the net of a representative R; we use R with each square's symbols
relabelled so that its row 0 is 0..7 (row-0 normalisation, part of the mathematics, not only a code step). Transport the
Q's (§1), regrid on R's rows/columns; by §2 each Q has a weight-3 entry in the frame of R's row 0. After standard form
w.r.t. row 0, the supports satisfy:
- (P0) supp Q_s(0,j) = {j};
- (P1) for i ≠ 0: supp ≠ ∅; j ∉ supp (rule #2); L_D(i,j) ∉ supp for both classical squares D, and supp Q_s(i,j) ∩
  supp Q_u(i,j) = ∅ for all three pairs s ≠ u — rule #3 / W8 applied to all 3 Q–Q pairs and all 6 Q–classical pairs
  (for a classical square the support at (i,j) is {L_D(i,j)}; equivalently, symbol avoidance is (P2) on the classical
  line through (0, L_D(i,j)));
- (P2) on every row, column and classical line, the necessary unitary-pattern conditions (coverage; no two cells
  sharing exactly one coordinate; no two coordinates co-occurring in exactly one cell);
- (P3) for every pair of Q's, no pair of DISTINCT cells shares exactly one coordinate in both;
- (P4) each Q has a weight-3 entry (W8: equivalently weight ≥ 3).
Hence the FIXED instance FK3(R) is satisfiable whenever T exists (soundness of the encoding, §5). All 2165 FK3(R) are
UNSAT with drat-trim-verified proofs (§4). So T does not exist. ∎

## 4. Certificates and controls
- RESULTS.jsonl sha256 39a7a3cdad13ac784713951693d16c7303e8f2ab43c0a81cf56a6836257c79e5; coverage ledger
  K3_COVERAGE_LEDGER.json sha256 ab63f64c8067ecfa60b73716a252f9c60b184f2adc964c0aa0b30fb04f9e0d98: 2165 nets, every
  encoder-A CNF bound by its exact DIMACS SHA-256 to the row-0-normalised representative, every A proof retained and
  VERIFIED; parent full replay PASS (CNFs regenerated byte-equal, all 2165 VERIFIED with the parent's checker).
- Production --squares positive control with three quantum squares (evidence/k3_fixed/relaxed_ctrl_v1/RECEIPT.json):
  (P3) ENABLED (no --no-p3), (P4) OFF (--p4 none): SAT with models satisfying every clause, also with the explicit
  classical configuration fixed by 1344 units. Limitation: (P4) is NOT exercised by any SAT control. A P4-on attempt
  (code/p4_on_control_k3.py; evidence/k3_fixed/p4on_ctrl_v1, no receipt) gave: (P3) off on the AG pair → UNSAT (A8r2);
  one classical square only → UNKNOWN at its 1200 s limit; no classical square → stopped by SIGTERM; abandoned per the
  parent's instruction. P4's clauses were checked by source review (Codex) instead.
- Deviations (evidence/LOG.md): premature full start and SIGTERM pause (09:51), second pause (11:00:07), 4 FIFO nodes.

## 5. Trust boundary (complete)
Imports: Ball–Simoens definitions (§2.2–2.3) and Lemma 10 (via its printed proof); E–W Table 6 entries (8,4) = 1,
(8,3) = 39, (8,2) = 2165 and E–W's paratopism definition. Soundness of the encodings (separately reviewed): every clause
of FK2(R) and FK3(R) is implied by P0–P4 for the row-0-normalised R, with no symmetry breaking (enc8_a2.py).
Machine facts, K1/K2 base: Lemma K1-AG's exact field checks (56 three-sets); the 78 K2 drat-trim verifications; the 39
representatives' validity and pairwise-distinct certificates. Machine facts, K3: the 2165 representatives' validity and
pairwise-distinct certificates (lane pynauty, parent labelg); the binding of each regenerated CNF to its representative
(ledger hashes); 2165 drat-trim VERIFIED encoder-A proofs (lane and parent). Written: §1–§3 here and the accepted K1/K2
package. Not relied on: encoder-B statuses, Wayback provenance, maximal/non-maximal labels, GA runs.
