# MOQLS(8) K5: root-level coverage and 122 proof replays — parent verdict

## Result and scope

**The declared K5 base plus each of 122 root cubes is UNSAT, with parent-checked DRAT certificates.** The frozen v003 ledger is an exhaustive, disjoint partition into 128 cubes. Six roots remain UNKNOWN: **c016, c032, c048, c064, c080, c096**. Consequently **K5 is not excluded**, K4 is not excluded, and Ball–Simoens Problem 16 at n = 8 is not solved by this record.

K5 means the reduced five-non-classical-square branch of the reviewed reduction, not every unreduced set with five non-classical members. The row-0 P4 restriction is lossless in that reduced branch; reduction can instead lead to K4. The [soundness reviews](moqls8-k4k5-codex-review-v1.note.md) and [actual-CNF binding](moqls8-encoder-parent-integration-v1.json) are imports for the mathematical interpretation of this Boolean formula.

## Frozen input and complete root cover

Base `GA5L_K5_sb2.cnf`: SHA-256 `6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b`, 509,915 variables, 5,740,230 clauses, 137,664,569 bytes. The actual encoder output is independently bound to its declared clause families (C1–C8 and C12; C9 list meanings only).

Ledger v003: SHA `b9b3fc67fe5abdf6be197b7cb642226bc1c5f344348edb068b6388c02bc8b14b`; predecessor chain v001 → v002 → v003 preserved. [Independent root-cover audit](moqls8-k5-root-cover-audit-v1.md): ROOT-COVER-HOLDS, no defects found in the frozen coverage/provenance mapping. Root IDs c000..c127 and indices 0..127 are unique; at literal position k, the sign is positive iff bit k of the index is one, for V1 = [57,106,155,204,253,302,351]. Thus all 128 sign assignments occur exactly once. There is no depth-two refinement in v003. The audit compares declared mappings/hashes; fresh cryptographic checks are in the replay below.

The six UNKNOWN roots have only worker-root evidence after roughly 900-second timeouts; their partial proof files are not certificates. Old positive root records were downgraded to worker evidence, not silently promoted.

## Parent-delegated proof replay

[Final receipt](moqls8-k5-root-parent-replay-v1/final-a1/FINAL.json), SHA `88cac421…2905`; [runner and report](moqls8-k5-root-parent-replay-v1/WORKER-REPORT.md). **122 planned / 122 receipts / 122 PASS / zero problems.** The six UNKNOWN roots were neither replayed nor accepted.

Every PASS requires:

- Metadata pinned before replay: v003 ledger, strict receipts, retained-proof manifest `65f6e0dd…c3b5e`, sidecar, old receipts, and the exact base. The base also passed a complete canonical-clause structural check.
- Exact leaf CNF: header clause count 5,740,237, unchanged base body, then the root's seven ledger literals as units; SHA equals the strict leaf-CNF hash.
- Each retained compressed proof has the manifest's SHA and size; total 444,419,127 bytes. In-process Python `compression.zstd` decompression finishes cleanly, and both produced and delivered proof bytes match the strict stream SHA/length.
- Parent-pinned drat-trim SHA `a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37`, native command `drat-trim /dev/fd/N -i -t 1500`, exact parsed CNF counts and proof-byte count, exit 0 with exactly `s VERIFIED` after carriage-return stripping; no TIMEOUT, fatal/unclassified warning, feed error or guard trip.

102 roots refute by unit propagation on base plus units alone. The other 20 require backward DRAT checking (largest: c040). All retained proof streams were fully read and bound even when unit propagation sufficed. The pipeline uses two processes (Python feeder and drat-trim), no helper subprocess and no `/tmp`; corpus peak sampled aggregate RSS 1,246,576,640 bytes, checker time sum 607.32 seconds, no corpus cap trips. New replay data: about 2.39 MB.

**20/20 scientific controls behaved as intended:** valid small and real proofs accepted; bogus empty-clause proofs rejected on SAT and non-UP UNSAT instances; compressed/raw mutations, wrong root/proof mapping and truncation rejected; a valid proof with an unread bad tail still returned UNKNOWN despite drat-trim printing VERIFIED; deliberately forced memory/wall/native TIMEOUT controls returned UNKNOWN; malformed base clauses rejected. A recompressed mutation that drat-trim itself accepted was rejected by the binding predicate. These controls establish that native VERIFIED alone is not the replay acceptance criterion.

## Remaining obligations

- Resolve the six UNKNOWN roots under a complete versioned refinement ledger, with every terminal leaf retained as CERTIFIED, UNKNOWN or unstarted.
- Independently re-check every new terminal proof. Newly streamed non-retained depth-two/K4 proofs are allowed under the dated lane approval, but parent acceptance requires independent re-solving and proof checking against the exact leaf CNF; receipts alone do not suffice.
- K4's separate six-cube pilot and full cover remain outside this verdict.

Computer-assisted; not Lean-checked. No novelty or whole-problem gate claim. C10 is accepted only for the frozen v003 root cover; C11 is accepted only for the 122 actually replayed roots.

**FRONTIER: CORRECTNESS-ACCEPTED (partial root exclusions); K4/K5 and the n = 8 gate remain open.**
