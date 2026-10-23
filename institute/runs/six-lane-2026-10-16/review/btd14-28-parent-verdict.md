# Balanced ternary design BTD(14,28;8,3,14;7,6): parent verdict

## Result

**BTD(14,28;8,3,14;7,6) exists.** An explicit 14 × 28 matrix over {0,1,2} has exactly eight entries 1 and three entries 2 in every row, column sums 7, and inner product 6 between any two distinct rows.

Witness: [btd14-28-witness-v1.btd](btd14-28-parent-inputs-v1/btd14-28-witness-v1.btd), 805 bytes, SHA-256 `18cadb923274cbad3f35112d26edf00889971f76d8a0cec28540dcb9d2e40bb1`. It has 27 distinct columns (columns 24 and 26, 0-based, coincide; repeated blocks are allowed by the [frozen contract](../screening/info-2-btd14-28-contract.json)); column types (ones, twos) are (3,2) × 18, (5,1) × 6 and (7,0) × 4. It is invariant under one order-3 permutation of rows and columns (rows in four 3-cycles with two fixed; columns in eight 3-cycles with four fixed), which is how it was found: kissat solved the restricted Z3-r4-c8 invariant model in about 15 s.

Status of the instance: Billington–Robinson class #234; Kunkle–Sarvate's 1996 CRC Handbook table lists it as entry #121 with no known design; Rosin (arXiv:2501.17725v1, Table 1) lists "(14,28;8,3,14;7,6)?" among the Handbook's smallest open BTDs with blank Greig and CPro1 cells; Rosin's May 2025 follow-up does not solve it. This is an **explicitly listed open finite instance**.

## Verification

| Evidence | Result |
|---|---|
| Parent definition-first checker (stdlib, strict format, every row composition, column sum and all 91 row pairs) | **VALID** ([checker](btd14-28-parent-inputs-v1/check_btd_parent.py), [receipt](btd14-28-parent-inputs-v1/parent-check-v1.json)) |
| Parent controls | 13/13 PASS: positives (small BTD(3,6;2,1,4;2,1), witness, row and column permutations) and intended-reason rejections (row composition, inner product via a sum-preserving 2 × 2 switch, column sum, header, final LF, alphabet, extra row, CRLF, SHA) ([receipt](btd14-28-parent-inputs-v1/controls-result.json)) |
| Codex CLI `gpt-6.1-sol`, own in-memory verifier written before seeing any checker | **RESULT: VALID**; 14 row, 28 column and 91 pair checks; four corruption controls rejected for the intended reasons ([note](btd14-28-codex-verifier-v1.note.md)) |
| Claude CLI `claude-opus-5-5`, prompt-only checker (definition and format only), executed by the parent | 32/32 runs as expected under `python3 -B` and `python3 -O -B`: witness VALID; wrong SHA and wrong parameters rejected; all 13 control fixtures accepted or rejected with the mapped intended reason ([checker](btd14-28-claude-checker-v1/checker.py), [receipt](btd14-28-claude-checker-v1/result.json)) |
| Parent producer replay | regenerated Z3-r4-c8 CNF byte-identical; kissat SAT; parent-written decoder gives a VALID matrix byte-identical to the witness; witness invariant under the declared order-3 permutation pair ([receipt](btd14-28-parent-inputs-v1/producer-replay-result.json)) |

Validity rests only on the explicit matrix and the three independent checkers; the symmetry model and solver are explanation and reproducibility, not proof.

## Priority and significance

A bounded scout screen ([report](btd14-28-priority-screen-v1.md)) read the 1996 Handbook table (author copy: entry #121, "none" known), Kunkle–Sarvate 1996, the Kaski–Östergård data page (row empty), both Rosin papers, the CPro1 repository at HEAD (no 14-28 result file), Dinitz's update pages, OpenAlex/DataCite forward citations and zbMATH; it found no published construction or nonexistence proof. Not read: the 2006 Handbook chapter VI.2 text, the body of Greig's 2003 chapter and Greig's unpublished updated table, so priority is **not** established (risk low to moderate). A search miss is not novelty.

**Significance: modest specialist.** Together with the parent-verified nonexistence of BTD(12,15;6,2,10;8,6), BTD(14,18;7,1,9;7,4) and BTD(12,20;4,3,10;6,4), all four Handbook BTD instances that Rosin's 2025 tables still list as open are now decided in this run (three do not exist, this one exists).

## Status

**FRONTIER: VERIFIED-WITNESS — the frozen info-2 target BTD(14,28;8,3,14;7,6) is met (existence), 2026-10-17 PT; NOVELTY-UNCLEAR.**

Process deviations of the producing lane: five concurrent processes from 12:01:13 to 12:04:42 PDT (shell-loop calibration; cap is four); the local-search calibration failed and never ran on the target. No commit, push, publication or external contact was authorized.
