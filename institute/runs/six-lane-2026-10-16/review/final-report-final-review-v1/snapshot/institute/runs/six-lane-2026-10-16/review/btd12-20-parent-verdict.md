# Balanced ternary design BTD(12,20;4,3,10;6,4): parent verdict

## Result

**BTD(12,20;4,3,10;6,4) does not exist.** No 12 × 20 matrix over {0,1,2} has exactly four entries 1 and three entries 2 in every row, every column summing to 6, and inner product 4 between any two distinct rows. Repeated columns (repeated blocks) are allowed.

[Frozen contract](../screening/info-2-btd12-20-contract.json). Rosin (arXiv:2501.17725v1, Table 1) lists the instance among the Handbook's smallest open BTDs; his May 2025 follow-up does not solve it, and the CPro1 definition file lists it in `OPEN_INSTANCES`. This is an **explicitly listed open finite instance**. Unlike BTD(12,15) and BTD(14,18), B − V = 8 here, so Connor-type determinant conditions are weak; the proof is a computer-assisted case split instead.

## Proof

Final candidate [r2](btd12-20-parent-inputs-r2/notes/case-split-r2.md), SHA-256 `6ef1e73b7e5e2b771cae6c2522d15837cc24ba36d4926d3d77e1b6bfc667e34f` (r1 `d405956c…4da2` unchanged; r2 adds the certificate results and a "carried data" paragraph).

Editorial [r3](../../../../information-science/evidence/six-lane-20261016/btd12-20/notes/case-split-r3.md) `4c1935c6…291a` applies the review wording items and adds count breakdowns; the parent read the full diff and recounted every new number from its regenerated data ([delta check](btd12-20-r3-parent-delta-check.json), PASS). r3 changes no mathematics, code or certificate.

1. **Parity.** Write M = A + 2D with A, D the indicator matrices of the 1s and 2s. Expanding the row inner product gives |A_i ∩ A_k| even, so distinct rows of A are 4-sets ("tetrads") meeting in 0 or 2 points; column covers a_j = 6 − 2d_j ∈ {0,2,4,6}.
2. **Lemma T (self-contained).** A connected family of distinct tetrads pairwise meeting in 0 or 2 points either splits consistently into pairs (d-type: a loopless multigraph on pair-vertices with degrees in {2,4,6}) or spans the 7-point e7 or 8-point e8 tetrad structure. The proof derives the needed [7,3,4], Hamming-dual and [8,4,4] facts locally; it never assumes the 20-coordinate row code is self-dual and does not use the length-24 classification.
3. **Covering case list.** Components have disjoint supports; at most two e-type components fit. Up to row and column permutations every A is one of 3073 covering representatives: 2069 multigraphs with 12 edges (E0) and 1004 patterns with one or two full-support e7/e8 multisets plus a multigraph (E1). Overlaps between E0 and E1 only duplicate work. Columns covered by no row keep their D-variables and need three 2s.
4. **Fixed-A completion.** For each case, a dedicated CNF encodes exactly the existence of D off A with row sums 3, column sums (6 − a_j)/2 and the pair equation x + 2u + 4z = 4. Every one of the 3073 CNFs is UNSAT with a DRAT proof.

## Verification

| Evidence | Observed result | Limit |
|---|---|---|
| Codex CLI `gpt-6.1-sol`, structural review (r1) | **ACCEPT**, no defect in Lemma T, the E0/E1 cover or the Part D predicate; independent derivation of the code facts ([note](btd12-20-structure-codex-review-v1.note.md)) | Mathematics only |
| Claude CLI `claude-opus-5-5`, structural review (r1) | **ACCEPT-WITH-FIXES**, no fatal/major; nine editorial/documentation minors; hand counts E0 n = 4 (7) and n = 10 (173) ([note](btd12-20-structure-claude-review-v1.note.md)) | No-tools review |
| Codex CLI `gpt-6.1-sol`, complete-claim audit of the frozen snapshot | **ACCEPT-WITH-FIXES**, no fatal/major: independently recovers group orders 168/1344, orbit totals 694/52,060 vectors (17/187 full-support orbits), E0 = 7, 59, 312, 550, 616, 352, 173 = 2069, E1 = 1004; verifies SAT-equivalence of the encoder by exhaustive small checks (40 cardinality instances, 23,864 assignments, 128 AND cases); checks all 6,146 CNF/proof hashes and coverage 0..3072 ([note](btd12-20-complete-codex-review-v1.note.md)) | Did not rerun the 3073 proofs |
| **Parent replay** (byte-identical pinned copy, deterministic PATH to the pinned nauty) | all generator outputs, case list, facts, cross-checks and controls reproduce; 3073/3073 CNFs rebuild byte-identically; 3073/3073 proofs `s VERIFIED` with exit 0 ([pin receipt](btd12-20-parent-inputs-r2/parent-pin-receipt.json), [replay result](btd12-20-parent-inputs-r2/runs/case-split-replay-parent-r01/result.json)) | Worker-authored replay driver; the checker binary is byte-identical (SHA `a46c0c71…8e37`) to the parent's own earlier compile of upstream drat-trim 2e3b2dc0 ([provenance](moqls7-parent-proofcheck-v1/parent-result.json)) |

Review findings are [dispositioned](btd12-20-review-dispositions.json). CP-SAT INFEASIBLE answers recorded earlier carry no proof weight.

**Contract mapping.** The nonexistence clause requires a complete unrestricted case split with a correctness proof plus independently checked DRAT/LRAT proofs. Parts A–C are the reviewed case split; the 3073 DRAT proofs were re-checked by the parent with its own checker build.

## Priority, significance and trust limits

- [Priority audit](btd12-15-priority-audit.md) (covers the four Rosin-listed BTDs still open after May 2025): no construction or nonexistence proof found for (12,20). A search miss is not novelty clearance.
- **Significance: modest specialist.** With BTD(12,15) and BTD(14,18), three of the four Handbook BTD instances Rosin still lists as open are now settled; (14,28;8,3,14;7,6) remains. The (12,20) method (tetrad-code structure plus certified case split) differs from the Connor argument used for the other two.
- **Trusted base:** nauty 2.9.3 (two generators cross-checked), Python 3.9.6 and the audited lane scripts, the C compiler, and drat-trim; kissat is only a proof producer. **Not Lean-checked.** Executable provenance beyond the recorded SHA-256 values was not independently rebuilt.

## Status

**FRONTIER: CORRECTNESS-ACCEPTED — computer-assisted proof (reviewed structural reduction + 3073 parent-checked DRAT certificates); NOVELTY-UNCLEAR. The frozen info-2 BTD(12,20;4,3,10;6,4) target is met (2026-10-17 PT): an explicitly listed open instance is settled, with modest significance.**

No commit, push, publication or external contact was authorized.
