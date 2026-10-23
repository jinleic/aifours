# Problem 16 at n = 8 — no set of five MOQLS(8) has exactly three non-classical squares (K3 = ∅)
# Written partial proof, revision r1

Scope: ONLY m = 3 (class K3). Builds on review/PROOF_K1_K2.r2.md (K1 = K2 = ∅, CORRECTNESS-ACCEPTED (partial) by the
parent) and reuses its §0–§3 (conventions, Prop 1, Lemmas 2, 3, 10, W8, A8, Lemma R + transport) verbatim. Not a
solution of Problem 16 at n = 8 (K4, K5 open here); the proof-free generic GA runs are not part of it. Model-authored.

Result (invariant form). No set of 5 MOQLS(8) has exactly three non-classical squares. Together with K1 = K2 = ∅: every
non-classical set of 5 MOQLS(8) has at least four non-classical squares, and in each of its row (column) standard
forms at least four squares have a weight-3 entry.

## 1. Lemma R for k = 4 classes and q = 3 quantum squares
Lemma R of PROOF_K1_K2.r2 §3 holds verbatim for a 4-net 𝒩 of order 8 (rows, columns and the symbol classes of two
orthogonal classical squares) carrying three assignments Ψ_1, Ψ_2, Ψ_3, each an ONB on every line of 𝒩, with pairwise
tensor-product ONBs: any choice of two classes as rows/columns gives three QLS(8), mutually orthogonal (the 64 tensor
products of each pair are the same vectors re-indexed), orthogonal to the two classical squares |L_D⟩ of the remaining
classes (Prop 1, ONB on D-lines), which are orthogonal Latin squares (two lines of different classes meet once);
vector multisets, ray counts and line-frame supports are unchanged; transport along a net isomorphism φ (Ψ_s ∘ φ⁻¹)
preserves the same data.

## 2. Reduction and the all-frames claim
Let S be a non-classical set of 5 MOQLS(8) in row-0 standard form and S′ := Lemma 10 applied to every square without a
weight-3 entry; the non-classical squares of S′ are the m untouched squares with a weight-3 entry; m ≥ 1 by A8 applied
to S, m ∉ {1, 2} by K1 = K2 = ∅. Class K3: m = 3, quantum squares Q1, Q2, Q3, two classical squares (2 MOLS(8)),
4-net 𝒩.
Claim: Q1, Q2, Q3 each have a weight-3 entry in the frame of EVERY line ℓ of 𝒩. Proof: regrid (§1) with ℓ's class as
rows and ℓ as row 0, pass to standard form, and apply the reduction in this frame: the squares without a weight-3
entry in this frame are replaced (Lemma 10) by classical ones; the resulting set has m_ℓ non-classical squares, namely
the Q's with a weight-3 entry in this frame (ray counts of untouched squares are unchanged). If m_ℓ = 0, all weights of
the regridded set are ≤ 2 (W8) and A8 makes the Q's classical — impossible (their ray counts are those of S′). So
m_ℓ ≥ 1, and m_ℓ ∉ {1, 2} by the invariant K1 = K2 = ∅ result. Hence m_ℓ = 3: all three Q's have a weight-3 entry. ∎

## 3. Finite exclusion over the 2165 nets
Catalogue (trust narrowed to an integer): E–W Table 6 (arXiv:1406.3681v2, layout.txt:761: n = 8, k = 2, Paratopism
2165; paratopism = net isomorphism, PROOF_K1_K2.r2 §4) states that there are exactly 2165 isomorphism classes of
4-nets of order 8 arising from 2 MOLS. The lane's 2165 representatives (Wayback copies of maxMOLS8.2.txt, 2127 pairs,
and nmaxMOLS8.2.txt, 38 pairs; provenance README §4) are valid (every pair Latin and orthogonal) and pairwise
non-isomorphic (2165 distinct nauty certificates of the incidence graphs; evidence/k3_fixed/ew_nets2.json, which also
confirms the maximal/non-maximal labels by exact SAT). Hence they exhaust all classes.
For a K3 set, its 4-net is isomorphic to the net of some representative R; transport Q1, Q2, Q3 (§1) and regrid on R's
own rows/columns; by the claim each Q has a weight-3 entry in the frame of R's row 0. After standard form the supports
satisfy Lemma P (PROOF_K1_K2.r2 §5) for three quantum squares: (P0) row 0 fixed, supp Q_s(0,j) = {j}; (P1) for i ≠ 0:
nonempty, avoiding j and both classical symbols, pairwise disjoint between the three Q's; (P2) on every row, column and
classical line the necessary unitary-pattern conditions (coverage; no two cells sharing exactly one coordinate; no two
coordinates co-occurring in exactly one cell); (P3) for every pair of Q's, no pair of cells shares exactly one
coordinate in both; (P4) each Q has a weight-3 entry. These are exactly the clause families of the FIXED instance
FK3(R) built by enc8_a2.build('fixed', (), (1,2,3), p3=True, p4=(1,2,3), squares=R) (and enc8_b2.encode with the same
data), no symmetry breaking. All 2165 FK3(R) are UNSAT with drat-trim-verified proofs (§4), so K3 = ∅. ∎

## 4. Certificates and controls
- evidence/k3_fixed/all_v1/RESULTS.jsonl (sha256 39a7a3cdad13ac784713951693d16c7303e8f2ab43c0a81cf56a6836257c79e5):
  4330 rows = 2165 nets × {A8r2 (CaDiCaL 3.0.1), B8r2 (kissat 4.0.4)}, all UNSAT.
- Coverage ledger evidence/k3_fixed/K3_COVERAGE_LEDGER.json (sha256 ab63f64c8067ecfa60b73716a252f9c60b184f2adc964c0aa0b30fb04f9e0d98;
  code/k3_ledger.py): per net the catalogue position, normalised-squares hash, exact DIMACS SHA-256 for both encoders,
  and for A the retained zstd binary DRAT proof (SHA-256 re-hashed and matching), drat-trim verdict VERIFIED for all
  2165; no orphan proof files; complete = true.
- Storage/regeneration: CNFs are NOT stored; run_fixed_k3.py builds them in memory from the frozen encoders and the
  catalogue (parse + row-0 normalisation), hashes the exact DIMACS bytes, and streams them through lane FIFOs. Encoder-A
  proofs are retained (zstd); check with `zstd -dc PROOF | drat-trim CNF -i`. Encoder-B results are solver statuses
  with CNF hashes (redundancy only, not a second proof-checked exclusion).
- Positive control of the production --squares path with three quantum squares (evidence/k3_fixed/relaxed_ctrl_v1/
  RECEIPT.json; code/relaxed_squares_control_k3.py): on the AG(2,8) pair (an extendable net), both encoders' CNFs with
  --p4 none are SAT with models satisfying every clause, and SAT with the explicit classical configuration (three
  completing MOLS found by exact SAT) fixed by 1344 unit clauses.
- Deviations (evidence/LOG.md): full batch started before the pilot projection was reported (09:51:33, stopped by
  SIGTERM); a second SIGTERM pause at 11:00:07 for the M2 control; in-flight instances had no rows and were recomputed;
  4 reusable FIFO nodes remain in all_v1.

## 5. Trust boundary for K3
Imported: E–W Table 6 entry (8, 2) = 2165 and E–W's paratopism definition; the definitions of the source. Machine
facts: 2165 drat-trim verifications (encoder A). Written: §1–§3 here plus the accepted K1/K2 package.
