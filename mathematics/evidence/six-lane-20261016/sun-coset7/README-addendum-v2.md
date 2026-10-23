# sun-coset7 README addendum v2: Stage C infrastructure, written under the parent HOLD (nothing launched)

- **Freeze record:** host-clock time and sha256 values in `evidence/addendum-v2.sha256`.
- **Unchanged:** README.md, README-addendum-v1.md, rules-k7-v1.md, rules-k7-addendum-v1.md, FINITE-COVERAGE-k7-v1.md and CERT-FORMAT-k7-v1.md are not modified.
- **Status:** Stage C is on HOLD. The parent permitted writing these files but did not permit launching them.
  - The two math-1 process slots are reserved for the parent's separately authored Stage A and Stage B checkers.
  - No Stage C process has ever run.
  - All six residual classes stay OPEN.

## 1. Parent decisions recorded

**HOLD** (received between 13:49:17 and 13:53:48 PDT, bounds from adjacent host-clock outputs). Stage C was put on hold pending a written-rule addendum, which is now `rules-k7-addendum-v1.md` (fb2c306b…1066).

**Option (a)** (received between 14:00:41 and 14:04:43 PDT, same kind of bounds). A new engine v3 with:
- cooperative SIGTERM handling: a flag that tick() reads;
- a guard on ru_maxrss at 0.9 GiB;
- UNKNOWN plus the exact frontier on every stop;
- no guard that could silently lose the frontier;
- no signal ever sent to an unchecked bare PID.

**Admission order.** The new admission check must read the monitor file before taking its fresh clock reading. Refusal stays fail-closed.

**Launcher.** The launcher should supervise owned Popen handles and record identity and settlement. No hard timeouts and no SIGKILL.

## 2. NOT_STARTED files

These files were frozen but **never executed**. They are not scientific UNKNOWN results.

| file | sha256 | superseded by |
|---|---|---|
| `code/core7_engine_v2.py` (v1 + K62/K63 in AUTHORISED) | 7ebb0bab09fdfe99bf016dbf0340c08148a5a61c3aa0444fc6f6e10c90f640c0 | `core7_engine_v3.py`, per decision (a) |
| `evidence/engine-v1-to-v2.diff` | acedb4a7201d512c5de36585740699998b257db98523f908d46ee9b3f1ef2cc6 | — (record only) |
| `code/admission_v1.py` | f58861d8e0d90435fd2e71b92ace3561076dfb5c247525ad94a7ee0122ab2cbc | `admission_v2.py` (read order; fail-closed typing) |
| `code/stageC_launch_v1.sh` | 158c074df266573451feccc20cbcb678829da531276da1349fca3ca999772db1 | `stageC_launch_v2.py` (Popen supervision) |

Defects found in self-review before any launch:
- **admission_v1** read the clock before the monitor file. A sample written in between could make the age negative, giving a spurious FAIL. That failure mode is fail-closed.
- **stageC_launch_v1.sh** signalled a shell PID without re-checking its identity.
- **Engines v1 and v2** have no handler for SIGTERM or RSS, so an external stop would lose the frontier.

## 3. New frozen files (written 14:04–14:09 PDT, frozen 14:09:06 PDT)

| file | sha256 | exact diff |
|---|---|---|
| `code/core7_engine_v3.py` | a26e6c686c78ee25b47635c9bea84bae170ee8d74fe57d48c2c955138f8b23a7 | `evidence/engine-v2-to-v3.diff`, f6315f1f81df7a6cb119f336185747d48eb797fc186c0cb966a6869a12aab697 |
| `code/admission_v2.py` | e0b6768aec643d160d4fb392b5598f6ada8ed47e22ab9ae2e469d1e4af0b52c0 | `evidence/admission-v1-to-v2.diff`, 0d9baebdb9f376205b1641ce8166a0cd844becad99e1345366c84d0630e52a0f |
| `code/stageC_launch_v2.py` | 9955a8e05265a78ba834067006356c5fee56b06c388f566464ac89d0a7d2bb4f | new file; rewrites the bash v1 in Python |

### Engine v3 = v2 + cooperative guard + memory-light writer

The search logic is unchanged: no line of the T, K, VFC, P, RPLP, enumeration or canonical-form code differs from v2. The changes:

**G1. Guard.**
- SIGTERM sets `Guard.term`.
- `tick()` raises StopRun on any of four conditions:
  - the term flag is set;
  - the self-budget is exceeded;
  - free disk < 12.0e9;
  - peak RSS (ru_maxrss) ≥ 966,367,641 B (0.9 GiB).
