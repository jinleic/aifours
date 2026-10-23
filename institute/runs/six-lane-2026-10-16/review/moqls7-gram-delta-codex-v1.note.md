DISPOSITION: ACCEPT-WITH-FIXES

## FATAL

none.

## MAJOR

**D-MAJOR-1 — The old lifecycle finding remains partially open.** `lane/code/gram_certify_r4.py:141` performs a blocking FIFO open before entering the monitor at `lane/code/gram_certify_r4.py:144`. A writer exiting before opening its proof path can therefore strand the parent outside its watchdog. Native limits, direct logs and monitored shutdown repair the other principal defects. `lane/review/GRAM-ENCODING.r2.md:155` correctly acknowledges the remaining startup failure paths.

**Correction:** retain this qualification and use bounded startup in the parent replay. The later `proof_stream.py` controls establish prospective behavior; they do not establish r4’s failure handling. This is a liveness defect, not a counterexample to any completed UNSAT certificate.

**D-MAJOR-2 — Added control coverage does not satisfy the historical timing requirement.** `lane/README.md:91` requires matched controls before production. The additional suite began after the final K2 certificate: `desk-digests/chronology.json:89`, `desk-digests/chronology.json:114`. The original frozen-control rerun did precede production; the additional symmetry and component tests did not.

**Correction:** record closure as retrospective component validation and an explicit timing deviation. Keep the old control findings PARTIAL with respect to preproduction compliance. This affects chronology/protocol compliance, not the mathematical implication conditional on independent replay.

## MINOR

**D-MINOR-1 — One sentence misdates the review requests.** `lane/review/K2-THEOREM.r2.md:130` says, “After K2 production, the static reviews requested additional matched controls.” The Codex request already existed at 19:16:11 (`parent/moqls7-gram-review-codex-v1.receipt.json:14`), before K2 production began at 19:31:09 (`desk-digests/chronology.json:59`).

**Correction:** “After K2 production, additional matched controls requested in the static reviews were run on the unchanged encoders.”

**D-MINOR-2 — Status parsing still exceeds the stated CR-only normalization.** `lane/code/gram_certify_r4.py:146` uses `strip()`, preserving the old discrepancy with `lane/review/AMENDMENT-1.r1.md:28`. Unknown identifiers are now rejected at `lane/code/gram_certify_r4.py:89`. The retained production logs contain the expected exact status; this is a parser-contract discrepancy.

**Correction:** document r4’s actual normalization and require exact CR-normalized checker status in the parent replay. No alteration of historical receipts is appropriate.

## T1 — Old findings

“Codex” and “Claude” identify the two pinned original reviews.

