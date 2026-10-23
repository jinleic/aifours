# FROZEN r1 — partial result: every AME(4,6) state has at least 49 non-zero coefficients in every product orthonormal basis

**Frozen.** Written once; the freeze time is this file's mtime (host clock). The SHA-256 is recorded outside the file
(README §1, `evidence/LOG.md`). Corrections go to r2.

**Status and scope.** CANDIDATE PROOF of a PARTIAL result, worker-written and not yet independently reviewed or
replayed.
- Contract: `institute/runs/six-lane-2026-10-16/screening/phys-2-ame46-support-contract.json` (SHA-256
  1baee48355c8e67e42c14ecf8164d4ace9591e6c5288c82f824ddec410d85f15). The target is 59 versus 60; this file proves only
  the lower bound 49.
- **Builds on:**
  - `review/SUPPORT_LOWER42.r2.md` (1db90164…1418), cited as L42;
  - `review/SUPPORT_LOWER46.r2.md` (fac5242b90554de86cd6bd8e17fb2a6800fbd4a3e71d2e4a99f154d5a216f35b), cited as
    L46: the parent accepted s ≥ 46;
  - `review/SUPPORT_LOWER48.r2.md` (70daac01707158b2842159dbdc6713afa33e541c51f100a91034fdf4d432f60e), cited as
    L48: the parent accepted s ≥ 48, with Lemmas 17 and 18;
  - the engine specifications `review/ENGINE_V3.r1.md` (fd7c7447…4449; Lemma 19), `review/ENGINE_V4.r1.md`
    (fd1d47f2…8c12; J, Lemma 20, completeness) and `review/ENGINE_V5.r1.md`
    (5393238f0aee2f37bf1641e644b0555691320ffbd4fccfdb65838b135e06bf0a; the review fixes and the asserted bindings),
    with the exact CNF schema `review/V4_PROOF_SCHEMA.r1.md`
    (f558e75b6d7f87ea5db3f8025be8475694715d1f8e2f94f88673094936e0b986).
- **Model reviews of the engine lemmas.**
  - Lemmas 19 and 20, J and the realizable-support completeness argument: Codex and Claude v4 reviews,
    ACCEPT-WITH-FIXES, with the mathematics accepted (`review/ame46-v4-codex-review-v1.note.md`,
    `review/ame46-v4-claude-review-v1.note.md`). The fixes are in v5.
  - The parent bound the W generator independently (`review/ame46-v4-triangle-parent-binding-v1/result.json`).
  - A Codex v5 delta review is running.
- **Computer-assisted part:** the five cases of the s = 48 layer, (24,0), (26,2), (27,3), (28,4) and (30,6), run with
  engine v5 in proof mode with `--joint`, plus `--triangles` for (24,0). The UNSAT proofs are gzip LRAT streams; the
  two worker checkers are same-author and give reproducibility only. The parent's independent replay is pending.
- No novelty or priority claim. Crowded field; a search miss is not novelty.

## Theorem

Let ψ ∈ (C^6)^{⊗4} be an AME(4,6) state (L42 LF32–34); arbitrary complex amplitudes are allowed. For every product
orthonormal basis, at least 49 of the 1296 coefficients of ψ are non-zero.

By the basis reduction (L42 LF47–50), it suffices to treat the computational basis.

## 1. Written lemmas used (all proved in the cited files)
- **L48 Lemma 17** (officer counting, f(α) ≥ 0) and **L48 Lemma 18** (a binary code).
- **Lemma 19** (officer placement; `review/ENGINE_V3.r1.md` §3). For a normalized AME state with officer set T:
  - (C1) every line outside V_j × V_k holds exactly one officer;
  - (C2) every line in V_j × V_k holds at most one;
  - (C3) for i ≠ j and a ∈ V_i, exactly |V_j| − d_{i,a} of the lines (a, b), b ∈ V_j, hold an officer.
- **J** (`review/ENGINE_V4.r1.md` §3). A line of V_i × V_j meets N if and only if it holds no officer (L42-2(a),
  L42-4), for every e.
- **Lemma 20** (doubled triangles, e = 0; `review/ENGINE_V4.r1.md` §4). For any coordinate i, values a ≠ a′, and
  z1, z2, z3 with the triangle agreement pattern, the six points (a; z_m), (a′; z_m) do not all lie in N.
  - At e = 0 each pair forms a closed 2×2 block, giving δ(z_m) − δ(z_n) ≡ π. Summing over the triangle gives π ≡ 0,
    a contradiction.
  - The moduli never enter.

## 2. The cases for s ≤ 48
By L42 §0, s = 72 − t + e with e ≥ 0 (L42-4). L48 already excludes s ≤ 47. The new pairs are those with s = 48, i.e.
e = t − 24 for t = 24..36.

| t | e (s = 48) | how excluded |
|---|---|---|
| 36 | 12 | Tarry (L42) |
| 33–35 | 9–11 | L42 corollary (LF202–204) |
| 32 | 8 | L46-16 |
| 31 | 7 | L46-13 |
| 30 | 6 | §3 (engine v5) |
| 29 | 5 | L48 Lemma 17 (t = 29 impossible) |
| 28 | 4 | §3 |
| 27 | 3 | §3 |
| 26 | 2 | §3 |
| 25 | 1 | L42-7 (e ≠ 1) |
| 24 | 0 | §3 (with W) |

