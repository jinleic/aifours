# Independent referee findings and resolutions

Date: 2026-10-14. All four recorded invocations used Codex CLI with registry-selected `gpt-6.1-sol`, reasoning effort `max`, read-only sandbox, ephemeral session, no further delegation. Observed identities are in the respective stderr headers. No model response is substituted for a proof.

## First review: correct

- Prompt: `review-prompt.txt`; output: `independent-review.md`; exit/runtime/model receipt: `review-receipt.json`.
- Nine inputs were pinned in `review-inputs.json`. The exact original proof is preserved as `proof-reviewed-original.md`, matching the original `proof.md` hash; other pinned inputs remain unchanged.
- The referee independently counted the full 9/15 certificates, replayed all 23 checker cases in memory, reviewed both exact encodings, and accepted proof Sections1–6. It reported no concrete errors.
- The referee explicitly did not certify unfinished/unpinned target-run logs or the externally attributed global spectrum.

## Second review: correct-with-fixes

- Prompt: `addendum-review-prompt.txt`; output: `addendum-review.md`; exit/runtime/model receipt: `addendum-review-receipt.json`.
- The new fixed-point divisibility and all-multiplier arguments were embedded in the prompt. The local auxiliary note was also read. Its unchanged-at-review text is preserved as `recursion-notes-reviewed-original.md`; unlike the first review, this file was not hash-pinned before invocation. The output itself records the sections and counts reviewed.

| Finding | Resolution |
|---|---|
| The order-five multiplier proof silently writes the infinity-pair block with finite point0 | `proof.md` §8 now uses the actual unique block `{r,u,w}`. It is setwise fixed, so its class is fixed; no normalization is required. |
| “No conclusion” from block-set invariance alone is too broad | `proof.md` §7 explicitly says this divisibility conclusion is not established from block-set invariance alone. |
| Fixed-subsystem bound needs w≥3 if degenerate STS(1)s are admitted | Added w≥3 to `sources/recursion-notes.md` §3. Uses at15 and21 are unchanged. |
| Numerical class sizes do not supply an actual resolution | The order87 formulation now explicitly assigns every matching edge and triangle exactly once, requires the remaining-stem edge to avoid the HHA outside point, and requires all other triples to partition the stated complement. |

The referee accepted the incidence identity `2cf=f²−2f+v`, the CRT/involution enumeration, all stated block inventories, and the sufficiency of both auxiliary packages. Their **existence remains unproved**. The corrections are explicit hypotheses/normalization clarifications; none weakens an acceptance check or changes a solver status.

## Extended review: correct-with-fixes

- Prompt/output/receipt: `extended-review-prompt.txt`, `extended-review.md`, `extended-review-receipt.json`. The37-entry input manifest is `extended-review-inputs.json`, with immutable copies under `extended-review-snapshot/`.
- The referee found **no active encoding unsoundness**. It accepted the block-set-only scalar exclusion, affine-normalizer classification, classical reverse-STS strength, C19/C29 AP obstructions, signed reflection/F55 packages, staged CNF, joint modular model, and C19 class/base symmetry breaking.
- It independently recounted all six involution fixed-orbit counts, the C19 AP inventory, and C29 incidence signatures, and checked all supplied small certificate contents. It also accepted README Status(a)–(c), including the uncertified-open label and universal-versus-finite distinction.
- **Sole finding:** the snapshot omitted seven files referenced by the replay/embedding receipts: frozen matching inputs, two blocked candidates, original CNF-hash ledger entries, and the Denniston certificate.
- **Applied fix:** those seven inputs were copied into the snapshot and separately hash-bound in `extended-review-supplement.json`; no original reviewed file/hash was changed. This worker then regenerated both CNFs using the completed snapshot, including the two-candidate-blocked15-point instance. Both matched the recorded hashes; see `extended-review-supplement-replay.json`.
- The referee did not execute those two CNF replays or the modular embedding; they remain explicitly worker-exercised checks. Their reproducibility gap is resolved, not disguised as independent execution.
- Current review reproduction uses `python3 work/run_review.py --phase initial`, `--phase addendum`, `--phase extended`, or `--phase completion`. Older invocation spelling in preserved historical tool logs is not rewritten.

## Concrete-completion review: correct-with-fixes

- Prompt/output/receipt: `completion-review-prompt.txt`, `completion-review.md`, `completion-review-receipt.json`; all35 input hashes matched.
- Independent counting confirmed the complete partial certificate:17 systems,28 classes each,19 triples per class, every pair once per system, and9,044 globally distinct blocks. The plain text and frozen packing JSON agree exactly, and all17 block sets and chosen resolutions are invariant under all19 translations.
- The referee rejected eight in-memory corruptions with the actual partial checker. It independently confirmed native dimensions, all20,216 offset translations, both incidences of all27 AP orbits, modular/native correspondence, the sole base/translation anchor, and all17 known resolutions satisfying the actual resolution-constructor constraints.
- **Operational finding:** early cancellation could wait for the original native-call deadline before escalating. This was demonstrated only with a fake child, not a real process. The fix starts grace when cancellation occurs, retains the handle until reaping, removes SIGKILL escalation, and records an unresponsive child's PID/cleanup-incomplete state if SIGTERM is insufficient.
- Six corrected virtual-clock/fake-child cases passed: `c19-paircover-lifecycle-unit.json` and independently exercised `c19-paircover-lifecycle-parent.json`. They launched zero real children and made zero SIGKILL calls. The already-running searches keep their original source snapshots and unchanged mathematical instances; the lifecycle correction applies to the current reproduction controller.
- **Replay limitation documented:** matching reconstructed model bytes does not authenticate the original source code. The recorded source copies/hashes remain available for audit, but replay does not falsely claim to verify them.
- The60-second resolution diagnostic remains UNKNOWN, despite its driver's assertion expecting a positive result. The supplied known resolution satisfies every saved model constraint; no failed search was rerun merely to confirm it.

## Remaining trust boundary

- Positive finite claims are backed by fully expanded certificates, the independent checker, and independent referee counting.
- Complete restricted-obstruction proofs are in `proof.md`, `sources/extended-group-analysis.md`, and `sources/c19-search-notes.md`; the finite arithmetic has executable checks and independent referee recounts.
- CP-SAT INFEASIBLE and native SAT-solver UNSAT are solver reports unless separately supported by a written proof; no general DRAT/LRAT archive is claimed. UNKNOWN is not UNSAT. The new proof excludes scalar block-set symmetry independently of the original bounded solver outcomes.
- No proof or certificate of LKTS(57), LKTS(87), or their unrestricted nonexistence is claimed.