| Finding id | Status | New evidence file:LF | Reason |
|---|---|---|---|
| Codex MAJOR-1 | RESOLVED | `parent/moqls7-ls147-parent-v1/REPORT.md:3`; `lane/review/K2-CLASSIFICATION-SOURCE.r1.json:8` | Independent representative/group/union checks and pinned EW source remove dependence on the producer binary and seeds. |
| Codex MAJOR-2 | RESOLVED | `lane/code/gram_certify_r4.py:180`; `lane/evidence/gram/controls_code_sha256.txt:1`; `desk-digests/chronology.json:14` | Actual receipts bind encoder, driver, decoder and classfile; original frozen controls and their code pins are retained. |
| Codex MAJOR-3 | PARTIAL | `lane/code/gram_certify_r4.py:137`; `lane/code/gram_certify_r4.py:141`; `lane/review/GRAM-ENCODING.r2.md:155` | Limits, logs and result gating improved; startup can still block before monitoring. |
| Codex MAJOR-4 | PARTIAL | `lane/code/gram_review_controls.py:106`; `lane/review/GRAM-ENCODING.r2.md:124` | Missing matched tests now exist, but were run after K2 certification. |
| Codex MINOR-1 | RESOLVED-BY-DOMAIN | `lane/review/GRAM-ENCODING.r2.md:25`; `lane/review/GRAM-ENCODING.r2.md:65` | Overlay explicitly replaces the frozen docstring’s K1 §8 justification. |
| Codex MINOR-2 | RESOLVED | `lane/review/GRAM-ENCODING.r2.md:30` | Diagonal, Hermitian and conjugate-linearity conventions are explicit. |
| Codex MINOR-3 | RESOLVED-BY-DOMAIN | `lane/review/GRAM-ENCODING.r2.md:3`; `lane/review/REVIEW-CORRECTIONS.r2.json:9` | Corrected status/prose and canonical-reference overlay preserve frozen bytes. |
| Codex MINOR-4 | RESOLVED-BY-DOMAIN | `lane/review/GRAM-ENCODING.r2.md:142`; `lane/code/gram_certify_r4.py:98`; `lane/code/gram_certify_r4.py:109` | Production nets exclude the malformed branch; production supplies no fixes. |
| Codex MINOR-5 | RESOLVED | `lane/review/K1-THEOREM.r3.md:82`; `lane/README.md:7` | Full driver digest and baseline suffix are corrected. |
| Codex MINOR-6 | RESOLVED | `desk-digests/old-manifest-lf-erratum.json:5`; `MANIFEST.json:8` | Explicit erratum supplies LF+1 while retaining the old manifest. |
| Claude MAJOR-1 | RESOLVED | `parent/moqls7-ls147-parent-v1/REPORT.md:26`; `parent/moqls7-ls147-parent-v1/REPORT.md:43`; `lane/review/K2-CLASSIFICATION-SOURCE.r1.json:8` | Free-action proof, independent counts/groups/union and primary-source binding are supplied. |
| Claude MAJOR-2 | PARTIAL | `lane/code/gram_certify_r4.py:141`; `lane/code/gram_certify_r4.py:147`; `lane/review/K2-THEOREM.r2.md:75` | Result/provenance handling is substantially repaired; startup liveness remains and historical solver-binary provenance is explicitly unbound. |
| Claude MAJOR-3 | PARTIAL | `lane/review/GRAM-ENCODING.r2.md:106`; `lane/review/GRAM-ENCODING.r2.md:124`; `lane/code/proof_stream.py:7` | Component coverage and mutation interpretation are repaired retrospectively; new transport tests concern a different transport. |
| Claude MINOR-1 | RESOLVED-BY-DOMAIN | `lane/review/GRAM-ENCODING.r2.md:25`; `lane/review/GRAM-ENCODING.r2.md:65` | Accepted K1 plus independent G4 replaces the insufficient §8 reference. |
| Claude MINOR-2 | RESOLVED-BY-DOMAIN | `lane/review/REVIEW-CORRECTIONS.r2.json:9`; `lane/review/GRAM-ENCODING.r2.md:3` | Canonical reference and corrected document supersede the historical draft wording. |
| Claude MINOR-3 | RESOLVED-BY-DOMAIN | `lane/review/GRAM-ENCODING.r2.md:142`; `lane/code/gram_certify_r4.py:98` | Valid production geometry excludes malformed literals and structural empty clauses. |
| Claude MINOR-4 | RESOLVED-BY-DOMAIN | `lane/code/gram_certify_r4.py:100`; `lane/code/gram_certify_r4.py:109`; `lane/code/gram_review_controls.py:45` | Production never supplies fixes; the added control harness checks fixed-input prerequisites. |
| Claude MINOR-5 | PARTIAL | `lane/code/gram_certify_r4.py:89`; `lane/code/gram_certify_r4.py:146` | Unknown identifiers are rejected; arbitrary whitespace stripping remains. |
| Claude MINOR-6 | RESOLVED | `lane/review/GRAM-ENCODING.r2.md:128`; `lane/review/K2-THEOREM.r2.md:123` | Exploratory results are separated from certificates; mutation claims are narrowed correctly. |
| Claude MINOR-7 | RESOLVED | `lane/review/GRAM-ENCODING.r2.md:43`; `lane/review/GRAM-ENCODING.r2.md:61`; `lane/review/GRAM-ENCODING.r2.md:90` | Transition convention, minimality/order prerequisites and row/column normalization are sufficiently explicit. |
| Claude MINOR-8 | RESOLVED | `lane/review/GRAM-ENCODING.r2.md:9`; `lane/evidence/gram/controls_code_sha256.txt:1`; `lane/review/K1-THEOREM.r3.md:82` | Full relevant pins are available and contextual hash errors are corrected. |

**Are ALL previous MAJORs resolved? No.** Codex MAJOR-3/Claude MAJOR-2 retain the r4 startup-liveness defect. Codex MAJOR-4/Claude MAJOR-3 retain the unmet preproduction timing requirement; prospective transport controls do not test historical r4. Historical solver-binary provenance is unavailable and its unsupported attribution was withdrawn. None supplies a remaining mathematical soundness objection once T6 succeeds.

## T2 — Production domain

**Validated; no production counterexample found.**

The actual calls are:

- A: `build(2,L,True,False,None)` for K2 and `build(3,None,True,True,None)` for K3 (`lane/code/gram_certify_r4.py:98`).
- B: two squares, decoded net and heavy for K2; three squares, heavy and sym without a net for K3 (`lane/code/gram_certify_r4.py:104`).

