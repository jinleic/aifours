# Covering sequences: exact L(12,3) — parent verdict

## Result

**L(12,3) = 36.** A cyclic binary sequence needs at least 36 positions for its length-12 cyclic windows to cover every binary 12-word within Hamming distance 3.

This is an exact finite minimum, not merely a longer search range. The upper-bound witness is already published by CPro1; the contribution is excluding every shorter length. [Frozen contract](../screening/info-2-cover12-r3-contract.json).

The definition is quantified over **all 4096 words**, including both constant words. Windows wrap modulo the actual sequence length, repeatedly when the length is below 12. No monotonicity in sequence length is assumed.

## Proof and exhaustive coverage

1. A radius-3 ball in the 12-cube has 1+12+66+220 = 299 words. A sequence of length L has at most L windows, so L ≤ 13 is impossible: 13·299 = 3887 < 4096.
2. Every length 14 through 35 is exhaustively excluded by three independently written implementations with different enumeration reductions. The published lower bound 34 is unnecessary.
3. The known CPro1 length-36 sequence covers every target. The parent's definition-first checker verifies all 4096 words ([baseline receipt](cover12-3-parent-screen-v1/baseline-parent-result.json)); the independent Codex reviewer reconstructs and verifies the same witness directly.

| Length | Worker unrestricted strings | Worker rotation representatives | Parent light-window candidates | Covering strings found |
|---:|---:|---:|---:|---:|
| 34 | 17,179,869,184 | 505,294,128 | 1,254,096,896 | 0 |
| 35 | 34,359,738,368 | 981,706,832 | 2,508,193,792 | 0 |
| 36 | 68,719,476,736 | 1,908,881,900 | 5,016,387,584 | 432 unrestricted; 12 rotation classes; 38 light-first |

The worker's first implementation enumerates every bit string, checking unions of radius-3 balls in chunks. Its second uses FKM necklaces and target Hamming distances, with rotation minimality, strict ordering, independently computed period, necklace totals and weighted-period totals. All ranges partition the full domains. The parent uses a third complete reduction: a covering string covers the zero target at some weight-≤3 window; rotate that window to position zero, enumerate every such prefix and every suffix, and test every target. Move-to-front orderings only speed rejection; acceptance always completes the target scan.

## Verification

- **Parent actual exhaustive replay:** [source and receipt](cover12-3-parent-exhaustive-v1/parent-result.json), [sweep](cover12-3-parent-exhaustive-v1/sweep-v1/sweep.jsonl). It excludes each length individually, including a redundant check of lengths 1–13. Every checked count equals an independently calculated expected count.
- **Calibration:** the parent reproduces all five exact entries from Chee–Etzion–Ta–Vu Table I: L(9,3)=12, L(10,3)=16, L(11,3)=20, L(9,2)=20 and L(10,2)=38. It confirms no sequence at lengths 21–22 for (11,3), despite existence at 20.
- **Witness checker controls:** eight baseline/boundary/format/digest cases behave as intended, including rejection of the n=1,R=0 sequence `0` because the all-one target is missing ([receipt](cover12-3-parent-checker-controls-v1/parent-result.json)). The public CPro1 verifier omits the all-one target and is not trusted; its length-36 witness is valid under complete checking.
- **Actual found-set binding:** the 38 parent hits pass the independent stdlib witness checker. Their 12 rotation classes equal the worker's classes; all 432 strings are exactly the 36 rotations of those classes. The [supplement](cover12-3-exhaustive-support-v1/manifest.json) binds 1905 files, including original binaries/receipts/found lists and all parent hit receipts; [set-equality receipt](cover12-3-exhaustive-support-v1/class-set-equality.json).
- **Codex CLI `gpt-6.1-sol`: ACCEPT**, no fatal or major defect. The reviewer independently audits all three C sources, reconstructs every worker range/necklace count from 269 jobs, checks all 144 parent run rows, verifies a length-36 witness against the definition, and compares tiny cases with independent Python implementations. It does not rerun the large searches ([review](cover12-3-completeness-codex-review-v1.note.md), [dispositions](cover12-3-review-dispositions.json)).

## Priority, significance and trust limits

The [bounded priority audit](cover12-3-priority-audit.md) found no earlier exact value. Chung–Cooper (2004) list 34–40; Chee–Etzion–Ta–Vu (2025) retain that interval. Rosin's CPro1 result supplies length 36, without an optimality claim. A search miss is not novelty clearance.

This settles one explicitly listed finite table entry. Significance is **modest and specialist**: no new upper-bound construction, asymptotic bound or general covering-sequence theorem. The source authors themselves describe small lower-bound improvements as comparatively accessible.

The exclusion is a conventional computer-assisted exhaustive proof trusting the C compiler, runtime and hardware. It is not a DRAT/LRAT certificate, Lean proof or independent-kernel result. Unchecked allocation/thread/stream error returns in the frozen programs are a disclosed diagnostic limit; the review found no resulting failure in the recorded runs. The missing-supporting-archive finding is resolved by the supplementary snapshot, not by altering reviewed inputs.

**FRONTIER: CORRECTNESS-ACCEPTED — exact finite minimum by three exhaustive implementations and independent completeness review; NOVELTY-UNCLEAR. The frozen info-2 L(12,3) target is met (2026-10-17 PT), with low significance and no broad breakthrough claim.**

No publication, external contact, commit or push was authorized.


**Priority addendum (2026-10-17 15:17:52 PDT, appended; text above unchanged):** a new-surface audit found an earlier public claim of the same result; status is now PRIOR-CLAIM and this is no longer counted as a contract gate. See [cover12-3-priority-addendum-v1.md](cover12-3-priority-addendum-v1.md).
