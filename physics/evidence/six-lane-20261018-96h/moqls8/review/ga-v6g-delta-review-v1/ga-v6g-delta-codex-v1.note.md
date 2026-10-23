VERDICT: HOLD

| Finding | Status | File:line evidence |
|---|---|---|
| **03a-1 — settlement, fallback, announcements and preserved status** | **PARTIAL** | Four outputs, including a separate fallback file, are reserved before spawn (`snapshot/10-launch_ga_v6i.py:152–164`). Primary settlement writing, minimal fallback writing and announcement exceptions are independently caught (`:255–270`). `Popen.wait()` preserves the cached driver status, which supplies settlement fields and the explicit exit decision (`:226–244,277–280`). A failed launch announcement after publication records an error without signalling the driver (`:212–222`). However, stdout blocking and shutdown flushing still defeat the overall settlement/status guarantee; NEW findings 1–2. |
| **03b-1 applied to GA — published registration gates natives** | **REPAIRED** | The launcher passes `MOQLS8_LAUNCH_RECORD` (`snapshot/10-launch_ga_v6i.py:153,160`). Run startup validates its location/name (`snapshot/00-replay_v6g.py:2424–2430`). `registration_problem()` requires a nonempty regular file, parseable JSON, this driver's PID and the identical absolute end (`:1430–1444`). `spawn_block()` calls it before both native spawn sites (`:1427,1649–1659,1681–1690`). An empty reservation under a suspended launcher therefore cannot admit either native. |

1. **NEW — MAJOR: a blocked launch announcement prevents reaping and settlement indefinitely.**

   The synchronous `print(..., flush=True)` occurs after registration publication but before `child.wait()` and all settlement writing. Its exception handler provides no protection when stdout is a full blocking pipe whose reader remains open without draining. The driver can finish independently while the launcher remains blocked; the driver is then unreaped and both reserved settlement files remain empty.

   Managed signals merely append to `SIGNALS_SEEN`; they do not interrupt this operation with an exception. Evidence: [snapshot/10-launch_ga_v6i.py:218–229](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/review/ga-v6g-delta-review-v1/snapshot/10-launch_ga_v6i.py:218), `:62–63,170–171,255–268`.

   This concerns the launcher's unrestricted stdout pipe. The documented rescue for a driver blocked on regular-file output does not settle this launcher. Announcements need bounded or nonblocking handling that cannot obstruct reaping or settlement publication. Unconditional settlement is **NOT ESTABLISHED**.

2. **NEW — MINOR: catching `BrokenPipeError` does not guarantee process exit 4.**

   Both announcement handlers retain the failed stdout stream. With buffered CPython 3.9 stdout, a caught flush failure can leave pending output; interpreter shutdown can retry that flush and replace `SystemExit(4)` with exit status **120**. The explicit decision is reached, but its resulting process status is not protected.

   Evidence: [snapshot/10-launch_ga_v6i.py:218–222](/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/review/ga-v6g-delta-review-v1/snapshot/10-launch_ga_v6i.py:218), `:267–280,283–284`. No failed-stream replacement or other shutdown-flush handling appears. The driver status remains cached and can survive in settlement; the promised launcher exit 4 is **NOT ESTABLISHED** for this path.

Verified:

- **Integrity and review method:** all **16 manifest-listed files** match their SHA256 pins. Only static reads, comparisons and hashing were used; no source execution, writes or delegation.
- **Unchanged acceptance machinery:** nine matching region-hash pairs independently confirm byte-identical ACCEPTANCE (`snapshot/00-replay_v6g.py:349–371`), five controls (`:305–327`), helper/scanner supervision (`:462–812`), input regeneration (`:886–1068`), strengthened binding/composition core (`:1084–1142`), measured writers/relay (`:1186–1409`), CR-only parsing (`:1548–1564`), evaluator (`:1941–2073`) and control admission (`:2142–2176`). Binding additionally retains the reviewed provenance-pin additions.
- **No additional false-PASS route identified:** regenerated formula bytes must match PRE-EXEC and binding identities (`:2473–2476,2518–2537`). PASS still requires both complete measured CNF feeds, FIFO EOF, nonzero and equal relay read/delivered counts and hashes, equal checker-consumed bytes, successful native results and clean supervision (`:1946–2007`).
- **Launcher admission remains:** real desk directories, regular PRE-EXEC/GO placement, driver/launcher/PRE-EXEC hashes, ordered items, tightening hash, reservation, canonical versioned STOP registry with schema/hash, and nonempty dispositions are checked (`snapshot/10-launch_ga_v6i.py:82–89,106–150`). Four outputs are exclusively reserved before spawn (`:152–175`).
- **Ownership remains:** the driver starts a new session; the launcher's sole explicit signalling operation is its single fail-closed SIGTERM to the owned, unreaped driver (`:173–175,213–217`).
- **Recorded and enforced ends match:** one quantized value supplies environment and launch record (`:148,159,194`). Driver validation makes its `min()` retain that value (`snapshot/00-replay_v6g.py:2416–2423`); registration equality, spawn admission, in-flight enforcement and terminal late-reap veto use it (`:1425,1440,1796–1803,1899–1903`). Grace exhaustion records survivors and stops further work (`:1810–1840,2597–2599`). No additional unreported-survivor path was identified.