In a valid \(d\)-net, an off-line point has exactly \(d-1\) distinct forbidden intersections on a frame line. Thus its structural candidate set has \(8-d\) points: five for K2 and six for K3. Two such sets intersect in at least \(2(8-d)-7\), giving three and five G2 products respectively.

Removing a shared transition-line point removes an already-forbidden point, so G3 still has five/six candidates. Heavy has 42 off-line candidate points, each with five/six available literals. Consequently A’s insufficient-cardinality/empty-disjunction branches and B’s zero/one-item malformed branches cannot occur. Internal `None` sentinels remain ordinary structural-zero handling; none is emitted as a literal.

The K3 symmetry literals join distinct rows and columns, hence exist. No production call combines sym with a net or supplies `fix`. B’s permissive malformed-fix API remains a general-API hazard only.

## T3 — Complete K2 bridge

**The implication is sound, conditional on the stated computational inputs. No mathematical gap or circularity found.**

1. **Straightening and C1.** Independent unitaries and entry phases permit straightening L alone (`lane/sources/2607.12933v2.layout.txt:111`; `lane/review/LEMMAS.md:8`). Its Latin labels follow from row/column ONBs. Tensor inner products with L reduce exactly to equal-symbol orthogonality, yielding all 21 ONB lines (`lane/review/LEMMAS.md:16`).

2. **Transport.** A paratopy gives one point bijection carrying the three line classes to the representative’s line classes. Apply that same bijection to both quantum assignments. New rows/columns remain ONBs, their tensor vectors are globally reindexed, and their projective-ray sets are unchanged. This preserves both non-classical squares and all partner orthogonalities (`parent/moqls7-ls147-parent-v1/REPORT.md:77`). It need not belong to the narrower source set-isotopy group.

3. **Necessary Gram conditions and heavy.** G1 is line orthogonality. Expansion in an ONB gives G2 over arbitrary complex coefficients. Unitary transition matrices give G3, including the shared-point block. Tensor inner-product factorization gives G5 (`lane/review/GRAM-ENCODING.r2.md:39`). For G4, the two-support replacement preserves every previously zero inner product simultaneously, hence every partner tensor orthogonality (`lane/review/LEMMAS.md:54`). A light K2 member would become classical while the other non-classical member remains untouched, contradicting accepted K1. Both squares are therefore heavy in every basis, including all 21 own-line frames.

4. **Extension to both CNFs.**
   - A’s product auxiliaries take their actual conjunction values (`lane/code/gram_enc.py:83`). Its G2 clauses express the zero/one implications; ordered G3 clauses express nonempty transitions and singleton reversal; G5 excludes shared edges (`lane/code/gram_enc.py:95`, `lane/code/gram_enc.py:100`, `lane/code/gram_enc.py:115`). Set a heavy guard true at an actual witness. Every \((n-2)\)-subset then contains a true literal; other guards may be false (`lane/code/gram_enc.py:45`, `lane/code/gram_enc.py:134`).
   - B’s product auxiliaries are the same conjunctions. Set `counter2` states to actual prefix thresholds ≥1 and ≥2; every recurrence and G2/G3 clause follows (`lane/code/gram_encB.py:41`, `lane/code/gram_encB.py:134`, `lane/code/gram_encB.py:146`, `lane/code/gram_encB.py:171`). Set heavy-counter states to actual prefix thresholds and choose true returned witnesses on each line (`lane/code/gram_encB.py:60`, `lane/code/gram_encB.py:200`). G5 is direct edge exclusion at `lane/code/gram_encB.py:184`.

   K2 receives neither symmetry units nor fixing clauses. Every genuine configuration therefore extends through every auxiliary family. Missing positivity/rank/phase-realizability constraints only weaken the relaxation.

5. **Decoder and coverage.** `square_from_key` restores natural first row/column and reads the 36 interior digits row-major (`lane/code/k2_classes.py:22`). Both production encoders use this decoder. Index \(i=0,\ldots,146\) selects the first field of nonempty line \(i+1\) (`lane/code/gram_certify_r4.py:94`, `lane/code/gram_certify_r4.py:186`). Parent LS147 coverage is an accepted input. The mechanical binding table reports exact index coverage and no failed static checks for both routes (`desk-digests/k2-cert-r4-binding-table.json:3`, `desk-digests/k2-cert-r4-binding-table.json:22`), with the indexing rule explicit at `desk-digests/k2-cert-r4-binding-table.json:4454`.

## T4 — References

