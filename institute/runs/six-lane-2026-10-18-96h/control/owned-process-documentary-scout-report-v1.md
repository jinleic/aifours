# Scout original narrative — CFR/aggregate count superseded

The following full original135-line narrative is preserved verbatim. Its CFR13/aggregate916counts are WRONG: complete returnedpatharraysandparentrecountestablishCFR14/aggregate917. Thisdoesnotchangethehistoricalidentity/returncodestatusqualifications. See owned-process-documentary-pathsets-scout-v1.json and owned-process-reconciliation-20261022-0233-v1.json.

## Summary

**Do not close v15 M4 yet.** The documentary launch/receipt census is concrete, and historical settlement evidence is substantially broader than the observer receipt. However, **the required fresh host-process census was not executable with this scout’s tools**: the available devices expose file/search tools and Gmail/Slack MCP, not shell/process inspection. `proc://` supplies harness-job status, **not** an OS PID/start/cwd/argv census. Live-owned process count therefore remains **UNKNOWN**, not zero.

No files changed, signals sent, programs/tests run, or agents launched.

### Boundaries

Paths below use:

- `R = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`
- `M = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h`
- `P = /Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h`
- `I = /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h`

The enumerated review set ends with `sixlane-report-v15-final-codex-v1`: launch **01:52:16**, terminal receipt **02:04:56 PT**. Continuation/ownership context includes checkpoint 215, recorded **02:15:22 PT**. These documentary timestamps are **not a fresh OS-snapshot timestamp**. Future parent launches are excluded.

## Report

### 1. Exact documentary census

Broad capped globs were split into complete, uncapped-result partitions. **Counts below count records, not unique processes**: some records are prelaunch declarations, batches, or nested-child records.

| Pathset | Launch records | Terminal coverage |
|---|---:|---|
| `R/control/active-launch-registry-v1.jsonl` | **102 nonblank events** | Historical state journal, not a comprehensive process inventory; last event is Oct 19 11:46:07 |
| `R/review/[a-n]*launch.json` | **54** | 54 same-stem receipts |
| `R/review/o*launch.json` | **137** | 137 same-stem receipts |
| `R/review/[p-r]*launch.json` | **74** | 74 same-stem receipts |
| `R/review/[s-z]*launch.json` | **189** | 189 same-stem receipts |
| Nested CLI review packets under `R/review/*/` | **62** | 62 same-stem receipts |
| Parent computation/control launches under `R/review/` | **64** | 64 same-stem receipts, finite recorded return codes |
| `M/sun-coset7/evidence/*/launch.json` | **28** | 27 JSON run records; one text run record with explicitly **UNKNOWN probe exit status** |
| `M/olson/evidence/probe-v1/LAUNCH-RECORD-pre-v1.json` | **1** | Written receipt; identity-recording qualification retained |
| `P/rqls10/evidence/*.launch.json` | **35** | 10 supervisor receipts; remaining coverage is written/grouped receipts and checkpoints; one declaration explicitly never launched |
| MOQLS native `P/moqls8/evidence/{ga-replay-v6g,gb-staged-v6e,gb-staged-v7}/launch/LAUNCH-*.json` | **22** = 3+12+7 | 22 matching nonempty `SETTLED-*` records; 22 empty fallback files are **not additional receipts** |
| MOQLS lane CLI reviews, `P/moqls8/review/*/*.launch.json` | **14** | 14 receipts, all rc 0 |
| PA19 `I/pa19/evidence/pilot-v1/*/launch-record.json` | **10** | 10 summaries: rc **60, 20, then eight 0s** |
| PA19 pilot `*/children/*.launch.json` | **112** | 112 matching `*.settle.json`; all 112 children recorded settled |
| PA19 preflight `evidence/probes/preflight-wave2a-d2-v1.launch.json` | **1** | Identity receipt plus checkpoint 026 terminal observation |
| PA19 lane CLI reviews, `review/codex-pilot-*/launch.json` | **8** | 8 receipts, all rc 0 |
| CFR21 `I/cfr21/evidence/**/launch.json` | **13** | 12 probe receipts plus one controls-batch receipt containing **17 child records**, `all_settled:true` |
| MOLS39 `I/mols39/evidence/**/launch.json` | **92** | 92 receipts: **51** `settled:true` probes and **41** supervisor `settlement:"SETTLED"` records |

Thus the explicit program **launch/prelaunch JSON pathsets contain 916 records**: **580** under `R/review/` and **336** across the domain trees. Observer v2/v3 add **two separately counted launch JSONs**; observer v1 ownership is established by its admission/stop records. `R/launch-v1.json` is a **six-agent ownership declaration**, not six OS launch receipts.

