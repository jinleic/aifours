# sun-coset7 README addendum v3: sequential Stage C launcher, CERT-FORMAT overlay, and a smoke harness (all NOT_STARTED)

- **Freeze record:** host-clock time and sha256 values in `evidence/addendum-v3.sha256`.
- **Earlier files:** no earlier file is modified.
- **Status:** Stage C is on HOLD. The two math-1 execution slots are reserved for the parent's independent Stage A and Stage B checkers. No Stage C process and no smoke process has run. All six residual classes stay OPEN.

## 1. Parent rulings recorded

Both arrived after 14:11:03 and before 14:17:53 PDT. These bounds come from adjacent host-clock outputs.

**Process cap.**
- A launcher plus two engine workers is three lane processes. That breaks the 2-process cap of transition 44, even if the launcher is mostly idle.
- Any later Stage C permission must run K62 and K63 **sequentially**: one supervised child plus one launcher, with a fresh admission immediately before each child.
- So `code/stageC_launch_v2.py` (9955a8e0…bb4f) is **non-compliant by design**. It was never executed and is NOT_STARTED. My earlier message disclosed it as "a third supervisory process"; a disclosure does not cure the cap violation.

**Engine v3 delta.**
- Engine v3 (a26e6c68…23a7) changed more than the guard. The changes also cover:
  - output buffering: a bounded in-memory gzip, with no joined copy of the leaf text;
  - the dual-key selection: memoised keys with value ≥ 1, replacing v1/v2's per-signature re-enumeration of q-vectors at write time;
  - removal of a no-op loop that re-parsed every leaf line.
- These remain explicit parts of its delta (`evidence/engine-v2-to-v3.diff`, f6315f1f…a697; README-addendum-v2 §3 G3). Engine v3 is **not** literally a guard patch.

**Before any Stage C GO.** The parent will:
- read the frozen sources and diffs;
- require a focused smoke of the stop paths and of small outputs. A syntax parse is not behaviour verification;
- check the process and admission conditions.

**Resource notice, relayed by the parent and not observed by me.**
- The parent monitor recorded free 11.985e9 at 14:07:50, below the frozen 12e9 floor, then 14.99e9 at 14:11:51. No causal writer has been established.
- From the end of Stage B (13:45:02) to this freeze, this lane started no engine or other computational process. It ran only short file operations: cp, chmod, shasum, diff, date, syntax parses and file writes.
- Every new launch still needs a fresh exact free/growth admission. Jobs of 60 min or more also need the 300 s stability rule. The in-flight floor guards stay mandatory.

## 2. New frozen files (NOT_STARTED)

| file | role | sha256 |
|---|---|---|
| `CERT-FORMAT-k7-addendum-v1.md` | overlay on CERT-FORMAT-k7-v1 (see below) | in `evidence/addendum-v3.sha256` |
| `code/stageC_launch_v3.py` | sequential launcher | in `evidence/addendum-v3.sha256` |
| `evidence/launcher-v2-to-v3.diff` | exact diff, v2 → v3 (a near-total rewrite) | in `evidence/addendum-v3.sha256` |
| `code/smoke_v3_v1.py` | smoke harness, proposed to the parent | in `evidence/addendum-v3.sha256` |

**CERT-FORMAT-k7-addendum-v1** contains:
- the K62 and K63 universe rows that v1 §1 does not list;
- the v3 output deltas: new run.json fields, the frontier semantics, the dual-key selection mechanism with its key-set argument, the buffering, the gzip container, and the empty-leaf payload.

**stageC_launch_v3** behaves as follows.
- **Process count:** the launcher plus at most ONE other process at a time, either one admission check or one engine child. It spawns no ps or other helper while an engine runs.
- **Order:** K62 runs, then K63. Before each child it does three things:
  - checks the clock: now ≤ 17:29:00, and the effective budget = min(BUDGET, 17:57:00 − now − 600 s) must be ≥ 300 s;
  - runs a FRESH admission_v2, which includes the 300 s stability rule, with projected growth = 16 MiB × the number of children not yet run;
  - re-reads statvfs and the clock immediately before spawning.
- **Supervision:** through the owned Popen handle only, by `poll()` every 10 s. A SIGTERM the launcher receives is forwarded once through `send_signal`. There is no escalation and no SIGKILL.
- **Settlement:** it records the return code, the kernel's RUSAGE_CHILDREN peak RSS (checked against 1 GiB after the fact), and the fields of the engine's run.json.
- **The sequence stops** on any of:
  - a refusal;
  - a non-zero return code;
  - a missing run.json;
  - a post-hoc RSS ≥ 1 GiB;
  - a SIGTERM.
- **RSS enforcement during a run** is the engine's cooperative 0.9 GiB guard, checked every 20 s, together with its 12.0e9 disk floor.

**smoke_v3_v1** is a sanity control, never gate evidence. It also uses one child at a time, a fresh statvfs ≥ 12.2e9 + 16 MiB before each child, and a refusal after 17:29. Four cases:

| case | run | expected outcome |
|---|---|---|
| S1 | KII, 20 s budget | UNKNOWN by self-budget, with the frontier and all files |
| S2 | KII, 600 s budget | one handle SIGTERM at 15 s gives UNKNOWN with reason "SIGTERM received (cooperative stop)" and sigterm_received true |
| S3 | MSP45, complete | stats, survivors, vfc_killed, leaf lines and the parsed lp_duals object equal the frozen Stage A v1 outputs |
| S4 | X1, complete | the same comparisons as S3 |

S3 and S4 check empirically that v3's search and writer changes leave the certificate content unchanged on those universes, including the dual-key-set equality argued in writing.

## 3. Cumulative NOT_STARTED list (never executed; not scientific UNKNOWN results)

| file | sha256 |
|---|---|
| engine v2 | 7ebb0bab09fdfe99bf016dbf0340c08148a5a61c3aa0444fc6f6e10c90f640c0 |
| admission_v1 | f58861d8e0d90435fd2e71b92ace3561076dfb5c247525ad94a7ee0122ab2cbc |
| stageC_launch_v1.sh | 158c074df266573451feccc20cbcb678829da531276da1349fca3ca999772db1 |
| stageC_launch_v2.py | 9955a8e05265a78ba834067006356c5fee56b06c388f566464ac89d0a7d2bb4f |

Also never executed so far:

| file | sha256 |
|---|---|
| engine v3 | a26e6c686c78ee25b47635c9bea84bae170ee8d74fe57d48c2c955138f8b23a7 |
| admission_v2 | e0b6768aec643d160d4fb392b5598f6ada8ed47e22ab9ae2e469d1e4af0b52c0 |
| stageC_launch_v3 | this freeze |
| smoke_v3_v1 | this freeze |

## 4. Proposed order, for the parent to decide; nothing here is authorised

1. Once the checkers release the slots and the parent gives a GO, run the smoke:
   `TMPDIR=$LANE/tmp /opt/homebrew/bin/python3 code/smoke_v3_v1.py a26e6c686c78ee25b47635c9bea84bae170ee8d74fe57d48c2c955138f8b23a7`
   This uses one child at a time and takes about 1 minute in total. [INFERENCE] The estimate comes from the Stage A run times (X1 1.2 s, MSP45 0.1 s) plus the 20 s and roughly 15–20 s KII cases.
2. Report the smoke once.
3. Only after a separate Stage C GO, run:
   `TMPDIR=$LANE/tmp /opt/homebrew/bin/python3 code/stageC_launch_v3.py code/core7_engine_v3.py a26e6c68… BUDGET`
   with BUDGET ≤ 3600 for each child, run sequentially.
