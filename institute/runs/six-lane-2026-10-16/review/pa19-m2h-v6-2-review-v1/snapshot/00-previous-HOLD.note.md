| Scope | Verdict |
|---|---|
| Supervisor v4 / v6→v6_1 transport | **HOLD** |
| M2H native admission | **HOLD** |

All 35 snapshot files match the supplied SHA-256 hashes and byte counts. Findings below use your SOURCE labels and physical file line numbers. No code or controls were executed.

1. **MAJOR — the re-poll window can turn a newly arriving stop into clean completion.**  
   [SOURCE02:358](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-m2h-v6_1-supervisor-review-v1/snapshot/02-supervise_pa19_v4.py:358), lines 358–362 and 391–392: the added loop checks neither the signal flag nor wall/RSS/floor conditions. SIGTERM/SIGINT merely sets the supervisor’s local flag; during re-poll it can be swallowed, followed by rc0 and `completed_cleanly=True`. Restoring the outer handler does not replay that cancellation. The final sample predates this window.

   **Repair:** check cancellation, elapsed wall time and applicable safety conditions throughout the wait, while the leader remains unreaped. Any detected trip must remain nonclean. Preserve the final checks and owned-child cleanup; never introduce `killpg` against an already reaped, reusable PGID. Bound sleeps by remaining time and recheck before polling: the current loop can poll after five seconds—SOURCE05:87 reports **5.011 s**.

2. **BLOCKER — M2H inventory can qualify historical, unmeasured evidence.**  
   [SOURCE12:99](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-m2h-v6_1-supervisor-review-v1/snapshot/12-run_m2h_v6_1.py:99) delegates to `E.inspect`; SOURCE18:117–121 permits historical records without `pipeline_schema` to become `QUALIFIED`. SOURCE13:31 then counts that state. Thus an eligible historical staged receipt, wrapped in otherwise matching new pin/commit metadata, can bypass every measured v6_1 supervisor/feed/replay check. Formula regeneration during final inventory does not close this transport loophole.

   **Repair:** make M2H inspection require the measured v6_1 schema explicitly. Also bind the primary record’s contract SHA, pre-child pin SHA/path, runner, coverage flag, historical reference, and split list/denominator to the contract and commit. Validate the pin’s supervisor SHA. SOURCE19:297–313 already illustrates stronger binding checks; historical fallback must remain unavailable to M2H final qualification.

3. **BLOCKER — the requested clocks are not enforced by this source.**  
   [SOURCE12:120](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-m2h-v6_1-supervisor-review-v1/snapshot/12-run_m2h_v6_1.py:120) uses **18:31:43−07:00**, not the requested native end **17:57**. There is no encoded **17:20** admission cutoff or supplied evidence of STOP-K1 installation at that time. SOURCE14:246–255 checks STOP markers before admission; it does not monitor an already running native process. `Capacity.supervise` also uses a fixed 2400-second wall allowance at SOURCE14:307.

   **Repair:** freeze both absolute clocks in the reviewed policy, reject admissions after 17:20 independently of marker timing, and cap running-group budgets against 17:57 with cleanup allowance. Preserve token ownership and quarantine if cleanup remains uncertain. STOP-K1 must continue refusing later worker/solver/checker admissions once present.

4. **MAJOR — historical split receipt identity is insufficiently checked.**  
   [SOURCE11:69](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-m2h-v6_1-supervisor-review-v1/snapshot/11-freeze_m2h_v6_1.py:69), lines 69–78: split selection checks filename, three UNSAT fields and encoder, but does not check the receipt’s multiset, B index or exact interval. SOURCE12:65–73 subsequently checks receipt hashes and partition shape without parsing those identity fields or checking that each contract CNF expectation actually equals the referenced receipt’s fields.

   **Repair:** validate receipt identity, exact integer interval, CNF SHA/positive byte count and historical native limit against each item. Bind the extension list’s source/index to the selected skeleton and require a positive, consistent complete denominator. Validate case/ID uniqueness and declared counts. Handle historical revisions explicitly; revisions 5/9 must not be forced through the unrelated 11–15 staged parser.

5. **MAJOR — binding refusal contradicts the documented unattempted/no-HALT policy.**  
   SOURCE12:160–161 raises `LookupError` on formula mismatch. SOURCE16:153–157 catches it, sets `INVALID`/`halt_production=True`, and persists `m2k3-INTEGRITY.flag`. SOURCE12:174–176 then archives the claim as a pre-pin construction/binding refusal. No native process need have started, yet production remains persistently vetoed.

   **Repair:** introduce an explicit pre-pin binding-refusal outcome that records the mismatch, proves no pin/job/group started, ends the chunk and retires only authorized unattempted metadata. Keep native integrity and safety failures persistent. Do not automatically clear flags already created.