Every row is impossible, so s ≥ 49. ∎

## 3. The engine-v5 computation
**Final CNF of a profile.** This is exactly `review/V4_PROOF_SCHEMA.r1.md`:
- base B1–B4 (L46 r2 §3 step 2);
- J: the officer-placement CNF of Lemma 19, shifted by nv0, and the linking clauses;
- W: the Lemma 20 clauses, for e = 0 only;
- Lex_Γ: the lex-leader chains of v2's generators in the shared point order with false < true. At k = 1 one
  substitutes q0 = true and drops the tautological clause;
- one all-negative blocking clause per recorded solution.

**Completeness** (realizable-support argument; L48 r2 §3, ENGINE_V4 §5 and ENGINE_V5 §3):
- Let ψ be a normalized AME state with parameters (t, e, profile), non-classical part N and officers T.
- For g ∈ H = ⟨Γ⟩, g·ψ is AME with non-classical part g(N) and officers g(T). Let N* be the lex-least member of H·N.
- (N*, g(T)), with the base auxiliaries (hl = [line meets N*]), the officer-CNF auxiliaries (C3 indicators and counter
  partial sums) and the lex chains (q_k = "prefixes agree"), satisfies base, J, W (if e = 0) and Lex_Γ.
- B3 fixes Σ n = 2h + e, so each blocking clause excludes exactly its recorded Y.
- Hence a certified final UNSAT makes N* a recorded Y. Every recorded Y has an exact, T-independent rejection, which
  contradicts realizability.

**Code-level bindings** (ENGINE_V5 §4) are asserted at build time in every run: V/d identity, two-sided hl, variable
ranges, linking equal to the schema, lex freshness, and the W count = 2·Π|V_k|(|V_k| − 1) with clause shapes.

## 4. Results
All runs used v5 `code/large_t_joint5.py` (e57067c247d3e5c6ca8e7f28035a6d9ec45b1a77238fe8ccd5046eff7f0033f8) under
CPython 3.13.9 and CaDiCaL 3.0.1 (601c9fa8…d1fa), on 2026-10-17 PDT, each as one chunk of `code/run_chunk5.sh`
(3231d8e754a8233510d80c0d3dc16f7368ea6679719310d8b95455646f548926). Parent GO: 16:02.

| case | report (SHA-256) | profiles: enumerated / Lemma 17 | recorded Y | final UNSAT streams |
|---|---|---|---|---|
| (30,6) | `evidence/large_t_joint5_t30_e6.json` 201bd511f961368170f5f39dfdeef50ff1b676f76260ddb808badc1c7fad64f6 | 1 / 1 | 0 | 1 |
| (28,4) | `evidence/large_t_joint5_t28_e4.json` 6bdfcd65ab2cf663d4d3f41c7dc777803bb182ba336fc0f7caf74b95e8fec1c0 | 5 / 2 | 0 | 5 |
| (27,3) | `evidence/large_t_joint5_t27_e3.json` 9604a3496f1af6a5befbb6555259f33b0f85ea3585f013aa365b31ba329e4167 | 3 / 3 | 0 | 3 |
| (26,2) | `evidence/large_t_joint5_t26_e2.json` 4b1289f57f959def42b298de28c6e21c9d4f7154f866bb5e2d57469384d1d633 | 24 / 1 | 0 | 24 |
| (24,0) | [[T24 REPORT]] | [[T24 PROFILES]] | [[T24 Y]] | [[T24 STREAMS]] |

[[T24 DETAILS]]

## 5. Executable record
- **Receipts** (same-author reproducibility):
  - `code/v5_receipt.py` (76872dbe21e269b23a069698611c14426af2f4feb7f73dfd47a18b8ad0bd04b5);
  - for the four e > 0 cases: `evidence/v5_receipt_s48_e_pos.json`
    (fa0bcf45befef061c36b008d6ef7598cb6e4411a1eda1a716936ce143b5e4ee9), all_required_true. Every final CNF is
    regenerated with matching SHA, every stream is verified by both worker checkers, and profile completeness and
    Lemma 17 are recomputed;
  - for (24,0): [[T24 RECEIPT]].
- **Proof streams:** gzip text LRAT in `explore/large_t_joint5/`, with paths and SHA-256 values in the receipts. CNFs
  are not stored; they are regenerated from the schema.
- **Controls:** `evidence/guard_smoke5.json` (1d9c3cb07ff99cbbd3365beb94f04c6f4042c232a7e1893206cd89324c5ee4a0),
  K1–K7.
- **Parent's independent route** (pending): regenerate every final CNF from V4_PROOF_SCHEMA, replay each gzip stream's
  additions with the parent's drat-trim, and check every Y certificate.

## 6. Not claimed
- Nothing about 59 versus 60 beyond the bound 49. With Pandya's upper bound 60, the range is 49..60.
- Exploration runs, the void 15:13 run, UNKNOWN runs and older-engine outputs are not part of this proof.
- No novelty or priority claim.
