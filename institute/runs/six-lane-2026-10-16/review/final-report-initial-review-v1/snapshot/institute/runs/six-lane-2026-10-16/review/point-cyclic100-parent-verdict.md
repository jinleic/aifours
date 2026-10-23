# Point-cyclic resolution of a 2-(100,4,1) design: parent verdict

## Result and status

**An explicit cyclic 2-(100,4,1) design has a point-cyclic resolution.** The pinned certificate gives 825 distinct blocks on Z100 and 33 parallel classes of 25 blocks. Every unordered pair lies in exactly one block. Each class partitions Z100; the classes partition the block set. The map x↦x+1 mod100 preserves both the block set and the set of classes and is one100-cycle on points.

This matches Topalova–Zhelezova Definitions2–5 and the isomorphism convention after Definition3 ([parent-read excerpts](point-cyclic88-primary-excerpts.txt), [definitions addendum](point-cyclic88-primary-definitions-addendum.txt)). Class orbits have lengths25,4,4; the block orbits have lengths25 and100×8.

- [Certificate](point-cyclic100-parent-inputs-v1/pc100_t2.cert): SHA256 `971f722460020f5a572b4f17f1cffe249488b8de079badbfa0184b9a79b4f7c1`.
- [Compact seed](point-cyclic100-parent-inputs-v1/pc100_t2.seed): SHA256 `ac727835e2f15075e0697206d81482b634ed76c5f7ff000adc58bef43b256245`.
- [Frozen contract](../screening/info-2-point-cyclic100-contract.json): **DERIVED-OPEN**. The source explicitly names88, not100, as its smallest undetermined case. No claim that100 was explicitly named open, or is provably the next open order, is made.

## Verification evidence

| Check | Observed result | Evidence |
|---|---|---|
| Parent definition-first checker | VALID: all825 distinct4-subsets, all4,950 pairs exactly once, all33 point partitions, block/class partition, and both +1 automorphism conditions | [checker](check_point_cyclic_resolution_independent.py), [candidate receipt](point-cyclic100-parent-check-v1/candidate.json) |
| Parent semantic controls | Six lane-transcribed published52-point examples and the published64-point example pass. Eight substantive candidate mutations reject for their intended reason, including a global0↔1 point relabelling that preserves the design/resolution but breaks the specified +1 automorphism | [positives](point-cyclic100-parent-check-v1/positive-controls/summary.json), [guarded v2 mutations](point-cyclic100-parent-check-v2/parent-result.json) |
| Class-action-specific negative control | In the64-point control, exchange four blocks between classes0 and12 whose unions coincide. The cyclic block set and all class partitions survive; +1 no longer maps classes to classes. The parent checker rejects exactly that condition | [receipt](point-cyclic100-parent-check-v1/class-branch-control/result.json) |
| Codex own verifier | Independently written in-memory code: VALID, with the exact counts, group-action checks, independent seed expansion and seven structural corruptions. It accessed only the pinned inputs, not lane code | [review](point-cyclic100-codex-verify-v1.note.md), [invocation receipt](point-cyclic100-codex-verify-v1.receipt.json) |
| Prompt-only third implementation | Claude wrote a checker from definitions/format only, without tools. Parent-executed: candidate passes under ordinary and optimized Python; seven positive controls pass; eight candidate mutations, the64-point class-action mutation, wrong expected order and wrong SHA reject. Twenty total runs, zero assert statements | [checker and receipt](point-cyclic100-claude-verifier-v1/parent-run-result.json) |
| Parent seed expansion | Parent independently implements the T2 expansion; the33 generated classes match, including byte-exact canonical certificate serialization. The96 directed differences of the eight full base blocks are exactly Z100 minus{0,25,50,75}, once each | [guarded v2 receipt](point-cyclic100-parent-check-v2/parent-result.json), [driver](point_cyclic100_parent_check.py) |
| Parent rebuilt discovery producer | Fresh compilation of the pinned C source; the stated seed/arguments regenerate the compact witness in22.5s. The pinned expander then regenerates the exact certificate, which again passes the parent definition checker | [receipt](point-cyclic100-producer-parent-replay-v1/parent-result.json), [driver](candidate_producer_parent_replay.py) |
| Lean 4.34.1 existence proof | PASS. The parent bound the worker's `cert100` literal to the pinned certificate (33 classes × 25 blocks, in raw order), rebuilt four pinned modules and proved its own unfolded statements: a 2-(100,4,1) design on `Fin 100` with a resolution and a permutation that is one cycle moving every point, preserving the block set and mapping every class onto a class; the same with the permutation named `PC100.shift 100`, and `shift 100 x = x + 1`. Fresh `leanchecker` 118 s; only standard axioms; four statement mutations fail. The first parent attempt failed only on the driver's wrong axiom expectation for `shift_is_succ` and is preserved. One toolchain only | [driver](point_cyclic100_parent_kernel_replay.py), [receipt](point-cyclic100-kernel-parent-replay-v2/parent-result.json), [superseded attempt](point-cyclic100-kernel-parent-replay-v1/parent-result.json), worker `information-science/evidence/six-lane-20261016/point-cyclic100/lean-kernel/` |