6. **MAJOR for any M6/M9 resumption — namespace renaming is not attempt continuity.**  
   SOURCE24:29–32 gives M6 new output/claim names; its freezer at lines 45–59 considers original receipts, ignoring existing measured v6 attempts. SOURCE19:42–52 and SOURCE20:83–96 similarly use the new M9 namespace. A newly frozen contract could therefore make previously attempted inputs eligible again.

   **Repair before resumption:** freeze and review a version-independent attempt/disposition mapping, including M6 **b74/b151/b182/b201/b295** and M9 **b5 0–299**. Preserve old contracts, records and UNKNOWN outcomes unchanged. SOURCE00:313 correctly leaves this unresolved; M6/M9 must remain parked.

The transport delta itself matches its stated scope: SOURCE01 agrees with the independently compared v3/v4 files; SOURCE06/07 show only the supervisor pin, contract source entry and v8-harness label/documentation changes after version normalization. The eight other production bodies have rename-only deltas. Versioned schemas/source checks reject old contracts rather than silently adopting v4. This does **not** resolve finding 6.

The existing controls mean exactly the following:

| Case | Meaning supported by source and supplied receipt |
|---|---|
| A | v3, injected first poll None: unclean, rc None, no trip, one poll. |
| B | v4, same injection: subsequent real poll observes rc0 after 15 ms; clean. |
| C | Every poll bypasses waitpid: unclean rc None after 350 polls/5.011 s; control later waits successfully. |
| D | Delayed observation of rc3 remains unclean. |
| E | Unmodified first poll observes rc0; normal clean path. |
| G/H | Existing wall trip in v4/v3: one poll, no re-poll, unclean; control later observes termination by SIGTERM. |

SOURCE04:50–62 confirms an instrumented **Popen subclass**, retaining the actual child object and suppressing waitpid in injected polls. This recreates the **record signature**, not the kernel race or its proposed cause. These seven cases do not test events arriving during re-poll, nor all RSS/floor/uncertain/signal/quarantine paths.

M2H’s construction route is otherwise faithful to its stated purpose. SOURCE12:104–114 calls the original `build_v2` or `build_partbatch`, and lines 153–161 compare regenerated SHA/bytes before pinning. Contract/source/supervisor/skeleton/historical hashes are checked before owner construction; binaries are checked through admission gates, and the worker rechecks sources, recipe inputs and reconstructed CNF. The measured branch requires exact successful CNF deliveries to both native programs, completed verdict collectors, matching proof replay, clean supervision and explicit owned-child reaping.

The manifest counts independently match:

- **5,393 direct + 187 intervals = 5,580 items**, covering 5,424 cases.
- All 31 split cases are in ms01; their listed intervals form contiguous B100 partitions ending at their declared denominators. No split case also has a direct item.
- **82 exclusions:** 80 without historical checked-UNSAT coverage, plus incomplete splits **ms06_b00068/b00073**.
- Only A2 ms01–08 appear; ms09 and **486 E0 cases** remain outside scope.
- Native limits are 600 seconds for 5,556 items and 300 seconds for 24; checker limit is 1200.

Those are manifest/source checks. The referenced historical receipts, skeletons, lists and binaries are absent from this snapshot, so their actual contents and regenerated-formula equality have **not** been independently verified here.

The reservation arithmetic is correct:

`(6351 + 5580) × 393216 + 2 × 67108864 = 4,825,677,824 B`.

With the 268,435,456-byte margin and 10,000,000,000-byte cap, the census must report usage **≤4,905,886,720 B**. Shared exclusive claims and existing-record skipping prevent automatic retries within M2H. Each instance owns one token, but the source permits two M2H instances; the initial singleton and reservation for parent manual M1 attempts need explicit launch control.

Before native admission, require actual evidence under freshly reviewed source hashes and a **new immutable contract**:

- Corrected supervisor controls, including signals and wall/floor/RSS/uncertainty events during delayed reaping, with no trip qualifying clean.
- M2H-specific negative reader/binding controls: historical-only wrappers, wrong contract/pin/interval/list, missing split, mismatched formula, existing UNKNOWN, duplicate claims, and all refusal stages. SOURCE23’s harness exercises M6/M9 paths; it supplies no executed M2H-control receipt.
- A complete **5,580-item binding receipt** showing regenerated SHA/bytes equal the referenced historical values, followed by a fresh **post-binding/control census** and admission-gate evidence satisfying the reservation, floor, RSS, binary and TTL checks.
- One initial M2H pipeline, the other token reserved for parent manual M1 work, and timestamped evidence of 17:20 admission closure and owned native-group quiescence by 17:57. Representative direct and split results must traverse the actual measured publisher→reader→inventory path.

Imported scientific encoding and enumeration validity remains a separate assumption. **No PA19 theorem or M2 completeness theorem follows from this review.**