# Optimal (v,5,1) and (v,6,1) CPCW codes for the eight lengths open in 2026: parent verdict

## Result

The parent lists every result below with explicit codewords in Z_v. An optimal (v,k,1) CPCW code has s = ⌊(v−1)/(k(k−1))⌋ k-subsets with all ordered differences nonzero and distinct, which is equivalent to auto- and cross-correlation at most 1 (Baicheva–Topalova, Axioms 15(1):35, Definition 1 and p.2). Each of the following exists:

| v | k | s | Codewords | Uncovered nonzero differences | Certificate SHA-256 |
|---|---|---|---|---|---|
| 122 | 6 | 4 | {0,1,3,21,59,111} {0,4,10,27,40,75} {0,5,34,42,67,83} {0,7,22,31,50,76} | 61 | `872912e9…51bc` |
| 123 | 6 | 4 | {0,1,3,7,84,99} {0,5,19,56,74,94} {0,8,21,30,53,65} {0,10,26,62,73,90} | 41, 82 | `d499ac51…5a83` |
| 124 | 6 | 4 | {0,1,3,27,33,43} {0,4,25,63,70,78} {0,5,18,52,93,107} {0,9,29,73,85,96} | 19, 62, 105 | `5fefb1f5…e225` |
| 143 | 5 | 7 | see pinned file | 39, 104 | `eeeada3d…06e8` |
| 144 | 5 | 7 | see pinned file | 30, 72, 114 | `b55797c7…da2c` |
| 146 | 5 | 7 | see pinned file | 11, 17, 73, 129, 135 | `52d69e01…a830` |
| 162 | 5 | 8 | see pinned file | 81 | `7e26a43e…638a` |
| 167 | 5 | 8 | see pinned file | 24, 25, 79, 88, 142, 143 | `4a46416e…2bda` |

These are exactly the eight lengths the source names as open for k=5 and k=6, apart from (126,6,1), which earlier work already gives ([contract](../screening/info-2-cpcw-optimal-contract.json)). Pinned inputs are `cpcwV-parent-inputs-v1/cpcw_V_K.txt`.

Open-status quote, p.5: "In particular, we have not found examples of optimal (v, 5, 1) CPCW codes for v = 143, 144, 146, 162, and 167, and of optimal (v, 6, 1) CPCW codes for v = 122, 123, 124, and 126." The same page adds that for these lengths "the question of the existence of such codes remains open".

Equivalent objects:
- optimal (v,k,1) optical orthogonal codes;
- cyclic difference packings;
- strictly cyclic optimal partial 2-designs;
- for v = 122, 123 and 162, regular codes, i.e. cyclic relative difference families over the order-2, 3 and 2 subgroups.

## Verification

| Gate | Result | Artifact |
|---|---|---|
| Parent definition-first checker | All 8 VALID. It checks every cyclic auto/cross shift directly, all ordered differences, and the complete developed packing: distinct s·v blocks, no pair covered twice, and missing pairs exactly matching the leave | [checker](check_cpcw_independent.py), `cpcwV-parent-check-v1.json` |
| Parent controls | 12 published optimal codes (k=5 and k=6) PASS; 8 intended-reason mutations on v=122 rejected with the intended reason | [positive](cpcw-parent-controls-v1/positive-result.json), [negative](cpcw-parent-controls-v1/negative-result.json) |
| Parent source rebuild and replay | All eight producers recompiled from pinned source with `cc -O3 -march=native` and replayed. The k=6 runs are deterministic exact-cover extractions; the k=5 runs are seed-1 tabu searches. Every regenerated certificate is byte-identical to its pin | [122](cpcw122-parent-replay-v1/parent-result.json), [123/124](cpcw123-124-parent-replay-v1/parent-result.json), [k=5](cpcw-k5-parent-replay-v1/parent-result.json) |
| Third implementation (prompt-only) | All 8 VALID under `python` and `python -O`. It also passes the 12 positives and rejects all 8 mutations, each with an invariant-specific reason. No asserts and a single file read | [receipt](cpcw-claude-verifier-v1/parent-run-result.json) |
| Codex cross-vendor own verifier | RESULT: ALL VALID: 7,090 auto- and 20,519 cross-correlation shift checks; 267 in-memory corruption controls, each rejected for the intended reason | [final](cpcw-codex-verify-v1/final.md) |
| Worker verifier | Prep verifier (`85f93e8b…`) ACCEPT for all 8; 165 worker mutation checks | lane `RESULTS.md` (`0b32f04f…0413`) |
| Lean formalization | PASS. The parent wrote an unfolded statement for each of the 8 frozen cases (existence of the code with the stated number of words, plus the universal upper bound), rebuilt the worker modules, and ran a fresh-kernel replay. Each theorem uses only `propext`, `Classical.choice` and `Quot.sound`. Both negative controls, `FullDifferenceFamily` and `WrongNumberOfWords`, fail to typecheck as intended. The run used one Lean toolchain, so this is not an independent kernel or Comparator check, and the 163 addendum is not formalized | [driver](cpcw_parent_kernel_replay.py), [receipt](cpcw-kernel-parent-replay-v1/parent-result.json), worker `cpcw-kernel-worker-v1/` |