These checks establish the finite existence claim without assuming a type classification, a solver result, or any exhaustive-search conclusion. Parser/parameter checks are separate from substantive corruption controls. The52/64 data are lane transcriptions of published examples: the parent verified the resulting designs, not their textual fidelity to every published table.

### Replay-driver guard correction

The initial parent aggregation driver recorded the lane expander's return code and output SHA but did not require them to succeed before its overall PASS. A real exit7/no-output mutation reproduced that fail-open status. The fixed driver now rejects both a failed expander and an exit0 expander producing wrong bytes; the real pinned positive replay and all eight structural mutations pass ([before/after evidence](point-cyclic100-replay-guard-mutation-v1/result.json)). The original positive expander actually exited0 and reproduced the correct bytes, so this does not invalidate the certificate or the earlier positive replay. The independently rebuilt discovery-producer replay already gated both conditions. Original v1 source/receipts are preserved; the guarded receipt is v2.


## Construction and separate structural claims

Let H={0,25,50,75}. The seed contains six blocks X_i and two blocks Y_j. A base parallel class is {H}∪{X_i+25t:1≤i≤6,0≤t≤3}; its25 translates supply25 classes. For each Y_j, the class {Y_j+4t:0≤t≤24} and its four translates supply the other eight classes. The independent expansion and direct checker verify this entire construction.

The worker's stronger reduction claims every such resolution must be type T2 (ruling out T1 and T3) and is equivalent to eight base blocks satisfying (S1)–(S3). That is **not required for existence**. A same-vendor Claude hostile review found no mathematical error (ACCEPT-WITH-FIXES); its presentation fixes are applied in a [parent revision](pc100-mcdsqs38-parent-inputs-r2/pc100-REDUCTION.md) with [dispositions](pc100-mcdsqs38-review-dispositions.json). No cross-vendor review of this classification has been run, so it is recorded as a reviewed structural lemma, not a promoted result.

## Priority and significance

The [bounded priority audit](point-cyclic100-priority-audit.md) found no earlier construction or impossibility result in accessible sources. It checked the prime-product families, author-preprint necessary conditions/recursions, and forward citations. None whose hypotheses could be checked supplies the100-point construction. Significant access holes remain: the Handbook, Lam–Miao1999 and2001, Kageyama–Miao1996 and other blocked bodies. A suitable older cyclic semiframe could already imply this result.

**Significance:** a modest specialist finite construction outside the existence families checked, not an established new method or priority claim. General resolvability, point-cyclic resolvability and unrelated uses of “cyclically resolvable” must not be conflated.

**FRONTIER:** CORRECTNESS-ACCEPTED for the finite existence claim (three independent checkers, byte-exact seed and producer replays, parent-replayed Lean proof). **NOVELTY-UNCLEAR; DERIVED-OPEN.** This result is **not counted as a new explicitly-named-open-target breakthrough gate**, because the source names 88, not 100. No publication, external contact or human peer review has taken place.