The 62 nested CLI records partition as:

- `beta-controls-v2-packets-v1`: 4
- `beta-controls-v4-packets-v1`: 5
- `beta-supervisor19-adapter-v2-packets-v1`: 4
- `beta-supervisor19-v3-packets-v1`: 4
- `rqls10-v9-v19-packets-v1`: 19
- `rqls10-io-guard-v10-packets-v1`: 8
- `rqls10-base-postcheck-packets-v1`: 3
- `rqls10-native-guard-v10-packets-v1`: 15

The 64 parent computation records comprise **25 PA19 replay/control invocations, three other finite controls, and 36 Sun invocations**.

### 2. Reviews: ended is not accepted

Across parent and lane-local review pathsets, **538 CLI launches have 538 terminal receipts**:

- **520 rc 0**
- **9 rc 1 / NO_VERDICT**
- **9 rc 143 / SELF_BUDGET_SIGTERM_NO_VERDICT**
- **No `returncode:null` or `unsettled_pid` marker found in these review receipts.**

The nine rc-1 stems, relative to `R/review/`, are:

- `olson-DELTA3-codex-v2-complete`
- `olson-RPdelta-claude-v1`
- `sixlane-report-v12-shard-olsonfoundations-claude-v4`
- `sixlane-report-v12-shard-olsonterminal-claude-v2`
- `sixlane-report-v12-single-context-codex-v4`
- `sun7-K62-M13-claude-v1`
- `sun7-K7-R2-claude-v1`
- `sun7-K7-R3a-claude-v1`
- `sun7-K7-R3b-claude-v1`

The nine rc-143 stems are:

- `olson-REFLHI-arcs-v4-claude-v1`
- `olson-REFLHI-v5-corollaries-claude-v1`
- `sun7-K7-A2-unit3-claude-v1`
- `sun7-K7-R3{a,b}-claude-v{2,3}` — four records
- `sun7-LEDGER-CLOSED-P1-claude-v1`
- `sun7-LEDGER-P1A-claude-v2`

Each stem has `.prompt.receipt.json`. These are **ended review attempts, not acceptance**. Likewise v15’s rc 0 records a returned review rejecting the report, not delivery approval. DELTA3’s required, unlaunched Claude gate is **an acceptance blocker, not an unsettled process**.

### 3. Historical native settlement is supported, with important qualifications

- **PA19:** All 10 pilot summaries record `all_children_settled:true`; their child arrays total **112**, with no unsettled/null-return entries. Run 001 failed before spawning a native child; run 002 ended after four controls. The registry’s lingering `LAUNCHING` for run 008 is a **journal-closure gap**, not evidence it remains live: `run-008/summary.json:1-5,141-143` records all 14 children settled and rc 0 at **04:30:18 Oct 19**.
- **PA19 receipt-only probes:** There are **13 identity receipts**, only one with a separate launch JSON. They must not disappear from the ownership set. Their PIDs are **39805, 48854, 49511, 50289, 57507, 57516, 71187, 72209, 76093, 86281, 86890, 87132, 2738**. Terminal observations are in PA19 checkpoints **006, 009–010, 012, 015, 018, 021, 026**; some are collective settlement statements rather than raw per-process waits. Checkpoint 006 also records sleep child **39810** reaped.
- **RQLS10 supervisors:** All **10** JSON supervisor receipts record finite returns, empty `group_members_after`, and `settlement:"SETTLED"`. The v2 smoke rc 3 is settled, scientifically nonqualifying.
- **MOLS39:** All **41** supervisor receipts record settlement; the other **51** probe receipts record settled. References to old inputs/binaries do not make these old-run processes: the launches belong to this new evidence tree.
- **MOQLS:** The 22 driver settlement records alone establish driver reaping, **not descendant clearance**. The item receipts and parent audits supply the latter. There are **38 primary pipeline receipts**, plus **31 commit** and **28 complete** companions.

**Two misleading MOQLS false flags are already resolved by actual historical evidence:** GBv7 B2.M2 and B3.M2 have `children_reaped:false` because their checkers were **never spawned**, not because a checker survived. Their solver reaps, ended started threads, empty live-child/helper sets and executed parent censuses are recorded in:

- `R/review/moqls8-gb-gbs7-P1-B2.M2-UNKNOWN-parent-audit-v1.json:146-179`
- `R/review/moqls8-gb-gbs7-P1-B3.M2-UNKNOWN-parent-audit-v1.json:118-178`

