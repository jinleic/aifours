# sun-coset7 README addendum v4: terminal-SIGTERM coercion, bounded settlement, frontier scope (all NOT_STARTED)

- **Freeze record:** host-clock time and sha256 values in `evidence/addendum-v4.sha256`.
- **Earlier files:** none is modified.
- **Status:** Stage C is on HOLD and the parent's checkers own the two math-1 execution slots. No Stage C process, no smoke process and no probe process has run. All six residual classes stay OPEN.

## 1. Parent review findings addressed

The findings arrived after 14:18:31 and before 14:22:28 PDT; these bounds come from adjacent host-clock outputs. The parent read the engine-v2→v3 diff, `stageC_launch_v3.py` and `smoke_v3_v1.py`.

### Finding 1: terminal SIGTERM

**Problem in v3.** A SIGTERM that arrives after the last search tick, or during `write_outputs`, could leave the published status COMPLETE while `sigterm_received` is true.

**Engine v4 fix.**
- Publication now runs with SIGTERM blocked. This applies to `write_outputs` and to the CONTROLS publication.
- At the status decision, a SIGTERM that is latched (`Guard.term`) or pending (`sigpending`) coerces the status to UNKNOWN.
  - An earlier stop reason is preserved.
  - Otherwise the reason becomes "SIGTERM received after the search loop (status coerced to UNKNOWN at publication)".
  - `status_before_publication` is recorded.
- A SIGTERM that becomes pending only after the decision is recorded in `post_publication_sigterm.json`, and the process exits with status 3.

**Launcher v4 classification.** The launcher classifies each settled child fail-closed:

| outcome | conditions |
|---|---|
| COMPLETE | rc 0; status COMPLETE; stop_reason null; sigterm_received false; profile_in_progress null; profiles_done = profiles_total; note null; engine sha matches; no marker file |
| UNKNOWN(self-budget) | as for COMPLETE, except status UNKNOWN with a "self-budget" reason |
| UNKNOWN(stopped) | any other well-formed outcome |
| INVALID | any required field missing or ill-typed, or no readable run.json |

The next child is admitted only after COMPLETE or UNKNOWN(self-budget). A budget stop was an anticipated outcome under the original Stage C GO, and K63 does not depend on K62. Every other outcome stops the sequence.

### Finding 2: bounded settlement

In launcher v4 and smoke v2, after the one owned SIGTERM:
- the wait is at most 120 s, polling every 1 s;
- if the child is still alive at the end, the step is recorded UNKNOWN/UNSETTLED with the live owned identity (pid, argv, spawn time, signal time);
- the sequence then stops, with no further case or launch;
- the child is left running for parent intervention, with no SIGKILL and no further signal.

### Finding 3: evidence scope

`profiles_done` together with `profile_in_progress` is a **completed-profile frontier**:
- the profiles before `profile_in_progress`, in the deterministic enumeration order, are complete;
- the α-prefix reached inside `profile_in_progress` is not recorded;
- that profile is never counted complete.

This wording now appears in the docstrings of engine v4, launcher v4 and smoke v2. It supersedes the phrase "exact frontier" used in README-addendum-v2 and in my messages.

### Smoke coverage of terminal coercion

`code/terminal_probe_v1.py` is a deterministic, isolated, one-process probe with no sleeps. It loads engine v4 as a module, runs MSP45 to COMPLETE through the engine's own `run_universe`, and sends one SIGTERM to itself at a fixed point:
- **T1:** after the search returned and before publication. Its precondition, that `Guard.term` is latched, is recorded.
- **T2:** inside publication, after SIGTERM is blocked and before the decision. This is the first call of the engine's `_gz_bounded`, which the probe wraps.
- **T3:** after the decision, while the run.json fields are built. This is the first call of the engine's `peak_rss_bytes`, which the probe wraps.

Expected results: T1 and T2 publish UNKNOWN through coercion. T3 publishes COMPLETE and writes the post-publication marker.

`smoke_v4_v2.py` covers both the search-loop stops and terminal coercion:
- S1 (budget stop) and S2 (handle SIGTERM during the search, with bounded settlement);
- S3 and S4 (COMPLETE runs that must equal the frozen Stage A v1 outputs);
- T1–T3, each run as its own child.

There is always one child at a time, and a fresh statvfs reading of at least 12.2e9 + 16 MiB is required before each child.

### Scope of the changes

- No unrelated changes were made.
- The engine v3→v4 diff touches only:
  - the docstring;
  - the SIGTERM block, the decision and the marker at publication;
  - the CONTROLS publication, under the same rule;
  - main's printed status and exit status 3.
- Search code, writer buffering and dual-key selection are unchanged from v3. The v3 writer and dual-selection changes remain part of the cumulative v2→v4 delta (`evidence/engine-v2-to-v3.diff` plus `evidence/engine-v3-to-v4.diff`). The engine is not a guard-only patch.

## 2. New frozen files (NOT_STARTED)

All sha256 values are in `evidence/addendum-v4.sha256`.

| file | role |
|---|---|
| `code/core7_engine_v4.py` | engine v4; exact diff `evidence/engine-v3-to-v4.diff` |
| `code/stageC_launch_v4.py` | sequential launcher v4; exact diff `evidence/launcher-v3-to-v4.diff` |
| `code/smoke_v4_v2.py` | smoke harness v2; exact diff from smoke_v3_v1 in `evidence/smoke-v3v1-to-v4v2.diff` |
| `code/terminal_probe_v1.py` | terminal-SIGTERM probe; new file |

**Superseded, never executed, NOT_STARTED:**
- engine v3 (a26e6c68…23a7) as a Stage C engine;
- `stageC_launch_v3.py` (4f00be28…d8dc);
- `smoke_v3_v1.py` (36ae890f…a386).

The earlier NOT_STARTED files remain listed in README-addendum-v3 §3.

**Verification status.** All four new files have passed a syntax parse only. No behaviour has been verified.

## 3. Proposed order (nothing here is authorised)

1. Once the checkers release the slots and the parent gives a GO for the smoke only:
   `TMPDIR=$LANE/tmp /opt/homebrew/bin/python3 code/smoke_v4_v2.py <engine v4 sha256>`
2. Report the smoke once.
3. Only after a separate Stage C GO:
   `TMPDIR=$LANE/tmp /opt/homebrew/bin/python3 code/stageC_launch_v4.py code/core7_engine_v4.py <engine v4 sha256> BUDGET`

**Disk.** The lane's statvfs read 13,844,172,800 B free at 14:20:41 PDT. Any admission must re-check free space fresh; this reading is only context.