Provenance limit: the parent did not capture the v=122 discovery source or binary at launch. The worker reconstructed that source, `k6cls_a_v1.c`, and SHA-matched it to its launch log. The parent replays use the frozen extraction source v2 and the frozen tabu source.

## Priority and significance

A bounded audit ([report](cpcw-priority-audit.md)) found no earlier construction of any of the eight, and no theorem that implies one. It checked:
- Baicheva–Topalova's later MEM 2026 and Axioms 15(9):679;
- Hetman–Baicheva–Topalova;
- 1-rotational and Steiner-system routes;
- cyclic relative difference family theorems for k=5 and k=6;
- nonexistence theorems for v = k(k−1)t+2.

The same audit calibrates the source list: 126 was already known in 2024 and 125 by April 2025, so the 2026 open list is not a novelty certificate. No full texts on cyclotomic relative difference families for k=6 or Galois-ring constructions over Z_81 were read.

Significance: modest. These are finite instances that fill the gaps named in one 2026 paper.
- (122,6,1) is the most notable, because the shorter lengths of the same 30t+2 form (32, 62 and 92) are proven nonexistent.
- The k=5 codes took 0.02–1.3 s of tabu search, which suggests those gaps reflected the source's search method rather than real hardness [INFERENCE].

The source's own Tables 1, 3 and A1 also leave (163,5,1) unresolved, although its text list omits it. Under the separate [table-attested addendum](../screening/info-2-cpcw163-addendum-contract.json), a code now exists for this length as well:

- **(163,5,1), s=8:** {0,12,17,75,107} {0,11,85,135,139} {0,3,9,19,34} {0,82,84,125,143} {0,21,65,117,118} {0,13,40,70,112} {0,23,49,71,126} {0,29,62,76,156}.
- Uncovered differences: 8 and 155. SHA-256 `27acd320…0bc`.
- Verification: parent checker VALID; seed-1 parent replay byte-identical (0.36 s); third checker VALID under `python` and `python -O` ([check](cpcw163-parent-check-v1.json), [replay](cpcw163-parent-replay-v1/parent-result.json)).
- Its open status rests on the tables only and is labelled TABLE-ATTESTED.

**FRONTIER:** CORRECTNESS-ACCEPTED for all eight finite existence claims, with four independent verification routes plus parent byte-exact replays. NOVELTY-UNCLEAR. No earlier equivalent was located in the bounded screen. **The frozen info-2 CPCW target gate is met** (2026-10-17 PT): every case in the frozen list is decided by an explicit verified witness. No classification or nonexistence claim is made.


**Priority addendum (2026-10-17 15:17:52 PDT, appended; text above unchanged):** a new-surface audit found an earlier public claim of the same result; status is now PRIOR-CLAIM and this is no longer counted as a contract gate. See [cpcw-priority-addendum-v1.md](cpcw-priority-addendum-v1.md).