Their scientific outcome remains **UNKNOWN**. Do not convert these flags into either a survivor allegation or scientific acceptance.

### 4. Missing/unbound coverage that must remain explicit

| Gap | Evidence and disposition | Exact parent action |
|---|---|---|
| **Fresh host census absent** | No OS PID/start/cwd/argv observations were possible here. **Live-owned count UNKNOWN.** | Execute one fresh host snapshot, identity-bind candidates and descendants, then create the immutable audit artifact. |
| **Parent CLI wrapper/descendant identities** | The four known runners record the CLI child PID/PGID/cwd/argv hash and poll return code, but not wrapper PID/native-start identity or a final descendant census. Their receipt coverage is not full process-tree settlement. | Include review Python wrappers, CLI descendants, shared evaluator parents and timers separately in the host snapshot. Do not infer them absent from CLI return codes. |
| **Sun first probe: permanently missing identity/status** | `M/sun-coset7/evidence/probe-lfc-row-v1-r1/postrun-v1.json:28-29`: PID/PGID/lstart not recorded; printed rc 0 was **wait-all**, not probe status. Historical postrun absence/completion evidence exists, but probe exit is explicitly **UNKNOWN**. | Preserve the qualification verbatim; do not “repair” it by rerunning or inventing an identity. |
| **Olson first probe: weak launch binding** | `M/olson/evidence/probe-v1/RECEIPT-run1-v1.md:7-13`: empty `$!`, later observed PID **16900**, PPID **61118**, PGID **16900**; receipt reports exit/completion. | Preserve the recording defect and distinguish the later identity observation from a proper launch-time record. |
| **RQLS helper batches not individually identity-bound in their cited receipts** | `exact-checker-v2-controls.receipt.md:8-10` reports five exited processes without per-child PIDs. `gate-selftest-v2.receipt.md:11-15` binds parent **25352**; its summary has **13 case exits and no PID records**. The v9 receipt separately records analysis PID **60353**, rc 0, at line 24. | Include these receipt-only launches/helper classes in the artifact; mark absent child identity bindings as historical coverage gaps, not current survivors. |
| **Cadence timers lack a complete ownership/terminal ledger** | Queue/checkpoint fields reference `bg…` job IDs, not PID/start/cwd/hash identities. Checkpoints 209 and 212 mark **bg3289** and **bg3294** completed; this does not settle every earlier timer. | Recover timer launch/return evidence from parent tool history and reconcile it against the single host snapshot. Cardinality of identity-bound OS timers is currently **UNKNOWN**. |

Registry aliases/corrections must also be joined by actual launch paths, not item-string equality: GB controls’ spacing typo; combined PA19 pilot/replay closures; run-008 replay name changes; split WH10/fixed-B entries; and registry rows **96–97**, which describe **one** launch/PID with an `abs_end` correction.

### 5. Observer and inherited-service coverage

- Observer v1 **87950** and v2 **89823** have identity-hash/cwd stop requests and settled receipts; harness services report **exit 0**.
- Observer v3 **90709** has historical native start **Oct 18 23:12:04**, cwd `R`, source SHA `fe311f28…f04196`, one owned SIGTERM, `observer_end` **Oct 22 01:50:18**, and supervisor **exit 0**.
- Preserve `R/control/observer-v3-chronology-and-closeout-status-erratum-v1.json`: the unsupported parent time labels are withdrawn; the actual clean exit remains valid. This establishes **observer settlement only**.
- The two `six-lane-*-recovery-0930` harness services report **exit 143** and refer to the **previous run**, predating this authorization. They are inherited records, not new 96h-owned launches.

The single `proc://` listing showed the new Olson written-worker task running and these observer/services terminal. It supplied **no OS identities**, so it cannot establish zero live native jobs, wrappers, descendants or timers.

## Architecture / next parent action

Ownership is distributed across **the incomplete global journal, same-stem CLI launch/receipt pairs, lane launch/settlement records, and written receipt-only checkpoints**. Neither the observer receipt nor the global registry is a complete authority by itself.

**Next action:** take one clocked, read-only host census; compare PID **plus native start, cwd and correctly normalized argv hash**, follow owned descendants, and classify wrappers/timers/observer separately. Reused PIDs and unrelated sessions must remain excluded unless identity matches. Then freeze the complete pathset and this historical qualification chain into the parent-owned immutable audit artifact.

**Supported conclusion now:** extensive recorded historical endedness, **not blanket all-owned settlement**.
