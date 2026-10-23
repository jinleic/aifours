# PA(19,8,6): two M2 cases closed; 149 remain

Recorded at 2026-10-19T02:16:12-0700.

**CORRECTNESS-ACCEPTED SCOPED PARTIAL.** The new run-003 proofs close ms09 b70 (A2 tag ms09_s00070) and b5 (A2 tag ms09_s00022) at the M2 layer. The lane-original undecided count is **149 = 86 ms06 + 63 ms09**, down from151. This does not settle PA(19,8,6). M1 and the separate M2H views3/5424 and1/5424 are unchanged.

## Exact-input evidence

| Case / placement interval | CNF SHA256 | Retained DRAT bytes | Provenanced replay |
|---|---|---:|---|
| b00070:00000-00024 | `565dd02cf532cb6a58fb70935d8e74fa7bca8e15432ad800c5019eaf5c98ff2b` | 4634811 | normal0, VERIFIED, consumed=filebytes |
| b00005:00200-00299 | `952b8839f7daa66ba499ba0e523696562425cce047b845dbdaef87b8d696a642` | 478666919 | normal0, VERIFIED, consumed=filebytes |
| b00005:00300-00350 | `4ed08d983896dfd5f27925dab5dc656be9374262c646a9c31792ec2cdb7e9196` | 179350362 | normal0, VERIFIED, consumed=filebytes |

[Raw audit](pa19-run003-raw-parent-audit-v1.json), [provenanced-build replay](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/pa19-provenanced-proof-replay-v1/science-results-v1.json), [closure receipt](pa19-run003-case-closure-receipt-v1.json), and [updated frontier](pa19-parent-frontier-v2.json) bind the exact files and receipts.

The parent launched runner v16 `0ef4cfdcf7f0220bdde78829198bea7a8acf603e2678e88eedafe0c04bd3170e`, observed exit0 and all14children settled, verified C1–C7 intended control outcomes, rehashed all three CNFs and proofs, checked every item commit against the clean run summary, and matched exact solver/checker status lines, parsed CNF headers and checker-consumed proof bytes. Exit0 alone is not a science verdict.

The retained proofs were then replayed sequentially using drat-trim `a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37`, compiled earlier from source `d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee` (upstream2e3b2dc0, cc -O2). Positive, satisfiable-foreign-proof and trailing-byte controls first behaved as intended; all three scientific replays exited normally0 with exact VERIFIED and consumed counts. This is **one verifier implementation with two binary builds**, not independent algorithms. The second build has recorded provenance; the original lane111b0405 build does not.

## Coverage

b70's single interval[0,24] equals its25-placement denominator. b5's inherited VALIDATED intervals[0,99],[100,199] plus the new[200,299],[300,350] form a disjoint exact union[0,350], matching351placements. Parent rehashed both inherited receipts and both old/new regenerated lists; list regeneration was byte-identical. Its completeness still rests on the accepted M2 bridge, not merely on the list count.

The old b5[200,299] UNKNOWN remains unchanged. run-001's pre-spawn symlink refusal and run-002's C4 stability-window refusal remain recorded; run-003 used only the approved Cellar-path and280s-span repairs. No old evidence was deleted or reclassified.

## Limits

This is case-level exclusion under the existing independent M2 encoding and complete-case bridge, not unrestricted PA nonexistence, a new design witness, a novelty result, or a Lean proof. The first two b5 intervals still rely on old measured-stream receipts rather than retained proof bytes. Next work: the newly identified inexpensive ms06 direct cases and a structural split before broad placement enumeration.
