VERDICT: ACCEPT-WITH-FIXES

**FATAL**: none.

**MAJOR**: none. I found no mathematical gap that leaves K3 = ∅ false or unproved. The fixes below are textual or concern trust accounting, but they are required.

**MINOR**

1. **(P3) wording.** `PROOF_K3.r1.md:45-46` says "no pair of cells". It must say "no pair of distinct cells", as in `PROOF_K1_K2.r2.md:88`.
   - Read literally, c = c′ is allowed. Every row-0 cell has support {j} in all three Q's, so it violates P3 against itself.
   - The claim "every transported K3 configuration satisfies Lemma P" is then false as written, and the text no longer reaches "UNSAT ⇒ K3 = ∅".
   - The SAT controls at `PROOF_K3.r1.md:61-64` show the encoder uses distinct pairs only if P3 was enabled in those runs. The text does not say so; state it.

2. **Invariant theorem vs. reduction-defined class.** The theorem at `PROOF_K3.r1.md:8-10` is invariant, but "K3 set" (`PROOF_K3.r1.md:24`, `:40`) is defined as a reduction output with m = 3.
   - Add: for any T with exactly three non-classical squares, the proof at `PROOF_K3.r1.md:26-31` uses only two facts. The Q's have ≥ 9 rays, and the other two squares are classical. So it applies to T itself, and §3 excludes T.
   - Write out the corollary at `PROOF_K3.r1.md:9-10`. In any row standard form, m ≥ 1 by W8 + A8, and m ∉ {1,2,3} by the invariant K1, K2, K3. Columns follow by transposition.

3. **Missing justifications** (one clause each):
   - `PROOF_K3.r1.md:13`: r1 states Lemma R only for k ∈ {5,6}, q ∈ {1,2} (`PROOF_K1_K2.r1.md:51-52`). Add that its proof uses neither k nor q.
   - `PROOF_K3.r1.md:23`: cite W8 (no weight 3 ⇒ all weights ≤ 2) before A8, as at `:30`.
   - `PROOF_K3.r1.md:26`: say the column class is arbitrary, because ℓ-frame weights do not depend on it (`PROOF_K1_K2.r1.md:58-59`).
   - `PROOF_K3.r1.md:42-43`: give the source of (P1).
     - Disjointness and classical-symbol avoidance are rule #3 / W8 applied to all 3 Q–Q pairs and all 6 Q–classical pairs.
     - Alternatively, symbol avoidance follows from (P2) on the classical line through (0, L_D(i,j)) (`PROOF_K1_K2.r2.md:81-82`).
     - Both routes need R's squares to be row-0-normalised. `PROOF_K3.r1.md:58` asserts this only as a code step; state it in the mathematics.

4. **Certificate graph.** Coverage (`PROOF_K3.r1.md:38-39`) needs "isomorphic nets ⇒ equal certificates".
   - This holds for the point–line incidence graph whose only colour classes are {points} and {lines}.
   - It fails if lines are coloured by parallel class, or if the grid or OA columns are encoded. Then distinct certificates would not imply non-isomorphic nets, and line 39 would not follow.
   - State the graph construction used by the lane and by the parent's labelg run.

5. **Encoder claim and P4 control.** "Exactly the clause families" at `PROOF_K3.r1.md:46-47` is an encoder claim.
   - The proof needs only soundness: every clause of FK3(R) is implied by P0–P4 for the row-0-normalised R, with no symmetry breaking. Rephrase it that way and move it to the imports.
   - The positive control at `PROOF_K3.r1.md:61-64` runs with --p4 none on a classical configuration, so it cannot exercise P4. Nothing in §4 witnesses P4's clause semantics.
   - Either say so, or add a control with P4 on and another family relaxed, with the model checked against P4.

6. **Trust boundary.** `PROOF_K3.r1.md:70-71` is incomplete and files the K1/K2 package under "Written".
   - Add K1/K2's transitive base: E–W (8,4) = 1 and (8,3) = 39, Lemma K1-AG's exact checks, the 78 K2 drat-trim verifications, K2 encoder soundness, and the 39-representative checks.
   - Add K3's own machine facts: representative validity, pairwise-distinct certificates (lane and parent), and the binding of each regenerated CNF to its normalised representative (ledger hashes).

7. **Optional cross-check of `PROOF_K3.r1.md:36-39`.** Delete each class from the 39 K2 representatives and canonicalise. The resulting non-maximal classes should number 38 and match nmaxMOLS8.2.txt, independently of E–W.

**What is established** (conditional on Imports)

- **Lemma R for k = 4, q = 3, with transport.** Regridding gives three QLS(8) and two classical |L_D⟩, pairwise orthogonal (Prop 1 in both directions). Vector multisets, ray counts and ℓ-frame supports are unchanged.
- **Reduction.** In every row standard form of a non-classical set, m ≥ 1 and m ∉ {1,2}.
- **All-frames claim (m = 3).** Correct.
  - In each frame, K1/K2 is applied to a genuine set of 5 MOQLS(8), built by Lemma R, per-square unitaries, and Lemma 10(iii) applied in sequence.
  - That set has exactly m_ℓ non-classical squares: untouched Q's keep ≥ 9 rays, while Lemma-10 outputs and the |L_D⟩ are classical.
  - The invariant K1 = K2 = ∅ applies to it with no frame condition. The case m_ℓ = 0 is excluded by W8 + A8 on all five squares.
- **No hidden q = 2 dependence.**
  - Rule #3 / W8, Prop 1, (P1) and (P3) are pairwise, and the text imposes them on all three Q-pairs. Mutual orthogonality has no triple condition.
  - A8 uses t = 5 regardless of q. Lemma 10(iii) covers replacing one or two Q's in sequence.
- **Lemma P (with fix 1).** P0–P4 are necessary conditions for any transported three-quantum-square configuration on a row-0-normalised representative. (P4) is needed only at the line φ⁻¹(R₀), and the claim supplies it.
- **Coverage.** By counting, the 2165 representatives meet every isomorphism class of 4-nets of order 8. The r2 §4 argument that paratopism equals net isomorphism does not depend on k.
- **Conclusion.** K3 = ∅. With K1 = K2 = ∅, every non-classical set of 5 MOQLS(8) has at least four non-classical squares, and in every row or column standard form at least four squares have a weight-3 entry.
- **Still open.** K4, K5, and Problem 16 at n = 8.

**Imports**

- Ball–Simoens definitions (§2.2–2.3), and Lemma 10 with its printed proof.
- K1 = K2 = ∅ (r2, parent-accepted), with its full trust base as listed in fix 6.
- E–W Table 6 entry (8,2) = 2165, and E–W's paratopism definition.
- Machine facts:
  - the 2165 representatives are valid;
  - their net-invariant certificates are pairwise distinct (lane, and parent labelg);
  - 2165 drat-trim VERIFIED encoder-A proofs, checked against CNFs regenerated byte-identically.
- Soundness of the FK3(R) encoding (separate review).
- Not relied on: encoder-B statuses, Wayback provenance, maximal/non-maximal labels, GA runs.