- Disk and RSS are read every 20 s.
- Nothing raises outside `tick()`. v2's constructor-time forced check, which could raise before the `try`, was removed; the first `tick()` now performs that check.
- `tick()` runs at every tree node, at every q in RPLP and every 256 q in the VFC kill test, all inside the `try … except StopRun`.
- A SIGTERM that arrives while outputs are being written has no effect, so the write completes.

**G2. Frontier.**
- `stats.profile_in_progress` is set before each profile and cleared at completion.
- `profiles_done` counts completed profiles in the deterministic enumeration order.
- Counts for the profile in progress (nodes, leaves) are partial on an UNKNOWN stop.

**G3. Writer.**
- Certificate files are gzip-compressed incrementally, in memory, by a bounded compressor. There is no joined copy of the leaf text.
- If the 15 MiB limit is exceeded, only `survivors.json` and `run.json` are written, with the v1 note.
- The dual-key set is now {memoised LP keys with value ≥ 1}, in key-tuple order. This is the same set as v1/v2's:
  - the kill test evaluates and memoises every q of every signature it kills, and all of those values are ≥ 1;
  - every RPLP "R" certificate cites such a key.
- v2's per-signature re-enumeration of q-vectors is removed. Its cost would have grown with the number of killed signatures, outside the budget. A no-op loop that re-parsed every leaf line is also removed.
- The JSON object order and separators of `lp_duals` differ from v1; CERT-FORMAT-k7-v1 §4 fixes neither.

**G4. run.json fields.**
- `engine` is now "core7_engine_v3".
- New fields: `sigterm_received`, `rss_cap_bytes`, `peak_rss_bytes_last_check`, `peak_rss_bytes_at_write`.

**Unchanged.** The program-level AUTHORISED list is the same as v2's; every run still needs a parent GO.

### admission_v2

- The monitor file is read first; then the clock; then a fresh statvfs. The age is computed as now − t_last.
- Fail-closed additions: duplicate JSON keys, a non-string `t`, and a non-int or boolean `free` all FAIL.
- The rule thresholds are those of the parent's 13:47 rule, unchanged from v1.

### stageC_launch_v2

**Usage:** `python3 code/stageC_launch_v2.py ENGINE ENGINE_SHA256 BUDGET`. The universes are fixed to K62 and K63.

**Refusals before admission:**
- engine sha mismatch;
- budget outside (0, 3600];
- now after 17:29:00 PDT;
- now + budget + 600 s past 17:57:00 PDT;
- an existing output directory.

**Record directory.** `evidence/stageC-launch-v2-<stamp>/` is created exclusively. Every stdout and stderr file is opened before admission.

**Admission.** admission_v2 runs for K62 and then K63. Each must exit 0 **and** its receipt must read PASS. Otherwise the launcher writes a REFUSED summary and launches nothing; it never retries.

**Spawn.** The clock and statvfs are re-checked immediately before spawning. Each engine is started with Popen: an argument list, no shell, stdin=DEVNULL, close_fds, and TMPDIR inside the lane.

**Supervision.** Every 10 s, the launcher works only through the owned handles. While `poll()` returns None the child is unreaped, so its PID cannot be recycled. For each child it:
- reads `ps -ww -o ppid=,rss=,command= -p PID`;
- verifies that the ppid is the launcher and that the exact engine argv appears.

It sends **one** SIGTERM through `Popen.send_signal`, which re-polls first, in either of these cases:
- a verified RSS ≥ 1 GiB;
- 3 consecutive unverifiable samples.

A SIGTERM received by the launcher is forwarded once in the same way. There is no escalation and never a SIGKILL. A note is logged if a child is still unsettled 300 s after its SIGTERM.

**Settlement.** For each child the launcher records the return code, the time and the fields from the engine's run.json (status, stop_reason, profiles_done, profile_in_progress, survivor_count, sha256). Records go to `summary.json` (exclusive) and `supervise.jsonl`.

**Disclosed.** The launcher is a third, supervisory process. It does no computation and makes transient `ps` calls.

## 4. Planned command (NOT authorised; for the parent's review)

```
cd /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7 && TMPDIR=$PWD/tmp \
  /opt/homebrew/bin/python3 code/stageC_launch_v2.py code/core7_engine_v3.py \
  a26e6c686c78ee25b47635c9bea84bae170ee8d74fe57d48c2c955138f8b23a7 BUDGET
```

- **BUDGET** = min(3600, seconds from launch to 17:57:00 − 600).
- **Invocation:** the bash tool with async true and timeout 0.
- **Timing:** only after a parent GO, and only once neither parent checker holds a math-1 slot.
- **No smoke test.** The new guard and writer code has passed a syntax parse only; it has never been executed. A short exploratory guard check (for example, v3 on KII with a 20 s budget, expecting UNKNOWN with "self-budget" plus full outputs) needs its own GO, if the parent wants one.