- **K2 r1:** `lane/review/K2-THEOREM.r1.md:16` cites K1 r2; `lane/review/K2-THEOREM.r1.md:27` cites Gram r1. These are historical dependency-document pointers. Standalone acceptance must substitute accepted K1 r3 and corrected Gram r2; K2 r2 does so at lines 16 and 27. The theorem assumptions themselves do not change.
- **LEMMAS:** `lane/review/LEMMAS.md:77` still names Gram r1. This is a benign backward reference to the same G4 argument; pointing additionally to r2 would clarify the active proof source.
- **Gram r2:** `lane/review/GRAM-ENCODING.r2.md:134` names K2 r1 explicitly as the original theorem/trust-boundary document. Historical, not an active dependency error.
- **Amendments:** both K2 texts correctly identify AMENDMENT-2 as separate K3 work. Its own old Gram-r1 reference at `lane/review/AMENDMENT-2.r1.md:5` is likewise historical and creates no K2 dependency.
- **Original production protocol:** `lane/review/AMENDMENT-1.r1.md:18` names K1 r1 and `lane/review/AMENDMENT-1.r1.md:27` names the unused driver. The overlays and driver-delta chain supersede these. Its unversioned Gram pointer at line 11 is addressed explicitly by `lane/review/REVIEW-CORRECTIONS.r2.json:9`.
- **Drivers/controls:** current K2 driver references and hashes are r4; r2/r3 references identify failed starts. Gram’s old exploration-control table at `lane/review/GRAM-ENCODING.r2.md:98` retains historical labels, followed by frozen and added-control evidence at lines 108–124. K3 driver/transport references remain prospective.

## T5 — Chronology

Recorded order is consistent except D-MINOR-1:

- Original frozen controls: approximately 19:06, before K2 production.
- K2 certificates: first start 19:31:09; final finish 20:12:37.
- Added matched controls: first receipt 21:24:52; summary 21:25:09.
- New transport controls: 21:38:40–21:38:43.
- K3 driver delta: frozen 21:39:20; first new K3 pipeline reportedly began 21:39:49.

Evidence: `desk-digests/chronology.json:14`, `desk-digests/chronology.json:59`, `desk-digests/chronology.json:89`, `desk-digests/chronology.json:114`, `desk-digests/chronology.json:144`, `lane/evidence/LOG.md:89`.

The transport summary binds `proof_stream.py` at `lane/evidence/gram/transport_controls_r2/summary.json:217`; r4 does not call that module. Its tests therefore support the new K3 transport prospectively. Neither added suite is retroactive preregistration. Gram r2 and REVIEW-CORRECTIONS state the after-K2 chronology correctly. I found no additional false chronology statement in the repaired proof/theorem texts.

## T6 — Parent replay acceptance conditions

For **each** of the 294 `(encoder, i)` instances, the parent must establish:

1. The classfile digest is `898065c8…a8158`; index \(i\) binds to the first token of nonempty line \(i+1\), preserving leading zeros. Decode using pinned `k2_classes.py` (`b49099e4…b891`).
2. Encoder A/B bytes match their full receipt pins. Generate exactly two squares, that decoded L, heavy enabled, sym disabled, and no fixes or additional clauses.
3. The regenerated CNF SHA-256 equals that instance’s receipt `cnf_sha256`. Validate DIMACS counts/literals and exclude malformed `None` or unexpected empty clauses. The exact checked CNF must remain unchanged throughout verification.
4. A parent-controlled, source/binary-bound checker checks a fresh complete proof against those exact CNF bytes. Require solver rc 20, checker rc 0, exact CR-normalized `s VERIFIED`, no conflicting status and no safety stop.
5. Retain parent logs, commands, hashes and per-instance bindings; require exact coverage of both routes over indices 0–146.
6. Validate the parent checker/stream with positive nontrivial UNSAT and negative SAT/invalid-proof controls. Streaming must deliver the proof and EOF without silently substituting an empty or different input.

The original streamed proof bytes need not be reproduced: a fresh valid proof of the identical CNF suffices. Historical solver versions/binaries are not soundness premises. Accepted K1 r3 and the established LS147 coverage remain explicit prerequisites. Producer booleans, logs and desk digests alone do not discharge proof validity.

Scope: I used only read-only inspection and hashing inside the pin, and hand reasoning for the mathematics and clauses. I checked the repaired documents, relevant source passages, encoder/driver/control code, selected underlying receipts/logs, and the supplied mechanical binding/chronology digests. I ran no interpreter, solver, compiler or proof checker; made no writes, network calls or delegations. I did not independently recompute all canonical classes or validate any DRAT stream. Acceptance remains conditional on the parent replay above and establishes K2 only.